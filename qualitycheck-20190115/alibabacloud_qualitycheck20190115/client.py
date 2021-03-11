# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_qualitycheck20190115 import models as qualitycheck_20190115_models
from alibabacloud_tea_util import models as util_models


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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.AddBusinessCategoryResponse().from_map(
            self.do_rpcrequest('AddBusinessCategory', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_business_category_with_options_async(
        self,
        request: qualitycheck_20190115_models.AddBusinessCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AddBusinessCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.AddBusinessCategoryResponse().from_map(
            await self.do_rpcrequest_async('AddBusinessCategory', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.AddRuleCategoryResponse().from_map(
            self.do_rpcrequest('AddRuleCategory', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_rule_category_with_options_async(
        self,
        request: qualitycheck_20190115_models.AddRuleCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AddRuleCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.AddRuleCategoryResponse().from_map(
            await self.do_rpcrequest_async('AddRuleCategory', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def add_thesaurus_for_api_with_options(
        self,
        request: qualitycheck_20190115_models.AddThesaurusForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AddThesaurusForApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.AddThesaurusForApiResponse().from_map(
            self.do_rpcrequest('AddThesaurusForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_thesaurus_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.AddThesaurusForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AddThesaurusForApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.AddThesaurusForApiResponse().from_map(
            await self.do_rpcrequest_async('AddThesaurusForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def add_upload_data_set_with_options(
        self,
        request: qualitycheck_20190115_models.AddUploadDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AddUploadDataSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.AddUploadDataSetResponse().from_map(
            self.do_rpcrequest('AddUploadDataSet', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_upload_data_set_with_options_async(
        self,
        request: qualitycheck_20190115_models.AddUploadDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AddUploadDataSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.AddUploadDataSetResponse().from_map(
            await self.do_rpcrequest_async('AddUploadDataSet', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_upload_data_set(
        self,
        request: qualitycheck_20190115_models.AddUploadDataSetRequest,
    ) -> qualitycheck_20190115_models.AddUploadDataSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_upload_data_set_with_options(request, runtime)

    async def add_upload_data_set_async(
        self,
        request: qualitycheck_20190115_models.AddUploadDataSetRequest,
    ) -> qualitycheck_20190115_models.AddUploadDataSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_upload_data_set_with_options_async(request, runtime)

    def assign_reviewer_with_options(
        self,
        request: qualitycheck_20190115_models.AssignReviewerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AssignReviewerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.AssignReviewerResponse().from_map(
            self.do_rpcrequest('AssignReviewer', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def assign_reviewer_with_options_async(
        self,
        request: qualitycheck_20190115_models.AssignReviewerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.AssignReviewerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.AssignReviewerResponse().from_map(
            await self.do_rpcrequest_async('AssignReviewer', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def config_data_set_with_options(
        self,
        request: qualitycheck_20190115_models.ConfigDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ConfigDataSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ConfigDataSetResponse().from_map(
            self.do_rpcrequest('ConfigDataSet', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_data_set_with_options_async(
        self,
        request: qualitycheck_20190115_models.ConfigDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ConfigDataSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ConfigDataSetResponse().from_map(
            await self.do_rpcrequest_async('ConfigDataSet', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_data_set(
        self,
        request: qualitycheck_20190115_models.ConfigDataSetRequest,
    ) -> qualitycheck_20190115_models.ConfigDataSetResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_data_set_with_options(request, runtime)

    async def config_data_set_async(
        self,
        request: qualitycheck_20190115_models.ConfigDataSetRequest,
    ) -> qualitycheck_20190115_models.ConfigDataSetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_data_set_with_options_async(request, runtime)

    def create_asr_vocab_with_options(
        self,
        request: qualitycheck_20190115_models.CreateAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateAsrVocabResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateAsrVocabResponse().from_map(
            self.do_rpcrequest('CreateAsrVocab', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_asr_vocab_with_options_async(
        self,
        request: qualitycheck_20190115_models.CreateAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateAsrVocabResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateAsrVocabResponse().from_map(
            await self.do_rpcrequest_async('CreateAsrVocab', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def create_rule_with_options(
        self,
        request: qualitycheck_20190115_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateRuleResponse().from_map(
            self.do_rpcrequest('CreateRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_rule_with_options_async(
        self,
        request: qualitycheck_20190115_models.CreateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_rule(
        self,
        request: qualitycheck_20190115_models.CreateRuleRequest,
    ) -> qualitycheck_20190115_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    async def create_rule_async(
        self,
        request: qualitycheck_20190115_models.CreateRuleRequest,
    ) -> qualitycheck_20190115_models.CreateRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_rule_with_options_async(request, runtime)

    def create_skill_group_config_with_options(
        self,
        request: qualitycheck_20190115_models.CreateSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateSkillGroupConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateSkillGroupConfigResponse().from_map(
            self.do_rpcrequest('CreateSkillGroupConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_skill_group_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.CreateSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateSkillGroupConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateSkillGroupConfigResponse().from_map(
            await self.do_rpcrequest_async('CreateSkillGroupConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateTaskAssignRuleResponse().from_map(
            self.do_rpcrequest('CreateTaskAssignRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_task_assign_rule_with_options_async(
        self,
        request: qualitycheck_20190115_models.CreateTaskAssignRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateTaskAssignRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateTaskAssignRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateTaskAssignRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateUserResponse().from_map(
            self.do_rpcrequest('CreateUser', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: qualitycheck_20190115_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateUserResponse().from_map(
            await self.do_rpcrequest_async('CreateUser', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateWarningConfigResponse().from_map(
            self.do_rpcrequest('CreateWarningConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_warning_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.CreateWarningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.CreateWarningConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.CreateWarningConfigResponse().from_map(
            await self.do_rpcrequest_async('CreateWarningConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_asr_vocab_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteAsrVocabResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteAsrVocabResponse().from_map(
            self.do_rpcrequest('DeleteAsrVocab', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_asr_vocab_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteAsrVocabResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteAsrVocabResponse().from_map(
            await self.do_rpcrequest_async('DeleteAsrVocab', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteBusinessCategoryResponse().from_map(
            self.do_rpcrequest('DeleteBusinessCategory', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_business_category_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteBusinessCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteBusinessCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteBusinessCategoryResponse().from_map(
            await self.do_rpcrequest_async('DeleteBusinessCategory', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteCustomizationConfigResponse().from_map(
            self.do_rpcrequest('DeleteCustomizationConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_customization_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteCustomizationConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteCustomizationConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteCustomizationConfigResponse().from_map(
            await self.do_rpcrequest_async('DeleteCustomizationConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteDataSetResponse().from_map(
            self.do_rpcrequest('DeleteDataSet', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_data_set_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteDataSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteDataSetResponse().from_map(
            await self.do_rpcrequest_async('DeleteDataSet', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeletePrecisionTaskResponse().from_map(
            self.do_rpcrequest('DeletePrecisionTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_precision_task_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeletePrecisionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeletePrecisionTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeletePrecisionTaskResponse().from_map(
            await self.do_rpcrequest_async('DeletePrecisionTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_score_for_api_with_options(
        self,
        request: qualitycheck_20190115_models.DeleteScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteScoreForApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteScoreForApiResponse().from_map(
            self.do_rpcrequest('DeleteScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_score_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteScoreForApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteScoreForApiResponse().from_map(
            await self.do_rpcrequest_async('DeleteScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteSkillGroupConfigResponse().from_map(
            self.do_rpcrequest('DeleteSkillGroupConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_skill_group_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteSkillGroupConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteSkillGroupConfigResponse().from_map(
            await self.do_rpcrequest_async('DeleteSkillGroupConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteSubScoreForApiResponse().from_map(
            self.do_rpcrequest('DeleteSubScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_sub_score_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteSubScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteSubScoreForApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteSubScoreForApiResponse().from_map(
            await self.do_rpcrequest_async('DeleteSubScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteTaskAssignRuleResponse().from_map(
            self.do_rpcrequest('DeleteTaskAssignRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_task_assign_rule_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteTaskAssignRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteTaskAssignRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteTaskAssignRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteTaskAssignRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteUserResponse().from_map(
            self.do_rpcrequest('DeleteUser', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteUserResponse().from_map(
            await self.do_rpcrequest_async('DeleteUser', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteWarningConfigResponse().from_map(
            self.do_rpcrequest('DeleteWarningConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_warning_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.DeleteWarningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DeleteWarningConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DeleteWarningConfigResponse().from_map(
            await self.do_rpcrequest_async('DeleteWarningConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def del_rule_category_with_options(
        self,
        request: qualitycheck_20190115_models.DelRuleCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DelRuleCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DelRuleCategoryResponse().from_map(
            self.do_rpcrequest('DelRuleCategory', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def del_rule_category_with_options_async(
        self,
        request: qualitycheck_20190115_models.DelRuleCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DelRuleCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DelRuleCategoryResponse().from_map(
            await self.do_rpcrequest_async('DelRuleCategory', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DelThesaurusForApiResponse().from_map(
            self.do_rpcrequest('DelThesaurusForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def del_thesaurus_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.DelThesaurusForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.DelThesaurusForApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.DelThesaurusForApiResponse().from_map(
            await self.do_rpcrequest_async('DelThesaurusForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def edit_thesaurus_for_api_with_options(
        self,
        request: qualitycheck_20190115_models.EditThesaurusForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.EditThesaurusForApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.EditThesaurusForApiResponse().from_map(
            self.do_rpcrequest('EditThesaurusForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def edit_thesaurus_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.EditThesaurusForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.EditThesaurusForApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.EditThesaurusForApiResponse().from_map(
            await self.do_rpcrequest_async('EditThesaurusForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetAsrVocabResponse().from_map(
            self.do_rpcrequest('GetAsrVocab', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_asr_vocab_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetAsrVocabResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetAsrVocabResponse().from_map(
            await self.do_rpcrequest_async('GetAsrVocab', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetBusinessCategoryListResponse().from_map(
            self.do_rpcrequest('GetBusinessCategoryList', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_business_category_list_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetBusinessCategoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetBusinessCategoryListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetBusinessCategoryListResponse().from_map(
            await self.do_rpcrequest_async('GetBusinessCategoryList', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetCustomizationConfigListResponse().from_map(
            self.do_rpcrequest('GetCustomizationConfigList', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_customization_config_list_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetCustomizationConfigListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetCustomizationConfigListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetCustomizationConfigListResponse().from_map(
            await self.do_rpcrequest_async('GetCustomizationConfigList', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetHitResultResponse().from_map(
            self.do_rpcrequest('GetHitResult', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_hit_result_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetHitResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetHitResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetHitResultResponse().from_map(
            await self.do_rpcrequest_async('GetHitResult', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetNextResultToVerifyResponse().from_map(
            self.do_rpcrequest('GetNextResultToVerify', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_next_result_to_verify_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetNextResultToVerifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetNextResultToVerifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetNextResultToVerifyResponse().from_map(
            await self.do_rpcrequest_async('GetNextResultToVerify', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetPrecisionTaskResponse().from_map(
            self.do_rpcrequest('GetPrecisionTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_precision_task_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetPrecisionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetPrecisionTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetPrecisionTaskResponse().from_map(
            await self.do_rpcrequest_async('GetPrecisionTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_result_with_options(
        self,
        request: qualitycheck_20190115_models.GetResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetResultResponse().from_map(
            self.do_rpcrequest('GetResult', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_result_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetResultResponse().from_map(
            await self.do_rpcrequest_async('GetResult', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetResultCallbackResponse().from_map(
            self.do_rpcrequest('GetResultCallback', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_result_callback_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetResultCallbackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetResultCallbackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetResultCallbackResponse().from_map(
            await self.do_rpcrequest_async('GetResultCallback', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetResultToReviewResponse().from_map(
            self.do_rpcrequest('GetResultToReview', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_result_to_review_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetResultToReviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetResultToReviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetResultToReviewResponse().from_map(
            await self.do_rpcrequest_async('GetResultToReview', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_review_info_with_options(
        self,
        request: qualitycheck_20190115_models.GetReviewInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetReviewInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetReviewInfoResponse().from_map(
            self.do_rpcrequest('GetReviewInfo', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_review_info_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetReviewInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetReviewInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetReviewInfoResponse().from_map(
            await self.do_rpcrequest_async('GetReviewInfo', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_review_info(
        self,
        request: qualitycheck_20190115_models.GetReviewInfoRequest,
    ) -> qualitycheck_20190115_models.GetReviewInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_review_info_with_options(request, runtime)

    async def get_review_info_async(
        self,
        request: qualitycheck_20190115_models.GetReviewInfoRequest,
    ) -> qualitycheck_20190115_models.GetReviewInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_review_info_with_options_async(request, runtime)

    def get_rule_with_options(
        self,
        request: qualitycheck_20190115_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetRuleResponse().from_map(
            self.do_rpcrequest('GetRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_rule_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetRuleResponse().from_map(
            await self.do_rpcrequest_async('GetRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_rule_category_with_options(
        self,
        request: qualitycheck_20190115_models.GetRuleCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetRuleCategoryResponse().from_map(
            self.do_rpcrequest('GetRuleCategory', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_rule_category_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetRuleCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetRuleCategoryResponse().from_map(
            await self.do_rpcrequest_async('GetRuleCategory', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetRuleDetailResponse().from_map(
            self.do_rpcrequest('GetRuleDetail', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_rule_detail_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetRuleDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetRuleDetailResponse().from_map(
            await self.do_rpcrequest_async('GetRuleDetail', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_rule_dimension_with_options(
        self,
        request: qualitycheck_20190115_models.GetRuleDimensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleDimensionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetRuleDimensionResponse().from_map(
            self.do_rpcrequest('GetRuleDimension', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_rule_dimension_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetRuleDimensionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetRuleDimensionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetRuleDimensionResponse().from_map(
            await self.do_rpcrequest_async('GetRuleDimension', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_rule_dimension(
        self,
        request: qualitycheck_20190115_models.GetRuleDimensionRequest,
    ) -> qualitycheck_20190115_models.GetRuleDimensionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_rule_dimension_with_options(request, runtime)

    async def get_rule_dimension_async(
        self,
        request: qualitycheck_20190115_models.GetRuleDimensionRequest,
    ) -> qualitycheck_20190115_models.GetRuleDimensionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rule_dimension_with_options_async(request, runtime)

    def get_score_info_with_options(
        self,
        request: qualitycheck_20190115_models.GetScoreInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetScoreInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetScoreInfoResponse().from_map(
            self.do_rpcrequest('GetScoreInfo', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_score_info_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetScoreInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetScoreInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetScoreInfoResponse().from_map(
            await self.do_rpcrequest_async('GetScoreInfo', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetSkillGroupConfigResponse().from_map(
            self.do_rpcrequest('GetSkillGroupConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_skill_group_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetSkillGroupConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetSkillGroupConfigResponse().from_map(
            await self.do_rpcrequest_async('GetSkillGroupConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetSyncResultResponse().from_map(
            self.do_rpcrequest('GetSyncResult', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_sync_result_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetSyncResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetSyncResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetSyncResultResponse().from_map(
            await self.do_rpcrequest_async('GetSyncResult', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def get_task_file_result_list_with_options(
        self,
        request: qualitycheck_20190115_models.GetTaskFileResultListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetTaskFileResultListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetTaskFileResultListResponse().from_map(
            self.do_rpcrequest('GetTaskFileResultList', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_task_file_result_list_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetTaskFileResultListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetTaskFileResultListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetTaskFileResultListResponse().from_map(
            await self.do_rpcrequest_async('GetTaskFileResultList', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task_file_result_list(
        self,
        request: qualitycheck_20190115_models.GetTaskFileResultListRequest,
    ) -> qualitycheck_20190115_models.GetTaskFileResultListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_file_result_list_with_options(request, runtime)

    async def get_task_file_result_list_async(
        self,
        request: qualitycheck_20190115_models.GetTaskFileResultListRequest,
    ) -> qualitycheck_20190115_models.GetTaskFileResultListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_file_result_list_with_options_async(request, runtime)

    def get_task_rule_list_with_options(
        self,
        request: qualitycheck_20190115_models.GetTaskRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetTaskRuleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetTaskRuleListResponse().from_map(
            self.do_rpcrequest('GetTaskRuleList', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_task_rule_list_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetTaskRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetTaskRuleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetTaskRuleListResponse().from_map(
            await self.do_rpcrequest_async('GetTaskRuleList', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_task_rule_list(
        self,
        request: qualitycheck_20190115_models.GetTaskRuleListRequest,
    ) -> qualitycheck_20190115_models.GetTaskRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_task_rule_list_with_options(request, runtime)

    async def get_task_rule_list_async(
        self,
        request: qualitycheck_20190115_models.GetTaskRuleListRequest,
    ) -> qualitycheck_20190115_models.GetTaskRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_task_rule_list_with_options_async(request, runtime)

    def get_thesaurus_by_synonym_for_api_with_options(
        self,
        request: qualitycheck_20190115_models.GetThesaurusBySynonymForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetThesaurusBySynonymForApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetThesaurusBySynonymForApiResponse().from_map(
            self.do_rpcrequest('GetThesaurusBySynonymForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_thesaurus_by_synonym_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.GetThesaurusBySynonymForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.GetThesaurusBySynonymForApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.GetThesaurusBySynonymForApiResponse().from_map(
            await self.do_rpcrequest_async('GetThesaurusBySynonymForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def handle_complaint_with_options(
        self,
        request: qualitycheck_20190115_models.HandleComplaintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.HandleComplaintResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.HandleComplaintResponse().from_map(
            self.do_rpcrequest('HandleComplaint', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def handle_complaint_with_options_async(
        self,
        request: qualitycheck_20190115_models.HandleComplaintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.HandleComplaintResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.HandleComplaintResponse().from_map(
            await self.do_rpcrequest_async('HandleComplaint', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.InsertScoreForApiResponse().from_map(
            self.do_rpcrequest('InsertScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def insert_score_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.InsertScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.InsertScoreForApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.InsertScoreForApiResponse().from_map(
            await self.do_rpcrequest_async('InsertScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.InsertSubScoreForApiResponse().from_map(
            self.do_rpcrequest('InsertSubScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def insert_sub_score_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.InsertSubScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.InsertSubScoreForApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.InsertSubScoreForApiResponse().from_map(
            await self.do_rpcrequest_async('InsertSubScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.InvalidRuleResponse().from_map(
            self.do_rpcrequest('InvalidRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def invalid_rule_with_options_async(
        self,
        request: qualitycheck_20190115_models.InvalidRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.InvalidRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.InvalidRuleResponse().from_map(
            await self.do_rpcrequest_async('InvalidRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListAsrVocabResponse().from_map(
            self.do_rpcrequest('ListAsrVocab', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_asr_vocab_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListAsrVocabResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListAsrVocabResponse().from_map(
            await self.do_rpcrequest_async('ListAsrVocab', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_data_set_task_with_options(
        self,
        request: qualitycheck_20190115_models.ListDataSetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListDataSetTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListDataSetTaskResponse().from_map(
            self.do_rpcrequest('ListDataSetTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_data_set_task_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListDataSetTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListDataSetTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListDataSetTaskResponse().from_map(
            await self.do_rpcrequest_async('ListDataSetTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_set_task(
        self,
        request: qualitycheck_20190115_models.ListDataSetTaskRequest,
    ) -> qualitycheck_20190115_models.ListDataSetTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_set_task_with_options(request, runtime)

    async def list_data_set_task_async(
        self,
        request: qualitycheck_20190115_models.ListDataSetTaskRequest,
    ) -> qualitycheck_20190115_models.ListDataSetTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_set_task_with_options_async(request, runtime)

    def list_hot_words_tasks_with_options(
        self,
        request: qualitycheck_20190115_models.ListHotWordsTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListHotWordsTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListHotWordsTasksResponse().from_map(
            self.do_rpcrequest('ListHotWordsTasks', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_hot_words_tasks_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListHotWordsTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListHotWordsTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListHotWordsTasksResponse().from_map(
            await self.do_rpcrequest_async('ListHotWordsTasks', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListPrecisionTaskResponse().from_map(
            self.do_rpcrequest('ListPrecisionTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_precision_task_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListPrecisionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListPrecisionTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListPrecisionTaskResponse().from_map(
            await self.do_rpcrequest_async('ListPrecisionTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_roles_with_options(
        self,
        request: qualitycheck_20190115_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListRolesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListRolesResponse().from_map(
            self.do_rpcrequest('ListRoles', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListRolesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListRolesResponse().from_map(
            await self.do_rpcrequest_async('ListRoles', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListRulesResponse().from_map(
            self.do_rpcrequest('ListRules', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_rules_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListRulesResponse().from_map(
            await self.do_rpcrequest_async('ListRules', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def list_skill_group_config_with_options(
        self,
        request: qualitycheck_20190115_models.ListSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListSkillGroupConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListSkillGroupConfigResponse().from_map(
            self.do_rpcrequest('ListSkillGroupConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_skill_group_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListSkillGroupConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListSkillGroupConfigResponse().from_map(
            await self.do_rpcrequest_async('ListSkillGroupConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListTaskAssignRulesResponse().from_map(
            self.do_rpcrequest('ListTaskAssignRules', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_task_assign_rules_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListTaskAssignRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListTaskAssignRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListTaskAssignRulesResponse().from_map(
            await self.do_rpcrequest_async('ListTaskAssignRules', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListUsersResponse().from_map(
            self.do_rpcrequest('ListUsers', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListUsersResponse().from_map(
            await self.do_rpcrequest_async('ListUsers', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListWarningConfigResponse().from_map(
            self.do_rpcrequest('ListWarningConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_warning_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.ListWarningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ListWarningConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ListWarningConfigResponse().from_map(
            await self.do_rpcrequest_async('ListWarningConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def remove_and_get_task_rules_with_options(
        self,
        request: qualitycheck_20190115_models.RemoveAndGetTaskRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.RemoveAndGetTaskRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.RemoveAndGetTaskRulesResponse().from_map(
            self.do_rpcrequest('RemoveAndGetTaskRules', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_and_get_task_rules_with_options_async(
        self,
        request: qualitycheck_20190115_models.RemoveAndGetTaskRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.RemoveAndGetTaskRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.RemoveAndGetTaskRulesResponse().from_map(
            await self.do_rpcrequest_async('RemoveAndGetTaskRules', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_and_get_task_rules(
        self,
        request: qualitycheck_20190115_models.RemoveAndGetTaskRulesRequest,
    ) -> qualitycheck_20190115_models.RemoveAndGetTaskRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_and_get_task_rules_with_options(request, runtime)

    async def remove_and_get_task_rules_async(
        self,
        request: qualitycheck_20190115_models.RemoveAndGetTaskRulesRequest,
    ) -> qualitycheck_20190115_models.RemoveAndGetTaskRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_and_get_task_rules_with_options_async(request, runtime)

    def restart_asr_task_with_options(
        self,
        request: qualitycheck_20190115_models.RestartAsrTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.RestartAsrTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.RestartAsrTaskResponse().from_map(
            self.do_rpcrequest('RestartAsrTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restart_asr_task_with_options_async(
        self,
        request: qualitycheck_20190115_models.RestartAsrTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.RestartAsrTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.RestartAsrTaskResponse().from_map(
            await self.do_rpcrequest_async('RestartAsrTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def review_single_result_by_id_with_options(
        self,
        request: qualitycheck_20190115_models.ReviewSingleResultByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ReviewSingleResultByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ReviewSingleResultByIdResponse().from_map(
            self.do_rpcrequest('ReviewSingleResultById', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def review_single_result_by_id_with_options_async(
        self,
        request: qualitycheck_20190115_models.ReviewSingleResultByIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.ReviewSingleResultByIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.ReviewSingleResultByIdResponse().from_map(
            await self.do_rpcrequest_async('ReviewSingleResultById', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def review_single_result_by_id(
        self,
        request: qualitycheck_20190115_models.ReviewSingleResultByIdRequest,
    ) -> qualitycheck_20190115_models.ReviewSingleResultByIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.review_single_result_by_id_with_options(request, runtime)

    async def review_single_result_by_id_async(
        self,
        request: qualitycheck_20190115_models.ReviewSingleResultByIdRequest,
    ) -> qualitycheck_20190115_models.ReviewSingleResultByIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.review_single_result_by_id_with_options_async(request, runtime)

    def save_config_data_set_with_options(
        self,
        request: qualitycheck_20190115_models.SaveConfigDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SaveConfigDataSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SaveConfigDataSetResponse().from_map(
            self.do_rpcrequest('SaveConfigDataSet', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_config_data_set_with_options_async(
        self,
        request: qualitycheck_20190115_models.SaveConfigDataSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SaveConfigDataSetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SaveConfigDataSetResponse().from_map(
            await self.do_rpcrequest_async('SaveConfigDataSet', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SubmitComplaintResponse().from_map(
            self.do_rpcrequest('SubmitComplaint', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_complaint_with_options_async(
        self,
        request: qualitycheck_20190115_models.SubmitComplaintRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitComplaintResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SubmitComplaintResponse().from_map(
            await self.do_rpcrequest_async('SubmitComplaint', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def submit_customization_config_with_options(
        self,
        request: qualitycheck_20190115_models.SubmitCustomizationConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitCustomizationConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SubmitCustomizationConfigResponse().from_map(
            self.do_rpcrequest('SubmitCustomizationConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_customization_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.SubmitCustomizationConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitCustomizationConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SubmitCustomizationConfigResponse().from_map(
            await self.do_rpcrequest_async('SubmitCustomizationConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_customization_config(
        self,
        request: qualitycheck_20190115_models.SubmitCustomizationConfigRequest,
    ) -> qualitycheck_20190115_models.SubmitCustomizationConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_customization_config_with_options(request, runtime)

    async def submit_customization_config_async(
        self,
        request: qualitycheck_20190115_models.SubmitCustomizationConfigRequest,
    ) -> qualitycheck_20190115_models.SubmitCustomizationConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_customization_config_with_options_async(request, runtime)

    def submit_precision_task_with_options(
        self,
        request: qualitycheck_20190115_models.SubmitPrecisionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitPrecisionTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SubmitPrecisionTaskResponse().from_map(
            self.do_rpcrequest('SubmitPrecisionTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_precision_task_with_options_async(
        self,
        request: qualitycheck_20190115_models.SubmitPrecisionTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitPrecisionTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SubmitPrecisionTaskResponse().from_map(
            await self.do_rpcrequest_async('SubmitPrecisionTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SubmitQualityCheckTaskResponse().from_map(
            self.do_rpcrequest('SubmitQualityCheckTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_quality_check_task_with_options_async(
        self,
        request: qualitycheck_20190115_models.SubmitQualityCheckTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitQualityCheckTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SubmitQualityCheckTaskResponse().from_map(
            await self.do_rpcrequest_async('SubmitQualityCheckTask', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SubmitReviewInfoResponse().from_map(
            self.do_rpcrequest('SubmitReviewInfo', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_review_info_with_options_async(
        self,
        request: qualitycheck_20190115_models.SubmitReviewInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SubmitReviewInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SubmitReviewInfoResponse().from_map(
            await self.do_rpcrequest_async('SubmitReviewInfo', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SyncQualityCheckResponse().from_map(
            self.do_rpcrequest('SyncQualityCheck', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def sync_quality_check_with_options_async(
        self,
        request: qualitycheck_20190115_models.SyncQualityCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.SyncQualityCheckResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.SyncQualityCheckResponse().from_map(
            await self.do_rpcrequest_async('SyncQualityCheck', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def test_rule_with_options(
        self,
        request: qualitycheck_20190115_models.TestRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.TestRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.TestRuleResponse().from_map(
            self.do_rpcrequest('TestRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def test_rule_with_options_async(
        self,
        request: qualitycheck_20190115_models.TestRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.TestRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.TestRuleResponse().from_map(
            await self.do_rpcrequest_async('TestRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def test_rule(
        self,
        request: qualitycheck_20190115_models.TestRuleRequest,
    ) -> qualitycheck_20190115_models.TestRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.test_rule_with_options(request, runtime)

    async def test_rule_async(
        self,
        request: qualitycheck_20190115_models.TestRuleRequest,
    ) -> qualitycheck_20190115_models.TestRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.test_rule_with_options_async(request, runtime)

    def update_asr_vocab_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateAsrVocabResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateAsrVocabResponse().from_map(
            self.do_rpcrequest('UpdateAsrVocab', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_asr_vocab_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateAsrVocabRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateAsrVocabResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateAsrVocabResponse().from_map(
            await self.do_rpcrequest_async('UpdateAsrVocab', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_on_purchase_success_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateOnPurchaseSuccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateOnPurchaseSuccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateOnPurchaseSuccessResponse().from_map(
            self.do_rpcrequest('UpdateOnPurchaseSuccess', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_on_purchase_success_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateOnPurchaseSuccessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateOnPurchaseSuccessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateOnPurchaseSuccessResponse().from_map(
            await self.do_rpcrequest_async('UpdateOnPurchaseSuccess', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_on_purchase_success(
        self,
        request: qualitycheck_20190115_models.UpdateOnPurchaseSuccessRequest,
    ) -> qualitycheck_20190115_models.UpdateOnPurchaseSuccessResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_on_purchase_success_with_options(request, runtime)

    async def update_on_purchase_success_async(
        self,
        request: qualitycheck_20190115_models.UpdateOnPurchaseSuccessRequest,
    ) -> qualitycheck_20190115_models.UpdateOnPurchaseSuccessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_on_purchase_success_with_options_async(request, runtime)

    def update_rule_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateRuleResponse().from_map(
            self.do_rpcrequest('UpdateRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_rule_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateRuleResponse().from_map(
            await self.do_rpcrequest_async('UpdateRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def update_score_for_api_with_options(
        self,
        request: qualitycheck_20190115_models.UpdateScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateScoreForApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateScoreForApiResponse().from_map(
            self.do_rpcrequest('UpdateScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_score_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateScoreForApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateScoreForApiResponse().from_map(
            await self.do_rpcrequest_async('UpdateScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateSkillGroupConfigResponse().from_map(
            self.do_rpcrequest('UpdateSkillGroupConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_skill_group_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateSkillGroupConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateSkillGroupConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateSkillGroupConfigResponse().from_map(
            await self.do_rpcrequest_async('UpdateSkillGroupConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateSubScoreForApiResponse().from_map(
            self.do_rpcrequest('UpdateSubScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_sub_score_for_api_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateSubScoreForApiRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateSubScoreForApiResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateSubScoreForApiResponse().from_map(
            await self.do_rpcrequest_async('UpdateSubScoreForApi', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateSyncQualityCheckDataResponse().from_map(
            self.do_rpcrequest('UpdateSyncQualityCheckData', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_sync_quality_check_data_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateSyncQualityCheckDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateSyncQualityCheckDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateSyncQualityCheckDataResponse().from_map(
            await self.do_rpcrequest_async('UpdateSyncQualityCheckData', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateTaskAssignRuleResponse().from_map(
            self.do_rpcrequest('UpdateTaskAssignRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_task_assign_rule_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateTaskAssignRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateTaskAssignRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateTaskAssignRuleResponse().from_map(
            await self.do_rpcrequest_async('UpdateTaskAssignRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateUserResponse().from_map(
            self.do_rpcrequest('UpdateUser', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateUserResponse().from_map(
            await self.do_rpcrequest_async('UpdateUser', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateUserConfigResponse().from_map(
            self.do_rpcrequest('UpdateUserConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_user_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateUserConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateUserConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateUserConfigResponse().from_map(
            await self.do_rpcrequest_async('UpdateUserConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateWarningConfigResponse().from_map(
            self.do_rpcrequest('UpdateWarningConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_warning_config_with_options_async(
        self,
        request: qualitycheck_20190115_models.UpdateWarningConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UpdateWarningConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UpdateWarningConfigResponse().from_map(
            await self.do_rpcrequest_async('UpdateWarningConfig', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def upload_audio_data_with_options(
        self,
        request: qualitycheck_20190115_models.UploadAudioDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadAudioDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UploadAudioDataResponse().from_map(
            self.do_rpcrequest('UploadAudioData', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_audio_data_with_options_async(
        self,
        request: qualitycheck_20190115_models.UploadAudioDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadAudioDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UploadAudioDataResponse().from_map(
            await self.do_rpcrequest_async('UploadAudioData', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UploadDataResponse().from_map(
            self.do_rpcrequest('UploadData', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_data_with_options_async(
        self,
        request: qualitycheck_20190115_models.UploadDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UploadDataResponse().from_map(
            await self.do_rpcrequest_async('UploadData', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UploadDataSyncResponse().from_map(
            self.do_rpcrequest('UploadDataSync', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_data_sync_with_options_async(
        self,
        request: qualitycheck_20190115_models.UploadDataSyncRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadDataSyncResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UploadDataSyncResponse().from_map(
            await self.do_rpcrequest_async('UploadDataSync', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UploadRuleResponse().from_map(
            self.do_rpcrequest('UploadRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upload_rule_with_options_async(
        self,
        request: qualitycheck_20190115_models.UploadRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.UploadRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.UploadRuleResponse().from_map(
            await self.do_rpcrequest_async('UploadRule', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.VerifyFileResponse().from_map(
            self.do_rpcrequest('VerifyFile', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_file_with_options_async(
        self,
        request: qualitycheck_20190115_models.VerifyFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.VerifyFileResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.VerifyFileResponse().from_map(
            await self.do_rpcrequest_async('VerifyFile', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.VerifySentenceResponse().from_map(
            self.do_rpcrequest('VerifySentence', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def verify_sentence_with_options_async(
        self,
        request: qualitycheck_20190115_models.VerifySentenceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> qualitycheck_20190115_models.VerifySentenceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return qualitycheck_20190115_models.VerifySentenceResponse().from_map(
            await self.do_rpcrequest_async('VerifySentence', '2019-01-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
