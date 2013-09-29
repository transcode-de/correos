var emtpyEmail = {
  header: {},
  body: ''
}

function MainViewModel() {
  self = this;

  self.domains = ko.observableArray([]);
  self.users = ko.observableArray([]);
  self.emails = ko.observableArray([]);

  self.domain = ko.observable();
  self.user = ko.observable();
  self.email = ko.observable(emtpyEmail);

  setInterval(function() {
    self.fetchUsers();
    self.fetchEmails();
  }, 5000);

  self.fetchEmails = function() {
    if (self.user()) {
      $.get('/api/email/?recipient__email=' + self.user(), function(data) {
        self.emails(_.map(data.results, function(email) {
          email.header = $.parseJSON(email.header);
          return email;
        }));
      });
    } else {
      self.emails([]);
    }
  };

  self.fetchDomains = function() {
    $.get('/api/domain/', self.domains);
  };
  self.fetchDomains();

  self.fetchUsers = function() {
    $.get('/api/user/?domain__name=' + self.domain(), self.users);
  };
  self.domain.subscribe(self.fetchUsers);

  self.activateUser = function(user) {
    self.email(emtpyEmail);
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
	$('.postbox-select, .email-select, .email-detail').niceScroll();
	$('#reload-domains').tooltip({'placement': 'bottom'});
	email_display_format();
});
