# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_nlp_automl20190529 import models as nlp_automl_20190529_models
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
        self._endpoint = self.get_endpoint('nlp-automl', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def predict_model_with_options(
        self,
        request: nlp_automl_20190529_models.PredictModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20190529_models.PredictModelResponse:
        """
        @param request: PredictModelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PredictModelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PredictModel',
            version='2019-05-29',
            protocol='HTTPS',
            pathname=f'/api/automl/predict',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlp_automl_20190529_models.PredictModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def predict_model_with_options_async(
        self,
        request: nlp_automl_20190529_models.PredictModelRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20190529_models.PredictModelResponse:
        """
        @param request: PredictModelRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PredictModelResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PredictModel',
            version='2019-05-29',
            protocol='HTTPS',
            pathname=f'/api/automl/predict',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlp_automl_20190529_models.PredictModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def predict_model(
        self,
        request: nlp_automl_20190529_models.PredictModelRequest,
    ) -> nlp_automl_20190529_models.PredictModelResponse:
        """
        @param request: PredictModelRequest
        @return: PredictModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.predict_model_with_options(request, headers, runtime)

    async def predict_model_async(
        self,
        request: nlp_automl_20190529_models.PredictModelRequest,
    ) -> nlp_automl_20190529_models.PredictModelResponse:
        """
        @param request: PredictModelRequest
        @return: PredictModelResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.predict_model_with_options_async(request, headers, runtime)
