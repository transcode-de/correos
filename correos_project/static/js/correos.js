function stripHTML(html) {
  return html.replace(/<\/?([a-z][a-z0-9]*)\b[^>]*>?/gi, '');
}

var emptyEmail = {
  header: {},
  body: ''
};

function MainViewModel() {
  self = this;

  self.domains = ko.observableArray([]);
  self.users = ko.observableArray([]);
  self.emails = ko.observableArray([]);

  self.domain = ko.observable();
  self.user = ko.observable();
  self.email = ko.observable(emptyEmail);

  setInterval(function() {
    self.fetchUsers();
    self.fetchEmails({prepend: true});
  }, 2000);

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

  self.fetchDomains = function() {
    $.get('/api/domain/', self.domains);
  };
  self.fetchDomains();
  self.domain.subscribe(function() {
    self.fetchUsers();
    self.user(null);
    self.emails([]);
  });

  self.fetchUsers = function() {
    $.get('/api/user/?domain__name=' + self.domain(), self.users);
  };
  self.activateUser = function(user) {
    self.email(emptyEmail);
    self.user(user.email);
  };
  self.user.subscribe(self.fetchEmails);

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

