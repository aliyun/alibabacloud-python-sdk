# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudcontrol20220606 import models as cloudcontrol_20220606_models
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
        self._endpoint = self.get_endpoint('cloudcontrol', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_resource(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: cloudcontrol_20220606_models.CreateResourceRequest,
    ) -> cloudcontrol_20220606_models.CreateResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_with_options(provider, product_code, resource_type_code, request, headers, runtime)

    async def create_resource_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: cloudcontrol_20220606_models.CreateResourceRequest,
    ) -> cloudcontrol_20220606_models.CreateResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_with_options_async(provider, product_code, resource_type_code, request, headers, runtime)

    def create_resource_with_options(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: cloudcontrol_20220606_models.CreateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.CreateResourceResponse:
        UtilClient.validate_model(request)
        provider = OpenApiUtilClient.get_encode_param(provider)
        product_code = OpenApiUtilClient.get_encode_param(product_code)
        resource_type_code = OpenApiUtilClient.get_encode_param(resource_type_code)
        query = {}
        if not UtilClient.is_unset(request.resource_type_version):
            query['resourceTypeVersion'] = request.resource_type_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.CreateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_with_options_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: cloudcontrol_20220606_models.CreateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.CreateResourceResponse:
        UtilClient.validate_model(request)
        provider = OpenApiUtilClient.get_encode_param(provider)
        product_code = OpenApiUtilClient.get_encode_param(product_code)
        resource_type_code = OpenApiUtilClient.get_encode_param(resource_type_code)
        query = {}
        if not UtilClient.is_unset(request.resource_type_version):
            query['resourceTypeVersion'] = request.resource_type_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.CreateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: cloudcontrol_20220606_models.DeleteResourceRequest,
    ) -> cloudcontrol_20220606_models.DeleteResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_with_options(provider, product_code, resource_type_code, resource_id, request, headers, runtime)

    async def delete_resource_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: cloudcontrol_20220606_models.DeleteResourceRequest,
    ) -> cloudcontrol_20220606_models.DeleteResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_with_options_async(provider, product_code, resource_type_code, resource_id, request, headers, runtime)

    def delete_resource_with_options(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: cloudcontrol_20220606_models.DeleteResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.DeleteResourceResponse:
        UtilClient.validate_model(request)
        provider = OpenApiUtilClient.get_encode_param(provider)
        product_code = OpenApiUtilClient.get_encode_param(product_code)
        resource_type_code = OpenApiUtilClient.get_encode_param(resource_type_code)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type_version):
            query['resourceTypeVersion'] = request.resource_type_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResource',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources/{resource_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.DeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_with_options_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: cloudcontrol_20220606_models.DeleteResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.DeleteResourceResponse:
        UtilClient.validate_model(request)
        provider = OpenApiUtilClient.get_encode_param(provider)
        product_code = OpenApiUtilClient.get_encode_param(product_code)
        resource_type_code = OpenApiUtilClient.get_encode_param(resource_type_code)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type_version):
            query['resourceTypeVersion'] = request.resource_type_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResource',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources/{resource_id}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.DeleteResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: cloudcontrol_20220606_models.GetResourceRequest,
    ) -> cloudcontrol_20220606_models.GetResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_with_options(provider, product_code, resource_type_code, resource_id, request, headers, runtime)

    async def get_resource_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: cloudcontrol_20220606_models.GetResourceRequest,
    ) -> cloudcontrol_20220606_models.GetResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_with_options_async(provider, product_code, resource_type_code, resource_id, request, headers, runtime)

    def get_resource_with_options(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: cloudcontrol_20220606_models.GetResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.GetResourceResponse:
        UtilClient.validate_model(request)
        provider = OpenApiUtilClient.get_encode_param(provider)
        product_code = OpenApiUtilClient.get_encode_param(product_code)
        resource_type_code = OpenApiUtilClient.get_encode_param(resource_type_code)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type_version):
            query['resourceTypeVersion'] = request.resource_type_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResource',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources/{resource_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.GetResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_with_options_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: cloudcontrol_20220606_models.GetResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.GetResourceResponse:
        UtilClient.validate_model(request)
        provider = OpenApiUtilClient.get_encode_param(provider)
        product_code = OpenApiUtilClient.get_encode_param(product_code)
        resource_type_code = OpenApiUtilClient.get_encode_param(resource_type_code)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type_version):
            query['resourceTypeVersion'] = request.resource_type_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResource',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources/{resource_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.GetResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_type(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: cloudcontrol_20220606_models.GetResourceTypeRequest,
    ) -> cloudcontrol_20220606_models.GetResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_type_with_options(provider, product_code, resource_type_code, request, headers, runtime)

    async def get_resource_type_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: cloudcontrol_20220606_models.GetResourceTypeRequest,
    ) -> cloudcontrol_20220606_models.GetResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_type_with_options_async(provider, product_code, resource_type_code, request, headers, runtime)

    def get_resource_type_with_options(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: cloudcontrol_20220606_models.GetResourceTypeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.GetResourceTypeResponse:
        UtilClient.validate_model(request)
        provider = OpenApiUtilClient.get_encode_param(provider)
        product_code = OpenApiUtilClient.get_encode_param(product_code)
        resource_type_code = OpenApiUtilClient.get_encode_param(resource_type_code)
        query = {}
        if not UtilClient.is_unset(request.resource_type_version):
            query['resourceTypeVersion'] = request.resource_type_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceType',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.GetResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_type_with_options_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: cloudcontrol_20220606_models.GetResourceTypeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.GetResourceTypeResponse:
        UtilClient.validate_model(request)
        provider = OpenApiUtilClient.get_encode_param(provider)
        product_code = OpenApiUtilClient.get_encode_param(product_code)
        resource_type_code = OpenApiUtilClient.get_encode_param(resource_type_code)
        query = {}
        if not UtilClient.is_unset(request.resource_type_version):
            query['resourceTypeVersion'] = request.resource_type_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceType',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.GetResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        task_id: str,
    ) -> cloudcontrol_20220606_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_with_options(task_id, headers, runtime)

    async def get_task_async(
        self,
        task_id: str,
    ) -> cloudcontrol_20220606_models.GetTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_with_options_async(task_id, headers, runtime)

    def get_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.GetTaskResponse:
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/tasks/{task_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.GetTaskResponse:
        task_id = OpenApiUtilClient.get_encode_param(task_id)
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/tasks/{task_id}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_sources(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        attribute_name: str,
        request: cloudcontrol_20220606_models.ListDataSourcesRequest,
    ) -> cloudcontrol_20220606_models.ListDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_sources_with_options(provider, product_code, resource_type_code, attribute_name, request, headers, runtime)

    async def list_data_sources_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        attribute_name: str,
        request: cloudcontrol_20220606_models.ListDataSourcesRequest,
    ) -> cloudcontrol_20220606_models.ListDataSourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_sources_with_options_async(provider, product_code, resource_type_code, attribute_name, request, headers, runtime)

    def list_data_sources_with_options(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        attribute_name: str,
        tmp_req: cloudcontrol_20220606_models.ListDataSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.ListDataSourcesResponse:
        UtilClient.validate_model(tmp_req)
        provider = OpenApiUtilClient.get_encode_param(provider)
        product_code = OpenApiUtilClient.get_encode_param(product_code)
        resource_type_code = OpenApiUtilClient.get_encode_param(resource_type_code)
        attribute_name = OpenApiUtilClient.get_encode_param(attribute_name)
        request = cloudcontrol_20220606_models.ListDataSourcesShrinkRequest()
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
        params = open_api_models.Params(
            action='ListDataSources',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/dataSources/{attribute_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.ListDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_sources_with_options_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        attribute_name: str,
        tmp_req: cloudcontrol_20220606_models.ListDataSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.ListDataSourcesResponse:
        UtilClient.validate_model(tmp_req)
        provider = OpenApiUtilClient.get_encode_param(provider)
        product_code = OpenApiUtilClient.get_encode_param(product_code)
        resource_type_code = OpenApiUtilClient.get_encode_param(resource_type_code)
        attribute_name = OpenApiUtilClient.get_encode_param(attribute_name)
        request = cloudcontrol_20220606_models.ListDataSourcesShrinkRequest()
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
        params = open_api_models.Params(
            action='ListDataSources',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/dataSources/{attribute_name}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.ListDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_products(
        self,
        provider: str,
        request: cloudcontrol_20220606_models.ListProductsRequest,
    ) -> cloudcontrol_20220606_models.ListProductsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_products_with_options(provider, request, headers, runtime)

    async def list_products_async(
        self,
        provider: str,
        request: cloudcontrol_20220606_models.ListProductsRequest,
    ) -> cloudcontrol_20220606_models.ListProductsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_products_with_options_async(provider, request, headers, runtime)

    def list_products_with_options(
        self,
        provider: str,
        request: cloudcontrol_20220606_models.ListProductsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.ListProductsResponse:
        UtilClient.validate_model(request)
        provider = OpenApiUtilClient.get_encode_param(provider)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.ListProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_products_with_options_async(
        self,
        provider: str,
        request: cloudcontrol_20220606_models.ListProductsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.ListProductsResponse:
        UtilClient.validate_model(request)
        provider = OpenApiUtilClient.get_encode_param(provider)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.ListProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_types(
        self,
        provider: str,
        product_code: str,
        request: cloudcontrol_20220606_models.ListResourceTypesRequest,
    ) -> cloudcontrol_20220606_models.ListResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_types_with_options(provider, product_code, request, headers, runtime)

    async def list_resource_types_async(
        self,
        provider: str,
        product_code: str,
        request: cloudcontrol_20220606_models.ListResourceTypesRequest,
    ) -> cloudcontrol_20220606_models.ListResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_types_with_options_async(provider, product_code, request, headers, runtime)

    def list_resource_types_with_options(
        self,
        provider: str,
        product_code: str,
        tmp_req: cloudcontrol_20220606_models.ListResourceTypesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.ListResourceTypesResponse:
        UtilClient.validate_model(tmp_req)
        provider = OpenApiUtilClient.get_encode_param(provider)
        product_code = OpenApiUtilClient.get_encode_param(product_code)
        request = cloudcontrol_20220606_models.ListResourceTypesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_type_codes):
            request.resource_type_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_type_codes, 'resourceTypeCodes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type_codes_shrink):
            query['resourceTypeCodes'] = request.resource_type_codes_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypes',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.ListResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_types_with_options_async(
        self,
        provider: str,
        product_code: str,
        tmp_req: cloudcontrol_20220606_models.ListResourceTypesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.ListResourceTypesResponse:
        UtilClient.validate_model(tmp_req)
        provider = OpenApiUtilClient.get_encode_param(provider)
        product_code = OpenApiUtilClient.get_encode_param(product_code)
        request = cloudcontrol_20220606_models.ListResourceTypesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_type_codes):
            request.resource_type_codes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_type_codes, 'resourceTypeCodes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type_codes_shrink):
            query['resourceTypeCodes'] = request.resource_type_codes_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypes',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.ListResourceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: cloudcontrol_20220606_models.ListResourcesRequest,
    ) -> cloudcontrol_20220606_models.ListResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resources_with_options(provider, product_code, resource_type_code, request, headers, runtime)

    async def list_resources_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        request: cloudcontrol_20220606_models.ListResourcesRequest,
    ) -> cloudcontrol_20220606_models.ListResourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resources_with_options_async(provider, product_code, resource_type_code, request, headers, runtime)

    def list_resources_with_options(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        tmp_req: cloudcontrol_20220606_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.ListResourcesResponse:
        UtilClient.validate_model(tmp_req)
        provider = OpenApiUtilClient.get_encode_param(provider)
        product_code = OpenApiUtilClient.get_encode_param(product_code)
        resource_type_code = OpenApiUtilClient.get_encode_param(resource_type_code)
        request = cloudcontrol_20220606_models.ListResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'regionIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['regionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.resource_type_version):
            query['resourceTypeVersion'] = request.resource_type_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        tmp_req: cloudcontrol_20220606_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.ListResourcesResponse:
        UtilClient.validate_model(tmp_req)
        provider = OpenApiUtilClient.get_encode_param(provider)
        product_code = OpenApiUtilClient.get_encode_param(product_code)
        resource_type_code = OpenApiUtilClient.get_encode_param(resource_type_code)
        request = cloudcontrol_20220606_models.ListResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'regionIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['regionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.resource_type_version):
            query['resourceTypeVersion'] = request.resource_type_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.ListResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: cloudcontrol_20220606_models.UpdateResourceRequest,
    ) -> cloudcontrol_20220606_models.UpdateResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_with_options(provider, product_code, resource_type_code, resource_id, request, headers, runtime)

    async def update_resource_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: cloudcontrol_20220606_models.UpdateResourceRequest,
    ) -> cloudcontrol_20220606_models.UpdateResourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resource_with_options_async(provider, product_code, resource_type_code, resource_id, request, headers, runtime)

    def update_resource_with_options(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: cloudcontrol_20220606_models.UpdateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.UpdateResourceResponse:
        UtilClient.validate_model(request)
        provider = OpenApiUtilClient.get_encode_param(provider)
        product_code = OpenApiUtilClient.get_encode_param(product_code)
        resource_type_code = OpenApiUtilClient.get_encode_param(resource_type_code)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type_version):
            query['resourceTypeVersion'] = request.resource_type_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateResource',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources/{resource_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.UpdateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_with_options_async(
        self,
        provider: str,
        product_code: str,
        resource_type_code: str,
        resource_id: str,
        request: cloudcontrol_20220606_models.UpdateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220606_models.UpdateResourceResponse:
        UtilClient.validate_model(request)
        provider = OpenApiUtilClient.get_encode_param(provider)
        product_code = OpenApiUtilClient.get_encode_param(product_code)
        resource_type_code = OpenApiUtilClient.get_encode_param(resource_type_code)
        resource_id = OpenApiUtilClient.get_encode_param(resource_id)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type_version):
            query['resourceTypeVersion'] = request.resource_type_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=request.body
        )
        params = open_api_models.Params(
            action='UpdateResource',
            version='2022-06-06',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{provider}/products/{product_code}/resourceTypes/{resource_type_code}/resources/{resource_id}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220606_models.UpdateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )
