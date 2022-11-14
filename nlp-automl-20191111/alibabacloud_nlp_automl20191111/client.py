# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_nlp_automl20191111 import models as nlp_automl_20191111_models
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

    def create_async_predict_with_options(
        self,
        request: nlp_automl_20191111_models.CreateAsyncPredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.CreateAsyncPredictResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.detail_tag):
            body['DetailTag'] = request.detail_tag
        if not UtilClient.is_unset(request.fetch_content):
            body['FetchContent'] = request.fetch_content
        if not UtilClient.is_unset(request.file_content):
            body['FileContent'] = request.file_content
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_version):
            body['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_version):
            body['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.top_k):
            body['TopK'] = request.top_k
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAsyncPredict',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlp_automl_20191111_models.CreateAsyncPredictResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_async_predict_with_options_async(
        self,
        request: nlp_automl_20191111_models.CreateAsyncPredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.CreateAsyncPredictResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.detail_tag):
            body['DetailTag'] = request.detail_tag
        if not UtilClient.is_unset(request.fetch_content):
            body['FetchContent'] = request.fetch_content
        if not UtilClient.is_unset(request.file_content):
            body['FileContent'] = request.file_content
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_version):
            body['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_version):
            body['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.top_k):
            body['TopK'] = request.top_k
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAsyncPredict',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlp_automl_20191111_models.CreateAsyncPredictResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_async_predict(
        self,
        request: nlp_automl_20191111_models.CreateAsyncPredictRequest,
    ) -> nlp_automl_20191111_models.CreateAsyncPredictResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_async_predict_with_options(request, runtime)

    async def create_async_predict_async(
        self,
        request: nlp_automl_20191111_models.CreateAsyncPredictRequest,
    ) -> nlp_automl_20191111_models.CreateAsyncPredictResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_async_predict_with_options_async(request, runtime)

    def get_async_predict_with_options(
        self,
        request: nlp_automl_20191111_models.GetAsyncPredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.GetAsyncPredictResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncPredict',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlp_automl_20191111_models.GetAsyncPredictResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_async_predict_with_options_async(
        self,
        request: nlp_automl_20191111_models.GetAsyncPredictRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.GetAsyncPredictResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncPredict',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlp_automl_20191111_models.GetAsyncPredictResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_async_predict(
        self,
        request: nlp_automl_20191111_models.GetAsyncPredictRequest,
    ) -> nlp_automl_20191111_models.GetAsyncPredictResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_async_predict_with_options(request, runtime)

    async def get_async_predict_async(
        self,
        request: nlp_automl_20191111_models.GetAsyncPredictRequest,
    ) -> nlp_automl_20191111_models.GetAsyncPredictResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_async_predict_with_options_async(request, runtime)

    def get_predict_result_with_options(
        self,
        request: nlp_automl_20191111_models.GetPredictResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.GetPredictResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.detail_tag):
            body['DetailTag'] = request.detail_tag
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_version):
            body['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.top_k):
            body['TopK'] = request.top_k
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPredictResult',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlp_automl_20191111_models.GetPredictResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_predict_result_with_options_async(
        self,
        request: nlp_automl_20191111_models.GetPredictResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.GetPredictResultResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.detail_tag):
            body['DetailTag'] = request.detail_tag
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.model_version):
            body['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.top_k):
            body['TopK'] = request.top_k
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPredictResult',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlp_automl_20191111_models.GetPredictResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_predict_result(
        self,
        request: nlp_automl_20191111_models.GetPredictResultRequest,
    ) -> nlp_automl_20191111_models.GetPredictResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_predict_result_with_options(request, runtime)

    async def get_predict_result_async(
        self,
        request: nlp_automl_20191111_models.GetPredictResultRequest,
    ) -> nlp_automl_20191111_models.GetPredictResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_predict_result_with_options_async(request, runtime)

    def run_pre_train_service_with_options(
        self,
        request: nlp_automl_20191111_models.RunPreTrainServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.RunPreTrainServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.predict_content):
            body['PredictContent'] = request.predict_content
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_version):
            body['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunPreTrainService',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlp_automl_20191111_models.RunPreTrainServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_pre_train_service_with_options_async(
        self,
        request: nlp_automl_20191111_models.RunPreTrainServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> nlp_automl_20191111_models.RunPreTrainServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.predict_content):
            body['PredictContent'] = request.predict_content
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.service_version):
            body['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunPreTrainService',
            version='2019-11-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            nlp_automl_20191111_models.RunPreTrainServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_pre_train_service(
        self,
        request: nlp_automl_20191111_models.RunPreTrainServiceRequest,
    ) -> nlp_automl_20191111_models.RunPreTrainServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_pre_train_service_with_options(request, runtime)

    async def run_pre_train_service_async(
        self,
        request: nlp_automl_20191111_models.RunPreTrainServiceRequest,
    ) -> nlp_automl_20191111_models.RunPreTrainServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_pre_train_service_with_options_async(request, runtime)
