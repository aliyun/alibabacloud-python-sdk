# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_bpstudio20200710 import models as bpstudio_20200710_models
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
        self._endpoint = self.get_endpoint('bpstudio', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def billing_application_with_options(
        self,
        request: bpstudio_20200710_models.BillingApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20200710_models.BillingApplicationResponse:
        """
        @summary BillingApplication
        
        @param request: BillingApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BillingApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.month):
            body['Month'] = request.month
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.year):
            body['Year'] = request.year
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BillingApplication',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20200710_models.BillingApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def billing_application_with_options_async(
        self,
        request: bpstudio_20200710_models.BillingApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20200710_models.BillingApplicationResponse:
        """
        @summary BillingApplication
        
        @param request: BillingApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BillingApplicationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.month):
            body['Month'] = request.month
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.year):
            body['Year'] = request.year
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BillingApplication',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20200710_models.BillingApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def billing_application(
        self,
        request: bpstudio_20200710_models.BillingApplicationRequest,
    ) -> bpstudio_20200710_models.BillingApplicationResponse:
        """
        @summary BillingApplication
        
        @param request: BillingApplicationRequest
        @return: BillingApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.billing_application_with_options(request, runtime)

    async def billing_application_async(
        self,
        request: bpstudio_20200710_models.BillingApplicationRequest,
    ) -> bpstudio_20200710_models.BillingApplicationResponse:
        """
        @summary BillingApplication
        
        @param request: BillingApplicationRequest
        @return: BillingApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.billing_application_with_options_async(request, runtime)

    def get_deploy_detail_with_options(
        self,
        request: bpstudio_20200710_models.GetDeployDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20200710_models.GetDeployDetailResponse:
        """
        @summary 分页查询部署清单
        
        @param request: GetDeployDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeployDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.ref_id):
            body['RefId'] = request.ref_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            body['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeployDetail',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20200710_models.GetDeployDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deploy_detail_with_options_async(
        self,
        request: bpstudio_20200710_models.GetDeployDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> bpstudio_20200710_models.GetDeployDetailResponse:
        """
        @summary 分页查询部署清单
        
        @param request: GetDeployDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDeployDetailResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.ref_id):
            body['RefId'] = request.ref_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            body['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeployDetail',
            version='2020-07-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            bpstudio_20200710_models.GetDeployDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deploy_detail(
        self,
        request: bpstudio_20200710_models.GetDeployDetailRequest,
    ) -> bpstudio_20200710_models.GetDeployDetailResponse:
        """
        @summary 分页查询部署清单
        
        @param request: GetDeployDetailRequest
        @return: GetDeployDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_deploy_detail_with_options(request, runtime)

    async def get_deploy_detail_async(
        self,
        request: bpstudio_20200710_models.GetDeployDetailRequest,
    ) -> bpstudio_20200710_models.GetDeployDetailResponse:
        """
        @summary 分页查询部署清单
        
        @param request: GetDeployDetailRequest
        @return: GetDeployDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_deploy_detail_with_options_async(request, runtime)
