# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_alimt20190102 import models as alimt_20190102_models
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
        self._endpoint_map = {
            'cn-hangzhou': 'mt.cn-hangzhou.aliyuncs.com',
            'ap-northeast-1': 'mt.aliyuncs.com',
            'ap-northeast-2-pop': 'mt.aliyuncs.com',
            'ap-south-1': 'mt.aliyuncs.com',
            'ap-southeast-1': 'mt.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'mt.aliyuncs.com',
            'ap-southeast-3': 'mt.aliyuncs.com',
            'ap-southeast-5': 'mt.aliyuncs.com',
            'cn-beijing': 'mt.aliyuncs.com',
            'cn-beijing-finance-1': 'mt.aliyuncs.com',
            'cn-beijing-finance-pop': 'mt.aliyuncs.com',
            'cn-beijing-gov-1': 'mt.aliyuncs.com',
            'cn-beijing-nu16-b01': 'mt.aliyuncs.com',
            'cn-chengdu': 'mt.aliyuncs.com',
            'cn-edge-1': 'mt.aliyuncs.com',
            'cn-fujian': 'mt.aliyuncs.com',
            'cn-haidian-cm12-c01': 'mt.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'mt.aliyuncs.com',
            'cn-hangzhou-finance': 'mt.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'mt.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'mt.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'mt.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'mt.aliyuncs.com',
            'cn-hangzhou-test-306': 'mt.aliyuncs.com',
            'cn-hongkong': 'mt.aliyuncs.com',
            'cn-hongkong-finance-pop': 'mt.aliyuncs.com',
            'cn-huhehaote': 'mt.aliyuncs.com',
            'cn-north-2-gov-1': 'mt.aliyuncs.com',
            'cn-qingdao': 'mt.aliyuncs.com',
            'cn-qingdao-nebula': 'mt.aliyuncs.com',
            'cn-shanghai': 'mt.aliyuncs.com',
            'cn-shanghai-et15-b01': 'mt.aliyuncs.com',
            'cn-shanghai-et2-b01': 'mt.aliyuncs.com',
            'cn-shanghai-finance-1': 'mt.aliyuncs.com',
            'cn-shanghai-inner': 'mt.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'mt.aliyuncs.com',
            'cn-shenzhen': 'mt.aliyuncs.com',
            'cn-shenzhen-finance-1': 'mt.aliyuncs.com',
            'cn-shenzhen-inner': 'mt.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'mt.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'mt.aliyuncs.com',
            'cn-wuhan': 'mt.aliyuncs.com',
            'cn-yushanfang': 'mt.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'mt.aliyuncs.com',
            'cn-zhangjiakou': 'mt.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'mt.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'mt.aliyuncs.com',
            'eu-central-1': 'mt.aliyuncs.com',
            'eu-west-1': 'mt.aliyuncs.com',
            'eu-west-1-oxs': 'mt.aliyuncs.com',
            'me-east-1': 'mt.aliyuncs.com',
            'rus-west-1-pop': 'mt.aliyuncs.com',
            'us-east-1': 'mt.aliyuncs.com',
            'us-west-1': 'mt.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('alimt', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_resource_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20190102_models.GetResourceResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetResource',
            version='2019-01-02',
            protocol='HTTPS',
            pathname=f'/api/resource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20190102_models.GetResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20190102_models.GetResourceResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetResource',
            version='2019-01-02',
            protocol='HTTPS',
            pathname=f'/api/resource',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20190102_models.GetResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource(self) -> alimt_20190102_models.GetResourceResponse:
        """
        @return: GetResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_with_options(headers, runtime)

    async def get_resource_async(self) -> alimt_20190102_models.GetResourceResponse:
        """
        @return: GetResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_with_options_async(headers, runtime)

    def list_mt_connector_with_options(
        self,
        request: alimt_20190102_models.ListMtConnectorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20190102_models.ListMtConnectorResponse:
        """
        @summary 获取系统模型和AI模型
        
        @param request: ListMtConnectorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMtConnectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMtConnector',
            version='2019-01-02',
            protocol='HTTPS',
            pathname=f'/api/alynx/listMtModels',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20190102_models.ListMtConnectorResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mt_connector_with_options_async(
        self,
        request: alimt_20190102_models.ListMtConnectorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20190102_models.ListMtConnectorResponse:
        """
        @summary 获取系统模型和AI模型
        
        @param request: ListMtConnectorRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMtConnectorResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMtConnector',
            version='2019-01-02',
            protocol='HTTPS',
            pathname=f'/api/alynx/listMtModels',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20190102_models.ListMtConnectorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mt_connector(
        self,
        request: alimt_20190102_models.ListMtConnectorRequest,
    ) -> alimt_20190102_models.ListMtConnectorResponse:
        """
        @summary 获取系统模型和AI模型
        
        @param request: ListMtConnectorRequest
        @return: ListMtConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_mt_connector_with_options(request, headers, runtime)

    async def list_mt_connector_async(
        self,
        request: alimt_20190102_models.ListMtConnectorRequest,
    ) -> alimt_20190102_models.ListMtConnectorResponse:
        """
        @summary 获取系统模型和AI模型
        
        @param request: ListMtConnectorRequest
        @return: ListMtConnectorResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_mt_connector_with_options_async(request, headers, runtime)

    def translate_ecommerce_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20190102_models.TranslateECommerceResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateECommerceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='TranslateECommerce',
            version='2019-01-02',
            protocol='HTTPS',
            pathname=f'/api/translate/web/ecommerce',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20190102_models.TranslateECommerceResponse(),
            self.call_api(params, req, runtime)
        )

    async def translate_ecommerce_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20190102_models.TranslateECommerceResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateECommerceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='TranslateECommerce',
            version='2019-01-02',
            protocol='HTTPS',
            pathname=f'/api/translate/web/ecommerce',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20190102_models.TranslateECommerceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def translate_ecommerce(self) -> alimt_20190102_models.TranslateECommerceResponse:
        """
        @return: TranslateECommerceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.translate_ecommerce_with_options(headers, runtime)

    async def translate_ecommerce_async(self) -> alimt_20190102_models.TranslateECommerceResponse:
        """
        @return: TranslateECommerceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.translate_ecommerce_with_options_async(headers, runtime)

    def translate_general_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20190102_models.TranslateGeneralResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateGeneralResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='TranslateGeneral',
            version='2019-01-02',
            protocol='HTTPS',
            pathname=f'/api/translate/web/general',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20190102_models.TranslateGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    async def translate_general_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> alimt_20190102_models.TranslateGeneralResponse:
        """
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: TranslateGeneralResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='TranslateGeneral',
            version='2019-01-02',
            protocol='HTTPS',
            pathname=f'/api/translate/web/general',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            alimt_20190102_models.TranslateGeneralResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def translate_general(self) -> alimt_20190102_models.TranslateGeneralResponse:
        """
        @return: TranslateGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.translate_general_with_options(headers, runtime)

    async def translate_general_async(self) -> alimt_20190102_models.TranslateGeneralResponse:
        """
        @return: TranslateGeneralResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.translate_general_with_options_async(headers, runtime)
