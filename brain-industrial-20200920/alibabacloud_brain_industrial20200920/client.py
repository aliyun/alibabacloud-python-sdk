# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_brain_industrial20200920 import models as brain_industrial_20200920_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('brain-industrial', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def activate_license_with_options(
        self,
        request: brain_industrial_20200920_models.ActivateLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.ActivateLicenseResponse:
        """
        @summary 激活License
        
        @param request: ActivateLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateLicenseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fingerprint):
            body['Fingerprint'] = request.fingerprint
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_id):
            body['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ActivateLicense',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            brain_industrial_20200920_models.ActivateLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def activate_license_with_options_async(
        self,
        request: brain_industrial_20200920_models.ActivateLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.ActivateLicenseResponse:
        """
        @summary 激活License
        
        @param request: ActivateLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ActivateLicenseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fingerprint):
            body['Fingerprint'] = request.fingerprint
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_id):
            body['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ActivateLicense',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            brain_industrial_20200920_models.ActivateLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def activate_license(
        self,
        request: brain_industrial_20200920_models.ActivateLicenseRequest,
    ) -> brain_industrial_20200920_models.ActivateLicenseResponse:
        """
        @summary 激活License
        
        @param request: ActivateLicenseRequest
        @return: ActivateLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.activate_license_with_options(request, runtime)

    async def activate_license_async(
        self,
        request: brain_industrial_20200920_models.ActivateLicenseRequest,
    ) -> brain_industrial_20200920_models.ActivateLicenseResponse:
        """
        @summary 激活License
        
        @param request: ActivateLicenseRequest
        @return: ActivateLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.activate_license_with_options_async(request, runtime)

    def get_license_with_options(
        self,
        request: brain_industrial_20200920_models.GetLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.GetLicenseResponse:
        """
        @summary License详情
        
        @param request: GetLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLicenseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLicense',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            brain_industrial_20200920_models.GetLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_license_with_options_async(
        self,
        request: brain_industrial_20200920_models.GetLicenseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.GetLicenseResponse:
        """
        @summary License详情
        
        @param request: GetLicenseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetLicenseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLicense',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            brain_industrial_20200920_models.GetLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_license(
        self,
        request: brain_industrial_20200920_models.GetLicenseRequest,
    ) -> brain_industrial_20200920_models.GetLicenseResponse:
        """
        @summary License详情
        
        @param request: GetLicenseRequest
        @return: GetLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_license_with_options(request, runtime)

    async def get_license_async(
        self,
        request: brain_industrial_20200920_models.GetLicenseRequest,
    ) -> brain_industrial_20200920_models.GetLicenseResponse:
        """
        @summary License详情
        
        @param request: GetLicenseRequest
        @return: GetLicenseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_license_with_options_async(request, runtime)

    def list_licenses_with_options(
        self,
        request: brain_industrial_20200920_models.ListLicensesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.ListLicensesResponse:
        """
        @summary License列表
        
        @param request: ListLicensesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLicensesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_str):
            body['QueryStr'] = request.query_str
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLicenses',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            brain_industrial_20200920_models.ListLicensesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_licenses_with_options_async(
        self,
        request: brain_industrial_20200920_models.ListLicensesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.ListLicensesResponse:
        """
        @summary License列表
        
        @param request: ListLicensesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListLicensesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_str):
            body['QueryStr'] = request.query_str
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListLicenses',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            brain_industrial_20200920_models.ListLicensesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_licenses(
        self,
        request: brain_industrial_20200920_models.ListLicensesRequest,
    ) -> brain_industrial_20200920_models.ListLicensesResponse:
        """
        @summary License列表
        
        @param request: ListLicensesRequest
        @return: ListLicensesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_licenses_with_options(request, runtime)

    async def list_licenses_async(
        self,
        request: brain_industrial_20200920_models.ListLicensesRequest,
    ) -> brain_industrial_20200920_models.ListLicensesResponse:
        """
        @summary License列表
        
        @param request: ListLicensesRequest
        @return: ListLicensesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_licenses_with_options_async(request, runtime)

    def list_user_resources_with_options(
        self,
        request: brain_industrial_20200920_models.ListUserResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.ListUserResourcesResponse:
        """
        @summary 获取用户资源列表
        
        @param request: ListUserResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserResources',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            brain_industrial_20200920_models.ListUserResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_resources_with_options_async(
        self,
        request: brain_industrial_20200920_models.ListUserResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.ListUserResourcesResponse:
        """
        @summary 获取用户资源列表
        
        @param request: ListUserResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserResourcesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserResources',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            brain_industrial_20200920_models.ListUserResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_resources(
        self,
        request: brain_industrial_20200920_models.ListUserResourcesRequest,
    ) -> brain_industrial_20200920_models.ListUserResourcesResponse:
        """
        @summary 获取用户资源列表
        
        @param request: ListUserResourcesRequest
        @return: ListUserResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_resources_with_options(request, runtime)

    async def list_user_resources_async(
        self,
        request: brain_industrial_20200920_models.ListUserResourcesRequest,
    ) -> brain_industrial_20200920_models.ListUserResourcesResponse:
        """
        @summary 获取用户资源列表
        
        @param request: ListUserResourcesRequest
        @return: ListUserResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_resources_with_options_async(request, runtime)

    def update_license_description_with_options(
        self,
        request: brain_industrial_20200920_models.UpdateLicenseDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.UpdateLicenseDescriptionResponse:
        """
        @summary 更新license描述
        
        @param request: UpdateLicenseDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLicenseDescriptionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLicenseDescription',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            brain_industrial_20200920_models.UpdateLicenseDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_license_description_with_options_async(
        self,
        request: brain_industrial_20200920_models.UpdateLicenseDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> brain_industrial_20200920_models.UpdateLicenseDescriptionResponse:
        """
        @summary 更新license描述
        
        @param request: UpdateLicenseDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateLicenseDescriptionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateLicenseDescription',
            version='2020-09-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            brain_industrial_20200920_models.UpdateLicenseDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_license_description(
        self,
        request: brain_industrial_20200920_models.UpdateLicenseDescriptionRequest,
    ) -> brain_industrial_20200920_models.UpdateLicenseDescriptionResponse:
        """
        @summary 更新license描述
        
        @param request: UpdateLicenseDescriptionRequest
        @return: UpdateLicenseDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_license_description_with_options(request, runtime)

    async def update_license_description_async(
        self,
        request: brain_industrial_20200920_models.UpdateLicenseDescriptionRequest,
    ) -> brain_industrial_20200920_models.UpdateLicenseDescriptionResponse:
        """
        @summary 更新license描述
        
        @param request: UpdateLicenseDescriptionRequest
        @return: UpdateLicenseDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_license_description_with_options_async(request, runtime)
