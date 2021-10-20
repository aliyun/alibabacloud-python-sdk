# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_iacservice20210722 import models as ia_cservice_20210722_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(
        self, 
        config: open_api_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('iacservice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(
        self,
        product_id: str,
        region_id: str,
        endpoint_rule: str,
        network: str,
        suffix: str,
        endpoint_map: Dict[str, str],
        endpoint: str,
    ) -> str:
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def reload_resources(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: ia_cservice_20210722_models.ReloadResourcesRequest,
    ) -> ia_cservice_20210722_models.ReloadResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.reload_resources_with_options(provider, product_code, resource_type_code, request, headers, runtime)

    async def reload_resources_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: ia_cservice_20210722_models.ReloadResourcesRequest,
    ) -> ia_cservice_20210722_models.ReloadResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.reload_resources_with_options_async(provider, product_code, resource_type_code, request, headers, runtime)

    def reload_resources_with_options(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        tmp_req: ia_cservice_20210722_models.ReloadResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.ReloadResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210722_models.ReloadResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'regionIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['regionIds'] = request.region_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.ReloadResourcesResponse(),
            self.do_roarequest('ReloadResources', '2021-07-22', 'HTTPS', 'PUT', 'AK', f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources/operation/reload', 'json', req, runtime)
        )

    async def reload_resources_with_options_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        tmp_req: ia_cservice_20210722_models.ReloadResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.ReloadResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210722_models.ReloadResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'regionIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['regionIds'] = request.region_ids_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.ReloadResourcesResponse(),
            await self.do_roarequest_async('ReloadResources', '2021-07-22', 'HTTPS', 'PUT', 'AK', f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources/operation/reload', 'json', req, runtime)
        )

    def list_resource_types(
        self,
        provider: str,
        product_code: str,
        request: ia_cservice_20210722_models.ListResourceTypesRequest,
    ) -> ia_cservice_20210722_models.ListResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_types_with_options(provider, product_code, request, headers, runtime)

    async def list_resource_types_async(
        self,
        provider: str,
        product_code: str,
        request: ia_cservice_20210722_models.ListResourceTypesRequest,
    ) -> ia_cservice_20210722_models.ListResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_types_with_options_async(provider, product_code, request, headers, runtime)

    def list_resource_types_with_options(
        self,
        provider: str,
        product_code: str,
        tmp_req: ia_cservice_20210722_models.ListResourceTypesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.ListResourceTypesResponse:
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210722_models.ListResourceTypesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_type_codes):
            request.resource_type_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_type_codes, 'resourceTypeCodes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.resource_type_codes_shrink):
            query['resourceTypeCodes'] = request.resource_type_codes_shrink
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.ListResourceTypesResponse(),
            self.do_roarequest('ListResourceTypes', '2021-07-22', 'HTTPS', 'GET', 'AK', f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes', 'json', req, runtime)
        )

    async def list_resource_types_with_options_async(
        self,
        provider: str,
        product_code: str,
        tmp_req: ia_cservice_20210722_models.ListResourceTypesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.ListResourceTypesResponse:
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210722_models.ListResourceTypesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_type_codes):
            request.resource_type_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_type_codes, 'resourceTypeCodes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.resource_type_codes_shrink):
            query['resourceTypeCodes'] = request.resource_type_codes_shrink
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.ListResourceTypesResponse(),
            await self.do_roarequest_async('ListResourceTypes', '2021-07-22', 'HTTPS', 'GET', 'AK', f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes', 'json', req, runtime)
        )

    def list_products(
        self,
        provider: str,
        request: ia_cservice_20210722_models.ListProductsRequest,
    ) -> ia_cservice_20210722_models.ListProductsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_products_with_options(provider, request, headers, runtime)

    async def list_products_async(
        self,
        provider: str,
        request: ia_cservice_20210722_models.ListProductsRequest,
    ) -> ia_cservice_20210722_models.ListProductsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_products_with_options_async(provider, request, headers, runtime)

    def list_products_with_options(
        self,
        provider: str,
        request: ia_cservice_20210722_models.ListProductsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.ListProductsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.ListProductsResponse(),
            self.do_roarequest('ListProducts', '2021-07-22', 'HTTPS', 'GET', 'AK', f'/api/v1/providers/{provider}/products', 'json', req, runtime)
        )

    async def list_products_with_options_async(
        self,
        provider: str,
        request: ia_cservice_20210722_models.ListProductsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.ListProductsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.ListProductsResponse(),
            await self.do_roarequest_async('ListProducts', '2021-07-22', 'HTTPS', 'GET', 'AK', f'/api/v1/providers/{provider}/products', 'json', req, runtime)
        )

    def list_resources(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: ia_cservice_20210722_models.ListResourcesRequest,
    ) -> ia_cservice_20210722_models.ListResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resources_with_options(provider, product_code, resource_type_code, request, headers, runtime)

    async def list_resources_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: ia_cservice_20210722_models.ListResourcesRequest,
    ) -> ia_cservice_20210722_models.ListResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resources_with_options_async(provider, product_code, resource_type_code, request, headers, runtime)

    def list_resources_with_options(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        tmp_req: ia_cservice_20210722_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.ListResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210722_models.ListResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'regionIds', 'simple')
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['regionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.is_reload):
            query['isReload'] = request.is_reload
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.ListResourcesResponse(),
            self.do_roarequest('ListResources', '2021-07-22', 'HTTPS', 'GET', 'AK', f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources', 'json', req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        tmp_req: ia_cservice_20210722_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.ListResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210722_models.ListResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'regionIds', 'simple')
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['regionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.page_num):
            query['pageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.is_reload):
            query['isReload'] = request.is_reload
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.ListResourcesResponse(),
            await self.do_roarequest_async('ListResources', '2021-07-22', 'HTTPS', 'GET', 'AK', f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources', 'json', req, runtime)
        )

    def list_data_sources(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        attribute_name: str,
        request: ia_cservice_20210722_models.ListDataSourcesRequest,
    ) -> ia_cservice_20210722_models.ListDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_sources_with_options(provider, product_code, resource_type_code, attribute_name, request, headers, runtime)

    async def list_data_sources_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        attribute_name: str,
        request: ia_cservice_20210722_models.ListDataSourcesRequest,
    ) -> ia_cservice_20210722_models.ListDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_sources_with_options_async(provider, product_code, resource_type_code, attribute_name, request, headers, runtime)

    def list_data_sources_with_options(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        attribute_name: str,
        tmp_req: ia_cservice_20210722_models.ListDataSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.ListDataSourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210722_models.ListDataSourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_shrink):
            query['filter'] = request.filter_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.ListDataSourcesResponse(),
            self.do_roarequest('ListDataSources', '2021-07-22', 'HTTPS', 'GET', 'AK', f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/dataSources/{attribute_name}', 'json', req, runtime)
        )

    async def list_data_sources_with_options_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        attribute_name: str,
        tmp_req: ia_cservice_20210722_models.ListDataSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.ListDataSourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210722_models.ListDataSourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_shrink):
            query['filter'] = request.filter_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.ListDataSourcesResponse(),
            await self.do_roarequest_async('ListDataSources', '2021-07-22', 'HTTPS', 'GET', 'AK', f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/dataSources/{attribute_name}', 'json', req, runtime)
        )

    def create_resource(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: ia_cservice_20210722_models.CreateResourceRequest,
    ) -> ia_cservice_20210722_models.CreateResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_with_options(provider, product_code, resource_type_code, request, headers, runtime)

    async def create_resource_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: ia_cservice_20210722_models.CreateResourceRequest,
    ) -> ia_cservice_20210722_models.CreateResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_with_options_async(provider, product_code, resource_type_code, request, headers, runtime)

    def create_resource_with_options(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: ia_cservice_20210722_models.CreateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.CreateResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_async):
            query['isAsync'] = request.is_async
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.CreateResourceResponse(),
            self.do_roarequest('CreateResource', '2021-07-22', 'HTTPS', 'POST', 'AK', f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources', 'json', req, runtime)
        )

    async def create_resource_with_options_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: ia_cservice_20210722_models.CreateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.CreateResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_async):
            query['isAsync'] = request.is_async
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.CreateResourceResponse(),
            await self.do_roarequest_async('CreateResource', '2021-07-22', 'HTTPS', 'POST', 'AK', f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources', 'json', req, runtime)
        )

    def get_task(
        self,
        task_id: str,
    ) -> ia_cservice_20210722_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_with_options(task_id, headers, runtime)

    async def get_task_async(
        self,
        task_id: str,
    ) -> ia_cservice_20210722_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_with_options_async(task_id, headers, runtime)

    def get_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.GetTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.GetTaskResponse(),
            self.do_roarequest('GetTask', '2021-07-22', 'HTTPS', 'GET', 'AK', f'/api/v1/tasks/{task_id}', 'json', req, runtime)
        )

    async def get_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.GetTaskResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.GetTaskResponse(),
            await self.do_roarequest_async('GetTask', '2021-07-22', 'HTTPS', 'GET', 'AK', f'/api/v1/tasks/{task_id}', 'json', req, runtime)
        )

    def update_resource(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: ia_cservice_20210722_models.UpdateResourceRequest,
    ) -> ia_cservice_20210722_models.UpdateResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_with_options(provider, product_code, resource_type_code, resource_id, request, headers, runtime)

    async def update_resource_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: ia_cservice_20210722_models.UpdateResourceRequest,
    ) -> ia_cservice_20210722_models.UpdateResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resource_with_options_async(provider, product_code, resource_type_code, resource_id, request, headers, runtime)

    def update_resource_with_options(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: ia_cservice_20210722_models.UpdateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.UpdateResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_async):
            query['isAsync'] = request.is_async
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.UpdateResourceResponse(),
            self.do_roarequest('UpdateResource', '2021-07-22', 'HTTPS', 'PUT', 'AK', f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources/{resource_id}', 'json', req, runtime)
        )

    async def update_resource_with_options_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: ia_cservice_20210722_models.UpdateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.UpdateResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_async):
            query['isAsync'] = request.is_async
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.UpdateResourceResponse(),
            await self.do_roarequest_async('UpdateResource', '2021-07-22', 'HTTPS', 'PUT', 'AK', f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources/{resource_id}', 'json', req, runtime)
        )

    def get_resource(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: ia_cservice_20210722_models.GetResourceRequest,
    ) -> ia_cservice_20210722_models.GetResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_with_options(provider, product_code, resource_type_code, resource_id, request, headers, runtime)

    async def get_resource_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: ia_cservice_20210722_models.GetResourceRequest,
    ) -> ia_cservice_20210722_models.GetResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_with_options_async(provider, product_code, resource_type_code, resource_id, request, headers, runtime)

    def get_resource_with_options(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: ia_cservice_20210722_models.GetResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.GetResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.GetResourceResponse(),
            self.do_roarequest('GetResource', '2021-07-22', 'HTTPS', 'GET', 'AK', f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources/{resource_id}', 'json', req, runtime)
        )

    async def get_resource_with_options_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: ia_cservice_20210722_models.GetResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.GetResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.GetResourceResponse(),
            await self.do_roarequest_async('GetResource', '2021-07-22', 'HTTPS', 'GET', 'AK', f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources/{resource_id}', 'json', req, runtime)
        )

    def delete_resource(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: ia_cservice_20210722_models.DeleteResourceRequest,
    ) -> ia_cservice_20210722_models.DeleteResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_with_options(provider, product_code, resource_type_code, resource_id, request, headers, runtime)

    async def delete_resource_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: ia_cservice_20210722_models.DeleteResourceRequest,
    ) -> ia_cservice_20210722_models.DeleteResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_with_options_async(provider, product_code, resource_type_code, resource_id, request, headers, runtime)

    def delete_resource_with_options(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: ia_cservice_20210722_models.DeleteResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.DeleteResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.is_async):
            query['isAsync'] = request.is_async
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.DeleteResourceResponse(),
            self.do_roarequest('DeleteResource', '2021-07-22', 'HTTPS', 'DELETE', 'AK', f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources/{resource_id}', 'json', req, runtime)
        )

    async def delete_resource_with_options_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: ia_cservice_20210722_models.DeleteResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210722_models.DeleteResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.is_async):
            query['isAsync'] = request.is_async
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return TeaCore.from_map(
            ia_cservice_20210722_models.DeleteResourceResponse(),
            await self.do_roarequest_async('DeleteResource', '2021-07-22', 'HTTPS', 'DELETE', 'AK', f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources/{resource_id}', 'json', req, runtime)
        )
