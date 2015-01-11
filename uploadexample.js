//create Uploads collection to store uploaded files
Uploads = new FS.Collection('uploads', {
  stores:[new FS.Store.FileSystem('uploads', {path:'~/projectUploads'})]
});
if (Meteor.isClient) {
  // counter starts at 0
  Session.setDefault("counter", 0);

  Template.hello.helpers({
    counter: function () {
      return Session.get("counter");
    }
  });

  Template.hello.events({
    'click button': function () {
      // increment the counter when button is clicked
      Session.set("counter", Session.get("counter") + 1);
    },
    'change .fileInput':funtion(event,template){
    FS.Utility.eachFile(event, function(){
      var fileObj = new FS.File(file);
      fileObj = new FS.File(file);
      // add file to uploads collection
       Uploads.insert(fileObj, function(err){
         console.log(err);
       })
    })
  }
  });
}

if (Meteor.isServer) {
  Meteor.startup(function () {
    // code to run on server at startup
  });
}
