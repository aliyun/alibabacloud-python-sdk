# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_superappnlp20240930 import models as superapp_nlp_20240930_models
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
        self._endpoint = self.get_endpoint('superappnlp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def nlp_address_normalization_with_options(
        self,
        request: superapp_nlp_20240930_models.NlpAddressNormalizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> superapp_nlp_20240930_models.NlpAddressNormalizationResponse:
        """
        @summary 地址解析
        
        @param request: NlpAddressNormalizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NlpAddressNormalizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city_std_manual):
            query['CityStdManual'] = request.city_std_manual
        if not UtilClient.is_unset(request.city_str):
            query['CityStr'] = request.city_str
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.district_std_manual):
            query['DistrictStdManual'] = request.district_std_manual
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.province_std_manual):
            query['ProvinceStdManual'] = request.province_std_manual
        if not UtilClient.is_unset(request.province_str):
            query['ProvinceStr'] = request.province_str
        if not UtilClient.is_unset(request.query_str):
            query['QueryStr'] = request.query_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NlpAddressNormalization',
            version='2024-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            superapp_nlp_20240930_models.NlpAddressNormalizationResponse(),
            self.call_api(params, req, runtime)
        )

    async def nlp_address_normalization_with_options_async(
        self,
        request: superapp_nlp_20240930_models.NlpAddressNormalizationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> superapp_nlp_20240930_models.NlpAddressNormalizationResponse:
        """
        @summary 地址解析
        
        @param request: NlpAddressNormalizationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: NlpAddressNormalizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.city_std_manual):
            query['CityStdManual'] = request.city_std_manual
        if not UtilClient.is_unset(request.city_str):
            query['CityStr'] = request.city_str
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.district_std_manual):
            query['DistrictStdManual'] = request.district_std_manual
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.province_std_manual):
            query['ProvinceStdManual'] = request.province_std_manual
        if not UtilClient.is_unset(request.province_str):
            query['ProvinceStr'] = request.province_str
        if not UtilClient.is_unset(request.query_str):
            query['QueryStr'] = request.query_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NlpAddressNormalization',
            version='2024-09-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            superapp_nlp_20240930_models.NlpAddressNormalizationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def nlp_address_normalization(
        self,
        request: superapp_nlp_20240930_models.NlpAddressNormalizationRequest,
    ) -> superapp_nlp_20240930_models.NlpAddressNormalizationResponse:
        """
        @summary 地址解析
        
        @param request: NlpAddressNormalizationRequest
        @return: NlpAddressNormalizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.nlp_address_normalization_with_options(request, runtime)

    async def nlp_address_normalization_async(
        self,
        request: superapp_nlp_20240930_models.NlpAddressNormalizationRequest,
    ) -> superapp_nlp_20240930_models.NlpAddressNormalizationResponse:
        """
        @summary 地址解析
        
        @param request: NlpAddressNormalizationRequest
        @return: NlpAddressNormalizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.nlp_address_normalization_with_options_async(request, runtime)
