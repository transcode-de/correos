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
  self.email = ko.observable();

  setInterval(function() {
    //$.get('/api/domain/', function(domains) {
      //self.domains(domains);
      self.domains([
        { name: 'example.net' },
        { name: 'example.org' },
        { name: 'example.foo' }
      ]);
    //});
    //$.get('/api/user/?domain=' + self.domain.name, function(users) {
      //self.users(users);
      self.users([
        { name: 'cindy@example.com', countMails: 10 },
        { name: 'bob@example.com', countMails: 15 },
      ]);
    //});
    self.fetchEmails();
  }, 1000);

  self.fetchEmails = function() {
    if (self.user()) {
      $.get('/api/email/?recipient=' + self.user(), self.emails);
    } else {
      $.get('/api/email/', self.emails);
    }
  }

  self.activate = function(user) {
    self.user(user.name);
  }
}
ko.applyBindings(new MainViewModel());

$(function() {
	$('.postbox-select, .email-select, .email-detail').niceScroll();
	$('#reload-domains').tooltip({'placement': 'bottom'});
});
