//util function to strip HTML form strings
function stripHTML(html) {
  return html.replace(/<\/?([a-z][a-z0-9]*)\b[^>]*>?/gi, '');
}

//placeholder mail if no mail is selected
var emptyEmail = {
  header: {},
  body: ''
};

//main view model
//TODO split to seperate view models for user/mail
function MainViewModel() {
  self = this;

  self.domains = ko.observableArray([]);
  self.users = ko.observableArray([]);
  self.emails = ko.observableArray([]);

  self.domain = ko.observable();
  self.user = ko.observable();
  self.email = ko.observable(emptyEmail);

  self.emailFilter = ko.observable('');

  //update poll
  setInterval(function() {
    self.fetchUsers();
    self.fetchEmails({prepend: true});
  }, 2000);

  //fetches mails of currently seleced user
  //if options.prepend is set, only the mails prior the last mail where
  //fetched.
  self.fetchEmails = function(options) {
    if (self.user()) {
      var existingEmails = self.emails();
      var params = {
        recipient__email: self.user(),
      };
      if (options.prepend && existingEmails[0]) {
        params.after = existingEmails[0].date;
      }
      $.get('/api/email', params , function(data) {
        var newEmails = _.map(data.results, function(email) {
          email.header = $.parseJSON(email.header);
          email.fuzzyDate = moment.utc(email.date).local().fromNow();
          email.formatedDate = moment.utc(email.date).local().format('YYYY-MM-DD\THH:mm:ss');
          email.preview = stripHTML(email.body);
          email.textAsHtml = '<p>' + email.body.replace(/\n{1,2}/, '</p><p>') + '</p>';
          return email;
        });
        if (newEmails.length) {
          if (options.prepend) {
            newEmails = newEmails.concat(existingEmails);
          }
          self.emails(newEmails);
        }
      });
    } else {
      self.emails([]);
    }
  };

  //fetches all domains
  self.fetchDomains = function() {
    $.get('/api/domain/', self.domains);
  };
  self.fetchDomains();
  self.domain.subscribe(function() {
    self.fetchUsers();
    self.user(null);
    self.emails([]);
    self.email(emptyEmail);
  });

  //fetches all users
  self.fetchUsers = function() {
    $.get('/api/user/?domain__name=' + self.domain(), self.users);
  };
  self.activateUser = function(user) {
    self.email(emptyEmail);
    self.user(user.email);
  };
  self.user.subscribe(self.fetchEmails);

  //property to filter the mails by input value
  self.filteredEmails = ko.computed(function() {
    var filter = self.emailFilter().toLowerCase();
    return ko.utils.arrayFilter(this.emails(), function(email) {
      if (!filter) {
        return true;
      }
      return _.some(['body', 'subject', 'sender'], function(key) {
        return email[key].toLowerCase().indexOf(filter) >= 0;
      });
    });
  }, self);

  //helper function to get raw version of currently seleced mail
  self.raw = ko.computed(function() {
    var email = self.email();
    if (email.header) {
      return _.reduce(email.header, function(result, value, key) {
        return result + key + ': ' + value + '\n';
      }, '') + '\n' + email.body;
    }
  });
}
ko.applyBindings(new MainViewModel());

function email_display_format() {
  $('.display_type_change').on('click', function(){
    $('.mail-format').hide();
    $($(this).find('input').data('target')).fadeIn();
  });
}

$(function() {
  $('#reload-domains').tooltip({'placement': 'bottom'});
  email_display_format();
});
