# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_cloudcontrol20220830 import models as cloudcontrol_20220830_models
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

    def cancel_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.CancelTaskResponse:
        """
        @summary Calls this operation to cancel a specified asynchronous task.
        
        @description Only tasks that are in the Pending or Running state can be canceled.
        You can call the CancelTask operation to cancel a Cloud Control API task, but the tasks that have been started in the downstream Alibaba Cloud services cannot be canceled.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'/api/v1/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/operation/cancel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.CancelTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.CancelTaskResponse:
        """
        @summary Calls this operation to cancel a specified asynchronous task.
        
        @description Only tasks that are in the Pending or Running state can be canceled.
        You can call the CancelTask operation to cancel a Cloud Control API task, but the tasks that have been started in the downstream Alibaba Cloud services cannot be canceled.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='CancelTask',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'/api/v1/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/operation/cancel',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.CancelTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_task(
        self,
        task_id: str,
    ) -> cloudcontrol_20220830_models.CancelTaskResponse:
        """
        @summary Calls this operation to cancel a specified asynchronous task.
        
        @description Only tasks that are in the Pending or Running state can be canceled.
        You can call the CancelTask operation to cancel a Cloud Control API task, but the tasks that have been started in the downstream Alibaba Cloud services cannot be canceled.
        
        @return: CancelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_task_with_options(task_id, headers, runtime)

    async def cancel_task_async(
        self,
        task_id: str,
    ) -> cloudcontrol_20220830_models.CancelTaskResponse:
        """
        @summary Calls this operation to cancel a specified asynchronous task.
        
        @description Only tasks that are in the Pending or Running state can be canceled.
        You can call the CancelTask operation to cancel a Cloud Control API task, but the tasks that have been started in the downstream Alibaba Cloud services cannot be canceled.
        
        @return: CancelTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_task_with_options_async(task_id, headers, runtime)

    def create_resource_with_options(
        self,
        request_path: str,
        request: cloudcontrol_20220830_models.CreateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.CreateResourceResponse:
        """
        @summary Calls this operation to create resources.
        
        @description You can go to [OpenAPI Explorer](https://next.api.aliyun.com/cloudcontrol) to view the documentation and try out Cloud Control API.
        
        @param request_path: the whole path of resource string
        @param request: CreateResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'{request_path}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.CreateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_with_options_async(
        self,
        request_path: str,
        request: cloudcontrol_20220830_models.CreateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.CreateResourceResponse:
        """
        @summary Calls this operation to create resources.
        
        @description You can go to [OpenAPI Explorer](https://next.api.aliyun.com/cloudcontrol) to view the documentation and try out Cloud Control API.
        
        @param request_path: the whole path of resource string
        @param request: CreateResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'{request_path}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.CreateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource(
        self,
        request_path: str,
        request: cloudcontrol_20220830_models.CreateResourceRequest,
    ) -> cloudcontrol_20220830_models.CreateResourceResponse:
        """
        @summary Calls this operation to create resources.
        
        @description You can go to [OpenAPI Explorer](https://next.api.aliyun.com/cloudcontrol) to view the documentation and try out Cloud Control API.
        
        @param request_path: the whole path of resource string
        @param request: CreateResourceRequest
        @return: CreateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_with_options(request_path, request, headers, runtime)

    async def create_resource_async(
        self,
        request_path: str,
        request: cloudcontrol_20220830_models.CreateResourceRequest,
    ) -> cloudcontrol_20220830_models.CreateResourceResponse:
        """
        @summary Calls this operation to create resources.
        
        @description You can go to [OpenAPI Explorer](https://next.api.aliyun.com/cloudcontrol) to view the documentation and try out Cloud Control API.
        
        @param request_path: the whole path of resource string
        @param request: CreateResourceRequest
        @return: CreateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_with_options_async(request_path, request, headers, runtime)

    def delete_resource_with_options(
        self,
        request_path: str,
        tmp_req: cloudcontrol_20220830_models.DeleteResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.DeleteResourceResponse:
        """
        @summary Calls this operation to delete resources.
        
        @description You can go to [OpenAPI Explorer](https://next.api.aliyun.com/cloudcontrol) to view the documentation and try out Cloud Control API.
        
        @param request_path: the whole path of resource string
        @param tmp_req: DeleteResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudcontrol_20220830_models.DeleteResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResource',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'{request_path}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.DeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_with_options_async(
        self,
        request_path: str,
        tmp_req: cloudcontrol_20220830_models.DeleteResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.DeleteResourceResponse:
        """
        @summary Calls this operation to delete resources.
        
        @description You can go to [OpenAPI Explorer](https://next.api.aliyun.com/cloudcontrol) to view the documentation and try out Cloud Control API.
        
        @param request_path: the whole path of resource string
        @param tmp_req: DeleteResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudcontrol_20220830_models.DeleteResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResource',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'{request_path}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.DeleteResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource(
        self,
        request_path: str,
        request: cloudcontrol_20220830_models.DeleteResourceRequest,
    ) -> cloudcontrol_20220830_models.DeleteResourceResponse:
        """
        @summary Calls this operation to delete resources.
        
        @description You can go to [OpenAPI Explorer](https://next.api.aliyun.com/cloudcontrol) to view the documentation and try out Cloud Control API.
        
        @param request_path: the whole path of resource string
        @param request: DeleteResourceRequest
        @return: DeleteResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_with_options(request_path, request, headers, runtime)

    async def delete_resource_async(
        self,
        request_path: str,
        request: cloudcontrol_20220830_models.DeleteResourceRequest,
    ) -> cloudcontrol_20220830_models.DeleteResourceResponse:
        """
        @summary Calls this operation to delete resources.
        
        @description You can go to [OpenAPI Explorer](https://next.api.aliyun.com/cloudcontrol) to view the documentation and try out Cloud Control API.
        
        @param request_path: the whole path of resource string
        @param request: DeleteResourceRequest
        @return: DeleteResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_with_options_async(request_path, request, headers, runtime)

    def get_price_with_options(
        self,
        request_path: str,
        tmp_req: cloudcontrol_20220830_models.GetPriceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.GetPriceResponse:
        """
        @summary An RFQ interface through which users can query resource prices.
        
        @param request_path: the whole path of resource string
        @param tmp_req: GetPriceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPriceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudcontrol_20220830_models.GetPriceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_attributes):
            request.resource_attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_attributes, 'resourceAttributes', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_attributes_shrink):
            query['resourceAttributes'] = request.resource_attributes_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrice',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'{request_path}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.GetPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_price_with_options_async(
        self,
        request_path: str,
        tmp_req: cloudcontrol_20220830_models.GetPriceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.GetPriceResponse:
        """
        @summary An RFQ interface through which users can query resource prices.
        
        @param request_path: the whole path of resource string
        @param tmp_req: GetPriceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPriceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudcontrol_20220830_models.GetPriceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_attributes):
            request.resource_attributes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_attributes, 'resourceAttributes', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_attributes_shrink):
            query['resourceAttributes'] = request.resource_attributes_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrice',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'{request_path}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.GetPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_price(
        self,
        request_path: str,
        request: cloudcontrol_20220830_models.GetPriceRequest,
    ) -> cloudcontrol_20220830_models.GetPriceResponse:
        """
        @summary An RFQ interface through which users can query resource prices.
        
        @param request_path: the whole path of resource string
        @param request: GetPriceRequest
        @return: GetPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_price_with_options(request_path, request, headers, runtime)

    async def get_price_async(
        self,
        request_path: str,
        request: cloudcontrol_20220830_models.GetPriceRequest,
    ) -> cloudcontrol_20220830_models.GetPriceResponse:
        """
        @summary An RFQ interface through which users can query resource prices.
        
        @param request_path: the whole path of resource string
        @param request: GetPriceRequest
        @return: GetPriceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_price_with_options_async(request_path, request, headers, runtime)

    def get_resource_type_with_options(
        self,
        request_path: str,
        headers: cloudcontrol_20220830_models.GetResourceTypeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.GetResourceTypeResponse:
        """
        @summary You can call the operation to obtain resource metadata.
        
        @param request_path: the whole path of resource string
        @param headers: GetResourceTypeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceTypeResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_accept_language):
            real_headers['x-acs-accept-language'] = UtilClient.to_jsonstring(headers.x_acs_accept_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetResourceType',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'{request_path}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.GetResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_type_with_options_async(
        self,
        request_path: str,
        headers: cloudcontrol_20220830_models.GetResourceTypeHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.GetResourceTypeResponse:
        """
        @summary You can call the operation to obtain resource metadata.
        
        @param request_path: the whole path of resource string
        @param headers: GetResourceTypeHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceTypeResponse
        """
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_accept_language):
            real_headers['x-acs-accept-language'] = UtilClient.to_jsonstring(headers.x_acs_accept_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers
        )
        params = open_api_models.Params(
            action='GetResourceType',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'{request_path}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.GetResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_type(
        self,
        request_path: str,
    ) -> cloudcontrol_20220830_models.GetResourceTypeResponse:
        """
        @summary You can call the operation to obtain resource metadata.
        
        @param request_path: the whole path of resource string
        @return: GetResourceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = cloudcontrol_20220830_models.GetResourceTypeHeaders()
        return self.get_resource_type_with_options(request_path, headers, runtime)

    async def get_resource_type_async(
        self,
        request_path: str,
    ) -> cloudcontrol_20220830_models.GetResourceTypeResponse:
        """
        @summary You can call the operation to obtain resource metadata.
        
        @param request_path: the whole path of resource string
        @return: GetResourceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = cloudcontrol_20220830_models.GetResourceTypeHeaders()
        return await self.get_resource_type_with_options_async(request_path, headers, runtime)

    def get_resources_with_options(
        self,
        request_path: str,
        tmp_req: cloudcontrol_20220830_models.GetResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.GetResourcesResponse:
        """
        @summary You can call the operation to query resources.
        
        @description You can go to [OpenAPI Explorer](https://next.api.aliyun.com/cloudcontrol) to view the documentation and try out CloudControl API.
        You can call this operation to query resources List and Get based on different request paths.
        
        @param request_path: the whole path of resource string
        @param tmp_req: GetResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudcontrol_20220830_models.GetResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResources',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'{request_path}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.GetResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resources_with_options_async(
        self,
        request_path: str,
        tmp_req: cloudcontrol_20220830_models.GetResourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.GetResourcesResponse:
        """
        @summary You can call the operation to query resources.
        
        @description You can go to [OpenAPI Explorer](https://next.api.aliyun.com/cloudcontrol) to view the documentation and try out CloudControl API.
        You can call this operation to query resources List and Get based on different request paths.
        
        @param request_path: the whole path of resource string
        @param tmp_req: GetResourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudcontrol_20220830_models.GetResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.filter_shrink):
            query['filter'] = request.filter_shrink
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResources',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'{request_path}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.GetResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resources(
        self,
        request_path: str,
        request: cloudcontrol_20220830_models.GetResourcesRequest,
    ) -> cloudcontrol_20220830_models.GetResourcesResponse:
        """
        @summary You can call the operation to query resources.
        
        @description You can go to [OpenAPI Explorer](https://next.api.aliyun.com/cloudcontrol) to view the documentation and try out CloudControl API.
        You can call this operation to query resources List and Get based on different request paths.
        
        @param request_path: the whole path of resource string
        @param request: GetResourcesRequest
        @return: GetResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resources_with_options(request_path, request, headers, runtime)

    async def get_resources_async(
        self,
        request_path: str,
        request: cloudcontrol_20220830_models.GetResourcesRequest,
    ) -> cloudcontrol_20220830_models.GetResourcesResponse:
        """
        @summary You can call the operation to query resources.
        
        @description You can go to [OpenAPI Explorer](https://next.api.aliyun.com/cloudcontrol) to view the documentation and try out CloudControl API.
        You can call this operation to query resources List and Get based on different request paths.
        
        @param request_path: the whole path of resource string
        @param request: GetResourcesRequest
        @return: GetResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resources_with_options_async(request_path, request, headers, runtime)

    def get_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.GetTaskResponse:
        """
        @summary Calls this operation to query a specified asynchronous task.
        
        @description GET /api/v1/tasks/{taskId}.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'/api/v1/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.GetTaskResponse:
        """
        @summary Calls this operation to query a specified asynchronous task.
        
        @description GET /api/v1/tasks/{taskId}.
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'/api/v1/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        task_id: str,
    ) -> cloudcontrol_20220830_models.GetTaskResponse:
        """
        @summary Calls this operation to query a specified asynchronous task.
        
        @description GET /api/v1/tasks/{taskId}.
        
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_with_options(task_id, headers, runtime)

    async def get_task_async(
        self,
        task_id: str,
    ) -> cloudcontrol_20220830_models.GetTaskResponse:
        """
        @summary Calls this operation to query a specified asynchronous task.
        
        @description GET /api/v1/tasks/{taskId}.
        
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_with_options_async(task_id, headers, runtime)

    def list_data_sources_with_options(
        self,
        request_path: str,
        tmp_req: cloudcontrol_20220830_models.ListDataSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.ListDataSourcesResponse:
        """
        @summary You can call the operation to query the valid values of resource attributes, such as RegionID and ZoneId.
        
        @param request_path: the whole path of resource string
        @param tmp_req: ListDataSourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudcontrol_20220830_models.ListDataSourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.attribute_name):
            query['attributeName'] = request.attribute_name
        if not UtilClient.is_unset(request.filter_shrink):
            query['filter'] = request.filter_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSources',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'{request_path}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.ListDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_sources_with_options_async(
        self,
        request_path: str,
        tmp_req: cloudcontrol_20220830_models.ListDataSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.ListDataSourcesResponse:
        """
        @summary You can call the operation to query the valid values of resource attributes, such as RegionID and ZoneId.
        
        @param request_path: the whole path of resource string
        @param tmp_req: ListDataSourcesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSourcesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudcontrol_20220830_models.ListDataSourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'filter', 'json')
        query = {}
        if not UtilClient.is_unset(request.attribute_name):
            query['attributeName'] = request.attribute_name
        if not UtilClient.is_unset(request.filter_shrink):
            query['filter'] = request.filter_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSources',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'{request_path}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.ListDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_sources(
        self,
        request_path: str,
        request: cloudcontrol_20220830_models.ListDataSourcesRequest,
    ) -> cloudcontrol_20220830_models.ListDataSourcesResponse:
        """
        @summary You can call the operation to query the valid values of resource attributes, such as RegionID and ZoneId.
        
        @param request_path: the whole path of resource string
        @param request: ListDataSourcesRequest
        @return: ListDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_sources_with_options(request_path, request, headers, runtime)

    async def list_data_sources_async(
        self,
        request_path: str,
        request: cloudcontrol_20220830_models.ListDataSourcesRequest,
    ) -> cloudcontrol_20220830_models.ListDataSourcesResponse:
        """
        @summary You can call the operation to query the valid values of resource attributes, such as RegionID and ZoneId.
        
        @param request_path: the whole path of resource string
        @param request: ListDataSourcesRequest
        @return: ListDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_sources_with_options_async(request_path, request, headers, runtime)

    def list_products_with_options(
        self,
        provider: str,
        request: cloudcontrol_20220830_models.ListProductsRequest,
        headers: cloudcontrol_20220830_models.ListProductsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.ListProductsResponse:
        """
        @summary Calls this operation to list the supported services.
        
        @description GET /api/v1/providers/{provider}/products.
        
        @param request: ListProductsRequest
        @param headers: ListProductsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_accept_language):
            real_headers['x-acs-accept-language'] = UtilClient.to_jsonstring(headers.x_acs_accept_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{OpenApiUtilClient.get_encode_param(provider)}/products',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.ListProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_products_with_options_async(
        self,
        provider: str,
        request: cloudcontrol_20220830_models.ListProductsRequest,
        headers: cloudcontrol_20220830_models.ListProductsHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.ListProductsResponse:
        """
        @summary Calls this operation to list the supported services.
        
        @description GET /api/v1/providers/{provider}/products.
        
        @param request: ListProductsRequest
        @param headers: ListProductsHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_accept_language):
            real_headers['x-acs-accept-language'] = UtilClient.to_jsonstring(headers.x_acs_accept_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{OpenApiUtilClient.get_encode_param(provider)}/products',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.ListProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_products(
        self,
        provider: str,
        request: cloudcontrol_20220830_models.ListProductsRequest,
    ) -> cloudcontrol_20220830_models.ListProductsResponse:
        """
        @summary Calls this operation to list the supported services.
        
        @description GET /api/v1/providers/{provider}/products.
        
        @param request: ListProductsRequest
        @return: ListProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = cloudcontrol_20220830_models.ListProductsHeaders()
        return self.list_products_with_options(provider, request, headers, runtime)

    async def list_products_async(
        self,
        provider: str,
        request: cloudcontrol_20220830_models.ListProductsRequest,
    ) -> cloudcontrol_20220830_models.ListProductsResponse:
        """
        @summary Calls this operation to list the supported services.
        
        @description GET /api/v1/providers/{provider}/products.
        
        @param request: ListProductsRequest
        @return: ListProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = cloudcontrol_20220830_models.ListProductsHeaders()
        return await self.list_products_with_options_async(provider, request, headers, runtime)

    def list_resource_types_with_options(
        self,
        provider: str,
        product: str,
        tmp_req: cloudcontrol_20220830_models.ListResourceTypesRequest,
        headers: cloudcontrol_20220830_models.ListResourceTypesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.ListResourceTypesResponse:
        """
        @summary Calls this operation to list the resource types of a service.
        
        @description GET /api/v1/providers/{provider}/products/{product}/resourceTypes.
        
        @param tmp_req: ListResourceTypesRequest
        @param headers: ListResourceTypesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceTypesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudcontrol_20220830_models.ListResourceTypesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_types):
            request.resource_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_types, 'resourceTypes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_types_shrink):
            query['resourceTypes'] = request.resource_types_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_accept_language):
            real_headers['x-acs-accept-language'] = UtilClient.to_jsonstring(headers.x_acs_accept_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypes',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{OpenApiUtilClient.get_encode_param(provider)}/products/{OpenApiUtilClient.get_encode_param(product)}/resourceTypes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.ListResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_types_with_options_async(
        self,
        provider: str,
        product: str,
        tmp_req: cloudcontrol_20220830_models.ListResourceTypesRequest,
        headers: cloudcontrol_20220830_models.ListResourceTypesHeaders,
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.ListResourceTypesResponse:
        """
        @summary Calls this operation to list the resource types of a service.
        
        @description GET /api/v1/providers/{provider}/products/{product}/resourceTypes.
        
        @param tmp_req: ListResourceTypesRequest
        @param headers: ListResourceTypesHeaders
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceTypesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cloudcontrol_20220830_models.ListResourceTypesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resource_types):
            request.resource_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_types, 'resourceTypes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_types_shrink):
            query['resourceTypes'] = request.resource_types_shrink
        real_headers = {}
        if not UtilClient.is_unset(headers.common_headers):
            real_headers = headers.common_headers
        if not UtilClient.is_unset(headers.x_acs_accept_language):
            real_headers['x-acs-accept-language'] = UtilClient.to_jsonstring(headers.x_acs_accept_language)
        req = open_api_models.OpenApiRequest(
            headers=real_headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypes',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'/api/v1/providers/{OpenApiUtilClient.get_encode_param(provider)}/products/{OpenApiUtilClient.get_encode_param(product)}/resourceTypes',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.ListResourceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_types(
        self,
        provider: str,
        product: str,
        request: cloudcontrol_20220830_models.ListResourceTypesRequest,
    ) -> cloudcontrol_20220830_models.ListResourceTypesResponse:
        """
        @summary Calls this operation to list the resource types of a service.
        
        @description GET /api/v1/providers/{provider}/products/{product}/resourceTypes.
        
        @param request: ListResourceTypesRequest
        @return: ListResourceTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = cloudcontrol_20220830_models.ListResourceTypesHeaders()
        return self.list_resource_types_with_options(provider, product, request, headers, runtime)

    async def list_resource_types_async(
        self,
        provider: str,
        product: str,
        request: cloudcontrol_20220830_models.ListResourceTypesRequest,
    ) -> cloudcontrol_20220830_models.ListResourceTypesResponse:
        """
        @summary Calls this operation to list the resource types of a service.
        
        @description GET /api/v1/providers/{provider}/products/{product}/resourceTypes.
        
        @param request: ListResourceTypesRequest
        @return: ListResourceTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = cloudcontrol_20220830_models.ListResourceTypesHeaders()
        return await self.list_resource_types_with_options_async(provider, product, request, headers, runtime)

    def update_resource_with_options(
        self,
        request_path: str,
        request: cloudcontrol_20220830_models.UpdateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.UpdateResourceResponse:
        """
        @summary Calls this operation to update resources.
        
        @description You can go to [OpenAPI Explorer](https://next.api.aliyun.com/cloudcontrol) to view the documentation and try out Cloud Control API.
        If resources fail to be updated at any time, the Cloud Control API does not roll the resource back to the original status.
        The resource APIs cannot be rolled back. If the API operation is partially failed to be called, you can call the GetResource operation to view the latest status of the resource. If necessary, you can call the UpdateResource or DeleteResource operation to manually compensate for the failure.
        
        @param request_path: the whole path of resource string
        @param request: UpdateResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateResource',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'{request_path}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.UpdateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_with_options_async(
        self,
        request_path: str,
        request: cloudcontrol_20220830_models.UpdateResourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cloudcontrol_20220830_models.UpdateResourceResponse:
        """
        @summary Calls this operation to update resources.
        
        @description You can go to [OpenAPI Explorer](https://next.api.aliyun.com/cloudcontrol) to view the documentation and try out Cloud Control API.
        If resources fail to be updated at any time, the Cloud Control API does not roll the resource back to the original status.
        The resource APIs cannot be rolled back. If the API operation is partially failed to be called, you can call the GetResource operation to view the latest status of the resource. If necessary, you can call the UpdateResource or DeleteResource operation to manually compensate for the failure.
        
        @param request_path: the whole path of resource string
        @param request: UpdateResourceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['regionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(request.body)
        )
        params = open_api_models.Params(
            action='UpdateResource',
            version='2022-08-30',
            protocol='HTTPS',
            pathname=f'{request_path}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudcontrol_20220830_models.UpdateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource(
        self,
        request_path: str,
        request: cloudcontrol_20220830_models.UpdateResourceRequest,
    ) -> cloudcontrol_20220830_models.UpdateResourceResponse:
        """
        @summary Calls this operation to update resources.
        
        @description You can go to [OpenAPI Explorer](https://next.api.aliyun.com/cloudcontrol) to view the documentation and try out Cloud Control API.
        If resources fail to be updated at any time, the Cloud Control API does not roll the resource back to the original status.
        The resource APIs cannot be rolled back. If the API operation is partially failed to be called, you can call the GetResource operation to view the latest status of the resource. If necessary, you can call the UpdateResource or DeleteResource operation to manually compensate for the failure.
        
        @param request_path: the whole path of resource string
        @param request: UpdateResourceRequest
        @return: UpdateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_with_options(request_path, request, headers, runtime)

    async def update_resource_async(
        self,
        request_path: str,
        request: cloudcontrol_20220830_models.UpdateResourceRequest,
    ) -> cloudcontrol_20220830_models.UpdateResourceResponse:
        """
        @summary Calls this operation to update resources.
        
        @description You can go to [OpenAPI Explorer](https://next.api.aliyun.com/cloudcontrol) to view the documentation and try out Cloud Control API.
        If resources fail to be updated at any time, the Cloud Control API does not roll the resource back to the original status.
        The resource APIs cannot be rolled back. If the API operation is partially failed to be called, you can call the GetResource operation to view the latest status of the resource. If necessary, you can call the UpdateResource or DeleteResource operation to manually compensate for the failure.
        
        @param request_path: the whole path of resource string
        @param request: UpdateResourceRequest
        @return: UpdateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resource_with_options_async(request_path, request, headers, runtime)
