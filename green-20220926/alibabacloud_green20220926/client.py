# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_green20220926 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
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
            'ap-northeast-1': 'green.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'green.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'green.ap-southeast-1.aliyuncs.com',
            'cn-chengdu': 'green.aliyuncs.com',
            'cn-hongkong': 'green.aliyuncs.com',
            'cn-huhehaote': 'green.aliyuncs.com',
            'cn-qingdao': 'green.aliyuncs.com',
            'cn-zhangjiakou': 'green.aliyuncs.com',
            'eu-central-1': 'green.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'green.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'green.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'green.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'green.aliyuncs.com',
            'cn-shenzhen-finance-1': 'green.aliyuncs.com',
            'cn-shanghai-finance-1': 'green.aliyuncs.com',
            'cn-north-2-gov-1': 'green.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('green', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_answer_sample_with_options(
        self,
        request: main_models.AddAnswerSampleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAnswerSampleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lib_id):
            query['LibId'] = request.lib_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sample_object):
            query['SampleObject'] = request.sample_object
        if not DaraCore.is_null(request.samples):
            query['Samples'] = request.samples
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAnswerSample',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAnswerSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_answer_sample_with_options_async(
        self,
        request: main_models.AddAnswerSampleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAnswerSampleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lib_id):
            query['LibId'] = request.lib_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sample_object):
            query['SampleObject'] = request.sample_object
        if not DaraCore.is_null(request.samples):
            query['Samples'] = request.samples
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAnswerSample',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAnswerSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_answer_sample(
        self,
        request: main_models.AddAnswerSampleRequest,
    ) -> main_models.AddAnswerSampleResponse:
        runtime = RuntimeOptions()
        return self.add_answer_sample_with_options(request, runtime)

    async def add_answer_sample_async(
        self,
        request: main_models.AddAnswerSampleRequest,
    ) -> main_models.AddAnswerSampleResponse:
        runtime = RuntimeOptions()
        return await self.add_answer_sample_with_options_async(request, runtime)

    def add_image_lib_with_options(
        self,
        request: main_models.AddImageLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddImageLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.lib_name):
            body['LibName'] = request.lib_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddImageLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddImageLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_image_lib_with_options_async(
        self,
        request: main_models.AddImageLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddImageLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.lib_name):
            body['LibName'] = request.lib_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddImageLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddImageLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_image_lib(
        self,
        request: main_models.AddImageLibRequest,
    ) -> main_models.AddImageLibResponse:
        runtime = RuntimeOptions()
        return self.add_image_lib_with_options(request, runtime)

    async def add_image_lib_async(
        self,
        request: main_models.AddImageLibRequest,
    ) -> main_models.AddImageLibResponse:
        runtime = RuntimeOptions()
        return await self.add_image_lib_with_options_async(request, runtime)

    def add_images_2lib_with_options(
        self,
        request: main_models.AddImages2LibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddImages2LibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.img_url):
            body['ImgUrl'] = request.img_url
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddImages2Lib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddImages2LibResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_images_2lib_with_options_async(
        self,
        request: main_models.AddImages2LibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddImages2LibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.img_url):
            body['ImgUrl'] = request.img_url
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddImages2Lib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddImages2LibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_images_2lib(
        self,
        request: main_models.AddImages2LibRequest,
    ) -> main_models.AddImages2LibResponse:
        runtime = RuntimeOptions()
        return self.add_images_2lib_with_options(request, runtime)

    async def add_images_2lib_async(
        self,
        request: main_models.AddImages2LibRequest,
    ) -> main_models.AddImages2LibResponse:
        runtime = RuntimeOptions()
        return await self.add_images_2lib_with_options_async(request, runtime)

    def add_keyword_lib_with_options(
        self,
        request: main_models.AddKeywordLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddKeywordLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.keywords):
            body['Keywords'] = request.keywords
        if not DaraCore.is_null(request.keywords_object):
            body['KeywordsObject'] = request.keywords_object
        if not DaraCore.is_null(request.lib_name):
            body['LibName'] = request.lib_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddKeywordLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddKeywordLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_keyword_lib_with_options_async(
        self,
        request: main_models.AddKeywordLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddKeywordLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.keywords):
            body['Keywords'] = request.keywords
        if not DaraCore.is_null(request.keywords_object):
            body['KeywordsObject'] = request.keywords_object
        if not DaraCore.is_null(request.lib_name):
            body['LibName'] = request.lib_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddKeywordLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddKeywordLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_keyword_lib(
        self,
        request: main_models.AddKeywordLibRequest,
    ) -> main_models.AddKeywordLibResponse:
        runtime = RuntimeOptions()
        return self.add_keyword_lib_with_options(request, runtime)

    async def add_keyword_lib_async(
        self,
        request: main_models.AddKeywordLibRequest,
    ) -> main_models.AddKeywordLibResponse:
        runtime = RuntimeOptions()
        return await self.add_keyword_lib_with_options_async(request, runtime)

    def add_keywords_with_options(
        self,
        request: main_models.AddKeywordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddKeywordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.keywords):
            body['Keywords'] = request.keywords
        if not DaraCore.is_null(request.keywords_object):
            body['KeywordsObject'] = request.keywords_object
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddKeywords',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddKeywordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_keywords_with_options_async(
        self,
        request: main_models.AddKeywordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddKeywordsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.keywords):
            body['Keywords'] = request.keywords
        if not DaraCore.is_null(request.keywords_object):
            body['KeywordsObject'] = request.keywords_object
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddKeywords',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddKeywordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_keywords(
        self,
        request: main_models.AddKeywordsRequest,
    ) -> main_models.AddKeywordsResponse:
        runtime = RuntimeOptions()
        return self.add_keywords_with_options(request, runtime)

    async def add_keywords_async(
        self,
        request: main_models.AddKeywordsRequest,
    ) -> main_models.AddKeywordsResponse:
        runtime = RuntimeOptions()
        return await self.add_keywords_with_options_async(request, runtime)

    def add_keywords_to_lib_with_options(
        self,
        request: main_models.AddKeywordsToLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddKeywordsToLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.keywords):
            body['Keywords'] = request.keywords
        if not DaraCore.is_null(request.keywords_object):
            body['KeywordsObject'] = request.keywords_object
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddKeywordsToLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddKeywordsToLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_keywords_to_lib_with_options_async(
        self,
        request: main_models.AddKeywordsToLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddKeywordsToLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.keywords):
            body['Keywords'] = request.keywords
        if not DaraCore.is_null(request.keywords_object):
            body['KeywordsObject'] = request.keywords_object
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddKeywordsToLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddKeywordsToLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_keywords_to_lib(
        self,
        request: main_models.AddKeywordsToLibRequest,
    ) -> main_models.AddKeywordsToLibResponse:
        runtime = RuntimeOptions()
        return self.add_keywords_to_lib_with_options(request, runtime)

    async def add_keywords_to_lib_async(
        self,
        request: main_models.AddKeywordsToLibRequest,
    ) -> main_models.AddKeywordsToLibResponse:
        runtime = RuntimeOptions()
        return await self.add_keywords_to_lib_with_options_async(request, runtime)

    def cancel_stock_oss_check_task_with_options(
        self,
        request: main_models.CancelStockOssCheckTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelStockOssCheckTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelStockOssCheckTask',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelStockOssCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_stock_oss_check_task_with_options_async(
        self,
        request: main_models.CancelStockOssCheckTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelStockOssCheckTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelStockOssCheckTask',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelStockOssCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_stock_oss_check_task(
        self,
        request: main_models.CancelStockOssCheckTaskRequest,
    ) -> main_models.CancelStockOssCheckTaskResponse:
        runtime = RuntimeOptions()
        return self.cancel_stock_oss_check_task_with_options(request, runtime)

    async def cancel_stock_oss_check_task_async(
        self,
        request: main_models.CancelStockOssCheckTaskRequest,
    ) -> main_models.CancelStockOssCheckTaskResponse:
        runtime = RuntimeOptions()
        return await self.cancel_stock_oss_check_task_with_options_async(request, runtime)

    def copy_service_config_with_options(
        self,
        request: main_models.CopyServiceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyServiceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.service_desc):
            body['ServiceDesc'] = request.service_desc
        if not DaraCore.is_null(request.service_name):
            body['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CopyServiceConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyServiceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_service_config_with_options_async(
        self,
        request: main_models.CopyServiceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyServiceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.service_desc):
            body['ServiceDesc'] = request.service_desc
        if not DaraCore.is_null(request.service_name):
            body['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CopyServiceConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyServiceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_service_config(
        self,
        request: main_models.CopyServiceConfigRequest,
    ) -> main_models.CopyServiceConfigResponse:
        runtime = RuntimeOptions()
        return self.copy_service_config_with_options(request, runtime)

    async def copy_service_config_async(
        self,
        request: main_models.CopyServiceConfigRequest,
    ) -> main_models.CopyServiceConfigResponse:
        runtime = RuntimeOptions()
        return await self.copy_service_config_with_options_async(request, runtime)

    def creat_stock_oss_check_task_with_options(
        self,
        request: main_models.CreatStockOssCheckTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatStockOssCheckTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_prefix_filter_config):
            query['BucketPrefixFilterConfig'] = request.bucket_prefix_filter_config
        if not DaraCore.is_null(request.buckets):
            query['Buckets'] = request.buckets
        if not DaraCore.is_null(request.callback_id):
            query['CallbackId'] = request.callback_id
        if not DaraCore.is_null(request.distinct_history_tasks):
            query['DistinctHistoryTasks'] = request.distinct_history_tasks
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.execute_date):
            query['ExecuteDate'] = request.execute_date
        if not DaraCore.is_null(request.execute_time):
            query['ExecuteTime'] = request.execute_time
        if not DaraCore.is_null(request.freeze):
            query['Freeze'] = request.freeze
        if not DaraCore.is_null(request.freeze_high_risk_1):
            query['FreezeHighRisk1'] = request.freeze_high_risk_1
        if not DaraCore.is_null(request.freeze_high_risk_2):
            query['FreezeHighRisk2'] = request.freeze_high_risk_2
        if not DaraCore.is_null(request.freeze_medium_risk_1):
            query['FreezeMediumRisk1'] = request.freeze_medium_risk_1
        if not DaraCore.is_null(request.freeze_medium_risk_2):
            query['FreezeMediumRisk2'] = request.freeze_medium_risk_2
        if not DaraCore.is_null(request.freeze_restore_path):
            query['FreezeRestorePath'] = request.freeze_restore_path
        if not DaraCore.is_null(request.freeze_type):
            query['FreezeType'] = request.freeze_type
        if not DaraCore.is_null(request.is_inc):
            query['IsInc'] = request.is_inc
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.prefix_filter_type):
            query['PrefixFilterType'] = request.prefix_filter_type
        if not DaraCore.is_null(request.prefix_filters):
            query['PrefixFilters'] = request.prefix_filters
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.referer):
            query['Referer'] = request.referer
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scan_limit):
            query['ScanLimit'] = request.scan_limit
        if not DaraCore.is_null(request.scan_no_file_type):
            query['ScanNoFileType'] = request.scan_no_file_type
        if not DaraCore.is_null(request.scan_resource_type):
            query['ScanResourceType'] = request.scan_resource_type
        if not DaraCore.is_null(request.scan_service):
            query['ScanService'] = request.scan_service
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_cycle):
            query['TaskCycle'] = request.task_cycle
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatStockOssCheckTask',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatStockOssCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def creat_stock_oss_check_task_with_options_async(
        self,
        request: main_models.CreatStockOssCheckTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatStockOssCheckTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket_prefix_filter_config):
            query['BucketPrefixFilterConfig'] = request.bucket_prefix_filter_config
        if not DaraCore.is_null(request.buckets):
            query['Buckets'] = request.buckets
        if not DaraCore.is_null(request.callback_id):
            query['CallbackId'] = request.callback_id
        if not DaraCore.is_null(request.distinct_history_tasks):
            query['DistinctHistoryTasks'] = request.distinct_history_tasks
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.execute_date):
            query['ExecuteDate'] = request.execute_date
        if not DaraCore.is_null(request.execute_time):
            query['ExecuteTime'] = request.execute_time
        if not DaraCore.is_null(request.freeze):
            query['Freeze'] = request.freeze
        if not DaraCore.is_null(request.freeze_high_risk_1):
            query['FreezeHighRisk1'] = request.freeze_high_risk_1
        if not DaraCore.is_null(request.freeze_high_risk_2):
            query['FreezeHighRisk2'] = request.freeze_high_risk_2
        if not DaraCore.is_null(request.freeze_medium_risk_1):
            query['FreezeMediumRisk1'] = request.freeze_medium_risk_1
        if not DaraCore.is_null(request.freeze_medium_risk_2):
            query['FreezeMediumRisk2'] = request.freeze_medium_risk_2
        if not DaraCore.is_null(request.freeze_restore_path):
            query['FreezeRestorePath'] = request.freeze_restore_path
        if not DaraCore.is_null(request.freeze_type):
            query['FreezeType'] = request.freeze_type
        if not DaraCore.is_null(request.is_inc):
            query['IsInc'] = request.is_inc
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.prefix_filter_type):
            query['PrefixFilterType'] = request.prefix_filter_type
        if not DaraCore.is_null(request.prefix_filters):
            query['PrefixFilters'] = request.prefix_filters
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.referer):
            query['Referer'] = request.referer
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scan_limit):
            query['ScanLimit'] = request.scan_limit
        if not DaraCore.is_null(request.scan_no_file_type):
            query['ScanNoFileType'] = request.scan_no_file_type
        if not DaraCore.is_null(request.scan_resource_type):
            query['ScanResourceType'] = request.scan_resource_type
        if not DaraCore.is_null(request.scan_service):
            query['ScanService'] = request.scan_service
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_cycle):
            query['TaskCycle'] = request.task_cycle
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatStockOssCheckTask',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatStockOssCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def creat_stock_oss_check_task(
        self,
        request: main_models.CreatStockOssCheckTaskRequest,
    ) -> main_models.CreatStockOssCheckTaskResponse:
        runtime = RuntimeOptions()
        return self.creat_stock_oss_check_task_with_options(request, runtime)

    async def creat_stock_oss_check_task_async(
        self,
        request: main_models.CreatStockOssCheckTaskRequest,
    ) -> main_models.CreatStockOssCheckTaskResponse:
        runtime = RuntimeOptions()
        return await self.creat_stock_oss_check_task_with_options_async(request, runtime)

    def create_answer_lib_with_options(
        self,
        request: main_models.CreateAnswerLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnswerLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.lib_name):
            body['LibName'] = request.lib_name
        if not DaraCore.is_null(request.sample_bucket):
            body['SampleBucket'] = request.sample_bucket
        if not DaraCore.is_null(request.sample_object):
            body['SampleObject'] = request.sample_object
        if not DaraCore.is_null(request.samples):
            body['Samples'] = request.samples
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnswerLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAnswerLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_answer_lib_with_options_async(
        self,
        request: main_models.CreateAnswerLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAnswerLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.lib_name):
            body['LibName'] = request.lib_name
        if not DaraCore.is_null(request.sample_bucket):
            body['SampleBucket'] = request.sample_bucket
        if not DaraCore.is_null(request.sample_object):
            body['SampleObject'] = request.sample_object
        if not DaraCore.is_null(request.samples):
            body['Samples'] = request.samples
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAnswerLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAnswerLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_answer_lib(
        self,
        request: main_models.CreateAnswerLibRequest,
    ) -> main_models.CreateAnswerLibResponse:
        runtime = RuntimeOptions()
        return self.create_answer_lib_with_options(request, runtime)

    async def create_answer_lib_async(
        self,
        request: main_models.CreateAnswerLibRequest,
    ) -> main_models.CreateAnswerLibResponse:
        runtime = RuntimeOptions()
        return await self.create_answer_lib_with_options_async(request, runtime)

    def create_callback_with_options(
        self,
        request: main_models.CreateCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.crypt_type):
            body['CryptType'] = request.crypt_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.scope):
            body['Scope'] = request.scope
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCallback',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_callback_with_options_async(
        self,
        request: main_models.CreateCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.crypt_type):
            body['CryptType'] = request.crypt_type
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.scope):
            body['Scope'] = request.scope
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCallback',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_callback(
        self,
        request: main_models.CreateCallbackRequest,
    ) -> main_models.CreateCallbackResponse:
        runtime = RuntimeOptions()
        return self.create_callback_with_options(request, runtime)

    async def create_callback_async(
        self,
        request: main_models.CreateCallbackRequest,
    ) -> main_models.CreateCallbackResponse:
        runtime = RuntimeOptions()
        return await self.create_callback_with_options_async(request, runtime)

    def create_online_test_with_options(
        self,
        request: main_models.CreateOnlineTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOnlineTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOnlineTest',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOnlineTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_online_test_with_options_async(
        self,
        request: main_models.CreateOnlineTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOnlineTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.data_id):
            query['DataId'] = request.data_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOnlineTest',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOnlineTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_online_test(
        self,
        request: main_models.CreateOnlineTestRequest,
    ) -> main_models.CreateOnlineTestResponse:
        runtime = RuntimeOptions()
        return self.create_online_test_with_options(request, runtime)

    async def create_online_test_async(
        self,
        request: main_models.CreateOnlineTestRequest,
    ) -> main_models.CreateOnlineTestResponse:
        runtime = RuntimeOptions()
        return await self.create_online_test_with_options_async(request, runtime)

    def create_pre_check_with_options(
        self,
        request: main_models.CreatePreCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePreCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.bucket_prefix_filter_config):
            body['BucketPrefixFilterConfig'] = request.bucket_prefix_filter_config
        if not DaraCore.is_null(request.buckets):
            body['Buckets'] = request.buckets
        if not DaraCore.is_null(request.distinct_history_tasks):
            body['DistinctHistoryTasks'] = request.distinct_history_tasks
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.is_inc):
            body['IsInc'] = request.is_inc
        if not DaraCore.is_null(request.media_type):
            body['MediaType'] = request.media_type
        if not DaraCore.is_null(request.prefix_filter_type):
            body['PrefixFilterType'] = request.prefix_filter_type
        if not DaraCore.is_null(request.prefix_filters):
            body['PrefixFilters'] = request.prefix_filters
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.scan_limit):
            body['ScanLimit'] = request.scan_limit
        if not DaraCore.is_null(request.scan_no_file_type):
            body['ScanNoFileType'] = request.scan_no_file_type
        if not DaraCore.is_null(request.scan_service):
            body['ScanService'] = request.scan_service
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePreCheck',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pre_check_with_options_async(
        self,
        request: main_models.CreatePreCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePreCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.bucket_prefix_filter_config):
            body['BucketPrefixFilterConfig'] = request.bucket_prefix_filter_config
        if not DaraCore.is_null(request.buckets):
            body['Buckets'] = request.buckets
        if not DaraCore.is_null(request.distinct_history_tasks):
            body['DistinctHistoryTasks'] = request.distinct_history_tasks
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.is_inc):
            body['IsInc'] = request.is_inc
        if not DaraCore.is_null(request.media_type):
            body['MediaType'] = request.media_type
        if not DaraCore.is_null(request.prefix_filter_type):
            body['PrefixFilterType'] = request.prefix_filter_type
        if not DaraCore.is_null(request.prefix_filters):
            body['PrefixFilters'] = request.prefix_filters
        if not DaraCore.is_null(request.priority):
            body['Priority'] = request.priority
        if not DaraCore.is_null(request.scan_limit):
            body['ScanLimit'] = request.scan_limit
        if not DaraCore.is_null(request.scan_no_file_type):
            body['ScanNoFileType'] = request.scan_no_file_type
        if not DaraCore.is_null(request.scan_service):
            body['ScanService'] = request.scan_service
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePreCheck',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePreCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pre_check(
        self,
        request: main_models.CreatePreCheckRequest,
    ) -> main_models.CreatePreCheckResponse:
        runtime = RuntimeOptions()
        return self.create_pre_check_with_options(request, runtime)

    async def create_pre_check_async(
        self,
        request: main_models.CreatePreCheckRequest,
    ) -> main_models.CreatePreCheckResponse:
        runtime = RuntimeOptions()
        return await self.create_pre_check_with_options_async(request, runtime)

    def delete_answer_lib_with_options(
        self,
        request: main_models.DeleteAnswerLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAnswerLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lib_id):
            query['LibId'] = request.lib_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAnswerLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAnswerLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_answer_lib_with_options_async(
        self,
        request: main_models.DeleteAnswerLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAnswerLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lib_id):
            query['LibId'] = request.lib_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAnswerLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAnswerLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_answer_lib(
        self,
        request: main_models.DeleteAnswerLibRequest,
    ) -> main_models.DeleteAnswerLibResponse:
        runtime = RuntimeOptions()
        return self.delete_answer_lib_with_options(request, runtime)

    async def delete_answer_lib_async(
        self,
        request: main_models.DeleteAnswerLibRequest,
    ) -> main_models.DeleteAnswerLibResponse:
        runtime = RuntimeOptions()
        return await self.delete_answer_lib_with_options_async(request, runtime)

    def delete_answer_sample_with_options(
        self,
        request: main_models.DeleteAnswerSampleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAnswerSampleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.ids):
            body['Ids'] = request.ids
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAnswerSample',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAnswerSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_answer_sample_with_options_async(
        self,
        request: main_models.DeleteAnswerSampleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAnswerSampleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.ids):
            body['Ids'] = request.ids
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAnswerSample',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAnswerSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_answer_sample(
        self,
        request: main_models.DeleteAnswerSampleRequest,
    ) -> main_models.DeleteAnswerSampleResponse:
        runtime = RuntimeOptions()
        return self.delete_answer_sample_with_options(request, runtime)

    async def delete_answer_sample_async(
        self,
        request: main_models.DeleteAnswerSampleRequest,
    ) -> main_models.DeleteAnswerSampleResponse:
        runtime = RuntimeOptions()
        return await self.delete_answer_sample_with_options_async(request, runtime)

    def delete_callback_with_options(
        self,
        request: main_models.DeleteCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCallback',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_callback_with_options_async(
        self,
        request: main_models.DeleteCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCallback',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_callback(
        self,
        request: main_models.DeleteCallbackRequest,
    ) -> main_models.DeleteCallbackResponse:
        runtime = RuntimeOptions()
        return self.delete_callback_with_options(request, runtime)

    async def delete_callback_async(
        self,
        request: main_models.DeleteCallbackRequest,
    ) -> main_models.DeleteCallbackResponse:
        runtime = RuntimeOptions()
        return await self.delete_callback_with_options_async(request, runtime)

    def delete_feature_config_with_options(
        self,
        request: main_models.DeleteFeatureConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFeatureConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.field):
            body['Field'] = request.field
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFeatureConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFeatureConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_feature_config_with_options_async(
        self,
        request: main_models.DeleteFeatureConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFeatureConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.field):
            body['Field'] = request.field
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFeatureConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFeatureConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_feature_config(
        self,
        request: main_models.DeleteFeatureConfigRequest,
    ) -> main_models.DeleteFeatureConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_feature_config_with_options(request, runtime)

    async def delete_feature_config_async(
        self,
        request: main_models.DeleteFeatureConfigRequest,
    ) -> main_models.DeleteFeatureConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_feature_config_with_options_async(request, runtime)

    def delete_images_from_lib_with_options(
        self,
        request: main_models.DeleteImagesFromLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteImagesFromLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.image_ids):
            body['ImageIds'] = request.image_ids
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteImagesFromLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteImagesFromLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_images_from_lib_with_options_async(
        self,
        request: main_models.DeleteImagesFromLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteImagesFromLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.image_ids):
            body['ImageIds'] = request.image_ids
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteImagesFromLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteImagesFromLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_images_from_lib(
        self,
        request: main_models.DeleteImagesFromLibRequest,
    ) -> main_models.DeleteImagesFromLibResponse:
        runtime = RuntimeOptions()
        return self.delete_images_from_lib_with_options(request, runtime)

    async def delete_images_from_lib_async(
        self,
        request: main_models.DeleteImagesFromLibRequest,
    ) -> main_models.DeleteImagesFromLibResponse:
        runtime = RuntimeOptions()
        return await self.delete_images_from_lib_with_options_async(request, runtime)

    def delete_keyword_with_options(
        self,
        request: main_models.DeleteKeywordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKeywordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.keyword_id_list):
            body['KeywordIdList'] = request.keyword_id_list
        if not DaraCore.is_null(request.keyword_ids):
            body['KeywordIds'] = request.keyword_ids
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKeyword',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKeywordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_keyword_with_options_async(
        self,
        request: main_models.DeleteKeywordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKeywordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.keyword_id_list):
            body['KeywordIdList'] = request.keyword_id_list
        if not DaraCore.is_null(request.keyword_ids):
            body['KeywordIds'] = request.keyword_ids
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKeyword',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKeywordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_keyword(
        self,
        request: main_models.DeleteKeywordRequest,
    ) -> main_models.DeleteKeywordResponse:
        runtime = RuntimeOptions()
        return self.delete_keyword_with_options(request, runtime)

    async def delete_keyword_async(
        self,
        request: main_models.DeleteKeywordRequest,
    ) -> main_models.DeleteKeywordResponse:
        runtime = RuntimeOptions()
        return await self.delete_keyword_with_options_async(request, runtime)

    def delete_keyword_lib_with_options(
        self,
        request: main_models.DeleteKeywordLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKeywordLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKeywordLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKeywordLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_keyword_lib_with_options_async(
        self,
        request: main_models.DeleteKeywordLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKeywordLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKeywordLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKeywordLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_keyword_lib(
        self,
        request: main_models.DeleteKeywordLibRequest,
    ) -> main_models.DeleteKeywordLibResponse:
        runtime = RuntimeOptions()
        return self.delete_keyword_lib_with_options(request, runtime)

    async def delete_keyword_lib_async(
        self,
        request: main_models.DeleteKeywordLibRequest,
    ) -> main_models.DeleteKeywordLibResponse:
        runtime = RuntimeOptions()
        return await self.delete_keyword_lib_with_options_async(request, runtime)

    def delete_online_test_with_options(
        self,
        request: main_models.DeleteOnlineTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOnlineTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOnlineTest',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOnlineTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_online_test_with_options_async(
        self,
        request: main_models.DeleteOnlineTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOnlineTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOnlineTest',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOnlineTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_online_test(
        self,
        request: main_models.DeleteOnlineTestRequest,
    ) -> main_models.DeleteOnlineTestResponse:
        runtime = RuntimeOptions()
        return self.delete_online_test_with_options(request, runtime)

    async def delete_online_test_async(
        self,
        request: main_models.DeleteOnlineTestRequest,
    ) -> main_models.DeleteOnlineTestResponse:
        runtime = RuntimeOptions()
        return await self.delete_online_test_with_options_async(request, runtime)

    def describe_online_test_result_with_options(
        self,
        request: main_models.DescribeOnlineTestResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOnlineTestResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOnlineTestResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOnlineTestResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_online_test_result_with_options_async(
        self,
        request: main_models.DescribeOnlineTestResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeOnlineTestResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeOnlineTestResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeOnlineTestResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_online_test_result(
        self,
        request: main_models.DescribeOnlineTestResultRequest,
    ) -> main_models.DescribeOnlineTestResultResponse:
        runtime = RuntimeOptions()
        return self.describe_online_test_result_with_options(request, runtime)

    async def describe_online_test_result_async(
        self,
        request: main_models.DescribeOnlineTestResultRequest,
    ) -> main_models.DescribeOnlineTestResultResponse:
        runtime = RuntimeOptions()
        return await self.describe_online_test_result_with_options_async(request, runtime)

    def export_answer_sample_with_options(
        self,
        request: main_models.ExportAnswerSampleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportAnswerSampleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportAnswerSample',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportAnswerSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_answer_sample_with_options_async(
        self,
        request: main_models.ExportAnswerSampleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportAnswerSampleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportAnswerSample',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportAnswerSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_answer_sample(
        self,
        request: main_models.ExportAnswerSampleRequest,
    ) -> main_models.ExportAnswerSampleResponse:
        runtime = RuntimeOptions()
        return self.export_answer_sample_with_options(request, runtime)

    async def export_answer_sample_async(
        self,
        request: main_models.ExportAnswerSampleRequest,
    ) -> main_models.ExportAnswerSampleResponse:
        runtime = RuntimeOptions()
        return await self.export_answer_sample_with_options_async(request, runtime)

    def export_cip_stats_with_options(
        self,
        request: main_models.ExportCipStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportCipStatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.by_month):
            body['ByMonth'] = request.by_month
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.export_type):
            body['ExportType'] = request.export_type
        if not DaraCore.is_null(request.label):
            body['Label'] = request.label
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_uid):
            body['SubUid'] = request.sub_uid
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportCipStats',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportCipStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_cip_stats_with_options_async(
        self,
        request: main_models.ExportCipStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportCipStatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.by_month):
            body['ByMonth'] = request.by_month
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.export_type):
            body['ExportType'] = request.export_type
        if not DaraCore.is_null(request.label):
            body['Label'] = request.label
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_uid):
            body['SubUid'] = request.sub_uid
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportCipStats',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportCipStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_cip_stats(
        self,
        request: main_models.ExportCipStatsRequest,
    ) -> main_models.ExportCipStatsResponse:
        runtime = RuntimeOptions()
        return self.export_cip_stats_with_options(request, runtime)

    async def export_cip_stats_async(
        self,
        request: main_models.ExportCipStatsRequest,
    ) -> main_models.ExportCipStatsResponse:
        runtime = RuntimeOptions()
        return await self.export_cip_stats_with_options_async(request, runtime)

    def export_keyword_with_options(
        self,
        request: main_models.ExportKeywordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportKeywordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportKeyword',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportKeywordResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_keyword_with_options_async(
        self,
        request: main_models.ExportKeywordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportKeywordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportKeyword',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportKeywordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_keyword(
        self,
        request: main_models.ExportKeywordRequest,
    ) -> main_models.ExportKeywordResponse:
        runtime = RuntimeOptions()
        return self.export_keyword_with_options(request, runtime)

    async def export_keyword_async(
        self,
        request: main_models.ExportKeywordRequest,
    ) -> main_models.ExportKeywordResponse:
        runtime = RuntimeOptions()
        return await self.export_keyword_with_options_async(request, runtime)

    def export_oss_check_stat_with_options(
        self,
        request: main_models.ExportOssCheckStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportOssCheckStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.by_month):
            body['ByMonth'] = request.by_month
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.parent_task_id):
            body['ParentTaskId'] = request.parent_task_id
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportOssCheckStat',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportOssCheckStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_oss_check_stat_with_options_async(
        self,
        request: main_models.ExportOssCheckStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportOssCheckStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.by_month):
            body['ByMonth'] = request.by_month
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.parent_task_id):
            body['ParentTaskId'] = request.parent_task_id
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportOssCheckStat',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportOssCheckStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_oss_check_stat(
        self,
        request: main_models.ExportOssCheckStatRequest,
    ) -> main_models.ExportOssCheckStatResponse:
        runtime = RuntimeOptions()
        return self.export_oss_check_stat_with_options(request, runtime)

    async def export_oss_check_stat_async(
        self,
        request: main_models.ExportOssCheckStatRequest,
    ) -> main_models.ExportOssCheckStatResponse:
        runtime = RuntimeOptions()
        return await self.export_oss_check_stat_with_options_async(request, runtime)

    def export_result_with_options(
        self,
        tmp_req: main_models.ExportResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportResultResponse:
        tmp_req.validate()
        request = main_models.ExportResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.source):
            body['Source'] = request.source
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_result_with_options_async(
        self,
        tmp_req: main_models.ExportResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportResultResponse:
        tmp_req.validate()
        request = main_models.ExportResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.source):
            body['Source'] = request.source
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_result(
        self,
        request: main_models.ExportResultRequest,
    ) -> main_models.ExportResultResponse:
        runtime = RuntimeOptions()
        return self.export_result_with_options(request, runtime)

    async def export_result_async(
        self,
        request: main_models.ExportResultRequest,
    ) -> main_models.ExportResultResponse:
        runtime = RuntimeOptions()
        return await self.export_result_with_options_async(request, runtime)

    def export_scan_result_with_options(
        self,
        tmp_req: main_models.ExportScanResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportScanResultResponse:
        tmp_req.validate()
        request = main_models.ExportScanResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_shrink):
            body['Query'] = request.query_shrink
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportScanResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportScanResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_scan_result_with_options_async(
        self,
        tmp_req: main_models.ExportScanResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportScanResultResponse:
        tmp_req.validate()
        request = main_models.ExportScanResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_shrink):
            body['Query'] = request.query_shrink
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportScanResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportScanResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_scan_result(
        self,
        request: main_models.ExportScanResultRequest,
    ) -> main_models.ExportScanResultResponse:
        runtime = RuntimeOptions()
        return self.export_scan_result_with_options(request, runtime)

    async def export_scan_result_async(
        self,
        request: main_models.ExportScanResultRequest,
    ) -> main_models.ExportScanResultResponse:
        runtime = RuntimeOptions()
        return await self.export_scan_result_with_options_async(request, runtime)

    def export_text_scan_result_with_options(
        self,
        tmp_req: main_models.ExportTextScanResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportTextScanResultResponse:
        tmp_req.validate()
        request = main_models.ExportTextScanResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.query_shrink):
            body['Query'] = request.query_shrink
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportTextScanResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportTextScanResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_text_scan_result_with_options_async(
        self,
        tmp_req: main_models.ExportTextScanResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportTextScanResultResponse:
        tmp_req.validate()
        request = main_models.ExportTextScanResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.query_shrink):
            body['Query'] = request.query_shrink
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExportTextScanResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportTextScanResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_text_scan_result(
        self,
        request: main_models.ExportTextScanResultRequest,
    ) -> main_models.ExportTextScanResultResponse:
        runtime = RuntimeOptions()
        return self.export_text_scan_result_with_options(request, runtime)

    async def export_text_scan_result_async(
        self,
        request: main_models.ExportTextScanResultRequest,
    ) -> main_models.ExportTextScanResultResponse:
        runtime = RuntimeOptions()
        return await self.export_text_scan_result_with_options_async(request, runtime)

    def get_answer_import_progress_with_options(
        self,
        request: main_models.GetAnswerImportProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAnswerImportProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAnswerImportProgress',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAnswerImportProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_answer_import_progress_with_options_async(
        self,
        request: main_models.GetAnswerImportProgressRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAnswerImportProgressResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAnswerImportProgress',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAnswerImportProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_answer_import_progress(
        self,
        request: main_models.GetAnswerImportProgressRequest,
    ) -> main_models.GetAnswerImportProgressResponse:
        runtime = RuntimeOptions()
        return self.get_answer_import_progress_with_options(request, runtime)

    async def get_answer_import_progress_async(
        self,
        request: main_models.GetAnswerImportProgressRequest,
    ) -> main_models.GetAnswerImportProgressResponse:
        runtime = RuntimeOptions()
        return await self.get_answer_import_progress_with_options_async(request, runtime)

    def get_backup_buckets_list_with_options(
        self,
        request: main_models.GetBackupBucketsListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBackupBucketsListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBackupBucketsList',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBackupBucketsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_backup_buckets_list_with_options_async(
        self,
        request: main_models.GetBackupBucketsListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBackupBucketsListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBackupBucketsList',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBackupBucketsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_backup_buckets_list(
        self,
        request: main_models.GetBackupBucketsListRequest,
    ) -> main_models.GetBackupBucketsListResponse:
        runtime = RuntimeOptions()
        return self.get_backup_buckets_list_with_options(request, runtime)

    async def get_backup_buckets_list_async(
        self,
        request: main_models.GetBackupBucketsListRequest,
    ) -> main_models.GetBackupBucketsListResponse:
        runtime = RuntimeOptions()
        return await self.get_backup_buckets_list_with_options_async(request, runtime)

    def get_backup_config_with_options(
        self,
        request: main_models.GetBackupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBackupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBackupConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBackupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_backup_config_with_options_async(
        self,
        request: main_models.GetBackupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBackupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBackupConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBackupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_backup_config(
        self,
        request: main_models.GetBackupConfigRequest,
    ) -> main_models.GetBackupConfigResponse:
        runtime = RuntimeOptions()
        return self.get_backup_config_with_options(request, runtime)

    async def get_backup_config_async(
        self,
        request: main_models.GetBackupConfigRequest,
    ) -> main_models.GetBackupConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_backup_config_with_options_async(request, runtime)

    def get_backup_status_with_options(
        self,
        request: main_models.GetBackupStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBackupStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBackupStatus',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBackupStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_backup_status_with_options_async(
        self,
        request: main_models.GetBackupStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBackupStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBackupStatus',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBackupStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_backup_status(
        self,
        request: main_models.GetBackupStatusRequest,
    ) -> main_models.GetBackupStatusResponse:
        runtime = RuntimeOptions()
        return self.get_backup_status_with_options(request, runtime)

    async def get_backup_status_async(
        self,
        request: main_models.GetBackupStatusRequest,
    ) -> main_models.GetBackupStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_backup_status_with_options_async(request, runtime)

    def get_buckets_list_with_options(
        self,
        request: main_models.GetBucketsListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBucketsListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBucketsList',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBucketsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_buckets_list_with_options_async(
        self,
        request: main_models.GetBucketsListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBucketsListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBucketsList',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBucketsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_buckets_list(
        self,
        request: main_models.GetBucketsListRequest,
    ) -> main_models.GetBucketsListResponse:
        runtime = RuntimeOptions()
        return self.get_buckets_list_with_options(request, runtime)

    async def get_buckets_list_async(
        self,
        request: main_models.GetBucketsListRequest,
    ) -> main_models.GetBucketsListResponse:
        runtime = RuntimeOptions()
        return await self.get_buckets_list_with_options_async(request, runtime)

    def get_cip_stats_with_options(
        self,
        request: main_models.GetCipStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCipStatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        body = {}
        if not DaraCore.is_null(request.by_month):
            body['ByMonth'] = request.by_month
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.label):
            body['Label'] = request.label
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_uid):
            body['SubUid'] = request.sub_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCipStats',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCipStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cip_stats_with_options_async(
        self,
        request: main_models.GetCipStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCipStatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        body = {}
        if not DaraCore.is_null(request.by_month):
            body['ByMonth'] = request.by_month
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.label):
            body['Label'] = request.label
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        if not DaraCore.is_null(request.sub_uid):
            body['SubUid'] = request.sub_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetCipStats',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCipStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cip_stats(
        self,
        request: main_models.GetCipStatsRequest,
    ) -> main_models.GetCipStatsResponse:
        runtime = RuntimeOptions()
        return self.get_cip_stats_with_options(request, runtime)

    async def get_cip_stats_async(
        self,
        request: main_models.GetCipStatsRequest,
    ) -> main_models.GetCipStatsResponse:
        runtime = RuntimeOptions()
        return await self.get_cip_stats_with_options_async(request, runtime)

    def get_execute_time_with_options(
        self,
        request: main_models.GetExecuteTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExecuteTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExecuteTime',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExecuteTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_execute_time_with_options_async(
        self,
        request: main_models.GetExecuteTimeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExecuteTimeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExecuteTime',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExecuteTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_execute_time(
        self,
        request: main_models.GetExecuteTimeRequest,
    ) -> main_models.GetExecuteTimeResponse:
        runtime = RuntimeOptions()
        return self.get_execute_time_with_options(request, runtime)

    async def get_execute_time_async(
        self,
        request: main_models.GetExecuteTimeRequest,
    ) -> main_models.GetExecuteTimeResponse:
        runtime = RuntimeOptions()
        return await self.get_execute_time_with_options_async(request, runtime)

    def get_feature_config_with_options(
        self,
        request: main_models.GetFeatureConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFeatureConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFeatureConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFeatureConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_feature_config_with_options_async(
        self,
        request: main_models.GetFeatureConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFeatureConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetFeatureConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFeatureConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_feature_config(
        self,
        request: main_models.GetFeatureConfigRequest,
    ) -> main_models.GetFeatureConfigResponse:
        runtime = RuntimeOptions()
        return self.get_feature_config_with_options(request, runtime)

    async def get_feature_config_async(
        self,
        request: main_models.GetFeatureConfigRequest,
    ) -> main_models.GetFeatureConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_feature_config_with_options_async(request, runtime)

    def get_image_scene_label_conf_with_options(
        self,
        request: main_models.GetImageSceneLabelConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageSceneLabelConfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageSceneLabelConf',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageSceneLabelConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_scene_label_conf_with_options_async(
        self,
        request: main_models.GetImageSceneLabelConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageSceneLabelConfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageSceneLabelConf',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageSceneLabelConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_scene_label_conf(
        self,
        request: main_models.GetImageSceneLabelConfRequest,
    ) -> main_models.GetImageSceneLabelConfResponse:
        runtime = RuntimeOptions()
        return self.get_image_scene_label_conf_with_options(request, runtime)

    async def get_image_scene_label_conf_async(
        self,
        request: main_models.GetImageSceneLabelConfRequest,
    ) -> main_models.GetImageSceneLabelConfResponse:
        runtime = RuntimeOptions()
        return await self.get_image_scene_label_conf_with_options_async(request, runtime)

    def get_image_scene_label_list_conf_with_options(
        self,
        request: main_models.GetImageSceneLabelListConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageSceneLabelListConfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_service_code):
            query['ImageServiceCode'] = request.image_service_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageSceneLabelListConf',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageSceneLabelListConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_scene_label_list_conf_with_options_async(
        self,
        request: main_models.GetImageSceneLabelListConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetImageSceneLabelListConfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.image_service_code):
            query['ImageServiceCode'] = request.image_service_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetImageSceneLabelListConf',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetImageSceneLabelListConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_scene_label_list_conf(
        self,
        request: main_models.GetImageSceneLabelListConfRequest,
    ) -> main_models.GetImageSceneLabelListConfResponse:
        runtime = RuntimeOptions()
        return self.get_image_scene_label_list_conf_with_options(request, runtime)

    async def get_image_scene_label_list_conf_async(
        self,
        request: main_models.GetImageSceneLabelListConfRequest,
    ) -> main_models.GetImageSceneLabelListConfResponse:
        runtime = RuntimeOptions()
        return await self.get_image_scene_label_list_conf_with_options_async(request, runtime)

    def get_job_name_list_with_options(
        self,
        tmp_req: main_models.GetJobNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobNameListResponse:
        tmp_req.validate()
        request = main_models.GetJobNameListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort_shrink):
            query['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobNameList',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobNameListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_name_list_with_options_async(
        self,
        tmp_req: main_models.GetJobNameListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetJobNameListResponse:
        tmp_req.validate()
        request = main_models.GetJobNameListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort_shrink):
            query['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJobNameList',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobNameListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_name_list(
        self,
        request: main_models.GetJobNameListRequest,
    ) -> main_models.GetJobNameListResponse:
        runtime = RuntimeOptions()
        return self.get_job_name_list_with_options(request, runtime)

    async def get_job_name_list_async(
        self,
        request: main_models.GetJobNameListRequest,
    ) -> main_models.GetJobNameListResponse:
        runtime = RuntimeOptions()
        return await self.get_job_name_list_with_options_async(request, runtime)

    def get_keyword_import_result_with_options(
        self,
        request: main_models.GetKeywordImportResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKeywordImportResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetKeywordImportResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKeywordImportResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_keyword_import_result_with_options_async(
        self,
        request: main_models.GetKeywordImportResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKeywordImportResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetKeywordImportResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKeywordImportResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_keyword_import_result(
        self,
        request: main_models.GetKeywordImportResultRequest,
    ) -> main_models.GetKeywordImportResultResponse:
        runtime = RuntimeOptions()
        return self.get_keyword_import_result_with_options(request, runtime)

    async def get_keyword_import_result_async(
        self,
        request: main_models.GetKeywordImportResultRequest,
    ) -> main_models.GetKeywordImportResultResponse:
        runtime = RuntimeOptions()
        return await self.get_keyword_import_result_with_options_async(request, runtime)

    def get_keyword_lib_with_options(
        self,
        request: main_models.GetKeywordLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKeywordLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetKeywordLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKeywordLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_keyword_lib_with_options_async(
        self,
        request: main_models.GetKeywordLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKeywordLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetKeywordLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKeywordLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_keyword_lib(
        self,
        request: main_models.GetKeywordLibRequest,
    ) -> main_models.GetKeywordLibResponse:
        runtime = RuntimeOptions()
        return self.get_keyword_lib_with_options(request, runtime)

    async def get_keyword_lib_async(
        self,
        request: main_models.GetKeywordLibRequest,
    ) -> main_models.GetKeywordLibResponse:
        runtime = RuntimeOptions()
        return await self.get_keyword_lib_with_options_async(request, runtime)

    def get_oss_check_freeze_result_with_options(
        self,
        tmp_req: main_models.GetOssCheckFreezeResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssCheckFreezeResultResponse:
        tmp_req.validate()
        request = main_models.GetOssCheckFreezeResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.finish_num):
            query['FinishNum'] = request.finish_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort_shrink):
            query['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssCheckFreezeResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssCheckFreezeResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_check_freeze_result_with_options_async(
        self,
        tmp_req: main_models.GetOssCheckFreezeResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssCheckFreezeResultResponse:
        tmp_req.validate()
        request = main_models.GetOssCheckFreezeResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.finish_num):
            query['FinishNum'] = request.finish_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort_shrink):
            query['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssCheckFreezeResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssCheckFreezeResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_check_freeze_result(
        self,
        request: main_models.GetOssCheckFreezeResultRequest,
    ) -> main_models.GetOssCheckFreezeResultResponse:
        runtime = RuntimeOptions()
        return self.get_oss_check_freeze_result_with_options(request, runtime)

    async def get_oss_check_freeze_result_async(
        self,
        request: main_models.GetOssCheckFreezeResultRequest,
    ) -> main_models.GetOssCheckFreezeResultResponse:
        runtime = RuntimeOptions()
        return await self.get_oss_check_freeze_result_with_options_async(request, runtime)

    def get_oss_check_result_detail_with_options(
        self,
        request: main_models.GetOssCheckResultDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssCheckResultDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket):
            query['Bucket'] = request.bucket
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.object):
            query['Object'] = request.object
        if not DaraCore.is_null(request.parent_task_id):
            query['ParentTaskId'] = request.parent_task_id
        if not DaraCore.is_null(request.query_request_id):
            query['QueryRequestId'] = request.query_request_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssCheckResultDetail',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssCheckResultDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_check_result_detail_with_options_async(
        self,
        request: main_models.GetOssCheckResultDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssCheckResultDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bucket):
            query['Bucket'] = request.bucket
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.object):
            query['Object'] = request.object
        if not DaraCore.is_null(request.parent_task_id):
            query['ParentTaskId'] = request.parent_task_id
        if not DaraCore.is_null(request.query_request_id):
            query['QueryRequestId'] = request.query_request_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssCheckResultDetail',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssCheckResultDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_check_result_detail(
        self,
        request: main_models.GetOssCheckResultDetailRequest,
    ) -> main_models.GetOssCheckResultDetailResponse:
        runtime = RuntimeOptions()
        return self.get_oss_check_result_detail_with_options(request, runtime)

    async def get_oss_check_result_detail_async(
        self,
        request: main_models.GetOssCheckResultDetailRequest,
    ) -> main_models.GetOssCheckResultDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_oss_check_result_detail_with_options_async(request, runtime)

    def get_oss_check_stat_with_options(
        self,
        request: main_models.GetOssCheckStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssCheckStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.by_month):
            body['ByMonth'] = request.by_month
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.parent_task_id):
            body['ParentTaskId'] = request.parent_task_id
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOssCheckStat',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssCheckStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_check_stat_with_options_async(
        self,
        request: main_models.GetOssCheckStatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssCheckStatResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.by_month):
            body['ByMonth'] = request.by_month
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.parent_task_id):
            body['ParentTaskId'] = request.parent_task_id
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetOssCheckStat',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssCheckStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_check_stat(
        self,
        request: main_models.GetOssCheckStatRequest,
    ) -> main_models.GetOssCheckStatResponse:
        runtime = RuntimeOptions()
        return self.get_oss_check_stat_with_options(request, runtime)

    async def get_oss_check_stat_async(
        self,
        request: main_models.GetOssCheckStatRequest,
    ) -> main_models.GetOssCheckStatResponse:
        runtime = RuntimeOptions()
        return await self.get_oss_check_stat_with_options_async(request, runtime)

    def get_oss_check_status_with_options(
        self,
        request: main_models.GetOssCheckStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssCheckStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssCheckStatus',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssCheckStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_check_status_with_options_async(
        self,
        request: main_models.GetOssCheckStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssCheckStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssCheckStatus',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssCheckStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_check_status(
        self,
        request: main_models.GetOssCheckStatusRequest,
    ) -> main_models.GetOssCheckStatusResponse:
        runtime = RuntimeOptions()
        return self.get_oss_check_status_with_options(request, runtime)

    async def get_oss_check_status_async(
        self,
        request: main_models.GetOssCheckStatusRequest,
    ) -> main_models.GetOssCheckStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_oss_check_status_with_options_async(request, runtime)

    def get_oss_check_task_info_with_options(
        self,
        request: main_models.GetOssCheckTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssCheckTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.parent_task_id):
            query['ParentTaskId'] = request.parent_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssCheckTaskInfo',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssCheckTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_check_task_info_with_options_async(
        self,
        request: main_models.GetOssCheckTaskInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOssCheckTaskInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.parent_task_id):
            query['ParentTaskId'] = request.parent_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOssCheckTaskInfo',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOssCheckTaskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_check_task_info(
        self,
        request: main_models.GetOssCheckTaskInfoRequest,
    ) -> main_models.GetOssCheckTaskInfoResponse:
        runtime = RuntimeOptions()
        return self.get_oss_check_task_info_with_options(request, runtime)

    async def get_oss_check_task_info_async(
        self,
        request: main_models.GetOssCheckTaskInfoRequest,
    ) -> main_models.GetOssCheckTaskInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_oss_check_task_info_with_options_async(request, runtime)

    def get_scan_num_with_options(
        self,
        request: main_models.GetScanNumRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScanNumResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.buckets):
            query['Buckets'] = request.buckets
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScanNum',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScanNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scan_num_with_options_async(
        self,
        request: main_models.GetScanNumRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScanNumResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.buckets):
            query['Buckets'] = request.buckets
        if not DaraCore.is_null(request.media_type):
            query['MediaType'] = request.media_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScanNum',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScanNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scan_num(
        self,
        request: main_models.GetScanNumRequest,
    ) -> main_models.GetScanNumResponse:
        runtime = RuntimeOptions()
        return self.get_scan_num_with_options(request, runtime)

    async def get_scan_num_async(
        self,
        request: main_models.GetScanNumRequest,
    ) -> main_models.GetScanNumResponse:
        runtime = RuntimeOptions()
        return await self.get_scan_num_with_options_async(request, runtime)

    def get_scan_result_with_options(
        self,
        tmp_req: main_models.GetScanResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScanResultResponse:
        tmp_req.validate()
        request = main_models.GetScanResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_shrink):
            body['Query'] = request.query_shrink
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetScanResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScanResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scan_result_with_options_async(
        self,
        tmp_req: main_models.GetScanResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScanResultResponse:
        tmp_req.validate()
        request = main_models.GetScanResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_shrink):
            body['Query'] = request.query_shrink
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetScanResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScanResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scan_result(
        self,
        request: main_models.GetScanResultRequest,
    ) -> main_models.GetScanResultResponse:
        runtime = RuntimeOptions()
        return self.get_scan_result_with_options(request, runtime)

    async def get_scan_result_async(
        self,
        request: main_models.GetScanResultRequest,
    ) -> main_models.GetScanResultResponse:
        runtime = RuntimeOptions()
        return await self.get_scan_result_with_options_async(request, runtime)

    def get_service_conf_with_options(
        self,
        request: main_models.GetServiceConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceConfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.by_default):
            body['ByDefault'] = request.by_default
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.scene):
            body['Scene'] = request.scene
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceConf',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_conf_with_options_async(
        self,
        request: main_models.GetServiceConfRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceConfResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.by_default):
            body['ByDefault'] = request.by_default
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.scene):
            body['Scene'] = request.scene
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceConf',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_conf(
        self,
        request: main_models.GetServiceConfRequest,
    ) -> main_models.GetServiceConfResponse:
        runtime = RuntimeOptions()
        return self.get_service_conf_with_options(request, runtime)

    async def get_service_conf_async(
        self,
        request: main_models.GetServiceConfRequest,
    ) -> main_models.GetServiceConfResponse:
        runtime = RuntimeOptions()
        return await self.get_service_conf_with_options_async(request, runtime)

    def get_service_config_with_options(
        self,
        request: main_models.GetServiceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_config_with_options_async(
        self,
        request: main_models.GetServiceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_config(
        self,
        request: main_models.GetServiceConfigRequest,
    ) -> main_models.GetServiceConfigResponse:
        runtime = RuntimeOptions()
        return self.get_service_config_with_options(request, runtime)

    async def get_service_config_async(
        self,
        request: main_models.GetServiceConfigRequest,
    ) -> main_models.GetServiceConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_service_config_with_options_async(request, runtime)

    def get_service_label_config_with_options(
        self,
        request: main_models.GetServiceLabelConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceLabelConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceLabelConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceLabelConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_label_config_with_options_async(
        self,
        request: main_models.GetServiceLabelConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceLabelConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceLabelConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceLabelConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_label_config(
        self,
        request: main_models.GetServiceLabelConfigRequest,
    ) -> main_models.GetServiceLabelConfigResponse:
        runtime = RuntimeOptions()
        return self.get_service_label_config_with_options(request, runtime)

    async def get_service_label_config_async(
        self,
        request: main_models.GetServiceLabelConfigRequest,
    ) -> main_models.GetServiceLabelConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_service_label_config_with_options_async(request, runtime)

    def get_stock_oss_check_tasks_list_with_options(
        self,
        tmp_req: main_models.GetStockOssCheckTasksListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStockOssCheckTasksListResponse:
        tmp_req.validate()
        request = main_models.GetStockOssCheckTasksListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.is_inc):
            query['IsInc'] = request.is_inc
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.media_type):
            body['MediaType'] = request.media_type
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStockOssCheckTasksList',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStockOssCheckTasksListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stock_oss_check_tasks_list_with_options_async(
        self,
        tmp_req: main_models.GetStockOssCheckTasksListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStockOssCheckTasksListResponse:
        tmp_req.validate()
        request = main_models.GetStockOssCheckTasksListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.is_inc):
            query['IsInc'] = request.is_inc
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.media_type):
            body['MediaType'] = request.media_type
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetStockOssCheckTasksList',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStockOssCheckTasksListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stock_oss_check_tasks_list(
        self,
        request: main_models.GetStockOssCheckTasksListRequest,
    ) -> main_models.GetStockOssCheckTasksListResponse:
        runtime = RuntimeOptions()
        return self.get_stock_oss_check_tasks_list_with_options(request, runtime)

    async def get_stock_oss_check_tasks_list_async(
        self,
        request: main_models.GetStockOssCheckTasksListRequest,
    ) -> main_models.GetStockOssCheckTasksListResponse:
        runtime = RuntimeOptions()
        return await self.get_stock_oss_check_tasks_list_with_options_async(request, runtime)

    def get_text_scan_result_with_options(
        self,
        tmp_req: main_models.GetTextScanResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTextScanResultResponse:
        tmp_req.validate()
        request = main_models.GetTextScanResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_shrink):
            body['Query'] = request.query_shrink
        if not DaraCore.is_null(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTextScanResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTextScanResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_text_scan_result_with_options_async(
        self,
        tmp_req: main_models.GetTextScanResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTextScanResultResponse:
        tmp_req.validate()
        request = main_models.GetTextScanResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.query):
            request.query_shrink = Utils.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query_shrink):
            body['Query'] = request.query_shrink
        if not DaraCore.is_null(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTextScanResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTextScanResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_text_scan_result(
        self,
        request: main_models.GetTextScanResultRequest,
    ) -> main_models.GetTextScanResultResponse:
        runtime = RuntimeOptions()
        return self.get_text_scan_result_with_options(request, runtime)

    async def get_text_scan_result_async(
        self,
        request: main_models.GetTextScanResultRequest,
    ) -> main_models.GetTextScanResultResponse:
        runtime = RuntimeOptions()
        return await self.get_text_scan_result_with_options_async(request, runtime)

    def get_upload_info_with_options(
        self,
        request: main_models.GetUploadInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadInfo',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upload_info_with_options_async(
        self,
        request: main_models.GetUploadInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadInfo',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upload_info(
        self,
        request: main_models.GetUploadInfoRequest,
    ) -> main_models.GetUploadInfoResponse:
        runtime = RuntimeOptions()
        return self.get_upload_info_with_options(request, runtime)

    async def get_upload_info_async(
        self,
        request: main_models.GetUploadInfoRequest,
    ) -> main_models.GetUploadInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_upload_info_with_options_async(request, runtime)

    def get_upload_link_with_options(
        self,
        request: main_models.GetUploadLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadLinkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.upload_url):
            query['UploadUrl'] = request.upload_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadLink',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upload_link_with_options_async(
        self,
        request: main_models.GetUploadLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadLinkResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.upload_url):
            query['UploadUrl'] = request.upload_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadLink',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upload_link(
        self,
        request: main_models.GetUploadLinkRequest,
    ) -> main_models.GetUploadLinkResponse:
        runtime = RuntimeOptions()
        return self.get_upload_link_with_options(request, runtime)

    async def get_upload_link_async(
        self,
        request: main_models.GetUploadLinkRequest,
    ) -> main_models.GetUploadLinkResponse:
        runtime = RuntimeOptions()
        return await self.get_upload_link_with_options_async(request, runtime)

    def get_user_buy_status_with_options(
        self,
        request: main_models.GetUserBuyStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserBuyStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserBuyStatus',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserBuyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_buy_status_with_options_async(
        self,
        request: main_models.GetUserBuyStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserBuyStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetUserBuyStatus',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserBuyStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_buy_status(
        self,
        request: main_models.GetUserBuyStatusRequest,
    ) -> main_models.GetUserBuyStatusResponse:
        runtime = RuntimeOptions()
        return self.get_user_buy_status_with_options(request, runtime)

    async def get_user_buy_status_async(
        self,
        request: main_models.GetUserBuyStatusRequest,
    ) -> main_models.GetUserBuyStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_user_buy_status_with_options_async(request, runtime)

    def list_answer_lib_with_options(
        self,
        request: main_models.ListAnswerLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAnswerLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnswerLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnswerLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_answer_lib_with_options_async(
        self,
        request: main_models.ListAnswerLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAnswerLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAnswerLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAnswerLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_answer_lib(
        self,
        request: main_models.ListAnswerLibRequest,
    ) -> main_models.ListAnswerLibResponse:
        runtime = RuntimeOptions()
        return self.list_answer_lib_with_options(request, runtime)

    async def list_answer_lib_async(
        self,
        request: main_models.ListAnswerLibRequest,
    ) -> main_models.ListAnswerLibResponse:
        runtime = RuntimeOptions()
        return await self.list_answer_lib_with_options_async(request, runtime)

    def list_callback_with_options(
        self,
        request: main_models.ListCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCallback',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_callback_with_options_async(
        self,
        request: main_models.ListCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCallback',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_callback(
        self,
        request: main_models.ListCallbackRequest,
    ) -> main_models.ListCallbackResponse:
        runtime = RuntimeOptions()
        return self.list_callback_with_options(request, runtime)

    async def list_callback_async(
        self,
        request: main_models.ListCallbackRequest,
    ) -> main_models.ListCallbackResponse:
        runtime = RuntimeOptions()
        return await self.list_callback_with_options_async(request, runtime)

    def list_image_lib_with_options(
        self,
        request: main_models.ListImageLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListImageLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListImageLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImageLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_image_lib_with_options_async(
        self,
        request: main_models.ListImageLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListImageLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListImageLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImageLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_image_lib(
        self,
        request: main_models.ListImageLibRequest,
    ) -> main_models.ListImageLibResponse:
        runtime = RuntimeOptions()
        return self.list_image_lib_with_options(request, runtime)

    async def list_image_lib_async(
        self,
        request: main_models.ListImageLibRequest,
    ) -> main_models.ListImageLibResponse:
        runtime = RuntimeOptions()
        return await self.list_image_lib_with_options_async(request, runtime)

    def list_images_from_lib_with_options(
        self,
        tmp_req: main_models.ListImagesFromLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListImagesFromLibResponse:
        tmp_req.validate()
        request = main_models.ListImagesFromLibShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.img_id):
            body['ImgId'] = request.img_id
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListImagesFromLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImagesFromLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_from_lib_with_options_async(
        self,
        tmp_req: main_models.ListImagesFromLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListImagesFromLibResponse:
        tmp_req.validate()
        request = main_models.ListImagesFromLibShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            body['EndDate'] = request.end_date
        if not DaraCore.is_null(request.img_id):
            body['ImgId'] = request.img_id
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListImagesFromLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImagesFromLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images_from_lib(
        self,
        request: main_models.ListImagesFromLibRequest,
    ) -> main_models.ListImagesFromLibResponse:
        runtime = RuntimeOptions()
        return self.list_images_from_lib_with_options(request, runtime)

    async def list_images_from_lib_async(
        self,
        request: main_models.ListImagesFromLibRequest,
    ) -> main_models.ListImagesFromLibResponse:
        runtime = RuntimeOptions()
        return await self.list_images_from_lib_with_options_async(request, runtime)

    def list_keyword_libs_with_options(
        self,
        request: main_models.ListKeywordLibsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKeywordLibsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKeywordLibs',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKeywordLibsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_keyword_libs_with_options_async(
        self,
        request: main_models.ListKeywordLibsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKeywordLibsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKeywordLibs',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKeywordLibsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_keyword_libs(
        self,
        request: main_models.ListKeywordLibsRequest,
    ) -> main_models.ListKeywordLibsResponse:
        runtime = RuntimeOptions()
        return self.list_keyword_libs_with_options(request, runtime)

    async def list_keyword_libs_async(
        self,
        request: main_models.ListKeywordLibsRequest,
    ) -> main_models.ListKeywordLibsResponse:
        runtime = RuntimeOptions()
        return await self.list_keyword_libs_with_options_async(request, runtime)

    def list_keywords_with_options(
        self,
        tmp_req: main_models.ListKeywordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKeywordsResponse:
        tmp_req.validate()
        request = main_models.ListKeywordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.word):
            body['Word'] = request.word
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListKeywords',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKeywordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_keywords_with_options_async(
        self,
        tmp_req: main_models.ListKeywordsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKeywordsResponse:
        tmp_req.validate()
        request = main_models.ListKeywordsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.word):
            body['Word'] = request.word
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListKeywords',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKeywordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_keywords(
        self,
        request: main_models.ListKeywordsRequest,
    ) -> main_models.ListKeywordsResponse:
        runtime = RuntimeOptions()
        return self.list_keywords_with_options(request, runtime)

    async def list_keywords_async(
        self,
        request: main_models.ListKeywordsRequest,
    ) -> main_models.ListKeywordsResponse:
        runtime = RuntimeOptions()
        return await self.list_keywords_with_options_async(request, runtime)

    def list_oss_check_result_with_options(
        self,
        tmp_req: main_models.ListOssCheckResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOssCheckResultResponse:
        tmp_req.validate()
        request = main_models.ListOssCheckResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.finish_num):
            query['FinishNum'] = request.finish_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort_shrink):
            query['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOssCheckResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOssCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_oss_check_result_with_options_async(
        self,
        tmp_req: main_models.ListOssCheckResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOssCheckResultResponse:
        tmp_req.validate()
        request = main_models.ListOssCheckResultShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.finish_num):
            query['FinishNum'] = request.finish_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort_shrink):
            query['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOssCheckResult',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOssCheckResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_oss_check_result(
        self,
        request: main_models.ListOssCheckResultRequest,
    ) -> main_models.ListOssCheckResultResponse:
        runtime = RuntimeOptions()
        return self.list_oss_check_result_with_options(request, runtime)

    async def list_oss_check_result_async(
        self,
        request: main_models.ListOssCheckResultRequest,
    ) -> main_models.ListOssCheckResultResponse:
        runtime = RuntimeOptions()
        return await self.list_oss_check_result_with_options_async(request, runtime)

    def list_service_configs_with_options(
        self,
        request: main_models.ListServiceConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.classify):
            query['Classify'] = request.classify
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.use_status):
            query['UseStatus'] = request.use_status
        body = {}
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceConfigs',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_configs_with_options_async(
        self,
        request: main_models.ListServiceConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.classify):
            query['Classify'] = request.classify
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.use_status):
            query['UseStatus'] = request.use_status
        body = {}
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceConfigs',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_configs(
        self,
        request: main_models.ListServiceConfigsRequest,
    ) -> main_models.ListServiceConfigsResponse:
        runtime = RuntimeOptions()
        return self.list_service_configs_with_options(request, runtime)

    async def list_service_configs_async(
        self,
        request: main_models.ListServiceConfigsRequest,
    ) -> main_models.ListServiceConfigsResponse:
        runtime = RuntimeOptions()
        return await self.list_service_configs_with_options_async(request, runtime)

    def llm_stream_chat_with_sse(
        self,
        request: main_models.LlmStreamChatRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.LlmStreamChatResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel):
            body['Channel'] = request.channel
        if not DaraCore.is_null(request.messages):
            body['Messages'] = request.messages
        if not DaraCore.is_null(request.temperature):
            body['Temperature'] = request.temperature
        if not DaraCore.is_null(request.top_p):
            body['TopP'] = request.top_p
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LlmStreamChat',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.LlmStreamChatResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def llm_stream_chat_with_sse_async(
        self,
        request: main_models.LlmStreamChatRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.LlmStreamChatResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel):
            body['Channel'] = request.channel
        if not DaraCore.is_null(request.messages):
            body['Messages'] = request.messages
        if not DaraCore.is_null(request.temperature):
            body['Temperature'] = request.temperature
        if not DaraCore.is_null(request.top_p):
            body['TopP'] = request.top_p
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LlmStreamChat',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.LlmStreamChatResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def llm_stream_chat_with_options(
        self,
        request: main_models.LlmStreamChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LlmStreamChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel):
            body['Channel'] = request.channel
        if not DaraCore.is_null(request.messages):
            body['Messages'] = request.messages
        if not DaraCore.is_null(request.temperature):
            body['Temperature'] = request.temperature
        if not DaraCore.is_null(request.top_p):
            body['TopP'] = request.top_p
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LlmStreamChat',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LlmStreamChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def llm_stream_chat_with_options_async(
        self,
        request: main_models.LlmStreamChatRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LlmStreamChatResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.channel):
            body['Channel'] = request.channel
        if not DaraCore.is_null(request.messages):
            body['Messages'] = request.messages
        if not DaraCore.is_null(request.temperature):
            body['Temperature'] = request.temperature
        if not DaraCore.is_null(request.top_p):
            body['TopP'] = request.top_p
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LlmStreamChat',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LlmStreamChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def llm_stream_chat(
        self,
        request: main_models.LlmStreamChatRequest,
    ) -> main_models.LlmStreamChatResponse:
        runtime = RuntimeOptions()
        return self.llm_stream_chat_with_options(request, runtime)

    async def llm_stream_chat_async(
        self,
        request: main_models.LlmStreamChatRequest,
    ) -> main_models.LlmStreamChatResponse:
        runtime = RuntimeOptions()
        return await self.llm_stream_chat_with_options_async(request, runtime)

    def modify_answer_lib_with_options(
        self,
        request: main_models.ModifyAnswerLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAnswerLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lib_id):
            query['LibId'] = request.lib_id
        if not DaraCore.is_null(request.lib_name):
            query['LibName'] = request.lib_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAnswerLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAnswerLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_answer_lib_with_options_async(
        self,
        request: main_models.ModifyAnswerLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyAnswerLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lib_id):
            query['LibId'] = request.lib_id
        if not DaraCore.is_null(request.lib_name):
            query['LibName'] = request.lib_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyAnswerLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyAnswerLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_answer_lib(
        self,
        request: main_models.ModifyAnswerLibRequest,
    ) -> main_models.ModifyAnswerLibResponse:
        runtime = RuntimeOptions()
        return self.modify_answer_lib_with_options(request, runtime)

    async def modify_answer_lib_async(
        self,
        request: main_models.ModifyAnswerLibRequest,
    ) -> main_models.ModifyAnswerLibResponse:
        runtime = RuntimeOptions()
        return await self.modify_answer_lib_with_options_async(request, runtime)

    def modify_callback_with_options(
        self,
        request: main_models.ModifyCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.crypt_type):
            body['CryptType'] = request.crypt_type
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.scope):
            body['Scope'] = request.scope
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCallback',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_callback_with_options_async(
        self,
        request: main_models.ModifyCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.crypt_type):
            body['CryptType'] = request.crypt_type
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.scope):
            body['Scope'] = request.scope
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyCallback',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_callback(
        self,
        request: main_models.ModifyCallbackRequest,
    ) -> main_models.ModifyCallbackResponse:
        runtime = RuntimeOptions()
        return self.modify_callback_with_options(request, runtime)

    async def modify_callback_async(
        self,
        request: main_models.ModifyCallbackRequest,
    ) -> main_models.ModifyCallbackResponse:
        runtime = RuntimeOptions()
        return await self.modify_callback_with_options_async(request, runtime)

    def modify_feature_config_with_options(
        self,
        request: main_models.ModifyFeatureConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFeatureConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.field):
            body['Field'] = request.field
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFeatureConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFeatureConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_feature_config_with_options_async(
        self,
        request: main_models.ModifyFeatureConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyFeatureConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.field):
            body['Field'] = request.field
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyFeatureConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyFeatureConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_feature_config(
        self,
        request: main_models.ModifyFeatureConfigRequest,
    ) -> main_models.ModifyFeatureConfigResponse:
        runtime = RuntimeOptions()
        return self.modify_feature_config_with_options(request, runtime)

    async def modify_feature_config_async(
        self,
        request: main_models.ModifyFeatureConfigRequest,
    ) -> main_models.ModifyFeatureConfigResponse:
        runtime = RuntimeOptions()
        return await self.modify_feature_config_with_options_async(request, runtime)

    def modify_service_info_with_options(
        self,
        request: main_models.ModifyServiceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyServiceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.service_desc):
            body['ServiceDesc'] = request.service_desc
        if not DaraCore.is_null(request.service_name):
            body['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyServiceInfo',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyServiceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_service_info_with_options_async(
        self,
        request: main_models.ModifyServiceInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyServiceInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.service_desc):
            body['ServiceDesc'] = request.service_desc
        if not DaraCore.is_null(request.service_name):
            body['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ModifyServiceInfo',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyServiceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_service_info(
        self,
        request: main_models.ModifyServiceInfoRequest,
    ) -> main_models.ModifyServiceInfoResponse:
        runtime = RuntimeOptions()
        return self.modify_service_info_with_options(request, runtime)

    async def modify_service_info_async(
        self,
        request: main_models.ModifyServiceInfoRequest,
    ) -> main_models.ModifyServiceInfoResponse:
        runtime = RuntimeOptions()
        return await self.modify_service_info_with_options_async(request, runtime)

    def oss_check_result_list_with_options(
        self,
        tmp_req: main_models.OssCheckResultListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OssCheckResultListResponse:
        tmp_req.validate()
        request = main_models.OssCheckResultListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.finish_num):
            query['FinishNum'] = request.finish_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort_shrink):
            query['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OssCheckResultList',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OssCheckResultListResponse(),
            self.call_api(params, req, runtime)
        )

    async def oss_check_result_list_with_options_async(
        self,
        tmp_req: main_models.OssCheckResultListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OssCheckResultListResponse:
        tmp_req.validate()
        request = main_models.OssCheckResultListShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.finish_num):
            query['FinishNum'] = request.finish_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort_shrink):
            query['Sort'] = request.sort_shrink
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OssCheckResultList',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OssCheckResultListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def oss_check_result_list(
        self,
        request: main_models.OssCheckResultListRequest,
    ) -> main_models.OssCheckResultListResponse:
        runtime = RuntimeOptions()
        return self.oss_check_result_list_with_options(request, runtime)

    async def oss_check_result_list_async(
        self,
        request: main_models.OssCheckResultListRequest,
    ) -> main_models.OssCheckResultListResponse:
        runtime = RuntimeOptions()
        return await self.oss_check_result_list_with_options_async(request, runtime)

    def query_answer_sample_by_page_with_options(
        self,
        tmp_req: main_models.QueryAnswerSampleByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAnswerSampleByPageResponse:
        tmp_req.validate()
        request = main_models.QueryAnswerSampleByPageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.answer):
            query['Answer'] = request.answer
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lib_id):
            query['LibId'] = request.lib_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort_shrink):
            query['Sort'] = request.sort_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAnswerSampleByPage',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAnswerSampleByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_answer_sample_by_page_with_options_async(
        self,
        tmp_req: main_models.QueryAnswerSampleByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAnswerSampleByPageResponse:
        tmp_req.validate()
        request = main_models.QueryAnswerSampleByPageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.sort):
            request.sort_shrink = Utils.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not DaraCore.is_null(request.answer):
            query['Answer'] = request.answer
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.lib_id):
            query['LibId'] = request.lib_id
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort_shrink):
            query['Sort'] = request.sort_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAnswerSampleByPage',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAnswerSampleByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_answer_sample_by_page(
        self,
        request: main_models.QueryAnswerSampleByPageRequest,
    ) -> main_models.QueryAnswerSampleByPageResponse:
        runtime = RuntimeOptions()
        return self.query_answer_sample_by_page_with_options(request, runtime)

    async def query_answer_sample_by_page_async(
        self,
        request: main_models.QueryAnswerSampleByPageRequest,
    ) -> main_models.QueryAnswerSampleByPageResponse:
        runtime = RuntimeOptions()
        return await self.query_answer_sample_by_page_with_options_async(request, runtime)

    def query_callback_with_options(
        self,
        request: main_models.QueryCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.check_for_oss):
            body['CheckForOss'] = request.check_for_oss
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryCallback',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_callback_with_options_async(
        self,
        request: main_models.QueryCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.check_for_oss):
            body['CheckForOss'] = request.check_for_oss
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryCallback',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_callback(
        self,
        request: main_models.QueryCallbackRequest,
    ) -> main_models.QueryCallbackResponse:
        runtime = RuntimeOptions()
        return self.query_callback_with_options(request, runtime)

    async def query_callback_async(
        self,
        request: main_models.QueryCallbackRequest,
    ) -> main_models.QueryCallbackResponse:
        runtime = RuntimeOptions()
        return await self.query_callback_with_options_async(request, runtime)

    def query_callback_by_page_with_options(
        self,
        request: main_models.QueryCallbackByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCallbackByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryCallbackByPage',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCallbackByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_callback_by_page_with_options_async(
        self,
        request: main_models.QueryCallbackByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCallbackByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'QueryCallbackByPage',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCallbackByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_callback_by_page(
        self,
        request: main_models.QueryCallbackByPageRequest,
    ) -> main_models.QueryCallbackByPageResponse:
        runtime = RuntimeOptions()
        return self.query_callback_by_page_with_options(request, runtime)

    async def query_callback_by_page_async(
        self,
        request: main_models.QueryCallbackByPageRequest,
    ) -> main_models.QueryCallbackByPageResponse:
        runtime = RuntimeOptions()
        return await self.query_callback_by_page_with_options_async(request, runtime)

    def stop_online_test_with_options(
        self,
        request: main_models.StopOnlineTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopOnlineTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopOnlineTest',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopOnlineTestResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_online_test_with_options_async(
        self,
        request: main_models.StopOnlineTestRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopOnlineTestResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopOnlineTest',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopOnlineTestResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_online_test(
        self,
        request: main_models.StopOnlineTestRequest,
    ) -> main_models.StopOnlineTestResponse:
        runtime = RuntimeOptions()
        return self.stop_online_test_with_options(request, runtime)

    async def stop_online_test_async(
        self,
        request: main_models.StopOnlineTestRequest,
    ) -> main_models.StopOnlineTestResponse:
        runtime = RuntimeOptions()
        return await self.stop_online_test_with_options_async(request, runtime)

    def update_backup_config_with_options(
        self,
        request: main_models.UpdateBackupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBackupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_config):
            query['BackupConfig'] = request.backup_config
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBackupConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBackupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_backup_config_with_options_async(
        self,
        request: main_models.UpdateBackupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateBackupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_config):
            query['BackupConfig'] = request.backup_config
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateBackupConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateBackupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_backup_config(
        self,
        request: main_models.UpdateBackupConfigRequest,
    ) -> main_models.UpdateBackupConfigResponse:
        runtime = RuntimeOptions()
        return self.update_backup_config_with_options(request, runtime)

    async def update_backup_config_async(
        self,
        request: main_models.UpdateBackupConfigRequest,
    ) -> main_models.UpdateBackupConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_backup_config_with_options_async(request, runtime)

    def update_image_lib_with_options(
        self,
        request: main_models.UpdateImageLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateImageLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.free_inspection):
            body['FreeInspection'] = request.free_inspection
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        if not DaraCore.is_null(request.lib_name):
            body['LibName'] = request.lib_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateImageLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateImageLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_image_lib_with_options_async(
        self,
        request: main_models.UpdateImageLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateImageLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.free_inspection):
            body['FreeInspection'] = request.free_inspection
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        if not DaraCore.is_null(request.lib_name):
            body['LibName'] = request.lib_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateImageLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateImageLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_image_lib(
        self,
        request: main_models.UpdateImageLibRequest,
    ) -> main_models.UpdateImageLibResponse:
        runtime = RuntimeOptions()
        return self.update_image_lib_with_options(request, runtime)

    async def update_image_lib_async(
        self,
        request: main_models.UpdateImageLibRequest,
    ) -> main_models.UpdateImageLibResponse:
        runtime = RuntimeOptions()
        return await self.update_image_lib_with_options_async(request, runtime)

    def update_image_lib_free_inspection_with_options(
        self,
        tmp_req: main_models.UpdateImageLibFreeInspectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateImageLibFreeInspectionResponse:
        tmp_req.validate()
        request = main_models.UpdateImageLibFreeInspectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config):
            request.config_shrink = Utils.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.config_shrink):
            body['Config'] = request.config_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateImageLibFreeInspection',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateImageLibFreeInspectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_image_lib_free_inspection_with_options_async(
        self,
        tmp_req: main_models.UpdateImageLibFreeInspectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateImageLibFreeInspectionResponse:
        tmp_req.validate()
        request = main_models.UpdateImageLibFreeInspectionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config):
            request.config_shrink = Utils.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.config_shrink):
            body['Config'] = request.config_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateImageLibFreeInspection',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateImageLibFreeInspectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_image_lib_free_inspection(
        self,
        request: main_models.UpdateImageLibFreeInspectionRequest,
    ) -> main_models.UpdateImageLibFreeInspectionResponse:
        runtime = RuntimeOptions()
        return self.update_image_lib_free_inspection_with_options(request, runtime)

    async def update_image_lib_free_inspection_async(
        self,
        request: main_models.UpdateImageLibFreeInspectionRequest,
    ) -> main_models.UpdateImageLibFreeInspectionResponse:
        runtime = RuntimeOptions()
        return await self.update_image_lib_free_inspection_with_options_async(request, runtime)

    def update_keyword_lib_with_options(
        self,
        request: main_models.UpdateKeywordLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKeywordLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        if not DaraCore.is_null(request.lib_name):
            body['LibName'] = request.lib_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKeywordLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKeywordLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_keyword_lib_with_options_async(
        self,
        request: main_models.UpdateKeywordLibRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKeywordLibResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.lib_id):
            body['LibId'] = request.lib_id
        if not DaraCore.is_null(request.lib_name):
            body['LibName'] = request.lib_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKeywordLib',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKeywordLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_keyword_lib(
        self,
        request: main_models.UpdateKeywordLibRequest,
    ) -> main_models.UpdateKeywordLibResponse:
        runtime = RuntimeOptions()
        return self.update_keyword_lib_with_options(request, runtime)

    async def update_keyword_lib_async(
        self,
        request: main_models.UpdateKeywordLibRequest,
    ) -> main_models.UpdateKeywordLibResponse:
        runtime = RuntimeOptions()
        return await self.update_keyword_lib_with_options_async(request, runtime)

    def update_oss_check_results_batch_feedback_with_options(
        self,
        request: main_models.UpdateOssCheckResultsBatchFeedbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOssCheckResultsBatchFeedbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feedback):
            query['Feedback'] = request.feedback
        if not DaraCore.is_null(request.items):
            query['Items'] = request.items
        if not DaraCore.is_null(request.parent_task_id):
            query['ParentTaskId'] = request.parent_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOssCheckResultsBatchFeedback',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOssCheckResultsBatchFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_oss_check_results_batch_feedback_with_options_async(
        self,
        request: main_models.UpdateOssCheckResultsBatchFeedbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOssCheckResultsBatchFeedbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feedback):
            query['Feedback'] = request.feedback
        if not DaraCore.is_null(request.items):
            query['Items'] = request.items
        if not DaraCore.is_null(request.parent_task_id):
            query['ParentTaskId'] = request.parent_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOssCheckResultsBatchFeedback',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOssCheckResultsBatchFeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_oss_check_results_batch_feedback(
        self,
        request: main_models.UpdateOssCheckResultsBatchFeedbackRequest,
    ) -> main_models.UpdateOssCheckResultsBatchFeedbackResponse:
        runtime = RuntimeOptions()
        return self.update_oss_check_results_batch_feedback_with_options(request, runtime)

    async def update_oss_check_results_batch_feedback_async(
        self,
        request: main_models.UpdateOssCheckResultsBatchFeedbackRequest,
    ) -> main_models.UpdateOssCheckResultsBatchFeedbackResponse:
        runtime = RuntimeOptions()
        return await self.update_oss_check_results_batch_feedback_with_options_async(request, runtime)

    def update_oss_check_results_feed_back_with_options(
        self,
        request: main_models.UpdateOssCheckResultsFeedBackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOssCheckResultsFeedBackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feedback):
            query['Feedback'] = request.feedback
        if not DaraCore.is_null(request.query_request_id):
            query['QueryRequestId'] = request.query_request_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOssCheckResultsFeedBack',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOssCheckResultsFeedBackResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_oss_check_results_feed_back_with_options_async(
        self,
        request: main_models.UpdateOssCheckResultsFeedBackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOssCheckResultsFeedBackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feedback):
            query['Feedback'] = request.feedback
        if not DaraCore.is_null(request.query_request_id):
            query['QueryRequestId'] = request.query_request_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_code):
            query['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOssCheckResultsFeedBack',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOssCheckResultsFeedBackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_oss_check_results_feed_back(
        self,
        request: main_models.UpdateOssCheckResultsFeedBackRequest,
    ) -> main_models.UpdateOssCheckResultsFeedBackResponse:
        runtime = RuntimeOptions()
        return self.update_oss_check_results_feed_back_with_options(request, runtime)

    async def update_oss_check_results_feed_back_async(
        self,
        request: main_models.UpdateOssCheckResultsFeedBackRequest,
    ) -> main_models.UpdateOssCheckResultsFeedBackResponse:
        runtime = RuntimeOptions()
        return await self.update_oss_check_results_feed_back_with_options_async(request, runtime)

    def update_oss_check_results_freeze_with_options(
        self,
        request: main_models.UpdateOssCheckResultsFreezeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOssCheckResultsFreezeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.freeze_items):
            query['FreezeItems'] = request.freeze_items
        if not DaraCore.is_null(request.freeze_restore_path):
            query['FreezeRestorePath'] = request.freeze_restore_path
        if not DaraCore.is_null(request.freeze_type):
            query['FreezeType'] = request.freeze_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOssCheckResultsFreeze',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOssCheckResultsFreezeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_oss_check_results_freeze_with_options_async(
        self,
        request: main_models.UpdateOssCheckResultsFreezeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOssCheckResultsFreezeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.freeze_items):
            query['FreezeItems'] = request.freeze_items
        if not DaraCore.is_null(request.freeze_restore_path):
            query['FreezeRestorePath'] = request.freeze_restore_path
        if not DaraCore.is_null(request.freeze_type):
            query['FreezeType'] = request.freeze_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOssCheckResultsFreeze',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOssCheckResultsFreezeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_oss_check_results_freeze(
        self,
        request: main_models.UpdateOssCheckResultsFreezeRequest,
    ) -> main_models.UpdateOssCheckResultsFreezeResponse:
        runtime = RuntimeOptions()
        return self.update_oss_check_results_freeze_with_options(request, runtime)

    async def update_oss_check_results_freeze_async(
        self,
        request: main_models.UpdateOssCheckResultsFreezeRequest,
    ) -> main_models.UpdateOssCheckResultsFreezeResponse:
        runtime = RuntimeOptions()
        return await self.update_oss_check_results_freeze_with_options_async(request, runtime)

    def update_oss_check_results_unfreeze_with_options(
        self,
        request: main_models.UpdateOssCheckResultsUnfreezeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOssCheckResultsUnfreezeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.freeze_items):
            query['FreezeItems'] = request.freeze_items
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOssCheckResultsUnfreeze',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOssCheckResultsUnfreezeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_oss_check_results_unfreeze_with_options_async(
        self,
        request: main_models.UpdateOssCheckResultsUnfreezeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOssCheckResultsUnfreezeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.freeze_items):
            query['FreezeItems'] = request.freeze_items
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOssCheckResultsUnfreeze',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOssCheckResultsUnfreezeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_oss_check_results_unfreeze(
        self,
        request: main_models.UpdateOssCheckResultsUnfreezeRequest,
    ) -> main_models.UpdateOssCheckResultsUnfreezeResponse:
        runtime = RuntimeOptions()
        return self.update_oss_check_results_unfreeze_with_options(request, runtime)

    async def update_oss_check_results_unfreeze_async(
        self,
        request: main_models.UpdateOssCheckResultsUnfreezeRequest,
    ) -> main_models.UpdateOssCheckResultsUnfreezeResponse:
        runtime = RuntimeOptions()
        return await self.update_oss_check_results_unfreeze_with_options_async(request, runtime)

    def update_scan_result_feedback_with_options(
        self,
        request: main_models.UpdateScanResultFeedbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateScanResultFeedbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.feedback):
            body['Feedback'] = request.feedback
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.query_request_id):
            body['QueryRequestId'] = request.query_request_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScanResultFeedback',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateScanResultFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scan_result_feedback_with_options_async(
        self,
        request: main_models.UpdateScanResultFeedbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateScanResultFeedbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.feedback):
            body['Feedback'] = request.feedback
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.query_request_id):
            body['QueryRequestId'] = request.query_request_id
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.risk_level):
            body['RiskLevel'] = request.risk_level
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScanResultFeedback',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateScanResultFeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scan_result_feedback(
        self,
        request: main_models.UpdateScanResultFeedbackRequest,
    ) -> main_models.UpdateScanResultFeedbackResponse:
        runtime = RuntimeOptions()
        return self.update_scan_result_feedback_with_options(request, runtime)

    async def update_scan_result_feedback_async(
        self,
        request: main_models.UpdateScanResultFeedbackRequest,
    ) -> main_models.UpdateScanResultFeedbackResponse:
        runtime = RuntimeOptions()
        return await self.update_scan_result_feedback_with_options_async(request, runtime)

    def update_service_config_with_options(
        self,
        request: main_models.UpdateServiceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.file_config):
            body['FileConfig'] = request.file_config
        if not DaraCore.is_null(request.keyword_filter_libs):
            body['KeywordFilterLibs'] = request.keyword_filter_libs
        if not DaraCore.is_null(request.keyword_hit_libs):
            body['KeywordHitLibs'] = request.keyword_hit_libs
        if not DaraCore.is_null(request.manual_machine_config):
            body['ManualMachineConfig'] = request.manual_machine_config
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.scene):
            body['Scene'] = request.scene
        if not DaraCore.is_null(request.scene_config):
            body['SceneConfig'] = request.scene_config
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.service_config):
            body['ServiceConfig'] = request.service_config
        if not DaraCore.is_null(request.video_config):
            body['VideoConfig'] = request.video_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_config_with_options_async(
        self,
        request: main_models.UpdateServiceConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.file_config):
            body['FileConfig'] = request.file_config
        if not DaraCore.is_null(request.keyword_filter_libs):
            body['KeywordFilterLibs'] = request.keyword_filter_libs
        if not DaraCore.is_null(request.keyword_hit_libs):
            body['KeywordHitLibs'] = request.keyword_hit_libs
        if not DaraCore.is_null(request.manual_machine_config):
            body['ManualMachineConfig'] = request.manual_machine_config
        if not DaraCore.is_null(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.scene):
            body['Scene'] = request.scene
        if not DaraCore.is_null(request.scene_config):
            body['SceneConfig'] = request.scene_config
        if not DaraCore.is_null(request.service_code):
            body['ServiceCode'] = request.service_code
        if not DaraCore.is_null(request.service_config):
            body['ServiceConfig'] = request.service_config
        if not DaraCore.is_null(request.video_config):
            body['VideoConfig'] = request.video_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceConfig',
            version = '2022-09-26',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_config(
        self,
        request: main_models.UpdateServiceConfigRequest,
    ) -> main_models.UpdateServiceConfigResponse:
        runtime = RuntimeOptions()
        return self.update_service_config_with_options(request, runtime)

    async def update_service_config_async(
        self,
        request: main_models.UpdateServiceConfigRequest,
    ) -> main_models.UpdateServiceConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_service_config_with_options_async(request, runtime)
