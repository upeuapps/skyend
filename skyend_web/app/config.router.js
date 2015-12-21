backendApp
.config(function ($httpProvider) {
    $httpProvider.interceptors.push('authInterceptorService');
})

.run(
    ['$rootScope', '$state', '$stateParams','authService','$location','$window',
      function ( $rootScope,   $state,   $stateParams, authService,$location, $window) {
        $rootScope.$state = $state;
        $rootScope.$stateParams = $stateParams;     
        /*******************************agregado**************************/
        authService.fillAuthData(); 
        if(authService.authentication.isAuth==false){
            //$window.location="../skyend_accounts";
        }       
        /******************************************************************/
      }
    ]
  )


.config(['$stateProvider', '$urlRouterProvider', function($stateProvider,   $urlRouterProvider) {
  $stateProvider

    //------------------------------
    // LOGIN
    //------------------------------
    .state('login', {
      url: '/login',
      templateUrl: 'login/index.html'
    })


    //------------------------------
    // HOME
    //------------------------------
    .state('app', {
      url: '/',
      templateUrl: 'partials/home.tmpl.html'
    })

    //------------------------------
    // test1
    //------------------------------
    .state('test1', {
      url: '/CSS/test1',
      templateUrl: 'app/views/test.html'
    })
    //------------------------------
    // test2
    //------------------------------
    .state('test2', {
      url: '/CSS/test2',
      templateUrl: 'app/views/test2.html',
      resolve: {
        loadPlugin: function($ocLazyLoad) {
          return $ocLazyLoad.load ([
          {
            name: 'app',
            files: [
            'app/loadpost.js',
            
            ]
          }
          ]);
        }
      },
    })
    //------------------------------
    // inicio page http://plnkr.co/edit/u18KQc?p=preview
    //------------------------------
    .state('getting-started', {
      url: '/getting-started',
      templateUrl: 'partials/getting-started.tmpl.html'
    })

    //==================================
    // test1 /app/test1x
    //==================================
    
    .state('test1x', {
      url: '/test1x',
      data : { title: '-tes 1xx' },
      templateUrl: 'app/views/test.html'
    });


    $stateProvider
    //------------------------------
    // naturalPerson
    //------------------------------
    .state('naturalperson', {
      url: '/naturalperson',
      templateUrl: 'app/views/naturalPerson.html'
    })

    //------------------------------
    // unidad medida
    //------------------------------
    .state('unidadmedida', {
      url: '/unidadmedida',
      templateUrl: 'app/views/unidadmedida/index.html'
    })
    //------------------------------
    // insumo
    //------------------------------
    .state('insumo', {
      url: '/insumo',
      templateUrl: 'app/views/insumo/index.html'
    })
    ;



    $urlRouterProvider.otherwise('/');


  }]);


