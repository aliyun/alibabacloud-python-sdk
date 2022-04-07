# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_yuqing20220301 import models as yuqing_20220301_models
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
        self._endpoint = self.get_endpoint('yuqing', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def close_product(
        self,
        request: yuqing_20220301_models.CloseProductRequest,
    ) -> yuqing_20220301_models.CloseProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.close_product_with_options(request, headers, runtime)

    async def close_product_async(
        self,
        request: yuqing_20220301_models.CloseProductRequest,
    ) -> yuqing_20220301_models.CloseProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.close_product_with_options_async(request, headers, runtime)

    def close_product_with_options(
        self,
        request: yuqing_20220301_models.CloseProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.CloseProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.product_instance):
            body['productInstance'] = request.product_instance
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseProduct',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/closeProduct.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.CloseProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_product_with_options_async(
        self,
        request: yuqing_20220301_models.CloseProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.CloseProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.product_instance):
            body['productInstance'] = request.product_instance
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseProduct',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/closeProduct.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.CloseProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def console_proxy(
        self,
        request: yuqing_20220301_models.ConsoleProxyRequest,
    ) -> yuqing_20220301_models.ConsoleProxyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.console_proxy_with_options(request, headers, runtime)

    async def console_proxy_async(
        self,
        request: yuqing_20220301_models.ConsoleProxyRequest,
    ) -> yuqing_20220301_models.ConsoleProxyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.console_proxy_with_options_async(request, headers, runtime)

    def console_proxy_with_options(
        self,
        request: yuqing_20220301_models.ConsoleProxyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.ConsoleProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.app_code):
            body['appCode'] = request.app_code
        if not UtilClient.is_unset(request.interface_name):
            body['interfaceName'] = request.interface_name
        if not UtilClient.is_unset(request.param_json):
            body['paramJson'] = request.param_json
        if not UtilClient.is_unset(request.team_hash_id):
            body['teamHashId'] = request.team_hash_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConsoleProxy',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/consoleProxy.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.ConsoleProxyResponse(),
            self.call_api(params, req, runtime)
        )

    async def console_proxy_with_options_async(
        self,
        request: yuqing_20220301_models.ConsoleProxyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.ConsoleProxyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.app_code):
            body['appCode'] = request.app_code
        if not UtilClient.is_unset(request.interface_name):
            body['interfaceName'] = request.interface_name
        if not UtilClient.is_unset(request.param_json):
            body['paramJson'] = request.param_json
        if not UtilClient.is_unset(request.team_hash_id):
            body['teamHashId'] = request.team_hash_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConsoleProxy',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/consoleProxy.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.ConsoleProxyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_analysis_task_result(
        self,
        request: yuqing_20220301_models.GetAnalysisTaskResultRequest,
    ) -> yuqing_20220301_models.GetAnalysisTaskResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_analysis_task_result_with_options(request, headers, runtime)

    async def get_analysis_task_result_async(
        self,
        request: yuqing_20220301_models.GetAnalysisTaskResultRequest,
    ) -> yuqing_20220301_models.GetAnalysisTaskResultResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_analysis_task_result_with_options_async(request, headers, runtime)

    def get_analysis_task_result_with_options(
        self,
        request: yuqing_20220301_models.GetAnalysisTaskResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.GetAnalysisTaskResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_id):
            query['analysisId'] = request.analysis_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAnalysisTaskResult',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/getAnalysisComponentResult.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.GetAnalysisTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_analysis_task_result_with_options_async(
        self,
        request: yuqing_20220301_models.GetAnalysisTaskResultRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.GetAnalysisTaskResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.analysis_id):
            query['analysisId'] = request.analysis_id
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.team_hash_id):
            query['teamHashId'] = request.team_hash_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAnalysisTaskResult',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/getAnalysisComponentResult.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.GetAnalysisTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_product(
        self,
        request: yuqing_20220301_models.OpenProductRequest,
    ) -> yuqing_20220301_models.OpenProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.open_product_with_options(request, headers, runtime)

    async def open_product_async(
        self,
        request: yuqing_20220301_models.OpenProductRequest,
    ) -> yuqing_20220301_models.OpenProductResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.open_product_with_options_async(request, headers, runtime)

    def open_product_with_options(
        self,
        request: yuqing_20220301_models.OpenProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.OpenProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.product_instance):
            body['productInstance'] = request.product_instance
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenProduct',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/openProduct.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.OpenProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_product_with_options_async(
        self,
        request: yuqing_20220301_models.OpenProductRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.OpenProductResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.product_instance):
            body['productInstance'] = request.product_instance
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenProduct',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/openProduct.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.OpenProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_product_instance_list(
        self,
        request: yuqing_20220301_models.QueryProductInstanceListRequest,
    ) -> yuqing_20220301_models.QueryProductInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_product_instance_list_with_options(request, headers, runtime)

    async def query_product_instance_list_async(
        self,
        request: yuqing_20220301_models.QueryProductInstanceListRequest,
    ) -> yuqing_20220301_models.QueryProductInstanceListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_product_instance_list_with_options_async(request, headers, runtime)

    def query_product_instance_list_with_options(
        self,
        request: yuqing_20220301_models.QueryProductInstanceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.QueryProductInstanceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['appCode'] = request.app_code
        if not UtilClient.is_unset(request.from_time):
            query['fromTime'] = request.from_time
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.tenant_uid):
            query['tenantUid'] = request.tenant_uid
        if not UtilClient.is_unset(request.to_time):
            query['toTime'] = request.to_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProductInstanceList',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/queryProductInstanceList.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.QueryProductInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_product_instance_list_with_options_async(
        self,
        request: yuqing_20220301_models.QueryProductInstanceListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.QueryProductInstanceListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_code):
            query['appCode'] = request.app_code
        if not UtilClient.is_unset(request.from_time):
            query['fromTime'] = request.from_time
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        if not UtilClient.is_unset(request.tenant_uid):
            query['tenantUid'] = request.tenant_uid
        if not UtilClient.is_unset(request.to_time):
            query['toTime'] = request.to_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProductInstanceList',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/queryProductInstanceList.json',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.QueryProductInstanceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_yuqing_message(
        self,
        request: yuqing_20220301_models.QueryYuqingMessageRequest,
    ) -> yuqing_20220301_models.QueryYuqingMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_yuqing_message_with_options(request, headers, runtime)

    async def query_yuqing_message_async(
        self,
        request: yuqing_20220301_models.QueryYuqingMessageRequest,
    ) -> yuqing_20220301_models.QueryYuqingMessageResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_yuqing_message_with_options_async(request, headers, runtime)

    def query_yuqing_message_with_options(
        self,
        request: yuqing_20220301_models.QueryYuqingMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.QueryYuqingMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.search_condition):
            body['searchCondition'] = request.search_condition
        if not UtilClient.is_unset(request.team_hash_id):
            body['teamHashId'] = request.team_hash_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryYuqingMessage',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/queryYuqingMessage.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.QueryYuqingMessageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_yuqing_message_with_options_async(
        self,
        request: yuqing_20220301_models.QueryYuqingMessageRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.QueryYuqingMessageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.search_condition):
            body['searchCondition'] = request.search_condition
        if not UtilClient.is_unset(request.team_hash_id):
            body['teamHashId'] = request.team_hash_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryYuqingMessage',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/queryYuqingMessage.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.QueryYuqingMessageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_analysis_task(
        self,
        request: yuqing_20220301_models.SubmitAnalysisTaskRequest,
    ) -> yuqing_20220301_models.SubmitAnalysisTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.submit_analysis_task_with_options(request, headers, runtime)

    async def submit_analysis_task_async(
        self,
        request: yuqing_20220301_models.SubmitAnalysisTaskRequest,
    ) -> yuqing_20220301_models.SubmitAnalysisTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.submit_analysis_task_with_options_async(request, headers, runtime)

    def submit_analysis_task_with_options(
        self,
        request: yuqing_20220301_models.SubmitAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.SubmitAnalysisTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.analyse_type):
            body['analyseType'] = request.analyse_type
        if not UtilClient.is_unset(request.search_condition):
            body['searchCondition'] = request.search_condition
        if not UtilClient.is_unset(request.team_hash_id):
            body['teamHashId'] = request.team_hash_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitAnalysisTask',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/submitAnalysisComponent.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.SubmitAnalysisTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_analysis_task_with_options_async(
        self,
        request: yuqing_20220301_models.SubmitAnalysisTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> yuqing_20220301_models.SubmitAnalysisTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.request_id):
            query['requestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.analyse_type):
            body['analyseType'] = request.analyse_type
        if not UtilClient.is_unset(request.search_condition):
            body['searchCondition'] = request.search_condition
        if not UtilClient.is_unset(request.team_hash_id):
            body['teamHashId'] = request.team_hash_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitAnalysisTask',
            version='2022-03-01',
            protocol='HTTPS',
            pathname=f'/openapi/aliyun/submitAnalysisComponent.json',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yuqing_20220301_models.SubmitAnalysisTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )
