# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rai20240701 import models as rai20240701_models
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
        self._endpoint = self.get_endpoint('rai', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_content_async_detect_with_options(
        self,
        request: rai20240701_models.BatchContentAsyncDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.BatchContentAsyncDetectResponse:
        """
        @summary BatchContentAsyncDetect
        
        @param request: BatchContentAsyncDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchContentAsyncDetectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        body = {}
        if not UtilClient.is_unset(request.service_parameter_list):
            body['serviceParameterList'] = request.service_parameter_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchContentAsyncDetect',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.BatchContentAsyncDetectResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_content_async_detect_with_options_async(
        self,
        request: rai20240701_models.BatchContentAsyncDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.BatchContentAsyncDetectResponse:
        """
        @summary BatchContentAsyncDetect
        
        @param request: BatchContentAsyncDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchContentAsyncDetectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        body = {}
        if not UtilClient.is_unset(request.service_parameter_list):
            body['serviceParameterList'] = request.service_parameter_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchContentAsyncDetect',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.BatchContentAsyncDetectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_content_async_detect(
        self,
        request: rai20240701_models.BatchContentAsyncDetectRequest,
    ) -> rai20240701_models.BatchContentAsyncDetectResponse:
        """
        @summary BatchContentAsyncDetect
        
        @param request: BatchContentAsyncDetectRequest
        @return: BatchContentAsyncDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_content_async_detect_with_options(request, runtime)

    async def batch_content_async_detect_async(
        self,
        request: rai20240701_models.BatchContentAsyncDetectRequest,
    ) -> rai20240701_models.BatchContentAsyncDetectResponse:
        """
        @summary BatchContentAsyncDetect
        
        @param request: BatchContentAsyncDetectRequest
        @return: BatchContentAsyncDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_content_async_detect_with_options_async(request, runtime)

    def batch_content_sync_detect_with_options(
        self,
        request: rai20240701_models.BatchContentSyncDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.BatchContentSyncDetectResponse:
        """
        @summary BatchContentSyncDetect
        
        @param request: BatchContentSyncDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchContentSyncDetectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        body = {}
        if not UtilClient.is_unset(request.service_parameter_list):
            body['serviceParameterList'] = request.service_parameter_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchContentSyncDetect',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.BatchContentSyncDetectResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_content_sync_detect_with_options_async(
        self,
        request: rai20240701_models.BatchContentSyncDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.BatchContentSyncDetectResponse:
        """
        @summary BatchContentSyncDetect
        
        @param request: BatchContentSyncDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchContentSyncDetectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        body = {}
        if not UtilClient.is_unset(request.service_parameter_list):
            body['serviceParameterList'] = request.service_parameter_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchContentSyncDetect',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.BatchContentSyncDetectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_content_sync_detect(
        self,
        request: rai20240701_models.BatchContentSyncDetectRequest,
    ) -> rai20240701_models.BatchContentSyncDetectResponse:
        """
        @summary BatchContentSyncDetect
        
        @param request: BatchContentSyncDetectRequest
        @return: BatchContentSyncDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_content_sync_detect_with_options(request, runtime)

    async def batch_content_sync_detect_async(
        self,
        request: rai20240701_models.BatchContentSyncDetectRequest,
    ) -> rai20240701_models.BatchContentSyncDetectResponse:
        """
        @summary BatchContentSyncDetect
        
        @param request: BatchContentSyncDetectRequest
        @return: BatchContentSyncDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_content_sync_detect_with_options_async(request, runtime)

    def check_account_with_options(
        self,
        request: rai20240701_models.CheckAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.CheckAccountResponse:
        """
        @summary 检查用户是否开通RAI服务
        
        @param request: CheckAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckAccount',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.CheckAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_account_with_options_async(
        self,
        request: rai20240701_models.CheckAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.CheckAccountResponse:
        """
        @summary 检查用户是否开通RAI服务
        
        @param request: CheckAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckAccount',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.CheckAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_account(
        self,
        request: rai20240701_models.CheckAccountRequest,
    ) -> rai20240701_models.CheckAccountResponse:
        """
        @summary 检查用户是否开通RAI服务
        
        @param request: CheckAccountRequest
        @return: CheckAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_account_with_options(request, runtime)

    async def check_account_async(
        self,
        request: rai20240701_models.CheckAccountRequest,
    ) -> rai20240701_models.CheckAccountResponse:
        """
        @summary 检查用户是否开通RAI服务
        
        @param request: CheckAccountRequest
        @return: CheckAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_account_with_options_async(request, runtime)

    def content_async_detect_with_options(
        self,
        request: rai20240701_models.ContentAsyncDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ContentAsyncDetectResponse:
        """
        @summary ContentAsyncDetect
        
        @param request: ContentAsyncDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContentAsyncDetectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        body = {}
        if not UtilClient.is_unset(request.service_parameter):
            body['serviceParameter'] = request.service_parameter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ContentAsyncDetect',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.ContentAsyncDetectResponse(),
            self.call_api(params, req, runtime)
        )

    async def content_async_detect_with_options_async(
        self,
        request: rai20240701_models.ContentAsyncDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ContentAsyncDetectResponse:
        """
        @summary ContentAsyncDetect
        
        @param request: ContentAsyncDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContentAsyncDetectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        body = {}
        if not UtilClient.is_unset(request.service_parameter):
            body['serviceParameter'] = request.service_parameter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ContentAsyncDetect',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.ContentAsyncDetectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def content_async_detect(
        self,
        request: rai20240701_models.ContentAsyncDetectRequest,
    ) -> rai20240701_models.ContentAsyncDetectResponse:
        """
        @summary ContentAsyncDetect
        
        @param request: ContentAsyncDetectRequest
        @return: ContentAsyncDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.content_async_detect_with_options(request, runtime)

    async def content_async_detect_async(
        self,
        request: rai20240701_models.ContentAsyncDetectRequest,
    ) -> rai20240701_models.ContentAsyncDetectResponse:
        """
        @summary ContentAsyncDetect
        
        @param request: ContentAsyncDetectRequest
        @return: ContentAsyncDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.content_async_detect_with_options_async(request, runtime)

    def content_sync_detect_with_options(
        self,
        request: rai20240701_models.ContentSyncDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ContentSyncDetectResponse:
        """
        @summary ContentSyncDetect
        
        @param request: ContentSyncDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContentSyncDetectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        body = {}
        if not UtilClient.is_unset(request.service_parameter):
            body['serviceParameter'] = request.service_parameter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ContentSyncDetect',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.ContentSyncDetectResponse(),
            self.call_api(params, req, runtime)
        )

    async def content_sync_detect_with_options_async(
        self,
        request: rai20240701_models.ContentSyncDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ContentSyncDetectResponse:
        """
        @summary ContentSyncDetect
        
        @param request: ContentSyncDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContentSyncDetectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        body = {}
        if not UtilClient.is_unset(request.service_parameter):
            body['serviceParameter'] = request.service_parameter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ContentSyncDetect',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.ContentSyncDetectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def content_sync_detect(
        self,
        request: rai20240701_models.ContentSyncDetectRequest,
    ) -> rai20240701_models.ContentSyncDetectResponse:
        """
        @summary ContentSyncDetect
        
        @param request: ContentSyncDetectRequest
        @return: ContentSyncDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.content_sync_detect_with_options(request, runtime)

    async def content_sync_detect_async(
        self,
        request: rai20240701_models.ContentSyncDetectRequest,
    ) -> rai20240701_models.ContentSyncDetectResponse:
        """
        @summary ContentSyncDetect
        
        @param request: ContentSyncDetectRequest
        @return: ContentSyncDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.content_sync_detect_with_options_async(request, runtime)

    def get_content_detect_result_with_options(
        self,
        request: rai20240701_models.GetContentDetectResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.GetContentDetectResultResponse:
        """
        @summary GetContentDetectResult
        
        @param request: GetContentDetectResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetContentDetectResultResponse
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
            action='GetContentDetectResult',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.GetContentDetectResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_content_detect_result_with_options_async(
        self,
        request: rai20240701_models.GetContentDetectResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.GetContentDetectResultResponse:
        """
        @summary GetContentDetectResult
        
        @param request: GetContentDetectResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetContentDetectResultResponse
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
            action='GetContentDetectResult',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.GetContentDetectResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_content_detect_result(
        self,
        request: rai20240701_models.GetContentDetectResultRequest,
    ) -> rai20240701_models.GetContentDetectResultResponse:
        """
        @summary GetContentDetectResult
        
        @param request: GetContentDetectResultRequest
        @return: GetContentDetectResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_content_detect_result_with_options(request, runtime)

    async def get_content_detect_result_async(
        self,
        request: rai20240701_models.GetContentDetectResultRequest,
    ) -> rai20240701_models.GetContentDetectResultResponse:
        """
        @summary GetContentDetectResult
        
        @param request: GetContentDetectResultRequest
        @return: GetContentDetectResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_content_detect_result_with_options_async(request, runtime)

    def list_sensitive_word_with_options(
        self,
        request: rai20240701_models.ListSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ListSensitiveWordResponse:
        """
        @summary ListSensitiveWord
        
        @param request: ListSensitiveWordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSensitiveWordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSensitiveWord',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.ListSensitiveWordResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_sensitive_word_with_options_async(
        self,
        request: rai20240701_models.ListSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ListSensitiveWordResponse:
        """
        @summary ListSensitiveWord
        
        @param request: ListSensitiveWordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSensitiveWordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSensitiveWord',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.ListSensitiveWordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_sensitive_word(
        self,
        request: rai20240701_models.ListSensitiveWordRequest,
    ) -> rai20240701_models.ListSensitiveWordResponse:
        """
        @summary ListSensitiveWord
        
        @param request: ListSensitiveWordRequest
        @return: ListSensitiveWordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_sensitive_word_with_options(request, runtime)

    async def list_sensitive_word_async(
        self,
        request: rai20240701_models.ListSensitiveWordRequest,
    ) -> rai20240701_models.ListSensitiveWordResponse:
        """
        @summary ListSensitiveWord
        
        @param request: ListSensitiveWordRequest
        @return: ListSensitiveWordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_sensitive_word_with_options_async(request, runtime)

    def register_account_with_options(
        self,
        request: rai20240701_models.RegisterAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.RegisterAccountResponse:
        """
        @summary 注册RAI账号
        
        @param request: RegisterAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.memo):
            query['Memo'] = request.memo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterAccount',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.RegisterAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_account_with_options_async(
        self,
        request: rai20240701_models.RegisterAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.RegisterAccountResponse:
        """
        @summary 注册RAI账号
        
        @param request: RegisterAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.memo):
            query['Memo'] = request.memo
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterAccount',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.RegisterAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_account(
        self,
        request: rai20240701_models.RegisterAccountRequest,
    ) -> rai20240701_models.RegisterAccountResponse:
        """
        @summary 注册RAI账号
        
        @param request: RegisterAccountRequest
        @return: RegisterAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_account_with_options(request, runtime)

    async def register_account_async(
        self,
        request: rai20240701_models.RegisterAccountRequest,
    ) -> rai20240701_models.RegisterAccountResponse:
        """
        @summary 注册RAI账号
        
        @param request: RegisterAccountRequest
        @return: RegisterAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.register_account_with_options_async(request, runtime)

    def sync_sensitive_word_with_options(
        self,
        tmp_req: rai20240701_models.SyncSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.SyncSensitiveWordResponse:
        """
        @summary SyncSensitiveWord
        
        @param tmp_req: SyncSensitiveWordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncSensitiveWordResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.SyncSensitiveWordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.commit):
            query['Commit'] = request.commit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncSensitiveWord',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.SyncSensitiveWordResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_sensitive_word_with_options_async(
        self,
        tmp_req: rai20240701_models.SyncSensitiveWordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.SyncSensitiveWordResponse:
        """
        @summary SyncSensitiveWord
        
        @param tmp_req: SyncSensitiveWordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncSensitiveWordResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.SyncSensitiveWordShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.commit):
            query['Commit'] = request.commit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncSensitiveWord',
            version='2024-07-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rai20240701_models.SyncSensitiveWordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_sensitive_word(
        self,
        request: rai20240701_models.SyncSensitiveWordRequest,
    ) -> rai20240701_models.SyncSensitiveWordResponse:
        """
        @summary SyncSensitiveWord
        
        @param request: SyncSensitiveWordRequest
        @return: SyncSensitiveWordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sync_sensitive_word_with_options(request, runtime)

    async def sync_sensitive_word_async(
        self,
        request: rai20240701_models.SyncSensitiveWordRequest,
    ) -> rai20240701_models.SyncSensitiveWordResponse:
        """
        @summary SyncSensitiveWord
        
        @param request: SyncSensitiveWordRequest
        @return: SyncSensitiveWordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sync_sensitive_word_with_options_async(request, runtime)
