# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_websitebuild20250429 import models as website_build_20250429_models
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
        self._endpoint = self.get_endpoint('websitebuild', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def operate_app_service_for_partner_with_options(
        self,
        request: website_build_20250429_models.OperateAppServiceForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.OperateAppServiceForPartnerResponse:
        """
        @summary 合作伙伴操作应用服务
        
        @param request: OperateAppServiceForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateAppServiceForPartnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.operate_event):
            query['OperateEvent'] = request.operate_event
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateAppServiceForPartner',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.OperateAppServiceForPartnerResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_app_service_for_partner_with_options_async(
        self,
        request: website_build_20250429_models.OperateAppServiceForPartnerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> website_build_20250429_models.OperateAppServiceForPartnerResponse:
        """
        @summary 合作伙伴操作应用服务
        
        @param request: OperateAppServiceForPartnerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateAppServiceForPartnerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_id):
            query['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.extend):
            query['Extend'] = request.extend
        if not UtilClient.is_unset(request.operate_event):
            query['OperateEvent'] = request.operate_event
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateAppServiceForPartner',
            version='2025-04-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            website_build_20250429_models.OperateAppServiceForPartnerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_app_service_for_partner(
        self,
        request: website_build_20250429_models.OperateAppServiceForPartnerRequest,
    ) -> website_build_20250429_models.OperateAppServiceForPartnerResponse:
        """
        @summary 合作伙伴操作应用服务
        
        @param request: OperateAppServiceForPartnerRequest
        @return: OperateAppServiceForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.operate_app_service_for_partner_with_options(request, runtime)

    async def operate_app_service_for_partner_async(
        self,
        request: website_build_20250429_models.OperateAppServiceForPartnerRequest,
    ) -> website_build_20250429_models.OperateAppServiceForPartnerResponse:
        """
        @summary 合作伙伴操作应用服务
        
        @param request: OperateAppServiceForPartnerRequest
        @return: OperateAppServiceForPartnerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.operate_app_service_for_partner_with_options_async(request, runtime)
