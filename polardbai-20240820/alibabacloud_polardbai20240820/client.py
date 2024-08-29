# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_polardbai20240820 import models as polardb_ai20240820_models
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
        self._endpoint = self.get_endpoint('polardbai', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def predict_sse_with_options(
        self,
        request: polardb_ai20240820_models.PredictSseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> polardb_ai20240820_models.PredictSseResponse:
        """
        @summary 模型推理（在线，离线）
        
        @param request: PredictSseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PredictSseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['dbName'] = request.db_name
        if not UtilClient.is_unset(request.input):
            body['input'] = request.input
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.model_class):
            body['modelClass'] = request.model_class
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PredictSse',
            version='2024-08-20',
            protocol='HTTPS',
            pathname=f'/v1/openapi/models/predictSse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_ai20240820_models.PredictSseResponse(),
            self.call_api(params, req, runtime)
        )

    async def predict_sse_with_options_async(
        self,
        request: polardb_ai20240820_models.PredictSseRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> polardb_ai20240820_models.PredictSseResponse:
        """
        @summary 模型推理（在线，离线）
        
        @param request: PredictSseRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PredictSseResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.db_name):
            body['dbName'] = request.db_name
        if not UtilClient.is_unset(request.input):
            body['input'] = request.input
        if not UtilClient.is_unset(request.instance_name):
            body['instanceName'] = request.instance_name
        if not UtilClient.is_unset(request.model_class):
            body['modelClass'] = request.model_class
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PredictSse',
            version='2024-08-20',
            protocol='HTTPS',
            pathname=f'/v1/openapi/models/predictSse',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            polardb_ai20240820_models.PredictSseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def predict_sse(
        self,
        request: polardb_ai20240820_models.PredictSseRequest,
    ) -> polardb_ai20240820_models.PredictSseResponse:
        """
        @summary 模型推理（在线，离线）
        
        @param request: PredictSseRequest
        @return: PredictSseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.predict_sse_with_options(request, headers, runtime)

    async def predict_sse_async(
        self,
        request: polardb_ai20240820_models.PredictSseRequest,
    ) -> polardb_ai20240820_models.PredictSseResponse:
        """
        @summary 模型推理（在线，离线）
        
        @param request: PredictSseRequest
        @return: PredictSseResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.predict_sse_with_options_async(request, headers, runtime)
