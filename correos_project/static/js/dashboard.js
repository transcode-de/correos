function MainViewModel() {
  self = this;
  self.emails = ko.observableArray([]);
  self.fetchEmails = function() {
    $.get('/api/email/', function(data) {
        self.emails(_.map(data, function(email) {
          email.header = $.parseJSON(email.header);
          return email;
        }));
      });
  };
  self.fetchEmails();
  console.log(self.emails());
}

ko.applyBindings(new MainViewModel());
