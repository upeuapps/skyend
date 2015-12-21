backendApp
.factory("API", function($resource, config ) {
    return {
        UnidadMedida:  $resource(
            config.baseUrl+'configs/unidadmedidas/:id/',
            {'id': '@id'},
        {
            'update': { method:'PUT' },
            'list': { method:'GET', params: { page: '@page', query:'@query', page_size: '@page_size'} }
        }),

        Insumo:  $resource(config.baseUrl+'configs/insumos/:id/', {'id': '@id'},
        {
            'update': { method:'PUT' },
            'list': { method:'GET', params: { page: '@page', query:'@query', page_size: '@page_size'} }
        }),

    };
});
