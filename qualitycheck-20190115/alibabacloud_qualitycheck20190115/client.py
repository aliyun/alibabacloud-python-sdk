# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_qualitycheck20190115 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_business_category_with_options(
        self,
        request: main_models.AddBusinessCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddBusinessCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddBusinessCategory',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddBusinessCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_business_category_with_options_async(
        self,
        request: main_models.AddBusinessCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddBusinessCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddBusinessCategory',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddBusinessCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_business_category(
        self,
        request: main_models.AddBusinessCategoryRequest,
    ) -> main_models.AddBusinessCategoryResponse:
        runtime = RuntimeOptions()
        return self.add_business_category_with_options(request, runtime)

    async def add_business_category_async(
        self,
        request: main_models.AddBusinessCategoryRequest,
    ) -> main_models.AddBusinessCategoryResponse:
        runtime = RuntimeOptions()
        return await self.add_business_category_with_options_async(request, runtime)

    def add_rule_category_with_options(
        self,
        request: main_models.AddRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRuleCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRuleCategory',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRuleCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_rule_category_with_options_async(
        self,
        request: main_models.AddRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRuleCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRuleCategory',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRuleCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_rule_category(
        self,
        request: main_models.AddRuleCategoryRequest,
    ) -> main_models.AddRuleCategoryResponse:
        runtime = RuntimeOptions()
        return self.add_rule_category_with_options(request, runtime)

    async def add_rule_category_async(
        self,
        request: main_models.AddRuleCategoryRequest,
    ) -> main_models.AddRuleCategoryResponse:
        runtime = RuntimeOptions()
        return await self.add_rule_category_with_options_async(request, runtime)

    def add_rule_v4with_options(
        self,
        request: main_models.AddRuleV4Request,
        runtime: RuntimeOptions,
    ) -> main_models.AddRuleV4Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.is_copy):
            body['IsCopy'] = request.is_copy
        if not DaraCore.is_null(request.json_str_for_rule):
            body['JsonStrForRule'] = request.json_str_for_rule
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddRuleV4',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRuleV4Response(),
            self.call_api(params, req, runtime)
        )

    async def add_rule_v4with_options_async(
        self,
        request: main_models.AddRuleV4Request,
        runtime: RuntimeOptions,
    ) -> main_models.AddRuleV4Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.is_copy):
            body['IsCopy'] = request.is_copy
        if not DaraCore.is_null(request.json_str_for_rule):
            body['JsonStrForRule'] = request.json_str_for_rule
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddRuleV4',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRuleV4Response(),
            await self.call_api_async(params, req, runtime)
        )

    def add_rule_v4(
        self,
        request: main_models.AddRuleV4Request,
    ) -> main_models.AddRuleV4Response:
        runtime = RuntimeOptions()
        return self.add_rule_v4with_options(request, runtime)

    async def add_rule_v4_async(
        self,
        request: main_models.AddRuleV4Request,
    ) -> main_models.AddRuleV4Response:
        runtime = RuntimeOptions()
        return await self.add_rule_v4with_options_async(request, runtime)

    def apply_ws_token_with_options(
        self,
        request: main_models.ApplyWsTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyWsTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyWsToken',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyWsTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_ws_token_with_options_async(
        self,
        request: main_models.ApplyWsTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyWsTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyWsToken',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyWsTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_ws_token(
        self,
        request: main_models.ApplyWsTokenRequest,
    ) -> main_models.ApplyWsTokenResponse:
        runtime = RuntimeOptions()
        return self.apply_ws_token_with_options(request, runtime)

    async def apply_ws_token_async(
        self,
        request: main_models.ApplyWsTokenRequest,
    ) -> main_models.ApplyWsTokenResponse:
        runtime = RuntimeOptions()
        return await self.apply_ws_token_with_options_async(request, runtime)

    def assign_reviewer_with_options(
        self,
        request: main_models.AssignReviewerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignReviewerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssignReviewer',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignReviewerResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_reviewer_with_options_async(
        self,
        request: main_models.AssignReviewerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignReviewerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssignReviewer',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignReviewerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_reviewer(
        self,
        request: main_models.AssignReviewerRequest,
    ) -> main_models.AssignReviewerResponse:
        runtime = RuntimeOptions()
        return self.assign_reviewer_with_options(request, runtime)

    async def assign_reviewer_async(
        self,
        request: main_models.AssignReviewerRequest,
    ) -> main_models.AssignReviewerResponse:
        runtime = RuntimeOptions()
        return await self.assign_reviewer_with_options_async(request, runtime)

    def assign_reviewer_by_session_group_with_options(
        self,
        request: main_models.AssignReviewerBySessionGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignReviewerBySessionGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssignReviewerBySessionGroup',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignReviewerBySessionGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def assign_reviewer_by_session_group_with_options_async(
        self,
        request: main_models.AssignReviewerBySessionGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssignReviewerBySessionGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssignReviewerBySessionGroup',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssignReviewerBySessionGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def assign_reviewer_by_session_group(
        self,
        request: main_models.AssignReviewerBySessionGroupRequest,
    ) -> main_models.AssignReviewerBySessionGroupResponse:
        runtime = RuntimeOptions()
        return self.assign_reviewer_by_session_group_with_options(request, runtime)

    async def assign_reviewer_by_session_group_async(
        self,
        request: main_models.AssignReviewerBySessionGroupRequest,
    ) -> main_models.AssignReviewerBySessionGroupResponse:
        runtime = RuntimeOptions()
        return await self.assign_reviewer_by_session_group_with_options_async(request, runtime)

    def batch_submit_review_info_with_options(
        self,
        request: main_models.BatchSubmitReviewInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSubmitReviewInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchSubmitReviewInfo',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSubmitReviewInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_submit_review_info_with_options_async(
        self,
        request: main_models.BatchSubmitReviewInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchSubmitReviewInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchSubmitReviewInfo',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchSubmitReviewInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_submit_review_info(
        self,
        request: main_models.BatchSubmitReviewInfoRequest,
    ) -> main_models.BatchSubmitReviewInfoResponse:
        runtime = RuntimeOptions()
        return self.batch_submit_review_info_with_options(request, runtime)

    async def batch_submit_review_info_async(
        self,
        request: main_models.BatchSubmitReviewInfoRequest,
    ) -> main_models.BatchSubmitReviewInfoResponse:
        runtime = RuntimeOptions()
        return await self.batch_submit_review_info_with_options_async(request, runtime)

    def create_asr_vocab_with_options(
        self,
        request: main_models.CreateAsrVocabRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAsrVocabResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAsrVocab',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAsrVocabResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_asr_vocab_with_options_async(
        self,
        request: main_models.CreateAsrVocabRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAsrVocabResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAsrVocab',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAsrVocabResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_asr_vocab(
        self,
        request: main_models.CreateAsrVocabRequest,
    ) -> main_models.CreateAsrVocabResponse:
        runtime = RuntimeOptions()
        return self.create_asr_vocab_with_options(request, runtime)

    async def create_asr_vocab_async(
        self,
        request: main_models.CreateAsrVocabRequest,
    ) -> main_models.CreateAsrVocabResponse:
        runtime = RuntimeOptions()
        return await self.create_asr_vocab_with_options_async(request, runtime)

    def create_check_type_to_scheme_with_options(
        self,
        request: main_models.CreateCheckTypeToSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCheckTypeToSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCheckTypeToScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCheckTypeToSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_check_type_to_scheme_with_options_async(
        self,
        request: main_models.CreateCheckTypeToSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateCheckTypeToSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCheckTypeToScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateCheckTypeToSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_check_type_to_scheme(
        self,
        request: main_models.CreateCheckTypeToSchemeRequest,
    ) -> main_models.CreateCheckTypeToSchemeResponse:
        runtime = RuntimeOptions()
        return self.create_check_type_to_scheme_with_options(request, runtime)

    async def create_check_type_to_scheme_async(
        self,
        request: main_models.CreateCheckTypeToSchemeRequest,
    ) -> main_models.CreateCheckTypeToSchemeResponse:
        runtime = RuntimeOptions()
        return await self.create_check_type_to_scheme_with_options_async(request, runtime)

    def create_mining_task_with_options(
        self,
        request: main_models.CreateMiningTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMiningTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.file_path):
            body['FilePath'] = request.file_path
        if not DaraCore.is_null(request.param):
            body['Param'] = request.param
        if not DaraCore.is_null(request.task_type):
            body['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMiningTask',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMiningTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mining_task_with_options_async(
        self,
        request: main_models.CreateMiningTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMiningTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.callback_url):
            body['CallbackUrl'] = request.callback_url
        if not DaraCore.is_null(request.file_path):
            body['FilePath'] = request.file_path
        if not DaraCore.is_null(request.param):
            body['Param'] = request.param
        if not DaraCore.is_null(request.task_type):
            body['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMiningTask',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMiningTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mining_task(
        self,
        request: main_models.CreateMiningTaskRequest,
    ) -> main_models.CreateMiningTaskResponse:
        runtime = RuntimeOptions()
        return self.create_mining_task_with_options(request, runtime)

    async def create_mining_task_async(
        self,
        request: main_models.CreateMiningTaskRequest,
    ) -> main_models.CreateMiningTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_mining_task_with_options_async(request, runtime)

    def create_quality_check_scheme_with_options(
        self,
        request: main_models.CreateQualityCheckSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQualityCheckSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQualityCheckScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQualityCheckSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_quality_check_scheme_with_options_async(
        self,
        request: main_models.CreateQualityCheckSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateQualityCheckSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateQualityCheckScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateQualityCheckSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_quality_check_scheme(
        self,
        request: main_models.CreateQualityCheckSchemeRequest,
    ) -> main_models.CreateQualityCheckSchemeResponse:
        runtime = RuntimeOptions()
        return self.create_quality_check_scheme_with_options(request, runtime)

    async def create_quality_check_scheme_async(
        self,
        request: main_models.CreateQualityCheckSchemeRequest,
    ) -> main_models.CreateQualityCheckSchemeResponse:
        runtime = RuntimeOptions()
        return await self.create_quality_check_scheme_with_options_async(request, runtime)

    def create_scheme_task_config_with_options(
        self,
        request: main_models.CreateSchemeTaskConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSchemeTaskConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSchemeTaskConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSchemeTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scheme_task_config_with_options_async(
        self,
        request: main_models.CreateSchemeTaskConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSchemeTaskConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSchemeTaskConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSchemeTaskConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scheme_task_config(
        self,
        request: main_models.CreateSchemeTaskConfigRequest,
    ) -> main_models.CreateSchemeTaskConfigResponse:
        runtime = RuntimeOptions()
        return self.create_scheme_task_config_with_options(request, runtime)

    async def create_scheme_task_config_async(
        self,
        request: main_models.CreateSchemeTaskConfigRequest,
    ) -> main_models.CreateSchemeTaskConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_scheme_task_config_with_options_async(request, runtime)

    def create_skill_group_config_with_options(
        self,
        request: main_models.CreateSkillGroupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillGroupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkillGroupConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSkillGroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_skill_group_config_with_options_async(
        self,
        request: main_models.CreateSkillGroupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillGroupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkillGroupConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSkillGroupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_skill_group_config(
        self,
        request: main_models.CreateSkillGroupConfigRequest,
    ) -> main_models.CreateSkillGroupConfigResponse:
        runtime = RuntimeOptions()
        return self.create_skill_group_config_with_options(request, runtime)

    async def create_skill_group_config_async(
        self,
        request: main_models.CreateSkillGroupConfigRequest,
    ) -> main_models.CreateSkillGroupConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_skill_group_config_with_options_async(request, runtime)

    def create_task_assign_rule_with_options(
        self,
        request: main_models.CreateTaskAssignRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTaskAssignRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTaskAssignRule',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTaskAssignRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_assign_rule_with_options_async(
        self,
        request: main_models.CreateTaskAssignRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTaskAssignRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTaskAssignRule',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTaskAssignRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task_assign_rule(
        self,
        request: main_models.CreateTaskAssignRuleRequest,
    ) -> main_models.CreateTaskAssignRuleResponse:
        runtime = RuntimeOptions()
        return self.create_task_assign_rule_with_options(request, runtime)

    async def create_task_assign_rule_async(
        self,
        request: main_models.CreateTaskAssignRuleRequest,
    ) -> main_models.CreateTaskAssignRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_task_assign_rule_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: main_models.CreateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            body['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            body['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: main_models.CreateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUserResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            body['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            body['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateUser',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: main_models.CreateUserRequest,
    ) -> main_models.CreateUserResponse:
        runtime = RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def create_warning_config_with_options(
        self,
        request: main_models.CreateWarningConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWarningConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWarningConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWarningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_warning_config_with_options_async(
        self,
        request: main_models.CreateWarningConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWarningConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWarningConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWarningConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_warning_config(
        self,
        request: main_models.CreateWarningConfigRequest,
    ) -> main_models.CreateWarningConfigResponse:
        runtime = RuntimeOptions()
        return self.create_warning_config_with_options(request, runtime)

    async def create_warning_config_async(
        self,
        request: main_models.CreateWarningConfigRequest,
    ) -> main_models.CreateWarningConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_warning_config_with_options_async(request, runtime)

    def create_warning_strategy_config_with_options(
        self,
        request: main_models.CreateWarningStrategyConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWarningStrategyConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWarningStrategyConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWarningStrategyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_warning_strategy_config_with_options_async(
        self,
        request: main_models.CreateWarningStrategyConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWarningStrategyConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWarningStrategyConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWarningStrategyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_warning_strategy_config(
        self,
        request: main_models.CreateWarningStrategyConfigRequest,
    ) -> main_models.CreateWarningStrategyConfigResponse:
        runtime = RuntimeOptions()
        return self.create_warning_strategy_config_with_options(request, runtime)

    async def create_warning_strategy_config_async(
        self,
        request: main_models.CreateWarningStrategyConfigRequest,
    ) -> main_models.CreateWarningStrategyConfigResponse:
        runtime = RuntimeOptions()
        return await self.create_warning_strategy_config_with_options_async(request, runtime)

    def del_rule_category_with_options(
        self,
        request: main_models.DelRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DelRuleCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DelRuleCategory',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DelRuleCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def del_rule_category_with_options_async(
        self,
        request: main_models.DelRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DelRuleCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DelRuleCategory',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DelRuleCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def del_rule_category(
        self,
        request: main_models.DelRuleCategoryRequest,
    ) -> main_models.DelRuleCategoryResponse:
        runtime = RuntimeOptions()
        return self.del_rule_category_with_options(request, runtime)

    async def del_rule_category_async(
        self,
        request: main_models.DelRuleCategoryRequest,
    ) -> main_models.DelRuleCategoryResponse:
        runtime = RuntimeOptions()
        return await self.del_rule_category_with_options_async(request, runtime)

    def delete_asr_vocab_with_options(
        self,
        request: main_models.DeleteAsrVocabRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAsrVocabResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAsrVocab',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAsrVocabResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_asr_vocab_with_options_async(
        self,
        request: main_models.DeleteAsrVocabRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAsrVocabResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAsrVocab',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAsrVocabResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_asr_vocab(
        self,
        request: main_models.DeleteAsrVocabRequest,
    ) -> main_models.DeleteAsrVocabResponse:
        runtime = RuntimeOptions()
        return self.delete_asr_vocab_with_options(request, runtime)

    async def delete_asr_vocab_async(
        self,
        request: main_models.DeleteAsrVocabRequest,
    ) -> main_models.DeleteAsrVocabResponse:
        runtime = RuntimeOptions()
        return await self.delete_asr_vocab_with_options_async(request, runtime)

    def delete_business_category_with_options(
        self,
        request: main_models.DeleteBusinessCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBusinessCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBusinessCategory',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBusinessCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_business_category_with_options_async(
        self,
        request: main_models.DeleteBusinessCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBusinessCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBusinessCategory',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBusinessCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_business_category(
        self,
        request: main_models.DeleteBusinessCategoryRequest,
    ) -> main_models.DeleteBusinessCategoryResponse:
        runtime = RuntimeOptions()
        return self.delete_business_category_with_options(request, runtime)

    async def delete_business_category_async(
        self,
        request: main_models.DeleteBusinessCategoryRequest,
    ) -> main_models.DeleteBusinessCategoryResponse:
        runtime = RuntimeOptions()
        return await self.delete_business_category_with_options_async(request, runtime)

    def delete_check_type_to_scheme_with_options(
        self,
        request: main_models.DeleteCheckTypeToSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCheckTypeToSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCheckTypeToScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCheckTypeToSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_check_type_to_scheme_with_options_async(
        self,
        request: main_models.DeleteCheckTypeToSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCheckTypeToSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCheckTypeToScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCheckTypeToSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_check_type_to_scheme(
        self,
        request: main_models.DeleteCheckTypeToSchemeRequest,
    ) -> main_models.DeleteCheckTypeToSchemeResponse:
        runtime = RuntimeOptions()
        return self.delete_check_type_to_scheme_with_options(request, runtime)

    async def delete_check_type_to_scheme_async(
        self,
        request: main_models.DeleteCheckTypeToSchemeRequest,
    ) -> main_models.DeleteCheckTypeToSchemeResponse:
        runtime = RuntimeOptions()
        return await self.delete_check_type_to_scheme_with_options_async(request, runtime)

    def delete_customization_config_with_options(
        self,
        request: main_models.DeleteCustomizationConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomizationConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomizationConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomizationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_customization_config_with_options_async(
        self,
        request: main_models.DeleteCustomizationConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomizationConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomizationConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomizationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_customization_config(
        self,
        request: main_models.DeleteCustomizationConfigRequest,
    ) -> main_models.DeleteCustomizationConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_customization_config_with_options(request, runtime)

    async def delete_customization_config_async(
        self,
        request: main_models.DeleteCustomizationConfigRequest,
    ) -> main_models.DeleteCustomizationConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_customization_config_with_options_async(request, runtime)

    def delete_data_set_with_options(
        self,
        request: main_models.DeleteDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSet',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_data_set_with_options_async(
        self,
        request: main_models.DeleteDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDataSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDataSet',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_data_set(
        self,
        request: main_models.DeleteDataSetRequest,
    ) -> main_models.DeleteDataSetResponse:
        runtime = RuntimeOptions()
        return self.delete_data_set_with_options(request, runtime)

    async def delete_data_set_async(
        self,
        request: main_models.DeleteDataSetRequest,
    ) -> main_models.DeleteDataSetResponse:
        runtime = RuntimeOptions()
        return await self.delete_data_set_with_options_async(request, runtime)

    def delete_precision_task_with_options(
        self,
        request: main_models.DeletePrecisionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrecisionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrecisionTask',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrecisionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_precision_task_with_options_async(
        self,
        request: main_models.DeletePrecisionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrecisionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrecisionTask',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrecisionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_precision_task(
        self,
        request: main_models.DeletePrecisionTaskRequest,
    ) -> main_models.DeletePrecisionTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_precision_task_with_options(request, runtime)

    async def delete_precision_task_async(
        self,
        request: main_models.DeletePrecisionTaskRequest,
    ) -> main_models.DeletePrecisionTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_precision_task_with_options_async(request, runtime)

    def delete_quality_check_scheme_with_options(
        self,
        request: main_models.DeleteQualityCheckSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQualityCheckSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQualityCheckScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQualityCheckSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_quality_check_scheme_with_options_async(
        self,
        request: main_models.DeleteQualityCheckSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteQualityCheckSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteQualityCheckScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteQualityCheckSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_quality_check_scheme(
        self,
        request: main_models.DeleteQualityCheckSchemeRequest,
    ) -> main_models.DeleteQualityCheckSchemeResponse:
        runtime = RuntimeOptions()
        return self.delete_quality_check_scheme_with_options(request, runtime)

    async def delete_quality_check_scheme_async(
        self,
        request: main_models.DeleteQualityCheckSchemeRequest,
    ) -> main_models.DeleteQualityCheckSchemeResponse:
        runtime = RuntimeOptions()
        return await self.delete_quality_check_scheme_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: main_models.DeleteRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.force_delete):
            body['ForceDelete'] = request.force_delete
        if not DaraCore.is_null(request.is_scheme_data):
            body['IsSchemeData'] = request.is_scheme_data
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRule',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rule_with_options_async(
        self,
        request: main_models.DeleteRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.force_delete):
            body['ForceDelete'] = request.force_delete
        if not DaraCore.is_null(request.is_scheme_data):
            body['IsSchemeData'] = request.is_scheme_data
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRule',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rule(
        self,
        request: main_models.DeleteRuleRequest,
    ) -> main_models.DeleteRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: main_models.DeleteRuleRequest,
    ) -> main_models.DeleteRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def delete_rule_v4with_options(
        self,
        request: main_models.DeleteRuleV4Request,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRuleV4Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.force_delete):
            body['ForceDelete'] = request.force_delete
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRuleV4',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRuleV4Response(),
            self.call_api(params, req, runtime)
        )

    async def delete_rule_v4with_options_async(
        self,
        request: main_models.DeleteRuleV4Request,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRuleV4Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.force_delete):
            body['ForceDelete'] = request.force_delete
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRuleV4',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRuleV4Response(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rule_v4(
        self,
        request: main_models.DeleteRuleV4Request,
    ) -> main_models.DeleteRuleV4Response:
        runtime = RuntimeOptions()
        return self.delete_rule_v4with_options(request, runtime)

    async def delete_rule_v4_async(
        self,
        request: main_models.DeleteRuleV4Request,
    ) -> main_models.DeleteRuleV4Response:
        runtime = RuntimeOptions()
        return await self.delete_rule_v4with_options_async(request, runtime)

    def delete_scheme_task_config_with_options(
        self,
        request: main_models.DeleteSchemeTaskConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSchemeTaskConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSchemeTaskConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSchemeTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scheme_task_config_with_options_async(
        self,
        request: main_models.DeleteSchemeTaskConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSchemeTaskConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSchemeTaskConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSchemeTaskConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scheme_task_config(
        self,
        request: main_models.DeleteSchemeTaskConfigRequest,
    ) -> main_models.DeleteSchemeTaskConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_scheme_task_config_with_options(request, runtime)

    async def delete_scheme_task_config_async(
        self,
        request: main_models.DeleteSchemeTaskConfigRequest,
    ) -> main_models.DeleteSchemeTaskConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_scheme_task_config_with_options_async(request, runtime)

    def delete_skill_group_config_with_options(
        self,
        request: main_models.DeleteSkillGroupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSkillGroupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSkillGroupConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSkillGroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_skill_group_config_with_options_async(
        self,
        request: main_models.DeleteSkillGroupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSkillGroupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSkillGroupConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSkillGroupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_skill_group_config(
        self,
        request: main_models.DeleteSkillGroupConfigRequest,
    ) -> main_models.DeleteSkillGroupConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_skill_group_config_with_options(request, runtime)

    async def delete_skill_group_config_async(
        self,
        request: main_models.DeleteSkillGroupConfigRequest,
    ) -> main_models.DeleteSkillGroupConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_skill_group_config_with_options_async(request, runtime)

    def delete_task_assign_rule_with_options(
        self,
        request: main_models.DeleteTaskAssignRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTaskAssignRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTaskAssignRule',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTaskAssignRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_task_assign_rule_with_options_async(
        self,
        request: main_models.DeleteTaskAssignRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTaskAssignRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTaskAssignRule',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTaskAssignRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_task_assign_rule(
        self,
        request: main_models.DeleteTaskAssignRuleRequest,
    ) -> main_models.DeleteTaskAssignRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_task_assign_rule_with_options(request, runtime)

    async def delete_task_assign_rule_async(
        self,
        request: main_models.DeleteTaskAssignRuleRequest,
    ) -> main_models.DeleteTaskAssignRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_task_assign_rule_with_options_async(request, runtime)

    def delete_warning_config_with_options(
        self,
        request: main_models.DeleteWarningConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWarningConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWarningConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWarningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_warning_config_with_options_async(
        self,
        request: main_models.DeleteWarningConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWarningConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWarningConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWarningConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_warning_config(
        self,
        request: main_models.DeleteWarningConfigRequest,
    ) -> main_models.DeleteWarningConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_warning_config_with_options(request, runtime)

    async def delete_warning_config_async(
        self,
        request: main_models.DeleteWarningConfigRequest,
    ) -> main_models.DeleteWarningConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_warning_config_with_options_async(request, runtime)

    def delete_warning_strategy_config_with_options(
        self,
        request: main_models.DeleteWarningStrategyConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWarningStrategyConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWarningStrategyConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWarningStrategyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_warning_strategy_config_with_options_async(
        self,
        request: main_models.DeleteWarningStrategyConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWarningStrategyConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWarningStrategyConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWarningStrategyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_warning_strategy_config(
        self,
        request: main_models.DeleteWarningStrategyConfigRequest,
    ) -> main_models.DeleteWarningStrategyConfigResponse:
        runtime = RuntimeOptions()
        return self.delete_warning_strategy_config_with_options(request, runtime)

    async def delete_warning_strategy_config_async(
        self,
        request: main_models.DeleteWarningStrategyConfigRequest,
    ) -> main_models.DeleteWarningStrategyConfigResponse:
        runtime = RuntimeOptions()
        return await self.delete_warning_strategy_config_with_options_async(request, runtime)

    def get_asr_vocab_with_options(
        self,
        request: main_models.GetAsrVocabRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAsrVocabResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsrVocab',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsrVocabResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_asr_vocab_with_options_async(
        self,
        request: main_models.GetAsrVocabRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAsrVocabResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAsrVocab',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAsrVocabResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_asr_vocab(
        self,
        request: main_models.GetAsrVocabRequest,
    ) -> main_models.GetAsrVocabResponse:
        runtime = RuntimeOptions()
        return self.get_asr_vocab_with_options(request, runtime)

    async def get_asr_vocab_async(
        self,
        request: main_models.GetAsrVocabRequest,
    ) -> main_models.GetAsrVocabResponse:
        runtime = RuntimeOptions()
        return await self.get_asr_vocab_with_options_async(request, runtime)

    def get_business_category_list_with_options(
        self,
        request: main_models.GetBusinessCategoryListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBusinessCategoryListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBusinessCategoryList',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBusinessCategoryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_business_category_list_with_options_async(
        self,
        request: main_models.GetBusinessCategoryListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBusinessCategoryListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBusinessCategoryList',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBusinessCategoryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_business_category_list(
        self,
        request: main_models.GetBusinessCategoryListRequest,
    ) -> main_models.GetBusinessCategoryListResponse:
        runtime = RuntimeOptions()
        return self.get_business_category_list_with_options(request, runtime)

    async def get_business_category_list_async(
        self,
        request: main_models.GetBusinessCategoryListRequest,
    ) -> main_models.GetBusinessCategoryListResponse:
        runtime = RuntimeOptions()
        return await self.get_business_category_list_with_options_async(request, runtime)

    def get_customization_config_list_with_options(
        self,
        request: main_models.GetCustomizationConfigListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomizationConfigListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomizationConfigList',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomizationConfigListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_customization_config_list_with_options_async(
        self,
        request: main_models.GetCustomizationConfigListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCustomizationConfigListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCustomizationConfigList',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCustomizationConfigListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_customization_config_list(
        self,
        request: main_models.GetCustomizationConfigListRequest,
    ) -> main_models.GetCustomizationConfigListResponse:
        runtime = RuntimeOptions()
        return self.get_customization_config_list_with_options(request, runtime)

    async def get_customization_config_list_async(
        self,
        request: main_models.GetCustomizationConfigListRequest,
    ) -> main_models.GetCustomizationConfigListResponse:
        runtime = RuntimeOptions()
        return await self.get_customization_config_list_with_options_async(request, runtime)

    def get_mining_task_result_with_options(
        self,
        request: main_models.GetMiningTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMiningTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMiningTaskResult',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMiningTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mining_task_result_with_options_async(
        self,
        request: main_models.GetMiningTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMiningTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMiningTaskResult',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMiningTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mining_task_result(
        self,
        request: main_models.GetMiningTaskResultRequest,
    ) -> main_models.GetMiningTaskResultResponse:
        runtime = RuntimeOptions()
        return self.get_mining_task_result_with_options(request, runtime)

    async def get_mining_task_result_async(
        self,
        request: main_models.GetMiningTaskResultRequest,
    ) -> main_models.GetMiningTaskResultResponse:
        runtime = RuntimeOptions()
        return await self.get_mining_task_result_with_options_async(request, runtime)

    def get_next_result_to_verify_with_options(
        self,
        request: main_models.GetNextResultToVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNextResultToVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNextResultToVerify',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNextResultToVerifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_next_result_to_verify_with_options_async(
        self,
        request: main_models.GetNextResultToVerifyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNextResultToVerifyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNextResultToVerify',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNextResultToVerifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_next_result_to_verify(
        self,
        request: main_models.GetNextResultToVerifyRequest,
    ) -> main_models.GetNextResultToVerifyResponse:
        runtime = RuntimeOptions()
        return self.get_next_result_to_verify_with_options(request, runtime)

    async def get_next_result_to_verify_async(
        self,
        request: main_models.GetNextResultToVerifyRequest,
    ) -> main_models.GetNextResultToVerifyResponse:
        runtime = RuntimeOptions()
        return await self.get_next_result_to_verify_with_options_async(request, runtime)

    def get_precision_task_with_options(
        self,
        request: main_models.GetPrecisionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPrecisionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrecisionTask',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrecisionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_precision_task_with_options_async(
        self,
        request: main_models.GetPrecisionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPrecisionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrecisionTask',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrecisionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_precision_task(
        self,
        request: main_models.GetPrecisionTaskRequest,
    ) -> main_models.GetPrecisionTaskResponse:
        runtime = RuntimeOptions()
        return self.get_precision_task_with_options(request, runtime)

    async def get_precision_task_async(
        self,
        request: main_models.GetPrecisionTaskRequest,
    ) -> main_models.GetPrecisionTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_precision_task_with_options_async(request, runtime)

    def get_quality_check_scheme_with_options(
        self,
        request: main_models.GetQualityCheckSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityCheckSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityCheckScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityCheckSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_quality_check_scheme_with_options_async(
        self,
        request: main_models.GetQualityCheckSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetQualityCheckSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetQualityCheckScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetQualityCheckSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_quality_check_scheme(
        self,
        request: main_models.GetQualityCheckSchemeRequest,
    ) -> main_models.GetQualityCheckSchemeResponse:
        runtime = RuntimeOptions()
        return self.get_quality_check_scheme_with_options(request, runtime)

    async def get_quality_check_scheme_async(
        self,
        request: main_models.GetQualityCheckSchemeRequest,
    ) -> main_models.GetQualityCheckSchemeResponse:
        runtime = RuntimeOptions()
        return await self.get_quality_check_scheme_with_options_async(request, runtime)

    def get_result_with_options(
        self,
        request: main_models.GetResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResult',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_result_with_options_async(
        self,
        request: main_models.GetResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResult',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_result(
        self,
        request: main_models.GetResultRequest,
    ) -> main_models.GetResultResponse:
        runtime = RuntimeOptions()
        return self.get_result_with_options(request, runtime)

    async def get_result_async(
        self,
        request: main_models.GetResultRequest,
    ) -> main_models.GetResultResponse:
        runtime = RuntimeOptions()
        return await self.get_result_with_options_async(request, runtime)

    def get_result_to_review_with_options(
        self,
        request: main_models.GetResultToReviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResultToReviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResultToReview',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResultToReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_result_to_review_with_options_async(
        self,
        request: main_models.GetResultToReviewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResultToReviewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResultToReview',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResultToReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_result_to_review(
        self,
        request: main_models.GetResultToReviewRequest,
    ) -> main_models.GetResultToReviewResponse:
        runtime = RuntimeOptions()
        return self.get_result_to_review_with_options(request, runtime)

    async def get_result_to_review_async(
        self,
        request: main_models.GetResultToReviewRequest,
    ) -> main_models.GetResultToReviewResponse:
        runtime = RuntimeOptions()
        return await self.get_result_to_review_with_options_async(request, runtime)

    def get_rule_with_options(
        self,
        request: main_models.GetRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRule',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rule_with_options_async(
        self,
        request: main_models.GetRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRule',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rule(
        self,
        request: main_models.GetRuleRequest,
    ) -> main_models.GetRuleResponse:
        runtime = RuntimeOptions()
        return self.get_rule_with_options(request, runtime)

    async def get_rule_async(
        self,
        request: main_models.GetRuleRequest,
    ) -> main_models.GetRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_rule_with_options_async(request, runtime)

    def get_rule_by_id_with_options(
        self,
        request: main_models.GetRuleByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRuleByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetRuleById',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRuleByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rule_by_id_with_options_async(
        self,
        request: main_models.GetRuleByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRuleByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetRuleById',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRuleByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rule_by_id(
        self,
        request: main_models.GetRuleByIdRequest,
    ) -> main_models.GetRuleByIdResponse:
        runtime = RuntimeOptions()
        return self.get_rule_by_id_with_options(request, runtime)

    async def get_rule_by_id_async(
        self,
        request: main_models.GetRuleByIdRequest,
    ) -> main_models.GetRuleByIdResponse:
        runtime = RuntimeOptions()
        return await self.get_rule_by_id_with_options_async(request, runtime)

    def get_rule_category_with_options(
        self,
        request: main_models.GetRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRuleCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRuleCategory',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRuleCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rule_category_with_options_async(
        self,
        request: main_models.GetRuleCategoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRuleCategoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRuleCategory',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRuleCategoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rule_category(
        self,
        request: main_models.GetRuleCategoryRequest,
    ) -> main_models.GetRuleCategoryResponse:
        runtime = RuntimeOptions()
        return self.get_rule_category_with_options(request, runtime)

    async def get_rule_category_async(
        self,
        request: main_models.GetRuleCategoryRequest,
    ) -> main_models.GetRuleCategoryResponse:
        runtime = RuntimeOptions()
        return await self.get_rule_category_with_options_async(request, runtime)

    def get_rule_detail_with_options(
        self,
        request: main_models.GetRuleDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRuleDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRuleDetail',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRuleDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rule_detail_with_options_async(
        self,
        request: main_models.GetRuleDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRuleDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRuleDetail',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRuleDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rule_detail(
        self,
        request: main_models.GetRuleDetailRequest,
    ) -> main_models.GetRuleDetailResponse:
        runtime = RuntimeOptions()
        return self.get_rule_detail_with_options(request, runtime)

    async def get_rule_detail_async(
        self,
        request: main_models.GetRuleDetailRequest,
    ) -> main_models.GetRuleDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_rule_detail_with_options_async(request, runtime)

    def get_rule_v4with_options(
        self,
        request: main_models.GetRuleV4Request,
        runtime: RuntimeOptions,
    ) -> main_models.GetRuleV4Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetRuleV4',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRuleV4Response(),
            self.call_api(params, req, runtime)
        )

    async def get_rule_v4with_options_async(
        self,
        request: main_models.GetRuleV4Request,
        runtime: RuntimeOptions,
    ) -> main_models.GetRuleV4Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetRuleV4',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRuleV4Response(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rule_v4(
        self,
        request: main_models.GetRuleV4Request,
    ) -> main_models.GetRuleV4Response:
        runtime = RuntimeOptions()
        return self.get_rule_v4with_options(request, runtime)

    async def get_rule_v4_async(
        self,
        request: main_models.GetRuleV4Request,
    ) -> main_models.GetRuleV4Response:
        runtime = RuntimeOptions()
        return await self.get_rule_v4with_options_async(request, runtime)

    def get_rules_count_list_with_options(
        self,
        request: main_models.GetRulesCountListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRulesCountListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.business_name):
            body['BusinessName'] = request.business_name
        if not DaraCore.is_null(request.business_range):
            body['BusinessRange'] = request.business_range
        if not DaraCore.is_null(request.category_name):
            body['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.count_total):
            body['CountTotal'] = request.count_total
        if not DaraCore.is_null(request.create_empid):
            body['CreateEmpid'] = request.create_empid
        if not DaraCore.is_null(request.create_user_id):
            body['CreateUserId'] = request.create_user_id
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.last_update_empid):
            body['LastUpdateEmpid'] = request.last_update_empid
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.require_infos):
            body['RequireInfos'] = request.require_infos
        if not DaraCore.is_null(request.rid):
            body['Rid'] = request.rid
        if not DaraCore.is_null(request.rule_id_or_rule_name):
            body['RuleIdOrRuleName'] = request.rule_id_or_rule_name
        if not DaraCore.is_null(request.rule_score_single_type):
            body['RuleScoreSingleType'] = request.rule_score_single_type
        if not DaraCore.is_null(request.rule_type):
            body['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.scheme_id):
            body['SchemeId'] = request.scheme_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.type_name):
            body['TypeName'] = request.type_name
        if not DaraCore.is_null(request.update_end_time):
            body['UpdateEndTime'] = request.update_end_time
        if not DaraCore.is_null(request.update_start_time):
            body['UpdateStartTime'] = request.update_start_time
        if not DaraCore.is_null(request.update_user_id):
            body['UpdateUserId'] = request.update_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetRulesCountList',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRulesCountListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rules_count_list_with_options_async(
        self,
        request: main_models.GetRulesCountListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRulesCountListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.business_name):
            body['BusinessName'] = request.business_name
        if not DaraCore.is_null(request.business_range):
            body['BusinessRange'] = request.business_range
        if not DaraCore.is_null(request.category_name):
            body['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.count_total):
            body['CountTotal'] = request.count_total
        if not DaraCore.is_null(request.create_empid):
            body['CreateEmpid'] = request.create_empid
        if not DaraCore.is_null(request.create_user_id):
            body['CreateUserId'] = request.create_user_id
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.last_update_empid):
            body['LastUpdateEmpid'] = request.last_update_empid
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.require_infos):
            body['RequireInfos'] = request.require_infos
        if not DaraCore.is_null(request.rid):
            body['Rid'] = request.rid
        if not DaraCore.is_null(request.rule_id_or_rule_name):
            body['RuleIdOrRuleName'] = request.rule_id_or_rule_name
        if not DaraCore.is_null(request.rule_score_single_type):
            body['RuleScoreSingleType'] = request.rule_score_single_type
        if not DaraCore.is_null(request.rule_type):
            body['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.scheme_id):
            body['SchemeId'] = request.scheme_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.type_name):
            body['TypeName'] = request.type_name
        if not DaraCore.is_null(request.update_end_time):
            body['UpdateEndTime'] = request.update_end_time
        if not DaraCore.is_null(request.update_start_time):
            body['UpdateStartTime'] = request.update_start_time
        if not DaraCore.is_null(request.update_user_id):
            body['UpdateUserId'] = request.update_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetRulesCountList',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRulesCountListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rules_count_list(
        self,
        request: main_models.GetRulesCountListRequest,
    ) -> main_models.GetRulesCountListResponse:
        runtime = RuntimeOptions()
        return self.get_rules_count_list_with_options(request, runtime)

    async def get_rules_count_list_async(
        self,
        request: main_models.GetRulesCountListRequest,
    ) -> main_models.GetRulesCountListResponse:
        runtime = RuntimeOptions()
        return await self.get_rules_count_list_with_options_async(request, runtime)

    def get_scheme_task_config_with_options(
        self,
        request: main_models.GetSchemeTaskConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSchemeTaskConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSchemeTaskConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSchemeTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scheme_task_config_with_options_async(
        self,
        request: main_models.GetSchemeTaskConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSchemeTaskConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSchemeTaskConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSchemeTaskConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scheme_task_config(
        self,
        request: main_models.GetSchemeTaskConfigRequest,
    ) -> main_models.GetSchemeTaskConfigResponse:
        runtime = RuntimeOptions()
        return self.get_scheme_task_config_with_options(request, runtime)

    async def get_scheme_task_config_async(
        self,
        request: main_models.GetSchemeTaskConfigRequest,
    ) -> main_models.GetSchemeTaskConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_scheme_task_config_with_options_async(request, runtime)

    def get_score_info_with_options(
        self,
        request: main_models.GetScoreInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScoreInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScoreInfo',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScoreInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_score_info_with_options_async(
        self,
        request: main_models.GetScoreInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScoreInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScoreInfo',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScoreInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_score_info(
        self,
        request: main_models.GetScoreInfoRequest,
    ) -> main_models.GetScoreInfoResponse:
        runtime = RuntimeOptions()
        return self.get_score_info_with_options(request, runtime)

    async def get_score_info_async(
        self,
        request: main_models.GetScoreInfoRequest,
    ) -> main_models.GetScoreInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_score_info_with_options_async(request, runtime)

    def get_skill_group_config_with_options(
        self,
        request: main_models.GetSkillGroupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillGroupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillGroupConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillGroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_group_config_with_options_async(
        self,
        request: main_models.GetSkillGroupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillGroupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillGroupConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillGroupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_group_config(
        self,
        request: main_models.GetSkillGroupConfigRequest,
    ) -> main_models.GetSkillGroupConfigResponse:
        runtime = RuntimeOptions()
        return self.get_skill_group_config_with_options(request, runtime)

    async def get_skill_group_config_async(
        self,
        request: main_models.GetSkillGroupConfigRequest,
    ) -> main_models.GetSkillGroupConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_skill_group_config_with_options_async(request, runtime)

    def get_sync_result_with_options(
        self,
        request: main_models.GetSyncResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSyncResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSyncResult',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sync_result_with_options_async(
        self,
        request: main_models.GetSyncResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSyncResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSyncResult',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSyncResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sync_result(
        self,
        request: main_models.GetSyncResultRequest,
    ) -> main_models.GetSyncResultResponse:
        runtime = RuntimeOptions()
        return self.get_sync_result_with_options(request, runtime)

    async def get_sync_result_async(
        self,
        request: main_models.GetSyncResultRequest,
    ) -> main_models.GetSyncResultResponse:
        runtime = RuntimeOptions()
        return await self.get_sync_result_with_options_async(request, runtime)

    def get_warning_strategy_config_with_options(
        self,
        request: main_models.GetWarningStrategyConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWarningStrategyConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWarningStrategyConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWarningStrategyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_warning_strategy_config_with_options_async(
        self,
        request: main_models.GetWarningStrategyConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetWarningStrategyConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetWarningStrategyConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetWarningStrategyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_warning_strategy_config(
        self,
        request: main_models.GetWarningStrategyConfigRequest,
    ) -> main_models.GetWarningStrategyConfigResponse:
        runtime = RuntimeOptions()
        return self.get_warning_strategy_config_with_options(request, runtime)

    async def get_warning_strategy_config_async(
        self,
        request: main_models.GetWarningStrategyConfigRequest,
    ) -> main_models.GetWarningStrategyConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_warning_strategy_config_with_options_async(request, runtime)

    def handle_complaint_with_options(
        self,
        request: main_models.HandleComplaintRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HandleComplaintResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HandleComplaint',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HandleComplaintResponse(),
            self.call_api(params, req, runtime)
        )

    async def handle_complaint_with_options_async(
        self,
        request: main_models.HandleComplaintRequest,
        runtime: RuntimeOptions,
    ) -> main_models.HandleComplaintResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'HandleComplaint',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.HandleComplaintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def handle_complaint(
        self,
        request: main_models.HandleComplaintRequest,
    ) -> main_models.HandleComplaintResponse:
        runtime = RuntimeOptions()
        return self.handle_complaint_with_options(request, runtime)

    async def handle_complaint_async(
        self,
        request: main_models.HandleComplaintRequest,
    ) -> main_models.HandleComplaintResponse:
        runtime = RuntimeOptions()
        return await self.handle_complaint_with_options_async(request, runtime)

    def invalid_rule_with_options(
        self,
        request: main_models.InvalidRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InvalidRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvalidRule',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvalidRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def invalid_rule_with_options_async(
        self,
        request: main_models.InvalidRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InvalidRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InvalidRule',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InvalidRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def invalid_rule(
        self,
        request: main_models.InvalidRuleRequest,
    ) -> main_models.InvalidRuleResponse:
        runtime = RuntimeOptions()
        return self.invalid_rule_with_options(request, runtime)

    async def invalid_rule_async(
        self,
        request: main_models.InvalidRuleRequest,
    ) -> main_models.InvalidRuleResponse:
        runtime = RuntimeOptions()
        return await self.invalid_rule_with_options_async(request, runtime)

    def list_asr_vocab_with_options(
        self,
        request: main_models.ListAsrVocabRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAsrVocabResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAsrVocab',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAsrVocabResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_asr_vocab_with_options_async(
        self,
        request: main_models.ListAsrVocabRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAsrVocabResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAsrVocab',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAsrVocabResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_asr_vocab(
        self,
        request: main_models.ListAsrVocabRequest,
    ) -> main_models.ListAsrVocabResponse:
        runtime = RuntimeOptions()
        return self.list_asr_vocab_with_options(request, runtime)

    async def list_asr_vocab_async(
        self,
        request: main_models.ListAsrVocabRequest,
    ) -> main_models.ListAsrVocabResponse:
        runtime = RuntimeOptions()
        return await self.list_asr_vocab_with_options_async(request, runtime)

    def list_data_set_with_options(
        self,
        request: main_models.ListDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSet',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_set_with_options_async(
        self,
        request: main_models.ListDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDataSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDataSet',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_set(
        self,
        request: main_models.ListDataSetRequest,
    ) -> main_models.ListDataSetResponse:
        runtime = RuntimeOptions()
        return self.list_data_set_with_options(request, runtime)

    async def list_data_set_async(
        self,
        request: main_models.ListDataSetRequest,
    ) -> main_models.ListDataSetResponse:
        runtime = RuntimeOptions()
        return await self.list_data_set_with_options_async(request, runtime)

    def list_precision_task_with_options(
        self,
        request: main_models.ListPrecisionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrecisionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrecisionTask',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrecisionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_precision_task_with_options_async(
        self,
        request: main_models.ListPrecisionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrecisionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrecisionTask',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrecisionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_precision_task(
        self,
        request: main_models.ListPrecisionTaskRequest,
    ) -> main_models.ListPrecisionTaskResponse:
        runtime = RuntimeOptions()
        return self.list_precision_task_with_options(request, runtime)

    async def list_precision_task_async(
        self,
        request: main_models.ListPrecisionTaskRequest,
    ) -> main_models.ListPrecisionTaskResponse:
        runtime = RuntimeOptions()
        return await self.list_precision_task_with_options_async(request, runtime)

    def list_quality_check_scheme_with_options(
        self,
        request: main_models.ListQualityCheckSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQualityCheckSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQualityCheckScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQualityCheckSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_quality_check_scheme_with_options_async(
        self,
        request: main_models.ListQualityCheckSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListQualityCheckSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListQualityCheckScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListQualityCheckSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_quality_check_scheme(
        self,
        request: main_models.ListQualityCheckSchemeRequest,
    ) -> main_models.ListQualityCheckSchemeResponse:
        runtime = RuntimeOptions()
        return self.list_quality_check_scheme_with_options(request, runtime)

    async def list_quality_check_scheme_async(
        self,
        request: main_models.ListQualityCheckSchemeRequest,
    ) -> main_models.ListQualityCheckSchemeResponse:
        runtime = RuntimeOptions()
        return await self.list_quality_check_scheme_with_options_async(request, runtime)

    def list_rules_with_options(
        self,
        request: main_models.ListRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRules',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_rules_with_options_async(
        self,
        request: main_models.ListRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRules',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rules(
        self,
        request: main_models.ListRulesRequest,
    ) -> main_models.ListRulesResponse:
        runtime = RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    async def list_rules_async(
        self,
        request: main_models.ListRulesRequest,
    ) -> main_models.ListRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_rules_with_options_async(request, runtime)

    def list_rules_v4with_options(
        self,
        request: main_models.ListRulesV4Request,
        runtime: RuntimeOptions,
    ) -> main_models.ListRulesV4Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.business_name):
            body['BusinessName'] = request.business_name
        if not DaraCore.is_null(request.business_range):
            body['BusinessRange'] = request.business_range
        if not DaraCore.is_null(request.category_name):
            body['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.count_total):
            body['CountTotal'] = request.count_total
        if not DaraCore.is_null(request.create_empid):
            body['CreateEmpid'] = request.create_empid
        if not DaraCore.is_null(request.create_user_id):
            body['CreateUserId'] = request.create_user_id
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.last_update_empid):
            body['LastUpdateEmpid'] = request.last_update_empid
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.require_infos):
            body['RequireInfos'] = request.require_infos
        if not DaraCore.is_null(request.rid):
            body['Rid'] = request.rid
        if not DaraCore.is_null(request.rule_id_or_rule_name):
            body['RuleIdOrRuleName'] = request.rule_id_or_rule_name
        if not DaraCore.is_null(request.rule_score_single_type):
            body['RuleScoreSingleType'] = request.rule_score_single_type
        if not DaraCore.is_null(request.rule_type):
            body['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.scheme_id):
            body['SchemeId'] = request.scheme_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.type_name):
            body['TypeName'] = request.type_name
        if not DaraCore.is_null(request.update_end_time):
            body['UpdateEndTime'] = request.update_end_time
        if not DaraCore.is_null(request.update_start_time):
            body['UpdateStartTime'] = request.update_start_time
        if not DaraCore.is_null(request.update_user_id):
            body['UpdateUserId'] = request.update_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRulesV4',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRulesV4Response(),
            self.call_api(params, req, runtime)
        )

    async def list_rules_v4with_options_async(
        self,
        request: main_models.ListRulesV4Request,
        runtime: RuntimeOptions,
    ) -> main_models.ListRulesV4Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.business_name):
            body['BusinessName'] = request.business_name
        if not DaraCore.is_null(request.business_range):
            body['BusinessRange'] = request.business_range
        if not DaraCore.is_null(request.category_name):
            body['CategoryName'] = request.category_name
        if not DaraCore.is_null(request.count_total):
            body['CountTotal'] = request.count_total
        if not DaraCore.is_null(request.create_empid):
            body['CreateEmpid'] = request.create_empid
        if not DaraCore.is_null(request.create_user_id):
            body['CreateUserId'] = request.create_user_id
        if not DaraCore.is_null(request.current_page):
            body['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.last_update_empid):
            body['LastUpdateEmpid'] = request.last_update_empid
        if not DaraCore.is_null(request.page_number):
            body['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            body['PageSize'] = request.page_size
        if not DaraCore.is_null(request.require_infos):
            body['RequireInfos'] = request.require_infos
        if not DaraCore.is_null(request.rid):
            body['Rid'] = request.rid
        if not DaraCore.is_null(request.rule_id_or_rule_name):
            body['RuleIdOrRuleName'] = request.rule_id_or_rule_name
        if not DaraCore.is_null(request.rule_score_single_type):
            body['RuleScoreSingleType'] = request.rule_score_single_type
        if not DaraCore.is_null(request.rule_type):
            body['RuleType'] = request.rule_type
        if not DaraCore.is_null(request.scheme_id):
            body['SchemeId'] = request.scheme_id
        if not DaraCore.is_null(request.source_type):
            body['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        if not DaraCore.is_null(request.type_name):
            body['TypeName'] = request.type_name
        if not DaraCore.is_null(request.update_end_time):
            body['UpdateEndTime'] = request.update_end_time
        if not DaraCore.is_null(request.update_start_time):
            body['UpdateStartTime'] = request.update_start_time
        if not DaraCore.is_null(request.update_user_id):
            body['UpdateUserId'] = request.update_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListRulesV4',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRulesV4Response(),
            await self.call_api_async(params, req, runtime)
        )

    def list_rules_v4(
        self,
        request: main_models.ListRulesV4Request,
    ) -> main_models.ListRulesV4Response:
        runtime = RuntimeOptions()
        return self.list_rules_v4with_options(request, runtime)

    async def list_rules_v4_async(
        self,
        request: main_models.ListRulesV4Request,
    ) -> main_models.ListRulesV4Response:
        runtime = RuntimeOptions()
        return await self.list_rules_v4with_options_async(request, runtime)

    def list_scheme_task_config_with_options(
        self,
        request: main_models.ListSchemeTaskConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSchemeTaskConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSchemeTaskConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSchemeTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scheme_task_config_with_options_async(
        self,
        request: main_models.ListSchemeTaskConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSchemeTaskConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSchemeTaskConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSchemeTaskConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scheme_task_config(
        self,
        request: main_models.ListSchemeTaskConfigRequest,
    ) -> main_models.ListSchemeTaskConfigResponse:
        runtime = RuntimeOptions()
        return self.list_scheme_task_config_with_options(request, runtime)

    async def list_scheme_task_config_async(
        self,
        request: main_models.ListSchemeTaskConfigRequest,
    ) -> main_models.ListSchemeTaskConfigResponse:
        runtime = RuntimeOptions()
        return await self.list_scheme_task_config_with_options_async(request, runtime)

    def list_session_group_with_options(
        self,
        request: main_models.ListSessionGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSessionGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSessionGroup',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSessionGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_session_group_with_options_async(
        self,
        request: main_models.ListSessionGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSessionGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSessionGroup',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSessionGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_session_group(
        self,
        request: main_models.ListSessionGroupRequest,
    ) -> main_models.ListSessionGroupResponse:
        runtime = RuntimeOptions()
        return self.list_session_group_with_options(request, runtime)

    async def list_session_group_async(
        self,
        request: main_models.ListSessionGroupRequest,
    ) -> main_models.ListSessionGroupResponse:
        runtime = RuntimeOptions()
        return await self.list_session_group_with_options_async(request, runtime)

    def list_skill_group_config_with_options(
        self,
        request: main_models.ListSkillGroupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillGroupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkillGroupConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillGroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skill_group_config_with_options_async(
        self,
        request: main_models.ListSkillGroupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillGroupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkillGroupConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillGroupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skill_group_config(
        self,
        request: main_models.ListSkillGroupConfigRequest,
    ) -> main_models.ListSkillGroupConfigResponse:
        runtime = RuntimeOptions()
        return self.list_skill_group_config_with_options(request, runtime)

    async def list_skill_group_config_async(
        self,
        request: main_models.ListSkillGroupConfigRequest,
    ) -> main_models.ListSkillGroupConfigResponse:
        runtime = RuntimeOptions()
        return await self.list_skill_group_config_with_options_async(request, runtime)

    def list_task_assign_rules_with_options(
        self,
        request: main_models.ListTaskAssignRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTaskAssignRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTaskAssignRules',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTaskAssignRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_assign_rules_with_options_async(
        self,
        request: main_models.ListTaskAssignRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTaskAssignRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTaskAssignRules',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTaskAssignRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_assign_rules(
        self,
        request: main_models.ListTaskAssignRulesRequest,
    ) -> main_models.ListTaskAssignRulesResponse:
        runtime = RuntimeOptions()
        return self.list_task_assign_rules_with_options(request, runtime)

    async def list_task_assign_rules_async(
        self,
        request: main_models.ListTaskAssignRulesRequest,
    ) -> main_models.ListTaskAssignRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_task_assign_rules_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_warning_config_with_options(
        self,
        request: main_models.ListWarningConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWarningConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWarningConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWarningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_warning_config_with_options_async(
        self,
        request: main_models.ListWarningConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWarningConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWarningConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWarningConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_warning_config(
        self,
        request: main_models.ListWarningConfigRequest,
    ) -> main_models.ListWarningConfigResponse:
        runtime = RuntimeOptions()
        return self.list_warning_config_with_options(request, runtime)

    async def list_warning_config_async(
        self,
        request: main_models.ListWarningConfigRequest,
    ) -> main_models.ListWarningConfigResponse:
        runtime = RuntimeOptions()
        return await self.list_warning_config_with_options_async(request, runtime)

    def list_warning_strategy_config_with_options(
        self,
        request: main_models.ListWarningStrategyConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWarningStrategyConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWarningStrategyConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWarningStrategyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_warning_strategy_config_with_options_async(
        self,
        request: main_models.ListWarningStrategyConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListWarningStrategyConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWarningStrategyConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWarningStrategyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_warning_strategy_config(
        self,
        request: main_models.ListWarningStrategyConfigRequest,
    ) -> main_models.ListWarningStrategyConfigResponse:
        runtime = RuntimeOptions()
        return self.list_warning_strategy_config_with_options(request, runtime)

    async def list_warning_strategy_config_async(
        self,
        request: main_models.ListWarningStrategyConfigRequest,
    ) -> main_models.ListWarningStrategyConfigResponse:
        runtime = RuntimeOptions()
        return await self.list_warning_strategy_config_with_options_async(request, runtime)

    def revert_assigned_session_with_options(
        self,
        request: main_models.RevertAssignedSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevertAssignedSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevertAssignedSession',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevertAssignedSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def revert_assigned_session_with_options_async(
        self,
        request: main_models.RevertAssignedSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevertAssignedSessionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevertAssignedSession',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevertAssignedSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revert_assigned_session(
        self,
        request: main_models.RevertAssignedSessionRequest,
    ) -> main_models.RevertAssignedSessionResponse:
        runtime = RuntimeOptions()
        return self.revert_assigned_session_with_options(request, runtime)

    async def revert_assigned_session_async(
        self,
        request: main_models.RevertAssignedSessionRequest,
    ) -> main_models.RevertAssignedSessionResponse:
        runtime = RuntimeOptions()
        return await self.revert_assigned_session_with_options_async(request, runtime)

    def revert_assigned_session_group_with_options(
        self,
        request: main_models.RevertAssignedSessionGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevertAssignedSessionGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevertAssignedSessionGroup',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevertAssignedSessionGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def revert_assigned_session_group_with_options_async(
        self,
        request: main_models.RevertAssignedSessionGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RevertAssignedSessionGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RevertAssignedSessionGroup',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevertAssignedSessionGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revert_assigned_session_group(
        self,
        request: main_models.RevertAssignedSessionGroupRequest,
    ) -> main_models.RevertAssignedSessionGroupResponse:
        runtime = RuntimeOptions()
        return self.revert_assigned_session_group_with_options(request, runtime)

    async def revert_assigned_session_group_async(
        self,
        request: main_models.RevertAssignedSessionGroupRequest,
    ) -> main_models.RevertAssignedSessionGroupResponse:
        runtime = RuntimeOptions()
        return await self.revert_assigned_session_group_with_options_async(request, runtime)

    def save_config_data_set_with_options(
        self,
        request: main_models.SaveConfigDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveConfigDataSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveConfigDataSet',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveConfigDataSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_config_data_set_with_options_async(
        self,
        request: main_models.SaveConfigDataSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveConfigDataSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveConfigDataSet',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveConfigDataSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_config_data_set(
        self,
        request: main_models.SaveConfigDataSetRequest,
    ) -> main_models.SaveConfigDataSetResponse:
        runtime = RuntimeOptions()
        return self.save_config_data_set_with_options(request, runtime)

    async def save_config_data_set_async(
        self,
        request: main_models.SaveConfigDataSetRequest,
    ) -> main_models.SaveConfigDataSetResponse:
        runtime = RuntimeOptions()
        return await self.save_config_data_set_with_options_async(request, runtime)

    def submit_complaint_with_options(
        self,
        request: main_models.SubmitComplaintRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitComplaintResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitComplaint',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitComplaintResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_complaint_with_options_async(
        self,
        request: main_models.SubmitComplaintRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitComplaintResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitComplaint',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitComplaintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_complaint(
        self,
        request: main_models.SubmitComplaintRequest,
    ) -> main_models.SubmitComplaintResponse:
        runtime = RuntimeOptions()
        return self.submit_complaint_with_options(request, runtime)

    async def submit_complaint_async(
        self,
        request: main_models.SubmitComplaintRequest,
    ) -> main_models.SubmitComplaintResponse:
        runtime = RuntimeOptions()
        return await self.submit_complaint_with_options_async(request, runtime)

    def submit_precision_task_with_options(
        self,
        request: main_models.SubmitPrecisionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitPrecisionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitPrecisionTask',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitPrecisionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_precision_task_with_options_async(
        self,
        request: main_models.SubmitPrecisionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitPrecisionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitPrecisionTask',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitPrecisionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_precision_task(
        self,
        request: main_models.SubmitPrecisionTaskRequest,
    ) -> main_models.SubmitPrecisionTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_precision_task_with_options(request, runtime)

    async def submit_precision_task_async(
        self,
        request: main_models.SubmitPrecisionTaskRequest,
    ) -> main_models.SubmitPrecisionTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_precision_task_with_options_async(request, runtime)

    def submit_quality_check_task_with_options(
        self,
        request: main_models.SubmitQualityCheckTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitQualityCheckTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitQualityCheckTask',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitQualityCheckTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_quality_check_task_with_options_async(
        self,
        request: main_models.SubmitQualityCheckTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitQualityCheckTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitQualityCheckTask',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitQualityCheckTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_quality_check_task(
        self,
        request: main_models.SubmitQualityCheckTaskRequest,
    ) -> main_models.SubmitQualityCheckTaskResponse:
        runtime = RuntimeOptions()
        return self.submit_quality_check_task_with_options(request, runtime)

    async def submit_quality_check_task_async(
        self,
        request: main_models.SubmitQualityCheckTaskRequest,
    ) -> main_models.SubmitQualityCheckTaskResponse:
        runtime = RuntimeOptions()
        return await self.submit_quality_check_task_with_options_async(request, runtime)

    def submit_review_info_with_options(
        self,
        request: main_models.SubmitReviewInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitReviewInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitReviewInfo',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitReviewInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_review_info_with_options_async(
        self,
        request: main_models.SubmitReviewInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitReviewInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitReviewInfo',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitReviewInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_review_info(
        self,
        request: main_models.SubmitReviewInfoRequest,
    ) -> main_models.SubmitReviewInfoResponse:
        runtime = RuntimeOptions()
        return self.submit_review_info_with_options(request, runtime)

    async def submit_review_info_async(
        self,
        request: main_models.SubmitReviewInfoRequest,
    ) -> main_models.SubmitReviewInfoResponse:
        runtime = RuntimeOptions()
        return await self.submit_review_info_with_options_async(request, runtime)

    def submit_review_info_v4with_options(
        self,
        request: main_models.SubmitReviewInfoV4Request,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitReviewInfoV4Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            body['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            body['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitReviewInfoV4',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitReviewInfoV4Response(),
            self.call_api(params, req, runtime)
        )

    async def submit_review_info_v4with_options_async(
        self,
        request: main_models.SubmitReviewInfoV4Request,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitReviewInfoV4Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            body['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            body['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SubmitReviewInfoV4',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitReviewInfoV4Response(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_review_info_v4(
        self,
        request: main_models.SubmitReviewInfoV4Request,
    ) -> main_models.SubmitReviewInfoV4Response:
        runtime = RuntimeOptions()
        return self.submit_review_info_v4with_options(request, runtime)

    async def submit_review_info_v4_async(
        self,
        request: main_models.SubmitReviewInfoV4Request,
    ) -> main_models.SubmitReviewInfoV4Response:
        runtime = RuntimeOptions()
        return await self.submit_review_info_v4with_options_async(request, runtime)

    def sync_quality_check_with_options(
        self,
        request: main_models.SyncQualityCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncQualityCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncQualityCheck',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncQualityCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_quality_check_with_options_async(
        self,
        request: main_models.SyncQualityCheckRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncQualityCheckResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncQualityCheck',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncQualityCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_quality_check(
        self,
        request: main_models.SyncQualityCheckRequest,
    ) -> main_models.SyncQualityCheckResponse:
        runtime = RuntimeOptions()
        return self.sync_quality_check_with_options(request, runtime)

    async def sync_quality_check_async(
        self,
        request: main_models.SyncQualityCheckRequest,
    ) -> main_models.SyncQualityCheckResponse:
        runtime = RuntimeOptions()
        return await self.sync_quality_check_with_options_async(request, runtime)

    def test_rule_v4with_options(
        self,
        request: main_models.TestRuleV4Request,
        runtime: RuntimeOptions,
    ) -> main_models.TestRuleV4Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.is_scheme_data):
            body['IsSchemeData'] = request.is_scheme_data
        if not DaraCore.is_null(request.test_json):
            body['TestJson'] = request.test_json
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TestRuleV4',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TestRuleV4Response(),
            self.call_api(params, req, runtime)
        )

    async def test_rule_v4with_options_async(
        self,
        request: main_models.TestRuleV4Request,
        runtime: RuntimeOptions,
    ) -> main_models.TestRuleV4Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.is_scheme_data):
            body['IsSchemeData'] = request.is_scheme_data
        if not DaraCore.is_null(request.test_json):
            body['TestJson'] = request.test_json
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TestRuleV4',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TestRuleV4Response(),
            await self.call_api_async(params, req, runtime)
        )

    def test_rule_v4(
        self,
        request: main_models.TestRuleV4Request,
    ) -> main_models.TestRuleV4Response:
        runtime = RuntimeOptions()
        return self.test_rule_v4with_options(request, runtime)

    async def test_rule_v4_async(
        self,
        request: main_models.TestRuleV4Request,
    ) -> main_models.TestRuleV4Response:
        runtime = RuntimeOptions()
        return await self.test_rule_v4with_options_async(request, runtime)

    def update_asr_vocab_with_options(
        self,
        request: main_models.UpdateAsrVocabRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAsrVocabResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAsrVocab',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAsrVocabResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_asr_vocab_with_options_async(
        self,
        request: main_models.UpdateAsrVocabRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAsrVocabResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAsrVocab',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAsrVocabResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_asr_vocab(
        self,
        request: main_models.UpdateAsrVocabRequest,
    ) -> main_models.UpdateAsrVocabResponse:
        runtime = RuntimeOptions()
        return self.update_asr_vocab_with_options(request, runtime)

    async def update_asr_vocab_async(
        self,
        request: main_models.UpdateAsrVocabRequest,
    ) -> main_models.UpdateAsrVocabResponse:
        runtime = RuntimeOptions()
        return await self.update_asr_vocab_with_options_async(request, runtime)

    def update_check_type_to_scheme_with_options(
        self,
        request: main_models.UpdateCheckTypeToSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCheckTypeToSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCheckTypeToScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCheckTypeToSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_check_type_to_scheme_with_options_async(
        self,
        request: main_models.UpdateCheckTypeToSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateCheckTypeToSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateCheckTypeToScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateCheckTypeToSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_check_type_to_scheme(
        self,
        request: main_models.UpdateCheckTypeToSchemeRequest,
    ) -> main_models.UpdateCheckTypeToSchemeResponse:
        runtime = RuntimeOptions()
        return self.update_check_type_to_scheme_with_options(request, runtime)

    async def update_check_type_to_scheme_async(
        self,
        request: main_models.UpdateCheckTypeToSchemeRequest,
    ) -> main_models.UpdateCheckTypeToSchemeResponse:
        runtime = RuntimeOptions()
        return await self.update_check_type_to_scheme_with_options_async(request, runtime)

    def update_quality_check_data_with_options(
        self,
        request: main_models.UpdateQualityCheckDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQualityCheckDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQualityCheckData',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQualityCheckDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quality_check_data_with_options_async(
        self,
        request: main_models.UpdateQualityCheckDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQualityCheckDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQualityCheckData',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQualityCheckDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quality_check_data(
        self,
        request: main_models.UpdateQualityCheckDataRequest,
    ) -> main_models.UpdateQualityCheckDataResponse:
        runtime = RuntimeOptions()
        return self.update_quality_check_data_with_options(request, runtime)

    async def update_quality_check_data_async(
        self,
        request: main_models.UpdateQualityCheckDataRequest,
    ) -> main_models.UpdateQualityCheckDataResponse:
        runtime = RuntimeOptions()
        return await self.update_quality_check_data_with_options_async(request, runtime)

    def update_quality_check_scheme_with_options(
        self,
        request: main_models.UpdateQualityCheckSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQualityCheckSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQualityCheckScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQualityCheckSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_quality_check_scheme_with_options_async(
        self,
        request: main_models.UpdateQualityCheckSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateQualityCheckSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateQualityCheckScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateQualityCheckSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_quality_check_scheme(
        self,
        request: main_models.UpdateQualityCheckSchemeRequest,
    ) -> main_models.UpdateQualityCheckSchemeResponse:
        runtime = RuntimeOptions()
        return self.update_quality_check_scheme_with_options(request, runtime)

    async def update_quality_check_scheme_async(
        self,
        request: main_models.UpdateQualityCheckSchemeRequest,
    ) -> main_models.UpdateQualityCheckSchemeResponse:
        runtime = RuntimeOptions()
        return await self.update_quality_check_scheme_with_options_async(request, runtime)

    def update_rule_with_options(
        self,
        request: main_models.UpdateRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRule',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rule_with_options_async(
        self,
        request: main_models.UpdateRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRule',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rule(
        self,
        request: main_models.UpdateRuleRequest,
    ) -> main_models.UpdateRuleResponse:
        runtime = RuntimeOptions()
        return self.update_rule_with_options(request, runtime)

    async def update_rule_async(
        self,
        request: main_models.UpdateRuleRequest,
    ) -> main_models.UpdateRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_rule_with_options_async(request, runtime)

    def update_rule_by_id_with_options(
        self,
        request: main_models.UpdateRuleByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRuleByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.is_copy):
            body['IsCopy'] = request.is_copy
        if not DaraCore.is_null(request.json_str_for_rule):
            body['JsonStrForRule'] = request.json_str_for_rule
        if not DaraCore.is_null(request.return_related_schemes):
            body['ReturnRelatedSchemes'] = request.return_related_schemes
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRuleById',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRuleByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rule_by_id_with_options_async(
        self,
        request: main_models.UpdateRuleByIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRuleByIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.is_copy):
            body['IsCopy'] = request.is_copy
        if not DaraCore.is_null(request.json_str_for_rule):
            body['JsonStrForRule'] = request.json_str_for_rule
        if not DaraCore.is_null(request.return_related_schemes):
            body['ReturnRelatedSchemes'] = request.return_related_schemes
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRuleById',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRuleByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rule_by_id(
        self,
        request: main_models.UpdateRuleByIdRequest,
    ) -> main_models.UpdateRuleByIdResponse:
        runtime = RuntimeOptions()
        return self.update_rule_by_id_with_options(request, runtime)

    async def update_rule_by_id_async(
        self,
        request: main_models.UpdateRuleByIdRequest,
    ) -> main_models.UpdateRuleByIdResponse:
        runtime = RuntimeOptions()
        return await self.update_rule_by_id_with_options_async(request, runtime)

    def update_rule_to_scheme_with_options(
        self,
        request: main_models.UpdateRuleToSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRuleToSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRuleToScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRuleToSchemeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rule_to_scheme_with_options_async(
        self,
        request: main_models.UpdateRuleToSchemeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRuleToSchemeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRuleToScheme',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRuleToSchemeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rule_to_scheme(
        self,
        request: main_models.UpdateRuleToSchemeRequest,
    ) -> main_models.UpdateRuleToSchemeResponse:
        runtime = RuntimeOptions()
        return self.update_rule_to_scheme_with_options(request, runtime)

    async def update_rule_to_scheme_async(
        self,
        request: main_models.UpdateRuleToSchemeRequest,
    ) -> main_models.UpdateRuleToSchemeResponse:
        runtime = RuntimeOptions()
        return await self.update_rule_to_scheme_with_options_async(request, runtime)

    def update_rule_v4with_options(
        self,
        request: main_models.UpdateRuleV4Request,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRuleV4Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.json_str_for_rule):
            body['JsonStrForRule'] = request.json_str_for_rule
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRuleV4',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRuleV4Response(),
            self.call_api(params, req, runtime)
        )

    async def update_rule_v4with_options_async(
        self,
        request: main_models.UpdateRuleV4Request,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRuleV4Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        body = {}
        if not DaraCore.is_null(request.json_str_for_rule):
            body['JsonStrForRule'] = request.json_str_for_rule
        if not DaraCore.is_null(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRuleV4',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRuleV4Response(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rule_v4(
        self,
        request: main_models.UpdateRuleV4Request,
    ) -> main_models.UpdateRuleV4Response:
        runtime = RuntimeOptions()
        return self.update_rule_v4with_options(request, runtime)

    async def update_rule_v4_async(
        self,
        request: main_models.UpdateRuleV4Request,
    ) -> main_models.UpdateRuleV4Response:
        runtime = RuntimeOptions()
        return await self.update_rule_v4with_options_async(request, runtime)

    def update_scheme_task_config_with_options(
        self,
        request: main_models.UpdateSchemeTaskConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSchemeTaskConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSchemeTaskConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSchemeTaskConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scheme_task_config_with_options_async(
        self,
        request: main_models.UpdateSchemeTaskConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSchemeTaskConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['jsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSchemeTaskConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSchemeTaskConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scheme_task_config(
        self,
        request: main_models.UpdateSchemeTaskConfigRequest,
    ) -> main_models.UpdateSchemeTaskConfigResponse:
        runtime = RuntimeOptions()
        return self.update_scheme_task_config_with_options(request, runtime)

    async def update_scheme_task_config_async(
        self,
        request: main_models.UpdateSchemeTaskConfigRequest,
    ) -> main_models.UpdateSchemeTaskConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_scheme_task_config_with_options_async(request, runtime)

    def update_skill_group_config_with_options(
        self,
        request: main_models.UpdateSkillGroupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillGroupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillGroupConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillGroupConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_skill_group_config_with_options_async(
        self,
        request: main_models.UpdateSkillGroupConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillGroupConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillGroupConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillGroupConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_skill_group_config(
        self,
        request: main_models.UpdateSkillGroupConfigRequest,
    ) -> main_models.UpdateSkillGroupConfigResponse:
        runtime = RuntimeOptions()
        return self.update_skill_group_config_with_options(request, runtime)

    async def update_skill_group_config_async(
        self,
        request: main_models.UpdateSkillGroupConfigRequest,
    ) -> main_models.UpdateSkillGroupConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_skill_group_config_with_options_async(request, runtime)

    def update_sync_quality_check_data_with_options(
        self,
        request: main_models.UpdateSyncQualityCheckDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSyncQualityCheckDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSyncQualityCheckData',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSyncQualityCheckDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sync_quality_check_data_with_options_async(
        self,
        request: main_models.UpdateSyncQualityCheckDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSyncQualityCheckDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSyncQualityCheckData',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSyncQualityCheckDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sync_quality_check_data(
        self,
        request: main_models.UpdateSyncQualityCheckDataRequest,
    ) -> main_models.UpdateSyncQualityCheckDataResponse:
        runtime = RuntimeOptions()
        return self.update_sync_quality_check_data_with_options(request, runtime)

    async def update_sync_quality_check_data_async(
        self,
        request: main_models.UpdateSyncQualityCheckDataRequest,
    ) -> main_models.UpdateSyncQualityCheckDataResponse:
        runtime = RuntimeOptions()
        return await self.update_sync_quality_check_data_with_options_async(request, runtime)

    def update_task_assign_rule_with_options(
        self,
        request: main_models.UpdateTaskAssignRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTaskAssignRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTaskAssignRule',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTaskAssignRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_task_assign_rule_with_options_async(
        self,
        request: main_models.UpdateTaskAssignRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTaskAssignRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTaskAssignRule',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTaskAssignRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_task_assign_rule(
        self,
        request: main_models.UpdateTaskAssignRuleRequest,
    ) -> main_models.UpdateTaskAssignRuleResponse:
        runtime = RuntimeOptions()
        return self.update_task_assign_rule_with_options(request, runtime)

    async def update_task_assign_rule_async(
        self,
        request: main_models.UpdateTaskAssignRuleRequest,
    ) -> main_models.UpdateTaskAssignRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_task_assign_rule_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: main_models.UpdateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: main_models.UpdateUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUser',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: main_models.UpdateUserRequest,
    ) -> main_models.UpdateUserResponse:
        runtime = RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)

    def update_warning_config_with_options(
        self,
        request: main_models.UpdateWarningConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWarningConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWarningConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWarningConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_warning_config_with_options_async(
        self,
        request: main_models.UpdateWarningConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWarningConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWarningConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWarningConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_warning_config(
        self,
        request: main_models.UpdateWarningConfigRequest,
    ) -> main_models.UpdateWarningConfigResponse:
        runtime = RuntimeOptions()
        return self.update_warning_config_with_options(request, runtime)

    async def update_warning_config_async(
        self,
        request: main_models.UpdateWarningConfigRequest,
    ) -> main_models.UpdateWarningConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_warning_config_with_options_async(request, runtime)

    def update_warning_strategy_config_with_options(
        self,
        request: main_models.UpdateWarningStrategyConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWarningStrategyConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWarningStrategyConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWarningStrategyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_warning_strategy_config_with_options_async(
        self,
        request: main_models.UpdateWarningStrategyConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWarningStrategyConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWarningStrategyConfig',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWarningStrategyConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_warning_strategy_config(
        self,
        request: main_models.UpdateWarningStrategyConfigRequest,
    ) -> main_models.UpdateWarningStrategyConfigResponse:
        runtime = RuntimeOptions()
        return self.update_warning_strategy_config_with_options(request, runtime)

    async def update_warning_strategy_config_async(
        self,
        request: main_models.UpdateWarningStrategyConfigRequest,
    ) -> main_models.UpdateWarningStrategyConfigResponse:
        runtime = RuntimeOptions()
        return await self.update_warning_strategy_config_with_options_async(request, runtime)

    def upload_audio_data_with_options(
        self,
        request: main_models.UploadAudioDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadAudioDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadAudioData',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadAudioDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_audio_data_with_options_async(
        self,
        request: main_models.UploadAudioDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadAudioDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadAudioData',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadAudioDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_audio_data(
        self,
        request: main_models.UploadAudioDataRequest,
    ) -> main_models.UploadAudioDataResponse:
        runtime = RuntimeOptions()
        return self.upload_audio_data_with_options(request, runtime)

    async def upload_audio_data_async(
        self,
        request: main_models.UploadAudioDataRequest,
    ) -> main_models.UploadAudioDataResponse:
        runtime = RuntimeOptions()
        return await self.upload_audio_data_with_options_async(request, runtime)

    def upload_data_with_options(
        self,
        request: main_models.UploadDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadData',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_data_with_options_async(
        self,
        request: main_models.UploadDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadData',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_data(
        self,
        request: main_models.UploadDataRequest,
    ) -> main_models.UploadDataResponse:
        runtime = RuntimeOptions()
        return self.upload_data_with_options(request, runtime)

    async def upload_data_async(
        self,
        request: main_models.UploadDataRequest,
    ) -> main_models.UploadDataResponse:
        runtime = RuntimeOptions()
        return await self.upload_data_with_options_async(request, runtime)

    def upload_data_sync_with_options(
        self,
        request: main_models.UploadDataSyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadDataSyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadDataSync',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDataSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_data_sync_with_options_async(
        self,
        request: main_models.UploadDataSyncRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadDataSyncResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadDataSync',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDataSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_data_sync(
        self,
        request: main_models.UploadDataSyncRequest,
    ) -> main_models.UploadDataSyncResponse:
        runtime = RuntimeOptions()
        return self.upload_data_sync_with_options(request, runtime)

    async def upload_data_sync_async(
        self,
        request: main_models.UploadDataSyncRequest,
    ) -> main_models.UploadDataSyncResponse:
        runtime = RuntimeOptions()
        return await self.upload_data_sync_with_options_async(request, runtime)

    def upload_data_sync_for_llmwith_options(
        self,
        request: main_models.UploadDataSyncForLLMRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadDataSyncForLLMResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadDataSyncForLLM',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDataSyncForLLMResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_data_sync_for_llmwith_options_async(
        self,
        request: main_models.UploadDataSyncForLLMRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadDataSyncForLLMResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadDataSyncForLLM',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDataSyncForLLMResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_data_sync_for_llm(
        self,
        request: main_models.UploadDataSyncForLLMRequest,
    ) -> main_models.UploadDataSyncForLLMResponse:
        runtime = RuntimeOptions()
        return self.upload_data_sync_for_llmwith_options(request, runtime)

    async def upload_data_sync_for_llm_async(
        self,
        request: main_models.UploadDataSyncForLLMRequest,
    ) -> main_models.UploadDataSyncForLLMResponse:
        runtime = RuntimeOptions()
        return await self.upload_data_sync_for_llmwith_options_async(request, runtime)

    def upload_data_v4with_options(
        self,
        request: main_models.UploadDataV4Request,
        runtime: RuntimeOptions,
    ) -> main_models.UploadDataV4Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            body['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            body['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadDataV4',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDataV4Response(),
            self.call_api(params, req, runtime)
        )

    async def upload_data_v4with_options_async(
        self,
        request: main_models.UploadDataV4Request,
        runtime: RuntimeOptions,
    ) -> main_models.UploadDataV4Response:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            body['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            body['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UploadDataV4',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadDataV4Response(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_data_v4(
        self,
        request: main_models.UploadDataV4Request,
    ) -> main_models.UploadDataV4Response:
        runtime = RuntimeOptions()
        return self.upload_data_v4with_options(request, runtime)

    async def upload_data_v4_async(
        self,
        request: main_models.UploadDataV4Request,
    ) -> main_models.UploadDataV4Response:
        runtime = RuntimeOptions()
        return await self.upload_data_v4with_options_async(request, runtime)

    def upload_rule_with_options(
        self,
        request: main_models.UploadRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadRule',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_rule_with_options_async(
        self,
        request: main_models.UploadRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadRule',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_rule(
        self,
        request: main_models.UploadRuleRequest,
    ) -> main_models.UploadRuleResponse:
        runtime = RuntimeOptions()
        return self.upload_rule_with_options(request, runtime)

    async def upload_rule_async(
        self,
        request: main_models.UploadRuleRequest,
    ) -> main_models.UploadRuleResponse:
        runtime = RuntimeOptions()
        return await self.upload_rule_with_options_async(request, runtime)

    def verify_file_with_options(
        self,
        request: main_models.VerifyFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyFile',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_file_with_options_async(
        self,
        request: main_models.VerifyFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifyFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifyFile',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifyFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_file(
        self,
        request: main_models.VerifyFileRequest,
    ) -> main_models.VerifyFileResponse:
        runtime = RuntimeOptions()
        return self.verify_file_with_options(request, runtime)

    async def verify_file_async(
        self,
        request: main_models.VerifyFileRequest,
    ) -> main_models.VerifyFileResponse:
        runtime = RuntimeOptions()
        return await self.verify_file_with_options_async(request, runtime)

    def verify_sentence_with_options(
        self,
        request: main_models.VerifySentenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifySentenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifySentence',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifySentenceResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_sentence_with_options_async(
        self,
        request: main_models.VerifySentenceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.VerifySentenceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.base_me_agent_id):
            query['BaseMeAgentId'] = request.base_me_agent_id
        if not DaraCore.is_null(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'VerifySentence',
            version = '2019-01-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.VerifySentenceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_sentence(
        self,
        request: main_models.VerifySentenceRequest,
    ) -> main_models.VerifySentenceResponse:
        runtime = RuntimeOptions()
        return self.verify_sentence_with_options(request, runtime)

    async def verify_sentence_async(
        self,
        request: main_models.VerifySentenceRequest,
    ) -> main_models.VerifySentenceResponse:
        runtime = RuntimeOptions()
        return await self.verify_sentence_with_options_async(request, runtime)
