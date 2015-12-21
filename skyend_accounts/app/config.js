
var baseUrl = 'http://localhost:8000/';
var baseAdmisionUrl = 'http://localhost:8001/';


var client_id = 'btlEG8EIYCavFtOeYaJLwrWPvPzQV7QMcnFK9lcI';
var client_secret = '5OJOnz4QzdB8U5U2UPDkxGq0Nd3UHhYnrhOiHW2SDdMiecqUABcyr9RrmiQt32XZC4wroAeTUhGBR1mFgLMPsfyN7R5LpMD57jrZY3p9imyzgM5T6WbGQUiExoZVIApT';
var grant_type= 'password';

var config = {
    appErrorPrefix: '[WebF1x Error] ', //Configure the exceptionHandler decorator
    docTitle: 'WebF1 xTest: ',
    httpCacheName: 'httpCache',
    baseUrl: baseUrl,
    baseAdmisionUrl: baseAdmisionUrl,

    client_id: client_id,
    client_secret: client_secret,
    grant_type: grant_type,

};

angular.module('accountsApp')

.value('config', config);



angular.module('accountsApp').config(function(toastrConfig) {
  angular.extend(toastrConfig, {
    allowHtml: false,
    autoDismiss: false,
    closeButton: false,
    closeHtml: '<button>&times;</button>',
    containerId: 'toast-container',
    extendedTimeOut: 1000,
    iconClasses: {
      error: 'toast-error',
      info: 'toast-info',
      success: 'toast-success',
      warning: 'toast-warning'
    },
    maxOpened: 0,    
    messageClass: 'toast-message',
    newestOnTop: true,
    onHidden: null,
    onShown: null,
    positionClass: 'toast-top-right',
    preventDuplicates: false,
    preventOpenDuplicates: false,
    progressBar: true,
    tapToDismiss: true,
    target: 'body',
    templates: {
      toast: 'directives/toast/toast.html',
      progressbar: 'directives/progressbar/progressbar.html'
    },
    timeOut: 0,
    titleClass: 'toast-title',
    toastClass: 'toast'
  });
});
//extendedTimeOut: 1000,
//timeOut: 5000,
