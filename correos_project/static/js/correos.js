function Email(data) {
  this.header = {};
  this.raw = '';
  this.sender = '';
  this.recipient = '';
  this.domain = '';
  this.date = new Date();
  this.body = '';
  this.subject = '';
}

function MainViewModel() {
  self = this;

  self.domains = ko.observableArray([]);
  self.users = ko.observableArray([]);
  self.emails = ko.observableArray([]);

  self.domain = ko.observable();
  self.user = ko.observable();
  self.email = ko.observable({});

  setInterval(function() {
    //$.get('/api/user/?domain=' + self.domain.name, users);
    self.users([
      { name: 'cindy@example.com', countMails: 10 },
      { name: 'bob@example.com', countMails: 15 },
    ]);
    self.fetchEmails();
  }, 1000);

  self.fetchEmails = function() {
    if (self.user()) {
      $.get('/api/email/?recipient=' + self.user(), self.emails);
    } else {
      $.get('/api/email/', self.emails);
    }
  };

  self.fetchDomains = function() {
    //$.get('/api/domain/', domains);
    self.domains([
      { name: 'example.net' },
      { name: 'example.org' },
      { name: 'example.foo' }
    ]);
  };
  self.fetchDomains();

  self.activateUser = function(user) {
    self.email({});
    self.user(user.name);
  };
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
