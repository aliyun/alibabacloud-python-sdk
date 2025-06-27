# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_green20220926 import models as green_20220926_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_answer_sample_with_options(
        self,
        request: green_20220926_models.AddAnswerSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.AddAnswerSampleResponse:
        """
        @summary 添加代答样本
        
        @param request: AddAnswerSampleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddAnswerSampleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lib_id):
            query['LibId'] = request.lib_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sample_object):
            query['SampleObject'] = request.sample_object
        if not UtilClient.is_unset(request.samples):
            query['Samples'] = request.samples
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAnswerSample',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.AddAnswerSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_answer_sample_with_options_async(
        self,
        request: green_20220926_models.AddAnswerSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.AddAnswerSampleResponse:
        """
        @summary 添加代答样本
        
        @param request: AddAnswerSampleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddAnswerSampleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lib_id):
            query['LibId'] = request.lib_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sample_object):
            query['SampleObject'] = request.sample_object
        if not UtilClient.is_unset(request.samples):
            query['Samples'] = request.samples
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAnswerSample',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.AddAnswerSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_answer_sample(
        self,
        request: green_20220926_models.AddAnswerSampleRequest,
    ) -> green_20220926_models.AddAnswerSampleResponse:
        """
        @summary 添加代答样本
        
        @param request: AddAnswerSampleRequest
        @return: AddAnswerSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_answer_sample_with_options(request, runtime)

    async def add_answer_sample_async(
        self,
        request: green_20220926_models.AddAnswerSampleRequest,
    ) -> green_20220926_models.AddAnswerSampleResponse:
        """
        @summary 添加代答样本
        
        @param request: AddAnswerSampleRequest
        @return: AddAnswerSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_answer_sample_with_options_async(request, runtime)

    def add_image_lib_with_options(
        self,
        request: green_20220926_models.AddImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.AddImageLibResponse:
        """
        @summary 创建图库
        
        @param request: AddImageLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddImageLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.lib_name):
            body['LibName'] = request.lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddImageLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.AddImageLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_image_lib_with_options_async(
        self,
        request: green_20220926_models.AddImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.AddImageLibResponse:
        """
        @summary 创建图库
        
        @param request: AddImageLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddImageLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.lib_name):
            body['LibName'] = request.lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddImageLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.AddImageLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_image_lib(
        self,
        request: green_20220926_models.AddImageLibRequest,
    ) -> green_20220926_models.AddImageLibResponse:
        """
        @summary 创建图库
        
        @param request: AddImageLibRequest
        @return: AddImageLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_image_lib_with_options(request, runtime)

    async def add_image_lib_async(
        self,
        request: green_20220926_models.AddImageLibRequest,
    ) -> green_20220926_models.AddImageLibResponse:
        """
        @summary 创建图库
        
        @param request: AddImageLibRequest
        @return: AddImageLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_image_lib_with_options_async(request, runtime)

    def add_images_2lib_with_options(
        self,
        request: green_20220926_models.AddImages2LibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.AddImages2LibResponse:
        """
        @summary 批量添加图片
        
        @param request: AddImages2LibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddImages2LibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.img_url):
            body['ImgUrl'] = request.img_url
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddImages2Lib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.AddImages2LibResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_images_2lib_with_options_async(
        self,
        request: green_20220926_models.AddImages2LibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.AddImages2LibResponse:
        """
        @summary 批量添加图片
        
        @param request: AddImages2LibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddImages2LibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.img_url):
            body['ImgUrl'] = request.img_url
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddImages2Lib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.AddImages2LibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_images_2lib(
        self,
        request: green_20220926_models.AddImages2LibRequest,
    ) -> green_20220926_models.AddImages2LibResponse:
        """
        @summary 批量添加图片
        
        @param request: AddImages2LibRequest
        @return: AddImages2LibResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_images_2lib_with_options(request, runtime)

    async def add_images_2lib_async(
        self,
        request: green_20220926_models.AddImages2LibRequest,
    ) -> green_20220926_models.AddImages2LibResponse:
        """
        @summary 批量添加图片
        
        @param request: AddImages2LibRequest
        @return: AddImages2LibResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_images_2lib_with_options_async(request, runtime)

    def add_keyword_lib_with_options(
        self,
        request: green_20220926_models.AddKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.AddKeywordLibResponse:
        """
        @summary 创建关键词库
        
        @param request: AddKeywordLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddKeywordLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.keywords):
            body['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.keywords_object):
            body['KeywordsObject'] = request.keywords_object
        if not UtilClient.is_unset(request.lib_name):
            body['LibName'] = request.lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddKeywordLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.AddKeywordLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_keyword_lib_with_options_async(
        self,
        request: green_20220926_models.AddKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.AddKeywordLibResponse:
        """
        @summary 创建关键词库
        
        @param request: AddKeywordLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddKeywordLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.keywords):
            body['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.keywords_object):
            body['KeywordsObject'] = request.keywords_object
        if not UtilClient.is_unset(request.lib_name):
            body['LibName'] = request.lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddKeywordLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.AddKeywordLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_keyword_lib(
        self,
        request: green_20220926_models.AddKeywordLibRequest,
    ) -> green_20220926_models.AddKeywordLibResponse:
        """
        @summary 创建关键词库
        
        @param request: AddKeywordLibRequest
        @return: AddKeywordLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_keyword_lib_with_options(request, runtime)

    async def add_keyword_lib_async(
        self,
        request: green_20220926_models.AddKeywordLibRequest,
    ) -> green_20220926_models.AddKeywordLibResponse:
        """
        @summary 创建关键词库
        
        @param request: AddKeywordLibRequest
        @return: AddKeywordLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_keyword_lib_with_options_async(request, runtime)

    def add_keywords_with_options(
        self,
        request: green_20220926_models.AddKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.AddKeywordsResponse:
        """
        @summary 添加关键词
        
        @param request: AddKeywordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddKeywordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.keywords):
            body['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.keywords_object):
            body['KeywordsObject'] = request.keywords_object
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddKeywords',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.AddKeywordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_keywords_with_options_async(
        self,
        request: green_20220926_models.AddKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.AddKeywordsResponse:
        """
        @summary 添加关键词
        
        @param request: AddKeywordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddKeywordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.keywords):
            body['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.keywords_object):
            body['KeywordsObject'] = request.keywords_object
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddKeywords',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.AddKeywordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_keywords(
        self,
        request: green_20220926_models.AddKeywordsRequest,
    ) -> green_20220926_models.AddKeywordsResponse:
        """
        @summary 添加关键词
        
        @param request: AddKeywordsRequest
        @return: AddKeywordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_keywords_with_options(request, runtime)

    async def add_keywords_async(
        self,
        request: green_20220926_models.AddKeywordsRequest,
    ) -> green_20220926_models.AddKeywordsResponse:
        """
        @summary 添加关键词
        
        @param request: AddKeywordsRequest
        @return: AddKeywordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_keywords_with_options_async(request, runtime)

    def add_keywords_to_lib_with_options(
        self,
        request: green_20220926_models.AddKeywordsToLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.AddKeywordsToLibResponse:
        """
        @summary 添加关键词
        
        @param request: AddKeywordsToLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddKeywordsToLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.keywords):
            body['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.keywords_object):
            body['KeywordsObject'] = request.keywords_object
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddKeywordsToLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.AddKeywordsToLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_keywords_to_lib_with_options_async(
        self,
        request: green_20220926_models.AddKeywordsToLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.AddKeywordsToLibResponse:
        """
        @summary 添加关键词
        
        @param request: AddKeywordsToLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddKeywordsToLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.keywords):
            body['Keywords'] = request.keywords
        if not UtilClient.is_unset(request.keywords_object):
            body['KeywordsObject'] = request.keywords_object
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddKeywordsToLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.AddKeywordsToLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_keywords_to_lib(
        self,
        request: green_20220926_models.AddKeywordsToLibRequest,
    ) -> green_20220926_models.AddKeywordsToLibResponse:
        """
        @summary 添加关键词
        
        @param request: AddKeywordsToLibRequest
        @return: AddKeywordsToLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_keywords_to_lib_with_options(request, runtime)

    async def add_keywords_to_lib_async(
        self,
        request: green_20220926_models.AddKeywordsToLibRequest,
    ) -> green_20220926_models.AddKeywordsToLibResponse:
        """
        @summary 添加关键词
        
        @param request: AddKeywordsToLibRequest
        @return: AddKeywordsToLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_keywords_to_lib_with_options_async(request, runtime)

    def cancel_stock_oss_check_task_with_options(
        self,
        request: green_20220926_models.CancelStockOssCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.CancelStockOssCheckTaskResponse:
        """
        @summary 取消oss扫描任务
        
        @param request: CancelStockOssCheckTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelStockOssCheckTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelStockOssCheckTask',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.CancelStockOssCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_stock_oss_check_task_with_options_async(
        self,
        request: green_20220926_models.CancelStockOssCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.CancelStockOssCheckTaskResponse:
        """
        @summary 取消oss扫描任务
        
        @param request: CancelStockOssCheckTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelStockOssCheckTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelStockOssCheckTask',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.CancelStockOssCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_stock_oss_check_task(
        self,
        request: green_20220926_models.CancelStockOssCheckTaskRequest,
    ) -> green_20220926_models.CancelStockOssCheckTaskResponse:
        """
        @summary 取消oss扫描任务
        
        @param request: CancelStockOssCheckTaskRequest
        @return: CancelStockOssCheckTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_stock_oss_check_task_with_options(request, runtime)

    async def cancel_stock_oss_check_task_async(
        self,
        request: green_20220926_models.CancelStockOssCheckTaskRequest,
    ) -> green_20220926_models.CancelStockOssCheckTaskResponse:
        """
        @summary 取消oss扫描任务
        
        @param request: CancelStockOssCheckTaskRequest
        @return: CancelStockOssCheckTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_stock_oss_check_task_with_options_async(request, runtime)

    def copy_service_config_with_options(
        self,
        request: green_20220926_models.CopyServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.CopyServiceConfigResponse:
        """
        @summary 复制服务
        
        @param request: CopyServiceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyServiceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.service_desc):
            body['ServiceDesc'] = request.service_desc
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyServiceConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.CopyServiceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_service_config_with_options_async(
        self,
        request: green_20220926_models.CopyServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.CopyServiceConfigResponse:
        """
        @summary 复制服务
        
        @param request: CopyServiceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CopyServiceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.service_desc):
            body['ServiceDesc'] = request.service_desc
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyServiceConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.CopyServiceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_service_config(
        self,
        request: green_20220926_models.CopyServiceConfigRequest,
    ) -> green_20220926_models.CopyServiceConfigResponse:
        """
        @summary 复制服务
        
        @param request: CopyServiceConfigRequest
        @return: CopyServiceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.copy_service_config_with_options(request, runtime)

    async def copy_service_config_async(
        self,
        request: green_20220926_models.CopyServiceConfigRequest,
    ) -> green_20220926_models.CopyServiceConfigResponse:
        """
        @summary 复制服务
        
        @param request: CopyServiceConfigRequest
        @return: CopyServiceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.copy_service_config_with_options_async(request, runtime)

    def creat_stock_oss_check_task_with_options(
        self,
        request: green_20220926_models.CreatStockOssCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.CreatStockOssCheckTaskResponse:
        """
        @summary 创建oss扫描任务
        
        @param request: CreatStockOssCheckTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatStockOssCheckTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buckets):
            query['Buckets'] = request.buckets
        if not UtilClient.is_unset(request.callback_id):
            query['CallbackId'] = request.callback_id
        if not UtilClient.is_unset(request.distinct_history_tasks):
            query['DistinctHistoryTasks'] = request.distinct_history_tasks
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execute_date):
            query['ExecuteDate'] = request.execute_date
        if not UtilClient.is_unset(request.execute_time):
            query['ExecuteTime'] = request.execute_time
        if not UtilClient.is_unset(request.freeze):
            query['Freeze'] = request.freeze
        if not UtilClient.is_unset(request.freeze_high_risk_1):
            query['FreezeHighRisk1'] = request.freeze_high_risk_1
        if not UtilClient.is_unset(request.freeze_high_risk_2):
            query['FreezeHighRisk2'] = request.freeze_high_risk_2
        if not UtilClient.is_unset(request.freeze_medium_risk_1):
            query['FreezeMediumRisk1'] = request.freeze_medium_risk_1
        if not UtilClient.is_unset(request.freeze_medium_risk_2):
            query['FreezeMediumRisk2'] = request.freeze_medium_risk_2
        if not UtilClient.is_unset(request.freeze_type):
            query['FreezeType'] = request.freeze_type
        if not UtilClient.is_unset(request.is_inc):
            query['IsInc'] = request.is_inc
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.prefix_filter_type):
            query['PrefixFilterType'] = request.prefix_filter_type
        if not UtilClient.is_unset(request.prefix_filters):
            query['PrefixFilters'] = request.prefix_filters
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scan_limit):
            query['ScanLimit'] = request.scan_limit
        if not UtilClient.is_unset(request.scan_no_file_type):
            query['ScanNoFileType'] = request.scan_no_file_type
        if not UtilClient.is_unset(request.scan_resource_type):
            query['ScanResourceType'] = request.scan_resource_type
        if not UtilClient.is_unset(request.scan_service):
            query['ScanService'] = request.scan_service
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_cycle):
            query['TaskCycle'] = request.task_cycle
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatStockOssCheckTask',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.CreatStockOssCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def creat_stock_oss_check_task_with_options_async(
        self,
        request: green_20220926_models.CreatStockOssCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.CreatStockOssCheckTaskResponse:
        """
        @summary 创建oss扫描任务
        
        @param request: CreatStockOssCheckTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatStockOssCheckTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buckets):
            query['Buckets'] = request.buckets
        if not UtilClient.is_unset(request.callback_id):
            query['CallbackId'] = request.callback_id
        if not UtilClient.is_unset(request.distinct_history_tasks):
            query['DistinctHistoryTasks'] = request.distinct_history_tasks
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.execute_date):
            query['ExecuteDate'] = request.execute_date
        if not UtilClient.is_unset(request.execute_time):
            query['ExecuteTime'] = request.execute_time
        if not UtilClient.is_unset(request.freeze):
            query['Freeze'] = request.freeze
        if not UtilClient.is_unset(request.freeze_high_risk_1):
            query['FreezeHighRisk1'] = request.freeze_high_risk_1
        if not UtilClient.is_unset(request.freeze_high_risk_2):
            query['FreezeHighRisk2'] = request.freeze_high_risk_2
        if not UtilClient.is_unset(request.freeze_medium_risk_1):
            query['FreezeMediumRisk1'] = request.freeze_medium_risk_1
        if not UtilClient.is_unset(request.freeze_medium_risk_2):
            query['FreezeMediumRisk2'] = request.freeze_medium_risk_2
        if not UtilClient.is_unset(request.freeze_type):
            query['FreezeType'] = request.freeze_type
        if not UtilClient.is_unset(request.is_inc):
            query['IsInc'] = request.is_inc
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.prefix_filter_type):
            query['PrefixFilterType'] = request.prefix_filter_type
        if not UtilClient.is_unset(request.prefix_filters):
            query['PrefixFilters'] = request.prefix_filters
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scan_limit):
            query['ScanLimit'] = request.scan_limit
        if not UtilClient.is_unset(request.scan_no_file_type):
            query['ScanNoFileType'] = request.scan_no_file_type
        if not UtilClient.is_unset(request.scan_resource_type):
            query['ScanResourceType'] = request.scan_resource_type
        if not UtilClient.is_unset(request.scan_service):
            query['ScanService'] = request.scan_service
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_cycle):
            query['TaskCycle'] = request.task_cycle
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatStockOssCheckTask',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.CreatStockOssCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def creat_stock_oss_check_task(
        self,
        request: green_20220926_models.CreatStockOssCheckTaskRequest,
    ) -> green_20220926_models.CreatStockOssCheckTaskResponse:
        """
        @summary 创建oss扫描任务
        
        @param request: CreatStockOssCheckTaskRequest
        @return: CreatStockOssCheckTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.creat_stock_oss_check_task_with_options(request, runtime)

    async def creat_stock_oss_check_task_async(
        self,
        request: green_20220926_models.CreatStockOssCheckTaskRequest,
    ) -> green_20220926_models.CreatStockOssCheckTaskResponse:
        """
        @summary 创建oss扫描任务
        
        @param request: CreatStockOssCheckTaskRequest
        @return: CreatStockOssCheckTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.creat_stock_oss_check_task_with_options_async(request, runtime)

    def create_answer_lib_with_options(
        self,
        request: green_20220926_models.CreateAnswerLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.CreateAnswerLibResponse:
        """
        @summary 创建代答库
        
        @param request: CreateAnswerLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAnswerLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.lib_name):
            body['LibName'] = request.lib_name
        if not UtilClient.is_unset(request.sample_bucket):
            body['SampleBucket'] = request.sample_bucket
        if not UtilClient.is_unset(request.sample_object):
            body['SampleObject'] = request.sample_object
        if not UtilClient.is_unset(request.samples):
            body['Samples'] = request.samples
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAnswerLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.CreateAnswerLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_answer_lib_with_options_async(
        self,
        request: green_20220926_models.CreateAnswerLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.CreateAnswerLibResponse:
        """
        @summary 创建代答库
        
        @param request: CreateAnswerLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAnswerLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.lib_name):
            body['LibName'] = request.lib_name
        if not UtilClient.is_unset(request.sample_bucket):
            body['SampleBucket'] = request.sample_bucket
        if not UtilClient.is_unset(request.sample_object):
            body['SampleObject'] = request.sample_object
        if not UtilClient.is_unset(request.samples):
            body['Samples'] = request.samples
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAnswerLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.CreateAnswerLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_answer_lib(
        self,
        request: green_20220926_models.CreateAnswerLibRequest,
    ) -> green_20220926_models.CreateAnswerLibResponse:
        """
        @summary 创建代答库
        
        @param request: CreateAnswerLibRequest
        @return: CreateAnswerLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_answer_lib_with_options(request, runtime)

    async def create_answer_lib_async(
        self,
        request: green_20220926_models.CreateAnswerLibRequest,
    ) -> green_20220926_models.CreateAnswerLibResponse:
        """
        @summary 创建代答库
        
        @param request: CreateAnswerLibRequest
        @return: CreateAnswerLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_answer_lib_with_options_async(request, runtime)

    def create_callback_with_options(
        self,
        request: green_20220926_models.CreateCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.CreateCallbackResponse:
        """
        @summary 新建消息通知
        
        @param request: CreateCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.crypt_type):
            body['CryptType'] = request.crypt_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.scope):
            body['Scope'] = request.scope
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCallback',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.CreateCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_callback_with_options_async(
        self,
        request: green_20220926_models.CreateCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.CreateCallbackResponse:
        """
        @summary 新建消息通知
        
        @param request: CreateCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.crypt_type):
            body['CryptType'] = request.crypt_type
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.scope):
            body['Scope'] = request.scope
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCallback',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.CreateCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_callback(
        self,
        request: green_20220926_models.CreateCallbackRequest,
    ) -> green_20220926_models.CreateCallbackResponse:
        """
        @summary 新建消息通知
        
        @param request: CreateCallbackRequest
        @return: CreateCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_callback_with_options(request, runtime)

    async def create_callback_async(
        self,
        request: green_20220926_models.CreateCallbackRequest,
    ) -> green_20220926_models.CreateCallbackResponse:
        """
        @summary 新建消息通知
        
        @param request: CreateCallbackRequest
        @return: CreateCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_callback_with_options_async(request, runtime)

    def create_pre_check_with_options(
        self,
        request: green_20220926_models.CreatePreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.CreatePreCheckResponse:
        """
        @summary 创建oss扫描任务前检查
        
        @param request: CreatePreCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePreCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.buckets):
            body['Buckets'] = request.buckets
        if not UtilClient.is_unset(request.distinct_history_tasks):
            body['DistinctHistoryTasks'] = request.distinct_history_tasks
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.is_inc):
            body['IsInc'] = request.is_inc
        if not UtilClient.is_unset(request.media_type):
            body['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.prefix_filter_type):
            body['PrefixFilterType'] = request.prefix_filter_type
        if not UtilClient.is_unset(request.prefix_filters):
            body['PrefixFilters'] = request.prefix_filters
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.scan_limit):
            body['ScanLimit'] = request.scan_limit
        if not UtilClient.is_unset(request.scan_no_file_type):
            body['ScanNoFileType'] = request.scan_no_file_type
        if not UtilClient.is_unset(request.scan_service):
            body['ScanService'] = request.scan_service
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePreCheck',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.CreatePreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pre_check_with_options_async(
        self,
        request: green_20220926_models.CreatePreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.CreatePreCheckResponse:
        """
        @summary 创建oss扫描任务前检查
        
        @param request: CreatePreCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePreCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.buckets):
            body['Buckets'] = request.buckets
        if not UtilClient.is_unset(request.distinct_history_tasks):
            body['DistinctHistoryTasks'] = request.distinct_history_tasks
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.is_inc):
            body['IsInc'] = request.is_inc
        if not UtilClient.is_unset(request.media_type):
            body['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.prefix_filter_type):
            body['PrefixFilterType'] = request.prefix_filter_type
        if not UtilClient.is_unset(request.prefix_filters):
            body['PrefixFilters'] = request.prefix_filters
        if not UtilClient.is_unset(request.priority):
            body['Priority'] = request.priority
        if not UtilClient.is_unset(request.scan_limit):
            body['ScanLimit'] = request.scan_limit
        if not UtilClient.is_unset(request.scan_no_file_type):
            body['ScanNoFileType'] = request.scan_no_file_type
        if not UtilClient.is_unset(request.scan_service):
            body['ScanService'] = request.scan_service
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePreCheck',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.CreatePreCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pre_check(
        self,
        request: green_20220926_models.CreatePreCheckRequest,
    ) -> green_20220926_models.CreatePreCheckResponse:
        """
        @summary 创建oss扫描任务前检查
        
        @param request: CreatePreCheckRequest
        @return: CreatePreCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_pre_check_with_options(request, runtime)

    async def create_pre_check_async(
        self,
        request: green_20220926_models.CreatePreCheckRequest,
    ) -> green_20220926_models.CreatePreCheckResponse:
        """
        @summary 创建oss扫描任务前检查
        
        @param request: CreatePreCheckRequest
        @return: CreatePreCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_pre_check_with_options_async(request, runtime)

    def delete_answer_lib_with_options(
        self,
        request: green_20220926_models.DeleteAnswerLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.DeleteAnswerLibResponse:
        """
        @summary 删除代答库
        
        @param request: DeleteAnswerLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAnswerLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lib_id):
            query['LibId'] = request.lib_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAnswerLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.DeleteAnswerLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_answer_lib_with_options_async(
        self,
        request: green_20220926_models.DeleteAnswerLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.DeleteAnswerLibResponse:
        """
        @summary 删除代答库
        
        @param request: DeleteAnswerLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAnswerLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lib_id):
            query['LibId'] = request.lib_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAnswerLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.DeleteAnswerLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_answer_lib(
        self,
        request: green_20220926_models.DeleteAnswerLibRequest,
    ) -> green_20220926_models.DeleteAnswerLibResponse:
        """
        @summary 删除代答库
        
        @param request: DeleteAnswerLibRequest
        @return: DeleteAnswerLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_answer_lib_with_options(request, runtime)

    async def delete_answer_lib_async(
        self,
        request: green_20220926_models.DeleteAnswerLibRequest,
    ) -> green_20220926_models.DeleteAnswerLibResponse:
        """
        @summary 删除代答库
        
        @param request: DeleteAnswerLibRequest
        @return: DeleteAnswerLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_answer_lib_with_options_async(request, runtime)

    def delete_answer_sample_with_options(
        self,
        request: green_20220926_models.DeleteAnswerSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.DeleteAnswerSampleResponse:
        """
        @summary 删除代答答案
        
        @param request: DeleteAnswerSampleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAnswerSampleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.ids):
            body['Ids'] = request.ids
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAnswerSample',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.DeleteAnswerSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_answer_sample_with_options_async(
        self,
        request: green_20220926_models.DeleteAnswerSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.DeleteAnswerSampleResponse:
        """
        @summary 删除代答答案
        
        @param request: DeleteAnswerSampleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAnswerSampleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.ids):
            body['Ids'] = request.ids
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAnswerSample',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.DeleteAnswerSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_answer_sample(
        self,
        request: green_20220926_models.DeleteAnswerSampleRequest,
    ) -> green_20220926_models.DeleteAnswerSampleResponse:
        """
        @summary 删除代答答案
        
        @param request: DeleteAnswerSampleRequest
        @return: DeleteAnswerSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_answer_sample_with_options(request, runtime)

    async def delete_answer_sample_async(
        self,
        request: green_20220926_models.DeleteAnswerSampleRequest,
    ) -> green_20220926_models.DeleteAnswerSampleResponse:
        """
        @summary 删除代答答案
        
        @param request: DeleteAnswerSampleRequest
        @return: DeleteAnswerSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_answer_sample_with_options_async(request, runtime)

    def delete_callback_with_options(
        self,
        request: green_20220926_models.DeleteCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.DeleteCallbackResponse:
        """
        @summary 删除消息通知
        
        @param request: DeleteCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCallback',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.DeleteCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_callback_with_options_async(
        self,
        request: green_20220926_models.DeleteCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.DeleteCallbackResponse:
        """
        @summary 删除消息通知
        
        @param request: DeleteCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCallback',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.DeleteCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_callback(
        self,
        request: green_20220926_models.DeleteCallbackRequest,
    ) -> green_20220926_models.DeleteCallbackResponse:
        """
        @summary 删除消息通知
        
        @param request: DeleteCallbackRequest
        @return: DeleteCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_callback_with_options(request, runtime)

    async def delete_callback_async(
        self,
        request: green_20220926_models.DeleteCallbackRequest,
    ) -> green_20220926_models.DeleteCallbackResponse:
        """
        @summary 删除消息通知
        
        @param request: DeleteCallbackRequest
        @return: DeleteCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_callback_with_options_async(request, runtime)

    def delete_feature_config_with_options(
        self,
        request: green_20220926_models.DeleteFeatureConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.DeleteFeatureConfigResponse:
        """
        @summary Delete feature configuration
        
        @param request: DeleteFeatureConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFeatureConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.field):
            body['Field'] = request.field
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFeatureConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.DeleteFeatureConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_feature_config_with_options_async(
        self,
        request: green_20220926_models.DeleteFeatureConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.DeleteFeatureConfigResponse:
        """
        @summary Delete feature configuration
        
        @param request: DeleteFeatureConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteFeatureConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.field):
            body['Field'] = request.field
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteFeatureConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.DeleteFeatureConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_feature_config(
        self,
        request: green_20220926_models.DeleteFeatureConfigRequest,
    ) -> green_20220926_models.DeleteFeatureConfigResponse:
        """
        @summary Delete feature configuration
        
        @param request: DeleteFeatureConfigRequest
        @return: DeleteFeatureConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_feature_config_with_options(request, runtime)

    async def delete_feature_config_async(
        self,
        request: green_20220926_models.DeleteFeatureConfigRequest,
    ) -> green_20220926_models.DeleteFeatureConfigResponse:
        """
        @summary Delete feature configuration
        
        @param request: DeleteFeatureConfigRequest
        @return: DeleteFeatureConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_feature_config_with_options_async(request, runtime)

    def delete_images_from_lib_with_options(
        self,
        request: green_20220926_models.DeleteImagesFromLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.DeleteImagesFromLibResponse:
        """
        @summary 批量删除
        
        @param request: DeleteImagesFromLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteImagesFromLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.image_ids):
            body['ImageIds'] = request.image_ids
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteImagesFromLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.DeleteImagesFromLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_images_from_lib_with_options_async(
        self,
        request: green_20220926_models.DeleteImagesFromLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.DeleteImagesFromLibResponse:
        """
        @summary 批量删除
        
        @param request: DeleteImagesFromLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteImagesFromLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.image_ids):
            body['ImageIds'] = request.image_ids
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteImagesFromLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.DeleteImagesFromLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_images_from_lib(
        self,
        request: green_20220926_models.DeleteImagesFromLibRequest,
    ) -> green_20220926_models.DeleteImagesFromLibResponse:
        """
        @summary 批量删除
        
        @param request: DeleteImagesFromLibRequest
        @return: DeleteImagesFromLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_images_from_lib_with_options(request, runtime)

    async def delete_images_from_lib_async(
        self,
        request: green_20220926_models.DeleteImagesFromLibRequest,
    ) -> green_20220926_models.DeleteImagesFromLibResponse:
        """
        @summary 批量删除
        
        @param request: DeleteImagesFromLibRequest
        @return: DeleteImagesFromLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_images_from_lib_with_options_async(request, runtime)

    def delete_keyword_with_options(
        self,
        request: green_20220926_models.DeleteKeywordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.DeleteKeywordResponse:
        """
        @summary 删除关键词
        
        @param request: DeleteKeywordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKeywordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.keyword_id_list):
            body['KeywordIdList'] = request.keyword_id_list
        if not UtilClient.is_unset(request.keyword_ids):
            body['KeywordIds'] = request.keyword_ids
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteKeyword',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.DeleteKeywordResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_keyword_with_options_async(
        self,
        request: green_20220926_models.DeleteKeywordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.DeleteKeywordResponse:
        """
        @summary 删除关键词
        
        @param request: DeleteKeywordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKeywordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.keyword_id_list):
            body['KeywordIdList'] = request.keyword_id_list
        if not UtilClient.is_unset(request.keyword_ids):
            body['KeywordIds'] = request.keyword_ids
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteKeyword',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.DeleteKeywordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_keyword(
        self,
        request: green_20220926_models.DeleteKeywordRequest,
    ) -> green_20220926_models.DeleteKeywordResponse:
        """
        @summary 删除关键词
        
        @param request: DeleteKeywordRequest
        @return: DeleteKeywordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_keyword_with_options(request, runtime)

    async def delete_keyword_async(
        self,
        request: green_20220926_models.DeleteKeywordRequest,
    ) -> green_20220926_models.DeleteKeywordResponse:
        """
        @summary 删除关键词
        
        @param request: DeleteKeywordRequest
        @return: DeleteKeywordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_keyword_with_options_async(request, runtime)

    def delete_keyword_lib_with_options(
        self,
        request: green_20220926_models.DeleteKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.DeleteKeywordLibResponse:
        """
        @summary 删除关键词库
        
        @param request: DeleteKeywordLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKeywordLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteKeywordLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.DeleteKeywordLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_keyword_lib_with_options_async(
        self,
        request: green_20220926_models.DeleteKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.DeleteKeywordLibResponse:
        """
        @summary 删除关键词库
        
        @param request: DeleteKeywordLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteKeywordLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteKeywordLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.DeleteKeywordLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_keyword_lib(
        self,
        request: green_20220926_models.DeleteKeywordLibRequest,
    ) -> green_20220926_models.DeleteKeywordLibResponse:
        """
        @summary 删除关键词库
        
        @param request: DeleteKeywordLibRequest
        @return: DeleteKeywordLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_keyword_lib_with_options(request, runtime)

    async def delete_keyword_lib_async(
        self,
        request: green_20220926_models.DeleteKeywordLibRequest,
    ) -> green_20220926_models.DeleteKeywordLibResponse:
        """
        @summary 删除关键词库
        
        @param request: DeleteKeywordLibRequest
        @return: DeleteKeywordLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_keyword_lib_with_options_async(request, runtime)

    def export_answer_sample_with_options(
        self,
        request: green_20220926_models.ExportAnswerSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ExportAnswerSampleResponse:
        """
        @summary 导出代答答案
        
        @param request: ExportAnswerSampleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportAnswerSampleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportAnswerSample',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ExportAnswerSampleResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_answer_sample_with_options_async(
        self,
        request: green_20220926_models.ExportAnswerSampleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ExportAnswerSampleResponse:
        """
        @summary 导出代答答案
        
        @param request: ExportAnswerSampleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportAnswerSampleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportAnswerSample',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ExportAnswerSampleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_answer_sample(
        self,
        request: green_20220926_models.ExportAnswerSampleRequest,
    ) -> green_20220926_models.ExportAnswerSampleResponse:
        """
        @summary 导出代答答案
        
        @param request: ExportAnswerSampleRequest
        @return: ExportAnswerSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_answer_sample_with_options(request, runtime)

    async def export_answer_sample_async(
        self,
        request: green_20220926_models.ExportAnswerSampleRequest,
    ) -> green_20220926_models.ExportAnswerSampleResponse:
        """
        @summary 导出代答答案
        
        @param request: ExportAnswerSampleRequest
        @return: ExportAnswerSampleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_answer_sample_with_options_async(request, runtime)

    def export_cip_stats_with_options(
        self,
        request: green_20220926_models.ExportCipStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ExportCipStatsResponse:
        """
        @summary 导出调用量
        
        @param request: ExportCipStatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportCipStatsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.by_month):
            body['ByMonth'] = request.by_month
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.export_type):
            body['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_uid):
            body['SubUid'] = request.sub_uid
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportCipStats',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ExportCipStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_cip_stats_with_options_async(
        self,
        request: green_20220926_models.ExportCipStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ExportCipStatsResponse:
        """
        @summary 导出调用量
        
        @param request: ExportCipStatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportCipStatsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.by_month):
            body['ByMonth'] = request.by_month
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.export_type):
            body['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_uid):
            body['SubUid'] = request.sub_uid
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportCipStats',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ExportCipStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_cip_stats(
        self,
        request: green_20220926_models.ExportCipStatsRequest,
    ) -> green_20220926_models.ExportCipStatsResponse:
        """
        @summary 导出调用量
        
        @param request: ExportCipStatsRequest
        @return: ExportCipStatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_cip_stats_with_options(request, runtime)

    async def export_cip_stats_async(
        self,
        request: green_20220926_models.ExportCipStatsRequest,
    ) -> green_20220926_models.ExportCipStatsResponse:
        """
        @summary 导出调用量
        
        @param request: ExportCipStatsRequest
        @return: ExportCipStatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_cip_stats_with_options_async(request, runtime)

    def export_keyword_with_options(
        self,
        request: green_20220926_models.ExportKeywordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ExportKeywordResponse:
        """
        @summary 导出关键词
        
        @param request: ExportKeywordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportKeywordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportKeyword',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ExportKeywordResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_keyword_with_options_async(
        self,
        request: green_20220926_models.ExportKeywordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ExportKeywordResponse:
        """
        @summary 导出关键词
        
        @param request: ExportKeywordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportKeywordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportKeyword',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ExportKeywordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_keyword(
        self,
        request: green_20220926_models.ExportKeywordRequest,
    ) -> green_20220926_models.ExportKeywordResponse:
        """
        @summary 导出关键词
        
        @param request: ExportKeywordRequest
        @return: ExportKeywordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_keyword_with_options(request, runtime)

    async def export_keyword_async(
        self,
        request: green_20220926_models.ExportKeywordRequest,
    ) -> green_20220926_models.ExportKeywordResponse:
        """
        @summary 导出关键词
        
        @param request: ExportKeywordRequest
        @return: ExportKeywordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_keyword_with_options_async(request, runtime)

    def export_oss_check_stat_with_options(
        self,
        request: green_20220926_models.ExportOssCheckStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ExportOssCheckStatResponse:
        """
        @summary oss用量统计导出
        
        @param request: ExportOssCheckStatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportOssCheckStatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.by_month):
            body['ByMonth'] = request.by_month
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.parent_task_id):
            body['ParentTaskId'] = request.parent_task_id
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportOssCheckStat',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ExportOssCheckStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_oss_check_stat_with_options_async(
        self,
        request: green_20220926_models.ExportOssCheckStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ExportOssCheckStatResponse:
        """
        @summary oss用量统计导出
        
        @param request: ExportOssCheckStatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportOssCheckStatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.by_month):
            body['ByMonth'] = request.by_month
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.parent_task_id):
            body['ParentTaskId'] = request.parent_task_id
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportOssCheckStat',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ExportOssCheckStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_oss_check_stat(
        self,
        request: green_20220926_models.ExportOssCheckStatRequest,
    ) -> green_20220926_models.ExportOssCheckStatResponse:
        """
        @summary oss用量统计导出
        
        @param request: ExportOssCheckStatRequest
        @return: ExportOssCheckStatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_oss_check_stat_with_options(request, runtime)

    async def export_oss_check_stat_async(
        self,
        request: green_20220926_models.ExportOssCheckStatRequest,
    ) -> green_20220926_models.ExportOssCheckStatResponse:
        """
        @summary oss用量统计导出
        
        @param request: ExportOssCheckStatRequest
        @return: ExportOssCheckStatResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_oss_check_stat_with_options_async(request, runtime)

    def export_result_with_options(
        self,
        tmp_req: green_20220926_models.ExportResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ExportResultResponse:
        """
        @summary 导出oss扫描结果
        
        @param tmp_req: ExportResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportResultResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.ExportResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportResult',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ExportResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_result_with_options_async(
        self,
        tmp_req: green_20220926_models.ExportResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ExportResultResponse:
        """
        @summary 导出oss扫描结果
        
        @param tmp_req: ExportResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportResultResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.ExportResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            body['Query'] = request.query
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportResult',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ExportResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_result(
        self,
        request: green_20220926_models.ExportResultRequest,
    ) -> green_20220926_models.ExportResultResponse:
        """
        @summary 导出oss扫描结果
        
        @param request: ExportResultRequest
        @return: ExportResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_result_with_options(request, runtime)

    async def export_result_async(
        self,
        request: green_20220926_models.ExportResultRequest,
    ) -> green_20220926_models.ExportResultResponse:
        """
        @summary 导出oss扫描结果
        
        @param request: ExportResultRequest
        @return: ExportResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_result_with_options_async(request, runtime)

    def export_scan_result_with_options(
        self,
        tmp_req: green_20220926_models.ExportScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ExportScanResultResponse:
        """
        @summary 导出调用结果，excel文件
        
        @param tmp_req: ExportScanResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportScanResultResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.ExportScanResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_shrink):
            body['Query'] = request.query_shrink
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportScanResult',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ExportScanResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_scan_result_with_options_async(
        self,
        tmp_req: green_20220926_models.ExportScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ExportScanResultResponse:
        """
        @summary 导出调用结果，excel文件
        
        @param tmp_req: ExportScanResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportScanResultResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.ExportScanResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_shrink):
            body['Query'] = request.query_shrink
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportScanResult',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ExportScanResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_scan_result(
        self,
        request: green_20220926_models.ExportScanResultRequest,
    ) -> green_20220926_models.ExportScanResultResponse:
        """
        @summary 导出调用结果，excel文件
        
        @param request: ExportScanResultRequest
        @return: ExportScanResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_scan_result_with_options(request, runtime)

    async def export_scan_result_async(
        self,
        request: green_20220926_models.ExportScanResultRequest,
    ) -> green_20220926_models.ExportScanResultResponse:
        """
        @summary 导出调用结果，excel文件
        
        @param request: ExportScanResultRequest
        @return: ExportScanResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_scan_result_with_options_async(request, runtime)

    def export_text_scan_result_with_options(
        self,
        tmp_req: green_20220926_models.ExportTextScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ExportTextScanResultResponse:
        """
        @summary 导出调用结果，excel文件
        
        @param tmp_req: ExportTextScanResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportTextScanResultResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.ExportTextScanResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.query_shrink):
            body['Query'] = request.query_shrink
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportTextScanResult',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ExportTextScanResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_text_scan_result_with_options_async(
        self,
        tmp_req: green_20220926_models.ExportTextScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ExportTextScanResultResponse:
        """
        @summary 导出调用结果，excel文件
        
        @param tmp_req: ExportTextScanResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExportTextScanResultResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.ExportTextScanResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.query_shrink):
            body['Query'] = request.query_shrink
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportTextScanResult',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ExportTextScanResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_text_scan_result(
        self,
        request: green_20220926_models.ExportTextScanResultRequest,
    ) -> green_20220926_models.ExportTextScanResultResponse:
        """
        @summary 导出调用结果，excel文件
        
        @param request: ExportTextScanResultRequest
        @return: ExportTextScanResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.export_text_scan_result_with_options(request, runtime)

    async def export_text_scan_result_async(
        self,
        request: green_20220926_models.ExportTextScanResultRequest,
    ) -> green_20220926_models.ExportTextScanResultResponse:
        """
        @summary 导出调用结果，excel文件
        
        @param request: ExportTextScanResultRequest
        @return: ExportTextScanResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.export_text_scan_result_with_options_async(request, runtime)

    def get_answer_import_progress_with_options(
        self,
        request: green_20220926_models.GetAnswerImportProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetAnswerImportProgressResponse:
        """
        @summary 获取代答样本导入进度
        
        @param request: GetAnswerImportProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAnswerImportProgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAnswerImportProgress',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetAnswerImportProgressResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_answer_import_progress_with_options_async(
        self,
        request: green_20220926_models.GetAnswerImportProgressRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetAnswerImportProgressResponse:
        """
        @summary 获取代答样本导入进度
        
        @param request: GetAnswerImportProgressRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAnswerImportProgressResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAnswerImportProgress',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetAnswerImportProgressResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_answer_import_progress(
        self,
        request: green_20220926_models.GetAnswerImportProgressRequest,
    ) -> green_20220926_models.GetAnswerImportProgressResponse:
        """
        @summary 获取代答样本导入进度
        
        @param request: GetAnswerImportProgressRequest
        @return: GetAnswerImportProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_answer_import_progress_with_options(request, runtime)

    async def get_answer_import_progress_async(
        self,
        request: green_20220926_models.GetAnswerImportProgressRequest,
    ) -> green_20220926_models.GetAnswerImportProgressResponse:
        """
        @summary 获取代答样本导入进度
        
        @param request: GetAnswerImportProgressRequest
        @return: GetAnswerImportProgressResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_answer_import_progress_with_options_async(request, runtime)

    def get_backup_buckets_list_with_options(
        self,
        request: green_20220926_models.GetBackupBucketsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetBackupBucketsListResponse:
        """
        @summary 证据转存获取用户bucket列表
        
        @param request: GetBackupBucketsListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBackupBucketsListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBackupBucketsList',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetBackupBucketsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_backup_buckets_list_with_options_async(
        self,
        request: green_20220926_models.GetBackupBucketsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetBackupBucketsListResponse:
        """
        @summary 证据转存获取用户bucket列表
        
        @param request: GetBackupBucketsListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBackupBucketsListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBackupBucketsList',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetBackupBucketsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_backup_buckets_list(
        self,
        request: green_20220926_models.GetBackupBucketsListRequest,
    ) -> green_20220926_models.GetBackupBucketsListResponse:
        """
        @summary 证据转存获取用户bucket列表
        
        @param request: GetBackupBucketsListRequest
        @return: GetBackupBucketsListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_backup_buckets_list_with_options(request, runtime)

    async def get_backup_buckets_list_async(
        self,
        request: green_20220926_models.GetBackupBucketsListRequest,
    ) -> green_20220926_models.GetBackupBucketsListResponse:
        """
        @summary 证据转存获取用户bucket列表
        
        @param request: GetBackupBucketsListRequest
        @return: GetBackupBucketsListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_backup_buckets_list_with_options_async(request, runtime)

    def get_backup_config_with_options(
        self,
        request: green_20220926_models.GetBackupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetBackupConfigResponse:
        """
        @summary 获取证据转存配置
        
        @param request: GetBackupConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBackupConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBackupConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetBackupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_backup_config_with_options_async(
        self,
        request: green_20220926_models.GetBackupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetBackupConfigResponse:
        """
        @summary 获取证据转存配置
        
        @param request: GetBackupConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBackupConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBackupConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetBackupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_backup_config(
        self,
        request: green_20220926_models.GetBackupConfigRequest,
    ) -> green_20220926_models.GetBackupConfigResponse:
        """
        @summary 获取证据转存配置
        
        @param request: GetBackupConfigRequest
        @return: GetBackupConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_backup_config_with_options(request, runtime)

    async def get_backup_config_async(
        self,
        request: green_20220926_models.GetBackupConfigRequest,
    ) -> green_20220926_models.GetBackupConfigResponse:
        """
        @summary 获取证据转存配置
        
        @param request: GetBackupConfigRequest
        @return: GetBackupConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_backup_config_with_options_async(request, runtime)

    def get_backup_status_with_options(
        self,
        request: green_20220926_models.GetBackupStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetBackupStatusResponse:
        """
        @summary 用户授权校验
        
        @param request: GetBackupStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBackupStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBackupStatus',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetBackupStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_backup_status_with_options_async(
        self,
        request: green_20220926_models.GetBackupStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetBackupStatusResponse:
        """
        @summary 用户授权校验
        
        @param request: GetBackupStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBackupStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBackupStatus',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetBackupStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_backup_status(
        self,
        request: green_20220926_models.GetBackupStatusRequest,
    ) -> green_20220926_models.GetBackupStatusResponse:
        """
        @summary 用户授权校验
        
        @param request: GetBackupStatusRequest
        @return: GetBackupStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_backup_status_with_options(request, runtime)

    async def get_backup_status_async(
        self,
        request: green_20220926_models.GetBackupStatusRequest,
    ) -> green_20220926_models.GetBackupStatusResponse:
        """
        @summary 用户授权校验
        
        @param request: GetBackupStatusRequest
        @return: GetBackupStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_backup_status_with_options_async(request, runtime)

    def get_buckets_list_with_options(
        self,
        request: green_20220926_models.GetBucketsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetBucketsListResponse:
        """
        @summary bucket列表
        
        @param request: GetBucketsListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBucketsListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBucketsList',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetBucketsListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_buckets_list_with_options_async(
        self,
        request: green_20220926_models.GetBucketsListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetBucketsListResponse:
        """
        @summary bucket列表
        
        @param request: GetBucketsListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBucketsListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBucketsList',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetBucketsListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_buckets_list(
        self,
        request: green_20220926_models.GetBucketsListRequest,
    ) -> green_20220926_models.GetBucketsListResponse:
        """
        @summary bucket列表
        
        @param request: GetBucketsListRequest
        @return: GetBucketsListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_buckets_list_with_options(request, runtime)

    async def get_buckets_list_async(
        self,
        request: green_20220926_models.GetBucketsListRequest,
    ) -> green_20220926_models.GetBucketsListResponse:
        """
        @summary bucket列表
        
        @param request: GetBucketsListRequest
        @return: GetBucketsListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_buckets_list_with_options_async(request, runtime)

    def get_cip_stats_with_options(
        self,
        request: green_20220926_models.GetCipStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetCipStatsResponse:
        """
        @summary 查询调用量
        
        @param request: GetCipStatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCipStatsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.by_month):
            body['ByMonth'] = request.by_month
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_uid):
            body['SubUid'] = request.sub_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCipStats',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetCipStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cip_stats_with_options_async(
        self,
        request: green_20220926_models.GetCipStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetCipStatsResponse:
        """
        @summary 查询调用量
        
        @param request: GetCipStatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCipStatsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.by_month):
            body['ByMonth'] = request.by_month
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.sub_uid):
            body['SubUid'] = request.sub_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCipStats',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetCipStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cip_stats(
        self,
        request: green_20220926_models.GetCipStatsRequest,
    ) -> green_20220926_models.GetCipStatsResponse:
        """
        @summary 查询调用量
        
        @param request: GetCipStatsRequest
        @return: GetCipStatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_cip_stats_with_options(request, runtime)

    async def get_cip_stats_async(
        self,
        request: green_20220926_models.GetCipStatsRequest,
    ) -> green_20220926_models.GetCipStatsResponse:
        """
        @summary 查询调用量
        
        @param request: GetCipStatsRequest
        @return: GetCipStatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_cip_stats_with_options_async(request, runtime)

    def get_execute_time_with_options(
        self,
        request: green_20220926_models.GetExecuteTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetExecuteTimeResponse:
        """
        @summary 获取定时任务预计执行时间
        
        @param request: GetExecuteTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExecuteTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExecuteTime',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetExecuteTimeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_execute_time_with_options_async(
        self,
        request: green_20220926_models.GetExecuteTimeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetExecuteTimeResponse:
        """
        @summary 获取定时任务预计执行时间
        
        @param request: GetExecuteTimeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExecuteTimeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExecuteTime',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetExecuteTimeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_execute_time(
        self,
        request: green_20220926_models.GetExecuteTimeRequest,
    ) -> green_20220926_models.GetExecuteTimeResponse:
        """
        @summary 获取定时任务预计执行时间
        
        @param request: GetExecuteTimeRequest
        @return: GetExecuteTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_execute_time_with_options(request, runtime)

    async def get_execute_time_async(
        self,
        request: green_20220926_models.GetExecuteTimeRequest,
    ) -> green_20220926_models.GetExecuteTimeResponse:
        """
        @summary 获取定时任务预计执行时间
        
        @param request: GetExecuteTimeRequest
        @return: GetExecuteTimeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_execute_time_with_options_async(request, runtime)

    def get_feature_config_with_options(
        self,
        request: green_20220926_models.GetFeatureConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetFeatureConfigResponse:
        """
        @summary Get Feature Configuration
        
        @param request: GetFeatureConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFeatureConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFeatureConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetFeatureConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_feature_config_with_options_async(
        self,
        request: green_20220926_models.GetFeatureConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetFeatureConfigResponse:
        """
        @summary Get Feature Configuration
        
        @param request: GetFeatureConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFeatureConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFeatureConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetFeatureConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_feature_config(
        self,
        request: green_20220926_models.GetFeatureConfigRequest,
    ) -> green_20220926_models.GetFeatureConfigResponse:
        """
        @summary Get Feature Configuration
        
        @param request: GetFeatureConfigRequest
        @return: GetFeatureConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_feature_config_with_options(request, runtime)

    async def get_feature_config_async(
        self,
        request: green_20220926_models.GetFeatureConfigRequest,
    ) -> green_20220926_models.GetFeatureConfigResponse:
        """
        @summary Get Feature Configuration
        
        @param request: GetFeatureConfigRequest
        @return: GetFeatureConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_feature_config_with_options_async(request, runtime)

    def get_image_scene_label_conf_with_options(
        self,
        request: green_20220926_models.GetImageSceneLabelConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetImageSceneLabelConfResponse:
        """
        @summary 获取图片规则标签信息
        
        @param request: GetImageSceneLabelConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageSceneLabelConfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageSceneLabelConf',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetImageSceneLabelConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_scene_label_conf_with_options_async(
        self,
        request: green_20220926_models.GetImageSceneLabelConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetImageSceneLabelConfResponse:
        """
        @summary 获取图片规则标签信息
        
        @param request: GetImageSceneLabelConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageSceneLabelConfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageSceneLabelConf',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetImageSceneLabelConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_scene_label_conf(
        self,
        request: green_20220926_models.GetImageSceneLabelConfRequest,
    ) -> green_20220926_models.GetImageSceneLabelConfResponse:
        """
        @summary 获取图片规则标签信息
        
        @param request: GetImageSceneLabelConfRequest
        @return: GetImageSceneLabelConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_image_scene_label_conf_with_options(request, runtime)

    async def get_image_scene_label_conf_async(
        self,
        request: green_20220926_models.GetImageSceneLabelConfRequest,
    ) -> green_20220926_models.GetImageSceneLabelConfResponse:
        """
        @summary 获取图片规则标签信息
        
        @param request: GetImageSceneLabelConfRequest
        @return: GetImageSceneLabelConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_image_scene_label_conf_with_options_async(request, runtime)

    def get_image_scene_label_list_conf_with_options(
        self,
        request: green_20220926_models.GetImageSceneLabelListConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetImageSceneLabelListConfResponse:
        """
        @summary 获取图片规则标签信息
        
        @param request: GetImageSceneLabelListConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageSceneLabelListConfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_service_code):
            query['ImageServiceCode'] = request.image_service_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageSceneLabelListConf',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetImageSceneLabelListConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_scene_label_list_conf_with_options_async(
        self,
        request: green_20220926_models.GetImageSceneLabelListConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetImageSceneLabelListConfResponse:
        """
        @summary 获取图片规则标签信息
        
        @param request: GetImageSceneLabelListConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetImageSceneLabelListConfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_service_code):
            query['ImageServiceCode'] = request.image_service_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetImageSceneLabelListConf',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetImageSceneLabelListConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image_scene_label_list_conf(
        self,
        request: green_20220926_models.GetImageSceneLabelListConfRequest,
    ) -> green_20220926_models.GetImageSceneLabelListConfResponse:
        """
        @summary 获取图片规则标签信息
        
        @param request: GetImageSceneLabelListConfRequest
        @return: GetImageSceneLabelListConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_image_scene_label_list_conf_with_options(request, runtime)

    async def get_image_scene_label_list_conf_async(
        self,
        request: green_20220926_models.GetImageSceneLabelListConfRequest,
    ) -> green_20220926_models.GetImageSceneLabelListConfResponse:
        """
        @summary 获取图片规则标签信息
        
        @param request: GetImageSceneLabelListConfRequest
        @return: GetImageSceneLabelListConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_image_scene_label_list_conf_with_options_async(request, runtime)

    def get_job_name_list_with_options(
        self,
        tmp_req: green_20220926_models.GetJobNameListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetJobNameListResponse:
        """
        @summary oss定时扫描检测周期查询
        
        @param tmp_req: GetJobNameListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobNameListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.GetJobNameListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_shrink):
            query['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobNameList',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetJobNameListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_name_list_with_options_async(
        self,
        tmp_req: green_20220926_models.GetJobNameListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetJobNameListResponse:
        """
        @summary oss定时扫描检测周期查询
        
        @param tmp_req: GetJobNameListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobNameListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.GetJobNameListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_shrink):
            query['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJobNameList',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetJobNameListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_name_list(
        self,
        request: green_20220926_models.GetJobNameListRequest,
    ) -> green_20220926_models.GetJobNameListResponse:
        """
        @summary oss定时扫描检测周期查询
        
        @param request: GetJobNameListRequest
        @return: GetJobNameListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_job_name_list_with_options(request, runtime)

    async def get_job_name_list_async(
        self,
        request: green_20220926_models.GetJobNameListRequest,
    ) -> green_20220926_models.GetJobNameListResponse:
        """
        @summary oss定时扫描检测周期查询
        
        @param request: GetJobNameListRequest
        @return: GetJobNameListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_job_name_list_with_options_async(request, runtime)

    def get_keyword_import_result_with_options(
        self,
        request: green_20220926_models.GetKeywordImportResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetKeywordImportResultResponse:
        """
        @summary 查询导入关键词结果
        
        @param request: GetKeywordImportResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKeywordImportResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetKeywordImportResult',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetKeywordImportResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_keyword_import_result_with_options_async(
        self,
        request: green_20220926_models.GetKeywordImportResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetKeywordImportResultResponse:
        """
        @summary 查询导入关键词结果
        
        @param request: GetKeywordImportResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKeywordImportResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetKeywordImportResult',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetKeywordImportResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_keyword_import_result(
        self,
        request: green_20220926_models.GetKeywordImportResultRequest,
    ) -> green_20220926_models.GetKeywordImportResultResponse:
        """
        @summary 查询导入关键词结果
        
        @param request: GetKeywordImportResultRequest
        @return: GetKeywordImportResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_keyword_import_result_with_options(request, runtime)

    async def get_keyword_import_result_async(
        self,
        request: green_20220926_models.GetKeywordImportResultRequest,
    ) -> green_20220926_models.GetKeywordImportResultResponse:
        """
        @summary 查询导入关键词结果
        
        @param request: GetKeywordImportResultRequest
        @return: GetKeywordImportResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_keyword_import_result_with_options_async(request, runtime)

    def get_keyword_lib_with_options(
        self,
        request: green_20220926_models.GetKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetKeywordLibResponse:
        """
        @summary 关键词库信息
        
        @param request: GetKeywordLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKeywordLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetKeywordLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetKeywordLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_keyword_lib_with_options_async(
        self,
        request: green_20220926_models.GetKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetKeywordLibResponse:
        """
        @summary 关键词库信息
        
        @param request: GetKeywordLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetKeywordLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetKeywordLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetKeywordLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_keyword_lib(
        self,
        request: green_20220926_models.GetKeywordLibRequest,
    ) -> green_20220926_models.GetKeywordLibResponse:
        """
        @summary 关键词库信息
        
        @param request: GetKeywordLibRequest
        @return: GetKeywordLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_keyword_lib_with_options(request, runtime)

    async def get_keyword_lib_async(
        self,
        request: green_20220926_models.GetKeywordLibRequest,
    ) -> green_20220926_models.GetKeywordLibResponse:
        """
        @summary 关键词库信息
        
        @param request: GetKeywordLibRequest
        @return: GetKeywordLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_keyword_lib_with_options_async(request, runtime)

    def get_oss_check_stat_with_options(
        self,
        request: green_20220926_models.GetOssCheckStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetOssCheckStatResponse:
        """
        @summary oss用量统计
        
        @param request: GetOssCheckStatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOssCheckStatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.by_month):
            body['ByMonth'] = request.by_month
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.parent_task_id):
            body['ParentTaskId'] = request.parent_task_id
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOssCheckStat',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetOssCheckStatResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_check_stat_with_options_async(
        self,
        request: green_20220926_models.GetOssCheckStatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetOssCheckStatResponse:
        """
        @summary oss用量统计
        
        @param request: GetOssCheckStatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOssCheckStatResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.by_month):
            body['ByMonth'] = request.by_month
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.parent_task_id):
            body['ParentTaskId'] = request.parent_task_id
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetOssCheckStat',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetOssCheckStatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_check_stat(
        self,
        request: green_20220926_models.GetOssCheckStatRequest,
    ) -> green_20220926_models.GetOssCheckStatResponse:
        """
        @summary oss用量统计
        
        @param request: GetOssCheckStatRequest
        @return: GetOssCheckStatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_oss_check_stat_with_options(request, runtime)

    async def get_oss_check_stat_async(
        self,
        request: green_20220926_models.GetOssCheckStatRequest,
    ) -> green_20220926_models.GetOssCheckStatResponse:
        """
        @summary oss用量统计
        
        @param request: GetOssCheckStatRequest
        @return: GetOssCheckStatResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_oss_check_stat_with_options_async(request, runtime)

    def get_oss_check_status_with_options(
        self,
        request: green_20220926_models.GetOssCheckStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetOssCheckStatusResponse:
        """
        @summary 获取OSS检测用户状态
        
        @param request: GetOssCheckStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOssCheckStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssCheckStatus',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetOssCheckStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_oss_check_status_with_options_async(
        self,
        request: green_20220926_models.GetOssCheckStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetOssCheckStatusResponse:
        """
        @summary 获取OSS检测用户状态
        
        @param request: GetOssCheckStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOssCheckStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOssCheckStatus',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetOssCheckStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_oss_check_status(
        self,
        request: green_20220926_models.GetOssCheckStatusRequest,
    ) -> green_20220926_models.GetOssCheckStatusResponse:
        """
        @summary 获取OSS检测用户状态
        
        @param request: GetOssCheckStatusRequest
        @return: GetOssCheckStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_oss_check_status_with_options(request, runtime)

    async def get_oss_check_status_async(
        self,
        request: green_20220926_models.GetOssCheckStatusRequest,
    ) -> green_20220926_models.GetOssCheckStatusResponse:
        """
        @summary 获取OSS检测用户状态
        
        @param request: GetOssCheckStatusRequest
        @return: GetOssCheckStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_oss_check_status_with_options_async(request, runtime)

    def get_scan_num_with_options(
        self,
        request: green_20220926_models.GetScanNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetScanNumResponse:
        """
        @summary 用户待检测信息
        
        @param request: GetScanNumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScanNumResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buckets):
            query['Buckets'] = request.buckets
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScanNum',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetScanNumResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scan_num_with_options_async(
        self,
        request: green_20220926_models.GetScanNumRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetScanNumResponse:
        """
        @summary 用户待检测信息
        
        @param request: GetScanNumRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScanNumResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buckets):
            query['Buckets'] = request.buckets
        if not UtilClient.is_unset(request.media_type):
            query['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScanNum',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetScanNumResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scan_num(
        self,
        request: green_20220926_models.GetScanNumRequest,
    ) -> green_20220926_models.GetScanNumResponse:
        """
        @summary 用户待检测信息
        
        @param request: GetScanNumRequest
        @return: GetScanNumResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_scan_num_with_options(request, runtime)

    async def get_scan_num_async(
        self,
        request: green_20220926_models.GetScanNumRequest,
    ) -> green_20220926_models.GetScanNumResponse:
        """
        @summary 用户待检测信息
        
        @param request: GetScanNumRequest
        @return: GetScanNumResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_scan_num_with_options_async(request, runtime)

    def get_scan_result_with_options(
        self,
        tmp_req: green_20220926_models.GetScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetScanResultResponse:
        """
        @summary 查询调用结果
        
        @param tmp_req: GetScanResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScanResultResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.GetScanResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_shrink):
            body['Query'] = request.query_shrink
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetScanResult',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetScanResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scan_result_with_options_async(
        self,
        tmp_req: green_20220926_models.GetScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetScanResultResponse:
        """
        @summary 查询调用结果
        
        @param tmp_req: GetScanResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScanResultResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.GetScanResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_shrink):
            body['Query'] = request.query_shrink
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetScanResult',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetScanResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scan_result(
        self,
        request: green_20220926_models.GetScanResultRequest,
    ) -> green_20220926_models.GetScanResultResponse:
        """
        @summary 查询调用结果
        
        @param request: GetScanResultRequest
        @return: GetScanResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_scan_result_with_options(request, runtime)

    async def get_scan_result_async(
        self,
        request: green_20220926_models.GetScanResultRequest,
    ) -> green_20220926_models.GetScanResultResponse:
        """
        @summary 查询调用结果
        
        @param request: GetScanResultRequest
        @return: GetScanResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_scan_result_with_options_async(request, runtime)

    def get_service_conf_with_options(
        self,
        request: green_20220926_models.GetServiceConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetServiceConfResponse:
        """
        @summary 获取单个服务
        
        @param request: GetServiceConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceConfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.by_default):
            body['ByDefault'] = request.by_default
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceConf',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetServiceConfResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_conf_with_options_async(
        self,
        request: green_20220926_models.GetServiceConfRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetServiceConfResponse:
        """
        @summary 获取单个服务
        
        @param request: GetServiceConfRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceConfResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.by_default):
            body['ByDefault'] = request.by_default
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceConf',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetServiceConfResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_conf(
        self,
        request: green_20220926_models.GetServiceConfRequest,
    ) -> green_20220926_models.GetServiceConfResponse:
        """
        @summary 获取单个服务
        
        @param request: GetServiceConfRequest
        @return: GetServiceConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_conf_with_options(request, runtime)

    async def get_service_conf_async(
        self,
        request: green_20220926_models.GetServiceConfRequest,
    ) -> green_20220926_models.GetServiceConfResponse:
        """
        @summary 获取单个服务
        
        @param request: GetServiceConfRequest
        @return: GetServiceConfResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_conf_with_options_async(request, runtime)

    def get_service_config_with_options(
        self,
        request: green_20220926_models.GetServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetServiceConfigResponse:
        """
        @summary 获取单个服务
        
        @param request: GetServiceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetServiceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_config_with_options_async(
        self,
        request: green_20220926_models.GetServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetServiceConfigResponse:
        """
        @summary 获取单个服务
        
        @param request: GetServiceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetServiceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_config(
        self,
        request: green_20220926_models.GetServiceConfigRequest,
    ) -> green_20220926_models.GetServiceConfigResponse:
        """
        @summary 获取单个服务
        
        @param request: GetServiceConfigRequest
        @return: GetServiceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_config_with_options(request, runtime)

    async def get_service_config_async(
        self,
        request: green_20220926_models.GetServiceConfigRequest,
    ) -> green_20220926_models.GetServiceConfigResponse:
        """
        @summary 获取单个服务
        
        @param request: GetServiceConfigRequest
        @return: GetServiceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_config_with_options_async(request, runtime)

    def get_service_label_config_with_options(
        self,
        request: green_20220926_models.GetServiceLabelConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetServiceLabelConfigResponse:
        """
        @summary 获取单个服务的标签配置
        
        @param request: GetServiceLabelConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceLabelConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceLabelConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetServiceLabelConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_label_config_with_options_async(
        self,
        request: green_20220926_models.GetServiceLabelConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetServiceLabelConfigResponse:
        """
        @summary 获取单个服务的标签配置
        
        @param request: GetServiceLabelConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceLabelConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceLabelConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetServiceLabelConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_label_config(
        self,
        request: green_20220926_models.GetServiceLabelConfigRequest,
    ) -> green_20220926_models.GetServiceLabelConfigResponse:
        """
        @summary 获取单个服务的标签配置
        
        @param request: GetServiceLabelConfigRequest
        @return: GetServiceLabelConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_label_config_with_options(request, runtime)

    async def get_service_label_config_async(
        self,
        request: green_20220926_models.GetServiceLabelConfigRequest,
    ) -> green_20220926_models.GetServiceLabelConfigResponse:
        """
        @summary 获取单个服务的标签配置
        
        @param request: GetServiceLabelConfigRequest
        @return: GetServiceLabelConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_label_config_with_options_async(request, runtime)

    def get_stock_oss_check_tasks_list_with_options(
        self,
        tmp_req: green_20220926_models.GetStockOssCheckTasksListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetStockOssCheckTasksListResponse:
        """
        @summary 查询oss扫描任务列表
        
        @param tmp_req: GetStockOssCheckTasksListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStockOssCheckTasksListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.GetStockOssCheckTasksListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.is_inc):
            query['IsInc'] = request.is_inc
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.media_type):
            body['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStockOssCheckTasksList',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetStockOssCheckTasksListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stock_oss_check_tasks_list_with_options_async(
        self,
        tmp_req: green_20220926_models.GetStockOssCheckTasksListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetStockOssCheckTasksListResponse:
        """
        @summary 查询oss扫描任务列表
        
        @param tmp_req: GetStockOssCheckTasksListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStockOssCheckTasksListResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.GetStockOssCheckTasksListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.is_inc):
            query['IsInc'] = request.is_inc
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.media_type):
            body['MediaType'] = request.media_type
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStockOssCheckTasksList',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetStockOssCheckTasksListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stock_oss_check_tasks_list(
        self,
        request: green_20220926_models.GetStockOssCheckTasksListRequest,
    ) -> green_20220926_models.GetStockOssCheckTasksListResponse:
        """
        @summary 查询oss扫描任务列表
        
        @param request: GetStockOssCheckTasksListRequest
        @return: GetStockOssCheckTasksListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_stock_oss_check_tasks_list_with_options(request, runtime)

    async def get_stock_oss_check_tasks_list_async(
        self,
        request: green_20220926_models.GetStockOssCheckTasksListRequest,
    ) -> green_20220926_models.GetStockOssCheckTasksListResponse:
        """
        @summary 查询oss扫描任务列表
        
        @param request: GetStockOssCheckTasksListRequest
        @return: GetStockOssCheckTasksListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_stock_oss_check_tasks_list_with_options_async(request, runtime)

    def get_text_scan_result_with_options(
        self,
        tmp_req: green_20220926_models.GetTextScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetTextScanResultResponse:
        """
        @summary 查询调用结果
        
        @param tmp_req: GetTextScanResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTextScanResultResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.GetTextScanResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_shrink):
            body['Query'] = request.query_shrink
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTextScanResult',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetTextScanResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_text_scan_result_with_options_async(
        self,
        tmp_req: green_20220926_models.GetTextScanResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetTextScanResultResponse:
        """
        @summary 查询调用结果
        
        @param tmp_req: GetTextScanResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTextScanResultResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.GetTextScanResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.query):
            request.query_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.query, 'Query', 'json')
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_shrink):
            body['Query'] = request.query_shrink
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTextScanResult',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetTextScanResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_text_scan_result(
        self,
        request: green_20220926_models.GetTextScanResultRequest,
    ) -> green_20220926_models.GetTextScanResultResponse:
        """
        @summary 查询调用结果
        
        @param request: GetTextScanResultRequest
        @return: GetTextScanResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_text_scan_result_with_options(request, runtime)

    async def get_text_scan_result_async(
        self,
        request: green_20220926_models.GetTextScanResultRequest,
    ) -> green_20220926_models.GetTextScanResultResponse:
        """
        @summary 查询调用结果
        
        @param request: GetTextScanResultRequest
        @return: GetTextScanResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_text_scan_result_with_options_async(request, runtime)

    def get_upload_info_with_options(
        self,
        request: green_20220926_models.GetUploadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetUploadInfoResponse:
        """
        @summary 文件上传获取相应信息
        
        @param request: GetUploadInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUploadInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUploadInfo',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetUploadInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upload_info_with_options_async(
        self,
        request: green_20220926_models.GetUploadInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetUploadInfoResponse:
        """
        @summary 文件上传获取相应信息
        
        @param request: GetUploadInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUploadInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUploadInfo',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetUploadInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upload_info(
        self,
        request: green_20220926_models.GetUploadInfoRequest,
    ) -> green_20220926_models.GetUploadInfoResponse:
        """
        @summary 文件上传获取相应信息
        
        @param request: GetUploadInfoRequest
        @return: GetUploadInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_upload_info_with_options(request, runtime)

    async def get_upload_info_async(
        self,
        request: green_20220926_models.GetUploadInfoRequest,
    ) -> green_20220926_models.GetUploadInfoResponse:
        """
        @summary 文件上传获取相应信息
        
        @param request: GetUploadInfoRequest
        @return: GetUploadInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_upload_info_with_options_async(request, runtime)

    def get_user_buy_status_with_options(
        self,
        request: green_20220926_models.GetUserBuyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetUserBuyStatusResponse:
        """
        @summary 获取用户购买状态
        
        @param request: GetUserBuyStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserBuyStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserBuyStatus',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetUserBuyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_buy_status_with_options_async(
        self,
        request: green_20220926_models.GetUserBuyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.GetUserBuyStatusResponse:
        """
        @summary 获取用户购买状态
        
        @param request: GetUserBuyStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserBuyStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserBuyStatus',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.GetUserBuyStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_buy_status(
        self,
        request: green_20220926_models.GetUserBuyStatusRequest,
    ) -> green_20220926_models.GetUserBuyStatusResponse:
        """
        @summary 获取用户购买状态
        
        @param request: GetUserBuyStatusRequest
        @return: GetUserBuyStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_buy_status_with_options(request, runtime)

    async def get_user_buy_status_async(
        self,
        request: green_20220926_models.GetUserBuyStatusRequest,
    ) -> green_20220926_models.GetUserBuyStatusResponse:
        """
        @summary 获取用户购买状态
        
        @param request: GetUserBuyStatusRequest
        @return: GetUserBuyStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_buy_status_with_options_async(request, runtime)

    def list_answer_lib_with_options(
        self,
        request: green_20220926_models.ListAnswerLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ListAnswerLibResponse:
        """
        @summary 代答库列表
        
        @param request: ListAnswerLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAnswerLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnswerLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ListAnswerLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_answer_lib_with_options_async(
        self,
        request: green_20220926_models.ListAnswerLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ListAnswerLibResponse:
        """
        @summary 代答库列表
        
        @param request: ListAnswerLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAnswerLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnswerLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ListAnswerLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_answer_lib(
        self,
        request: green_20220926_models.ListAnswerLibRequest,
    ) -> green_20220926_models.ListAnswerLibResponse:
        """
        @summary 代答库列表
        
        @param request: ListAnswerLibRequest
        @return: ListAnswerLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_answer_lib_with_options(request, runtime)

    async def list_answer_lib_async(
        self,
        request: green_20220926_models.ListAnswerLibRequest,
    ) -> green_20220926_models.ListAnswerLibResponse:
        """
        @summary 代答库列表
        
        @param request: ListAnswerLibRequest
        @return: ListAnswerLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_answer_lib_with_options_async(request, runtime)

    def list_callback_with_options(
        self,
        request: green_20220926_models.ListCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ListCallbackResponse:
        """
        @summary 消息通知列表
        
        @param request: ListCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCallback',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ListCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_callback_with_options_async(
        self,
        request: green_20220926_models.ListCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ListCallbackResponse:
        """
        @summary 消息通知列表
        
        @param request: ListCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCallback',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ListCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_callback(
        self,
        request: green_20220926_models.ListCallbackRequest,
    ) -> green_20220926_models.ListCallbackResponse:
        """
        @summary 消息通知列表
        
        @param request: ListCallbackRequest
        @return: ListCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_callback_with_options(request, runtime)

    async def list_callback_async(
        self,
        request: green_20220926_models.ListCallbackRequest,
    ) -> green_20220926_models.ListCallbackResponse:
        """
        @summary 消息通知列表
        
        @param request: ListCallbackRequest
        @return: ListCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_callback_with_options_async(request, runtime)

    def list_image_lib_with_options(
        self,
        request: green_20220926_models.ListImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ListImageLibResponse:
        """
        @summary 图库列表
        
        @param request: ListImageLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImageLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImageLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ListImageLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_image_lib_with_options_async(
        self,
        request: green_20220926_models.ListImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ListImageLibResponse:
        """
        @summary 图库列表
        
        @param request: ListImageLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImageLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListImageLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ListImageLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_image_lib(
        self,
        request: green_20220926_models.ListImageLibRequest,
    ) -> green_20220926_models.ListImageLibResponse:
        """
        @summary 图库列表
        
        @param request: ListImageLibRequest
        @return: ListImageLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_image_lib_with_options(request, runtime)

    async def list_image_lib_async(
        self,
        request: green_20220926_models.ListImageLibRequest,
    ) -> green_20220926_models.ListImageLibResponse:
        """
        @summary 图库列表
        
        @param request: ListImageLibRequest
        @return: ListImageLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_image_lib_with_options_async(request, runtime)

    def list_images_from_lib_with_options(
        self,
        tmp_req: green_20220926_models.ListImagesFromLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ListImagesFromLibResponse:
        """
        @summary 图片列表 分页
        
        @param tmp_req: ListImagesFromLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImagesFromLibResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.ListImagesFromLibShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.img_id):
            body['ImgId'] = request.img_id
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListImagesFromLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ListImagesFromLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_from_lib_with_options_async(
        self,
        tmp_req: green_20220926_models.ListImagesFromLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ListImagesFromLibResponse:
        """
        @summary 图片列表 分页
        
        @param tmp_req: ListImagesFromLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImagesFromLibResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.ListImagesFromLibShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.img_id):
            body['ImgId'] = request.img_id
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListImagesFromLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ListImagesFromLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images_from_lib(
        self,
        request: green_20220926_models.ListImagesFromLibRequest,
    ) -> green_20220926_models.ListImagesFromLibResponse:
        """
        @summary 图片列表 分页
        
        @param request: ListImagesFromLibRequest
        @return: ListImagesFromLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_images_from_lib_with_options(request, runtime)

    async def list_images_from_lib_async(
        self,
        request: green_20220926_models.ListImagesFromLibRequest,
    ) -> green_20220926_models.ListImagesFromLibResponse:
        """
        @summary 图片列表 分页
        
        @param request: ListImagesFromLibRequest
        @return: ListImagesFromLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_images_from_lib_with_options_async(request, runtime)

    def list_keyword_libs_with_options(
        self,
        request: green_20220926_models.ListKeywordLibsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ListKeywordLibsResponse:
        """
        @summary 关键词库列表
        
        @param request: ListKeywordLibsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKeywordLibsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKeywordLibs',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ListKeywordLibsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_keyword_libs_with_options_async(
        self,
        request: green_20220926_models.ListKeywordLibsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ListKeywordLibsResponse:
        """
        @summary 关键词库列表
        
        @param request: ListKeywordLibsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKeywordLibsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListKeywordLibs',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ListKeywordLibsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_keyword_libs(
        self,
        request: green_20220926_models.ListKeywordLibsRequest,
    ) -> green_20220926_models.ListKeywordLibsResponse:
        """
        @summary 关键词库列表
        
        @param request: ListKeywordLibsRequest
        @return: ListKeywordLibsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_keyword_libs_with_options(request, runtime)

    async def list_keyword_libs_async(
        self,
        request: green_20220926_models.ListKeywordLibsRequest,
    ) -> green_20220926_models.ListKeywordLibsResponse:
        """
        @summary 关键词库列表
        
        @param request: ListKeywordLibsRequest
        @return: ListKeywordLibsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_keyword_libs_with_options_async(request, runtime)

    def list_keywords_with_options(
        self,
        tmp_req: green_20220926_models.ListKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ListKeywordsResponse:
        """
        @summary 查询关键词列表
        
        @param tmp_req: ListKeywordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKeywordsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.ListKeywordsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.word):
            body['Word'] = request.word
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListKeywords',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ListKeywordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_keywords_with_options_async(
        self,
        tmp_req: green_20220926_models.ListKeywordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ListKeywordsResponse:
        """
        @summary 查询关键词列表
        
        @param tmp_req: ListKeywordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListKeywordsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.ListKeywordsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_shrink):
            body['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.word):
            body['Word'] = request.word
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListKeywords',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ListKeywordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_keywords(
        self,
        request: green_20220926_models.ListKeywordsRequest,
    ) -> green_20220926_models.ListKeywordsResponse:
        """
        @summary 查询关键词列表
        
        @param request: ListKeywordsRequest
        @return: ListKeywordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_keywords_with_options(request, runtime)

    async def list_keywords_async(
        self,
        request: green_20220926_models.ListKeywordsRequest,
    ) -> green_20220926_models.ListKeywordsResponse:
        """
        @summary 查询关键词列表
        
        @param request: ListKeywordsRequest
        @return: ListKeywordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_keywords_with_options_async(request, runtime)

    def list_oss_check_result_with_options(
        self,
        tmp_req: green_20220926_models.ListOssCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ListOssCheckResultResponse:
        """
        @summary oss扫描结果查询
        
        @param tmp_req: ListOssCheckResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOssCheckResultResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.ListOssCheckResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.finish_num):
            query['FinishNum'] = request.finish_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_shrink):
            query['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOssCheckResult',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ListOssCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_oss_check_result_with_options_async(
        self,
        tmp_req: green_20220926_models.ListOssCheckResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ListOssCheckResultResponse:
        """
        @summary oss扫描结果查询
        
        @param tmp_req: ListOssCheckResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListOssCheckResultResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.ListOssCheckResultShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.finish_num):
            query['FinishNum'] = request.finish_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_shrink):
            query['Sort'] = request.sort_shrink
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOssCheckResult',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ListOssCheckResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_oss_check_result(
        self,
        request: green_20220926_models.ListOssCheckResultRequest,
    ) -> green_20220926_models.ListOssCheckResultResponse:
        """
        @summary oss扫描结果查询
        
        @param request: ListOssCheckResultRequest
        @return: ListOssCheckResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_oss_check_result_with_options(request, runtime)

    async def list_oss_check_result_async(
        self,
        request: green_20220926_models.ListOssCheckResultRequest,
    ) -> green_20220926_models.ListOssCheckResultResponse:
        """
        @summary oss扫描结果查询
        
        @param request: ListOssCheckResultRequest
        @return: ListOssCheckResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_oss_check_result_with_options_async(request, runtime)

    def list_service_configs_with_options(
        self,
        request: green_20220926_models.ListServiceConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ListServiceConfigsResponse:
        """
        @summary 获取服务列表
        
        @param request: ListServiceConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classify):
            query['Classify'] = request.classify
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.use_status):
            query['UseStatus'] = request.use_status
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServiceConfigs',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ListServiceConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_configs_with_options_async(
        self,
        request: green_20220926_models.ListServiceConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ListServiceConfigsResponse:
        """
        @summary 获取服务列表
        
        @param request: ListServiceConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.classify):
            query['Classify'] = request.classify
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.use_status):
            query['UseStatus'] = request.use_status
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServiceConfigs',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ListServiceConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_configs(
        self,
        request: green_20220926_models.ListServiceConfigsRequest,
    ) -> green_20220926_models.ListServiceConfigsResponse:
        """
        @summary 获取服务列表
        
        @param request: ListServiceConfigsRequest
        @return: ListServiceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_configs_with_options(request, runtime)

    async def list_service_configs_async(
        self,
        request: green_20220926_models.ListServiceConfigsRequest,
    ) -> green_20220926_models.ListServiceConfigsResponse:
        """
        @summary 获取服务列表
        
        @param request: ListServiceConfigsRequest
        @return: ListServiceConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_configs_with_options_async(request, runtime)

    def llm_stream_chat_with_options(
        self,
        request: green_20220926_models.LlmStreamChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.LlmStreamChatResponse:
        """
        @summary 使用SSE接口流式调用大模型
        
        @param request: LlmStreamChatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LlmStreamChatResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.messages):
            body['Messages'] = request.messages
        if not UtilClient.is_unset(request.temperature):
            body['Temperature'] = request.temperature
        if not UtilClient.is_unset(request.top_p):
            body['TopP'] = request.top_p
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LlmStreamChat',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.LlmStreamChatResponse(),
            self.call_api(params, req, runtime)
        )

    async def llm_stream_chat_with_options_async(
        self,
        request: green_20220926_models.LlmStreamChatRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.LlmStreamChatResponse:
        """
        @summary 使用SSE接口流式调用大模型
        
        @param request: LlmStreamChatRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LlmStreamChatResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.messages):
            body['Messages'] = request.messages
        if not UtilClient.is_unset(request.temperature):
            body['Temperature'] = request.temperature
        if not UtilClient.is_unset(request.top_p):
            body['TopP'] = request.top_p
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LlmStreamChat',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.LlmStreamChatResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def llm_stream_chat(
        self,
        request: green_20220926_models.LlmStreamChatRequest,
    ) -> green_20220926_models.LlmStreamChatResponse:
        """
        @summary 使用SSE接口流式调用大模型
        
        @param request: LlmStreamChatRequest
        @return: LlmStreamChatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.llm_stream_chat_with_options(request, runtime)

    async def llm_stream_chat_async(
        self,
        request: green_20220926_models.LlmStreamChatRequest,
    ) -> green_20220926_models.LlmStreamChatResponse:
        """
        @summary 使用SSE接口流式调用大模型
        
        @param request: LlmStreamChatRequest
        @return: LlmStreamChatResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.llm_stream_chat_with_options_async(request, runtime)

    def modify_answer_lib_with_options(
        self,
        request: green_20220926_models.ModifyAnswerLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ModifyAnswerLibResponse:
        """
        @summary 更新代答库
        
        @param request: ModifyAnswerLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAnswerLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lib_id):
            query['LibId'] = request.lib_id
        if not UtilClient.is_unset(request.lib_name):
            query['LibName'] = request.lib_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAnswerLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ModifyAnswerLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_answer_lib_with_options_async(
        self,
        request: green_20220926_models.ModifyAnswerLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ModifyAnswerLibResponse:
        """
        @summary 更新代答库
        
        @param request: ModifyAnswerLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAnswerLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.lib_id):
            query['LibId'] = request.lib_id
        if not UtilClient.is_unset(request.lib_name):
            query['LibName'] = request.lib_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAnswerLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ModifyAnswerLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_answer_lib(
        self,
        request: green_20220926_models.ModifyAnswerLibRequest,
    ) -> green_20220926_models.ModifyAnswerLibResponse:
        """
        @summary 更新代答库
        
        @param request: ModifyAnswerLibRequest
        @return: ModifyAnswerLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_answer_lib_with_options(request, runtime)

    async def modify_answer_lib_async(
        self,
        request: green_20220926_models.ModifyAnswerLibRequest,
    ) -> green_20220926_models.ModifyAnswerLibResponse:
        """
        @summary 更新代答库
        
        @param request: ModifyAnswerLibRequest
        @return: ModifyAnswerLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_answer_lib_with_options_async(request, runtime)

    def modify_callback_with_options(
        self,
        request: green_20220926_models.ModifyCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ModifyCallbackResponse:
        """
        @summary 修改消息通知
        
        @param request: ModifyCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.crypt_type):
            body['CryptType'] = request.crypt_type
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.scope):
            body['Scope'] = request.scope
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyCallback',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ModifyCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_callback_with_options_async(
        self,
        request: green_20220926_models.ModifyCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ModifyCallbackResponse:
        """
        @summary 修改消息通知
        
        @param request: ModifyCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.crypt_type):
            body['CryptType'] = request.crypt_type
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.scope):
            body['Scope'] = request.scope
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyCallback',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ModifyCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_callback(
        self,
        request: green_20220926_models.ModifyCallbackRequest,
    ) -> green_20220926_models.ModifyCallbackResponse:
        """
        @summary 修改消息通知
        
        @param request: ModifyCallbackRequest
        @return: ModifyCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_callback_with_options(request, runtime)

    async def modify_callback_async(
        self,
        request: green_20220926_models.ModifyCallbackRequest,
    ) -> green_20220926_models.ModifyCallbackResponse:
        """
        @summary 修改消息通知
        
        @param request: ModifyCallbackRequest
        @return: ModifyCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_callback_with_options_async(request, runtime)

    def modify_feature_config_with_options(
        self,
        request: green_20220926_models.ModifyFeatureConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ModifyFeatureConfigResponse:
        """
        @summary Save Feature Configuration
        
        @param request: ModifyFeatureConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFeatureConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.field):
            body['Field'] = request.field
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyFeatureConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ModifyFeatureConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_feature_config_with_options_async(
        self,
        request: green_20220926_models.ModifyFeatureConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ModifyFeatureConfigResponse:
        """
        @summary Save Feature Configuration
        
        @param request: ModifyFeatureConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyFeatureConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.config):
            body['Config'] = request.config
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.field):
            body['Field'] = request.field
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyFeatureConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ModifyFeatureConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_feature_config(
        self,
        request: green_20220926_models.ModifyFeatureConfigRequest,
    ) -> green_20220926_models.ModifyFeatureConfigResponse:
        """
        @summary Save Feature Configuration
        
        @param request: ModifyFeatureConfigRequest
        @return: ModifyFeatureConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_feature_config_with_options(request, runtime)

    async def modify_feature_config_async(
        self,
        request: green_20220926_models.ModifyFeatureConfigRequest,
    ) -> green_20220926_models.ModifyFeatureConfigResponse:
        """
        @summary Save Feature Configuration
        
        @param request: ModifyFeatureConfigRequest
        @return: ModifyFeatureConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_feature_config_with_options_async(request, runtime)

    def modify_service_info_with_options(
        self,
        request: green_20220926_models.ModifyServiceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ModifyServiceInfoResponse:
        """
        @summary 编辑服务
        
        @param request: ModifyServiceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyServiceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.service_desc):
            body['ServiceDesc'] = request.service_desc
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyServiceInfo',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ModifyServiceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_service_info_with_options_async(
        self,
        request: green_20220926_models.ModifyServiceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.ModifyServiceInfoResponse:
        """
        @summary 编辑服务
        
        @param request: ModifyServiceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyServiceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.service_desc):
            body['ServiceDesc'] = request.service_desc
        if not UtilClient.is_unset(request.service_name):
            body['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyServiceInfo',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.ModifyServiceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_service_info(
        self,
        request: green_20220926_models.ModifyServiceInfoRequest,
    ) -> green_20220926_models.ModifyServiceInfoResponse:
        """
        @summary 编辑服务
        
        @param request: ModifyServiceInfoRequest
        @return: ModifyServiceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_service_info_with_options(request, runtime)

    async def modify_service_info_async(
        self,
        request: green_20220926_models.ModifyServiceInfoRequest,
    ) -> green_20220926_models.ModifyServiceInfoResponse:
        """
        @summary 编辑服务
        
        @param request: ModifyServiceInfoRequest
        @return: ModifyServiceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_service_info_with_options_async(request, runtime)

    def query_answer_sample_by_page_with_options(
        self,
        tmp_req: green_20220926_models.QueryAnswerSampleByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.QueryAnswerSampleByPageResponse:
        """
        @summary 分页查询代答样本
        
        @param tmp_req: QueryAnswerSampleByPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAnswerSampleByPageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.QueryAnswerSampleByPageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.answer):
            query['Answer'] = request.answer
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lib_id):
            query['LibId'] = request.lib_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_shrink):
            query['Sort'] = request.sort_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAnswerSampleByPage',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.QueryAnswerSampleByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_answer_sample_by_page_with_options_async(
        self,
        tmp_req: green_20220926_models.QueryAnswerSampleByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.QueryAnswerSampleByPageResponse:
        """
        @summary 分页查询代答样本
        
        @param tmp_req: QueryAnswerSampleByPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryAnswerSampleByPageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.QueryAnswerSampleByPageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sort):
            request.sort_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sort, 'Sort', 'json')
        query = {}
        if not UtilClient.is_unset(request.answer):
            query['Answer'] = request.answer
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.lib_id):
            query['LibId'] = request.lib_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_shrink):
            query['Sort'] = request.sort_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAnswerSampleByPage',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.QueryAnswerSampleByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_answer_sample_by_page(
        self,
        request: green_20220926_models.QueryAnswerSampleByPageRequest,
    ) -> green_20220926_models.QueryAnswerSampleByPageResponse:
        """
        @summary 分页查询代答样本
        
        @param request: QueryAnswerSampleByPageRequest
        @return: QueryAnswerSampleByPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_answer_sample_by_page_with_options(request, runtime)

    async def query_answer_sample_by_page_async(
        self,
        request: green_20220926_models.QueryAnswerSampleByPageRequest,
    ) -> green_20220926_models.QueryAnswerSampleByPageResponse:
        """
        @summary 分页查询代答样本
        
        @param request: QueryAnswerSampleByPageRequest
        @return: QueryAnswerSampleByPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_answer_sample_by_page_with_options_async(request, runtime)

    def query_callback_with_options(
        self,
        request: green_20220926_models.QueryCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.QueryCallbackResponse:
        """
        @summary 查询单个回调配置
        
        @param request: QueryCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.check_for_oss):
            body['CheckForOss'] = request.check_for_oss
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCallback',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.QueryCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_callback_with_options_async(
        self,
        request: green_20220926_models.QueryCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.QueryCallbackResponse:
        """
        @summary 查询单个回调配置
        
        @param request: QueryCallbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCallbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.check_for_oss):
            body['CheckForOss'] = request.check_for_oss
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCallback',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.QueryCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_callback(
        self,
        request: green_20220926_models.QueryCallbackRequest,
    ) -> green_20220926_models.QueryCallbackResponse:
        """
        @summary 查询单个回调配置
        
        @param request: QueryCallbackRequest
        @return: QueryCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_callback_with_options(request, runtime)

    async def query_callback_async(
        self,
        request: green_20220926_models.QueryCallbackRequest,
    ) -> green_20220926_models.QueryCallbackResponse:
        """
        @summary 查询单个回调配置
        
        @param request: QueryCallbackRequest
        @return: QueryCallbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_callback_with_options_async(request, runtime)

    def query_callback_by_page_with_options(
        self,
        request: green_20220926_models.QueryCallbackByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.QueryCallbackByPageResponse:
        """
        @summary 消息通知
        
        @param request: QueryCallbackByPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCallbackByPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCallbackByPage',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.QueryCallbackByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_callback_by_page_with_options_async(
        self,
        request: green_20220926_models.QueryCallbackByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.QueryCallbackByPageResponse:
        """
        @summary 消息通知
        
        @param request: QueryCallbackByPageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: QueryCallbackByPageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryCallbackByPage',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.QueryCallbackByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_callback_by_page(
        self,
        request: green_20220926_models.QueryCallbackByPageRequest,
    ) -> green_20220926_models.QueryCallbackByPageResponse:
        """
        @summary 消息通知
        
        @param request: QueryCallbackByPageRequest
        @return: QueryCallbackByPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_callback_by_page_with_options(request, runtime)

    async def query_callback_by_page_async(
        self,
        request: green_20220926_models.QueryCallbackByPageRequest,
    ) -> green_20220926_models.QueryCallbackByPageResponse:
        """
        @summary 消息通知
        
        @param request: QueryCallbackByPageRequest
        @return: QueryCallbackByPageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.query_callback_by_page_with_options_async(request, runtime)

    def update_backup_config_with_options(
        self,
        request: green_20220926_models.UpdateBackupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.UpdateBackupConfigResponse:
        """
        @summary 更新证据转存配置
        
        @param request: UpdateBackupConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBackupConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_config):
            query['BackupConfig'] = request.backup_config
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBackupConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.UpdateBackupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_backup_config_with_options_async(
        self,
        request: green_20220926_models.UpdateBackupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.UpdateBackupConfigResponse:
        """
        @summary 更新证据转存配置
        
        @param request: UpdateBackupConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateBackupConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_config):
            query['BackupConfig'] = request.backup_config
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service_code):
            query['ServiceCode'] = request.service_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBackupConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.UpdateBackupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_backup_config(
        self,
        request: green_20220926_models.UpdateBackupConfigRequest,
    ) -> green_20220926_models.UpdateBackupConfigResponse:
        """
        @summary 更新证据转存配置
        
        @param request: UpdateBackupConfigRequest
        @return: UpdateBackupConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_backup_config_with_options(request, runtime)

    async def update_backup_config_async(
        self,
        request: green_20220926_models.UpdateBackupConfigRequest,
    ) -> green_20220926_models.UpdateBackupConfigResponse:
        """
        @summary 更新证据转存配置
        
        @param request: UpdateBackupConfigRequest
        @return: UpdateBackupConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_backup_config_with_options_async(request, runtime)

    def update_image_lib_with_options(
        self,
        request: green_20220926_models.UpdateImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.UpdateImageLibResponse:
        """
        @summary 编辑图库
        
        @param request: UpdateImageLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateImageLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.free_inspection):
            body['FreeInspection'] = request.free_inspection
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        if not UtilClient.is_unset(request.lib_name):
            body['LibName'] = request.lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateImageLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.UpdateImageLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_image_lib_with_options_async(
        self,
        request: green_20220926_models.UpdateImageLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.UpdateImageLibResponse:
        """
        @summary 编辑图库
        
        @param request: UpdateImageLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateImageLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.comment):
            body['Comment'] = request.comment
        if not UtilClient.is_unset(request.free_inspection):
            body['FreeInspection'] = request.free_inspection
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        if not UtilClient.is_unset(request.lib_name):
            body['LibName'] = request.lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateImageLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.UpdateImageLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_image_lib(
        self,
        request: green_20220926_models.UpdateImageLibRequest,
    ) -> green_20220926_models.UpdateImageLibResponse:
        """
        @summary 编辑图库
        
        @param request: UpdateImageLibRequest
        @return: UpdateImageLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_image_lib_with_options(request, runtime)

    async def update_image_lib_async(
        self,
        request: green_20220926_models.UpdateImageLibRequest,
    ) -> green_20220926_models.UpdateImageLibResponse:
        """
        @summary 编辑图库
        
        @param request: UpdateImageLibRequest
        @return: UpdateImageLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_image_lib_with_options_async(request, runtime)

    def update_image_lib_free_inspection_with_options(
        self,
        tmp_req: green_20220926_models.UpdateImageLibFreeInspectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.UpdateImageLibFreeInspectionResponse:
        """
        @summary 编辑图库免检配置
        
        @param tmp_req: UpdateImageLibFreeInspectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateImageLibFreeInspectionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.UpdateImageLibFreeInspectionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.config_shrink):
            body['Config'] = request.config_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateImageLibFreeInspection',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.UpdateImageLibFreeInspectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_image_lib_free_inspection_with_options_async(
        self,
        tmp_req: green_20220926_models.UpdateImageLibFreeInspectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.UpdateImageLibFreeInspectionResponse:
        """
        @summary 编辑图库免检配置
        
        @param tmp_req: UpdateImageLibFreeInspectionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateImageLibFreeInspectionResponse
        """
        UtilClient.validate_model(tmp_req)
        request = green_20220926_models.UpdateImageLibFreeInspectionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.config_shrink):
            body['Config'] = request.config_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateImageLibFreeInspection',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.UpdateImageLibFreeInspectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_image_lib_free_inspection(
        self,
        request: green_20220926_models.UpdateImageLibFreeInspectionRequest,
    ) -> green_20220926_models.UpdateImageLibFreeInspectionResponse:
        """
        @summary 编辑图库免检配置
        
        @param request: UpdateImageLibFreeInspectionRequest
        @return: UpdateImageLibFreeInspectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_image_lib_free_inspection_with_options(request, runtime)

    async def update_image_lib_free_inspection_async(
        self,
        request: green_20220926_models.UpdateImageLibFreeInspectionRequest,
    ) -> green_20220926_models.UpdateImageLibFreeInspectionResponse:
        """
        @summary 编辑图库免检配置
        
        @param request: UpdateImageLibFreeInspectionRequest
        @return: UpdateImageLibFreeInspectionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_image_lib_free_inspection_with_options_async(request, runtime)

    def update_keyword_lib_with_options(
        self,
        request: green_20220926_models.UpdateKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.UpdateKeywordLibResponse:
        """
        @summary 编辑关键词库
        
        @param request: UpdateKeywordLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateKeywordLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        if not UtilClient.is_unset(request.lib_name):
            body['LibName'] = request.lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateKeywordLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.UpdateKeywordLibResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_keyword_lib_with_options_async(
        self,
        request: green_20220926_models.UpdateKeywordLibRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.UpdateKeywordLibResponse:
        """
        @summary 编辑关键词库
        
        @param request: UpdateKeywordLibRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateKeywordLibResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.lib_id):
            body['LibId'] = request.lib_id
        if not UtilClient.is_unset(request.lib_name):
            body['LibName'] = request.lib_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateKeywordLib',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.UpdateKeywordLibResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_keyword_lib(
        self,
        request: green_20220926_models.UpdateKeywordLibRequest,
    ) -> green_20220926_models.UpdateKeywordLibResponse:
        """
        @summary 编辑关键词库
        
        @param request: UpdateKeywordLibRequest
        @return: UpdateKeywordLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_keyword_lib_with_options(request, runtime)

    async def update_keyword_lib_async(
        self,
        request: green_20220926_models.UpdateKeywordLibRequest,
    ) -> green_20220926_models.UpdateKeywordLibResponse:
        """
        @summary 编辑关键词库
        
        @param request: UpdateKeywordLibRequest
        @return: UpdateKeywordLibResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_keyword_lib_with_options_async(request, runtime)

    def update_scan_result_feedback_with_options(
        self,
        request: green_20220926_models.UpdateScanResultFeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.UpdateScanResultFeedbackResponse:
        """
        @summary 检测结果反馈
        
        @param request: UpdateScanResultFeedbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateScanResultFeedbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.feedback):
            body['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.query_request_id):
            body['QueryRequestId'] = request.query_request_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateScanResultFeedback',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.UpdateScanResultFeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scan_result_feedback_with_options_async(
        self,
        request: green_20220926_models.UpdateScanResultFeedbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.UpdateScanResultFeedbackResponse:
        """
        @summary 检测结果反馈
        
        @param request: UpdateScanResultFeedbackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateScanResultFeedbackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.feedback):
            body['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.query_request_id):
            body['QueryRequestId'] = request.query_request_id
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.risk_level):
            body['RiskLevel'] = request.risk_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateScanResultFeedback',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.UpdateScanResultFeedbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scan_result_feedback(
        self,
        request: green_20220926_models.UpdateScanResultFeedbackRequest,
    ) -> green_20220926_models.UpdateScanResultFeedbackResponse:
        """
        @summary 检测结果反馈
        
        @param request: UpdateScanResultFeedbackRequest
        @return: UpdateScanResultFeedbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_scan_result_feedback_with_options(request, runtime)

    async def update_scan_result_feedback_async(
        self,
        request: green_20220926_models.UpdateScanResultFeedbackRequest,
    ) -> green_20220926_models.UpdateScanResultFeedbackResponse:
        """
        @summary 检测结果反馈
        
        @param request: UpdateScanResultFeedbackRequest
        @return: UpdateScanResultFeedbackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_scan_result_feedback_with_options_async(request, runtime)

    def update_service_config_with_options(
        self,
        request: green_20220926_models.UpdateServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.UpdateServiceConfigResponse:
        """
        @summary 更新服务
        
        @param request: UpdateServiceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.file_config):
            body['FileConfig'] = request.file_config
        if not UtilClient.is_unset(request.keyword_filter_libs):
            body['KeywordFilterLibs'] = request.keyword_filter_libs
        if not UtilClient.is_unset(request.keyword_hit_libs):
            body['KeywordHitLibs'] = request.keyword_hit_libs
        if not UtilClient.is_unset(request.manual_machine_config):
            body['ManualMachineConfig'] = request.manual_machine_config
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.scene_config):
            body['SceneConfig'] = request.scene_config
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.service_config):
            body['ServiceConfig'] = request.service_config
        if not UtilClient.is_unset(request.video_config):
            body['VideoConfig'] = request.video_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.UpdateServiceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_config_with_options_async(
        self,
        request: green_20220926_models.UpdateServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> green_20220926_models.UpdateServiceConfigResponse:
        """
        @summary 更新服务
        
        @param request: UpdateServiceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.file_config):
            body['FileConfig'] = request.file_config
        if not UtilClient.is_unset(request.keyword_filter_libs):
            body['KeywordFilterLibs'] = request.keyword_filter_libs
        if not UtilClient.is_unset(request.keyword_hit_libs):
            body['KeywordHitLibs'] = request.keyword_hit_libs
        if not UtilClient.is_unset(request.manual_machine_config):
            body['ManualMachineConfig'] = request.manual_machine_config
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.scene_config):
            body['SceneConfig'] = request.scene_config
        if not UtilClient.is_unset(request.service_code):
            body['ServiceCode'] = request.service_code
        if not UtilClient.is_unset(request.service_config):
            body['ServiceConfig'] = request.service_config
        if not UtilClient.is_unset(request.video_config):
            body['VideoConfig'] = request.video_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceConfig',
            version='2022-09-26',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            green_20220926_models.UpdateServiceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_config(
        self,
        request: green_20220926_models.UpdateServiceConfigRequest,
    ) -> green_20220926_models.UpdateServiceConfigResponse:
        """
        @summary 更新服务
        
        @param request: UpdateServiceConfigRequest
        @return: UpdateServiceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_service_config_with_options(request, runtime)

    async def update_service_config_async(
        self,
        request: green_20220926_models.UpdateServiceConfigRequest,
    ) -> green_20220926_models.UpdateServiceConfigResponse:
        """
        @summary 更新服务
        
        @param request: UpdateServiceConfigRequest
        @return: UpdateServiceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_service_config_with_options_async(request, runtime)
