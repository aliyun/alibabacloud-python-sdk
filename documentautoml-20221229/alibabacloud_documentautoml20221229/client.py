# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_documentautoml20221229 import models as document_automl_20221229_models
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
        self._endpoint = self.get_endpoint('documentautoml', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def predict_classifier_model_with_options(
        self,
        request: document_automl_20221229_models.PredictClassifierModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> document_automl_20221229_models.PredictClassifierModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_prediction):
            query['AutoPrediction'] = request.auto_prediction
        if not UtilClient.is_unset(request.classifier_id):
            query['ClassifierId'] = request.classifier_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PredictClassifierModel',
            version='2022-12-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            document_automl_20221229_models.PredictClassifierModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def predict_classifier_model_with_options_async(
        self,
        request: document_automl_20221229_models.PredictClassifierModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> document_automl_20221229_models.PredictClassifierModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_prediction):
            query['AutoPrediction'] = request.auto_prediction
        if not UtilClient.is_unset(request.classifier_id):
            query['ClassifierId'] = request.classifier_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PredictClassifierModel',
            version='2022-12-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            document_automl_20221229_models.PredictClassifierModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def predict_classifier_model(
        self,
        request: document_automl_20221229_models.PredictClassifierModelRequest,
    ) -> document_automl_20221229_models.PredictClassifierModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.predict_classifier_model_with_options(request, runtime)

    async def predict_classifier_model_async(
        self,
        request: document_automl_20221229_models.PredictClassifierModelRequest,
    ) -> document_automl_20221229_models.PredictClassifierModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.predict_classifier_model_with_options_async(request, runtime)

    def predict_model_with_options(
        self,
        request: document_automl_20221229_models.PredictModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> document_automl_20221229_models.PredictModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.binary_to_text):
            query['BinaryToText'] = request.binary_to_text
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_version):
            query['ModelVersion'] = request.model_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PredictModel',
            version='2022-12-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            document_automl_20221229_models.PredictModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def predict_model_with_options_async(
        self,
        request: document_automl_20221229_models.PredictModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> document_automl_20221229_models.PredictModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.binary_to_text):
            query['BinaryToText'] = request.binary_to_text
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.model_id):
            query['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_version):
            query['ModelVersion'] = request.model_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PredictModel',
            version='2022-12-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            document_automl_20221229_models.PredictModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def predict_model(
        self,
        request: document_automl_20221229_models.PredictModelRequest,
    ) -> document_automl_20221229_models.PredictModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.predict_model_with_options(request, runtime)

    async def predict_model_async(
        self,
        request: document_automl_20221229_models.PredictModelRequest,
    ) -> document_automl_20221229_models.PredictModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.predict_model_with_options_async(request, runtime)

    def predict_template_model_with_options(
        self,
        request: document_automl_20221229_models.PredictTemplateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> document_automl_20221229_models.PredictTemplateModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PredictTemplateModel',
            version='2022-12-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            document_automl_20221229_models.PredictTemplateModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def predict_template_model_with_options_async(
        self,
        request: document_automl_20221229_models.PredictTemplateModelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> document_automl_20221229_models.PredictTemplateModelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PredictTemplateModel',
            version='2022-12-29',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            document_automl_20221229_models.PredictTemplateModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def predict_template_model(
        self,
        request: document_automl_20221229_models.PredictTemplateModelRequest,
    ) -> document_automl_20221229_models.PredictTemplateModelResponse:
        runtime = util_models.RuntimeOptions()
        return self.predict_template_model_with_options(request, runtime)

    async def predict_template_model_async(
        self,
        request: document_automl_20221229_models.PredictTemplateModelRequest,
    ) -> document_automl_20221229_models.PredictTemplateModelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.predict_template_model_with_options_async(request, runtime)
