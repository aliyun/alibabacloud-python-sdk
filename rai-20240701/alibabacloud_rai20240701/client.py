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

    def create_model_instance_with_options(
        self,
        request: rai20240701_models.CreateModelInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.CreateModelInstanceResponse:
        """
        @summary CreateModelInstance
        
        @param request: CreateModelInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModelInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.eas_service_id):
            query['EasServiceId'] = request.eas_service_id
        if not UtilClient.is_unset(request.eas_service_name):
            query['EasServiceName'] = request.eas_service_name
        if not UtilClient.is_unset(request.model_call_name):
            query['ModelCallName'] = request.model_call_name
        if not UtilClient.is_unset(request.model_category_id):
            query['ModelCategoryId'] = request.model_category_id
        if not UtilClient.is_unset(request.model_token):
            query['ModelToken'] = request.model_token
        if not UtilClient.is_unset(request.model_url):
            query['ModelUrl'] = request.model_url
        if not UtilClient.is_unset(request.model_vpc_url):
            query['ModelVpcUrl'] = request.model_vpc_url
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateModelInstance',
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
            rai20240701_models.CreateModelInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_model_instance_with_options_async(
        self,
        request: rai20240701_models.CreateModelInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.CreateModelInstanceResponse:
        """
        @summary CreateModelInstance
        
        @param request: CreateModelInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModelInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.eas_service_id):
            query['EasServiceId'] = request.eas_service_id
        if not UtilClient.is_unset(request.eas_service_name):
            query['EasServiceName'] = request.eas_service_name
        if not UtilClient.is_unset(request.model_call_name):
            query['ModelCallName'] = request.model_call_name
        if not UtilClient.is_unset(request.model_category_id):
            query['ModelCategoryId'] = request.model_category_id
        if not UtilClient.is_unset(request.model_token):
            query['ModelToken'] = request.model_token
        if not UtilClient.is_unset(request.model_url):
            query['ModelUrl'] = request.model_url
        if not UtilClient.is_unset(request.model_vpc_url):
            query['ModelVpcUrl'] = request.model_vpc_url
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateModelInstance',
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
            rai20240701_models.CreateModelInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_model_instance(
        self,
        request: rai20240701_models.CreateModelInstanceRequest,
    ) -> rai20240701_models.CreateModelInstanceResponse:
        """
        @summary CreateModelInstance
        
        @param request: CreateModelInstanceRequest
        @return: CreateModelInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_model_instance_with_options(request, runtime)

    async def create_model_instance_async(
        self,
        request: rai20240701_models.CreateModelInstanceRequest,
    ) -> rai20240701_models.CreateModelInstanceResponse:
        """
        @summary CreateModelInstance
        
        @param request: CreateModelInstanceRequest
        @return: CreateModelInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_model_instance_with_options_async(request, runtime)

    def create_policy_with_options(
        self,
        tmp_req: rai20240701_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.CreatePolicyResponse:
        """
        @summary CreatePolicy
        
        @param tmp_req: CreatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.CreatePolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.harmful_category_config_info_list):
            request.harmful_category_config_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.harmful_category_config_info_list, 'HarmfulCategoryConfigInfoList', 'json')
        if not UtilClient.is_unset(tmp_req.prompt_attack_info):
            request.prompt_attack_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prompt_attack_info, 'PromptAttackInfo', 'json')
        if not UtilClient.is_unset(tmp_req.prompt_attack_info_list):
            request.prompt_attack_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prompt_attack_info_list, 'PromptAttackInfoList', 'json')
        if not UtilClient.is_unset(tmp_req.regular_express_list):
            request.regular_express_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.regular_express_list, 'RegularExpressList', 'json')
        if not UtilClient.is_unset(tmp_req.sensitive_config_list):
            request.sensitive_config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sensitive_config_list, 'SensitiveConfigList', 'json')
        if not UtilClient.is_unset(tmp_req.sensitive_topic_list):
            request.sensitive_topic_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sensitive_topic_list, 'SensitiveTopicList', 'json')
        if not UtilClient.is_unset(tmp_req.sensitive_word_list):
            request.sensitive_word_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sensitive_word_list, 'SensitiveWordList', 'json')
        if not UtilClient.is_unset(tmp_req.topic_config_info_list):
            request.topic_config_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topic_config_info_list, 'TopicConfigInfoList', 'json')
        if not UtilClient.is_unset(tmp_req.word_group_info_list):
            request.word_group_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.word_group_info_list, 'WordGroupInfoList', 'json')
        query = {}
        if not UtilClient.is_unset(request.content_safe_model_instance_id):
            query['ContentSafeModelInstanceId'] = request.content_safe_model_instance_id
        if not UtilClient.is_unset(request.enable_sensitive_input_check):
            query['EnableSensitiveInputCheck'] = request.enable_sensitive_input_check
        if not UtilClient.is_unset(request.enable_sensitive_output_check):
            query['EnableSensitiveOutputCheck'] = request.enable_sensitive_output_check
        if not UtilClient.is_unset(request.harmful_category_config_info_list_shrink):
            query['HarmfulCategoryConfigInfoList'] = request.harmful_category_config_info_list_shrink
        if not UtilClient.is_unset(request.input_safe_answer):
            query['InputSafeAnswer'] = request.input_safe_answer
        if not UtilClient.is_unset(request.input_safe_answer_switch):
            query['InputSafeAnswerSwitch'] = request.input_safe_answer_switch
        if not UtilClient.is_unset(request.is_sidecar_policy):
            query['IsSidecarPolicy'] = request.is_sidecar_policy
        if not UtilClient.is_unset(request.output_safe_answer):
            query['OutputSafeAnswer'] = request.output_safe_answer
        if not UtilClient.is_unset(request.output_safe_answer_switch):
            query['OutputSafeAnswerSwitch'] = request.output_safe_answer_switch
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.prompt_attack_info_shrink):
            query['PromptAttackInfo'] = request.prompt_attack_info_shrink
        if not UtilClient.is_unset(request.prompt_attack_info_list_shrink):
            query['PromptAttackInfoList'] = request.prompt_attack_info_list_shrink
        if not UtilClient.is_unset(request.prompt_attack_model_instance_id):
            query['PromptAttackModelInstanceId'] = request.prompt_attack_model_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.regular_express_list_shrink):
            query['RegularExpressList'] = request.regular_express_list_shrink
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.sensitive_config_list_shrink):
            query['SensitiveConfigList'] = request.sensitive_config_list_shrink
        if not UtilClient.is_unset(request.sensitive_topic_list_shrink):
            query['SensitiveTopicList'] = request.sensitive_topic_list_shrink
        if not UtilClient.is_unset(request.sensitive_topic_model_instance_id):
            query['SensitiveTopicModelInstanceId'] = request.sensitive_topic_model_instance_id
        if not UtilClient.is_unset(request.sensitive_word_list_shrink):
            query['SensitiveWordList'] = request.sensitive_word_list_shrink
        if not UtilClient.is_unset(request.topic_config_info_list_shrink):
            query['TopicConfigInfoList'] = request.topic_config_info_list_shrink
        if not UtilClient.is_unset(request.word_group_info_list_shrink):
            query['WordGroupInfoList'] = request.word_group_info_list_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
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
            rai20240701_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_policy_with_options_async(
        self,
        tmp_req: rai20240701_models.CreatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.CreatePolicyResponse:
        """
        @summary CreatePolicy
        
        @param tmp_req: CreatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreatePolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.CreatePolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.harmful_category_config_info_list):
            request.harmful_category_config_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.harmful_category_config_info_list, 'HarmfulCategoryConfigInfoList', 'json')
        if not UtilClient.is_unset(tmp_req.prompt_attack_info):
            request.prompt_attack_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prompt_attack_info, 'PromptAttackInfo', 'json')
        if not UtilClient.is_unset(tmp_req.prompt_attack_info_list):
            request.prompt_attack_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prompt_attack_info_list, 'PromptAttackInfoList', 'json')
        if not UtilClient.is_unset(tmp_req.regular_express_list):
            request.regular_express_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.regular_express_list, 'RegularExpressList', 'json')
        if not UtilClient.is_unset(tmp_req.sensitive_config_list):
            request.sensitive_config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sensitive_config_list, 'SensitiveConfigList', 'json')
        if not UtilClient.is_unset(tmp_req.sensitive_topic_list):
            request.sensitive_topic_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sensitive_topic_list, 'SensitiveTopicList', 'json')
        if not UtilClient.is_unset(tmp_req.sensitive_word_list):
            request.sensitive_word_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sensitive_word_list, 'SensitiveWordList', 'json')
        if not UtilClient.is_unset(tmp_req.topic_config_info_list):
            request.topic_config_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topic_config_info_list, 'TopicConfigInfoList', 'json')
        if not UtilClient.is_unset(tmp_req.word_group_info_list):
            request.word_group_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.word_group_info_list, 'WordGroupInfoList', 'json')
        query = {}
        if not UtilClient.is_unset(request.content_safe_model_instance_id):
            query['ContentSafeModelInstanceId'] = request.content_safe_model_instance_id
        if not UtilClient.is_unset(request.enable_sensitive_input_check):
            query['EnableSensitiveInputCheck'] = request.enable_sensitive_input_check
        if not UtilClient.is_unset(request.enable_sensitive_output_check):
            query['EnableSensitiveOutputCheck'] = request.enable_sensitive_output_check
        if not UtilClient.is_unset(request.harmful_category_config_info_list_shrink):
            query['HarmfulCategoryConfigInfoList'] = request.harmful_category_config_info_list_shrink
        if not UtilClient.is_unset(request.input_safe_answer):
            query['InputSafeAnswer'] = request.input_safe_answer
        if not UtilClient.is_unset(request.input_safe_answer_switch):
            query['InputSafeAnswerSwitch'] = request.input_safe_answer_switch
        if not UtilClient.is_unset(request.is_sidecar_policy):
            query['IsSidecarPolicy'] = request.is_sidecar_policy
        if not UtilClient.is_unset(request.output_safe_answer):
            query['OutputSafeAnswer'] = request.output_safe_answer
        if not UtilClient.is_unset(request.output_safe_answer_switch):
            query['OutputSafeAnswerSwitch'] = request.output_safe_answer_switch
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.prompt_attack_info_shrink):
            query['PromptAttackInfo'] = request.prompt_attack_info_shrink
        if not UtilClient.is_unset(request.prompt_attack_info_list_shrink):
            query['PromptAttackInfoList'] = request.prompt_attack_info_list_shrink
        if not UtilClient.is_unset(request.prompt_attack_model_instance_id):
            query['PromptAttackModelInstanceId'] = request.prompt_attack_model_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.regular_express_list_shrink):
            query['RegularExpressList'] = request.regular_express_list_shrink
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.sensitive_config_list_shrink):
            query['SensitiveConfigList'] = request.sensitive_config_list_shrink
        if not UtilClient.is_unset(request.sensitive_topic_list_shrink):
            query['SensitiveTopicList'] = request.sensitive_topic_list_shrink
        if not UtilClient.is_unset(request.sensitive_topic_model_instance_id):
            query['SensitiveTopicModelInstanceId'] = request.sensitive_topic_model_instance_id
        if not UtilClient.is_unset(request.sensitive_word_list_shrink):
            query['SensitiveWordList'] = request.sensitive_word_list_shrink
        if not UtilClient.is_unset(request.topic_config_info_list_shrink):
            query['TopicConfigInfoList'] = request.topic_config_info_list_shrink
        if not UtilClient.is_unset(request.word_group_info_list_shrink):
            query['WordGroupInfoList'] = request.word_group_info_list_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
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
            rai20240701_models.CreatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_policy(
        self,
        request: rai20240701_models.CreatePolicyRequest,
    ) -> rai20240701_models.CreatePolicyResponse:
        """
        @summary CreatePolicy
        
        @param request: CreatePolicyRequest
        @return: CreatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    async def create_policy_async(
        self,
        request: rai20240701_models.CreatePolicyRequest,
    ) -> rai20240701_models.CreatePolicyResponse:
        """
        @summary CreatePolicy
        
        @param request: CreatePolicyRequest
        @return: CreatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_policy_with_options_async(request, runtime)

    def create_topic_with_options(
        self,
        tmp_req: rai20240701_models.CreateTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.CreateTopicResponse:
        """
        @summary CreateTopic
        
        @param tmp_req: CreateTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTopicResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.CreateTopicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic_definition):
            query['TopicDefinition'] = request.topic_definition
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTopic',
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
            rai20240701_models.CreateTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_topic_with_options_async(
        self,
        tmp_req: rai20240701_models.CreateTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.CreateTopicResponse:
        """
        @summary CreateTopic
        
        @param tmp_req: CreateTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTopicResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.CreateTopicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic_definition):
            query['TopicDefinition'] = request.topic_definition
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTopic',
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
            rai20240701_models.CreateTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_topic(
        self,
        request: rai20240701_models.CreateTopicRequest,
    ) -> rai20240701_models.CreateTopicResponse:
        """
        @summary CreateTopic
        
        @param request: CreateTopicRequest
        @return: CreateTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_topic_with_options(request, runtime)

    async def create_topic_async(
        self,
        request: rai20240701_models.CreateTopicRequest,
    ) -> rai20240701_models.CreateTopicResponse:
        """
        @summary CreateTopic
        
        @param request: CreateTopicRequest
        @return: CreateTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_topic_with_options_async(request, runtime)

    def create_word_group_with_options(
        self,
        tmp_req: rai20240701_models.CreateWordGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.CreateWordGroupResponse:
        """
        @summary CreateWordGroup
        
        @param tmp_req: CreateWordGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWordGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.CreateWordGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.commit):
            query['Commit'] = request.commit
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWordGroup',
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
            rai20240701_models.CreateWordGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_word_group_with_options_async(
        self,
        tmp_req: rai20240701_models.CreateWordGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.CreateWordGroupResponse:
        """
        @summary CreateWordGroup
        
        @param tmp_req: CreateWordGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWordGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.CreateWordGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.commit):
            query['Commit'] = request.commit
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWordGroup',
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
            rai20240701_models.CreateWordGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_word_group(
        self,
        request: rai20240701_models.CreateWordGroupRequest,
    ) -> rai20240701_models.CreateWordGroupResponse:
        """
        @summary CreateWordGroup
        
        @param request: CreateWordGroupRequest
        @return: CreateWordGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_word_group_with_options(request, runtime)

    async def create_word_group_async(
        self,
        request: rai20240701_models.CreateWordGroupRequest,
    ) -> rai20240701_models.CreateWordGroupResponse:
        """
        @summary CreateWordGroup
        
        @param request: CreateWordGroupRequest
        @return: CreateWordGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_word_group_with_options_async(request, runtime)

    def delete_model_instance_with_options(
        self,
        tmp_req: rai20240701_models.DeleteModelInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.DeleteModelInstanceResponse:
        """
        @summary DeleteModelInstance
        
        @param tmp_req: DeleteModelInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModelInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.DeleteModelInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.model_instance_id_list):
            request.model_instance_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model_instance_id_list, 'ModelInstanceIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.model_instance_id_list_shrink):
            query['ModelInstanceIdList'] = request.model_instance_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteModelInstance',
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
            rai20240701_models.DeleteModelInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_model_instance_with_options_async(
        self,
        tmp_req: rai20240701_models.DeleteModelInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.DeleteModelInstanceResponse:
        """
        @summary DeleteModelInstance
        
        @param tmp_req: DeleteModelInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModelInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.DeleteModelInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.model_instance_id_list):
            request.model_instance_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.model_instance_id_list, 'ModelInstanceIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.model_instance_id_list_shrink):
            query['ModelInstanceIdList'] = request.model_instance_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteModelInstance',
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
            rai20240701_models.DeleteModelInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_model_instance(
        self,
        request: rai20240701_models.DeleteModelInstanceRequest,
    ) -> rai20240701_models.DeleteModelInstanceResponse:
        """
        @summary DeleteModelInstance
        
        @param request: DeleteModelInstanceRequest
        @return: DeleteModelInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_model_instance_with_options(request, runtime)

    async def delete_model_instance_async(
        self,
        request: rai20240701_models.DeleteModelInstanceRequest,
    ) -> rai20240701_models.DeleteModelInstanceResponse:
        """
        @summary DeleteModelInstance
        
        @param request: DeleteModelInstanceRequest
        @return: DeleteModelInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_model_instance_with_options_async(request, runtime)

    def delete_policy_with_options(
        self,
        tmp_req: rai20240701_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.DeletePolicyResponse:
        """
        @summary DeletePolicy
        
        @param tmp_req: DeletePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.DeletePolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.policy_id_list):
            request.policy_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy_id_list, 'PolicyIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.policy_id_list_shrink):
            query['PolicyIdList'] = request.policy_id_list_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
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
            rai20240701_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_policy_with_options_async(
        self,
        tmp_req: rai20240701_models.DeletePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.DeletePolicyResponse:
        """
        @summary DeletePolicy
        
        @param tmp_req: DeletePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.DeletePolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.policy_id_list):
            request.policy_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.policy_id_list, 'PolicyIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.policy_id_list_shrink):
            query['PolicyIdList'] = request.policy_id_list_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
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
            rai20240701_models.DeletePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_policy(
        self,
        request: rai20240701_models.DeletePolicyRequest,
    ) -> rai20240701_models.DeletePolicyResponse:
        """
        @summary DeletePolicy
        
        @param request: DeletePolicyRequest
        @return: DeletePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    async def delete_policy_async(
        self,
        request: rai20240701_models.DeletePolicyRequest,
    ) -> rai20240701_models.DeletePolicyResponse:
        """
        @summary DeletePolicy
        
        @param request: DeletePolicyRequest
        @return: DeletePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_policy_with_options_async(request, runtime)

    def delete_topic_with_options(
        self,
        tmp_req: rai20240701_models.DeleteTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.DeleteTopicResponse:
        """
        @summary DeleteTopic
        
        @param tmp_req: DeleteTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTopicResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.DeleteTopicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.topic_id_list):
            request.topic_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topic_id_list, 'TopicIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic_id_list_shrink):
            query['TopicIdList'] = request.topic_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTopic',
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
            rai20240701_models.DeleteTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_topic_with_options_async(
        self,
        tmp_req: rai20240701_models.DeleteTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.DeleteTopicResponse:
        """
        @summary DeleteTopic
        
        @param tmp_req: DeleteTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTopicResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.DeleteTopicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.topic_id_list):
            request.topic_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topic_id_list, 'TopicIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic_id_list_shrink):
            query['TopicIdList'] = request.topic_id_list_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTopic',
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
            rai20240701_models.DeleteTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_topic(
        self,
        request: rai20240701_models.DeleteTopicRequest,
    ) -> rai20240701_models.DeleteTopicResponse:
        """
        @summary DeleteTopic
        
        @param request: DeleteTopicRequest
        @return: DeleteTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_topic_with_options(request, runtime)

    async def delete_topic_async(
        self,
        request: rai20240701_models.DeleteTopicRequest,
    ) -> rai20240701_models.DeleteTopicResponse:
        """
        @summary DeleteTopic
        
        @param request: DeleteTopicRequest
        @return: DeleteTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_topic_with_options_async(request, runtime)

    def delete_word_group_with_options(
        self,
        tmp_req: rai20240701_models.DeleteWordGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.DeleteWordGroupResponse:
        """
        @summary DeleteWordGroup
        
        @param tmp_req: DeleteWordGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWordGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.DeleteWordGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.group_id_list):
            request.group_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_id_list, 'GroupIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.group_id_list_shrink):
            query['GroupIdList'] = request.group_id_list_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWordGroup',
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
            rai20240701_models.DeleteWordGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_word_group_with_options_async(
        self,
        tmp_req: rai20240701_models.DeleteWordGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.DeleteWordGroupResponse:
        """
        @summary DeleteWordGroup
        
        @param tmp_req: DeleteWordGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWordGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.DeleteWordGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.group_id_list):
            request.group_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.group_id_list, 'GroupIdList', 'json')
        query = {}
        if not UtilClient.is_unset(request.group_id_list_shrink):
            query['GroupIdList'] = request.group_id_list_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWordGroup',
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
            rai20240701_models.DeleteWordGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_word_group(
        self,
        request: rai20240701_models.DeleteWordGroupRequest,
    ) -> rai20240701_models.DeleteWordGroupResponse:
        """
        @summary DeleteWordGroup
        
        @param request: DeleteWordGroupRequest
        @return: DeleteWordGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_word_group_with_options(request, runtime)

    async def delete_word_group_async(
        self,
        request: rai20240701_models.DeleteWordGroupRequest,
    ) -> rai20240701_models.DeleteWordGroupResponse:
        """
        @summary DeleteWordGroup
        
        @param request: DeleteWordGroupRequest
        @return: DeleteWordGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_word_group_with_options_async(request, runtime)

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

    def get_model_input_content_detect_result_with_options(
        self,
        request: rai20240701_models.GetModelInputContentDetectResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.GetModelInputContentDetectResultResponse:
        """
        @summary GetModelInputContentDetectResult
        
        @param request: GetModelInputContentDetectResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelInputContentDetectResultResponse
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
            action='GetModelInputContentDetectResult',
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
            rai20240701_models.GetModelInputContentDetectResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_input_content_detect_result_with_options_async(
        self,
        request: rai20240701_models.GetModelInputContentDetectResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.GetModelInputContentDetectResultResponse:
        """
        @summary GetModelInputContentDetectResult
        
        @param request: GetModelInputContentDetectResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelInputContentDetectResultResponse
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
            action='GetModelInputContentDetectResult',
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
            rai20240701_models.GetModelInputContentDetectResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_input_content_detect_result(
        self,
        request: rai20240701_models.GetModelInputContentDetectResultRequest,
    ) -> rai20240701_models.GetModelInputContentDetectResultResponse:
        """
        @summary GetModelInputContentDetectResult
        
        @param request: GetModelInputContentDetectResultRequest
        @return: GetModelInputContentDetectResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_model_input_content_detect_result_with_options(request, runtime)

    async def get_model_input_content_detect_result_async(
        self,
        request: rai20240701_models.GetModelInputContentDetectResultRequest,
    ) -> rai20240701_models.GetModelInputContentDetectResultResponse:
        """
        @summary GetModelInputContentDetectResult
        
        @param request: GetModelInputContentDetectResultRequest
        @return: GetModelInputContentDetectResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_model_input_content_detect_result_with_options_async(request, runtime)

    def get_model_instance_info_with_options(
        self,
        request: rai20240701_models.GetModelInstanceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.GetModelInstanceInfoResponse:
        """
        @summary GetModelInstanceInfo
        
        @param request: GetModelInstanceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelInstanceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_instance_id):
            query['ModelInstanceId'] = request.model_instance_id
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetModelInstanceInfo',
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
            rai20240701_models.GetModelInstanceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_instance_info_with_options_async(
        self,
        request: rai20240701_models.GetModelInstanceInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.GetModelInstanceInfoResponse:
        """
        @summary GetModelInstanceInfo
        
        @param request: GetModelInstanceInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelInstanceInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.model_instance_id):
            query['ModelInstanceId'] = request.model_instance_id
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetModelInstanceInfo',
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
            rai20240701_models.GetModelInstanceInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_instance_info(
        self,
        request: rai20240701_models.GetModelInstanceInfoRequest,
    ) -> rai20240701_models.GetModelInstanceInfoResponse:
        """
        @summary GetModelInstanceInfo
        
        @param request: GetModelInstanceInfoRequest
        @return: GetModelInstanceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_model_instance_info_with_options(request, runtime)

    async def get_model_instance_info_async(
        self,
        request: rai20240701_models.GetModelInstanceInfoRequest,
    ) -> rai20240701_models.GetModelInstanceInfoResponse:
        """
        @summary GetModelInstanceInfo
        
        @param request: GetModelInstanceInfoRequest
        @return: GetModelInstanceInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_model_instance_info_with_options_async(request, runtime)

    def get_model_output_content_detect_result_with_options(
        self,
        request: rai20240701_models.GetModelOutputContentDetectResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.GetModelOutputContentDetectResultResponse:
        """
        @summary GetModelOutputContentDetectResult
        
        @param request: GetModelOutputContentDetectResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelOutputContentDetectResultResponse
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
            action='GetModelOutputContentDetectResult',
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
            rai20240701_models.GetModelOutputContentDetectResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_model_output_content_detect_result_with_options_async(
        self,
        request: rai20240701_models.GetModelOutputContentDetectResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.GetModelOutputContentDetectResultResponse:
        """
        @summary GetModelOutputContentDetectResult
        
        @param request: GetModelOutputContentDetectResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModelOutputContentDetectResultResponse
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
            action='GetModelOutputContentDetectResult',
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
            rai20240701_models.GetModelOutputContentDetectResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_model_output_content_detect_result(
        self,
        request: rai20240701_models.GetModelOutputContentDetectResultRequest,
    ) -> rai20240701_models.GetModelOutputContentDetectResultResponse:
        """
        @summary GetModelOutputContentDetectResult
        
        @param request: GetModelOutputContentDetectResultRequest
        @return: GetModelOutputContentDetectResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_model_output_content_detect_result_with_options(request, runtime)

    async def get_model_output_content_detect_result_async(
        self,
        request: rai20240701_models.GetModelOutputContentDetectResultRequest,
    ) -> rai20240701_models.GetModelOutputContentDetectResultResponse:
        """
        @summary GetModelOutputContentDetectResult
        
        @param request: GetModelOutputContentDetectResultRequest
        @return: GetModelOutputContentDetectResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_model_output_content_detect_result_with_options_async(request, runtime)

    def get_policy_default_options_with_options(
        self,
        request: rai20240701_models.GetPolicyDefaultOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.GetPolicyDefaultOptionsResponse:
        """
        @summary GetPolicyDefaultOptions
        
        @param request: GetPolicyDefaultOptionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyDefaultOptionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicyDefaultOptions',
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
            rai20240701_models.GetPolicyDefaultOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_default_options_with_options_async(
        self,
        request: rai20240701_models.GetPolicyDefaultOptionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.GetPolicyDefaultOptionsResponse:
        """
        @summary GetPolicyDefaultOptions
        
        @param request: GetPolicyDefaultOptionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyDefaultOptionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicyDefaultOptions',
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
            rai20240701_models.GetPolicyDefaultOptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy_default_options(
        self,
        request: rai20240701_models.GetPolicyDefaultOptionsRequest,
    ) -> rai20240701_models.GetPolicyDefaultOptionsResponse:
        """
        @summary GetPolicyDefaultOptions
        
        @param request: GetPolicyDefaultOptionsRequest
        @return: GetPolicyDefaultOptionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_policy_default_options_with_options(request, runtime)

    async def get_policy_default_options_async(
        self,
        request: rai20240701_models.GetPolicyDefaultOptionsRequest,
    ) -> rai20240701_models.GetPolicyDefaultOptionsResponse:
        """
        @summary GetPolicyDefaultOptions
        
        @param request: GetPolicyDefaultOptionsRequest
        @return: GetPolicyDefaultOptionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_default_options_with_options_async(request, runtime)

    def get_policy_info_with_options(
        self,
        request: rai20240701_models.GetPolicyInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.GetPolicyInfoResponse:
        """
        @summary GetPolicyInfo
        
        @param request: GetPolicyInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicyInfo',
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
            rai20240701_models.GetPolicyInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_policy_info_with_options_async(
        self,
        request: rai20240701_models.GetPolicyInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.GetPolicyInfoResponse:
        """
        @summary GetPolicyInfo
        
        @param request: GetPolicyInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPolicyInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicyInfo',
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
            rai20240701_models.GetPolicyInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_policy_info(
        self,
        request: rai20240701_models.GetPolicyInfoRequest,
    ) -> rai20240701_models.GetPolicyInfoResponse:
        """
        @summary GetPolicyInfo
        
        @param request: GetPolicyInfoRequest
        @return: GetPolicyInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_policy_info_with_options(request, runtime)

    async def get_policy_info_async(
        self,
        request: rai20240701_models.GetPolicyInfoRequest,
    ) -> rai20240701_models.GetPolicyInfoResponse:
        """
        @summary GetPolicyInfo
        
        @param request: GetPolicyInfoRequest
        @return: GetPolicyInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_policy_info_with_options_async(request, runtime)

    def get_topic_with_options(
        self,
        request: rai20240701_models.GetTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.GetTopicResponse:
        """
        @summary GetTopic
        
        @param request: GetTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic_id):
            query['TopicId'] = request.topic_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTopic',
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
            rai20240701_models.GetTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_topic_with_options_async(
        self,
        request: rai20240701_models.GetTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.GetTopicResponse:
        """
        @summary GetTopic
        
        @param request: GetTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic_id):
            query['TopicId'] = request.topic_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTopic',
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
            rai20240701_models.GetTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_topic(
        self,
        request: rai20240701_models.GetTopicRequest,
    ) -> rai20240701_models.GetTopicResponse:
        """
        @summary GetTopic
        
        @param request: GetTopicRequest
        @return: GetTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_topic_with_options(request, runtime)

    async def get_topic_async(
        self,
        request: rai20240701_models.GetTopicRequest,
    ) -> rai20240701_models.GetTopicResponse:
        """
        @summary GetTopic
        
        @param request: GetTopicRequest
        @return: GetTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_topic_with_options_async(request, runtime)

    def get_word_group_with_options(
        self,
        request: rai20240701_models.GetWordGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.GetWordGroupResponse:
        """
        @summary GetWordGroup
        
        @param request: GetWordGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWordGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWordGroup',
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
            rai20240701_models.GetWordGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_word_group_with_options_async(
        self,
        request: rai20240701_models.GetWordGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.GetWordGroupResponse:
        """
        @summary GetWordGroup
        
        @param request: GetWordGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWordGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWordGroup',
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
            rai20240701_models.GetWordGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_word_group(
        self,
        request: rai20240701_models.GetWordGroupRequest,
    ) -> rai20240701_models.GetWordGroupResponse:
        """
        @summary GetWordGroup
        
        @param request: GetWordGroupRequest
        @return: GetWordGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_word_group_with_options(request, runtime)

    async def get_word_group_async(
        self,
        request: rai20240701_models.GetWordGroupRequest,
    ) -> rai20240701_models.GetWordGroupResponse:
        """
        @summary GetWordGroup
        
        @param request: GetWordGroupRequest
        @return: GetWordGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_word_group_with_options_async(request, runtime)

    def list_model_category_with_options(
        self,
        request: rai20240701_models.ListModelCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ListModelCategoryResponse:
        """
        @summary ListModelCategory
        
        @param request: ListModelCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content_safe_image_supported):
            query['ContentSafeImageSupported'] = request.content_safe_image_supported
        if not UtilClient.is_unset(request.content_safe_text_supported):
            query['ContentSafeTextSupported'] = request.content_safe_text_supported
        if not UtilClient.is_unset(request.model_category_name):
            query['ModelCategoryName'] = request.model_category_name
        if not UtilClient.is_unset(request.model_source):
            query['ModelSource'] = request.model_source
        if not UtilClient.is_unset(request.prompt_attack_text_supported):
            query['PromptAttackTextSupported'] = request.prompt_attack_text_supported
        if not UtilClient.is_unset(request.sensitive_topic_text_supported):
            query['SensitiveTopicTextSupported'] = request.sensitive_topic_text_supported
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelCategory',
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
            rai20240701_models.ListModelCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_category_with_options_async(
        self,
        request: rai20240701_models.ListModelCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ListModelCategoryResponse:
        """
        @summary ListModelCategory
        
        @param request: ListModelCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.content_safe_image_supported):
            query['ContentSafeImageSupported'] = request.content_safe_image_supported
        if not UtilClient.is_unset(request.content_safe_text_supported):
            query['ContentSafeTextSupported'] = request.content_safe_text_supported
        if not UtilClient.is_unset(request.model_category_name):
            query['ModelCategoryName'] = request.model_category_name
        if not UtilClient.is_unset(request.model_source):
            query['ModelSource'] = request.model_source
        if not UtilClient.is_unset(request.prompt_attack_text_supported):
            query['PromptAttackTextSupported'] = request.prompt_attack_text_supported
        if not UtilClient.is_unset(request.sensitive_topic_text_supported):
            query['SensitiveTopicTextSupported'] = request.sensitive_topic_text_supported
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelCategory',
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
            rai20240701_models.ListModelCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_category(
        self,
        request: rai20240701_models.ListModelCategoryRequest,
    ) -> rai20240701_models.ListModelCategoryResponse:
        """
        @summary ListModelCategory
        
        @param request: ListModelCategoryRequest
        @return: ListModelCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_model_category_with_options(request, runtime)

    async def list_model_category_async(
        self,
        request: rai20240701_models.ListModelCategoryRequest,
    ) -> rai20240701_models.ListModelCategoryResponse:
        """
        @summary ListModelCategory
        
        @param request: ListModelCategoryRequest
        @return: ListModelCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_model_category_with_options_async(request, runtime)

    def list_model_instance_with_options(
        self,
        request: rai20240701_models.ListModelInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ListModelInstanceResponse:
        """
        @summary ListModelInstance
        
        @param request: ListModelInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.eas_service_name):
            query['EasServiceName'] = request.eas_service_name
        if not UtilClient.is_unset(request.is_sidecar_policy):
            query['IsSidecarPolicy'] = request.is_sidecar_policy
        if not UtilClient.is_unset(request.is_support_content_safe):
            query['IsSupportContentSafe'] = request.is_support_content_safe
        if not UtilClient.is_unset(request.is_support_prompt_attack):
            query['IsSupportPromptAttack'] = request.is_support_prompt_attack
        if not UtilClient.is_unset(request.is_support_sensitive_topic):
            query['IsSupportSensitiveTopic'] = request.is_support_sensitive_topic
        if not UtilClient.is_unset(request.model_source):
            query['ModelSource'] = request.model_source
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelInstance',
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
            rai20240701_models.ListModelInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_instance_with_options_async(
        self,
        request: rai20240701_models.ListModelInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ListModelInstanceResponse:
        """
        @summary ListModelInstance
        
        @param request: ListModelInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModelInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.eas_service_name):
            query['EasServiceName'] = request.eas_service_name
        if not UtilClient.is_unset(request.is_sidecar_policy):
            query['IsSidecarPolicy'] = request.is_sidecar_policy
        if not UtilClient.is_unset(request.is_support_content_safe):
            query['IsSupportContentSafe'] = request.is_support_content_safe
        if not UtilClient.is_unset(request.is_support_prompt_attack):
            query['IsSupportPromptAttack'] = request.is_support_prompt_attack
        if not UtilClient.is_unset(request.is_support_sensitive_topic):
            query['IsSupportSensitiveTopic'] = request.is_support_sensitive_topic
        if not UtilClient.is_unset(request.model_source):
            query['ModelSource'] = request.model_source
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModelInstance',
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
            rai20240701_models.ListModelInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_instance(
        self,
        request: rai20240701_models.ListModelInstanceRequest,
    ) -> rai20240701_models.ListModelInstanceResponse:
        """
        @summary ListModelInstance
        
        @param request: ListModelInstanceRequest
        @return: ListModelInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_model_instance_with_options(request, runtime)

    async def list_model_instance_async(
        self,
        request: rai20240701_models.ListModelInstanceRequest,
    ) -> rai20240701_models.ListModelInstanceResponse:
        """
        @summary ListModelInstance
        
        @param request: ListModelInstanceRequest
        @return: ListModelInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_model_instance_with_options_async(request, runtime)

    def list_policy_with_options(
        self,
        request: rai20240701_models.ListPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ListPolicyResponse:
        """
        @summary ListPolicy
        
        @param request: ListPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_sidecar_policy):
            query['IsSidecarPolicy'] = request.is_sidecar_policy
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_identifier):
            query['PolicyIdentifier'] = request.policy_identifier
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicy',
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
            rai20240701_models.ListPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policy_with_options_async(
        self,
        request: rai20240701_models.ListPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ListPolicyResponse:
        """
        @summary ListPolicy
        
        @param request: ListPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_sidecar_policy):
            query['IsSidecarPolicy'] = request.is_sidecar_policy
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_identifier):
            query['PolicyIdentifier'] = request.policy_identifier
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicy',
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
            rai20240701_models.ListPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policy(
        self,
        request: rai20240701_models.ListPolicyRequest,
    ) -> rai20240701_models.ListPolicyResponse:
        """
        @summary ListPolicy
        
        @param request: ListPolicyRequest
        @return: ListPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_policy_with_options(request, runtime)

    async def list_policy_async(
        self,
        request: rai20240701_models.ListPolicyRequest,
    ) -> rai20240701_models.ListPolicyResponse:
        """
        @summary ListPolicy
        
        @param request: ListPolicyRequest
        @return: ListPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_policy_with_options_async(request, runtime)

    def list_topic_with_options(
        self,
        request: rai20240701_models.ListTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ListTopicResponse:
        """
        @summary ListTopic
        
        @param request: ListTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTopic',
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
            rai20240701_models.ListTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_topic_with_options_async(
        self,
        request: rai20240701_models.ListTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ListTopicResponse:
        """
        @summary ListTopic
        
        @param request: ListTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTopicResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTopic',
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
            rai20240701_models.ListTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_topic(
        self,
        request: rai20240701_models.ListTopicRequest,
    ) -> rai20240701_models.ListTopicResponse:
        """
        @summary ListTopic
        
        @param request: ListTopicRequest
        @return: ListTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_topic_with_options(request, runtime)

    async def list_topic_async(
        self,
        request: rai20240701_models.ListTopicRequest,
    ) -> rai20240701_models.ListTopicResponse:
        """
        @summary ListTopic
        
        @param request: ListTopicRequest
        @return: ListTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_topic_with_options_async(request, runtime)

    def list_word_group_with_options(
        self,
        request: rai20240701_models.ListWordGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ListWordGroupResponse:
        """
        @summary ListWordGroup
        
        @param request: ListWordGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWordGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWordGroup',
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
            rai20240701_models.ListWordGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_word_group_with_options_async(
        self,
        request: rai20240701_models.ListWordGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ListWordGroupResponse:
        """
        @summary ListWordGroup
        
        @param request: ListWordGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWordGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWordGroup',
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
            rai20240701_models.ListWordGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_word_group(
        self,
        request: rai20240701_models.ListWordGroupRequest,
    ) -> rai20240701_models.ListWordGroupResponse:
        """
        @summary ListWordGroup
        
        @param request: ListWordGroupRequest
        @return: ListWordGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_word_group_with_options(request, runtime)

    async def list_word_group_async(
        self,
        request: rai20240701_models.ListWordGroupRequest,
    ) -> rai20240701_models.ListWordGroupResponse:
        """
        @summary ListWordGroup
        
        @param request: ListWordGroupRequest
        @return: ListWordGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_word_group_with_options_async(request, runtime)

    def model_input_content_async_detect_with_options(
        self,
        tmp_req: rai20240701_models.ModelInputContentAsyncDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ModelInputContentAsyncDetectResponse:
        """
        @summary ModelInputContentAsyncDetect
        
        @param tmp_req: ModelInputContentAsyncDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModelInputContentAsyncDetectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.ModelInputContentAsyncDetectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.policy_identifier):
            query['PolicyIdentifier'] = request.policy_identifier
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModelInputContentAsyncDetect',
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
            rai20240701_models.ModelInputContentAsyncDetectResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_input_content_async_detect_with_options_async(
        self,
        tmp_req: rai20240701_models.ModelInputContentAsyncDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ModelInputContentAsyncDetectResponse:
        """
        @summary ModelInputContentAsyncDetect
        
        @param tmp_req: ModelInputContentAsyncDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModelInputContentAsyncDetectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.ModelInputContentAsyncDetectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.policy_identifier):
            query['PolicyIdentifier'] = request.policy_identifier
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModelInputContentAsyncDetect',
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
            rai20240701_models.ModelInputContentAsyncDetectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_input_content_async_detect(
        self,
        request: rai20240701_models.ModelInputContentAsyncDetectRequest,
    ) -> rai20240701_models.ModelInputContentAsyncDetectResponse:
        """
        @summary ModelInputContentAsyncDetect
        
        @param request: ModelInputContentAsyncDetectRequest
        @return: ModelInputContentAsyncDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.model_input_content_async_detect_with_options(request, runtime)

    async def model_input_content_async_detect_async(
        self,
        request: rai20240701_models.ModelInputContentAsyncDetectRequest,
    ) -> rai20240701_models.ModelInputContentAsyncDetectResponse:
        """
        @summary ModelInputContentAsyncDetect
        
        @param request: ModelInputContentAsyncDetectRequest
        @return: ModelInputContentAsyncDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.model_input_content_async_detect_with_options_async(request, runtime)

    def model_input_content_sync_detect_with_options(
        self,
        tmp_req: rai20240701_models.ModelInputContentSyncDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ModelInputContentSyncDetectResponse:
        """
        @summary ModelInputContentSyncDetect
        
        @param tmp_req: ModelInputContentSyncDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModelInputContentSyncDetectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.ModelInputContentSyncDetectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.policy_identifier):
            query['PolicyIdentifier'] = request.policy_identifier
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModelInputContentSyncDetect',
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
            rai20240701_models.ModelInputContentSyncDetectResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_input_content_sync_detect_with_options_async(
        self,
        tmp_req: rai20240701_models.ModelInputContentSyncDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ModelInputContentSyncDetectResponse:
        """
        @summary ModelInputContentSyncDetect
        
        @param tmp_req: ModelInputContentSyncDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModelInputContentSyncDetectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.ModelInputContentSyncDetectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.policy_identifier):
            query['PolicyIdentifier'] = request.policy_identifier
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModelInputContentSyncDetect',
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
            rai20240701_models.ModelInputContentSyncDetectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_input_content_sync_detect(
        self,
        request: rai20240701_models.ModelInputContentSyncDetectRequest,
    ) -> rai20240701_models.ModelInputContentSyncDetectResponse:
        """
        @summary ModelInputContentSyncDetect
        
        @param request: ModelInputContentSyncDetectRequest
        @return: ModelInputContentSyncDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.model_input_content_sync_detect_with_options(request, runtime)

    async def model_input_content_sync_detect_async(
        self,
        request: rai20240701_models.ModelInputContentSyncDetectRequest,
    ) -> rai20240701_models.ModelInputContentSyncDetectResponse:
        """
        @summary ModelInputContentSyncDetect
        
        @param request: ModelInputContentSyncDetectRequest
        @return: ModelInputContentSyncDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.model_input_content_sync_detect_with_options_async(request, runtime)

    def model_output_content_async_detect_with_options(
        self,
        tmp_req: rai20240701_models.ModelOutputContentAsyncDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ModelOutputContentAsyncDetectResponse:
        """
        @summary ModelOutputContentAsyncDetect
        
        @param tmp_req: ModelOutputContentAsyncDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModelOutputContentAsyncDetectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.ModelOutputContentAsyncDetectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.policy_identifier):
            query['PolicyIdentifier'] = request.policy_identifier
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModelOutputContentAsyncDetect',
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
            rai20240701_models.ModelOutputContentAsyncDetectResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_output_content_async_detect_with_options_async(
        self,
        tmp_req: rai20240701_models.ModelOutputContentAsyncDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ModelOutputContentAsyncDetectResponse:
        """
        @summary ModelOutputContentAsyncDetect
        
        @param tmp_req: ModelOutputContentAsyncDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModelOutputContentAsyncDetectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.ModelOutputContentAsyncDetectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.policy_identifier):
            query['PolicyIdentifier'] = request.policy_identifier
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModelOutputContentAsyncDetect',
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
            rai20240701_models.ModelOutputContentAsyncDetectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_output_content_async_detect(
        self,
        request: rai20240701_models.ModelOutputContentAsyncDetectRequest,
    ) -> rai20240701_models.ModelOutputContentAsyncDetectResponse:
        """
        @summary ModelOutputContentAsyncDetect
        
        @param request: ModelOutputContentAsyncDetectRequest
        @return: ModelOutputContentAsyncDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.model_output_content_async_detect_with_options(request, runtime)

    async def model_output_content_async_detect_async(
        self,
        request: rai20240701_models.ModelOutputContentAsyncDetectRequest,
    ) -> rai20240701_models.ModelOutputContentAsyncDetectResponse:
        """
        @summary ModelOutputContentAsyncDetect
        
        @param request: ModelOutputContentAsyncDetectRequest
        @return: ModelOutputContentAsyncDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.model_output_content_async_detect_with_options_async(request, runtime)

    def model_output_content_sync_detect_with_options(
        self,
        tmp_req: rai20240701_models.ModelOutputContentSyncDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ModelOutputContentSyncDetectResponse:
        """
        @summary ModelOutputContentSyncDetect
        
        @param tmp_req: ModelOutputContentSyncDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModelOutputContentSyncDetectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.ModelOutputContentSyncDetectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.policy_identifier):
            query['PolicyIdentifier'] = request.policy_identifier
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModelOutputContentSyncDetect',
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
            rai20240701_models.ModelOutputContentSyncDetectResponse(),
            self.call_api(params, req, runtime)
        )

    async def model_output_content_sync_detect_with_options_async(
        self,
        tmp_req: rai20240701_models.ModelOutputContentSyncDetectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.ModelOutputContentSyncDetectResponse:
        """
        @summary ModelOutputContentSyncDetect
        
        @param tmp_req: ModelOutputContentSyncDetectRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModelOutputContentSyncDetectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.ModelOutputContentSyncDetectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.policy_identifier):
            query['PolicyIdentifier'] = request.policy_identifier
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene_name):
            query['SceneName'] = request.scene_name
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModelOutputContentSyncDetect',
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
            rai20240701_models.ModelOutputContentSyncDetectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def model_output_content_sync_detect(
        self,
        request: rai20240701_models.ModelOutputContentSyncDetectRequest,
    ) -> rai20240701_models.ModelOutputContentSyncDetectResponse:
        """
        @summary ModelOutputContentSyncDetect
        
        @param request: ModelOutputContentSyncDetectRequest
        @return: ModelOutputContentSyncDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.model_output_content_sync_detect_with_options(request, runtime)

    async def model_output_content_sync_detect_async(
        self,
        request: rai20240701_models.ModelOutputContentSyncDetectRequest,
    ) -> rai20240701_models.ModelOutputContentSyncDetectResponse:
        """
        @summary ModelOutputContentSyncDetect
        
        @param request: ModelOutputContentSyncDetectRequest
        @return: ModelOutputContentSyncDetectResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.model_output_content_sync_detect_with_options_async(request, runtime)

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

    def update_model_instance_with_options(
        self,
        request: rai20240701_models.UpdateModelInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.UpdateModelInstanceResponse:
        """
        @summary UpdateModelInstance
        
        @param request: UpdateModelInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModelInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.eas_service_id):
            query['EasServiceId'] = request.eas_service_id
        if not UtilClient.is_unset(request.eas_service_name):
            query['EasServiceName'] = request.eas_service_name
        if not UtilClient.is_unset(request.model_call_name):
            query['ModelCallName'] = request.model_call_name
        if not UtilClient.is_unset(request.model_category_id):
            query['ModelCategoryId'] = request.model_category_id
        if not UtilClient.is_unset(request.model_instance_id):
            query['ModelInstanceId'] = request.model_instance_id
        if not UtilClient.is_unset(request.model_token):
            query['ModelToken'] = request.model_token
        if not UtilClient.is_unset(request.model_url):
            query['ModelUrl'] = request.model_url
        if not UtilClient.is_unset(request.model_vpc_url):
            query['ModelVpcUrl'] = request.model_vpc_url
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateModelInstance',
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
            rai20240701_models.UpdateModelInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_model_instance_with_options_async(
        self,
        request: rai20240701_models.UpdateModelInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.UpdateModelInstanceResponse:
        """
        @summary UpdateModelInstance
        
        @param request: UpdateModelInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModelInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.eas_service_id):
            query['EasServiceId'] = request.eas_service_id
        if not UtilClient.is_unset(request.eas_service_name):
            query['EasServiceName'] = request.eas_service_name
        if not UtilClient.is_unset(request.model_call_name):
            query['ModelCallName'] = request.model_call_name
        if not UtilClient.is_unset(request.model_category_id):
            query['ModelCategoryId'] = request.model_category_id
        if not UtilClient.is_unset(request.model_instance_id):
            query['ModelInstanceId'] = request.model_instance_id
        if not UtilClient.is_unset(request.model_token):
            query['ModelToken'] = request.model_token
        if not UtilClient.is_unset(request.model_url):
            query['ModelUrl'] = request.model_url
        if not UtilClient.is_unset(request.model_vpc_url):
            query['ModelVpcUrl'] = request.model_vpc_url
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateModelInstance',
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
            rai20240701_models.UpdateModelInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_model_instance(
        self,
        request: rai20240701_models.UpdateModelInstanceRequest,
    ) -> rai20240701_models.UpdateModelInstanceResponse:
        """
        @summary UpdateModelInstance
        
        @param request: UpdateModelInstanceRequest
        @return: UpdateModelInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_model_instance_with_options(request, runtime)

    async def update_model_instance_async(
        self,
        request: rai20240701_models.UpdateModelInstanceRequest,
    ) -> rai20240701_models.UpdateModelInstanceResponse:
        """
        @summary UpdateModelInstance
        
        @param request: UpdateModelInstanceRequest
        @return: UpdateModelInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_model_instance_with_options_async(request, runtime)

    def update_policy_with_options(
        self,
        tmp_req: rai20240701_models.UpdatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.UpdatePolicyResponse:
        """
        @summary UpdatePolicy
        
        @param tmp_req: UpdatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.UpdatePolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.harmful_category_config_info_list):
            request.harmful_category_config_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.harmful_category_config_info_list, 'HarmfulCategoryConfigInfoList', 'json')
        if not UtilClient.is_unset(tmp_req.prompt_attack_info):
            request.prompt_attack_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prompt_attack_info, 'PromptAttackInfo', 'json')
        if not UtilClient.is_unset(tmp_req.prompt_attack_info_list):
            request.prompt_attack_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prompt_attack_info_list, 'PromptAttackInfoList', 'json')
        if not UtilClient.is_unset(tmp_req.regular_express_list):
            request.regular_express_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.regular_express_list, 'RegularExpressList', 'json')
        if not UtilClient.is_unset(tmp_req.sensitive_config_list):
            request.sensitive_config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sensitive_config_list, 'SensitiveConfigList', 'json')
        if not UtilClient.is_unset(tmp_req.sensitive_topic_list):
            request.sensitive_topic_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sensitive_topic_list, 'SensitiveTopicList', 'json')
        if not UtilClient.is_unset(tmp_req.sensitive_word_list):
            request.sensitive_word_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sensitive_word_list, 'SensitiveWordList', 'json')
        if not UtilClient.is_unset(tmp_req.topic_config_info_list):
            request.topic_config_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topic_config_info_list, 'TopicConfigInfoList', 'json')
        if not UtilClient.is_unset(tmp_req.word_group_info_list):
            request.word_group_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.word_group_info_list, 'WordGroupInfoList', 'json')
        query = {}
        if not UtilClient.is_unset(request.content_safe_model_instance_id):
            query['ContentSafeModelInstanceId'] = request.content_safe_model_instance_id
        if not UtilClient.is_unset(request.enable_sensitive_input_check):
            query['EnableSensitiveInputCheck'] = request.enable_sensitive_input_check
        if not UtilClient.is_unset(request.enable_sensitive_output_check):
            query['EnableSensitiveOutputCheck'] = request.enable_sensitive_output_check
        if not UtilClient.is_unset(request.harmful_category_config_info_list_shrink):
            query['HarmfulCategoryConfigInfoList'] = request.harmful_category_config_info_list_shrink
        if not UtilClient.is_unset(request.input_safe_answer):
            query['InputSafeAnswer'] = request.input_safe_answer
        if not UtilClient.is_unset(request.input_safe_answer_switch):
            query['InputSafeAnswerSwitch'] = request.input_safe_answer_switch
        if not UtilClient.is_unset(request.is_sidecar_policy):
            query['IsSidecarPolicy'] = request.is_sidecar_policy
        if not UtilClient.is_unset(request.output_safe_answer):
            query['OutputSafeAnswer'] = request.output_safe_answer
        if not UtilClient.is_unset(request.output_safe_answer_switch):
            query['OutputSafeAnswerSwitch'] = request.output_safe_answer_switch
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.prompt_attack_info_shrink):
            query['PromptAttackInfo'] = request.prompt_attack_info_shrink
        if not UtilClient.is_unset(request.prompt_attack_info_list_shrink):
            query['PromptAttackInfoList'] = request.prompt_attack_info_list_shrink
        if not UtilClient.is_unset(request.prompt_attack_model_instance_id):
            query['PromptAttackModelInstanceId'] = request.prompt_attack_model_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.regular_express_list_shrink):
            query['RegularExpressList'] = request.regular_express_list_shrink
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.sensitive_config_list_shrink):
            query['SensitiveConfigList'] = request.sensitive_config_list_shrink
        if not UtilClient.is_unset(request.sensitive_topic_list_shrink):
            query['SensitiveTopicList'] = request.sensitive_topic_list_shrink
        if not UtilClient.is_unset(request.sensitive_topic_model_instance_id):
            query['SensitiveTopicModelInstanceId'] = request.sensitive_topic_model_instance_id
        if not UtilClient.is_unset(request.sensitive_word_list_shrink):
            query['SensitiveWordList'] = request.sensitive_word_list_shrink
        if not UtilClient.is_unset(request.topic_config_info_list_shrink):
            query['TopicConfigInfoList'] = request.topic_config_info_list_shrink
        if not UtilClient.is_unset(request.word_group_info_list_shrink):
            query['WordGroupInfoList'] = request.word_group_info_list_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePolicy',
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
            rai20240701_models.UpdatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_policy_with_options_async(
        self,
        tmp_req: rai20240701_models.UpdatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.UpdatePolicyResponse:
        """
        @summary UpdatePolicy
        
        @param tmp_req: UpdatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdatePolicyResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.UpdatePolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.harmful_category_config_info_list):
            request.harmful_category_config_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.harmful_category_config_info_list, 'HarmfulCategoryConfigInfoList', 'json')
        if not UtilClient.is_unset(tmp_req.prompt_attack_info):
            request.prompt_attack_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prompt_attack_info, 'PromptAttackInfo', 'json')
        if not UtilClient.is_unset(tmp_req.prompt_attack_info_list):
            request.prompt_attack_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.prompt_attack_info_list, 'PromptAttackInfoList', 'json')
        if not UtilClient.is_unset(tmp_req.regular_express_list):
            request.regular_express_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.regular_express_list, 'RegularExpressList', 'json')
        if not UtilClient.is_unset(tmp_req.sensitive_config_list):
            request.sensitive_config_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sensitive_config_list, 'SensitiveConfigList', 'json')
        if not UtilClient.is_unset(tmp_req.sensitive_topic_list):
            request.sensitive_topic_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sensitive_topic_list, 'SensitiveTopicList', 'json')
        if not UtilClient.is_unset(tmp_req.sensitive_word_list):
            request.sensitive_word_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sensitive_word_list, 'SensitiveWordList', 'json')
        if not UtilClient.is_unset(tmp_req.topic_config_info_list):
            request.topic_config_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topic_config_info_list, 'TopicConfigInfoList', 'json')
        if not UtilClient.is_unset(tmp_req.word_group_info_list):
            request.word_group_info_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.word_group_info_list, 'WordGroupInfoList', 'json')
        query = {}
        if not UtilClient.is_unset(request.content_safe_model_instance_id):
            query['ContentSafeModelInstanceId'] = request.content_safe_model_instance_id
        if not UtilClient.is_unset(request.enable_sensitive_input_check):
            query['EnableSensitiveInputCheck'] = request.enable_sensitive_input_check
        if not UtilClient.is_unset(request.enable_sensitive_output_check):
            query['EnableSensitiveOutputCheck'] = request.enable_sensitive_output_check
        if not UtilClient.is_unset(request.harmful_category_config_info_list_shrink):
            query['HarmfulCategoryConfigInfoList'] = request.harmful_category_config_info_list_shrink
        if not UtilClient.is_unset(request.input_safe_answer):
            query['InputSafeAnswer'] = request.input_safe_answer
        if not UtilClient.is_unset(request.input_safe_answer_switch):
            query['InputSafeAnswerSwitch'] = request.input_safe_answer_switch
        if not UtilClient.is_unset(request.is_sidecar_policy):
            query['IsSidecarPolicy'] = request.is_sidecar_policy
        if not UtilClient.is_unset(request.output_safe_answer):
            query['OutputSafeAnswer'] = request.output_safe_answer
        if not UtilClient.is_unset(request.output_safe_answer_switch):
            query['OutputSafeAnswerSwitch'] = request.output_safe_answer_switch
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.prompt_attack_info_shrink):
            query['PromptAttackInfo'] = request.prompt_attack_info_shrink
        if not UtilClient.is_unset(request.prompt_attack_info_list_shrink):
            query['PromptAttackInfoList'] = request.prompt_attack_info_list_shrink
        if not UtilClient.is_unset(request.prompt_attack_model_instance_id):
            query['PromptAttackModelInstanceId'] = request.prompt_attack_model_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.regular_express_list_shrink):
            query['RegularExpressList'] = request.regular_express_list_shrink
        if not UtilClient.is_unset(request.scene_type):
            query['SceneType'] = request.scene_type
        if not UtilClient.is_unset(request.sensitive_config_list_shrink):
            query['SensitiveConfigList'] = request.sensitive_config_list_shrink
        if not UtilClient.is_unset(request.sensitive_topic_list_shrink):
            query['SensitiveTopicList'] = request.sensitive_topic_list_shrink
        if not UtilClient.is_unset(request.sensitive_topic_model_instance_id):
            query['SensitiveTopicModelInstanceId'] = request.sensitive_topic_model_instance_id
        if not UtilClient.is_unset(request.sensitive_word_list_shrink):
            query['SensitiveWordList'] = request.sensitive_word_list_shrink
        if not UtilClient.is_unset(request.topic_config_info_list_shrink):
            query['TopicConfigInfoList'] = request.topic_config_info_list_shrink
        if not UtilClient.is_unset(request.word_group_info_list_shrink):
            query['WordGroupInfoList'] = request.word_group_info_list_shrink
        if not UtilClient.is_unset(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePolicy',
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
            rai20240701_models.UpdatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_policy(
        self,
        request: rai20240701_models.UpdatePolicyRequest,
    ) -> rai20240701_models.UpdatePolicyResponse:
        """
        @summary UpdatePolicy
        
        @param request: UpdatePolicyRequest
        @return: UpdatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_policy_with_options(request, runtime)

    async def update_policy_async(
        self,
        request: rai20240701_models.UpdatePolicyRequest,
    ) -> rai20240701_models.UpdatePolicyResponse:
        """
        @summary UpdatePolicy
        
        @param request: UpdatePolicyRequest
        @return: UpdatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_policy_with_options_async(request, runtime)

    def update_topic_with_options(
        self,
        tmp_req: rai20240701_models.UpdateTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.UpdateTopicResponse:
        """
        @summary UpdateTopic
        
        @param tmp_req: UpdateTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTopicResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.UpdateTopicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic_definition):
            query['TopicDefinition'] = request.topic_definition
        if not UtilClient.is_unset(request.topic_id):
            query['TopicId'] = request.topic_id
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTopic',
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
            rai20240701_models.UpdateTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_topic_with_options_async(
        self,
        tmp_req: rai20240701_models.UpdateTopicRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.UpdateTopicResponse:
        """
        @summary UpdateTopic
        
        @param tmp_req: UpdateTopicRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTopicResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.UpdateTopicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic_definition):
            query['TopicDefinition'] = request.topic_definition
        if not UtilClient.is_unset(request.topic_id):
            query['TopicId'] = request.topic_id
        if not UtilClient.is_unset(request.topic_name):
            query['TopicName'] = request.topic_name
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTopic',
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
            rai20240701_models.UpdateTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_topic(
        self,
        request: rai20240701_models.UpdateTopicRequest,
    ) -> rai20240701_models.UpdateTopicResponse:
        """
        @summary UpdateTopic
        
        @param request: UpdateTopicRequest
        @return: UpdateTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_topic_with_options(request, runtime)

    async def update_topic_async(
        self,
        request: rai20240701_models.UpdateTopicRequest,
    ) -> rai20240701_models.UpdateTopicResponse:
        """
        @summary UpdateTopic
        
        @param request: UpdateTopicRequest
        @return: UpdateTopicResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_topic_with_options_async(request, runtime)

    def update_word_group_with_options(
        self,
        tmp_req: rai20240701_models.UpdateWordGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.UpdateWordGroupResponse:
        """
        @summary UpdateWordGroup
        
        @param tmp_req: UpdateWordGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWordGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.UpdateWordGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.commit):
            query['Commit'] = request.commit
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.word_info_list_modified):
            query['WordInfoListModified'] = request.word_info_list_modified
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWordGroup',
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
            rai20240701_models.UpdateWordGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_word_group_with_options_async(
        self,
        tmp_req: rai20240701_models.UpdateWordGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> rai20240701_models.UpdateWordGroupResponse:
        """
        @summary UpdateWordGroup
        
        @param tmp_req: UpdateWordGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWordGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = rai20240701_models.UpdateWordGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.body_data):
            request.body_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.body_data, 'BodyData', 'json')
        query = {}
        if not UtilClient.is_unset(request.commit):
            query['Commit'] = request.commit
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.word_info_list_modified):
            query['WordInfoListModified'] = request.word_info_list_modified
        body = {}
        if not UtilClient.is_unset(request.body_data_shrink):
            body['BodyData'] = request.body_data_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWordGroup',
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
            rai20240701_models.UpdateWordGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_word_group(
        self,
        request: rai20240701_models.UpdateWordGroupRequest,
    ) -> rai20240701_models.UpdateWordGroupResponse:
        """
        @summary UpdateWordGroup
        
        @param request: UpdateWordGroupRequest
        @return: UpdateWordGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_word_group_with_options(request, runtime)

    async def update_word_group_async(
        self,
        request: rai20240701_models.UpdateWordGroupRequest,
    ) -> rai20240701_models.UpdateWordGroupResponse:
        """
        @summary UpdateWordGroup
        
        @param request: UpdateWordGroupRequest
        @return: UpdateWordGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_word_group_with_options_async(request, runtime)
