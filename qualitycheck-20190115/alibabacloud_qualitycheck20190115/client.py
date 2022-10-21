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
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.add_business_category_with_options(request, runtime)

    async def add_business_category_async(
        self,
        request: qualitycheck_20190115_models.AddBusinessCategoryRequest,
    ) -> qualitycheck_20190115_models.AddBusinessCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_business_category_with_options_async(request, runtime)

    def add_rule_category_with_options(
        self,
        request: qualitycheck_20190115_models.AddRuleCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AddRuleCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.add_rule_category_with_options(request, runtime)

    async def add_rule_category_async(
        self,
        request: qualitycheck_20190115_models.AddRuleCategoryRequest,
    ) -> qualitycheck_20190115_models.AddRuleCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_rule_category_with_options_async(request, runtime)

    def add_rule_v4with_options(
        self,
        request: qualitycheck_20190115_models.AddRuleV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AddRuleV4Response:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_copy):
            body['IsCopy'] = request.is_copy
        if not UtilClient.is_unset(request.json_str_for_rule):
            body['JsonStrForRule'] = request.json_str_for_rule
        req = open_api_models.OpenApiRequest(
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.is_copy):
            body['IsCopy'] = request.is_copy
        if not UtilClient.is_unset(request.json_str_for_rule):
            body['JsonStrForRule'] = request.json_str_for_rule
        req = open_api_models.OpenApiRequest(
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
        runtime = util_models.RuntimeOptions()
        return self.add_rule_v4with_options(request, runtime)

    async def add_rule_v4_async(
        self,
        request: qualitycheck_20190115_models.AddRuleV4Request,
    ) -> qualitycheck_20190115_models.AddRuleV4Response:
        runtime = util_models.RuntimeOptions()
        return await self.add_rule_v4with_options_async(request, runtime)

    def add_thesaurus_for_api_with_options(
        self,
        request: qualitycheck_20190115_models.AddThesaurusForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AddThesaurusForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddThesaurusForApi',
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
            qualitycheck_20190115_models.AddThesaurusForApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_thesaurus_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.AddThesaurusForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AddThesaurusForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddThesaurusForApi',
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
            qualitycheck_20190115_models.AddThesaurusForApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_thesaurus_for_api(
        self,
        request: qualitycheck_20190115_models.AddThesaurusForApiRequest,
    ) -> qualitycheck_20190115_models.AddThesaurusForApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_thesaurus_for_api_with_options(request, runtime)

    async def add_thesaurus_for_api_async(
        self,
        request: qualitycheck_20190115_models.AddThesaurusForApiRequest,
    ) -> qualitycheck_20190115_models.AddThesaurusForApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_thesaurus_for_api_with_options_async(request, runtime)

    def assign_reviewer_with_options(
        self,
        request: qualitycheck_20190115_models.AssignReviewerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AssignReviewerResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.assign_reviewer_with_options(request, runtime)

    async def assign_reviewer_async(
        self,
        request: qualitycheck_20190115_models.AssignReviewerRequest,
    ) -> qualitycheck_20190115_models.AssignReviewerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assign_reviewer_with_options_async(request, runtime)

    def assign_reviewer_by_session_group_with_options(
        self,
        request: qualitycheck_20190115_models.AssignReviewerBySessionGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AssignReviewerBySessionGroupResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.assign_reviewer_by_session_group_with_options(request, runtime)

    async def assign_reviewer_by_session_group_async(
        self,
        request: qualitycheck_20190115_models.AssignReviewerBySessionGroupRequest,
    ) -> qualitycheck_20190115_models.AssignReviewerBySessionGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.assign_reviewer_by_session_group_with_options_async(request, runtime)

    def batch_submit_review_info_with_options(
        self,
        request: qualitycheck_20190115_models.BatchSubmitReviewInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.BatchSubmitReviewInfoResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.batch_submit_review_info_with_options(request, runtime)

    async def batch_submit_review_info_async(
        self,
        request: qualitycheck_20190115_models.BatchSubmitReviewInfoRequest,
    ) -> qualitycheck_20190115_models.BatchSubmitReviewInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_submit_review_info_with_options_async(request, runtime)

    def create_asr_vocab_with_options(
        self,
        request: qualitycheck_20190115_models.CreateAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateAsrVocabResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.create_asr_vocab_with_options(request, runtime)

    async def create_asr_vocab_async(
        self,
        request: qualitycheck_20190115_models.CreateAsrVocabRequest,
    ) -> qualitycheck_20190115_models.CreateAsrVocabResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_asr_vocab_with_options_async(request, runtime)

    def create_check_type_to_scheme_with_options(
        self,
        request: qualitycheck_20190115_models.CreateCheckTypeToSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateCheckTypeToSchemeResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.create_check_type_to_scheme_with_options(request, runtime)

    async def create_check_type_to_scheme_async(
        self,
        request: qualitycheck_20190115_models.CreateCheckTypeToSchemeRequest,
    ) -> qualitycheck_20190115_models.CreateCheckTypeToSchemeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_check_type_to_scheme_with_options_async(request, runtime)

    def create_quality_check_scheme_with_options(
        self,
        request: qualitycheck_20190115_models.CreateQualityCheckSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateQualityCheckSchemeResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.create_quality_check_scheme_with_options(request, runtime)

    async def create_quality_check_scheme_async(
        self,
        request: qualitycheck_20190115_models.CreateQualityCheckSchemeRequest,
    ) -> qualitycheck_20190115_models.CreateQualityCheckSchemeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_quality_check_scheme_with_options_async(request, runtime)

    def create_scheme_task_config_with_options(
        self,
        request: qualitycheck_20190115_models.CreateSchemeTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateSchemeTaskConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.create_scheme_task_config_with_options(request, runtime)

    async def create_scheme_task_config_async(
        self,
        request: qualitycheck_20190115_models.CreateSchemeTaskConfigRequest,
    ) -> qualitycheck_20190115_models.CreateSchemeTaskConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scheme_task_config_with_options_async(request, runtime)

    def create_skill_group_config_with_options(
        self,
        request: qualitycheck_20190115_models.CreateSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateSkillGroupConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.create_skill_group_config_with_options(request, runtime)

    async def create_skill_group_config_async(
        self,
        request: qualitycheck_20190115_models.CreateSkillGroupConfigRequest,
    ) -> qualitycheck_20190115_models.CreateSkillGroupConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_skill_group_config_with_options_async(request, runtime)

    def create_task_assign_rule_with_options(
        self,
        request: qualitycheck_20190115_models.CreateTaskAssignRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateTaskAssignRuleResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.create_task_assign_rule_with_options(request, runtime)

    async def create_task_assign_rule_async(
        self,
        request: qualitycheck_20190115_models.CreateTaskAssignRuleRequest,
    ) -> qualitycheck_20190115_models.CreateTaskAssignRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_task_assign_rule_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: qualitycheck_20190115_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
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
            qualitycheck_20190115_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: qualitycheck_20190115_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
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
            qualitycheck_20190115_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        request: qualitycheck_20190115_models.CreateUserRequest,
    ) -> qualitycheck_20190115_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: qualitycheck_20190115_models.CreateUserRequest,
    ) -> qualitycheck_20190115_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def create_warning_config_with_options(
        self,
        request: qualitycheck_20190115_models.CreateWarningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateWarningConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.create_warning_config_with_options(request, runtime)

    async def create_warning_config_async(
        self,
        request: qualitycheck_20190115_models.CreateWarningConfigRequest,
    ) -> qualitycheck_20190115_models.CreateWarningConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_warning_config_with_options_async(request, runtime)

    def create_warning_strategy_config_with_options(
        self,
        request: qualitycheck_20190115_models.CreateWarningStrategyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateWarningStrategyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.create_warning_strategy_config_with_options(request, runtime)

    async def create_warning_strategy_config_async(
        self,
        request: qualitycheck_20190115_models.CreateWarningStrategyConfigRequest,
    ) -> qualitycheck_20190115_models.CreateWarningStrategyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_warning_strategy_config_with_options_async(request, runtime)

    def del_rule_category_with_options(
        self,
        request: qualitycheck_20190115_models.DelRuleCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DelRuleCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.del_rule_category_with_options(request, runtime)

    async def del_rule_category_async(
        self,
        request: qualitycheck_20190115_models.DelRuleCategoryRequest,
    ) -> qualitycheck_20190115_models.DelRuleCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.del_rule_category_with_options_async(request, runtime)

    def del_thesaurus_for_api_with_options(
        self,
        request: qualitycheck_20190115_models.DelThesaurusForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DelThesaurusForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelThesaurusForApi',
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
            qualitycheck_20190115_models.DelThesaurusForApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def del_thesaurus_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.DelThesaurusForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DelThesaurusForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelThesaurusForApi',
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
            qualitycheck_20190115_models.DelThesaurusForApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def del_thesaurus_for_api(
        self,
        request: qualitycheck_20190115_models.DelThesaurusForApiRequest,
    ) -> qualitycheck_20190115_models.DelThesaurusForApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.del_thesaurus_for_api_with_options(request, runtime)

    async def del_thesaurus_for_api_async(
        self,
        request: qualitycheck_20190115_models.DelThesaurusForApiRequest,
    ) -> qualitycheck_20190115_models.DelThesaurusForApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.del_thesaurus_for_api_with_options_async(request, runtime)

    def delete_asr_vocab_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteAsrVocabResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.delete_asr_vocab_with_options(request, runtime)

    async def delete_asr_vocab_async(
        self,
        request: qualitycheck_20190115_models.DeleteAsrVocabRequest,
    ) -> qualitycheck_20190115_models.DeleteAsrVocabResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_asr_vocab_with_options_async(request, runtime)

    def delete_business_category_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteBusinessCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteBusinessCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.delete_business_category_with_options(request, runtime)

    async def delete_business_category_async(
        self,
        request: qualitycheck_20190115_models.DeleteBusinessCategoryRequest,
    ) -> qualitycheck_20190115_models.DeleteBusinessCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_business_category_with_options_async(request, runtime)

    def delete_customization_config_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteCustomizationConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteCustomizationConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.delete_customization_config_with_options(request, runtime)

    async def delete_customization_config_async(
        self,
        request: qualitycheck_20190115_models.DeleteCustomizationConfigRequest,
    ) -> qualitycheck_20190115_models.DeleteCustomizationConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_customization_config_with_options_async(request, runtime)

    def delete_data_set_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteDataSetResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.delete_data_set_with_options(request, runtime)

    async def delete_data_set_async(
        self,
        request: qualitycheck_20190115_models.DeleteDataSetRequest,
    ) -> qualitycheck_20190115_models.DeleteDataSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_data_set_with_options_async(request, runtime)

    def delete_precision_task_with_options(
        self,
        request: qualitycheck_20190115_models.DeletePrecisionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeletePrecisionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.delete_precision_task_with_options(request, runtime)

    async def delete_precision_task_async(
        self,
        request: qualitycheck_20190115_models.DeletePrecisionTaskRequest,
    ) -> qualitycheck_20190115_models.DeletePrecisionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_precision_task_with_options_async(request, runtime)

    def delete_quality_check_scheme_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteQualityCheckSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteQualityCheckSchemeResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.delete_quality_check_scheme_with_options(request, runtime)

    async def delete_quality_check_scheme_async(
        self,
        request: qualitycheck_20190115_models.DeleteQualityCheckSchemeRequest,
    ) -> qualitycheck_20190115_models.DeleteQualityCheckSchemeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_quality_check_scheme_with_options_async(request, runtime)

    def delete_rule_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.force_delete):
            body['ForceDelete'] = request.force_delete
        if not UtilClient.is_unset(request.is_scheme_data):
            body['IsSchemeData'] = request.is_scheme_data
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.force_delete):
            body['ForceDelete'] = request.force_delete
        if not UtilClient.is_unset(request.is_scheme_data):
            body['IsSchemeData'] = request.is_scheme_data
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
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
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    async def delete_rule_async(
        self,
        request: qualitycheck_20190115_models.DeleteRuleRequest,
    ) -> qualitycheck_20190115_models.DeleteRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_with_options_async(request, runtime)

    def delete_rule_v4with_options(
        self,
        request: qualitycheck_20190115_models.DeleteRuleV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteRuleV4Response:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.force_delete):
            body['ForceDelete'] = request.force_delete
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.force_delete):
            body['ForceDelete'] = request.force_delete
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
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
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_v4with_options(request, runtime)

    async def delete_rule_v4_async(
        self,
        request: qualitycheck_20190115_models.DeleteRuleV4Request,
    ) -> qualitycheck_20190115_models.DeleteRuleV4Response:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rule_v4with_options_async(request, runtime)

    def delete_scheme_task_config_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteSchemeTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteSchemeTaskConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.delete_scheme_task_config_with_options(request, runtime)

    async def delete_scheme_task_config_async(
        self,
        request: qualitycheck_20190115_models.DeleteSchemeTaskConfigRequest,
    ) -> qualitycheck_20190115_models.DeleteSchemeTaskConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scheme_task_config_with_options_async(request, runtime)

    def delete_score_for_api_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteScoreForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScoreForApi',
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
            qualitycheck_20190115_models.DeleteScoreForApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_score_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteScoreForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScoreForApi',
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
            qualitycheck_20190115_models.DeleteScoreForApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_score_for_api(
        self,
        request: qualitycheck_20190115_models.DeleteScoreForApiRequest,
    ) -> qualitycheck_20190115_models.DeleteScoreForApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_score_for_api_with_options(request, runtime)

    async def delete_score_for_api_async(
        self,
        request: qualitycheck_20190115_models.DeleteScoreForApiRequest,
    ) -> qualitycheck_20190115_models.DeleteScoreForApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_score_for_api_with_options_async(request, runtime)

    def delete_skill_group_config_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteSkillGroupConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.delete_skill_group_config_with_options(request, runtime)

    async def delete_skill_group_config_async(
        self,
        request: qualitycheck_20190115_models.DeleteSkillGroupConfigRequest,
    ) -> qualitycheck_20190115_models.DeleteSkillGroupConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_skill_group_config_with_options_async(request, runtime)

    def delete_sub_score_for_api_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteSubScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteSubScoreForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubScoreForApi',
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
            qualitycheck_20190115_models.DeleteSubScoreForApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_sub_score_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteSubScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteSubScoreForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubScoreForApi',
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
            qualitycheck_20190115_models.DeleteSubScoreForApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_sub_score_for_api(
        self,
        request: qualitycheck_20190115_models.DeleteSubScoreForApiRequest,
    ) -> qualitycheck_20190115_models.DeleteSubScoreForApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_sub_score_for_api_with_options(request, runtime)

    async def delete_sub_score_for_api_async(
        self,
        request: qualitycheck_20190115_models.DeleteSubScoreForApiRequest,
    ) -> qualitycheck_20190115_models.DeleteSubScoreForApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_sub_score_for_api_with_options_async(request, runtime)

    def delete_task_assign_rule_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteTaskAssignRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteTaskAssignRuleResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.delete_task_assign_rule_with_options(request, runtime)

    async def delete_task_assign_rule_async(
        self,
        request: qualitycheck_20190115_models.DeleteTaskAssignRuleRequest,
    ) -> qualitycheck_20190115_models.DeleteTaskAssignRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_task_assign_rule_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
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
            qualitycheck_20190115_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
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
            qualitycheck_20190115_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        request: qualitycheck_20190115_models.DeleteUserRequest,
    ) -> qualitycheck_20190115_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: qualitycheck_20190115_models.DeleteUserRequest,
    ) -> qualitycheck_20190115_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def delete_warning_config_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteWarningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteWarningConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.delete_warning_config_with_options(request, runtime)

    async def delete_warning_config_async(
        self,
        request: qualitycheck_20190115_models.DeleteWarningConfigRequest,
    ) -> qualitycheck_20190115_models.DeleteWarningConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_warning_config_with_options_async(request, runtime)

    def delete_warning_strategy_config_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteWarningStrategyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteWarningStrategyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.delete_warning_strategy_config_with_options(request, runtime)

    async def delete_warning_strategy_config_async(
        self,
        request: qualitycheck_20190115_models.DeleteWarningStrategyConfigRequest,
    ) -> qualitycheck_20190115_models.DeleteWarningStrategyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_warning_strategy_config_with_options_async(request, runtime)

    def edit_thesaurus_for_api_with_options(
        self,
        request: qualitycheck_20190115_models.EditThesaurusForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.EditThesaurusForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditThesaurusForApi',
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
            qualitycheck_20190115_models.EditThesaurusForApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def edit_thesaurus_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.EditThesaurusForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.EditThesaurusForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditThesaurusForApi',
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
            qualitycheck_20190115_models.EditThesaurusForApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def edit_thesaurus_for_api(
        self,
        request: qualitycheck_20190115_models.EditThesaurusForApiRequest,
    ) -> qualitycheck_20190115_models.EditThesaurusForApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.edit_thesaurus_for_api_with_options(request, runtime)

    async def edit_thesaurus_for_api_async(
        self,
        request: qualitycheck_20190115_models.EditThesaurusForApiRequest,
    ) -> qualitycheck_20190115_models.EditThesaurusForApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.edit_thesaurus_for_api_with_options_async(request, runtime)

    def get_asr_vocab_with_options(
        self,
        request: qualitycheck_20190115_models.GetAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetAsrVocabResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.get_asr_vocab_with_options(request, runtime)

    async def get_asr_vocab_async(
        self,
        request: qualitycheck_20190115_models.GetAsrVocabRequest,
    ) -> qualitycheck_20190115_models.GetAsrVocabResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_asr_vocab_with_options_async(request, runtime)

    def get_business_category_list_with_options(
        self,
        request: qualitycheck_20190115_models.GetBusinessCategoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetBusinessCategoryListResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.get_business_category_list_with_options(request, runtime)

    async def get_business_category_list_async(
        self,
        request: qualitycheck_20190115_models.GetBusinessCategoryListRequest,
    ) -> qualitycheck_20190115_models.GetBusinessCategoryListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_business_category_list_with_options_async(request, runtime)

    def get_customization_config_list_with_options(
        self,
        request: qualitycheck_20190115_models.GetCustomizationConfigListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetCustomizationConfigListResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.get_customization_config_list_with_options(request, runtime)

    async def get_customization_config_list_async(
        self,
        request: qualitycheck_20190115_models.GetCustomizationConfigListRequest,
    ) -> qualitycheck_20190115_models.GetCustomizationConfigListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_customization_config_list_with_options_async(request, runtime)

    def get_hit_result_with_options(
        self,
        request: qualitycheck_20190115_models.GetHitResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetHitResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHitResult',
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
            qualitycheck_20190115_models.GetHitResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hit_result_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetHitResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetHitResultResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHitResult',
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
            qualitycheck_20190115_models.GetHitResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_hit_result(
        self,
        request: qualitycheck_20190115_models.GetHitResultRequest,
    ) -> qualitycheck_20190115_models.GetHitResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hit_result_with_options(request, runtime)

    async def get_hit_result_async(
        self,
        request: qualitycheck_20190115_models.GetHitResultRequest,
    ) -> qualitycheck_20190115_models.GetHitResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hit_result_with_options_async(request, runtime)

    def get_next_result_to_verify_with_options(
        self,
        request: qualitycheck_20190115_models.GetNextResultToVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetNextResultToVerifyResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.get_next_result_to_verify_with_options(request, runtime)

    async def get_next_result_to_verify_async(
        self,
        request: qualitycheck_20190115_models.GetNextResultToVerifyRequest,
    ) -> qualitycheck_20190115_models.GetNextResultToVerifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_next_result_to_verify_with_options_async(request, runtime)

    def get_precision_task_with_options(
        self,
        request: qualitycheck_20190115_models.GetPrecisionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetPrecisionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.get_precision_task_with_options(request, runtime)

    async def get_precision_task_async(
        self,
        request: qualitycheck_20190115_models.GetPrecisionTaskRequest,
    ) -> qualitycheck_20190115_models.GetPrecisionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_precision_task_with_options_async(request, runtime)

    def get_quality_check_scheme_with_options(
        self,
        request: qualitycheck_20190115_models.GetQualityCheckSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetQualityCheckSchemeResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.get_quality_check_scheme_with_options(request, runtime)

    async def get_quality_check_scheme_async(
        self,
        request: qualitycheck_20190115_models.GetQualityCheckSchemeRequest,
    ) -> qualitycheck_20190115_models.GetQualityCheckSchemeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_quality_check_scheme_with_options_async(request, runtime)

    def get_result_with_options(
        self,
        request: qualitycheck_20190115_models.GetResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetResultResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.get_result_with_options(request, runtime)

    async def get_result_async(
        self,
        request: qualitycheck_20190115_models.GetResultRequest,
    ) -> qualitycheck_20190115_models.GetResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_result_with_options_async(request, runtime)

    def get_result_callback_with_options(
        self,
        request: qualitycheck_20190115_models.GetResultCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetResultCallbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResultCallback',
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
            qualitycheck_20190115_models.GetResultCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_result_callback_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetResultCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetResultCallbackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResultCallback',
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
            qualitycheck_20190115_models.GetResultCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_result_callback(
        self,
        request: qualitycheck_20190115_models.GetResultCallbackRequest,
    ) -> qualitycheck_20190115_models.GetResultCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_result_callback_with_options(request, runtime)

    async def get_result_callback_async(
        self,
        request: qualitycheck_20190115_models.GetResultCallbackRequest,
    ) -> qualitycheck_20190115_models.GetResultCallbackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_result_callback_with_options_async(request, runtime)

    def get_result_to_review_with_options(
        self,
        request: qualitycheck_20190115_models.GetResultToReviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetResultToReviewResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.get_result_to_review_with_options(request, runtime)

    async def get_result_to_review_async(
        self,
        request: qualitycheck_20190115_models.GetResultToReviewRequest,
    ) -> qualitycheck_20190115_models.GetResultToReviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_result_to_review_with_options_async(request, runtime)

    def get_rule_with_options(
        self,
        request: qualitycheck_20190115_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.get_rule_with_options(request, runtime)

    async def get_rule_async(
        self,
        request: qualitycheck_20190115_models.GetRuleRequest,
    ) -> qualitycheck_20190115_models.GetRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_with_options_async(request, runtime)

    def get_rule_by_id_with_options(
        self,
        request: qualitycheck_20190115_models.GetRuleByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleByIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
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
        runtime = util_models.RuntimeOptions()
        return self.get_rule_by_id_with_options(request, runtime)

    async def get_rule_by_id_async(
        self,
        request: qualitycheck_20190115_models.GetRuleByIdRequest,
    ) -> qualitycheck_20190115_models.GetRuleByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_by_id_with_options_async(request, runtime)

    def get_rule_category_with_options(
        self,
        request: qualitycheck_20190115_models.GetRuleCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.get_rule_category_with_options(request, runtime)

    async def get_rule_category_async(
        self,
        request: qualitycheck_20190115_models.GetRuleCategoryRequest,
    ) -> qualitycheck_20190115_models.GetRuleCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_category_with_options_async(request, runtime)

    def get_rule_detail_with_options(
        self,
        request: qualitycheck_20190115_models.GetRuleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleDetailResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.get_rule_detail_with_options(request, runtime)

    async def get_rule_detail_async(
        self,
        request: qualitycheck_20190115_models.GetRuleDetailRequest,
    ) -> qualitycheck_20190115_models.GetRuleDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_detail_with_options_async(request, runtime)

    def get_rule_v4with_options(
        self,
        request: qualitycheck_20190115_models.GetRuleV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleV4Response:
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
        runtime = util_models.RuntimeOptions()
        return self.get_rule_v4with_options(request, runtime)

    async def get_rule_v4_async(
        self,
        request: qualitycheck_20190115_models.GetRuleV4Request,
    ) -> qualitycheck_20190115_models.GetRuleV4Response:
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_v4with_options_async(request, runtime)

    def get_rules_count_list_with_options(
        self,
        request: qualitycheck_20190115_models.GetRulesCountListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRulesCountListResponse:
        UtilClient.validate_model(request)
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
        UtilClient.validate_model(request)
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
        runtime = util_models.RuntimeOptions()
        return self.get_rules_count_list_with_options(request, runtime)

    async def get_rules_count_list_async(
        self,
        request: qualitycheck_20190115_models.GetRulesCountListRequest,
    ) -> qualitycheck_20190115_models.GetRulesCountListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rules_count_list_with_options_async(request, runtime)

    def get_score_info_with_options(
        self,
        request: qualitycheck_20190115_models.GetScoreInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetScoreInfoResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.get_score_info_with_options(request, runtime)

    async def get_score_info_async(
        self,
        request: qualitycheck_20190115_models.GetScoreInfoRequest,
    ) -> qualitycheck_20190115_models.GetScoreInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_score_info_with_options_async(request, runtime)

    def get_skill_group_config_with_options(
        self,
        request: qualitycheck_20190115_models.GetSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetSkillGroupConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.get_skill_group_config_with_options(request, runtime)

    async def get_skill_group_config_async(
        self,
        request: qualitycheck_20190115_models.GetSkillGroupConfigRequest,
    ) -> qualitycheck_20190115_models.GetSkillGroupConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_skill_group_config_with_options_async(request, runtime)

    def get_sync_result_with_options(
        self,
        request: qualitycheck_20190115_models.GetSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetSyncResultResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.get_sync_result_with_options(request, runtime)

    async def get_sync_result_async(
        self,
        request: qualitycheck_20190115_models.GetSyncResultRequest,
    ) -> qualitycheck_20190115_models.GetSyncResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_sync_result_with_options_async(request, runtime)

    def get_thesaurus_by_synonym_for_api_with_options(
        self,
        request: qualitycheck_20190115_models.GetThesaurusBySynonymForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetThesaurusBySynonymForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetThesaurusBySynonymForApi',
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
            qualitycheck_20190115_models.GetThesaurusBySynonymForApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_thesaurus_by_synonym_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetThesaurusBySynonymForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetThesaurusBySynonymForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetThesaurusBySynonymForApi',
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
            qualitycheck_20190115_models.GetThesaurusBySynonymForApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_thesaurus_by_synonym_for_api(
        self,
        request: qualitycheck_20190115_models.GetThesaurusBySynonymForApiRequest,
    ) -> qualitycheck_20190115_models.GetThesaurusBySynonymForApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_thesaurus_by_synonym_for_api_with_options(request, runtime)

    async def get_thesaurus_by_synonym_for_api_async(
        self,
        request: qualitycheck_20190115_models.GetThesaurusBySynonymForApiRequest,
    ) -> qualitycheck_20190115_models.GetThesaurusBySynonymForApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_thesaurus_by_synonym_for_api_with_options_async(request, runtime)

    def get_warning_strategy_config_with_options(
        self,
        request: qualitycheck_20190115_models.GetWarningStrategyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetWarningStrategyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.get_warning_strategy_config_with_options(request, runtime)

    async def get_warning_strategy_config_async(
        self,
        request: qualitycheck_20190115_models.GetWarningStrategyConfigRequest,
    ) -> qualitycheck_20190115_models.GetWarningStrategyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_warning_strategy_config_with_options_async(request, runtime)

    def handle_complaint_with_options(
        self,
        request: qualitycheck_20190115_models.HandleComplaintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.HandleComplaintResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.handle_complaint_with_options(request, runtime)

    async def handle_complaint_async(
        self,
        request: qualitycheck_20190115_models.HandleComplaintRequest,
    ) -> qualitycheck_20190115_models.HandleComplaintResponse:
        runtime = util_models.RuntimeOptions()
        return await self.handle_complaint_with_options_async(request, runtime)

    def insert_score_for_api_with_options(
        self,
        request: qualitycheck_20190115_models.InsertScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.InsertScoreForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertScoreForApi',
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
            qualitycheck_20190115_models.InsertScoreForApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_score_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.InsertScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.InsertScoreForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertScoreForApi',
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
            qualitycheck_20190115_models.InsertScoreForApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_score_for_api(
        self,
        request: qualitycheck_20190115_models.InsertScoreForApiRequest,
    ) -> qualitycheck_20190115_models.InsertScoreForApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_score_for_api_with_options(request, runtime)

    async def insert_score_for_api_async(
        self,
        request: qualitycheck_20190115_models.InsertScoreForApiRequest,
    ) -> qualitycheck_20190115_models.InsertScoreForApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_score_for_api_with_options_async(request, runtime)

    def insert_sub_score_for_api_with_options(
        self,
        request: qualitycheck_20190115_models.InsertSubScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.InsertSubScoreForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertSubScoreForApi',
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
            qualitycheck_20190115_models.InsertSubScoreForApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def insert_sub_score_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.InsertSubScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.InsertSubScoreForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InsertSubScoreForApi',
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
            qualitycheck_20190115_models.InsertSubScoreForApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def insert_sub_score_for_api(
        self,
        request: qualitycheck_20190115_models.InsertSubScoreForApiRequest,
    ) -> qualitycheck_20190115_models.InsertSubScoreForApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.insert_sub_score_for_api_with_options(request, runtime)

    async def insert_sub_score_for_api_async(
        self,
        request: qualitycheck_20190115_models.InsertSubScoreForApiRequest,
    ) -> qualitycheck_20190115_models.InsertSubScoreForApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.insert_sub_score_for_api_with_options_async(request, runtime)

    def invalid_rule_with_options(
        self,
        request: qualitycheck_20190115_models.InvalidRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.InvalidRuleResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.invalid_rule_with_options(request, runtime)

    async def invalid_rule_async(
        self,
        request: qualitycheck_20190115_models.InvalidRuleRequest,
    ) -> qualitycheck_20190115_models.InvalidRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invalid_rule_with_options_async(request, runtime)

    def list_asr_vocab_with_options(
        self,
        request: qualitycheck_20190115_models.ListAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListAsrVocabResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.list_asr_vocab_with_options(request, runtime)

    async def list_asr_vocab_async(
        self,
        request: qualitycheck_20190115_models.ListAsrVocabRequest,
    ) -> qualitycheck_20190115_models.ListAsrVocabResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_asr_vocab_with_options_async(request, runtime)

    def list_business_spaces_with_options(
        self,
        request: qualitycheck_20190115_models.ListBusinessSpacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListBusinessSpacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBusinessSpaces',
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
            qualitycheck_20190115_models.ListBusinessSpacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_business_spaces_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListBusinessSpacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListBusinessSpacesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBusinessSpaces',
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
            qualitycheck_20190115_models.ListBusinessSpacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_business_spaces(
        self,
        request: qualitycheck_20190115_models.ListBusinessSpacesRequest,
    ) -> qualitycheck_20190115_models.ListBusinessSpacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_business_spaces_with_options(request, runtime)

    async def list_business_spaces_async(
        self,
        request: qualitycheck_20190115_models.ListBusinessSpacesRequest,
    ) -> qualitycheck_20190115_models.ListBusinessSpacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_business_spaces_with_options_async(request, runtime)

    def list_data_set_with_options(
        self,
        request: qualitycheck_20190115_models.ListDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListDataSetResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.list_data_set_with_options(request, runtime)

    async def list_data_set_async(
        self,
        request: qualitycheck_20190115_models.ListDataSetRequest,
    ) -> qualitycheck_20190115_models.ListDataSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_set_with_options_async(request, runtime)

    def list_hot_words_tasks_with_options(
        self,
        request: qualitycheck_20190115_models.ListHotWordsTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListHotWordsTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotWordsTasks',
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
            qualitycheck_20190115_models.ListHotWordsTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hot_words_tasks_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListHotWordsTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListHotWordsTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHotWordsTasks',
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
            qualitycheck_20190115_models.ListHotWordsTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hot_words_tasks(
        self,
        request: qualitycheck_20190115_models.ListHotWordsTasksRequest,
    ) -> qualitycheck_20190115_models.ListHotWordsTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_hot_words_tasks_with_options(request, runtime)

    async def list_hot_words_tasks_async(
        self,
        request: qualitycheck_20190115_models.ListHotWordsTasksRequest,
    ) -> qualitycheck_20190115_models.ListHotWordsTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_hot_words_tasks_with_options_async(request, runtime)

    def list_precision_task_with_options(
        self,
        request: qualitycheck_20190115_models.ListPrecisionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListPrecisionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.list_precision_task_with_options(request, runtime)

    async def list_precision_task_async(
        self,
        request: qualitycheck_20190115_models.ListPrecisionTaskRequest,
    ) -> qualitycheck_20190115_models.ListPrecisionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_precision_task_with_options_async(request, runtime)

    def list_quality_check_scheme_with_options(
        self,
        request: qualitycheck_20190115_models.ListQualityCheckSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListQualityCheckSchemeResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.list_quality_check_scheme_with_options(request, runtime)

    async def list_quality_check_scheme_async(
        self,
        request: qualitycheck_20190115_models.ListQualityCheckSchemeRequest,
    ) -> qualitycheck_20190115_models.ListQualityCheckSchemeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_quality_check_scheme_with_options_async(request, runtime)

    def list_roles_with_options(
        self,
        request: qualitycheck_20190115_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
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
            qualitycheck_20190115_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
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
            qualitycheck_20190115_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        request: qualitycheck_20190115_models.ListRolesRequest,
    ) -> qualitycheck_20190115_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    async def list_roles_async(
        self,
        request: qualitycheck_20190115_models.ListRolesRequest,
    ) -> qualitycheck_20190115_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_roles_with_options_async(request, runtime)

    def list_rules_with_options(
        self,
        request: qualitycheck_20190115_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListRulesResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.list_rules_with_options(request, runtime)

    async def list_rules_async(
        self,
        request: qualitycheck_20190115_models.ListRulesRequest,
    ) -> qualitycheck_20190115_models.ListRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_rules_with_options_async(request, runtime)

    def list_rules_v4with_options(
        self,
        request: qualitycheck_20190115_models.ListRulesV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListRulesV4Response:
        UtilClient.validate_model(request)
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
        UtilClient.validate_model(request)
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
        runtime = util_models.RuntimeOptions()
        return self.list_rules_v4with_options(request, runtime)

    async def list_rules_v4_async(
        self,
        request: qualitycheck_20190115_models.ListRulesV4Request,
    ) -> qualitycheck_20190115_models.ListRulesV4Response:
        runtime = util_models.RuntimeOptions()
        return await self.list_rules_v4with_options_async(request, runtime)

    def list_scheme_task_config_with_options(
        self,
        request: qualitycheck_20190115_models.ListSchemeTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListSchemeTaskConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.list_scheme_task_config_with_options(request, runtime)

    async def list_scheme_task_config_async(
        self,
        request: qualitycheck_20190115_models.ListSchemeTaskConfigRequest,
    ) -> qualitycheck_20190115_models.ListSchemeTaskConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_scheme_task_config_with_options_async(request, runtime)

    def list_session_group_with_options(
        self,
        request: qualitycheck_20190115_models.ListSessionGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListSessionGroupResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.list_session_group_with_options(request, runtime)

    async def list_session_group_async(
        self,
        request: qualitycheck_20190115_models.ListSessionGroupRequest,
    ) -> qualitycheck_20190115_models.ListSessionGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_session_group_with_options_async(request, runtime)

    def list_skill_group_config_with_options(
        self,
        request: qualitycheck_20190115_models.ListSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListSkillGroupConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.list_skill_group_config_with_options(request, runtime)

    async def list_skill_group_config_async(
        self,
        request: qualitycheck_20190115_models.ListSkillGroupConfigRequest,
    ) -> qualitycheck_20190115_models.ListSkillGroupConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_skill_group_config_with_options_async(request, runtime)

    def list_task_assign_rules_with_options(
        self,
        request: qualitycheck_20190115_models.ListTaskAssignRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListTaskAssignRulesResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.list_task_assign_rules_with_options(request, runtime)

    async def list_task_assign_rules_async(
        self,
        request: qualitycheck_20190115_models.ListTaskAssignRulesRequest,
    ) -> qualitycheck_20190115_models.ListTaskAssignRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_task_assign_rules_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: qualitycheck_20190115_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: qualitycheck_20190115_models.ListUsersRequest,
    ) -> qualitycheck_20190115_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_warning_config_with_options(
        self,
        request: qualitycheck_20190115_models.ListWarningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListWarningConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.list_warning_config_with_options(request, runtime)

    async def list_warning_config_async(
        self,
        request: qualitycheck_20190115_models.ListWarningConfigRequest,
    ) -> qualitycheck_20190115_models.ListWarningConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_warning_config_with_options_async(request, runtime)

    def list_warning_strategy_config_with_options(
        self,
        request: qualitycheck_20190115_models.ListWarningStrategyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListWarningStrategyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.list_warning_strategy_config_with_options(request, runtime)

    async def list_warning_strategy_config_async(
        self,
        request: qualitycheck_20190115_models.ListWarningStrategyConfigRequest,
    ) -> qualitycheck_20190115_models.ListWarningStrategyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_warning_strategy_config_with_options_async(request, runtime)

    def restart_asr_task_with_options(
        self,
        request: qualitycheck_20190115_models.RestartAsrTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.RestartAsrTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartAsrTask',
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
            qualitycheck_20190115_models.RestartAsrTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_asr_task_with_options_async(
        self,
        request: qualitycheck_20190115_models.RestartAsrTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.RestartAsrTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartAsrTask',
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
            qualitycheck_20190115_models.RestartAsrTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_asr_task(
        self,
        request: qualitycheck_20190115_models.RestartAsrTaskRequest,
    ) -> qualitycheck_20190115_models.RestartAsrTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_asr_task_with_options(request, runtime)

    async def restart_asr_task_async(
        self,
        request: qualitycheck_20190115_models.RestartAsrTaskRequest,
    ) -> qualitycheck_20190115_models.RestartAsrTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_asr_task_with_options_async(request, runtime)

    def revert_assigned_session_with_options(
        self,
        request: qualitycheck_20190115_models.RevertAssignedSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.RevertAssignedSessionResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.revert_assigned_session_with_options(request, runtime)

    async def revert_assigned_session_async(
        self,
        request: qualitycheck_20190115_models.RevertAssignedSessionRequest,
    ) -> qualitycheck_20190115_models.RevertAssignedSessionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revert_assigned_session_with_options_async(request, runtime)

    def revert_assigned_session_group_with_options(
        self,
        request: qualitycheck_20190115_models.RevertAssignedSessionGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.RevertAssignedSessionGroupResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.revert_assigned_session_group_with_options(request, runtime)

    async def revert_assigned_session_group_async(
        self,
        request: qualitycheck_20190115_models.RevertAssignedSessionGroupRequest,
    ) -> qualitycheck_20190115_models.RevertAssignedSessionGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.revert_assigned_session_group_with_options_async(request, runtime)

    def save_config_data_set_with_options(
        self,
        request: qualitycheck_20190115_models.SaveConfigDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SaveConfigDataSetResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.save_config_data_set_with_options(request, runtime)

    async def save_config_data_set_async(
        self,
        request: qualitycheck_20190115_models.SaveConfigDataSetRequest,
    ) -> qualitycheck_20190115_models.SaveConfigDataSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_config_data_set_with_options_async(request, runtime)

    def submit_complaint_with_options(
        self,
        request: qualitycheck_20190115_models.SubmitComplaintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitComplaintResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.submit_complaint_with_options(request, runtime)

    async def submit_complaint_async(
        self,
        request: qualitycheck_20190115_models.SubmitComplaintRequest,
    ) -> qualitycheck_20190115_models.SubmitComplaintResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_complaint_with_options_async(request, runtime)

    def submit_precision_task_with_options(
        self,
        request: qualitycheck_20190115_models.SubmitPrecisionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitPrecisionTaskResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.submit_precision_task_with_options(request, runtime)

    async def submit_precision_task_async(
        self,
        request: qualitycheck_20190115_models.SubmitPrecisionTaskRequest,
    ) -> qualitycheck_20190115_models.SubmitPrecisionTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_precision_task_with_options_async(request, runtime)

    def submit_quality_check_task_with_options(
        self,
        request: qualitycheck_20190115_models.SubmitQualityCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitQualityCheckTaskResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.submit_quality_check_task_with_options(request, runtime)

    async def submit_quality_check_task_async(
        self,
        request: qualitycheck_20190115_models.SubmitQualityCheckTaskRequest,
    ) -> qualitycheck_20190115_models.SubmitQualityCheckTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_quality_check_task_with_options_async(request, runtime)

    def submit_review_info_with_options(
        self,
        request: qualitycheck_20190115_models.SubmitReviewInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitReviewInfoResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.submit_review_info_with_options(request, runtime)

    async def submit_review_info_async(
        self,
        request: qualitycheck_20190115_models.SubmitReviewInfoRequest,
    ) -> qualitycheck_20190115_models.SubmitReviewInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_review_info_with_options_async(request, runtime)

    def sync_quality_check_with_options(
        self,
        request: qualitycheck_20190115_models.SyncQualityCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SyncQualityCheckResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.sync_quality_check_with_options(request, runtime)

    async def sync_quality_check_async(
        self,
        request: qualitycheck_20190115_models.SyncQualityCheckRequest,
    ) -> qualitycheck_20190115_models.SyncQualityCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sync_quality_check_with_options_async(request, runtime)

    def update_asr_vocab_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateAsrVocabResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.update_asr_vocab_with_options(request, runtime)

    async def update_asr_vocab_async(
        self,
        request: qualitycheck_20190115_models.UpdateAsrVocabRequest,
    ) -> qualitycheck_20190115_models.UpdateAsrVocabResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_asr_vocab_with_options_async(request, runtime)

    def update_check_type_to_scheme_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateCheckTypeToSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateCheckTypeToSchemeResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.update_check_type_to_scheme_with_options(request, runtime)

    async def update_check_type_to_scheme_async(
        self,
        request: qualitycheck_20190115_models.UpdateCheckTypeToSchemeRequest,
    ) -> qualitycheck_20190115_models.UpdateCheckTypeToSchemeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_check_type_to_scheme_with_options_async(request, runtime)

    def update_quality_check_data_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateQualityCheckDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateQualityCheckDataResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.update_quality_check_data_with_options(request, runtime)

    async def update_quality_check_data_async(
        self,
        request: qualitycheck_20190115_models.UpdateQualityCheckDataRequest,
    ) -> qualitycheck_20190115_models.UpdateQualityCheckDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_quality_check_data_with_options_async(request, runtime)

    def update_quality_check_scheme_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateQualityCheckSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateQualityCheckSchemeResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.update_quality_check_scheme_with_options(request, runtime)

    async def update_quality_check_scheme_async(
        self,
        request: qualitycheck_20190115_models.UpdateQualityCheckSchemeRequest,
    ) -> qualitycheck_20190115_models.UpdateQualityCheckSchemeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_quality_check_scheme_with_options_async(request, runtime)

    def update_rule_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateRuleResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.update_rule_with_options(request, runtime)

    async def update_rule_async(
        self,
        request: qualitycheck_20190115_models.UpdateRuleRequest,
    ) -> qualitycheck_20190115_models.UpdateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_rule_with_options_async(request, runtime)

    def update_rule_by_id_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateRuleByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateRuleByIdResponse:
        UtilClient.validate_model(request)
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
        UtilClient.validate_model(request)
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
        runtime = util_models.RuntimeOptions()
        return self.update_rule_by_id_with_options(request, runtime)

    async def update_rule_by_id_async(
        self,
        request: qualitycheck_20190115_models.UpdateRuleByIdRequest,
    ) -> qualitycheck_20190115_models.UpdateRuleByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_rule_by_id_with_options_async(request, runtime)

    def update_rule_to_scheme_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateRuleToSchemeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateRuleToSchemeResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.update_rule_to_scheme_with_options(request, runtime)

    async def update_rule_to_scheme_async(
        self,
        request: qualitycheck_20190115_models.UpdateRuleToSchemeRequest,
    ) -> qualitycheck_20190115_models.UpdateRuleToSchemeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_rule_to_scheme_with_options_async(request, runtime)

    def update_rule_v4with_options(
        self,
        request: qualitycheck_20190115_models.UpdateRuleV4Request,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateRuleV4Response:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.json_str_for_rule):
            body['JsonStrForRule'] = request.json_str_for_rule
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.json_str_for_rule):
            body['JsonStrForRule'] = request.json_str_for_rule
        if not UtilClient.is_unset(request.rule_id):
            body['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
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
        runtime = util_models.RuntimeOptions()
        return self.update_rule_v4with_options(request, runtime)

    async def update_rule_v4_async(
        self,
        request: qualitycheck_20190115_models.UpdateRuleV4Request,
    ) -> qualitycheck_20190115_models.UpdateRuleV4Response:
        runtime = util_models.RuntimeOptions()
        return await self.update_rule_v4with_options_async(request, runtime)

    def update_scheme_task_config_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateSchemeTaskConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateSchemeTaskConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.update_scheme_task_config_with_options(request, runtime)

    async def update_scheme_task_config_async(
        self,
        request: qualitycheck_20190115_models.UpdateSchemeTaskConfigRequest,
    ) -> qualitycheck_20190115_models.UpdateSchemeTaskConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_scheme_task_config_with_options_async(request, runtime)

    def update_score_for_api_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateScoreForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScoreForApi',
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
            qualitycheck_20190115_models.UpdateScoreForApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_score_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateScoreForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScoreForApi',
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
            qualitycheck_20190115_models.UpdateScoreForApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_score_for_api(
        self,
        request: qualitycheck_20190115_models.UpdateScoreForApiRequest,
    ) -> qualitycheck_20190115_models.UpdateScoreForApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_score_for_api_with_options(request, runtime)

    async def update_score_for_api_async(
        self,
        request: qualitycheck_20190115_models.UpdateScoreForApiRequest,
    ) -> qualitycheck_20190115_models.UpdateScoreForApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_score_for_api_with_options_async(request, runtime)

    def update_skill_group_config_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateSkillGroupConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.update_skill_group_config_with_options(request, runtime)

    async def update_skill_group_config_async(
        self,
        request: qualitycheck_20190115_models.UpdateSkillGroupConfigRequest,
    ) -> qualitycheck_20190115_models.UpdateSkillGroupConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_skill_group_config_with_options_async(request, runtime)

    def update_sub_score_for_api_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateSubScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateSubScoreForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSubScoreForApi',
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
            qualitycheck_20190115_models.UpdateSubScoreForApiResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_sub_score_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateSubScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateSubScoreForApiResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSubScoreForApi',
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
            qualitycheck_20190115_models.UpdateSubScoreForApiResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_sub_score_for_api(
        self,
        request: qualitycheck_20190115_models.UpdateSubScoreForApiRequest,
    ) -> qualitycheck_20190115_models.UpdateSubScoreForApiResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_sub_score_for_api_with_options(request, runtime)

    async def update_sub_score_for_api_async(
        self,
        request: qualitycheck_20190115_models.UpdateSubScoreForApiRequest,
    ) -> qualitycheck_20190115_models.UpdateSubScoreForApiResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_sub_score_for_api_with_options_async(request, runtime)

    def update_sync_quality_check_data_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateSyncQualityCheckDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateSyncQualityCheckDataResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.update_sync_quality_check_data_with_options(request, runtime)

    async def update_sync_quality_check_data_async(
        self,
        request: qualitycheck_20190115_models.UpdateSyncQualityCheckDataRequest,
    ) -> qualitycheck_20190115_models.UpdateSyncQualityCheckDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_sync_quality_check_data_with_options_async(request, runtime)

    def update_task_assign_rule_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateTaskAssignRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateTaskAssignRuleResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.update_task_assign_rule_with_options(request, runtime)

    async def update_task_assign_rule_async(
        self,
        request: qualitycheck_20190115_models.UpdateTaskAssignRuleRequest,
    ) -> qualitycheck_20190115_models.UpdateTaskAssignRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_task_assign_rule_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: qualitycheck_20190115_models.UpdateUserRequest,
    ) -> qualitycheck_20190115_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)

    def update_user_config_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateUserConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateUserConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserConfig',
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
            qualitycheck_20190115_models.UpdateUserConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateUserConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateUserConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.json_str):
            query['JsonStr'] = request.json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserConfig',
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
            qualitycheck_20190115_models.UpdateUserConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_config(
        self,
        request: qualitycheck_20190115_models.UpdateUserConfigRequest,
    ) -> qualitycheck_20190115_models.UpdateUserConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_config_with_options(request, runtime)

    async def update_user_config_async(
        self,
        request: qualitycheck_20190115_models.UpdateUserConfigRequest,
    ) -> qualitycheck_20190115_models.UpdateUserConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_config_with_options_async(request, runtime)

    def update_warning_config_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateWarningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateWarningConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.update_warning_config_with_options(request, runtime)

    async def update_warning_config_async(
        self,
        request: qualitycheck_20190115_models.UpdateWarningConfigRequest,
    ) -> qualitycheck_20190115_models.UpdateWarningConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_warning_config_with_options_async(request, runtime)

    def update_warning_strategy_config_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateWarningStrategyConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateWarningStrategyConfigResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.update_warning_strategy_config_with_options(request, runtime)

    async def update_warning_strategy_config_async(
        self,
        request: qualitycheck_20190115_models.UpdateWarningStrategyConfigRequest,
    ) -> qualitycheck_20190115_models.UpdateWarningStrategyConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_warning_strategy_config_with_options_async(request, runtime)

    def upload_audio_data_with_options(
        self,
        request: qualitycheck_20190115_models.UploadAudioDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadAudioDataResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.upload_audio_data_with_options(request, runtime)

    async def upload_audio_data_async(
        self,
        request: qualitycheck_20190115_models.UploadAudioDataRequest,
    ) -> qualitycheck_20190115_models.UploadAudioDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_audio_data_with_options_async(request, runtime)

    def upload_data_with_options(
        self,
        request: qualitycheck_20190115_models.UploadDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadDataResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.upload_data_with_options(request, runtime)

    async def upload_data_async(
        self,
        request: qualitycheck_20190115_models.UploadDataRequest,
    ) -> qualitycheck_20190115_models.UploadDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_data_with_options_async(request, runtime)

    def upload_data_sync_with_options(
        self,
        request: qualitycheck_20190115_models.UploadDataSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadDataSyncResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.upload_data_sync_with_options(request, runtime)

    async def upload_data_sync_async(
        self,
        request: qualitycheck_20190115_models.UploadDataSyncRequest,
    ) -> qualitycheck_20190115_models.UploadDataSyncResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_data_sync_with_options_async(request, runtime)

    def upload_rule_with_options(
        self,
        request: qualitycheck_20190115_models.UploadRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadRuleResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.upload_rule_with_options(request, runtime)

    async def upload_rule_async(
        self,
        request: qualitycheck_20190115_models.UploadRuleRequest,
    ) -> qualitycheck_20190115_models.UploadRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_rule_with_options_async(request, runtime)

    def verify_file_with_options(
        self,
        request: qualitycheck_20190115_models.VerifyFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.VerifyFileResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.verify_file_with_options(request, runtime)

    async def verify_file_async(
        self,
        request: qualitycheck_20190115_models.VerifyFileRequest,
    ) -> qualitycheck_20190115_models.VerifyFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_file_with_options_async(request, runtime)

    def verify_sentence_with_options(
        self,
        request: qualitycheck_20190115_models.VerifySentenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.VerifySentenceResponse:
        UtilClient.validate_model(request)
        query = {}
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
        UtilClient.validate_model(request)
        query = {}
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
        runtime = util_models.RuntimeOptions()
        return self.verify_sentence_with_options(request, runtime)

    async def verify_sentence_async(
        self,
        request: qualitycheck_20190115_models.VerifySentenceRequest,
    ) -> qualitycheck_20190115_models.VerifySentenceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.verify_sentence_with_options_async(request, runtime)
