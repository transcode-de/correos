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

  self.domain = ko.observable({ name: 'None' });
  self.domains = ko.observableArray([]);

  setInterval(function() {
    //$.get('/api/domain/', function(domains) {
      self.domains([
        { name: 'example.net' },
        { name: 'example.org' },
        { name: 'example.foo' }
      ]);
    //});
  }, 1000);
}

ko.applyBindings(new MainViewModel());

$(function() {
	$('.postbox-select, .email-select, .email-detail').niceScroll();
	$('#reload-domains').tooltip({'placement': 'bottom'});
});
