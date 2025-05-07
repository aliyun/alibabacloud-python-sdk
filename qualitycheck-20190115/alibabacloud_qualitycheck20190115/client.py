# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_qualitycheck20190115 import models as qualitycheck_20190115_models
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
        self._endpoint = self.get_endpoint('qualitycheck', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_business_category_with_options(
        self,
        request: qualitycheck_20190115_models.AddBusinessCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AddBusinessCategoryResponse:
        """
        @param request: AddBusinessCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddBusinessCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBusinessCategory',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.AddBusinessCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_business_category_with_options_async(
        self,
        request: qualitycheck_20190115_models.AddBusinessCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AddBusinessCategoryResponse:
        """
        @param request: AddBusinessCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddBusinessCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBusinessCategory',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.AddBusinessCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_business_category(
        self,
        request: qualitycheck_20190115_models.AddBusinessCategoryRequest,
    ) -> qualitycheck_20190115_models.AddBusinessCategoryResponse:
        """
        @param request: AddBusinessCategoryRequest
        @return: AddBusinessCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_business_category_with_options(request, runtime)

    async def add_business_category_async(
        self,
        request: qualitycheck_20190115_models.AddBusinessCategoryRequest,
    ) -> qualitycheck_20190115_models.AddBusinessCategoryResponse:
        """
        @param request: AddBusinessCategoryRequest
        @return: AddBusinessCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_business_category_with_options_async(request, runtime)

    def add_rule_category_with_options(
        self,
        request: qualitycheck_20190115_models.AddRuleCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AddRuleCategoryResponse:
        """
        @param request: AddRuleCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddRuleCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRuleCategory',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.AddRuleCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_rule_category_with_options_async(
        self,
        request: qualitycheck_20190115_models.AddRuleCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AddRuleCategoryResponse:
        """
        @param request: AddRuleCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddRuleCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRuleCategory',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.AddRuleCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_rule_category(
        self,
        request: qualitycheck_20190115_models.AddRuleCategoryRequest,
    ) -> qualitycheck_20190115_models.AddRuleCategoryResponse:
        """
        @param request: AddRuleCategoryRequest
        @return: AddRuleCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_rule_category_with_options(request, runtime)

    async def add_rule_category_async(
        self,
        request: qualitycheck_20190115_models.AddRuleCategoryRequest,
    ) -> qualitycheck_20190115_models.AddRuleCategoryResponse:
        """
        @param request: AddRuleCategoryRequest
        @return: AddRuleCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_rule_category_with_options_async(request, runtime)

    def add_rule_v4with_options(
        self,
        request: qualitycheck_20190115_models.AddRuleV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AddRuleV4Response:
        """
        @summary V4创建规则
        
        @param request: AddRuleV4Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddRuleV4Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not UtilClient.is_unset(request.is_copy):
            body['IsCopy'] = request.is_copy
        if not UtilClient.is_unset(request.json_str_for_rule):
            body['JsonStrForRule'] = request.json_str_for_rule
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddRuleV4',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.AddRuleV4Response(),
            self.call_api(params, req, runtime)
        )

    async def add_rule_v4with_options_async(
        self,
        request: qualitycheck_20190115_models.AddRuleV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AddRuleV4Response:
        """
        @summary V4创建规则
        
        @param request: AddRuleV4Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddRuleV4Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not UtilClient.is_unset(request.is_copy):
            body['IsCopy'] = request.is_copy
        if not UtilClient.is_unset(request.json_str_for_rule):
            body['JsonStrForRule'] = request.json_str_for_rule
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddRuleV4',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.AddRuleV4Response(),
            await self.call_api_async(params, req, runtime)
        )

    def add_rule_v4(
        self,
        request: qualitycheck_20190115_models.AddRuleV4Request,
    ) -> qualitycheck_20190115_models.AddRuleV4Response:
        """
        @summary V4创建规则
        
        @param request: AddRuleV4Request
        @return: AddRuleV4Response
        """
        runtime = util_models.RuntimeOptions()
        return self.add_rule_v4with_options(request, runtime)

    async def add_rule_v4_async(
        self,
        request: qualitycheck_20190115_models.AddRuleV4Request,
    ) -> qualitycheck_20190115_models.AddRuleV4Response:
        """
        @summary V4创建规则
        
        @param request: AddRuleV4Request
        @return: AddRuleV4Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_rule_v4with_options_async(request, runtime)

    def apply_ws_token_with_options(
        self,
        request: qualitycheck_20190115_models.ApplyWsTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ApplyWsTokenResponse:
        """
        @summary 申领实时语音所需token
        
        @param request: ApplyWsTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyWsTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyWsToken',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ApplyWsTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_ws_token_with_options_async(
        self,
        request: qualitycheck_20190115_models.ApplyWsTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ApplyWsTokenResponse:
        """
        @summary 申领实时语音所需token
        
        @param request: ApplyWsTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApplyWsTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyWsToken',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ApplyWsTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_ws_token(
        self,
        request: qualitycheck_20190115_models.ApplyWsTokenRequest,
    ) -> qualitycheck_20190115_models.ApplyWsTokenResponse:
        """
        @summary 申领实时语音所需token
        
        @param request: ApplyWsTokenRequest
        @return: ApplyWsTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.apply_ws_token_with_options(request, runtime)

    async def apply_ws_token_async(
        self,
        request: qualitycheck_20190115_models.ApplyWsTokenRequest,
    ) -> qualitycheck_20190115_models.ApplyWsTokenResponse:
        """
        @summary 申领实时语音所需token
        
        @param request: ApplyWsTokenRequest
        @return: ApplyWsTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.apply_ws_token_with_options_async(request, runtime)

    def assign_reviewer_with_options(
        self,
        request: qualitycheck_20190115_models.AssignReviewerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AssignReviewerResponse:
        """
        @param request: AssignReviewerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignReviewerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssignReviewer',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.AssignReviewerResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_reviewer_with_options_async(
        self,
        request: qualitycheck_20190115_models.AssignReviewerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AssignReviewerResponse:
        """
        @param request: AssignReviewerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignReviewerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssignReviewer',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.AssignReviewerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_reviewer(
        self,
        request: qualitycheck_20190115_models.AssignReviewerRequest,
    ) -> qualitycheck_20190115_models.AssignReviewerResponse:
        """
        @param request: AssignReviewerRequest
        @return: AssignReviewerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.assign_reviewer_with_options(request, runtime)

    async def assign_reviewer_async(
        self,
        request: qualitycheck_20190115_models.AssignReviewerRequest,
    ) -> qualitycheck_20190115_models.AssignReviewerResponse:
        """
        @param request: AssignReviewerRequest
        @return: AssignReviewerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.assign_reviewer_with_options_async(request, runtime)

    def assign_reviewer_by_session_group_with_options(
        self,
        request: qualitycheck_20190115_models.AssignReviewerBySessionGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AssignReviewerBySessionGroupResponse:
        """
        @deprecated OpenAPI AssignReviewerBySessionGroup is deprecated
        
        @summary 会话组批量分配
        
        @param request: AssignReviewerBySessionGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignReviewerBySessionGroupResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssignReviewerBySessionGroup',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.AssignReviewerBySessionGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_reviewer_by_session_group_with_options_async(
        self,
        request: qualitycheck_20190115_models.AssignReviewerBySessionGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AssignReviewerBySessionGroupResponse:
        """
        @deprecated OpenAPI AssignReviewerBySessionGroup is deprecated
        
        @summary 会话组批量分配
        
        @param request: AssignReviewerBySessionGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssignReviewerBySessionGroupResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssignReviewerBySessionGroup',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.AssignReviewerBySessionGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_reviewer_by_session_group(
        self,
        request: qualitycheck_20190115_models.AssignReviewerBySessionGroupRequest,
    ) -> qualitycheck_20190115_models.AssignReviewerBySessionGroupResponse:
        """
        @deprecated OpenAPI AssignReviewerBySessionGroup is deprecated
        
        @summary 会话组批量分配
        
        @param request: AssignReviewerBySessionGroupRequest
        @return: AssignReviewerBySessionGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.assign_reviewer_by_session_group_with_options(request, runtime)

    async def assign_reviewer_by_session_group_async(
        self,
        request: qualitycheck_20190115_models.AssignReviewerBySessionGroupRequest,
    ) -> qualitycheck_20190115_models.AssignReviewerBySessionGroupResponse:
        """
        @deprecated OpenAPI AssignReviewerBySessionGroup is deprecated
        
        @summary 会话组批量分配
        
        @param request: AssignReviewerBySessionGroupRequest
        @return: AssignReviewerBySessionGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.assign_reviewer_by_session_group_with_options_async(request, runtime)

    def batch_submit_review_info_with_options(
        self,
        request: qualitycheck_20190115_models.BatchSubmitReviewInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.BatchSubmitReviewInfoResponse:
        """
        @summary 批量复核
        
        @param request: BatchSubmitReviewInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSubmitReviewInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSubmitReviewInfo',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.BatchSubmitReviewInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_submit_review_info_with_options_async(
        self,
        request: qualitycheck_20190115_models.BatchSubmitReviewInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.BatchSubmitReviewInfoResponse:
        """
        @summary 批量复核
        
        @param request: BatchSubmitReviewInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: BatchSubmitReviewInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSubmitReviewInfo',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.BatchSubmitReviewInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_submit_review_info(
        self,
        request: qualitycheck_20190115_models.BatchSubmitReviewInfoRequest,
    ) -> qualitycheck_20190115_models.BatchSubmitReviewInfoResponse:
        """
        @summary 批量复核
        
        @param request: BatchSubmitReviewInfoRequest
        @return: BatchSubmitReviewInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.batch_submit_review_info_with_options(request, runtime)

    async def batch_submit_review_info_async(
        self,
        request: qualitycheck_20190115_models.BatchSubmitReviewInfoRequest,
    ) -> qualitycheck_20190115_models.BatchSubmitReviewInfoResponse:
        """
        @summary 批量复核
        
        @param request: BatchSubmitReviewInfoRequest
        @return: BatchSubmitReviewInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.batch_submit_review_info_with_options_async(request, runtime)

    def create_asr_vocab_with_options(
        self,
        request: qualitycheck_20190115_models.CreateAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateAsrVocabResponse:
        """
        @summary 创建热词模型
        
        @param request: CreateAsrVocabRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAsrVocabResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAsrVocab',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateAsrVocabResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_asr_vocab_with_options_async(
        self,
        request: qualitycheck_20190115_models.CreateAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateAsrVocabResponse:
        """
        @summary 创建热词模型
        
        @param request: CreateAsrVocabRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAsrVocabResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAsrVocab',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateAsrVocabResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_asr_vocab(
        self,
        request: qualitycheck_20190115_models.CreateAsrVocabRequest,
    ) -> qualitycheck_20190115_models.CreateAsrVocabResponse:
        """
        @summary 创建热词模型
        
        @param request: CreateAsrVocabRequest
        @return: CreateAsrVocabResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_asr_vocab_with_options(request, runtime)

    async def create_asr_vocab_async(
        self,
        request: qualitycheck_20190115_models.CreateAsrVocabRequest,
    ) -> qualitycheck_20190115_models.CreateAsrVocabResponse:
        """
        @summary 创建热词模型
        
        @param request: CreateAsrVocabRequest
        @return: CreateAsrVocabResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_asr_vocab_with_options_async(request, runtime)

    def create_check_type_to_scheme_with_options(
        self,
        request: qualitycheck_20190115_models.CreateCheckTypeToSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateCheckTypeToSchemeResponse:
        """
        @summary 创建质检方案中的质检维度
        
        @param request: CreateCheckTypeToSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCheckTypeToSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCheckTypeToScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateCheckTypeToSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_check_type_to_scheme_with_options_async(
        self,
        request: qualitycheck_20190115_models.CreateCheckTypeToSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateCheckTypeToSchemeResponse:
        """
        @summary 创建质检方案中的质检维度
        
        @param request: CreateCheckTypeToSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateCheckTypeToSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCheckTypeToScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateCheckTypeToSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_check_type_to_scheme(
        self,
        request: qualitycheck_20190115_models.CreateCheckTypeToSchemeRequest,
    ) -> qualitycheck_20190115_models.CreateCheckTypeToSchemeResponse:
        """
        @summary 创建质检方案中的质检维度
        
        @param request: CreateCheckTypeToSchemeRequest
        @return: CreateCheckTypeToSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_check_type_to_scheme_with_options(request, runtime)

    async def create_check_type_to_scheme_async(
        self,
        request: qualitycheck_20190115_models.CreateCheckTypeToSchemeRequest,
    ) -> qualitycheck_20190115_models.CreateCheckTypeToSchemeResponse:
        """
        @summary 创建质检方案中的质检维度
        
        @param request: CreateCheckTypeToSchemeRequest
        @return: CreateCheckTypeToSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_check_type_to_scheme_with_options_async(request, runtime)

    def create_quality_check_scheme_with_options(
        self,
        request: qualitycheck_20190115_models.CreateQualityCheckSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateQualityCheckSchemeResponse:
        """
        @summary 新增质检方案
        
        @param request: CreateQualityCheckSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQualityCheckSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQualityCheckScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateQualityCheckSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quality_check_scheme_with_options_async(
        self,
        request: qualitycheck_20190115_models.CreateQualityCheckSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateQualityCheckSchemeResponse:
        """
        @summary 新增质检方案
        
        @param request: CreateQualityCheckSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateQualityCheckSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateQualityCheckScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateQualityCheckSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quality_check_scheme(
        self,
        request: qualitycheck_20190115_models.CreateQualityCheckSchemeRequest,
    ) -> qualitycheck_20190115_models.CreateQualityCheckSchemeResponse:
        """
        @summary 新增质检方案
        
        @param request: CreateQualityCheckSchemeRequest
        @return: CreateQualityCheckSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_quality_check_scheme_with_options(request, runtime)

    async def create_quality_check_scheme_async(
        self,
        request: qualitycheck_20190115_models.CreateQualityCheckSchemeRequest,
    ) -> qualitycheck_20190115_models.CreateQualityCheckSchemeResponse:
        """
        @summary 新增质检方案
        
        @param request: CreateQualityCheckSchemeRequest
        @return: CreateQualityCheckSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_quality_check_scheme_with_options_async(request, runtime)

    def create_scheme_task_config_with_options(
        self,
        request: qualitycheck_20190115_models.CreateSchemeTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateSchemeTaskConfigResponse:
        """
        @summary 新建质检任务
        
        @param request: CreateSchemeTaskConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSchemeTaskConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSchemeTaskConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateSchemeTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheme_task_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.CreateSchemeTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateSchemeTaskConfigResponse:
        """
        @summary 新建质检任务
        
        @param request: CreateSchemeTaskConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSchemeTaskConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSchemeTaskConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateSchemeTaskConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheme_task_config(
        self,
        request: qualitycheck_20190115_models.CreateSchemeTaskConfigRequest,
    ) -> qualitycheck_20190115_models.CreateSchemeTaskConfigResponse:
        """
        @summary 新建质检任务
        
        @param request: CreateSchemeTaskConfigRequest
        @return: CreateSchemeTaskConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_scheme_task_config_with_options(request, runtime)

    async def create_scheme_task_config_async(
        self,
        request: qualitycheck_20190115_models.CreateSchemeTaskConfigRequest,
    ) -> qualitycheck_20190115_models.CreateSchemeTaskConfigResponse:
        """
        @summary 新建质检任务
        
        @param request: CreateSchemeTaskConfigRequest
        @return: CreateSchemeTaskConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_scheme_task_config_with_options_async(request, runtime)

    def create_skill_group_config_with_options(
        self,
        request: qualitycheck_20190115_models.CreateSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateSkillGroupConfigResponse:
        """
        @param request: CreateSkillGroupConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSkillGroupConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSkillGroupConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateSkillGroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_skill_group_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.CreateSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateSkillGroupConfigResponse:
        """
        @param request: CreateSkillGroupConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSkillGroupConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSkillGroupConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateSkillGroupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_skill_group_config(
        self,
        request: qualitycheck_20190115_models.CreateSkillGroupConfigRequest,
    ) -> qualitycheck_20190115_models.CreateSkillGroupConfigResponse:
        """
        @param request: CreateSkillGroupConfigRequest
        @return: CreateSkillGroupConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_skill_group_config_with_options(request, runtime)

    async def create_skill_group_config_async(
        self,
        request: qualitycheck_20190115_models.CreateSkillGroupConfigRequest,
    ) -> qualitycheck_20190115_models.CreateSkillGroupConfigResponse:
        """
        @param request: CreateSkillGroupConfigRequest
        @return: CreateSkillGroupConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_skill_group_config_with_options_async(request, runtime)

    def create_task_assign_rule_with_options(
        self,
        request: qualitycheck_20190115_models.CreateTaskAssignRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateTaskAssignRuleResponse:
        """
        @param request: CreateTaskAssignRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskAssignRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTaskAssignRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateTaskAssignRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_assign_rule_with_options_async(
        self,
        request: qualitycheck_20190115_models.CreateTaskAssignRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateTaskAssignRuleResponse:
        """
        @param request: CreateTaskAssignRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskAssignRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTaskAssignRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateTaskAssignRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task_assign_rule(
        self,
        request: qualitycheck_20190115_models.CreateTaskAssignRuleRequest,
    ) -> qualitycheck_20190115_models.CreateTaskAssignRuleResponse:
        """
        @param request: CreateTaskAssignRuleRequest
        @return: CreateTaskAssignRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_task_assign_rule_with_options(request, runtime)

    async def create_task_assign_rule_async(
        self,
        request: qualitycheck_20190115_models.CreateTaskAssignRuleRequest,
    ) -> qualitycheck_20190115_models.CreateTaskAssignRuleResponse:
        """
        @param request: CreateTaskAssignRuleRequest
        @return: CreateTaskAssignRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_task_assign_rule_with_options_async(request, runtime)

    def create_warning_config_with_options(
        self,
        request: qualitycheck_20190115_models.CreateWarningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateWarningConfigResponse:
        """
        @param request: CreateWarningConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWarningConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWarningConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateWarningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_warning_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.CreateWarningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateWarningConfigResponse:
        """
        @param request: CreateWarningConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWarningConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWarningConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateWarningConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_warning_config(
        self,
        request: qualitycheck_20190115_models.CreateWarningConfigRequest,
    ) -> qualitycheck_20190115_models.CreateWarningConfigResponse:
        """
        @param request: CreateWarningConfigRequest
        @return: CreateWarningConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_warning_config_with_options(request, runtime)

    async def create_warning_config_async(
        self,
        request: qualitycheck_20190115_models.CreateWarningConfigRequest,
    ) -> qualitycheck_20190115_models.CreateWarningConfigResponse:
        """
        @param request: CreateWarningConfigRequest
        @return: CreateWarningConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_warning_config_with_options_async(request, runtime)

    def create_warning_strategy_config_with_options(
        self,
        request: qualitycheck_20190115_models.CreateWarningStrategyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateWarningStrategyConfigResponse:
        """
        @summary  预警策略-新增
        
        @param request: CreateWarningStrategyConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWarningStrategyConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWarningStrategyConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateWarningStrategyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_warning_strategy_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.CreateWarningStrategyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateWarningStrategyConfigResponse:
        """
        @summary  预警策略-新增
        
        @param request: CreateWarningStrategyConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWarningStrategyConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWarningStrategyConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.CreateWarningStrategyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_warning_strategy_config(
        self,
        request: qualitycheck_20190115_models.CreateWarningStrategyConfigRequest,
    ) -> qualitycheck_20190115_models.CreateWarningStrategyConfigResponse:
        """
        @summary  预警策略-新增
        
        @param request: CreateWarningStrategyConfigRequest
        @return: CreateWarningStrategyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_warning_strategy_config_with_options(request, runtime)

    async def create_warning_strategy_config_async(
        self,
        request: qualitycheck_20190115_models.CreateWarningStrategyConfigRequest,
    ) -> qualitycheck_20190115_models.CreateWarningStrategyConfigResponse:
        """
        @summary  预警策略-新增
        
        @param request: CreateWarningStrategyConfigRequest
        @return: CreateWarningStrategyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_warning_strategy_config_with_options_async(request, runtime)

    def del_rule_category_with_options(
        self,
        request: qualitycheck_20190115_models.DelRuleCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DelRuleCategoryResponse:
        """
        @param request: DelRuleCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DelRuleCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelRuleCategory',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DelRuleCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def del_rule_category_with_options_async(
        self,
        request: qualitycheck_20190115_models.DelRuleCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DelRuleCategoryResponse:
        """
        @param request: DelRuleCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DelRuleCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelRuleCategory',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DelRuleCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def del_rule_category(
        self,
        request: qualitycheck_20190115_models.DelRuleCategoryRequest,
    ) -> qualitycheck_20190115_models.DelRuleCategoryResponse:
        """
        @param request: DelRuleCategoryRequest
        @return: DelRuleCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.del_rule_category_with_options(request, runtime)

    async def del_rule_category_async(
        self,
        request: qualitycheck_20190115_models.DelRuleCategoryRequest,
    ) -> qualitycheck_20190115_models.DelRuleCategoryResponse:
        """
        @param request: DelRuleCategoryRequest
        @return: DelRuleCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.del_rule_category_with_options_async(request, runtime)

    def delete_asr_vocab_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteAsrVocabResponse:
        """
        @param request: DeleteAsrVocabRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAsrVocabResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAsrVocab',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteAsrVocabResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_asr_vocab_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteAsrVocabResponse:
        """
        @param request: DeleteAsrVocabRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAsrVocabResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAsrVocab',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteAsrVocabResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_asr_vocab(
        self,
        request: qualitycheck_20190115_models.DeleteAsrVocabRequest,
    ) -> qualitycheck_20190115_models.DeleteAsrVocabResponse:
        """
        @param request: DeleteAsrVocabRequest
        @return: DeleteAsrVocabResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_asr_vocab_with_options(request, runtime)

    async def delete_asr_vocab_async(
        self,
        request: qualitycheck_20190115_models.DeleteAsrVocabRequest,
    ) -> qualitycheck_20190115_models.DeleteAsrVocabResponse:
        """
        @param request: DeleteAsrVocabRequest
        @return: DeleteAsrVocabResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_asr_vocab_with_options_async(request, runtime)

    def delete_business_category_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteBusinessCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteBusinessCategoryResponse:
        """
        @param request: DeleteBusinessCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBusinessCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBusinessCategory',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteBusinessCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_business_category_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteBusinessCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteBusinessCategoryResponse:
        """
        @param request: DeleteBusinessCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBusinessCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBusinessCategory',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteBusinessCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_business_category(
        self,
        request: qualitycheck_20190115_models.DeleteBusinessCategoryRequest,
    ) -> qualitycheck_20190115_models.DeleteBusinessCategoryResponse:
        """
        @param request: DeleteBusinessCategoryRequest
        @return: DeleteBusinessCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_business_category_with_options(request, runtime)

    async def delete_business_category_async(
        self,
        request: qualitycheck_20190115_models.DeleteBusinessCategoryRequest,
    ) -> qualitycheck_20190115_models.DeleteBusinessCategoryResponse:
        """
        @param request: DeleteBusinessCategoryRequest
        @return: DeleteBusinessCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_business_category_with_options_async(request, runtime)

    def delete_check_type_to_scheme_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteCheckTypeToSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteCheckTypeToSchemeResponse:
        """
        @summary 删除质检唯独
        
        @param request: DeleteCheckTypeToSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCheckTypeToSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCheckTypeToScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteCheckTypeToSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_check_type_to_scheme_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteCheckTypeToSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteCheckTypeToSchemeResponse:
        """
        @summary 删除质检唯独
        
        @param request: DeleteCheckTypeToSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCheckTypeToSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCheckTypeToScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteCheckTypeToSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_check_type_to_scheme(
        self,
        request: qualitycheck_20190115_models.DeleteCheckTypeToSchemeRequest,
    ) -> qualitycheck_20190115_models.DeleteCheckTypeToSchemeResponse:
        """
        @summary 删除质检唯独
        
        @param request: DeleteCheckTypeToSchemeRequest
        @return: DeleteCheckTypeToSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_check_type_to_scheme_with_options(request, runtime)

    async def delete_check_type_to_scheme_async(
        self,
        request: qualitycheck_20190115_models.DeleteCheckTypeToSchemeRequest,
    ) -> qualitycheck_20190115_models.DeleteCheckTypeToSchemeResponse:
        """
        @summary 删除质检唯独
        
        @param request: DeleteCheckTypeToSchemeRequest
        @return: DeleteCheckTypeToSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_check_type_to_scheme_with_options_async(request, runtime)

    def delete_customization_config_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteCustomizationConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteCustomizationConfigResponse:
        """
        @param request: DeleteCustomizationConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomizationConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomizationConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteCustomizationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_customization_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteCustomizationConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteCustomizationConfigResponse:
        """
        @param request: DeleteCustomizationConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCustomizationConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomizationConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteCustomizationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_customization_config(
        self,
        request: qualitycheck_20190115_models.DeleteCustomizationConfigRequest,
    ) -> qualitycheck_20190115_models.DeleteCustomizationConfigResponse:
        """
        @param request: DeleteCustomizationConfigRequest
        @return: DeleteCustomizationConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_customization_config_with_options(request, runtime)

    async def delete_customization_config_async(
        self,
        request: qualitycheck_20190115_models.DeleteCustomizationConfigRequest,
    ) -> qualitycheck_20190115_models.DeleteCustomizationConfigResponse:
        """
        @param request: DeleteCustomizationConfigRequest
        @return: DeleteCustomizationConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_customization_config_with_options_async(request, runtime)

    def delete_data_set_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteDataSetResponse:
        """
        @deprecated OpenAPI DeleteDataSet is deprecated
        
        @param request: DeleteDataSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSetResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataSet',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_set_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteDataSetResponse:
        """
        @deprecated OpenAPI DeleteDataSet is deprecated
        
        @param request: DeleteDataSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDataSetResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataSet',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_set(
        self,
        request: qualitycheck_20190115_models.DeleteDataSetRequest,
    ) -> qualitycheck_20190115_models.DeleteDataSetResponse:
        """
        @deprecated OpenAPI DeleteDataSet is deprecated
        
        @param request: DeleteDataSetRequest
        @return: DeleteDataSetResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_data_set_with_options(request, runtime)

    async def delete_data_set_async(
        self,
        request: qualitycheck_20190115_models.DeleteDataSetRequest,
    ) -> qualitycheck_20190115_models.DeleteDataSetResponse:
        """
        @deprecated OpenAPI DeleteDataSet is deprecated
        
        @param request: DeleteDataSetRequest
        @return: DeleteDataSetResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_set_with_options_async(request, runtime)

    def delete_precision_task_with_options(
        self,
        request: qualitycheck_20190115_models.DeletePrecisionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeletePrecisionTaskResponse:
        """
        @param request: DeletePrecisionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePrecisionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrecisionTask',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeletePrecisionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_precision_task_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeletePrecisionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeletePrecisionTaskResponse:
        """
        @param request: DeletePrecisionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeletePrecisionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrecisionTask',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeletePrecisionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_precision_task(
        self,
        request: qualitycheck_20190115_models.DeletePrecisionTaskRequest,
    ) -> qualitycheck_20190115_models.DeletePrecisionTaskResponse:
        """
        @param request: DeletePrecisionTaskRequest
        @return: DeletePrecisionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_precision_task_with_options(request, runtime)

    async def delete_precision_task_async(
        self,
        request: qualitycheck_20190115_models.DeletePrecisionTaskRequest,
    ) -> qualitycheck_20190115_models.DeletePrecisionTaskResponse:
        """
        @param request: DeletePrecisionTaskRequest
        @return: DeletePrecisionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_precision_task_with_options_async(request, runtime)

    def delete_quality_check_scheme_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteQualityCheckSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteQualityCheckSchemeResponse:
        """
        @summary 删除质检方案
        
        @param request: DeleteQualityCheckSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQualityCheckSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQualityCheckScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteQualityCheckSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quality_check_scheme_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteQualityCheckSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteQualityCheckSchemeResponse:
        """
        @summary 删除质检方案
        
        @param request: DeleteQualityCheckSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteQualityCheckSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteQualityCheckScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteQualityCheckSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quality_check_scheme(
        self,
        request: qualitycheck_20190115_models.DeleteQualityCheckSchemeRequest,
    ) -> qualitycheck_20190115_models.DeleteQualityCheckSchemeResponse:
        """
        @summary 删除质检方案
        
        @param request: DeleteQualityCheckSchemeRequest
        @return: DeleteQualityCheckSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_check_scheme_with_options(request, runtime)

    async def delete_quality_check_scheme_async(
        self,
        request: qualitycheck_20190115_models.DeleteQualityCheckSchemeRequest,
    ) -> qualitycheck_20190115_models.DeleteQualityCheckSchemeResponse:
        """
        @summary 删除质检方案
        
        @param request: DeleteQualityCheckSchemeRequest
        @return: DeleteQualityCheckSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_quality_check_scheme_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteRuleResponse:
        """
        @deprecated OpenAPI DeleteRule is deprecated, please use Qualitycheck::2019-01-15::DeleteRuleV4 instead.
        
        @summary 删除规则
        
        @param request: DeleteRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not UtilClient.is_unset(request.force_delete):
            body['ForceDelete'] = request.force_delete
        if not UtilClient.is_unset(request.is_scheme_data):
            body['IsSchemeData'] = request.is_scheme_data
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteRuleResponse:
        """
        @deprecated OpenAPI DeleteRule is deprecated, please use Qualitycheck::2019-01-15::DeleteRuleV4 instead.
        
        @summary 删除规则
        
        @param request: DeleteRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not UtilClient.is_unset(request.force_delete):
            body['ForceDelete'] = request.force_delete
        if not UtilClient.is_unset(request.is_scheme_data):
            body['IsSchemeData'] = request.is_scheme_data
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rule(
        self,
        request: qualitycheck_20190115_models.DeleteRuleRequest,
    ) -> qualitycheck_20190115_models.DeleteRuleResponse:
        """
        @deprecated OpenAPI DeleteRule is deprecated, please use Qualitycheck::2019-01-15::DeleteRuleV4 instead.
        
        @summary 删除规则
        
        @param request: DeleteRuleRequest
        @return: DeleteRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: qualitycheck_20190115_models.DeleteRuleRequest,
    ) -> qualitycheck_20190115_models.DeleteRuleResponse:
        """
        @deprecated OpenAPI DeleteRule is deprecated, please use Qualitycheck::2019-01-15::DeleteRuleV4 instead.
        
        @summary 删除规则
        
        @param request: DeleteRuleRequest
        @return: DeleteRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def delete_rule_v4with_options(
        self,
        request: qualitycheck_20190115_models.DeleteRuleV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteRuleV4Response:
        """
        @summary V4删除规则
        
        @param request: DeleteRuleV4Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRuleV4Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not UtilClient.is_unset(request.force_delete):
            body['ForceDelete'] = request.force_delete
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRuleV4',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteRuleV4Response(),
            self.call_api(params, req, runtime)
        )

    async def delete_rule_v4with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteRuleV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteRuleV4Response:
        """
        @summary V4删除规则
        
        @param request: DeleteRuleV4Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRuleV4Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not UtilClient.is_unset(request.force_delete):
            body['ForceDelete'] = request.force_delete
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRuleV4',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteRuleV4Response(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rule_v4(
        self,
        request: qualitycheck_20190115_models.DeleteRuleV4Request,
    ) -> qualitycheck_20190115_models.DeleteRuleV4Response:
        """
        @summary V4删除规则
        
        @param request: DeleteRuleV4Request
        @return: DeleteRuleV4Response
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_v4with_options(request, runtime)

    async def delete_rule_v4_async(
        self,
        request: qualitycheck_20190115_models.DeleteRuleV4Request,
    ) -> qualitycheck_20190115_models.DeleteRuleV4Response:
        """
        @summary V4删除规则
        
        @param request: DeleteRuleV4Request
        @return: DeleteRuleV4Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_v4with_options_async(request, runtime)

    def delete_scheme_task_config_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteSchemeTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteSchemeTaskConfigResponse:
        """
        @summary 删除质检任务
        
        @param request: DeleteSchemeTaskConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSchemeTaskConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSchemeTaskConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteSchemeTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scheme_task_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteSchemeTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteSchemeTaskConfigResponse:
        """
        @summary 删除质检任务
        
        @param request: DeleteSchemeTaskConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSchemeTaskConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSchemeTaskConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteSchemeTaskConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scheme_task_config(
        self,
        request: qualitycheck_20190115_models.DeleteSchemeTaskConfigRequest,
    ) -> qualitycheck_20190115_models.DeleteSchemeTaskConfigResponse:
        """
        @summary 删除质检任务
        
        @param request: DeleteSchemeTaskConfigRequest
        @return: DeleteSchemeTaskConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_scheme_task_config_with_options(request, runtime)

    async def delete_scheme_task_config_async(
        self,
        request: qualitycheck_20190115_models.DeleteSchemeTaskConfigRequest,
    ) -> qualitycheck_20190115_models.DeleteSchemeTaskConfigResponse:
        """
        @summary 删除质检任务
        
        @param request: DeleteSchemeTaskConfigRequest
        @return: DeleteSchemeTaskConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_scheme_task_config_with_options_async(request, runtime)

    def delete_skill_group_config_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteSkillGroupConfigResponse:
        """
        @param request: DeleteSkillGroupConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSkillGroupConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSkillGroupConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteSkillGroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_skill_group_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteSkillGroupConfigResponse:
        """
        @param request: DeleteSkillGroupConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteSkillGroupConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSkillGroupConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteSkillGroupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_skill_group_config(
        self,
        request: qualitycheck_20190115_models.DeleteSkillGroupConfigRequest,
    ) -> qualitycheck_20190115_models.DeleteSkillGroupConfigResponse:
        """
        @param request: DeleteSkillGroupConfigRequest
        @return: DeleteSkillGroupConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_skill_group_config_with_options(request, runtime)

    async def delete_skill_group_config_async(
        self,
        request: qualitycheck_20190115_models.DeleteSkillGroupConfigRequest,
    ) -> qualitycheck_20190115_models.DeleteSkillGroupConfigResponse:
        """
        @param request: DeleteSkillGroupConfigRequest
        @return: DeleteSkillGroupConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_skill_group_config_with_options_async(request, runtime)

    def delete_task_assign_rule_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteTaskAssignRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteTaskAssignRuleResponse:
        """
        @param request: DeleteTaskAssignRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTaskAssignRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTaskAssignRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteTaskAssignRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_task_assign_rule_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteTaskAssignRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteTaskAssignRuleResponse:
        """
        @param request: DeleteTaskAssignRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTaskAssignRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTaskAssignRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteTaskAssignRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_task_assign_rule(
        self,
        request: qualitycheck_20190115_models.DeleteTaskAssignRuleRequest,
    ) -> qualitycheck_20190115_models.DeleteTaskAssignRuleResponse:
        """
        @param request: DeleteTaskAssignRuleRequest
        @return: DeleteTaskAssignRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_task_assign_rule_with_options(request, runtime)

    async def delete_task_assign_rule_async(
        self,
        request: qualitycheck_20190115_models.DeleteTaskAssignRuleRequest,
    ) -> qualitycheck_20190115_models.DeleteTaskAssignRuleResponse:
        """
        @param request: DeleteTaskAssignRuleRequest
        @return: DeleteTaskAssignRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_task_assign_rule_with_options_async(request, runtime)

    def delete_warning_config_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteWarningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteWarningConfigResponse:
        """
        @param request: DeleteWarningConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWarningConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWarningConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteWarningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_warning_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteWarningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteWarningConfigResponse:
        """
        @param request: DeleteWarningConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWarningConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWarningConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteWarningConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_warning_config(
        self,
        request: qualitycheck_20190115_models.DeleteWarningConfigRequest,
    ) -> qualitycheck_20190115_models.DeleteWarningConfigResponse:
        """
        @param request: DeleteWarningConfigRequest
        @return: DeleteWarningConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_warning_config_with_options(request, runtime)

    async def delete_warning_config_async(
        self,
        request: qualitycheck_20190115_models.DeleteWarningConfigRequest,
    ) -> qualitycheck_20190115_models.DeleteWarningConfigResponse:
        """
        @param request: DeleteWarningConfigRequest
        @return: DeleteWarningConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_warning_config_with_options_async(request, runtime)

    def delete_warning_strategy_config_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteWarningStrategyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteWarningStrategyConfigResponse:
        """
        @summary  预警策略-删除
        
        @param request: DeleteWarningStrategyConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWarningStrategyConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWarningStrategyConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteWarningStrategyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_warning_strategy_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteWarningStrategyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteWarningStrategyConfigResponse:
        """
        @summary  预警策略-删除
        
        @param request: DeleteWarningStrategyConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWarningStrategyConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWarningStrategyConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.DeleteWarningStrategyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_warning_strategy_config(
        self,
        request: qualitycheck_20190115_models.DeleteWarningStrategyConfigRequest,
    ) -> qualitycheck_20190115_models.DeleteWarningStrategyConfigResponse:
        """
        @summary  预警策略-删除
        
        @param request: DeleteWarningStrategyConfigRequest
        @return: DeleteWarningStrategyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_warning_strategy_config_with_options(request, runtime)

    async def delete_warning_strategy_config_async(
        self,
        request: qualitycheck_20190115_models.DeleteWarningStrategyConfigRequest,
    ) -> qualitycheck_20190115_models.DeleteWarningStrategyConfigResponse:
        """
        @summary  预警策略-删除
        
        @param request: DeleteWarningStrategyConfigRequest
        @return: DeleteWarningStrategyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_warning_strategy_config_with_options_async(request, runtime)

    def get_asr_vocab_with_options(
        self,
        request: qualitycheck_20190115_models.GetAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetAsrVocabResponse:
        """
        @param request: GetAsrVocabRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsrVocabResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsrVocab',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetAsrVocabResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_asr_vocab_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetAsrVocabResponse:
        """
        @param request: GetAsrVocabRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAsrVocabResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsrVocab',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetAsrVocabResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_asr_vocab(
        self,
        request: qualitycheck_20190115_models.GetAsrVocabRequest,
    ) -> qualitycheck_20190115_models.GetAsrVocabResponse:
        """
        @param request: GetAsrVocabRequest
        @return: GetAsrVocabResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_asr_vocab_with_options(request, runtime)

    async def get_asr_vocab_async(
        self,
        request: qualitycheck_20190115_models.GetAsrVocabRequest,
    ) -> qualitycheck_20190115_models.GetAsrVocabResponse:
        """
        @param request: GetAsrVocabRequest
        @return: GetAsrVocabResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_asr_vocab_with_options_async(request, runtime)

    def get_business_category_list_with_options(
        self,
        request: qualitycheck_20190115_models.GetBusinessCategoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetBusinessCategoryListResponse:
        """
        @param request: GetBusinessCategoryListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBusinessCategoryListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessCategoryList',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetBusinessCategoryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_category_list_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetBusinessCategoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetBusinessCategoryListResponse:
        """
        @param request: GetBusinessCategoryListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetBusinessCategoryListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBusinessCategoryList',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetBusinessCategoryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business_category_list(
        self,
        request: qualitycheck_20190115_models.GetBusinessCategoryListRequest,
    ) -> qualitycheck_20190115_models.GetBusinessCategoryListResponse:
        """
        @param request: GetBusinessCategoryListRequest
        @return: GetBusinessCategoryListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_business_category_list_with_options(request, runtime)

    async def get_business_category_list_async(
        self,
        request: qualitycheck_20190115_models.GetBusinessCategoryListRequest,
    ) -> qualitycheck_20190115_models.GetBusinessCategoryListResponse:
        """
        @param request: GetBusinessCategoryListRequest
        @return: GetBusinessCategoryListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_business_category_list_with_options_async(request, runtime)

    def get_customization_config_list_with_options(
        self,
        request: qualitycheck_20190115_models.GetCustomizationConfigListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetCustomizationConfigListResponse:
        """
        @summary 获取语音模型列表
        
        @param request: GetCustomizationConfigListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomizationConfigListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomizationConfigList',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetCustomizationConfigListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_customization_config_list_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetCustomizationConfigListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetCustomizationConfigListResponse:
        """
        @summary 获取语音模型列表
        
        @param request: GetCustomizationConfigListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCustomizationConfigListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomizationConfigList',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetCustomizationConfigListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_customization_config_list(
        self,
        request: qualitycheck_20190115_models.GetCustomizationConfigListRequest,
    ) -> qualitycheck_20190115_models.GetCustomizationConfigListResponse:
        """
        @summary 获取语音模型列表
        
        @param request: GetCustomizationConfigListRequest
        @return: GetCustomizationConfigListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_customization_config_list_with_options(request, runtime)

    async def get_customization_config_list_async(
        self,
        request: qualitycheck_20190115_models.GetCustomizationConfigListRequest,
    ) -> qualitycheck_20190115_models.GetCustomizationConfigListResponse:
        """
        @summary 获取语音模型列表
        
        @param request: GetCustomizationConfigListRequest
        @return: GetCustomizationConfigListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_customization_config_list_with_options_async(request, runtime)

    def get_next_result_to_verify_with_options(
        self,
        request: qualitycheck_20190115_models.GetNextResultToVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetNextResultToVerifyResponse:
        """
        @param request: GetNextResultToVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNextResultToVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNextResultToVerify',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetNextResultToVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_next_result_to_verify_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetNextResultToVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetNextResultToVerifyResponse:
        """
        @param request: GetNextResultToVerifyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNextResultToVerifyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNextResultToVerify',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetNextResultToVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_next_result_to_verify(
        self,
        request: qualitycheck_20190115_models.GetNextResultToVerifyRequest,
    ) -> qualitycheck_20190115_models.GetNextResultToVerifyResponse:
        """
        @param request: GetNextResultToVerifyRequest
        @return: GetNextResultToVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_next_result_to_verify_with_options(request, runtime)

    async def get_next_result_to_verify_async(
        self,
        request: qualitycheck_20190115_models.GetNextResultToVerifyRequest,
    ) -> qualitycheck_20190115_models.GetNextResultToVerifyResponse:
        """
        @param request: GetNextResultToVerifyRequest
        @return: GetNextResultToVerifyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_next_result_to_verify_with_options_async(request, runtime)

    def get_precision_task_with_options(
        self,
        request: qualitycheck_20190115_models.GetPrecisionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetPrecisionTaskResponse:
        """
        @param request: GetPrecisionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrecisionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrecisionTask',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetPrecisionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_precision_task_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetPrecisionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetPrecisionTaskResponse:
        """
        @param request: GetPrecisionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrecisionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrecisionTask',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetPrecisionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_precision_task(
        self,
        request: qualitycheck_20190115_models.GetPrecisionTaskRequest,
    ) -> qualitycheck_20190115_models.GetPrecisionTaskResponse:
        """
        @param request: GetPrecisionTaskRequest
        @return: GetPrecisionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_precision_task_with_options(request, runtime)

    async def get_precision_task_async(
        self,
        request: qualitycheck_20190115_models.GetPrecisionTaskRequest,
    ) -> qualitycheck_20190115_models.GetPrecisionTaskResponse:
        """
        @param request: GetPrecisionTaskRequest
        @return: GetPrecisionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_precision_task_with_options_async(request, runtime)

    def get_quality_check_scheme_with_options(
        self,
        request: qualitycheck_20190115_models.GetQualityCheckSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetQualityCheckSchemeResponse:
        """
        @summary 获取质检方案
        
        @param request: GetQualityCheckSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityCheckSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualityCheckScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetQualityCheckSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_check_scheme_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetQualityCheckSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetQualityCheckSchemeResponse:
        """
        @summary 获取质检方案
        
        @param request: GetQualityCheckSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetQualityCheckSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetQualityCheckScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetQualityCheckSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_check_scheme(
        self,
        request: qualitycheck_20190115_models.GetQualityCheckSchemeRequest,
    ) -> qualitycheck_20190115_models.GetQualityCheckSchemeResponse:
        """
        @summary 获取质检方案
        
        @param request: GetQualityCheckSchemeRequest
        @return: GetQualityCheckSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_quality_check_scheme_with_options(request, runtime)

    async def get_quality_check_scheme_async(
        self,
        request: qualitycheck_20190115_models.GetQualityCheckSchemeRequest,
    ) -> qualitycheck_20190115_models.GetQualityCheckSchemeResponse:
        """
        @summary 获取质检方案
        
        @param request: GetQualityCheckSchemeRequest
        @return: GetQualityCheckSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_check_scheme_with_options_async(request, runtime)

    def get_result_with_options(
        self,
        request: qualitycheck_20190115_models.GetResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetResultResponse:
        """
        @param request: GetResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResult',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_result_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetResultResponse:
        """
        @param request: GetResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResult',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_result(
        self,
        request: qualitycheck_20190115_models.GetResultRequest,
    ) -> qualitycheck_20190115_models.GetResultResponse:
        """
        @param request: GetResultRequest
        @return: GetResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_result_with_options(request, runtime)

    async def get_result_async(
        self,
        request: qualitycheck_20190115_models.GetResultRequest,
    ) -> qualitycheck_20190115_models.GetResultResponse:
        """
        @param request: GetResultRequest
        @return: GetResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_result_with_options_async(request, runtime)

    def get_result_to_review_with_options(
        self,
        request: qualitycheck_20190115_models.GetResultToReviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetResultToReviewResponse:
        """
        @param request: GetResultToReviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResultToReviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResultToReview',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetResultToReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_result_to_review_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetResultToReviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetResultToReviewResponse:
        """
        @param request: GetResultToReviewRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResultToReviewResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResultToReview',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetResultToReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_result_to_review(
        self,
        request: qualitycheck_20190115_models.GetResultToReviewRequest,
    ) -> qualitycheck_20190115_models.GetResultToReviewResponse:
        """
        @param request: GetResultToReviewRequest
        @return: GetResultToReviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_result_to_review_with_options(request, runtime)

    async def get_result_to_review_async(
        self,
        request: qualitycheck_20190115_models.GetResultToReviewRequest,
    ) -> qualitycheck_20190115_models.GetResultToReviewResponse:
        """
        @param request: GetResultToReviewRequest
        @return: GetResultToReviewResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_result_to_review_with_options_async(request, runtime)

    def get_rule_with_options(
        self,
        request: qualitycheck_20190115_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleResponse:
        """
        @deprecated OpenAPI GetRule is deprecated, please use Qualitycheck::2019-01-15::GetRuleV4 instead.
        
        @param request: GetRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rule_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleResponse:
        """
        @deprecated OpenAPI GetRule is deprecated, please use Qualitycheck::2019-01-15::GetRuleV4 instead.
        
        @param request: GetRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rule(
        self,
        request: qualitycheck_20190115_models.GetRuleRequest,
    ) -> qualitycheck_20190115_models.GetRuleResponse:
        """
        @deprecated OpenAPI GetRule is deprecated, please use Qualitycheck::2019-01-15::GetRuleV4 instead.
        
        @param request: GetRuleRequest
        @return: GetRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_rule_with_options(request, runtime)

    async def get_rule_async(
        self,
        request: qualitycheck_20190115_models.GetRuleRequest,
    ) -> qualitycheck_20190115_models.GetRuleResponse:
        """
        @deprecated OpenAPI GetRule is deprecated, please use Qualitycheck::2019-01-15::GetRuleV4 instead.
        
        @param request: GetRuleRequest
        @return: GetRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_with_options_async(request, runtime)

    def get_rule_by_id_with_options(
        self,
        request: qualitycheck_20190115_models.GetRuleByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleByIdResponse:
        """
        @deprecated OpenAPI GetRuleById is deprecated, please use Qualitycheck::2019-01-15::GetRuleV4 instead.
        
        @summary 获取规则
        
        @param request: GetRuleByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRuleByIdResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRuleById',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetRuleByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rule_by_id_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetRuleByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleByIdResponse:
        """
        @deprecated OpenAPI GetRuleById is deprecated, please use Qualitycheck::2019-01-15::GetRuleV4 instead.
        
        @summary 获取规则
        
        @param request: GetRuleByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRuleByIdResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRuleById',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetRuleByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rule_by_id(
        self,
        request: qualitycheck_20190115_models.GetRuleByIdRequest,
    ) -> qualitycheck_20190115_models.GetRuleByIdResponse:
        """
        @deprecated OpenAPI GetRuleById is deprecated, please use Qualitycheck::2019-01-15::GetRuleV4 instead.
        
        @summary 获取规则
        
        @param request: GetRuleByIdRequest
        @return: GetRuleByIdResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_rule_by_id_with_options(request, runtime)

    async def get_rule_by_id_async(
        self,
        request: qualitycheck_20190115_models.GetRuleByIdRequest,
    ) -> qualitycheck_20190115_models.GetRuleByIdResponse:
        """
        @deprecated OpenAPI GetRuleById is deprecated, please use Qualitycheck::2019-01-15::GetRuleV4 instead.
        
        @summary 获取规则
        
        @param request: GetRuleByIdRequest
        @return: GetRuleByIdResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_by_id_with_options_async(request, runtime)

    def get_rule_category_with_options(
        self,
        request: qualitycheck_20190115_models.GetRuleCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleCategoryResponse:
        """
        @param request: GetRuleCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRuleCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRuleCategory',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetRuleCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rule_category_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetRuleCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleCategoryResponse:
        """
        @param request: GetRuleCategoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRuleCategoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRuleCategory',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetRuleCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rule_category(
        self,
        request: qualitycheck_20190115_models.GetRuleCategoryRequest,
    ) -> qualitycheck_20190115_models.GetRuleCategoryResponse:
        """
        @param request: GetRuleCategoryRequest
        @return: GetRuleCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_rule_category_with_options(request, runtime)

    async def get_rule_category_async(
        self,
        request: qualitycheck_20190115_models.GetRuleCategoryRequest,
    ) -> qualitycheck_20190115_models.GetRuleCategoryResponse:
        """
        @param request: GetRuleCategoryRequest
        @return: GetRuleCategoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_category_with_options_async(request, runtime)

    def get_rule_detail_with_options(
        self,
        request: qualitycheck_20190115_models.GetRuleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleDetailResponse:
        """
        @deprecated OpenAPI GetRuleDetail is deprecated, please use Qualitycheck::2019-01-15::GetRuleV4 instead.
        
        @param request: GetRuleDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRuleDetailResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRuleDetail',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetRuleDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rule_detail_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetRuleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleDetailResponse:
        """
        @deprecated OpenAPI GetRuleDetail is deprecated, please use Qualitycheck::2019-01-15::GetRuleV4 instead.
        
        @param request: GetRuleDetailRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRuleDetailResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRuleDetail',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetRuleDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rule_detail(
        self,
        request: qualitycheck_20190115_models.GetRuleDetailRequest,
    ) -> qualitycheck_20190115_models.GetRuleDetailResponse:
        """
        @deprecated OpenAPI GetRuleDetail is deprecated, please use Qualitycheck::2019-01-15::GetRuleV4 instead.
        
        @param request: GetRuleDetailRequest
        @return: GetRuleDetailResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_rule_detail_with_options(request, runtime)

    async def get_rule_detail_async(
        self,
        request: qualitycheck_20190115_models.GetRuleDetailRequest,
    ) -> qualitycheck_20190115_models.GetRuleDetailResponse:
        """
        @deprecated OpenAPI GetRuleDetail is deprecated, please use Qualitycheck::2019-01-15::GetRuleV4 instead.
        
        @param request: GetRuleDetailRequest
        @return: GetRuleDetailResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_detail_with_options_async(request, runtime)

    def get_rule_v4with_options(
        self,
        request: qualitycheck_20190115_models.GetRuleV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleV4Response:
        """
        @summary V4获取规则
        
        @param request: GetRuleV4Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRuleV4Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRuleV4',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetRuleV4Response(),
            self.call_api(params, req, runtime)
        )

    async def get_rule_v4with_options_async(
        self,
        request: qualitycheck_20190115_models.GetRuleV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleV4Response:
        """
        @summary V4获取规则
        
        @param request: GetRuleV4Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRuleV4Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRuleV4',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetRuleV4Response(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rule_v4(
        self,
        request: qualitycheck_20190115_models.GetRuleV4Request,
    ) -> qualitycheck_20190115_models.GetRuleV4Response:
        """
        @summary V4获取规则
        
        @param request: GetRuleV4Request
        @return: GetRuleV4Response
        """
        runtime = util_models.RuntimeOptions()
        return self.get_rule_v4with_options(request, runtime)

    async def get_rule_v4_async(
        self,
        request: qualitycheck_20190115_models.GetRuleV4Request,
    ) -> qualitycheck_20190115_models.GetRuleV4Response:
        """
        @summary V4获取规则
        
        @param request: GetRuleV4Request
        @return: GetRuleV4Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_v4with_options_async(request, runtime)

    def get_rules_count_list_with_options(
        self,
        request: qualitycheck_20190115_models.GetRulesCountListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRulesCountListResponse:
        """
        @summary 获得规则列表
        
        @param request: GetRulesCountListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRulesCountListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not UtilClient.is_unset(request.business_name):
            body['BusinessName'] = request.business_name
        if not UtilClient.is_unset(request.business_range):
            body['BusinessRange'] = request.business_range
        if not UtilClient.is_unset(request.category_name):
            body['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.count_total):
            body['CountTotal'] = request.count_total
        if not UtilClient.is_unset(request.create_empid):
            body['CreateEmpid'] = request.create_empid
        if not UtilClient.is_unset(request.create_user_id):
            body['CreateUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.last_update_empid):
            body['LastUpdateEmpid'] = request.last_update_empid
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.require_infos):
            body['RequireInfos'] = request.require_infos
        if not UtilClient.is_unset(request.rid):
            body['Rid'] = request.rid
        if not UtilClient.is_unset(request.rule_id_or_rule_name):
            body['RuleIdOrRuleName'] = request.rule_id_or_rule_name
        if not UtilClient.is_unset(request.rule_score_single_type):
            body['RuleScoreSingleType'] = request.rule_score_single_type
        if not UtilClient.is_unset(request.rule_type):
            body['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.scheme_id):
            body['SchemeId'] = request.scheme_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.type_name):
            body['TypeName'] = request.type_name
        if not UtilClient.is_unset(request.update_end_time):
            body['UpdateEndTime'] = request.update_end_time
        if not UtilClient.is_unset(request.update_start_time):
            body['UpdateStartTime'] = request.update_start_time
        if not UtilClient.is_unset(request.update_user_id):
            body['UpdateUserId'] = request.update_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRulesCountList',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetRulesCountListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rules_count_list_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetRulesCountListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRulesCountListResponse:
        """
        @summary 获得规则列表
        
        @param request: GetRulesCountListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRulesCountListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not UtilClient.is_unset(request.business_name):
            body['BusinessName'] = request.business_name
        if not UtilClient.is_unset(request.business_range):
            body['BusinessRange'] = request.business_range
        if not UtilClient.is_unset(request.category_name):
            body['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.count_total):
            body['CountTotal'] = request.count_total
        if not UtilClient.is_unset(request.create_empid):
            body['CreateEmpid'] = request.create_empid
        if not UtilClient.is_unset(request.create_user_id):
            body['CreateUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.last_update_empid):
            body['LastUpdateEmpid'] = request.last_update_empid
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.require_infos):
            body['RequireInfos'] = request.require_infos
        if not UtilClient.is_unset(request.rid):
            body['Rid'] = request.rid
        if not UtilClient.is_unset(request.rule_id_or_rule_name):
            body['RuleIdOrRuleName'] = request.rule_id_or_rule_name
        if not UtilClient.is_unset(request.rule_score_single_type):
            body['RuleScoreSingleType'] = request.rule_score_single_type
        if not UtilClient.is_unset(request.rule_type):
            body['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.scheme_id):
            body['SchemeId'] = request.scheme_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.type_name):
            body['TypeName'] = request.type_name
        if not UtilClient.is_unset(request.update_end_time):
            body['UpdateEndTime'] = request.update_end_time
        if not UtilClient.is_unset(request.update_start_time):
            body['UpdateStartTime'] = request.update_start_time
        if not UtilClient.is_unset(request.update_user_id):
            body['UpdateUserId'] = request.update_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRulesCountList',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetRulesCountListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rules_count_list(
        self,
        request: qualitycheck_20190115_models.GetRulesCountListRequest,
    ) -> qualitycheck_20190115_models.GetRulesCountListResponse:
        """
        @summary 获得规则列表
        
        @param request: GetRulesCountListRequest
        @return: GetRulesCountListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_rules_count_list_with_options(request, runtime)

    async def get_rules_count_list_async(
        self,
        request: qualitycheck_20190115_models.GetRulesCountListRequest,
    ) -> qualitycheck_20190115_models.GetRulesCountListResponse:
        """
        @summary 获得规则列表
        
        @param request: GetRulesCountListRequest
        @return: GetRulesCountListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_rules_count_list_with_options_async(request, runtime)

    def get_score_info_with_options(
        self,
        request: qualitycheck_20190115_models.GetScoreInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetScoreInfoResponse:
        """
        @deprecated OpenAPI GetScoreInfo is deprecated
        
        @param request: GetScoreInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScoreInfoResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScoreInfo',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetScoreInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_score_info_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetScoreInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetScoreInfoResponse:
        """
        @deprecated OpenAPI GetScoreInfo is deprecated
        
        @param request: GetScoreInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetScoreInfoResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetScoreInfo',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetScoreInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_score_info(
        self,
        request: qualitycheck_20190115_models.GetScoreInfoRequest,
    ) -> qualitycheck_20190115_models.GetScoreInfoResponse:
        """
        @deprecated OpenAPI GetScoreInfo is deprecated
        
        @param request: GetScoreInfoRequest
        @return: GetScoreInfoResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_score_info_with_options(request, runtime)

    async def get_score_info_async(
        self,
        request: qualitycheck_20190115_models.GetScoreInfoRequest,
    ) -> qualitycheck_20190115_models.GetScoreInfoResponse:
        """
        @deprecated OpenAPI GetScoreInfo is deprecated
        
        @param request: GetScoreInfoRequest
        @return: GetScoreInfoResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_score_info_with_options_async(request, runtime)

    def get_skill_group_config_with_options(
        self,
        request: qualitycheck_20190115_models.GetSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetSkillGroupConfigResponse:
        """
        @param request: GetSkillGroupConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSkillGroupConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSkillGroupConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetSkillGroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_group_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetSkillGroupConfigResponse:
        """
        @param request: GetSkillGroupConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSkillGroupConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSkillGroupConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetSkillGroupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_group_config(
        self,
        request: qualitycheck_20190115_models.GetSkillGroupConfigRequest,
    ) -> qualitycheck_20190115_models.GetSkillGroupConfigResponse:
        """
        @param request: GetSkillGroupConfigRequest
        @return: GetSkillGroupConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_config_with_options(request, runtime)

    async def get_skill_group_config_async(
        self,
        request: qualitycheck_20190115_models.GetSkillGroupConfigRequest,
    ) -> qualitycheck_20190115_models.GetSkillGroupConfigResponse:
        """
        @param request: GetSkillGroupConfigRequest
        @return: GetSkillGroupConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_skill_group_config_with_options_async(request, runtime)

    def get_sync_result_with_options(
        self,
        request: qualitycheck_20190115_models.GetSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetSyncResultResponse:
        """
        @deprecated OpenAPI GetSyncResult is deprecated, please use Qualitycheck::2019-01-15::GetResult instead.
        
        @param request: GetSyncResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSyncResultResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSyncResult',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetSyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sync_result_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetSyncResultResponse:
        """
        @deprecated OpenAPI GetSyncResult is deprecated, please use Qualitycheck::2019-01-15::GetResult instead.
        
        @param request: GetSyncResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSyncResultResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSyncResult',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetSyncResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sync_result(
        self,
        request: qualitycheck_20190115_models.GetSyncResultRequest,
    ) -> qualitycheck_20190115_models.GetSyncResultResponse:
        """
        @deprecated OpenAPI GetSyncResult is deprecated, please use Qualitycheck::2019-01-15::GetResult instead.
        
        @param request: GetSyncResultRequest
        @return: GetSyncResultResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_sync_result_with_options(request, runtime)

    async def get_sync_result_async(
        self,
        request: qualitycheck_20190115_models.GetSyncResultRequest,
    ) -> qualitycheck_20190115_models.GetSyncResultResponse:
        """
        @deprecated OpenAPI GetSyncResult is deprecated, please use Qualitycheck::2019-01-15::GetResult instead.
        
        @param request: GetSyncResultRequest
        @return: GetSyncResultResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_sync_result_with_options_async(request, runtime)

    def get_warning_strategy_config_with_options(
        self,
        request: qualitycheck_20190115_models.GetWarningStrategyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetWarningStrategyConfigResponse:
        """
        @summary 预警策略-详情
        
        @param request: GetWarningStrategyConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWarningStrategyConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWarningStrategyConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetWarningStrategyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_warning_strategy_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetWarningStrategyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetWarningStrategyConfigResponse:
        """
        @summary 预警策略-详情
        
        @param request: GetWarningStrategyConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWarningStrategyConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWarningStrategyConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.GetWarningStrategyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_warning_strategy_config(
        self,
        request: qualitycheck_20190115_models.GetWarningStrategyConfigRequest,
    ) -> qualitycheck_20190115_models.GetWarningStrategyConfigResponse:
        """
        @summary 预警策略-详情
        
        @param request: GetWarningStrategyConfigRequest
        @return: GetWarningStrategyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_warning_strategy_config_with_options(request, runtime)

    async def get_warning_strategy_config_async(
        self,
        request: qualitycheck_20190115_models.GetWarningStrategyConfigRequest,
    ) -> qualitycheck_20190115_models.GetWarningStrategyConfigResponse:
        """
        @summary 预警策略-详情
        
        @param request: GetWarningStrategyConfigRequest
        @return: GetWarningStrategyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_warning_strategy_config_with_options_async(request, runtime)

    def handle_complaint_with_options(
        self,
        request: qualitycheck_20190115_models.HandleComplaintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.HandleComplaintResponse:
        """
        @param request: HandleComplaintRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: HandleComplaintResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HandleComplaint',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.HandleComplaintResponse(),
            self.call_api(params, req, runtime)
        )

    async def handle_complaint_with_options_async(
        self,
        request: qualitycheck_20190115_models.HandleComplaintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.HandleComplaintResponse:
        """
        @param request: HandleComplaintRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: HandleComplaintResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HandleComplaint',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.HandleComplaintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def handle_complaint(
        self,
        request: qualitycheck_20190115_models.HandleComplaintRequest,
    ) -> qualitycheck_20190115_models.HandleComplaintResponse:
        """
        @param request: HandleComplaintRequest
        @return: HandleComplaintResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.handle_complaint_with_options(request, runtime)

    async def handle_complaint_async(
        self,
        request: qualitycheck_20190115_models.HandleComplaintRequest,
    ) -> qualitycheck_20190115_models.HandleComplaintResponse:
        """
        @param request: HandleComplaintRequest
        @return: HandleComplaintResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.handle_complaint_with_options_async(request, runtime)

    def invalid_rule_with_options(
        self,
        request: qualitycheck_20190115_models.InvalidRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.InvalidRuleResponse:
        """
        @deprecated OpenAPI InvalidRule is deprecated, please use Qualitycheck::2019-01-15::DeleteRuleV4 instead.
        
        @param request: InvalidRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvalidRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvalidRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.InvalidRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def invalid_rule_with_options_async(
        self,
        request: qualitycheck_20190115_models.InvalidRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.InvalidRuleResponse:
        """
        @deprecated OpenAPI InvalidRule is deprecated, please use Qualitycheck::2019-01-15::DeleteRuleV4 instead.
        
        @param request: InvalidRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InvalidRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvalidRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.InvalidRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invalid_rule(
        self,
        request: qualitycheck_20190115_models.InvalidRuleRequest,
    ) -> qualitycheck_20190115_models.InvalidRuleResponse:
        """
        @deprecated OpenAPI InvalidRule is deprecated, please use Qualitycheck::2019-01-15::DeleteRuleV4 instead.
        
        @param request: InvalidRuleRequest
        @return: InvalidRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.invalid_rule_with_options(request, runtime)

    async def invalid_rule_async(
        self,
        request: qualitycheck_20190115_models.InvalidRuleRequest,
    ) -> qualitycheck_20190115_models.InvalidRuleResponse:
        """
        @deprecated OpenAPI InvalidRule is deprecated, please use Qualitycheck::2019-01-15::DeleteRuleV4 instead.
        
        @param request: InvalidRuleRequest
        @return: InvalidRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.invalid_rule_with_options_async(request, runtime)

    def list_asr_vocab_with_options(
        self,
        request: qualitycheck_20190115_models.ListAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListAsrVocabResponse:
        """
        @summary 获取热词模型列表
        
        @param request: ListAsrVocabRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAsrVocabResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAsrVocab',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListAsrVocabResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_asr_vocab_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListAsrVocabResponse:
        """
        @summary 获取热词模型列表
        
        @param request: ListAsrVocabRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAsrVocabResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAsrVocab',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListAsrVocabResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_asr_vocab(
        self,
        request: qualitycheck_20190115_models.ListAsrVocabRequest,
    ) -> qualitycheck_20190115_models.ListAsrVocabResponse:
        """
        @summary 获取热词模型列表
        
        @param request: ListAsrVocabRequest
        @return: ListAsrVocabResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_asr_vocab_with_options(request, runtime)

    async def list_asr_vocab_async(
        self,
        request: qualitycheck_20190115_models.ListAsrVocabRequest,
    ) -> qualitycheck_20190115_models.ListAsrVocabResponse:
        """
        @summary 获取热词模型列表
        
        @param request: ListAsrVocabRequest
        @return: ListAsrVocabResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_asr_vocab_with_options_async(request, runtime)

    def list_data_set_with_options(
        self,
        request: qualitycheck_20190115_models.ListDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListDataSetResponse:
        """
        @deprecated OpenAPI ListDataSet is deprecated
        
        @summary 获取数据集列表
        
        @param request: ListDataSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSetResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSet',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_set_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListDataSetResponse:
        """
        @deprecated OpenAPI ListDataSet is deprecated
        
        @summary 获取数据集列表
        
        @param request: ListDataSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDataSetResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSet',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_set(
        self,
        request: qualitycheck_20190115_models.ListDataSetRequest,
    ) -> qualitycheck_20190115_models.ListDataSetResponse:
        """
        @deprecated OpenAPI ListDataSet is deprecated
        
        @summary 获取数据集列表
        
        @param request: ListDataSetRequest
        @return: ListDataSetResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_data_set_with_options(request, runtime)

    async def list_data_set_async(
        self,
        request: qualitycheck_20190115_models.ListDataSetRequest,
    ) -> qualitycheck_20190115_models.ListDataSetResponse:
        """
        @deprecated OpenAPI ListDataSet is deprecated
        
        @summary 获取数据集列表
        
        @param request: ListDataSetRequest
        @return: ListDataSetResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_data_set_with_options_async(request, runtime)

    def list_precision_task_with_options(
        self,
        request: qualitycheck_20190115_models.ListPrecisionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListPrecisionTaskResponse:
        """
        @param request: ListPrecisionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrecisionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrecisionTask',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListPrecisionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_precision_task_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListPrecisionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListPrecisionTaskResponse:
        """
        @param request: ListPrecisionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPrecisionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrecisionTask',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListPrecisionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_precision_task(
        self,
        request: qualitycheck_20190115_models.ListPrecisionTaskRequest,
    ) -> qualitycheck_20190115_models.ListPrecisionTaskResponse:
        """
        @param request: ListPrecisionTaskRequest
        @return: ListPrecisionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_precision_task_with_options(request, runtime)

    async def list_precision_task_async(
        self,
        request: qualitycheck_20190115_models.ListPrecisionTaskRequest,
    ) -> qualitycheck_20190115_models.ListPrecisionTaskResponse:
        """
        @param request: ListPrecisionTaskRequest
        @return: ListPrecisionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_precision_task_with_options_async(request, runtime)

    def list_quality_check_scheme_with_options(
        self,
        request: qualitycheck_20190115_models.ListQualityCheckSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListQualityCheckSchemeResponse:
        """
        @summary 质检方案列表
        
        @param request: ListQualityCheckSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQualityCheckSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQualityCheckScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListQualityCheckSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quality_check_scheme_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListQualityCheckSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListQualityCheckSchemeResponse:
        """
        @summary 质检方案列表
        
        @param request: ListQualityCheckSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListQualityCheckSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListQualityCheckScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListQualityCheckSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quality_check_scheme(
        self,
        request: qualitycheck_20190115_models.ListQualityCheckSchemeRequest,
    ) -> qualitycheck_20190115_models.ListQualityCheckSchemeResponse:
        """
        @summary 质检方案列表
        
        @param request: ListQualityCheckSchemeRequest
        @return: ListQualityCheckSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_quality_check_scheme_with_options(request, runtime)

    async def list_quality_check_scheme_async(
        self,
        request: qualitycheck_20190115_models.ListQualityCheckSchemeRequest,
    ) -> qualitycheck_20190115_models.ListQualityCheckSchemeResponse:
        """
        @summary 质检方案列表
        
        @param request: ListQualityCheckSchemeRequest
        @return: ListQualityCheckSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_quality_check_scheme_with_options_async(request, runtime)

    def list_rules_with_options(
        self,
        request: qualitycheck_20190115_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListRulesResponse:
        """
        @deprecated OpenAPI ListRules is deprecated, please use Qualitycheck::2019-01-15::ListRulesV4 instead.
        
        @param request: ListRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRulesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rules_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListRulesResponse:
        """
        @deprecated OpenAPI ListRules is deprecated, please use Qualitycheck::2019-01-15::ListRulesV4 instead.
        
        @param request: ListRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRulesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRules',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rules(
        self,
        request: qualitycheck_20190115_models.ListRulesRequest,
    ) -> qualitycheck_20190115_models.ListRulesResponse:
        """
        @deprecated OpenAPI ListRules is deprecated, please use Qualitycheck::2019-01-15::ListRulesV4 instead.
        
        @param request: ListRulesRequest
        @return: ListRulesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    async def list_rules_async(
        self,
        request: qualitycheck_20190115_models.ListRulesRequest,
    ) -> qualitycheck_20190115_models.ListRulesResponse:
        """
        @deprecated OpenAPI ListRules is deprecated, please use Qualitycheck::2019-01-15::ListRulesV4 instead.
        
        @param request: ListRulesRequest
        @return: ListRulesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_rules_with_options_async(request, runtime)

    def list_rules_v4with_options(
        self,
        request: qualitycheck_20190115_models.ListRulesV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListRulesV4Response:
        """
        @summary V4获得规则列表
        
        @param request: ListRulesV4Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRulesV4Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not UtilClient.is_unset(request.business_name):
            body['BusinessName'] = request.business_name
        if not UtilClient.is_unset(request.business_range):
            body['BusinessRange'] = request.business_range
        if not UtilClient.is_unset(request.category_name):
            body['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.count_total):
            body['CountTotal'] = request.count_total
        if not UtilClient.is_unset(request.create_empid):
            body['CreateEmpid'] = request.create_empid
        if not UtilClient.is_unset(request.create_user_id):
            body['CreateUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.last_update_empid):
            body['LastUpdateEmpid'] = request.last_update_empid
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.require_infos):
            body['RequireInfos'] = request.require_infos
        if not UtilClient.is_unset(request.rid):
            body['Rid'] = request.rid
        if not UtilClient.is_unset(request.rule_id_or_rule_name):
            body['RuleIdOrRuleName'] = request.rule_id_or_rule_name
        if not UtilClient.is_unset(request.rule_score_single_type):
            body['RuleScoreSingleType'] = request.rule_score_single_type
        if not UtilClient.is_unset(request.rule_type):
            body['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.scheme_id):
            body['SchemeId'] = request.scheme_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.type_name):
            body['TypeName'] = request.type_name
        if not UtilClient.is_unset(request.update_end_time):
            body['UpdateEndTime'] = request.update_end_time
        if not UtilClient.is_unset(request.update_start_time):
            body['UpdateStartTime'] = request.update_start_time
        if not UtilClient.is_unset(request.update_user_id):
            body['UpdateUserId'] = request.update_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRulesV4',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListRulesV4Response(),
            self.call_api(params, req, runtime)
        )

    async def list_rules_v4with_options_async(
        self,
        request: qualitycheck_20190115_models.ListRulesV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListRulesV4Response:
        """
        @summary V4获得规则列表
        
        @param request: ListRulesV4Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRulesV4Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not UtilClient.is_unset(request.business_name):
            body['BusinessName'] = request.business_name
        if not UtilClient.is_unset(request.business_range):
            body['BusinessRange'] = request.business_range
        if not UtilClient.is_unset(request.category_name):
            body['CategoryName'] = request.category_name
        if not UtilClient.is_unset(request.count_total):
            body['CountTotal'] = request.count_total
        if not UtilClient.is_unset(request.create_empid):
            body['CreateEmpid'] = request.create_empid
        if not UtilClient.is_unset(request.create_user_id):
            body['CreateUserId'] = request.create_user_id
        if not UtilClient.is_unset(request.current_page):
            body['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.last_update_empid):
            body['LastUpdateEmpid'] = request.last_update_empid
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.require_infos):
            body['RequireInfos'] = request.require_infos
        if not UtilClient.is_unset(request.rid):
            body['Rid'] = request.rid
        if not UtilClient.is_unset(request.rule_id_or_rule_name):
            body['RuleIdOrRuleName'] = request.rule_id_or_rule_name
        if not UtilClient.is_unset(request.rule_score_single_type):
            body['RuleScoreSingleType'] = request.rule_score_single_type
        if not UtilClient.is_unset(request.rule_type):
            body['RuleType'] = request.rule_type
        if not UtilClient.is_unset(request.scheme_id):
            body['SchemeId'] = request.scheme_id
        if not UtilClient.is_unset(request.source_type):
            body['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.type_name):
            body['TypeName'] = request.type_name
        if not UtilClient.is_unset(request.update_end_time):
            body['UpdateEndTime'] = request.update_end_time
        if not UtilClient.is_unset(request.update_start_time):
            body['UpdateStartTime'] = request.update_start_time
        if not UtilClient.is_unset(request.update_user_id):
            body['UpdateUserId'] = request.update_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRulesV4',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListRulesV4Response(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rules_v4(
        self,
        request: qualitycheck_20190115_models.ListRulesV4Request,
    ) -> qualitycheck_20190115_models.ListRulesV4Response:
        """
        @summary V4获得规则列表
        
        @param request: ListRulesV4Request
        @return: ListRulesV4Response
        """
        runtime = util_models.RuntimeOptions()
        return self.list_rules_v4with_options(request, runtime)

    async def list_rules_v4_async(
        self,
        request: qualitycheck_20190115_models.ListRulesV4Request,
    ) -> qualitycheck_20190115_models.ListRulesV4Response:
        """
        @summary V4获得规则列表
        
        @param request: ListRulesV4Request
        @return: ListRulesV4Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_rules_v4with_options_async(request, runtime)

    def list_scheme_task_config_with_options(
        self,
        request: qualitycheck_20190115_models.ListSchemeTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListSchemeTaskConfigResponse:
        """
        @summary 获取质检任务列表
        
        @param request: ListSchemeTaskConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSchemeTaskConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchemeTaskConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListSchemeTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scheme_task_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListSchemeTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListSchemeTaskConfigResponse:
        """
        @summary 获取质检任务列表
        
        @param request: ListSchemeTaskConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSchemeTaskConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSchemeTaskConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListSchemeTaskConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scheme_task_config(
        self,
        request: qualitycheck_20190115_models.ListSchemeTaskConfigRequest,
    ) -> qualitycheck_20190115_models.ListSchemeTaskConfigResponse:
        """
        @summary 获取质检任务列表
        
        @param request: ListSchemeTaskConfigRequest
        @return: ListSchemeTaskConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_scheme_task_config_with_options(request, runtime)

    async def list_scheme_task_config_async(
        self,
        request: qualitycheck_20190115_models.ListSchemeTaskConfigRequest,
    ) -> qualitycheck_20190115_models.ListSchemeTaskConfigResponse:
        """
        @summary 获取质检任务列表
        
        @param request: ListSchemeTaskConfigRequest
        @return: ListSchemeTaskConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_scheme_task_config_with_options_async(request, runtime)

    def list_session_group_with_options(
        self,
        request: qualitycheck_20190115_models.ListSessionGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListSessionGroupResponse:
        """
        @deprecated OpenAPI ListSessionGroup is deprecated
        
        @summary 获取会话组列表
        
        @param request: ListSessionGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSessionGroupResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSessionGroup',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListSessionGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_session_group_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListSessionGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListSessionGroupResponse:
        """
        @deprecated OpenAPI ListSessionGroup is deprecated
        
        @summary 获取会话组列表
        
        @param request: ListSessionGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSessionGroupResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSessionGroup',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListSessionGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_session_group(
        self,
        request: qualitycheck_20190115_models.ListSessionGroupRequest,
    ) -> qualitycheck_20190115_models.ListSessionGroupResponse:
        """
        @deprecated OpenAPI ListSessionGroup is deprecated
        
        @summary 获取会话组列表
        
        @param request: ListSessionGroupRequest
        @return: ListSessionGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_session_group_with_options(request, runtime)

    async def list_session_group_async(
        self,
        request: qualitycheck_20190115_models.ListSessionGroupRequest,
    ) -> qualitycheck_20190115_models.ListSessionGroupResponse:
        """
        @deprecated OpenAPI ListSessionGroup is deprecated
        
        @summary 获取会话组列表
        
        @param request: ListSessionGroupRequest
        @return: ListSessionGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_session_group_with_options_async(request, runtime)

    def list_skill_group_config_with_options(
        self,
        request: qualitycheck_20190115_models.ListSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListSkillGroupConfigResponse:
        """
        @param request: ListSkillGroupConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSkillGroupConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSkillGroupConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListSkillGroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skill_group_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListSkillGroupConfigResponse:
        """
        @param request: ListSkillGroupConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSkillGroupConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSkillGroupConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListSkillGroupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skill_group_config(
        self,
        request: qualitycheck_20190115_models.ListSkillGroupConfigRequest,
    ) -> qualitycheck_20190115_models.ListSkillGroupConfigResponse:
        """
        @param request: ListSkillGroupConfigRequest
        @return: ListSkillGroupConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_config_with_options(request, runtime)

    async def list_skill_group_config_async(
        self,
        request: qualitycheck_20190115_models.ListSkillGroupConfigRequest,
    ) -> qualitycheck_20190115_models.ListSkillGroupConfigResponse:
        """
        @param request: ListSkillGroupConfigRequest
        @return: ListSkillGroupConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_group_config_with_options_async(request, runtime)

    def list_task_assign_rules_with_options(
        self,
        request: qualitycheck_20190115_models.ListTaskAssignRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListTaskAssignRulesResponse:
        """
        @param request: ListTaskAssignRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskAssignRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskAssignRules',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListTaskAssignRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_assign_rules_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListTaskAssignRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListTaskAssignRulesResponse:
        """
        @param request: ListTaskAssignRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskAssignRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskAssignRules',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListTaskAssignRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_assign_rules(
        self,
        request: qualitycheck_20190115_models.ListTaskAssignRulesRequest,
    ) -> qualitycheck_20190115_models.ListTaskAssignRulesResponse:
        """
        @param request: ListTaskAssignRulesRequest
        @return: ListTaskAssignRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_task_assign_rules_with_options(request, runtime)

    async def list_task_assign_rules_async(
        self,
        request: qualitycheck_20190115_models.ListTaskAssignRulesRequest,
    ) -> qualitycheck_20190115_models.ListTaskAssignRulesResponse:
        """
        @param request: ListTaskAssignRulesRequest
        @return: ListTaskAssignRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_task_assign_rules_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: qualitycheck_20190115_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListUsersResponse:
        """
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListUsersResponse:
        """
        @param request: ListUsersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: qualitycheck_20190115_models.ListUsersRequest,
    ) -> qualitycheck_20190115_models.ListUsersResponse:
        """
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: qualitycheck_20190115_models.ListUsersRequest,
    ) -> qualitycheck_20190115_models.ListUsersResponse:
        """
        @param request: ListUsersRequest
        @return: ListUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_warning_config_with_options(
        self,
        request: qualitycheck_20190115_models.ListWarningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListWarningConfigResponse:
        """
        @param request: ListWarningConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWarningConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWarningConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListWarningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_warning_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListWarningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListWarningConfigResponse:
        """
        @param request: ListWarningConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWarningConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWarningConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListWarningConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_warning_config(
        self,
        request: qualitycheck_20190115_models.ListWarningConfigRequest,
    ) -> qualitycheck_20190115_models.ListWarningConfigResponse:
        """
        @param request: ListWarningConfigRequest
        @return: ListWarningConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_warning_config_with_options(request, runtime)

    async def list_warning_config_async(
        self,
        request: qualitycheck_20190115_models.ListWarningConfigRequest,
    ) -> qualitycheck_20190115_models.ListWarningConfigResponse:
        """
        @param request: ListWarningConfigRequest
        @return: ListWarningConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_warning_config_with_options_async(request, runtime)

    def list_warning_strategy_config_with_options(
        self,
        request: qualitycheck_20190115_models.ListWarningStrategyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListWarningStrategyConfigResponse:
        """
        @summary  预警策略-列表
        
        @param request: ListWarningStrategyConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWarningStrategyConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWarningStrategyConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListWarningStrategyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_warning_strategy_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListWarningStrategyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListWarningStrategyConfigResponse:
        """
        @summary  预警策略-列表
        
        @param request: ListWarningStrategyConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWarningStrategyConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWarningStrategyConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.ListWarningStrategyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_warning_strategy_config(
        self,
        request: qualitycheck_20190115_models.ListWarningStrategyConfigRequest,
    ) -> qualitycheck_20190115_models.ListWarningStrategyConfigResponse:
        """
        @summary  预警策略-列表
        
        @param request: ListWarningStrategyConfigRequest
        @return: ListWarningStrategyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_warning_strategy_config_with_options(request, runtime)

    async def list_warning_strategy_config_async(
        self,
        request: qualitycheck_20190115_models.ListWarningStrategyConfigRequest,
    ) -> qualitycheck_20190115_models.ListWarningStrategyConfigResponse:
        """
        @summary  预警策略-列表
        
        @param request: ListWarningStrategyConfigRequest
        @return: ListWarningStrategyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_warning_strategy_config_with_options_async(request, runtime)

    def revert_assigned_session_with_options(
        self,
        request: qualitycheck_20190115_models.RevertAssignedSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.RevertAssignedSessionResponse:
        """
        @summary 批量回收
        
        @param request: RevertAssignedSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevertAssignedSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevertAssignedSession',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.RevertAssignedSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def revert_assigned_session_with_options_async(
        self,
        request: qualitycheck_20190115_models.RevertAssignedSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.RevertAssignedSessionResponse:
        """
        @summary 批量回收
        
        @param request: RevertAssignedSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevertAssignedSessionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevertAssignedSession',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.RevertAssignedSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revert_assigned_session(
        self,
        request: qualitycheck_20190115_models.RevertAssignedSessionRequest,
    ) -> qualitycheck_20190115_models.RevertAssignedSessionResponse:
        """
        @summary 批量回收
        
        @param request: RevertAssignedSessionRequest
        @return: RevertAssignedSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.revert_assigned_session_with_options(request, runtime)

    async def revert_assigned_session_async(
        self,
        request: qualitycheck_20190115_models.RevertAssignedSessionRequest,
    ) -> qualitycheck_20190115_models.RevertAssignedSessionResponse:
        """
        @summary 批量回收
        
        @param request: RevertAssignedSessionRequest
        @return: RevertAssignedSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.revert_assigned_session_with_options_async(request, runtime)

    def revert_assigned_session_group_with_options(
        self,
        request: qualitycheck_20190115_models.RevertAssignedSessionGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.RevertAssignedSessionGroupResponse:
        """
        @deprecated OpenAPI RevertAssignedSessionGroup is deprecated
        
        @summary 会话组批量回收
        
        @param request: RevertAssignedSessionGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevertAssignedSessionGroupResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevertAssignedSessionGroup',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.RevertAssignedSessionGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def revert_assigned_session_group_with_options_async(
        self,
        request: qualitycheck_20190115_models.RevertAssignedSessionGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.RevertAssignedSessionGroupResponse:
        """
        @deprecated OpenAPI RevertAssignedSessionGroup is deprecated
        
        @summary 会话组批量回收
        
        @param request: RevertAssignedSessionGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RevertAssignedSessionGroupResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RevertAssignedSessionGroup',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.RevertAssignedSessionGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revert_assigned_session_group(
        self,
        request: qualitycheck_20190115_models.RevertAssignedSessionGroupRequest,
    ) -> qualitycheck_20190115_models.RevertAssignedSessionGroupResponse:
        """
        @deprecated OpenAPI RevertAssignedSessionGroup is deprecated
        
        @summary 会话组批量回收
        
        @param request: RevertAssignedSessionGroupRequest
        @return: RevertAssignedSessionGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.revert_assigned_session_group_with_options(request, runtime)

    async def revert_assigned_session_group_async(
        self,
        request: qualitycheck_20190115_models.RevertAssignedSessionGroupRequest,
    ) -> qualitycheck_20190115_models.RevertAssignedSessionGroupResponse:
        """
        @deprecated OpenAPI RevertAssignedSessionGroup is deprecated
        
        @summary 会话组批量回收
        
        @param request: RevertAssignedSessionGroupRequest
        @return: RevertAssignedSessionGroupResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.revert_assigned_session_group_with_options_async(request, runtime)

    def save_config_data_set_with_options(
        self,
        request: qualitycheck_20190115_models.SaveConfigDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SaveConfigDataSetResponse:
        """
        @deprecated OpenAPI SaveConfigDataSet is deprecated
        
        @param request: SaveConfigDataSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveConfigDataSetResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveConfigDataSet',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SaveConfigDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_config_data_set_with_options_async(
        self,
        request: qualitycheck_20190115_models.SaveConfigDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SaveConfigDataSetResponse:
        """
        @deprecated OpenAPI SaveConfigDataSet is deprecated
        
        @param request: SaveConfigDataSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SaveConfigDataSetResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveConfigDataSet',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SaveConfigDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_config_data_set(
        self,
        request: qualitycheck_20190115_models.SaveConfigDataSetRequest,
    ) -> qualitycheck_20190115_models.SaveConfigDataSetResponse:
        """
        @deprecated OpenAPI SaveConfigDataSet is deprecated
        
        @param request: SaveConfigDataSetRequest
        @return: SaveConfigDataSetResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.save_config_data_set_with_options(request, runtime)

    async def save_config_data_set_async(
        self,
        request: qualitycheck_20190115_models.SaveConfigDataSetRequest,
    ) -> qualitycheck_20190115_models.SaveConfigDataSetResponse:
        """
        @deprecated OpenAPI SaveConfigDataSet is deprecated
        
        @param request: SaveConfigDataSetRequest
        @return: SaveConfigDataSetResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.save_config_data_set_with_options_async(request, runtime)

    def submit_complaint_with_options(
        self,
        request: qualitycheck_20190115_models.SubmitComplaintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitComplaintResponse:
        """
        @param request: SubmitComplaintRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitComplaintResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitComplaint',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SubmitComplaintResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_complaint_with_options_async(
        self,
        request: qualitycheck_20190115_models.SubmitComplaintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitComplaintResponse:
        """
        @param request: SubmitComplaintRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitComplaintResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitComplaint',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SubmitComplaintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_complaint(
        self,
        request: qualitycheck_20190115_models.SubmitComplaintRequest,
    ) -> qualitycheck_20190115_models.SubmitComplaintResponse:
        """
        @param request: SubmitComplaintRequest
        @return: SubmitComplaintResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_complaint_with_options(request, runtime)

    async def submit_complaint_async(
        self,
        request: qualitycheck_20190115_models.SubmitComplaintRequest,
    ) -> qualitycheck_20190115_models.SubmitComplaintResponse:
        """
        @param request: SubmitComplaintRequest
        @return: SubmitComplaintResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_complaint_with_options_async(request, runtime)

    def submit_precision_task_with_options(
        self,
        request: qualitycheck_20190115_models.SubmitPrecisionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitPrecisionTaskResponse:
        """
        @param request: SubmitPrecisionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitPrecisionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitPrecisionTask',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SubmitPrecisionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_precision_task_with_options_async(
        self,
        request: qualitycheck_20190115_models.SubmitPrecisionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitPrecisionTaskResponse:
        """
        @param request: SubmitPrecisionTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitPrecisionTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitPrecisionTask',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SubmitPrecisionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_precision_task(
        self,
        request: qualitycheck_20190115_models.SubmitPrecisionTaskRequest,
    ) -> qualitycheck_20190115_models.SubmitPrecisionTaskResponse:
        """
        @param request: SubmitPrecisionTaskRequest
        @return: SubmitPrecisionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_precision_task_with_options(request, runtime)

    async def submit_precision_task_async(
        self,
        request: qualitycheck_20190115_models.SubmitPrecisionTaskRequest,
    ) -> qualitycheck_20190115_models.SubmitPrecisionTaskResponse:
        """
        @param request: SubmitPrecisionTaskRequest
        @return: SubmitPrecisionTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_precision_task_with_options_async(request, runtime)

    def submit_quality_check_task_with_options(
        self,
        request: qualitycheck_20190115_models.SubmitQualityCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitQualityCheckTaskResponse:
        """
        @param request: SubmitQualityCheckTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitQualityCheckTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitQualityCheckTask',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SubmitQualityCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_quality_check_task_with_options_async(
        self,
        request: qualitycheck_20190115_models.SubmitQualityCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitQualityCheckTaskResponse:
        """
        @param request: SubmitQualityCheckTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitQualityCheckTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitQualityCheckTask',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SubmitQualityCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_quality_check_task(
        self,
        request: qualitycheck_20190115_models.SubmitQualityCheckTaskRequest,
    ) -> qualitycheck_20190115_models.SubmitQualityCheckTaskResponse:
        """
        @param request: SubmitQualityCheckTaskRequest
        @return: SubmitQualityCheckTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_quality_check_task_with_options(request, runtime)

    async def submit_quality_check_task_async(
        self,
        request: qualitycheck_20190115_models.SubmitQualityCheckTaskRequest,
    ) -> qualitycheck_20190115_models.SubmitQualityCheckTaskResponse:
        """
        @param request: SubmitQualityCheckTaskRequest
        @return: SubmitQualityCheckTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_quality_check_task_with_options_async(request, runtime)

    def submit_review_info_with_options(
        self,
        request: qualitycheck_20190115_models.SubmitReviewInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitReviewInfoResponse:
        """
        @param request: SubmitReviewInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitReviewInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitReviewInfo',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SubmitReviewInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_review_info_with_options_async(
        self,
        request: qualitycheck_20190115_models.SubmitReviewInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitReviewInfoResponse:
        """
        @param request: SubmitReviewInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SubmitReviewInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitReviewInfo',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SubmitReviewInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_review_info(
        self,
        request: qualitycheck_20190115_models.SubmitReviewInfoRequest,
    ) -> qualitycheck_20190115_models.SubmitReviewInfoResponse:
        """
        @param request: SubmitReviewInfoRequest
        @return: SubmitReviewInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_review_info_with_options(request, runtime)

    async def submit_review_info_async(
        self,
        request: qualitycheck_20190115_models.SubmitReviewInfoRequest,
    ) -> qualitycheck_20190115_models.SubmitReviewInfoResponse:
        """
        @param request: SubmitReviewInfoRequest
        @return: SubmitReviewInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.submit_review_info_with_options_async(request, runtime)

    def sync_quality_check_with_options(
        self,
        request: qualitycheck_20190115_models.SyncQualityCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SyncQualityCheckResponse:
        """
        @param request: SyncQualityCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncQualityCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncQualityCheck',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SyncQualityCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_quality_check_with_options_async(
        self,
        request: qualitycheck_20190115_models.SyncQualityCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SyncQualityCheckResponse:
        """
        @param request: SyncQualityCheckRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SyncQualityCheckResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncQualityCheck',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.SyncQualityCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_quality_check(
        self,
        request: qualitycheck_20190115_models.SyncQualityCheckRequest,
    ) -> qualitycheck_20190115_models.SyncQualityCheckResponse:
        """
        @param request: SyncQualityCheckRequest
        @return: SyncQualityCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.sync_quality_check_with_options(request, runtime)

    async def sync_quality_check_async(
        self,
        request: qualitycheck_20190115_models.SyncQualityCheckRequest,
    ) -> qualitycheck_20190115_models.SyncQualityCheckResponse:
        """
        @param request: SyncQualityCheckRequest
        @return: SyncQualityCheckResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.sync_quality_check_with_options_async(request, runtime)

    def test_rule_v4with_options(
        self,
        request: qualitycheck_20190115_models.TestRuleV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.TestRuleV4Response:
        """
        @summary 测试规则
        
        @param request: TestRuleV4Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: TestRuleV4Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_scheme_data):
            body['IsSchemeData'] = request.is_scheme_data
        if not UtilClient.is_unset(request.test_json):
            body['TestJson'] = request.test_json
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TestRuleV4',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.TestRuleV4Response(),
            self.call_api(params, req, runtime)
        )

    async def test_rule_v4with_options_async(
        self,
        request: qualitycheck_20190115_models.TestRuleV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.TestRuleV4Response:
        """
        @summary 测试规则
        
        @param request: TestRuleV4Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: TestRuleV4Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_scheme_data):
            body['IsSchemeData'] = request.is_scheme_data
        if not UtilClient.is_unset(request.test_json):
            body['TestJson'] = request.test_json
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TestRuleV4',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.TestRuleV4Response(),
            await self.call_api_async(params, req, runtime)
        )

    def test_rule_v4(
        self,
        request: qualitycheck_20190115_models.TestRuleV4Request,
    ) -> qualitycheck_20190115_models.TestRuleV4Response:
        """
        @summary 测试规则
        
        @param request: TestRuleV4Request
        @return: TestRuleV4Response
        """
        runtime = util_models.RuntimeOptions()
        return self.test_rule_v4with_options(request, runtime)

    async def test_rule_v4_async(
        self,
        request: qualitycheck_20190115_models.TestRuleV4Request,
    ) -> qualitycheck_20190115_models.TestRuleV4Response:
        """
        @summary 测试规则
        
        @param request: TestRuleV4Request
        @return: TestRuleV4Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.test_rule_v4with_options_async(request, runtime)

    def update_asr_vocab_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateAsrVocabResponse:
        """
        @param request: UpdateAsrVocabRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAsrVocabResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAsrVocab',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateAsrVocabResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_asr_vocab_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateAsrVocabResponse:
        """
        @param request: UpdateAsrVocabRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAsrVocabResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAsrVocab',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateAsrVocabResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_asr_vocab(
        self,
        request: qualitycheck_20190115_models.UpdateAsrVocabRequest,
    ) -> qualitycheck_20190115_models.UpdateAsrVocabResponse:
        """
        @param request: UpdateAsrVocabRequest
        @return: UpdateAsrVocabResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_asr_vocab_with_options(request, runtime)

    async def update_asr_vocab_async(
        self,
        request: qualitycheck_20190115_models.UpdateAsrVocabRequest,
    ) -> qualitycheck_20190115_models.UpdateAsrVocabResponse:
        """
        @param request: UpdateAsrVocabRequest
        @return: UpdateAsrVocabResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_asr_vocab_with_options_async(request, runtime)

    def update_check_type_to_scheme_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateCheckTypeToSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateCheckTypeToSchemeResponse:
        """
        @summary 更新质检方案中的质检维度
        
        @param request: UpdateCheckTypeToSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCheckTypeToSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCheckTypeToScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateCheckTypeToSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_check_type_to_scheme_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateCheckTypeToSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateCheckTypeToSchemeResponse:
        """
        @summary 更新质检方案中的质检维度
        
        @param request: UpdateCheckTypeToSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateCheckTypeToSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCheckTypeToScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateCheckTypeToSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_check_type_to_scheme(
        self,
        request: qualitycheck_20190115_models.UpdateCheckTypeToSchemeRequest,
    ) -> qualitycheck_20190115_models.UpdateCheckTypeToSchemeResponse:
        """
        @summary 更新质检方案中的质检维度
        
        @param request: UpdateCheckTypeToSchemeRequest
        @return: UpdateCheckTypeToSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_check_type_to_scheme_with_options(request, runtime)

    async def update_check_type_to_scheme_async(
        self,
        request: qualitycheck_20190115_models.UpdateCheckTypeToSchemeRequest,
    ) -> qualitycheck_20190115_models.UpdateCheckTypeToSchemeResponse:
        """
        @summary 更新质检方案中的质检维度
        
        @param request: UpdateCheckTypeToSchemeRequest
        @return: UpdateCheckTypeToSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_check_type_to_scheme_with_options_async(request, runtime)

    def update_quality_check_data_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateQualityCheckDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateQualityCheckDataResponse:
        """
        @summary 更新会话随录数据
        
        @param request: UpdateQualityCheckDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQualityCheckDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateQualityCheckData',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateQualityCheckDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quality_check_data_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateQualityCheckDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateQualityCheckDataResponse:
        """
        @summary 更新会话随录数据
        
        @param request: UpdateQualityCheckDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQualityCheckDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateQualityCheckData',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateQualityCheckDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quality_check_data(
        self,
        request: qualitycheck_20190115_models.UpdateQualityCheckDataRequest,
    ) -> qualitycheck_20190115_models.UpdateQualityCheckDataResponse:
        """
        @summary 更新会话随录数据
        
        @param request: UpdateQualityCheckDataRequest
        @return: UpdateQualityCheckDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_quality_check_data_with_options(request, runtime)

    async def update_quality_check_data_async(
        self,
        request: qualitycheck_20190115_models.UpdateQualityCheckDataRequest,
    ) -> qualitycheck_20190115_models.UpdateQualityCheckDataResponse:
        """
        @summary 更新会话随录数据
        
        @param request: UpdateQualityCheckDataRequest
        @return: UpdateQualityCheckDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_quality_check_data_with_options_async(request, runtime)

    def update_quality_check_scheme_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateQualityCheckSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateQualityCheckSchemeResponse:
        """
        @summary 更新质检方案
        
        @param request: UpdateQualityCheckSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQualityCheckSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateQualityCheckScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateQualityCheckSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quality_check_scheme_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateQualityCheckSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateQualityCheckSchemeResponse:
        """
        @summary 更新质检方案
        
        @param request: UpdateQualityCheckSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateQualityCheckSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateQualityCheckScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateQualityCheckSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quality_check_scheme(
        self,
        request: qualitycheck_20190115_models.UpdateQualityCheckSchemeRequest,
    ) -> qualitycheck_20190115_models.UpdateQualityCheckSchemeResponse:
        """
        @summary 更新质检方案
        
        @param request: UpdateQualityCheckSchemeRequest
        @return: UpdateQualityCheckSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_quality_check_scheme_with_options(request, runtime)

    async def update_quality_check_scheme_async(
        self,
        request: qualitycheck_20190115_models.UpdateQualityCheckSchemeRequest,
    ) -> qualitycheck_20190115_models.UpdateQualityCheckSchemeResponse:
        """
        @summary 更新质检方案
        
        @param request: UpdateQualityCheckSchemeRequest
        @return: UpdateQualityCheckSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_quality_check_scheme_with_options_async(request, runtime)

    def update_rule_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateRuleResponse:
        """
        @deprecated OpenAPI UpdateRule is deprecated, please use Qualitycheck::2019-01-15::UpdateRuleV4 instead.
        
        @param request: UpdateRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rule_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateRuleResponse:
        """
        @deprecated OpenAPI UpdateRule is deprecated, please use Qualitycheck::2019-01-15::UpdateRuleV4 instead.
        
        @param request: UpdateRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRuleResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rule(
        self,
        request: qualitycheck_20190115_models.UpdateRuleRequest,
    ) -> qualitycheck_20190115_models.UpdateRuleResponse:
        """
        @deprecated OpenAPI UpdateRule is deprecated, please use Qualitycheck::2019-01-15::UpdateRuleV4 instead.
        
        @param request: UpdateRuleRequest
        @return: UpdateRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.update_rule_with_options(request, runtime)

    async def update_rule_async(
        self,
        request: qualitycheck_20190115_models.UpdateRuleRequest,
    ) -> qualitycheck_20190115_models.UpdateRuleResponse:
        """
        @deprecated OpenAPI UpdateRule is deprecated, please use Qualitycheck::2019-01-15::UpdateRuleV4 instead.
        
        @param request: UpdateRuleRequest
        @return: UpdateRuleResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_rule_with_options_async(request, runtime)

    def update_rule_by_id_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateRuleByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateRuleByIdResponse:
        """
        @deprecated OpenAPI UpdateRuleById is deprecated, please use Qualitycheck::2019-01-15::UpdateRuleV4 instead.
        
        @summary 更新规则
        
        @param request: UpdateRuleByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRuleByIdResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not UtilClient.is_unset(request.is_copy):
            body['IsCopy'] = request.is_copy
        if not UtilClient.is_unset(request.json_str_for_rule):
            body['JsonStrForRule'] = request.json_str_for_rule
        if not UtilClient.is_unset(request.return_related_schemes):
            body['ReturnRelatedSchemes'] = request.return_related_schemes
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRuleById',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateRuleByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rule_by_id_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateRuleByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateRuleByIdResponse:
        """
        @deprecated OpenAPI UpdateRuleById is deprecated, please use Qualitycheck::2019-01-15::UpdateRuleV4 instead.
        
        @summary 更新规则
        
        @param request: UpdateRuleByIdRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRuleByIdResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not UtilClient.is_unset(request.is_copy):
            body['IsCopy'] = request.is_copy
        if not UtilClient.is_unset(request.json_str_for_rule):
            body['JsonStrForRule'] = request.json_str_for_rule
        if not UtilClient.is_unset(request.return_related_schemes):
            body['ReturnRelatedSchemes'] = request.return_related_schemes
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRuleById',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateRuleByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rule_by_id(
        self,
        request: qualitycheck_20190115_models.UpdateRuleByIdRequest,
    ) -> qualitycheck_20190115_models.UpdateRuleByIdResponse:
        """
        @deprecated OpenAPI UpdateRuleById is deprecated, please use Qualitycheck::2019-01-15::UpdateRuleV4 instead.
        
        @summary 更新规则
        
        @param request: UpdateRuleByIdRequest
        @return: UpdateRuleByIdResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.update_rule_by_id_with_options(request, runtime)

    async def update_rule_by_id_async(
        self,
        request: qualitycheck_20190115_models.UpdateRuleByIdRequest,
    ) -> qualitycheck_20190115_models.UpdateRuleByIdResponse:
        """
        @deprecated OpenAPI UpdateRuleById is deprecated, please use Qualitycheck::2019-01-15::UpdateRuleV4 instead.
        
        @summary 更新规则
        
        @param request: UpdateRuleByIdRequest
        @return: UpdateRuleByIdResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_rule_by_id_with_options_async(request, runtime)

    def update_rule_to_scheme_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateRuleToSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateRuleToSchemeResponse:
        """
        @summary 更新质检方案的规则
        
        @param request: UpdateRuleToSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRuleToSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRuleToScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateRuleToSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rule_to_scheme_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateRuleToSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateRuleToSchemeResponse:
        """
        @summary 更新质检方案的规则
        
        @param request: UpdateRuleToSchemeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRuleToSchemeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRuleToScheme',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateRuleToSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rule_to_scheme(
        self,
        request: qualitycheck_20190115_models.UpdateRuleToSchemeRequest,
    ) -> qualitycheck_20190115_models.UpdateRuleToSchemeResponse:
        """
        @summary 更新质检方案的规则
        
        @param request: UpdateRuleToSchemeRequest
        @return: UpdateRuleToSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_rule_to_scheme_with_options(request, runtime)

    async def update_rule_to_scheme_async(
        self,
        request: qualitycheck_20190115_models.UpdateRuleToSchemeRequest,
    ) -> qualitycheck_20190115_models.UpdateRuleToSchemeResponse:
        """
        @summary 更新质检方案的规则
        
        @param request: UpdateRuleToSchemeRequest
        @return: UpdateRuleToSchemeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_rule_to_scheme_with_options_async(request, runtime)

    def update_rule_v4with_options(
        self,
        request: qualitycheck_20190115_models.UpdateRuleV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateRuleV4Response:
        """
        @summary V4更新规则
        
        @param request: UpdateRuleV4Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRuleV4Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not UtilClient.is_unset(request.json_str_for_rule):
            body['JsonStrForRule'] = request.json_str_for_rule
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRuleV4',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateRuleV4Response(),
            self.call_api(params, req, runtime)
        )

    async def update_rule_v4with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateRuleV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateRuleV4Response:
        """
        @summary V4更新规则
        
        @param request: UpdateRuleV4Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRuleV4Response
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not UtilClient.is_unset(request.json_str_for_rule):
            body['JsonStrForRule'] = request.json_str_for_rule
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRuleV4',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateRuleV4Response(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rule_v4(
        self,
        request: qualitycheck_20190115_models.UpdateRuleV4Request,
    ) -> qualitycheck_20190115_models.UpdateRuleV4Response:
        """
        @summary V4更新规则
        
        @param request: UpdateRuleV4Request
        @return: UpdateRuleV4Response
        """
        runtime = util_models.RuntimeOptions()
        return self.update_rule_v4with_options(request, runtime)

    async def update_rule_v4_async(
        self,
        request: qualitycheck_20190115_models.UpdateRuleV4Request,
    ) -> qualitycheck_20190115_models.UpdateRuleV4Response:
        """
        @summary V4更新规则
        
        @param request: UpdateRuleV4Request
        @return: UpdateRuleV4Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_rule_v4with_options_async(request, runtime)

    def update_scheme_task_config_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateSchemeTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateSchemeTaskConfigResponse:
        """
        @summary 更新质检任务
        
        @param request: UpdateSchemeTaskConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSchemeTaskConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSchemeTaskConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateSchemeTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scheme_task_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateSchemeTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateSchemeTaskConfigResponse:
        """
        @summary 更新质检任务
        
        @param request: UpdateSchemeTaskConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSchemeTaskConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSchemeTaskConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateSchemeTaskConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scheme_task_config(
        self,
        request: qualitycheck_20190115_models.UpdateSchemeTaskConfigRequest,
    ) -> qualitycheck_20190115_models.UpdateSchemeTaskConfigResponse:
        """
        @summary 更新质检任务
        
        @param request: UpdateSchemeTaskConfigRequest
        @return: UpdateSchemeTaskConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_scheme_task_config_with_options(request, runtime)

    async def update_scheme_task_config_async(
        self,
        request: qualitycheck_20190115_models.UpdateSchemeTaskConfigRequest,
    ) -> qualitycheck_20190115_models.UpdateSchemeTaskConfigResponse:
        """
        @summary 更新质检任务
        
        @param request: UpdateSchemeTaskConfigRequest
        @return: UpdateSchemeTaskConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_scheme_task_config_with_options_async(request, runtime)

    def update_skill_group_config_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateSkillGroupConfigResponse:
        """
        @param request: UpdateSkillGroupConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSkillGroupConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSkillGroupConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateSkillGroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_skill_group_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateSkillGroupConfigResponse:
        """
        @param request: UpdateSkillGroupConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSkillGroupConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSkillGroupConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateSkillGroupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_skill_group_config(
        self,
        request: qualitycheck_20190115_models.UpdateSkillGroupConfigRequest,
    ) -> qualitycheck_20190115_models.UpdateSkillGroupConfigResponse:
        """
        @param request: UpdateSkillGroupConfigRequest
        @return: UpdateSkillGroupConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_skill_group_config_with_options(request, runtime)

    async def update_skill_group_config_async(
        self,
        request: qualitycheck_20190115_models.UpdateSkillGroupConfigRequest,
    ) -> qualitycheck_20190115_models.UpdateSkillGroupConfigResponse:
        """
        @param request: UpdateSkillGroupConfigRequest
        @return: UpdateSkillGroupConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_skill_group_config_with_options_async(request, runtime)

    def update_sync_quality_check_data_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateSyncQualityCheckDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateSyncQualityCheckDataResponse:
        """
        @param request: UpdateSyncQualityCheckDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSyncQualityCheckDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSyncQualityCheckData',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateSyncQualityCheckDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sync_quality_check_data_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateSyncQualityCheckDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateSyncQualityCheckDataResponse:
        """
        @param request: UpdateSyncQualityCheckDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSyncQualityCheckDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSyncQualityCheckData',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateSyncQualityCheckDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sync_quality_check_data(
        self,
        request: qualitycheck_20190115_models.UpdateSyncQualityCheckDataRequest,
    ) -> qualitycheck_20190115_models.UpdateSyncQualityCheckDataResponse:
        """
        @param request: UpdateSyncQualityCheckDataRequest
        @return: UpdateSyncQualityCheckDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_sync_quality_check_data_with_options(request, runtime)

    async def update_sync_quality_check_data_async(
        self,
        request: qualitycheck_20190115_models.UpdateSyncQualityCheckDataRequest,
    ) -> qualitycheck_20190115_models.UpdateSyncQualityCheckDataResponse:
        """
        @param request: UpdateSyncQualityCheckDataRequest
        @return: UpdateSyncQualityCheckDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_sync_quality_check_data_with_options_async(request, runtime)

    def update_task_assign_rule_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateTaskAssignRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateTaskAssignRuleResponse:
        """
        @param request: UpdateTaskAssignRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTaskAssignRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTaskAssignRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateTaskAssignRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_task_assign_rule_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateTaskAssignRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateTaskAssignRuleResponse:
        """
        @param request: UpdateTaskAssignRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTaskAssignRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTaskAssignRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateTaskAssignRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_task_assign_rule(
        self,
        request: qualitycheck_20190115_models.UpdateTaskAssignRuleRequest,
    ) -> qualitycheck_20190115_models.UpdateTaskAssignRuleResponse:
        """
        @param request: UpdateTaskAssignRuleRequest
        @return: UpdateTaskAssignRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_task_assign_rule_with_options(request, runtime)

    async def update_task_assign_rule_async(
        self,
        request: qualitycheck_20190115_models.UpdateTaskAssignRuleRequest,
    ) -> qualitycheck_20190115_models.UpdateTaskAssignRuleResponse:
        """
        @param request: UpdateTaskAssignRuleRequest
        @return: UpdateTaskAssignRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_task_assign_rule_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateUserResponse:
        """
        @param request: UpdateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateUserResponse:
        """
        @param request: UpdateUserRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: qualitycheck_20190115_models.UpdateUserRequest,
    ) -> qualitycheck_20190115_models.UpdateUserResponse:
        """
        @param request: UpdateUserRequest
        @return: UpdateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: qualitycheck_20190115_models.UpdateUserRequest,
    ) -> qualitycheck_20190115_models.UpdateUserResponse:
        """
        @param request: UpdateUserRequest
        @return: UpdateUserResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)

    def update_warning_config_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateWarningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateWarningConfigResponse:
        """
        @param request: UpdateWarningConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWarningConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWarningConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateWarningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_warning_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateWarningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateWarningConfigResponse:
        """
        @param request: UpdateWarningConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWarningConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWarningConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateWarningConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_warning_config(
        self,
        request: qualitycheck_20190115_models.UpdateWarningConfigRequest,
    ) -> qualitycheck_20190115_models.UpdateWarningConfigResponse:
        """
        @param request: UpdateWarningConfigRequest
        @return: UpdateWarningConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_warning_config_with_options(request, runtime)

    async def update_warning_config_async(
        self,
        request: qualitycheck_20190115_models.UpdateWarningConfigRequest,
    ) -> qualitycheck_20190115_models.UpdateWarningConfigResponse:
        """
        @param request: UpdateWarningConfigRequest
        @return: UpdateWarningConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_warning_config_with_options_async(request, runtime)

    def update_warning_strategy_config_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateWarningStrategyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateWarningStrategyConfigResponse:
        """
        @summary  预警策略-更新
        
        @param request: UpdateWarningStrategyConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWarningStrategyConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWarningStrategyConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateWarningStrategyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_warning_strategy_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateWarningStrategyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateWarningStrategyConfigResponse:
        """
        @summary  预警策略-更新
        
        @param request: UpdateWarningStrategyConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWarningStrategyConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWarningStrategyConfig',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UpdateWarningStrategyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_warning_strategy_config(
        self,
        request: qualitycheck_20190115_models.UpdateWarningStrategyConfigRequest,
    ) -> qualitycheck_20190115_models.UpdateWarningStrategyConfigResponse:
        """
        @summary  预警策略-更新
        
        @param request: UpdateWarningStrategyConfigRequest
        @return: UpdateWarningStrategyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_warning_strategy_config_with_options(request, runtime)

    async def update_warning_strategy_config_async(
        self,
        request: qualitycheck_20190115_models.UpdateWarningStrategyConfigRequest,
    ) -> qualitycheck_20190115_models.UpdateWarningStrategyConfigResponse:
        """
        @summary  预警策略-更新
        
        @param request: UpdateWarningStrategyConfigRequest
        @return: UpdateWarningStrategyConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_warning_strategy_config_with_options_async(request, runtime)

    def upload_audio_data_with_options(
        self,
        request: qualitycheck_20190115_models.UploadAudioDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadAudioDataResponse:
        """
        @param request: UploadAudioDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadAudioDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadAudioData',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UploadAudioDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_audio_data_with_options_async(
        self,
        request: qualitycheck_20190115_models.UploadAudioDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadAudioDataResponse:
        """
        @param request: UploadAudioDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadAudioDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadAudioData',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UploadAudioDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_audio_data(
        self,
        request: qualitycheck_20190115_models.UploadAudioDataRequest,
    ) -> qualitycheck_20190115_models.UploadAudioDataResponse:
        """
        @param request: UploadAudioDataRequest
        @return: UploadAudioDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_audio_data_with_options(request, runtime)

    async def upload_audio_data_async(
        self,
        request: qualitycheck_20190115_models.UploadAudioDataRequest,
    ) -> qualitycheck_20190115_models.UploadAudioDataResponse:
        """
        @param request: UploadAudioDataRequest
        @return: UploadAudioDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_audio_data_with_options_async(request, runtime)

    def upload_data_with_options(
        self,
        request: qualitycheck_20190115_models.UploadDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadDataResponse:
        """
        @deprecated OpenAPI UploadData is deprecated, please use Qualitycheck::2019-01-15::UploadDataV4 instead.
        
        @summary 推荐使用UploadDataV4接口,支持更长的JsonStr,但仅支持POST方法.
        
        @param request: UploadDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadDataResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadData',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UploadDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_data_with_options_async(
        self,
        request: qualitycheck_20190115_models.UploadDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadDataResponse:
        """
        @deprecated OpenAPI UploadData is deprecated, please use Qualitycheck::2019-01-15::UploadDataV4 instead.
        
        @summary 推荐使用UploadDataV4接口,支持更长的JsonStr,但仅支持POST方法.
        
        @param request: UploadDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadDataResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadData',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UploadDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_data(
        self,
        request: qualitycheck_20190115_models.UploadDataRequest,
    ) -> qualitycheck_20190115_models.UploadDataResponse:
        """
        @deprecated OpenAPI UploadData is deprecated, please use Qualitycheck::2019-01-15::UploadDataV4 instead.
        
        @summary 推荐使用UploadDataV4接口,支持更长的JsonStr,但仅支持POST方法.
        
        @param request: UploadDataRequest
        @return: UploadDataResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_data_with_options(request, runtime)

    async def upload_data_async(
        self,
        request: qualitycheck_20190115_models.UploadDataRequest,
    ) -> qualitycheck_20190115_models.UploadDataResponse:
        """
        @deprecated OpenAPI UploadData is deprecated, please use Qualitycheck::2019-01-15::UploadDataV4 instead.
        
        @summary 推荐使用UploadDataV4接口,支持更长的JsonStr,但仅支持POST方法.
        
        @param request: UploadDataRequest
        @return: UploadDataResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_data_with_options_async(request, runtime)

    def upload_data_sync_with_options(
        self,
        request: qualitycheck_20190115_models.UploadDataSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadDataSyncResponse:
        """
        @summary http_hsf
        
        @param request: UploadDataSyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadDataSyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadDataSync',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UploadDataSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_data_sync_with_options_async(
        self,
        request: qualitycheck_20190115_models.UploadDataSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadDataSyncResponse:
        """
        @summary http_hsf
        
        @param request: UploadDataSyncRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadDataSyncResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadDataSync',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UploadDataSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_data_sync(
        self,
        request: qualitycheck_20190115_models.UploadDataSyncRequest,
    ) -> qualitycheck_20190115_models.UploadDataSyncResponse:
        """
        @summary http_hsf
        
        @param request: UploadDataSyncRequest
        @return: UploadDataSyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_data_sync_with_options(request, runtime)

    async def upload_data_sync_async(
        self,
        request: qualitycheck_20190115_models.UploadDataSyncRequest,
    ) -> qualitycheck_20190115_models.UploadDataSyncResponse:
        """
        @summary http_hsf
        
        @param request: UploadDataSyncRequest
        @return: UploadDataSyncResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_data_sync_with_options_async(request, runtime)

    def upload_data_sync_for_llmwith_options(
        self,
        request: qualitycheck_20190115_models.UploadDataSyncForLLMRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadDataSyncForLLMResponse:
        """
        @summary http_hsf
        
        @param request: UploadDataSyncForLLMRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadDataSyncForLLMResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadDataSyncForLLM',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UploadDataSyncForLLMResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_data_sync_for_llmwith_options_async(
        self,
        request: qualitycheck_20190115_models.UploadDataSyncForLLMRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadDataSyncForLLMResponse:
        """
        @summary http_hsf
        
        @param request: UploadDataSyncForLLMRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadDataSyncForLLMResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadDataSyncForLLM',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UploadDataSyncForLLMResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_data_sync_for_llm(
        self,
        request: qualitycheck_20190115_models.UploadDataSyncForLLMRequest,
    ) -> qualitycheck_20190115_models.UploadDataSyncForLLMResponse:
        """
        @summary http_hsf
        
        @param request: UploadDataSyncForLLMRequest
        @return: UploadDataSyncForLLMResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_data_sync_for_llmwith_options(request, runtime)

    async def upload_data_sync_for_llm_async(
        self,
        request: qualitycheck_20190115_models.UploadDataSyncForLLMRequest,
    ) -> qualitycheck_20190115_models.UploadDataSyncForLLMResponse:
        """
        @summary http_hsf
        
        @param request: UploadDataSyncForLLMRequest
        @return: UploadDataSyncForLLMResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_data_sync_for_llmwith_options_async(request, runtime)

    def upload_data_v4with_options(
        self,
        request: qualitycheck_20190115_models.UploadDataV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadDataV4Response:
        """
        @summary UploadDataV4
        
        @param request: UploadDataV4Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadDataV4Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            body['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            body['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadDataV4',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UploadDataV4Response(),
            self.call_api(params, req, runtime)
        )

    async def upload_data_v4with_options_async(
        self,
        request: qualitycheck_20190115_models.UploadDataV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadDataV4Response:
        """
        @summary UploadDataV4
        
        @param request: UploadDataV4Request
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadDataV4Response
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            body['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            body['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadDataV4',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UploadDataV4Response(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_data_v4(
        self,
        request: qualitycheck_20190115_models.UploadDataV4Request,
    ) -> qualitycheck_20190115_models.UploadDataV4Response:
        """
        @summary UploadDataV4
        
        @param request: UploadDataV4Request
        @return: UploadDataV4Response
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_data_v4with_options(request, runtime)

    async def upload_data_v4_async(
        self,
        request: qualitycheck_20190115_models.UploadDataV4Request,
    ) -> qualitycheck_20190115_models.UploadDataV4Response:
        """
        @summary UploadDataV4
        
        @param request: UploadDataV4Request
        @return: UploadDataV4Response
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_data_v4with_options_async(request, runtime)

    def upload_rule_with_options(
        self,
        request: qualitycheck_20190115_models.UploadRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadRuleResponse:
        """
        @param request: UploadRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UploadRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_rule_with_options_async(
        self,
        request: qualitycheck_20190115_models.UploadRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadRuleResponse:
        """
        @param request: UploadRuleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UploadRuleResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadRule',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.UploadRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_rule(
        self,
        request: qualitycheck_20190115_models.UploadRuleRequest,
    ) -> qualitycheck_20190115_models.UploadRuleResponse:
        """
        @param request: UploadRuleRequest
        @return: UploadRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_rule_with_options(request, runtime)

    async def upload_rule_async(
        self,
        request: qualitycheck_20190115_models.UploadRuleRequest,
    ) -> qualitycheck_20190115_models.UploadRuleResponse:
        """
        @param request: UploadRuleRequest
        @return: UploadRuleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upload_rule_with_options_async(request, runtime)

    def verify_file_with_options(
        self,
        request: qualitycheck_20190115_models.VerifyFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.VerifyFileResponse:
        """
        @param request: VerifyFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyFile',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.VerifyFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_file_with_options_async(
        self,
        request: qualitycheck_20190115_models.VerifyFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.VerifyFileResponse:
        """
        @param request: VerifyFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifyFileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyFile',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.VerifyFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_file(
        self,
        request: qualitycheck_20190115_models.VerifyFileRequest,
    ) -> qualitycheck_20190115_models.VerifyFileResponse:
        """
        @param request: VerifyFileRequest
        @return: VerifyFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_file_with_options(request, runtime)

    async def verify_file_async(
        self,
        request: qualitycheck_20190115_models.VerifyFileRequest,
    ) -> qualitycheck_20190115_models.VerifyFileResponse:
        """
        @param request: VerifyFileRequest
        @return: VerifyFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_file_with_options_async(request, runtime)

    def verify_sentence_with_options(
        self,
        request: qualitycheck_20190115_models.VerifySentenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.VerifySentenceResponse:
        """
        @param request: VerifySentenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifySentenceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifySentence',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.VerifySentenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_sentence_with_options_async(
        self,
        request: qualitycheck_20190115_models.VerifySentenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.VerifySentenceResponse:
        """
        @param request: VerifySentenceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: VerifySentenceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifySentence',
            version='2019-01-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            qualitycheck_20190115_models.VerifySentenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_sentence(
        self,
        request: qualitycheck_20190115_models.VerifySentenceRequest,
    ) -> qualitycheck_20190115_models.VerifySentenceResponse:
        """
        @param request: VerifySentenceRequest
        @return: VerifySentenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.verify_sentence_with_options(request, runtime)

    async def verify_sentence_async(
        self,
        request: qualitycheck_20190115_models.VerifySentenceRequest,
    ) -> qualitycheck_20190115_models.VerifySentenceResponse:
        """
        @param request: VerifySentenceRequest
        @return: VerifySentenceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.verify_sentence_with_options_async(request, runtime)
