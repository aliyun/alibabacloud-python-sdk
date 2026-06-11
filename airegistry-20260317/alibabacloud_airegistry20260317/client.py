# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_airegistry20260317 import models as main_models
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
        self._endpoint = self.get_endpoint('airegistry', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_namespace_with_options(
        self,
        request: main_models.CreateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.scan_policy):
            query['ScanPolicy'] = request.scan_policy
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNamespace',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_namespace_with_options_async(
        self,
        request: main_models.CreateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.scan_policy):
            query['ScanPolicy'] = request.scan_policy
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNamespace',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_namespace(
        self,
        request: main_models.CreateNamespaceRequest,
    ) -> main_models.CreateNamespaceResponse:
        runtime = RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    async def create_namespace_async(
        self,
        request: main_models.CreateNamespaceRequest,
    ) -> main_models.CreateNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.create_namespace_with_options_async(request, runtime)

    def create_prompt_with_options(
        self,
        request: main_models.CreatePromptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePromptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_tags):
            query['BizTags'] = request.biz_tags
        if not DaraCore.is_null(request.commit_msg):
            query['CommitMsg'] = request.commit_msg
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        if not DaraCore.is_null(request.target_version):
            query['TargetVersion'] = request.target_version
        if not DaraCore.is_null(request.template):
            query['Template'] = request.template
        if not DaraCore.is_null(request.variables):
            query['Variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrompt',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePromptResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prompt_with_options_async(
        self,
        request: main_models.CreatePromptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePromptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_tags):
            query['BizTags'] = request.biz_tags
        if not DaraCore.is_null(request.commit_msg):
            query['CommitMsg'] = request.commit_msg
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        if not DaraCore.is_null(request.target_version):
            query['TargetVersion'] = request.target_version
        if not DaraCore.is_null(request.template):
            query['Template'] = request.template
        if not DaraCore.is_null(request.variables):
            query['Variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrompt',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePromptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prompt(
        self,
        request: main_models.CreatePromptRequest,
    ) -> main_models.CreatePromptResponse:
        runtime = RuntimeOptions()
        return self.create_prompt_with_options(request, runtime)

    async def create_prompt_async(
        self,
        request: main_models.CreatePromptRequest,
    ) -> main_models.CreatePromptResponse:
        runtime = RuntimeOptions()
        return await self.create_prompt_with_options_async(request, runtime)

    def create_prompt_version_with_options(
        self,
        request: main_models.CreatePromptVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePromptVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.based_on_version):
            query['BasedOnVersion'] = request.based_on_version
        if not DaraCore.is_null(request.commit_msg):
            query['CommitMsg'] = request.commit_msg
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        if not DaraCore.is_null(request.target_version):
            query['TargetVersion'] = request.target_version
        if not DaraCore.is_null(request.template):
            query['Template'] = request.template
        if not DaraCore.is_null(request.variables):
            query['Variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePromptVersion',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePromptVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prompt_version_with_options_async(
        self,
        request: main_models.CreatePromptVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePromptVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.based_on_version):
            query['BasedOnVersion'] = request.based_on_version
        if not DaraCore.is_null(request.commit_msg):
            query['CommitMsg'] = request.commit_msg
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        if not DaraCore.is_null(request.target_version):
            query['TargetVersion'] = request.target_version
        if not DaraCore.is_null(request.template):
            query['Template'] = request.template
        if not DaraCore.is_null(request.variables):
            query['Variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePromptVersion',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePromptVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prompt_version(
        self,
        request: main_models.CreatePromptVersionRequest,
    ) -> main_models.CreatePromptVersionResponse:
        runtime = RuntimeOptions()
        return self.create_prompt_version_with_options(request, runtime)

    async def create_prompt_version_async(
        self,
        request: main_models.CreatePromptVersionRequest,
    ) -> main_models.CreatePromptVersionResponse:
        runtime = RuntimeOptions()
        return await self.create_prompt_version_with_options_async(request, runtime)

    def create_skill_draft_with_options(
        self,
        request: main_models.CreateSkillDraftRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillDraftResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.based_on_version):
            query['BasedOnVersion'] = request.based_on_version
        if not DaraCore.is_null(request.commit_msg):
            query['CommitMsg'] = request.commit_msg
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_card):
            query['SkillCard'] = request.skill_card
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.target_version):
            query['TargetVersion'] = request.target_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkillDraft',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSkillDraftResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_skill_draft_with_options_async(
        self,
        request: main_models.CreateSkillDraftRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSkillDraftResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.based_on_version):
            query['BasedOnVersion'] = request.based_on_version
        if not DaraCore.is_null(request.commit_msg):
            query['CommitMsg'] = request.commit_msg
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_card):
            query['SkillCard'] = request.skill_card
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.target_version):
            query['TargetVersion'] = request.target_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSkillDraft',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSkillDraftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_skill_draft(
        self,
        request: main_models.CreateSkillDraftRequest,
    ) -> main_models.CreateSkillDraftResponse:
        runtime = RuntimeOptions()
        return self.create_skill_draft_with_options(request, runtime)

    async def create_skill_draft_async(
        self,
        request: main_models.CreateSkillDraftRequest,
    ) -> main_models.CreateSkillDraftResponse:
        runtime = RuntimeOptions()
        return await self.create_skill_draft_with_options_async(request, runtime)

    def delete_namespace_with_options(
        self,
        request: main_models.DeleteNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNamespace',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_namespace_with_options_async(
        self,
        request: main_models.DeleteNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNamespace',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_namespace(
        self,
        request: main_models.DeleteNamespaceRequest,
    ) -> main_models.DeleteNamespaceResponse:
        runtime = RuntimeOptions()
        return self.delete_namespace_with_options(request, runtime)

    async def delete_namespace_async(
        self,
        request: main_models.DeleteNamespaceRequest,
    ) -> main_models.DeleteNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.delete_namespace_with_options_async(request, runtime)

    def delete_prompt_with_options(
        self,
        request: main_models.DeletePromptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePromptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrompt',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePromptResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_prompt_with_options_async(
        self,
        request: main_models.DeletePromptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePromptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrompt',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePromptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_prompt(
        self,
        request: main_models.DeletePromptRequest,
    ) -> main_models.DeletePromptResponse:
        runtime = RuntimeOptions()
        return self.delete_prompt_with_options(request, runtime)

    async def delete_prompt_async(
        self,
        request: main_models.DeletePromptRequest,
    ) -> main_models.DeletePromptResponse:
        runtime = RuntimeOptions()
        return await self.delete_prompt_with_options_async(request, runtime)

    def delete_skill_with_options(
        self,
        request: main_models.DeleteSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSkill',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_skill_with_options_async(
        self,
        request: main_models.DeleteSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSkill',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_skill(
        self,
        request: main_models.DeleteSkillRequest,
    ) -> main_models.DeleteSkillResponse:
        runtime = RuntimeOptions()
        return self.delete_skill_with_options(request, runtime)

    async def delete_skill_async(
        self,
        request: main_models.DeleteSkillRequest,
    ) -> main_models.DeleteSkillResponse:
        runtime = RuntimeOptions()
        return await self.delete_skill_with_options_async(request, runtime)

    def download_skill_version_via_oss_with_options(
        self,
        request: main_models.DownloadSkillVersionViaOssRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadSkillVersionViaOssResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadSkillVersionViaOss',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadSkillVersionViaOssResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_skill_version_via_oss_with_options_async(
        self,
        request: main_models.DownloadSkillVersionViaOssRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadSkillVersionViaOssResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadSkillVersionViaOss',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadSkillVersionViaOssResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_skill_version_via_oss(
        self,
        request: main_models.DownloadSkillVersionViaOssRequest,
    ) -> main_models.DownloadSkillVersionViaOssResponse:
        runtime = RuntimeOptions()
        return self.download_skill_version_via_oss_with_options(request, runtime)

    async def download_skill_version_via_oss_async(
        self,
        request: main_models.DownloadSkillVersionViaOssRequest,
    ) -> main_models.DownloadSkillVersionViaOssResponse:
        runtime = RuntimeOptions()
        return await self.download_skill_version_via_oss_with_options_async(request, runtime)

    def force_publish_skill_version_with_options(
        self,
        request: main_models.ForcePublishSkillVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ForcePublishSkillVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        if not DaraCore.is_null(request.update_latest_label):
            query['UpdateLatestLabel'] = request.update_latest_label
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ForcePublishSkillVersion',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ForcePublishSkillVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def force_publish_skill_version_with_options_async(
        self,
        request: main_models.ForcePublishSkillVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ForcePublishSkillVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        if not DaraCore.is_null(request.update_latest_label):
            query['UpdateLatestLabel'] = request.update_latest_label
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ForcePublishSkillVersion',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ForcePublishSkillVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def force_publish_skill_version(
        self,
        request: main_models.ForcePublishSkillVersionRequest,
    ) -> main_models.ForcePublishSkillVersionResponse:
        runtime = RuntimeOptions()
        return self.force_publish_skill_version_with_options(request, runtime)

    async def force_publish_skill_version_async(
        self,
        request: main_models.ForcePublishSkillVersionRequest,
    ) -> main_models.ForcePublishSkillVersionResponse:
        runtime = RuntimeOptions()
        return await self.force_publish_skill_version_with_options_async(request, runtime)

    def get_namespace_with_options(
        self,
        request: main_models.GetNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNamespace',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_namespace_with_options_async(
        self,
        request: main_models.GetNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNamespace',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_namespace(
        self,
        request: main_models.GetNamespaceRequest,
    ) -> main_models.GetNamespaceResponse:
        runtime = RuntimeOptions()
        return self.get_namespace_with_options(request, runtime)

    async def get_namespace_async(
        self,
        request: main_models.GetNamespaceRequest,
    ) -> main_models.GetNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.get_namespace_with_options_async(request, runtime)

    def get_prompt_with_options(
        self,
        request: main_models.GetPromptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPromptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrompt',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPromptResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prompt_with_options_async(
        self,
        request: main_models.GetPromptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPromptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrompt',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPromptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prompt(
        self,
        request: main_models.GetPromptRequest,
    ) -> main_models.GetPromptResponse:
        runtime = RuntimeOptions()
        return self.get_prompt_with_options(request, runtime)

    async def get_prompt_async(
        self,
        request: main_models.GetPromptRequest,
    ) -> main_models.GetPromptResponse:
        runtime = RuntimeOptions()
        return await self.get_prompt_with_options_async(request, runtime)

    def get_prompt_version_with_options(
        self,
        request: main_models.GetPromptVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPromptVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        if not DaraCore.is_null(request.prompt_version):
            query['PromptVersion'] = request.prompt_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPromptVersion',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPromptVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prompt_version_with_options_async(
        self,
        request: main_models.GetPromptVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPromptVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        if not DaraCore.is_null(request.prompt_version):
            query['PromptVersion'] = request.prompt_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPromptVersion',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPromptVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prompt_version(
        self,
        request: main_models.GetPromptVersionRequest,
    ) -> main_models.GetPromptVersionResponse:
        runtime = RuntimeOptions()
        return self.get_prompt_version_with_options(request, runtime)

    async def get_prompt_version_async(
        self,
        request: main_models.GetPromptVersionRequest,
    ) -> main_models.GetPromptVersionResponse:
        runtime = RuntimeOptions()
        return await self.get_prompt_version_with_options_async(request, runtime)

    def get_skill_detail_with_options(
        self,
        request: main_models.GetSkillDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillDetail',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_detail_with_options_async(
        self,
        request: main_models.GetSkillDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillDetail',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_detail(
        self,
        request: main_models.GetSkillDetailRequest,
    ) -> main_models.GetSkillDetailResponse:
        runtime = RuntimeOptions()
        return self.get_skill_detail_with_options(request, runtime)

    async def get_skill_detail_async(
        self,
        request: main_models.GetSkillDetailRequest,
    ) -> main_models.GetSkillDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_skill_detail_with_options_async(request, runtime)

    def get_skill_import_file_url_with_options(
        self,
        request: main_models.GetSkillImportFileUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillImportFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content_type):
            query['ContentType'] = request.content_type
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillImportFileUrl',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillImportFileUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_import_file_url_with_options_async(
        self,
        request: main_models.GetSkillImportFileUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillImportFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content_type):
            query['ContentType'] = request.content_type
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillImportFileUrl',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillImportFileUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_import_file_url(
        self,
        request: main_models.GetSkillImportFileUrlRequest,
    ) -> main_models.GetSkillImportFileUrlResponse:
        runtime = RuntimeOptions()
        return self.get_skill_import_file_url_with_options(request, runtime)

    async def get_skill_import_file_url_async(
        self,
        request: main_models.GetSkillImportFileUrlRequest,
    ) -> main_models.GetSkillImportFileUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_skill_import_file_url_with_options_async(request, runtime)

    def get_skill_version_detail_with_options(
        self,
        request: main_models.GetSkillVersionDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillVersionDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillVersionDetail',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillVersionDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_skill_version_detail_with_options_async(
        self,
        request: main_models.GetSkillVersionDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSkillVersionDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSkillVersionDetail',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSkillVersionDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_skill_version_detail(
        self,
        request: main_models.GetSkillVersionDetailRequest,
    ) -> main_models.GetSkillVersionDetailResponse:
        runtime = RuntimeOptions()
        return self.get_skill_version_detail_with_options(request, runtime)

    async def get_skill_version_detail_async(
        self,
        request: main_models.GetSkillVersionDetailRequest,
    ) -> main_models.GetSkillVersionDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_skill_version_detail_with_options_async(request, runtime)

    def list_namespaces_with_options(
        self,
        request: main_models.ListNamespacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamespaces',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_namespaces_with_options_async(
        self,
        request: main_models.ListNamespacesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamespaces',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_namespaces(
        self,
        request: main_models.ListNamespacesRequest,
    ) -> main_models.ListNamespacesResponse:
        runtime = RuntimeOptions()
        return self.list_namespaces_with_options(request, runtime)

    async def list_namespaces_async(
        self,
        request: main_models.ListNamespacesRequest,
    ) -> main_models.ListNamespacesResponse:
        runtime = RuntimeOptions()
        return await self.list_namespaces_with_options_async(request, runtime)

    def list_prompt_versions_with_options(
        self,
        request: main_models.ListPromptVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPromptVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPromptVersions',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPromptVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prompt_versions_with_options_async(
        self,
        request: main_models.ListPromptVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPromptVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPromptVersions',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPromptVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prompt_versions(
        self,
        request: main_models.ListPromptVersionsRequest,
    ) -> main_models.ListPromptVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_prompt_versions_with_options(request, runtime)

    async def list_prompt_versions_async(
        self,
        request: main_models.ListPromptVersionsRequest,
    ) -> main_models.ListPromptVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_prompt_versions_with_options_async(request, runtime)

    def list_prompts_with_options(
        self,
        request: main_models.ListPromptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPromptsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_tags):
            query['BizTags'] = request.biz_tags
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        if not DaraCore.is_null(request.search):
            query['Search'] = request.search
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrompts',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPromptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prompts_with_options_async(
        self,
        request: main_models.ListPromptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPromptsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_tags):
            query['BizTags'] = request.biz_tags
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        if not DaraCore.is_null(request.search):
            query['Search'] = request.search
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrompts',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPromptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prompts(
        self,
        request: main_models.ListPromptsRequest,
    ) -> main_models.ListPromptsResponse:
        runtime = RuntimeOptions()
        return self.list_prompts_with_options(request, runtime)

    async def list_prompts_async(
        self,
        request: main_models.ListPromptsRequest,
    ) -> main_models.ListPromptsResponse:
        runtime = RuntimeOptions()
        return await self.list_prompts_with_options_async(request, runtime)

    def list_skills_with_options(
        self,
        request: main_models.ListSkillsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.search):
            query['Search'] = request.search
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkills',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_skills_with_options_async(
        self,
        request: main_models.ListSkillsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSkillsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.search):
            query['Search'] = request.search
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSkills',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSkillsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_skills(
        self,
        request: main_models.ListSkillsRequest,
    ) -> main_models.ListSkillsResponse:
        runtime = RuntimeOptions()
        return self.list_skills_with_options(request, runtime)

    async def list_skills_async(
        self,
        request: main_models.ListSkillsRequest,
    ) -> main_models.ListSkillsResponse:
        runtime = RuntimeOptions()
        return await self.list_skills_with_options_async(request, runtime)

    def offline_skill_with_options(
        self,
        request: main_models.OfflineSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflineSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OfflineSkill',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def offline_skill_with_options_async(
        self,
        request: main_models.OfflineSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OfflineSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OfflineSkill',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OfflineSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def offline_skill(
        self,
        request: main_models.OfflineSkillRequest,
    ) -> main_models.OfflineSkillResponse:
        runtime = RuntimeOptions()
        return self.offline_skill_with_options(request, runtime)

    async def offline_skill_async(
        self,
        request: main_models.OfflineSkillRequest,
    ) -> main_models.OfflineSkillResponse:
        runtime = RuntimeOptions()
        return await self.offline_skill_with_options_async(request, runtime)

    def online_skill_with_options(
        self,
        request: main_models.OnlineSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnlineSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnlineSkill',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnlineSkillResponse(),
            self.call_api(params, req, runtime)
        )

    async def online_skill_with_options_async(
        self,
        request: main_models.OnlineSkillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OnlineSkillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OnlineSkill',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OnlineSkillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def online_skill(
        self,
        request: main_models.OnlineSkillRequest,
    ) -> main_models.OnlineSkillResponse:
        runtime = RuntimeOptions()
        return self.online_skill_with_options(request, runtime)

    async def online_skill_async(
        self,
        request: main_models.OnlineSkillRequest,
    ) -> main_models.OnlineSkillResponse:
        runtime = RuntimeOptions()
        return await self.online_skill_with_options_async(request, runtime)

    def publish_skill_version_with_options(
        self,
        request: main_models.PublishSkillVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishSkillVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        if not DaraCore.is_null(request.update_latest_label):
            query['UpdateLatestLabel'] = request.update_latest_label
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishSkillVersion',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishSkillVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_skill_version_with_options_async(
        self,
        request: main_models.PublishSkillVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PublishSkillVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        if not DaraCore.is_null(request.update_latest_label):
            query['UpdateLatestLabel'] = request.update_latest_label
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PublishSkillVersion',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishSkillVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_skill_version(
        self,
        request: main_models.PublishSkillVersionRequest,
    ) -> main_models.PublishSkillVersionResponse:
        runtime = RuntimeOptions()
        return self.publish_skill_version_with_options(request, runtime)

    async def publish_skill_version_async(
        self,
        request: main_models.PublishSkillVersionRequest,
    ) -> main_models.PublishSkillVersionResponse:
        runtime = RuntimeOptions()
        return await self.publish_skill_version_with_options_async(request, runtime)

    def submit_prompt_version_with_options(
        self,
        request: main_models.SubmitPromptVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitPromptVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        if not DaraCore.is_null(request.prompt_version):
            query['PromptVersion'] = request.prompt_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitPromptVersion',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitPromptVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_prompt_version_with_options_async(
        self,
        request: main_models.SubmitPromptVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitPromptVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        if not DaraCore.is_null(request.prompt_version):
            query['PromptVersion'] = request.prompt_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitPromptVersion',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitPromptVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_prompt_version(
        self,
        request: main_models.SubmitPromptVersionRequest,
    ) -> main_models.SubmitPromptVersionResponse:
        runtime = RuntimeOptions()
        return self.submit_prompt_version_with_options(request, runtime)

    async def submit_prompt_version_async(
        self,
        request: main_models.SubmitPromptVersionRequest,
    ) -> main_models.SubmitPromptVersionResponse:
        runtime = RuntimeOptions()
        return await self.submit_prompt_version_with_options_async(request, runtime)

    def submit_skill_version_with_options(
        self,
        request: main_models.SubmitSkillVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSkillVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSkillVersion',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSkillVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_skill_version_with_options_async(
        self,
        request: main_models.SubmitSkillVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SubmitSkillVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        if not DaraCore.is_null(request.skill_version):
            query['SkillVersion'] = request.skill_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SubmitSkillVersion',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubmitSkillVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_skill_version(
        self,
        request: main_models.SubmitSkillVersionRequest,
    ) -> main_models.SubmitSkillVersionResponse:
        runtime = RuntimeOptions()
        return self.submit_skill_version_with_options(request, runtime)

    async def submit_skill_version_async(
        self,
        request: main_models.SubmitSkillVersionRequest,
    ) -> main_models.SubmitSkillVersionResponse:
        runtime = RuntimeOptions()
        return await self.submit_skill_version_with_options_async(request, runtime)

    def update_namespace_with_options(
        self,
        request: main_models.UpdateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.scan_policy):
            query['ScanPolicy'] = request.scan_policy
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNamespace',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_namespace_with_options_async(
        self,
        request: main_models.UpdateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.scan_policy):
            query['ScanPolicy'] = request.scan_policy
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNamespace',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_namespace(
        self,
        request: main_models.UpdateNamespaceRequest,
    ) -> main_models.UpdateNamespaceResponse:
        runtime = RuntimeOptions()
        return self.update_namespace_with_options(request, runtime)

    async def update_namespace_async(
        self,
        request: main_models.UpdateNamespaceRequest,
    ) -> main_models.UpdateNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.update_namespace_with_options_async(request, runtime)

    def update_prompt_with_options(
        self,
        tmp_req: main_models.UpdatePromptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePromptResponse:
        tmp_req.validate()
        request = main_models.UpdatePromptShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_tags):
            request.biz_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_tags, 'BizTags', 'json')
        if not DaraCore.is_null(tmp_req.labels):
            request.labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_tags_shrink):
            query['BizTags'] = request.biz_tags_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrompt',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePromptResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prompt_with_options_async(
        self,
        tmp_req: main_models.UpdatePromptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePromptResponse:
        tmp_req.validate()
        request = main_models.UpdatePromptShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.biz_tags):
            request.biz_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.biz_tags, 'BizTags', 'json')
        if not DaraCore.is_null(tmp_req.labels):
            request.labels_shrink = Utils.array_to_string_with_specified_style(tmp_req.labels, 'Labels', 'json')
        query = {}
        if not DaraCore.is_null(request.biz_tags_shrink):
            query['BizTags'] = request.biz_tags_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.labels_shrink):
            query['Labels'] = request.labels_shrink
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrompt',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePromptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prompt(
        self,
        request: main_models.UpdatePromptRequest,
    ) -> main_models.UpdatePromptResponse:
        runtime = RuntimeOptions()
        return self.update_prompt_with_options(request, runtime)

    async def update_prompt_async(
        self,
        request: main_models.UpdatePromptRequest,
    ) -> main_models.UpdatePromptResponse:
        runtime = RuntimeOptions()
        return await self.update_prompt_with_options_async(request, runtime)

    def update_prompt_version_with_options(
        self,
        request: main_models.UpdatePromptVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePromptVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commit_msg):
            query['CommitMsg'] = request.commit_msg
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        if not DaraCore.is_null(request.template):
            query['Template'] = request.template
        if not DaraCore.is_null(request.variables):
            query['Variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePromptVersion',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePromptVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prompt_version_with_options_async(
        self,
        request: main_models.UpdatePromptVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePromptVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commit_msg):
            query['CommitMsg'] = request.commit_msg
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.prompt_key):
            query['PromptKey'] = request.prompt_key
        if not DaraCore.is_null(request.template):
            query['Template'] = request.template
        if not DaraCore.is_null(request.variables):
            query['Variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePromptVersion',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePromptVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prompt_version(
        self,
        request: main_models.UpdatePromptVersionRequest,
    ) -> main_models.UpdatePromptVersionResponse:
        runtime = RuntimeOptions()
        return self.update_prompt_version_with_options(request, runtime)

    async def update_prompt_version_async(
        self,
        request: main_models.UpdatePromptVersionRequest,
    ) -> main_models.UpdatePromptVersionResponse:
        runtime = RuntimeOptions()
        return await self.update_prompt_version_with_options_async(request, runtime)

    def update_skill_biz_tags_with_options(
        self,
        request: main_models.UpdateSkillBizTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillBizTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_tags):
            query['BizTags'] = request.biz_tags
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillBizTags',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillBizTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_skill_biz_tags_with_options_async(
        self,
        request: main_models.UpdateSkillBizTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillBizTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.biz_tags):
            query['BizTags'] = request.biz_tags
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillBizTags',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillBizTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_skill_biz_tags(
        self,
        request: main_models.UpdateSkillBizTagsRequest,
    ) -> main_models.UpdateSkillBizTagsResponse:
        runtime = RuntimeOptions()
        return self.update_skill_biz_tags_with_options(request, runtime)

    async def update_skill_biz_tags_async(
        self,
        request: main_models.UpdateSkillBizTagsRequest,
    ) -> main_models.UpdateSkillBizTagsResponse:
        runtime = RuntimeOptions()
        return await self.update_skill_biz_tags_with_options_async(request, runtime)

    def update_skill_draft_with_options(
        self,
        request: main_models.UpdateSkillDraftRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillDraftResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commit_msg):
            query['CommitMsg'] = request.commit_msg
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_card):
            query['SkillCard'] = request.skill_card
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillDraft',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillDraftResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_skill_draft_with_options_async(
        self,
        request: main_models.UpdateSkillDraftRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillDraftResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commit_msg):
            query['CommitMsg'] = request.commit_msg
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_card):
            query['SkillCard'] = request.skill_card
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillDraft',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillDraftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_skill_draft(
        self,
        request: main_models.UpdateSkillDraftRequest,
    ) -> main_models.UpdateSkillDraftResponse:
        runtime = RuntimeOptions()
        return self.update_skill_draft_with_options(request, runtime)

    async def update_skill_draft_async(
        self,
        request: main_models.UpdateSkillDraftRequest,
    ) -> main_models.UpdateSkillDraftResponse:
        runtime = RuntimeOptions()
        return await self.update_skill_draft_with_options_async(request, runtime)

    def update_skill_labels_with_options(
        self,
        request: main_models.UpdateSkillLabelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillLabels',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_skill_labels_with_options_async(
        self,
        request: main_models.UpdateSkillLabelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillLabelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillLabels',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_skill_labels(
        self,
        request: main_models.UpdateSkillLabelsRequest,
    ) -> main_models.UpdateSkillLabelsResponse:
        runtime = RuntimeOptions()
        return self.update_skill_labels_with_options(request, runtime)

    async def update_skill_labels_async(
        self,
        request: main_models.UpdateSkillLabelsRequest,
    ) -> main_models.UpdateSkillLabelsResponse:
        runtime = RuntimeOptions()
        return await self.update_skill_labels_with_options_async(request, runtime)

    def update_skill_scope_with_options(
        self,
        request: main_models.UpdateSkillScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillScope',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillScopeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_skill_scope_with_options_async(
        self,
        request: main_models.UpdateSkillScopeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSkillScopeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.skill_name):
            query['SkillName'] = request.skill_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSkillScope',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSkillScopeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_skill_scope(
        self,
        request: main_models.UpdateSkillScopeRequest,
    ) -> main_models.UpdateSkillScopeResponse:
        runtime = RuntimeOptions()
        return self.update_skill_scope_with_options(request, runtime)

    async def update_skill_scope_async(
        self,
        request: main_models.UpdateSkillScopeRequest,
    ) -> main_models.UpdateSkillScopeResponse:
        runtime = RuntimeOptions()
        return await self.update_skill_scope_with_options_async(request, runtime)

    def upload_skill_via_oss_with_options(
        self,
        request: main_models.UploadSkillViaOssRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadSkillViaOssResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commit_msg):
            query['CommitMsg'] = request.commit_msg
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.oss_object_name):
            query['OssObjectName'] = request.oss_object_name
        if not DaraCore.is_null(request.overwrite):
            query['Overwrite'] = request.overwrite
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadSkillViaOss',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadSkillViaOssResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_skill_via_oss_with_options_async(
        self,
        request: main_models.UploadSkillViaOssRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadSkillViaOssResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commit_msg):
            query['CommitMsg'] = request.commit_msg
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.oss_object_name):
            query['OssObjectName'] = request.oss_object_name
        if not DaraCore.is_null(request.overwrite):
            query['Overwrite'] = request.overwrite
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadSkillViaOss',
            version = '2026-03-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadSkillViaOssResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_skill_via_oss(
        self,
        request: main_models.UploadSkillViaOssRequest,
    ) -> main_models.UploadSkillViaOssResponse:
        runtime = RuntimeOptions()
        return self.upload_skill_via_oss_with_options(request, runtime)

    async def upload_skill_via_oss_async(
        self,
        request: main_models.UploadSkillViaOssRequest,
    ) -> main_models.UploadSkillViaOssResponse:
        runtime = RuntimeOptions()
        return await self.upload_skill_via_oss_with_options_async(request, runtime)
