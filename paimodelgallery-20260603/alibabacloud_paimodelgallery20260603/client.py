# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_paimodelgallery20260603 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
    ):
        super().__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'us-west-1': 'paimodelgallery.us-west-1.aliyuncs.com',
            'us-east-1': 'paimodelgallery.us-east-1.aliyuncs.com',
            'eu-central-1': 'paimodelgallery.eu-central-1.aliyuncs.com',
            'cn-wulanchabu': 'paimodelgallery.cn-wulanchabu.aliyuncs.com',
            'cn-shenzhen': 'paimodelgallery.cn-shenzhen.aliyuncs.com',
            'cn-shanghai': 'paimodelgallery.cn-shanghai.aliyuncs.com',
            'cn-hongkong': 'paimodelgallery.cn-hongkong.aliyuncs.com',
            'cn-hangzhou': 'paimodelgallery.cn-hangzhou.aliyuncs.com',
            'cn-guangzhou': 'paimodelgallery.cn-guangzhou.aliyuncs.com',
            'cn-beijing': 'paimodelgallery.cn-beijing.aliyuncs.com',
            'ap-southeast-5': 'paimodelgallery.ap-southeast-5.aliyuncs.com',
            'ap-southeast-3': 'paimodelgallery.ap-southeast-3.aliyuncs.com',
            'ap-southeast-1': 'paimodelgallery.ap-southeast-1.aliyuncs.com',
            'ap-northeast-2': 'paimodelgallery.ap-northeast-2.aliyuncs.com',
            'ap-northeast-1': 'paimodelgallery.ap-northeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('paimodelgallery', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def list_model_gallery_models_with_options(
        self,
        tmp_req: main_models.ListModelGalleryModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelGalleryModelsResponse:
        tmp_req.validate()
        request = main_models.ListModelGalleryModelsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.conditions):
            request.conditions_shrink = Utils.array_to_string_with_specified_style(tmp_req.conditions, 'Conditions', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.collections):
            query['Collections'] = request.collections
        if not DaraCore.is_null(request.compressible):
            query['Compressible'] = request.compressible
        if not DaraCore.is_null(request.conditions_shrink):
            query['Conditions'] = request.conditions_shrink
        if not DaraCore.is_null(request.deep_think):
            query['DeepThink'] = request.deep_think
        if not DaraCore.is_null(request.demonstrable):
            query['Demonstrable'] = request.demonstrable
        if not DaraCore.is_null(request.deployable):
            query['Deployable'] = request.deployable
        if not DaraCore.is_null(request.distillable):
            query['Distillable'] = request.distillable
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.evaluable):
            query['Evaluable'] = request.evaluable
        if not DaraCore.is_null(request.function_call):
            query['FunctionCall'] = request.function_call
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.model_series):
            query['ModelSeries'] = request.model_series
        if not DaraCore.is_null(request.model_type):
            query['ModelType'] = request.model_type
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.origin):
            query['Origin'] = request.origin
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.supported_compression_resource):
            query['SupportedCompressionResource'] = request.supported_compression_resource
        if not DaraCore.is_null(request.supported_distillation_resource):
            query['SupportedDistillationResource'] = request.supported_distillation_resource
        if not DaraCore.is_null(request.supported_evaluation_resource):
            query['SupportedEvaluationResource'] = request.supported_evaluation_resource
        if not DaraCore.is_null(request.supported_inference_resource):
            query['SupportedInferenceResource'] = request.supported_inference_resource
        if not DaraCore.is_null(request.supported_training_resource):
            query['SupportedTrainingResource'] = request.supported_training_resource
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.task):
            query['Task'] = request.task
        if not DaraCore.is_null(request.trainable):
            query['Trainable'] = request.trainable
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelGalleryModels',
            version = '2026-06-03',
            protocol = 'HTTPS',
            pathname = f'/api/v2/modelgallery/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelGalleryModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_gallery_models_with_options_async(
        self,
        tmp_req: main_models.ListModelGalleryModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelGalleryModelsResponse:
        tmp_req.validate()
        request = main_models.ListModelGalleryModelsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.conditions):
            request.conditions_shrink = Utils.array_to_string_with_specified_style(tmp_req.conditions, 'Conditions', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.collections):
            query['Collections'] = request.collections
        if not DaraCore.is_null(request.compressible):
            query['Compressible'] = request.compressible
        if not DaraCore.is_null(request.conditions_shrink):
            query['Conditions'] = request.conditions_shrink
        if not DaraCore.is_null(request.deep_think):
            query['DeepThink'] = request.deep_think
        if not DaraCore.is_null(request.demonstrable):
            query['Demonstrable'] = request.demonstrable
        if not DaraCore.is_null(request.deployable):
            query['Deployable'] = request.deployable
        if not DaraCore.is_null(request.distillable):
            query['Distillable'] = request.distillable
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.evaluable):
            query['Evaluable'] = request.evaluable
        if not DaraCore.is_null(request.function_call):
            query['FunctionCall'] = request.function_call
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.model_series):
            query['ModelSeries'] = request.model_series
        if not DaraCore.is_null(request.model_type):
            query['ModelType'] = request.model_type
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.origin):
            query['Origin'] = request.origin
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.supported_compression_resource):
            query['SupportedCompressionResource'] = request.supported_compression_resource
        if not DaraCore.is_null(request.supported_distillation_resource):
            query['SupportedDistillationResource'] = request.supported_distillation_resource
        if not DaraCore.is_null(request.supported_evaluation_resource):
            query['SupportedEvaluationResource'] = request.supported_evaluation_resource
        if not DaraCore.is_null(request.supported_inference_resource):
            query['SupportedInferenceResource'] = request.supported_inference_resource
        if not DaraCore.is_null(request.supported_training_resource):
            query['SupportedTrainingResource'] = request.supported_training_resource
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.task):
            query['Task'] = request.task
        if not DaraCore.is_null(request.trainable):
            query['Trainable'] = request.trainable
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelGalleryModels',
            version = '2026-06-03',
            protocol = 'HTTPS',
            pathname = f'/api/v2/modelgallery/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelGalleryModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_gallery_models(
        self,
        request: main_models.ListModelGalleryModelsRequest,
    ) -> main_models.ListModelGalleryModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_model_gallery_models_with_options(request, headers, runtime)

    async def list_model_gallery_models_async(
        self,
        request: main_models.ListModelGalleryModelsRequest,
    ) -> main_models.ListModelGalleryModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_model_gallery_models_with_options_async(request, headers, runtime)
