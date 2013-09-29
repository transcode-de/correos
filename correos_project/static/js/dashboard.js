function MainViewModel() {
  self = this;
  self.emails = ko.observableArray();
  self.next_url = ko.observable('/api/email/?page_size=7');
  self.previous_url = ko.observable();

  self.fetchEmails = function(url) {
    $.get(url, function(data) {
        console.log(data);
        self.next_url(data['next']);
        self.previous_url(data['previous']);
        self.emails(_.map(data['results'], function(email) {
          email.header = $.parseJSON(email.header);
          return email;
      }));
    });
  };

  self.fetchNextEmails = function() {
    self.fetchEmails(self.next_url());
  };

  self.fetchPreviousEmails = function() {
    self.fetchEmails(self.previous_url());
  };

  self.fetchEmails(self.next_url());
}

ko.applyBindings(new MainViewModel());
