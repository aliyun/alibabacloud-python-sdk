# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cr20181201 import models as main_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_artifact_build_task_with_options(
        self,
        request: main_models.CancelArtifactBuildTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelArtifactBuildTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_task_id):
            query['BuildTaskId'] = request.build_task_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelArtifactBuildTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelArtifactBuildTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_artifact_build_task_with_options_async(
        self,
        request: main_models.CancelArtifactBuildTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelArtifactBuildTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_task_id):
            query['BuildTaskId'] = request.build_task_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelArtifactBuildTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelArtifactBuildTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_artifact_build_task(
        self,
        request: main_models.CancelArtifactBuildTaskRequest,
    ) -> main_models.CancelArtifactBuildTaskResponse:
        runtime = RuntimeOptions()
        return self.cancel_artifact_build_task_with_options(request, runtime)

    async def cancel_artifact_build_task_async(
        self,
        request: main_models.CancelArtifactBuildTaskRequest,
    ) -> main_models.CancelArtifactBuildTaskResponse:
        runtime = RuntimeOptions()
        return await self.cancel_artifact_build_task_with_options_async(request, runtime)

    def cancel_repo_build_record_with_options(
        self,
        request: main_models.CancelRepoBuildRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelRepoBuildRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelRepoBuildRecord',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelRepoBuildRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_repo_build_record_with_options_async(
        self,
        request: main_models.CancelRepoBuildRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelRepoBuildRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelRepoBuildRecord',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelRepoBuildRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_repo_build_record(
        self,
        request: main_models.CancelRepoBuildRecordRequest,
    ) -> main_models.CancelRepoBuildRecordResponse:
        runtime = RuntimeOptions()
        return self.cancel_repo_build_record_with_options(request, runtime)

    async def cancel_repo_build_record_async(
        self,
        request: main_models.CancelRepoBuildRecordRequest,
    ) -> main_models.CancelRepoBuildRecordResponse:
        runtime = RuntimeOptions()
        return await self.cancel_repo_build_record_with_options_async(request, runtime)

    def cancel_repo_sync_task_with_options(
        self,
        request: main_models.CancelRepoSyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelRepoSyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sync_task_id):
            query['SyncTaskId'] = request.sync_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelRepoSyncTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelRepoSyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_repo_sync_task_with_options_async(
        self,
        request: main_models.CancelRepoSyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelRepoSyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sync_task_id):
            query['SyncTaskId'] = request.sync_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelRepoSyncTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelRepoSyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_repo_sync_task(
        self,
        request: main_models.CancelRepoSyncTaskRequest,
    ) -> main_models.CancelRepoSyncTaskResponse:
        runtime = RuntimeOptions()
        return self.cancel_repo_sync_task_with_options(request, runtime)

    async def cancel_repo_sync_task_async(
        self,
        request: main_models.CancelRepoSyncTaskRequest,
    ) -> main_models.CancelRepoSyncTaskResponse:
        runtime = RuntimeOptions()
        return await self.cancel_repo_sync_task_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def create_artifact_build_rule_with_options(
        self,
        tmp_req: main_models.CreateArtifactBuildRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateArtifactBuildRuleResponse:
        tmp_req.validate()
        request = main_models.CreateArtifactBuildRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.scope_id):
            query['ScopeId'] = request.scope_id
        if not DaraCore.is_null(request.scope_type):
            query['ScopeType'] = request.scope_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateArtifactBuildRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateArtifactBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_artifact_build_rule_with_options_async(
        self,
        tmp_req: main_models.CreateArtifactBuildRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateArtifactBuildRuleResponse:
        tmp_req.validate()
        request = main_models.CreateArtifactBuildRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.scope_id):
            query['ScopeId'] = request.scope_id
        if not DaraCore.is_null(request.scope_type):
            query['ScopeType'] = request.scope_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateArtifactBuildRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateArtifactBuildRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_artifact_build_rule(
        self,
        request: main_models.CreateArtifactBuildRuleRequest,
    ) -> main_models.CreateArtifactBuildRuleResponse:
        runtime = RuntimeOptions()
        return self.create_artifact_build_rule_with_options(request, runtime)

    async def create_artifact_build_rule_async(
        self,
        request: main_models.CreateArtifactBuildRuleRequest,
    ) -> main_models.CreateArtifactBuildRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_artifact_build_rule_with_options_async(request, runtime)

    def create_artifact_lifecycle_rule_with_options(
        self,
        request: main_models.CreateArtifactLifecycleRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateArtifactLifecycleRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto):
            query['Auto'] = request.auto
        if not DaraCore.is_null(request.enable_delete_tag):
            query['EnableDeleteTag'] = request.enable_delete_tag
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.retention_tag_count):
            query['RetentionTagCount'] = request.retention_tag_count
        if not DaraCore.is_null(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.tag_regexp):
            query['TagRegexp'] = request.tag_regexp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateArtifactLifecycleRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateArtifactLifecycleRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_artifact_lifecycle_rule_with_options_async(
        self,
        request: main_models.CreateArtifactLifecycleRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateArtifactLifecycleRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto):
            query['Auto'] = request.auto
        if not DaraCore.is_null(request.enable_delete_tag):
            query['EnableDeleteTag'] = request.enable_delete_tag
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.retention_tag_count):
            query['RetentionTagCount'] = request.retention_tag_count
        if not DaraCore.is_null(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.tag_regexp):
            query['TagRegexp'] = request.tag_regexp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateArtifactLifecycleRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateArtifactLifecycleRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_artifact_lifecycle_rule(
        self,
        request: main_models.CreateArtifactLifecycleRuleRequest,
    ) -> main_models.CreateArtifactLifecycleRuleResponse:
        runtime = RuntimeOptions()
        return self.create_artifact_lifecycle_rule_with_options(request, runtime)

    async def create_artifact_lifecycle_rule_async(
        self,
        request: main_models.CreateArtifactLifecycleRuleRequest,
    ) -> main_models.CreateArtifactLifecycleRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_artifact_lifecycle_rule_with_options_async(request, runtime)

    def create_artifact_subscription_rule_with_options(
        self,
        request: main_models.CreateArtifactSubscriptionRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateArtifactSubscriptionRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate):
            query['Accelerate'] = request.accelerate
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.override):
            query['Override'] = request.override
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.source_namespace_name):
            query['SourceNamespaceName'] = request.source_namespace_name
        if not DaraCore.is_null(request.source_provider):
            query['SourceProvider'] = request.source_provider
        if not DaraCore.is_null(request.source_repo_name):
            query['SourceRepoName'] = request.source_repo_name
        if not DaraCore.is_null(request.tag_count):
            query['TagCount'] = request.tag_count
        if not DaraCore.is_null(request.tag_regexp):
            query['TagRegexp'] = request.tag_regexp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateArtifactSubscriptionRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateArtifactSubscriptionRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_artifact_subscription_rule_with_options_async(
        self,
        request: main_models.CreateArtifactSubscriptionRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateArtifactSubscriptionRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate):
            query['Accelerate'] = request.accelerate
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.override):
            query['Override'] = request.override
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.source_namespace_name):
            query['SourceNamespaceName'] = request.source_namespace_name
        if not DaraCore.is_null(request.source_provider):
            query['SourceProvider'] = request.source_provider
        if not DaraCore.is_null(request.source_repo_name):
            query['SourceRepoName'] = request.source_repo_name
        if not DaraCore.is_null(request.tag_count):
            query['TagCount'] = request.tag_count
        if not DaraCore.is_null(request.tag_regexp):
            query['TagRegexp'] = request.tag_regexp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateArtifactSubscriptionRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateArtifactSubscriptionRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_artifact_subscription_rule(
        self,
        request: main_models.CreateArtifactSubscriptionRuleRequest,
    ) -> main_models.CreateArtifactSubscriptionRuleResponse:
        runtime = RuntimeOptions()
        return self.create_artifact_subscription_rule_with_options(request, runtime)

    async def create_artifact_subscription_rule_async(
        self,
        request: main_models.CreateArtifactSubscriptionRuleRequest,
    ) -> main_models.CreateArtifactSubscriptionRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_artifact_subscription_rule_with_options_async(request, runtime)

    def create_artifact_subscription_task_with_options(
        self,
        request: main_models.CreateArtifactSubscriptionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateArtifactSubscriptionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateArtifactSubscriptionTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateArtifactSubscriptionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_artifact_subscription_task_with_options_async(
        self,
        request: main_models.CreateArtifactSubscriptionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateArtifactSubscriptionTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateArtifactSubscriptionTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateArtifactSubscriptionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_artifact_subscription_task(
        self,
        request: main_models.CreateArtifactSubscriptionTaskRequest,
    ) -> main_models.CreateArtifactSubscriptionTaskResponse:
        runtime = RuntimeOptions()
        return self.create_artifact_subscription_task_with_options(request, runtime)

    async def create_artifact_subscription_task_async(
        self,
        request: main_models.CreateArtifactSubscriptionTaskRequest,
    ) -> main_models.CreateArtifactSubscriptionTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_artifact_subscription_task_with_options_async(request, runtime)

    def create_build_record_by_record_with_options(
        self,
        request: main_models.CreateBuildRecordByRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBuildRecordByRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBuildRecordByRecord',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBuildRecordByRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_build_record_by_record_with_options_async(
        self,
        request: main_models.CreateBuildRecordByRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBuildRecordByRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBuildRecordByRecord',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBuildRecordByRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_build_record_by_record(
        self,
        request: main_models.CreateBuildRecordByRecordRequest,
    ) -> main_models.CreateBuildRecordByRecordResponse:
        runtime = RuntimeOptions()
        return self.create_build_record_by_record_with_options(request, runtime)

    async def create_build_record_by_record_async(
        self,
        request: main_models.CreateBuildRecordByRecordRequest,
    ) -> main_models.CreateBuildRecordByRecordResponse:
        runtime = RuntimeOptions()
        return await self.create_build_record_by_record_with_options_async(request, runtime)

    def create_build_record_by_rule_with_options(
        self,
        request: main_models.CreateBuildRecordByRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBuildRecordByRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_rule_id):
            query['BuildRuleId'] = request.build_rule_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBuildRecordByRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBuildRecordByRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_build_record_by_rule_with_options_async(
        self,
        request: main_models.CreateBuildRecordByRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBuildRecordByRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_rule_id):
            query['BuildRuleId'] = request.build_rule_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBuildRecordByRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBuildRecordByRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_build_record_by_rule(
        self,
        request: main_models.CreateBuildRecordByRuleRequest,
    ) -> main_models.CreateBuildRecordByRuleResponse:
        runtime = RuntimeOptions()
        return self.create_build_record_by_rule_with_options(request, runtime)

    async def create_build_record_by_rule_async(
        self,
        request: main_models.CreateBuildRecordByRuleRequest,
    ) -> main_models.CreateBuildRecordByRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_build_record_by_rule_with_options_async(request, runtime)

    def create_chain_with_options(
        self,
        request: main_models.CreateChainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chain_config):
            query['ChainConfig'] = request.chain_config
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not DaraCore.is_null(request.scope_exclude):
            query['ScopeExclude'] = request.scope_exclude
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChain',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chain_with_options_async(
        self,
        request: main_models.CreateChainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chain_config):
            query['ChainConfig'] = request.chain_config
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not DaraCore.is_null(request.scope_exclude):
            query['ScopeExclude'] = request.scope_exclude
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChain',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chain(
        self,
        request: main_models.CreateChainRequest,
    ) -> main_models.CreateChainResponse:
        runtime = RuntimeOptions()
        return self.create_chain_with_options(request, runtime)

    async def create_chain_async(
        self,
        request: main_models.CreateChainRequest,
    ) -> main_models.CreateChainResponse:
        runtime = RuntimeOptions()
        return await self.create_chain_with_options_async(request, runtime)

    def create_chart_namespace_with_options(
        self,
        request: main_models.CreateChartNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChartNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not DaraCore.is_null(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChartNamespace',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChartNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chart_namespace_with_options_async(
        self,
        request: main_models.CreateChartNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChartNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not DaraCore.is_null(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChartNamespace',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChartNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chart_namespace(
        self,
        request: main_models.CreateChartNamespaceRequest,
    ) -> main_models.CreateChartNamespaceResponse:
        runtime = RuntimeOptions()
        return self.create_chart_namespace_with_options(request, runtime)

    async def create_chart_namespace_async(
        self,
        request: main_models.CreateChartNamespaceRequest,
    ) -> main_models.CreateChartNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.create_chart_namespace_with_options_async(request, runtime)

    def create_chart_repository_with_options(
        self,
        request: main_models.CreateChartRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChartRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not DaraCore.is_null(request.repo_type):
            query['RepoType'] = request.repo_type
        if not DaraCore.is_null(request.summary):
            query['Summary'] = request.summary
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChartRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChartRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_chart_repository_with_options_async(
        self,
        request: main_models.CreateChartRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChartRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not DaraCore.is_null(request.repo_type):
            query['RepoType'] = request.repo_type
        if not DaraCore.is_null(request.summary):
            query['Summary'] = request.summary
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateChartRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChartRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_chart_repository(
        self,
        request: main_models.CreateChartRepositoryRequest,
    ) -> main_models.CreateChartRepositoryResponse:
        runtime = RuntimeOptions()
        return self.create_chart_repository_with_options(request, runtime)

    async def create_chart_repository_async(
        self,
        request: main_models.CreateChartRepositoryRequest,
    ) -> main_models.CreateChartRepositoryResponse:
        runtime = RuntimeOptions()
        return await self.create_chart_repository_with_options_async(request, runtime)

    def create_instance_endpoint_acl_policy_with_options(
        self,
        request: main_models.CreateInstanceEndpointAclPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceEndpointAclPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.entry):
            query['Entry'] = request.entry
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceEndpointAclPolicy',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceEndpointAclPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_endpoint_acl_policy_with_options_async(
        self,
        request: main_models.CreateInstanceEndpointAclPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceEndpointAclPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['Comment'] = request.comment
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.entry):
            query['Entry'] = request.entry
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceEndpointAclPolicy',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceEndpointAclPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_endpoint_acl_policy(
        self,
        request: main_models.CreateInstanceEndpointAclPolicyRequest,
    ) -> main_models.CreateInstanceEndpointAclPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_instance_endpoint_acl_policy_with_options(request, runtime)

    async def create_instance_endpoint_acl_policy_async(
        self,
        request: main_models.CreateInstanceEndpointAclPolicyRequest,
    ) -> main_models.CreateInstanceEndpointAclPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_instance_endpoint_acl_policy_with_options_async(request, runtime)

    def create_instance_vpc_endpoint_linked_vpc_with_options(
        self,
        request: main_models.CreateInstanceVpcEndpointLinkedVpcRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceVpcEndpointLinkedVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_create_dnsrecord_in_pvzt):
            query['EnableCreateDNSRecordInPvzt'] = request.enable_create_dnsrecord_in_pvzt
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceVpcEndpointLinkedVpc',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceVpcEndpointLinkedVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instance_vpc_endpoint_linked_vpc_with_options_async(
        self,
        request: main_models.CreateInstanceVpcEndpointLinkedVpcRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstanceVpcEndpointLinkedVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_create_dnsrecord_in_pvzt):
            query['EnableCreateDNSRecordInPvzt'] = request.enable_create_dnsrecord_in_pvzt
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstanceVpcEndpointLinkedVpc',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstanceVpcEndpointLinkedVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instance_vpc_endpoint_linked_vpc(
        self,
        request: main_models.CreateInstanceVpcEndpointLinkedVpcRequest,
    ) -> main_models.CreateInstanceVpcEndpointLinkedVpcResponse:
        runtime = RuntimeOptions()
        return self.create_instance_vpc_endpoint_linked_vpc_with_options(request, runtime)

    async def create_instance_vpc_endpoint_linked_vpc_async(
        self,
        request: main_models.CreateInstanceVpcEndpointLinkedVpcRequest,
    ) -> main_models.CreateInstanceVpcEndpointLinkedVpcResponse:
        runtime = RuntimeOptions()
        return await self.create_instance_vpc_endpoint_linked_vpc_with_options_async(request, runtime)

    def create_namespace_with_options(
        self,
        tmp_req: main_models.CreateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNamespaceResponse:
        tmp_req.validate()
        request = main_models.CreateNamespaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.default_repo_configuration):
            request.default_repo_configuration_shrink = Utils.array_to_string_with_specified_style(tmp_req.default_repo_configuration, 'DefaultRepoConfiguration', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not DaraCore.is_null(request.default_repo_configuration_shrink):
            query['DefaultRepoConfiguration'] = request.default_repo_configuration_shrink
        if not DaraCore.is_null(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNamespace',
            version = '2018-12-01',
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
        tmp_req: main_models.CreateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNamespaceResponse:
        tmp_req.validate()
        request = main_models.CreateNamespaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.default_repo_configuration):
            request.default_repo_configuration_shrink = Utils.array_to_string_with_specified_style(tmp_req.default_repo_configuration, 'DefaultRepoConfiguration', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not DaraCore.is_null(request.default_repo_configuration_shrink):
            query['DefaultRepoConfiguration'] = request.default_repo_configuration_shrink
        if not DaraCore.is_null(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNamespace',
            version = '2018-12-01',
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

    def create_repo_build_rule_with_options(
        self,
        request: main_models.CreateRepoBuildRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoBuildRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_args):
            query['BuildArgs'] = request.build_args
        if not DaraCore.is_null(request.dockerfile_location):
            query['DockerfileLocation'] = request.dockerfile_location
        if not DaraCore.is_null(request.dockerfile_name):
            query['DockerfileName'] = request.dockerfile_name
        if not DaraCore.is_null(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.platforms):
            query['Platforms'] = request.platforms
        if not DaraCore.is_null(request.push_name):
            query['PushName'] = request.push_name
        if not DaraCore.is_null(request.push_type):
            query['PushType'] = request.push_type
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoBuildRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_build_rule_with_options_async(
        self,
        request: main_models.CreateRepoBuildRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoBuildRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_args):
            query['BuildArgs'] = request.build_args
        if not DaraCore.is_null(request.dockerfile_location):
            query['DockerfileLocation'] = request.dockerfile_location
        if not DaraCore.is_null(request.dockerfile_name):
            query['DockerfileName'] = request.dockerfile_name
        if not DaraCore.is_null(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.platforms):
            query['Platforms'] = request.platforms
        if not DaraCore.is_null(request.push_name):
            query['PushName'] = request.push_name
        if not DaraCore.is_null(request.push_type):
            query['PushType'] = request.push_type
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoBuildRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoBuildRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repo_build_rule(
        self,
        request: main_models.CreateRepoBuildRuleRequest,
    ) -> main_models.CreateRepoBuildRuleResponse:
        runtime = RuntimeOptions()
        return self.create_repo_build_rule_with_options(request, runtime)

    async def create_repo_build_rule_async(
        self,
        request: main_models.CreateRepoBuildRuleRequest,
    ) -> main_models.CreateRepoBuildRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_repo_build_rule_with_options_async(request, runtime)

    def create_repo_source_code_repo_with_options(
        self,
        request: main_models.CreateRepoSourceCodeRepoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoSourceCodeRepoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_build):
            query['AutoBuild'] = request.auto_build
        if not DaraCore.is_null(request.code_repo_name):
            query['CodeRepoName'] = request.code_repo_name
        if not DaraCore.is_null(request.code_repo_namespace_name):
            query['CodeRepoNamespaceName'] = request.code_repo_namespace_name
        if not DaraCore.is_null(request.code_repo_type):
            query['CodeRepoType'] = request.code_repo_type
        if not DaraCore.is_null(request.disable_cache_build):
            query['DisableCacheBuild'] = request.disable_cache_build
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.oversea_build):
            query['OverseaBuild'] = request.oversea_build
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoSourceCodeRepo',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoSourceCodeRepoResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_source_code_repo_with_options_async(
        self,
        request: main_models.CreateRepoSourceCodeRepoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoSourceCodeRepoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_build):
            query['AutoBuild'] = request.auto_build
        if not DaraCore.is_null(request.code_repo_name):
            query['CodeRepoName'] = request.code_repo_name
        if not DaraCore.is_null(request.code_repo_namespace_name):
            query['CodeRepoNamespaceName'] = request.code_repo_namespace_name
        if not DaraCore.is_null(request.code_repo_type):
            query['CodeRepoType'] = request.code_repo_type
        if not DaraCore.is_null(request.disable_cache_build):
            query['DisableCacheBuild'] = request.disable_cache_build
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.oversea_build):
            query['OverseaBuild'] = request.oversea_build
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoSourceCodeRepo',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoSourceCodeRepoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repo_source_code_repo(
        self,
        request: main_models.CreateRepoSourceCodeRepoRequest,
    ) -> main_models.CreateRepoSourceCodeRepoResponse:
        runtime = RuntimeOptions()
        return self.create_repo_source_code_repo_with_options(request, runtime)

    async def create_repo_source_code_repo_async(
        self,
        request: main_models.CreateRepoSourceCodeRepoRequest,
    ) -> main_models.CreateRepoSourceCodeRepoResponse:
        runtime = RuntimeOptions()
        return await self.create_repo_source_code_repo_with_options_async(request, runtime)

    def create_repo_sync_rule_with_options(
        self,
        request: main_models.CreateRepoSyncRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoSyncRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_name_filter):
            query['RepoNameFilter'] = request.repo_name_filter
        if not DaraCore.is_null(request.sync_rule_name):
            query['SyncRuleName'] = request.sync_rule_name
        if not DaraCore.is_null(request.sync_scope):
            query['SyncScope'] = request.sync_scope
        if not DaraCore.is_null(request.sync_trigger):
            query['SyncTrigger'] = request.sync_trigger
        if not DaraCore.is_null(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        if not DaraCore.is_null(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        if not DaraCore.is_null(request.target_namespace_name):
            query['TargetNamespaceName'] = request.target_namespace_name
        if not DaraCore.is_null(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        if not DaraCore.is_null(request.target_repo_name):
            query['TargetRepoName'] = request.target_repo_name
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoSyncRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoSyncRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_sync_rule_with_options_async(
        self,
        request: main_models.CreateRepoSyncRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoSyncRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_name_filter):
            query['RepoNameFilter'] = request.repo_name_filter
        if not DaraCore.is_null(request.sync_rule_name):
            query['SyncRuleName'] = request.sync_rule_name
        if not DaraCore.is_null(request.sync_scope):
            query['SyncScope'] = request.sync_scope
        if not DaraCore.is_null(request.sync_trigger):
            query['SyncTrigger'] = request.sync_trigger
        if not DaraCore.is_null(request.tag_filter):
            query['TagFilter'] = request.tag_filter
        if not DaraCore.is_null(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        if not DaraCore.is_null(request.target_namespace_name):
            query['TargetNamespaceName'] = request.target_namespace_name
        if not DaraCore.is_null(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        if not DaraCore.is_null(request.target_repo_name):
            query['TargetRepoName'] = request.target_repo_name
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoSyncRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoSyncRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repo_sync_rule(
        self,
        request: main_models.CreateRepoSyncRuleRequest,
    ) -> main_models.CreateRepoSyncRuleResponse:
        runtime = RuntimeOptions()
        return self.create_repo_sync_rule_with_options(request, runtime)

    async def create_repo_sync_rule_async(
        self,
        request: main_models.CreateRepoSyncRuleRequest,
    ) -> main_models.CreateRepoSyncRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_repo_sync_rule_with_options_async(request, runtime)

    def create_repo_sync_task_with_options(
        self,
        request: main_models.CreateRepoSyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoSyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.override):
            query['Override'] = request.override
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        if not DaraCore.is_null(request.target_namespace):
            query['TargetNamespace'] = request.target_namespace
        if not DaraCore.is_null(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        if not DaraCore.is_null(request.target_repo_name):
            query['TargetRepoName'] = request.target_repo_name
        if not DaraCore.is_null(request.target_tag):
            query['TargetTag'] = request.target_tag
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoSyncTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoSyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_sync_task_with_options_async(
        self,
        request: main_models.CreateRepoSyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoSyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.override):
            query['Override'] = request.override
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        if not DaraCore.is_null(request.target_namespace):
            query['TargetNamespace'] = request.target_namespace
        if not DaraCore.is_null(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        if not DaraCore.is_null(request.target_repo_name):
            query['TargetRepoName'] = request.target_repo_name
        if not DaraCore.is_null(request.target_tag):
            query['TargetTag'] = request.target_tag
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoSyncTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoSyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repo_sync_task(
        self,
        request: main_models.CreateRepoSyncTaskRequest,
    ) -> main_models.CreateRepoSyncTaskResponse:
        runtime = RuntimeOptions()
        return self.create_repo_sync_task_with_options(request, runtime)

    async def create_repo_sync_task_async(
        self,
        request: main_models.CreateRepoSyncTaskRequest,
    ) -> main_models.CreateRepoSyncTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_repo_sync_task_with_options_async(request, runtime)

    def create_repo_sync_task_by_rule_with_options(
        self,
        request: main_models.CreateRepoSyncTaskByRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoSyncTaskByRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.sync_rule_id):
            query['SyncRuleId'] = request.sync_rule_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoSyncTaskByRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoSyncTaskByRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_sync_task_by_rule_with_options_async(
        self,
        request: main_models.CreateRepoSyncTaskByRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoSyncTaskByRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.sync_rule_id):
            query['SyncRuleId'] = request.sync_rule_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoSyncTaskByRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoSyncTaskByRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repo_sync_task_by_rule(
        self,
        request: main_models.CreateRepoSyncTaskByRuleRequest,
    ) -> main_models.CreateRepoSyncTaskByRuleResponse:
        runtime = RuntimeOptions()
        return self.create_repo_sync_task_by_rule_with_options(request, runtime)

    async def create_repo_sync_task_by_rule_async(
        self,
        request: main_models.CreateRepoSyncTaskByRuleRequest,
    ) -> main_models.CreateRepoSyncTaskByRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_repo_sync_task_by_rule_with_options_async(request, runtime)

    def create_repo_tag_with_options(
        self,
        request: main_models.CreateRepoTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_tag):
            query['FromTag'] = request.from_tag
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.to_tag):
            query['ToTag'] = request.to_tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoTag',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_tag_with_options_async(
        self,
        request: main_models.CreateRepoTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_tag):
            query['FromTag'] = request.from_tag
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.to_tag):
            query['ToTag'] = request.to_tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoTag',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repo_tag(
        self,
        request: main_models.CreateRepoTagRequest,
    ) -> main_models.CreateRepoTagResponse:
        runtime = RuntimeOptions()
        return self.create_repo_tag_with_options(request, runtime)

    async def create_repo_tag_async(
        self,
        request: main_models.CreateRepoTagRequest,
    ) -> main_models.CreateRepoTagResponse:
        runtime = RuntimeOptions()
        return await self.create_repo_tag_with_options_async(request, runtime)

    def create_repo_tag_scan_task_with_options(
        self,
        request: main_models.CreateRepoTagScanTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoTagScanTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.digest):
            query['Digest'] = request.digest
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.scan_service):
            query['ScanService'] = request.scan_service
        if not DaraCore.is_null(request.scan_type):
            query['ScanType'] = request.scan_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoTagScanTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoTagScanTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_tag_scan_task_with_options_async(
        self,
        request: main_models.CreateRepoTagScanTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoTagScanTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.digest):
            query['Digest'] = request.digest
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.scan_service):
            query['ScanService'] = request.scan_service
        if not DaraCore.is_null(request.scan_type):
            query['ScanType'] = request.scan_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoTagScanTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoTagScanTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repo_tag_scan_task(
        self,
        request: main_models.CreateRepoTagScanTaskRequest,
    ) -> main_models.CreateRepoTagScanTaskResponse:
        runtime = RuntimeOptions()
        return self.create_repo_tag_scan_task_with_options(request, runtime)

    async def create_repo_tag_scan_task_async(
        self,
        request: main_models.CreateRepoTagScanTaskRequest,
    ) -> main_models.CreateRepoTagScanTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_repo_tag_scan_task_with_options_async(request, runtime)

    def create_repo_trigger_with_options(
        self,
        request: main_models.CreateRepoTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.trigger_name):
            query['TriggerName'] = request.trigger_name
        if not DaraCore.is_null(request.trigger_tag):
            query['TriggerTag'] = request.trigger_tag
        if not DaraCore.is_null(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not DaraCore.is_null(request.trigger_url):
            query['TriggerUrl'] = request.trigger_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoTrigger',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_trigger_with_options_async(
        self,
        request: main_models.CreateRepoTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.trigger_name):
            query['TriggerName'] = request.trigger_name
        if not DaraCore.is_null(request.trigger_tag):
            query['TriggerTag'] = request.trigger_tag
        if not DaraCore.is_null(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not DaraCore.is_null(request.trigger_url):
            query['TriggerUrl'] = request.trigger_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoTrigger',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repo_trigger(
        self,
        request: main_models.CreateRepoTriggerRequest,
    ) -> main_models.CreateRepoTriggerResponse:
        runtime = RuntimeOptions()
        return self.create_repo_trigger_with_options(request, runtime)

    async def create_repo_trigger_async(
        self,
        request: main_models.CreateRepoTriggerRequest,
    ) -> main_models.CreateRepoTriggerResponse:
        runtime = RuntimeOptions()
        return await self.create_repo_trigger_with_options_async(request, runtime)

    def create_repository_with_options(
        self,
        request: main_models.CreateRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.detail):
            query['Detail'] = request.detail
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not DaraCore.is_null(request.repo_type):
            query['RepoType'] = request.repo_type
        if not DaraCore.is_null(request.summary):
            query['Summary'] = request.summary
        if not DaraCore.is_null(request.tag_immutability):
            query['TagImmutability'] = request.tag_immutability
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repository_with_options_async(
        self,
        request: main_models.CreateRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.detail):
            query['Detail'] = request.detail
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not DaraCore.is_null(request.repo_type):
            query['RepoType'] = request.repo_type
        if not DaraCore.is_null(request.summary):
            query['Summary'] = request.summary
        if not DaraCore.is_null(request.tag_immutability):
            query['TagImmutability'] = request.tag_immutability
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repository(
        self,
        request: main_models.CreateRepositoryRequest,
    ) -> main_models.CreateRepositoryResponse:
        runtime = RuntimeOptions()
        return self.create_repository_with_options(request, runtime)

    async def create_repository_async(
        self,
        request: main_models.CreateRepositoryRequest,
    ) -> main_models.CreateRepositoryResponse:
        runtime = RuntimeOptions()
        return await self.create_repository_with_options_async(request, runtime)

    def create_scan_rule_with_options(
        self,
        tmp_req: main_models.CreateScanRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScanRuleResponse:
        tmp_req.validate()
        request = main_models.CreateScanRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.namespaces):
            request.namespaces_shrink = Utils.array_to_string_with_specified_style(tmp_req.namespaces, 'Namespaces', 'json')
        if not DaraCore.is_null(tmp_req.repo_names):
            request.repo_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.repo_names, 'RepoNames', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespaces_shrink):
            query['Namespaces'] = request.namespaces_shrink
        if not DaraCore.is_null(request.repo_names_shrink):
            query['RepoNames'] = request.repo_names_shrink
        if not DaraCore.is_null(request.repo_tag_filter_pattern):
            query['RepoTagFilterPattern'] = request.repo_tag_filter_pattern
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.scan_scope):
            query['ScanScope'] = request.scan_scope
        if not DaraCore.is_null(request.scan_type):
            query['ScanType'] = request.scan_type
        if not DaraCore.is_null(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScanRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScanRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scan_rule_with_options_async(
        self,
        tmp_req: main_models.CreateScanRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScanRuleResponse:
        tmp_req.validate()
        request = main_models.CreateScanRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.namespaces):
            request.namespaces_shrink = Utils.array_to_string_with_specified_style(tmp_req.namespaces, 'Namespaces', 'json')
        if not DaraCore.is_null(tmp_req.repo_names):
            request.repo_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.repo_names, 'RepoNames', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespaces_shrink):
            query['Namespaces'] = request.namespaces_shrink
        if not DaraCore.is_null(request.repo_names_shrink):
            query['RepoNames'] = request.repo_names_shrink
        if not DaraCore.is_null(request.repo_tag_filter_pattern):
            query['RepoTagFilterPattern'] = request.repo_tag_filter_pattern
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.scan_scope):
            query['ScanScope'] = request.scan_scope
        if not DaraCore.is_null(request.scan_type):
            query['ScanType'] = request.scan_type
        if not DaraCore.is_null(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScanRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScanRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_scan_rule(
        self,
        request: main_models.CreateScanRuleRequest,
    ) -> main_models.CreateScanRuleResponse:
        runtime = RuntimeOptions()
        return self.create_scan_rule_with_options(request, runtime)

    async def create_scan_rule_async(
        self,
        request: main_models.CreateScanRuleRequest,
    ) -> main_models.CreateScanRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_scan_rule_with_options_async(request, runtime)

    def create_storage_domain_routing_rule_with_options(
        self,
        tmp_req: main_models.CreateStorageDomainRoutingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStorageDomainRoutingRuleResponse:
        tmp_req.validate()
        request = main_models.CreateStorageDomainRoutingRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.routes):
            request.routes_shrink = Utils.array_to_string_with_specified_style(tmp_req.routes, 'Routes', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.routes_shrink):
            query['Routes'] = request.routes_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStorageDomainRoutingRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStorageDomainRoutingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_storage_domain_routing_rule_with_options_async(
        self,
        tmp_req: main_models.CreateStorageDomainRoutingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStorageDomainRoutingRuleResponse:
        tmp_req.validate()
        request = main_models.CreateStorageDomainRoutingRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.routes):
            request.routes_shrink = Utils.array_to_string_with_specified_style(tmp_req.routes, 'Routes', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.routes_shrink):
            query['Routes'] = request.routes_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStorageDomainRoutingRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStorageDomainRoutingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_storage_domain_routing_rule(
        self,
        request: main_models.CreateStorageDomainRoutingRuleRequest,
    ) -> main_models.CreateStorageDomainRoutingRuleResponse:
        runtime = RuntimeOptions()
        return self.create_storage_domain_routing_rule_with_options(request, runtime)

    async def create_storage_domain_routing_rule_async(
        self,
        request: main_models.CreateStorageDomainRoutingRuleRequest,
    ) -> main_models.CreateStorageDomainRoutingRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_storage_domain_routing_rule_with_options_async(request, runtime)

    def delete_artifact_lifecycle_rule_with_options(
        self,
        request: main_models.DeleteArtifactLifecycleRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteArtifactLifecycleRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteArtifactLifecycleRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteArtifactLifecycleRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_artifact_lifecycle_rule_with_options_async(
        self,
        request: main_models.DeleteArtifactLifecycleRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteArtifactLifecycleRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteArtifactLifecycleRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteArtifactLifecycleRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_artifact_lifecycle_rule(
        self,
        request: main_models.DeleteArtifactLifecycleRuleRequest,
    ) -> main_models.DeleteArtifactLifecycleRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_artifact_lifecycle_rule_with_options(request, runtime)

    async def delete_artifact_lifecycle_rule_async(
        self,
        request: main_models.DeleteArtifactLifecycleRuleRequest,
    ) -> main_models.DeleteArtifactLifecycleRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_artifact_lifecycle_rule_with_options_async(request, runtime)

    def delete_artifact_subscription_rule_with_options(
        self,
        request: main_models.DeleteArtifactSubscriptionRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteArtifactSubscriptionRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteArtifactSubscriptionRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteArtifactSubscriptionRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_artifact_subscription_rule_with_options_async(
        self,
        request: main_models.DeleteArtifactSubscriptionRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteArtifactSubscriptionRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteArtifactSubscriptionRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteArtifactSubscriptionRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_artifact_subscription_rule(
        self,
        request: main_models.DeleteArtifactSubscriptionRuleRequest,
    ) -> main_models.DeleteArtifactSubscriptionRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_artifact_subscription_rule_with_options(request, runtime)

    async def delete_artifact_subscription_rule_async(
        self,
        request: main_models.DeleteArtifactSubscriptionRuleRequest,
    ) -> main_models.DeleteArtifactSubscriptionRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_artifact_subscription_rule_with_options_async(request, runtime)

    def delete_chain_with_options(
        self,
        request: main_models.DeleteChainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chain_id):
            query['ChainId'] = request.chain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChain',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chain_with_options_async(
        self,
        request: main_models.DeleteChainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chain_id):
            query['ChainId'] = request.chain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChain',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chain(
        self,
        request: main_models.DeleteChainRequest,
    ) -> main_models.DeleteChainResponse:
        runtime = RuntimeOptions()
        return self.delete_chain_with_options(request, runtime)

    async def delete_chain_async(
        self,
        request: main_models.DeleteChainRequest,
    ) -> main_models.DeleteChainResponse:
        runtime = RuntimeOptions()
        return await self.delete_chain_with_options_async(request, runtime)

    def delete_chart_namespace_with_options(
        self,
        request: main_models.DeleteChartNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChartNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChartNamespace',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChartNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chart_namespace_with_options_async(
        self,
        request: main_models.DeleteChartNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChartNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChartNamespace',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChartNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chart_namespace(
        self,
        request: main_models.DeleteChartNamespaceRequest,
    ) -> main_models.DeleteChartNamespaceResponse:
        runtime = RuntimeOptions()
        return self.delete_chart_namespace_with_options(request, runtime)

    async def delete_chart_namespace_async(
        self,
        request: main_models.DeleteChartNamespaceRequest,
    ) -> main_models.DeleteChartNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.delete_chart_namespace_with_options_async(request, runtime)

    def delete_chart_release_with_options(
        self,
        request: main_models.DeleteChartReleaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChartReleaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chart):
            query['Chart'] = request.chart
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChartRelease',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChartReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chart_release_with_options_async(
        self,
        request: main_models.DeleteChartReleaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChartReleaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chart):
            query['Chart'] = request.chart
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.release):
            query['Release'] = request.release
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChartRelease',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChartReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chart_release(
        self,
        request: main_models.DeleteChartReleaseRequest,
    ) -> main_models.DeleteChartReleaseResponse:
        runtime = RuntimeOptions()
        return self.delete_chart_release_with_options(request, runtime)

    async def delete_chart_release_async(
        self,
        request: main_models.DeleteChartReleaseRequest,
    ) -> main_models.DeleteChartReleaseResponse:
        runtime = RuntimeOptions()
        return await self.delete_chart_release_with_options_async(request, runtime)

    def delete_chart_repository_with_options(
        self,
        request: main_models.DeleteChartRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChartRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChartRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChartRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_chart_repository_with_options_async(
        self,
        request: main_models.DeleteChartRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChartRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChartRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChartRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_chart_repository(
        self,
        request: main_models.DeleteChartRepositoryRequest,
    ) -> main_models.DeleteChartRepositoryResponse:
        runtime = RuntimeOptions()
        return self.delete_chart_repository_with_options(request, runtime)

    async def delete_chart_repository_async(
        self,
        request: main_models.DeleteChartRepositoryRequest,
    ) -> main_models.DeleteChartRepositoryResponse:
        runtime = RuntimeOptions()
        return await self.delete_chart_repository_with_options_async(request, runtime)

    def delete_event_center_rule_with_options(
        self,
        request: main_models.DeleteEventCenterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventCenterRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventCenterRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventCenterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_center_rule_with_options_async(
        self,
        request: main_models.DeleteEventCenterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventCenterRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventCenterRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventCenterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_center_rule(
        self,
        request: main_models.DeleteEventCenterRuleRequest,
    ) -> main_models.DeleteEventCenterRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_event_center_rule_with_options(request, runtime)

    async def delete_event_center_rule_async(
        self,
        request: main_models.DeleteEventCenterRuleRequest,
    ) -> main_models.DeleteEventCenterRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_event_center_rule_with_options_async(request, runtime)

    def delete_instance_endpoint_acl_policy_with_options(
        self,
        request: main_models.DeleteInstanceEndpointAclPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceEndpointAclPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.entry):
            query['Entry'] = request.entry
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceEndpointAclPolicy',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceEndpointAclPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_endpoint_acl_policy_with_options_async(
        self,
        request: main_models.DeleteInstanceEndpointAclPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceEndpointAclPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.entry):
            query['Entry'] = request.entry
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceEndpointAclPolicy',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceEndpointAclPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_endpoint_acl_policy(
        self,
        request: main_models.DeleteInstanceEndpointAclPolicyRequest,
    ) -> main_models.DeleteInstanceEndpointAclPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_instance_endpoint_acl_policy_with_options(request, runtime)

    async def delete_instance_endpoint_acl_policy_async(
        self,
        request: main_models.DeleteInstanceEndpointAclPolicyRequest,
    ) -> main_models.DeleteInstanceEndpointAclPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_instance_endpoint_acl_policy_with_options_async(request, runtime)

    def delete_instance_vpc_endpoint_linked_vpc_with_options(
        self,
        request: main_models.DeleteInstanceVpcEndpointLinkedVpcRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceVpcEndpointLinkedVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceVpcEndpointLinkedVpc',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceVpcEndpointLinkedVpcResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_instance_vpc_endpoint_linked_vpc_with_options_async(
        self,
        request: main_models.DeleteInstanceVpcEndpointLinkedVpcRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteInstanceVpcEndpointLinkedVpcResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not DaraCore.is_null(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteInstanceVpcEndpointLinkedVpc',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteInstanceVpcEndpointLinkedVpcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_instance_vpc_endpoint_linked_vpc(
        self,
        request: main_models.DeleteInstanceVpcEndpointLinkedVpcRequest,
    ) -> main_models.DeleteInstanceVpcEndpointLinkedVpcResponse:
        runtime = RuntimeOptions()
        return self.delete_instance_vpc_endpoint_linked_vpc_with_options(request, runtime)

    async def delete_instance_vpc_endpoint_linked_vpc_async(
        self,
        request: main_models.DeleteInstanceVpcEndpointLinkedVpcRequest,
    ) -> main_models.DeleteInstanceVpcEndpointLinkedVpcResponse:
        runtime = RuntimeOptions()
        return await self.delete_instance_vpc_endpoint_linked_vpc_with_options_async(request, runtime)

    def delete_namespace_with_options(
        self,
        request: main_models.DeleteNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNamespace',
            version = '2018-12-01',
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
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNamespace',
            version = '2018-12-01',
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

    def delete_repo_build_rule_with_options(
        self,
        request: main_models.DeleteRepoBuildRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRepoBuildRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_rule_id):
            query['BuildRuleId'] = request.build_rule_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRepoBuildRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repo_build_rule_with_options_async(
        self,
        request: main_models.DeleteRepoBuildRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRepoBuildRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_rule_id):
            query['BuildRuleId'] = request.build_rule_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRepoBuildRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRepoBuildRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repo_build_rule(
        self,
        request: main_models.DeleteRepoBuildRuleRequest,
    ) -> main_models.DeleteRepoBuildRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_repo_build_rule_with_options(request, runtime)

    async def delete_repo_build_rule_async(
        self,
        request: main_models.DeleteRepoBuildRuleRequest,
    ) -> main_models.DeleteRepoBuildRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_repo_build_rule_with_options_async(request, runtime)

    def delete_repo_sync_rule_with_options(
        self,
        request: main_models.DeleteRepoSyncRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRepoSyncRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sync_rule_id):
            query['SyncRuleId'] = request.sync_rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRepoSyncRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRepoSyncRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repo_sync_rule_with_options_async(
        self,
        request: main_models.DeleteRepoSyncRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRepoSyncRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sync_rule_id):
            query['SyncRuleId'] = request.sync_rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRepoSyncRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRepoSyncRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repo_sync_rule(
        self,
        request: main_models.DeleteRepoSyncRuleRequest,
    ) -> main_models.DeleteRepoSyncRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_repo_sync_rule_with_options(request, runtime)

    async def delete_repo_sync_rule_async(
        self,
        request: main_models.DeleteRepoSyncRuleRequest,
    ) -> main_models.DeleteRepoSyncRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_repo_sync_rule_with_options_async(request, runtime)

    def delete_repo_tag_with_options(
        self,
        request: main_models.DeleteRepoTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRepoTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRepoTag',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRepoTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repo_tag_with_options_async(
        self,
        request: main_models.DeleteRepoTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRepoTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRepoTag',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRepoTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repo_tag(
        self,
        request: main_models.DeleteRepoTagRequest,
    ) -> main_models.DeleteRepoTagResponse:
        runtime = RuntimeOptions()
        return self.delete_repo_tag_with_options(request, runtime)

    async def delete_repo_tag_async(
        self,
        request: main_models.DeleteRepoTagRequest,
    ) -> main_models.DeleteRepoTagResponse:
        runtime = RuntimeOptions()
        return await self.delete_repo_tag_with_options_async(request, runtime)

    def delete_repo_trigger_with_options(
        self,
        request: main_models.DeleteRepoTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRepoTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.trigger_id):
            query['TriggerId'] = request.trigger_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRepoTrigger',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRepoTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repo_trigger_with_options_async(
        self,
        request: main_models.DeleteRepoTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRepoTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.trigger_id):
            query['TriggerId'] = request.trigger_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRepoTrigger',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRepoTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repo_trigger(
        self,
        request: main_models.DeleteRepoTriggerRequest,
    ) -> main_models.DeleteRepoTriggerResponse:
        runtime = RuntimeOptions()
        return self.delete_repo_trigger_with_options(request, runtime)

    async def delete_repo_trigger_async(
        self,
        request: main_models.DeleteRepoTriggerRequest,
    ) -> main_models.DeleteRepoTriggerResponse:
        runtime = RuntimeOptions()
        return await self.delete_repo_trigger_with_options_async(request, runtime)

    def delete_repository_with_options(
        self,
        request: main_models.DeleteRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_repository_with_options_async(
        self,
        request: main_models.DeleteRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_repository(
        self,
        request: main_models.DeleteRepositoryRequest,
    ) -> main_models.DeleteRepositoryResponse:
        runtime = RuntimeOptions()
        return self.delete_repository_with_options(request, runtime)

    async def delete_repository_async(
        self,
        request: main_models.DeleteRepositoryRequest,
    ) -> main_models.DeleteRepositoryResponse:
        runtime = RuntimeOptions()
        return await self.delete_repository_with_options_async(request, runtime)

    def delete_scan_rule_with_options(
        self,
        request: main_models.DeleteScanRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScanRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.scan_rule_id):
            query['ScanRuleId'] = request.scan_rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScanRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScanRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scan_rule_with_options_async(
        self,
        request: main_models.DeleteScanRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScanRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.scan_rule_id):
            query['ScanRuleId'] = request.scan_rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScanRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScanRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scan_rule(
        self,
        request: main_models.DeleteScanRuleRequest,
    ) -> main_models.DeleteScanRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_scan_rule_with_options(request, runtime)

    async def delete_scan_rule_async(
        self,
        request: main_models.DeleteScanRuleRequest,
    ) -> main_models.DeleteScanRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_scan_rule_with_options_async(request, runtime)

    def delete_storage_domain_routing_rule_with_options(
        self,
        request: main_models.DeleteStorageDomainRoutingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStorageDomainRoutingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStorageDomainRoutingRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStorageDomainRoutingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_storage_domain_routing_rule_with_options_async(
        self,
        request: main_models.DeleteStorageDomainRoutingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStorageDomainRoutingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStorageDomainRoutingRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStorageDomainRoutingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_storage_domain_routing_rule(
        self,
        request: main_models.DeleteStorageDomainRoutingRuleRequest,
    ) -> main_models.DeleteStorageDomainRoutingRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_storage_domain_routing_rule_with_options(request, runtime)

    async def delete_storage_domain_routing_rule_async(
        self,
        request: main_models.DeleteStorageDomainRoutingRuleRequest,
    ) -> main_models.DeleteStorageDomainRoutingRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_storage_domain_routing_rule_with_options_async(request, runtime)

    def get_artifact_build_rule_with_options(
        self,
        request: main_models.GetArtifactBuildRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactBuildRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifactBuildRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArtifactBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_artifact_build_rule_with_options_async(
        self,
        request: main_models.GetArtifactBuildRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactBuildRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifactBuildRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArtifactBuildRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_artifact_build_rule(
        self,
        request: main_models.GetArtifactBuildRuleRequest,
    ) -> main_models.GetArtifactBuildRuleResponse:
        runtime = RuntimeOptions()
        return self.get_artifact_build_rule_with_options(request, runtime)

    async def get_artifact_build_rule_async(
        self,
        request: main_models.GetArtifactBuildRuleRequest,
    ) -> main_models.GetArtifactBuildRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_artifact_build_rule_with_options_async(request, runtime)

    def get_artifact_build_task_with_options(
        self,
        request: main_models.GetArtifactBuildTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactBuildTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifactBuildTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArtifactBuildTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_artifact_build_task_with_options_async(
        self,
        request: main_models.GetArtifactBuildTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactBuildTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifactBuildTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArtifactBuildTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_artifact_build_task(
        self,
        request: main_models.GetArtifactBuildTaskRequest,
    ) -> main_models.GetArtifactBuildTaskResponse:
        runtime = RuntimeOptions()
        return self.get_artifact_build_task_with_options(request, runtime)

    async def get_artifact_build_task_async(
        self,
        request: main_models.GetArtifactBuildTaskRequest,
    ) -> main_models.GetArtifactBuildTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_artifact_build_task_with_options_async(request, runtime)

    def get_artifact_lifecycle_rule_with_options(
        self,
        request: main_models.GetArtifactLifecycleRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactLifecycleRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifactLifecycleRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArtifactLifecycleRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_artifact_lifecycle_rule_with_options_async(
        self,
        request: main_models.GetArtifactLifecycleRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactLifecycleRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifactLifecycleRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArtifactLifecycleRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_artifact_lifecycle_rule(
        self,
        request: main_models.GetArtifactLifecycleRuleRequest,
    ) -> main_models.GetArtifactLifecycleRuleResponse:
        runtime = RuntimeOptions()
        return self.get_artifact_lifecycle_rule_with_options(request, runtime)

    async def get_artifact_lifecycle_rule_async(
        self,
        request: main_models.GetArtifactLifecycleRuleRequest,
    ) -> main_models.GetArtifactLifecycleRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_artifact_lifecycle_rule_with_options_async(request, runtime)

    def get_artifact_subscription_rule_with_options(
        self,
        request: main_models.GetArtifactSubscriptionRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactSubscriptionRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifactSubscriptionRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArtifactSubscriptionRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_artifact_subscription_rule_with_options_async(
        self,
        request: main_models.GetArtifactSubscriptionRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactSubscriptionRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifactSubscriptionRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArtifactSubscriptionRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_artifact_subscription_rule(
        self,
        request: main_models.GetArtifactSubscriptionRuleRequest,
    ) -> main_models.GetArtifactSubscriptionRuleResponse:
        runtime = RuntimeOptions()
        return self.get_artifact_subscription_rule_with_options(request, runtime)

    async def get_artifact_subscription_rule_async(
        self,
        request: main_models.GetArtifactSubscriptionRuleRequest,
    ) -> main_models.GetArtifactSubscriptionRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_artifact_subscription_rule_with_options_async(request, runtime)

    def get_artifact_subscription_task_with_options(
        self,
        request: main_models.GetArtifactSubscriptionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactSubscriptionTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifactSubscriptionTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArtifactSubscriptionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_artifact_subscription_task_with_options_async(
        self,
        request: main_models.GetArtifactSubscriptionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactSubscriptionTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifactSubscriptionTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArtifactSubscriptionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_artifact_subscription_task(
        self,
        request: main_models.GetArtifactSubscriptionTaskRequest,
    ) -> main_models.GetArtifactSubscriptionTaskResponse:
        runtime = RuntimeOptions()
        return self.get_artifact_subscription_task_with_options(request, runtime)

    async def get_artifact_subscription_task_async(
        self,
        request: main_models.GetArtifactSubscriptionTaskRequest,
    ) -> main_models.GetArtifactSubscriptionTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_artifact_subscription_task_with_options_async(request, runtime)

    def get_artifact_subscription_task_result_with_options(
        self,
        request: main_models.GetArtifactSubscriptionTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactSubscriptionTaskResultResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifactSubscriptionTaskResult',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArtifactSubscriptionTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_artifact_subscription_task_result_with_options_async(
        self,
        request: main_models.GetArtifactSubscriptionTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactSubscriptionTaskResultResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifactSubscriptionTaskResult',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArtifactSubscriptionTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_artifact_subscription_task_result(
        self,
        request: main_models.GetArtifactSubscriptionTaskResultRequest,
    ) -> main_models.GetArtifactSubscriptionTaskResultResponse:
        runtime = RuntimeOptions()
        return self.get_artifact_subscription_task_result_with_options(request, runtime)

    async def get_artifact_subscription_task_result_async(
        self,
        request: main_models.GetArtifactSubscriptionTaskResultRequest,
    ) -> main_models.GetArtifactSubscriptionTaskResultResponse:
        runtime = RuntimeOptions()
        return await self.get_artifact_subscription_task_result_with_options_async(request, runtime)

    def get_authorization_token_with_options(
        self,
        request: main_models.GetAuthorizationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuthorizationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAuthorizationToken',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuthorizationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_authorization_token_with_options_async(
        self,
        request: main_models.GetAuthorizationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuthorizationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAuthorizationToken',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuthorizationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_authorization_token(
        self,
        request: main_models.GetAuthorizationTokenRequest,
    ) -> main_models.GetAuthorizationTokenResponse:
        runtime = RuntimeOptions()
        return self.get_authorization_token_with_options(request, runtime)

    async def get_authorization_token_async(
        self,
        request: main_models.GetAuthorizationTokenRequest,
    ) -> main_models.GetAuthorizationTokenResponse:
        runtime = RuntimeOptions()
        return await self.get_authorization_token_with_options_async(request, runtime)

    def get_chain_with_options(
        self,
        request: main_models.GetChainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chain_id):
            query['ChainId'] = request.chain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChain',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chain_with_options_async(
        self,
        request: main_models.GetChainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chain_id):
            query['ChainId'] = request.chain_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChain',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chain(
        self,
        request: main_models.GetChainRequest,
    ) -> main_models.GetChainResponse:
        runtime = RuntimeOptions()
        return self.get_chain_with_options(request, runtime)

    async def get_chain_async(
        self,
        request: main_models.GetChainRequest,
    ) -> main_models.GetChainResponse:
        runtime = RuntimeOptions()
        return await self.get_chain_with_options_async(request, runtime)

    def get_chart_namespace_with_options(
        self,
        request: main_models.GetChartNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChartNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChartNamespace',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChartNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chart_namespace_with_options_async(
        self,
        request: main_models.GetChartNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChartNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChartNamespace',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChartNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chart_namespace(
        self,
        request: main_models.GetChartNamespaceRequest,
    ) -> main_models.GetChartNamespaceResponse:
        runtime = RuntimeOptions()
        return self.get_chart_namespace_with_options(request, runtime)

    async def get_chart_namespace_async(
        self,
        request: main_models.GetChartNamespaceRequest,
    ) -> main_models.GetChartNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.get_chart_namespace_with_options_async(request, runtime)

    def get_chart_repository_with_options(
        self,
        request: main_models.GetChartRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChartRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChartRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChartRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_chart_repository_with_options_async(
        self,
        request: main_models.GetChartRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChartRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChartRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChartRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_chart_repository(
        self,
        request: main_models.GetChartRepositoryRequest,
    ) -> main_models.GetChartRepositoryResponse:
        runtime = RuntimeOptions()
        return self.get_chart_repository_with_options(request, runtime)

    async def get_chart_repository_async(
        self,
        request: main_models.GetChartRepositoryRequest,
    ) -> main_models.GetChartRepositoryResponse:
        runtime = RuntimeOptions()
        return await self.get_chart_repository_with_options_async(request, runtime)

    def get_instance_with_options(
        self,
        request: main_models.GetInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_with_options_async(
        self,
        request: main_models.GetInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstance',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance(
        self,
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_instance_with_options(request, runtime)

    async def get_instance_async(
        self,
        request: main_models.GetInstanceRequest,
    ) -> main_models.GetInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_with_options_async(request, runtime)

    def get_instance_count_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceCountResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetInstanceCount',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_count_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceCountResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetInstanceCount',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_count(self) -> main_models.GetInstanceCountResponse:
        runtime = RuntimeOptions()
        return self.get_instance_count_with_options(runtime)

    async def get_instance_count_async(self) -> main_models.GetInstanceCountResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_count_with_options_async(runtime)

    def get_instance_endpoint_with_options(
        self,
        request: main_models.GetInstanceEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceEndpoint',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_endpoint_with_options_async(
        self,
        request: main_models.GetInstanceEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceEndpoint',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_endpoint(
        self,
        request: main_models.GetInstanceEndpointRequest,
    ) -> main_models.GetInstanceEndpointResponse:
        runtime = RuntimeOptions()
        return self.get_instance_endpoint_with_options(request, runtime)

    async def get_instance_endpoint_async(
        self,
        request: main_models.GetInstanceEndpointRequest,
    ) -> main_models.GetInstanceEndpointResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_endpoint_with_options_async(request, runtime)

    def get_instance_usage_with_options(
        self,
        request: main_models.GetInstanceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceUsage',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_usage_with_options_async(
        self,
        request: main_models.GetInstanceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceUsage',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_usage(
        self,
        request: main_models.GetInstanceUsageRequest,
    ) -> main_models.GetInstanceUsageResponse:
        runtime = RuntimeOptions()
        return self.get_instance_usage_with_options(request, runtime)

    async def get_instance_usage_async(
        self,
        request: main_models.GetInstanceUsageRequest,
    ) -> main_models.GetInstanceUsageResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_usage_with_options_async(request, runtime)

    def get_instance_vpc_endpoint_with_options(
        self,
        request: main_models.GetInstanceVpcEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceVpcEndpoint',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceVpcEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_instance_vpc_endpoint_with_options_async(
        self,
        request: main_models.GetInstanceVpcEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInstanceVpcEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInstanceVpcEndpoint',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInstanceVpcEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_instance_vpc_endpoint(
        self,
        request: main_models.GetInstanceVpcEndpointRequest,
    ) -> main_models.GetInstanceVpcEndpointResponse:
        runtime = RuntimeOptions()
        return self.get_instance_vpc_endpoint_with_options(request, runtime)

    async def get_instance_vpc_endpoint_async(
        self,
        request: main_models.GetInstanceVpcEndpointRequest,
    ) -> main_models.GetInstanceVpcEndpointResponse:
        runtime = RuntimeOptions()
        return await self.get_instance_vpc_endpoint_with_options_async(request, runtime)

    def get_namespace_with_options(
        self,
        request: main_models.GetNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNamespace',
            version = '2018-12-01',
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
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_id):
            query['NamespaceId'] = request.namespace_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNamespace',
            version = '2018-12-01',
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

    def get_repo_build_record_with_options(
        self,
        request: main_models.GetRepoBuildRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRepoBuildRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRepoBuildRecord',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRepoBuildRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_build_record_with_options_async(
        self,
        request: main_models.GetRepoBuildRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRepoBuildRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRepoBuildRecord',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRepoBuildRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repo_build_record(
        self,
        request: main_models.GetRepoBuildRecordRequest,
    ) -> main_models.GetRepoBuildRecordResponse:
        runtime = RuntimeOptions()
        return self.get_repo_build_record_with_options(request, runtime)

    async def get_repo_build_record_async(
        self,
        request: main_models.GetRepoBuildRecordRequest,
    ) -> main_models.GetRepoBuildRecordResponse:
        runtime = RuntimeOptions()
        return await self.get_repo_build_record_with_options_async(request, runtime)

    def get_repo_build_record_status_with_options(
        self,
        request: main_models.GetRepoBuildRecordStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRepoBuildRecordStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRepoBuildRecordStatus',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRepoBuildRecordStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_build_record_status_with_options_async(
        self,
        request: main_models.GetRepoBuildRecordStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRepoBuildRecordStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRepoBuildRecordStatus',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRepoBuildRecordStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repo_build_record_status(
        self,
        request: main_models.GetRepoBuildRecordStatusRequest,
    ) -> main_models.GetRepoBuildRecordStatusResponse:
        runtime = RuntimeOptions()
        return self.get_repo_build_record_status_with_options(request, runtime)

    async def get_repo_build_record_status_async(
        self,
        request: main_models.GetRepoBuildRecordStatusRequest,
    ) -> main_models.GetRepoBuildRecordStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_repo_build_record_status_with_options_async(request, runtime)

    def get_repo_source_code_repo_with_options(
        self,
        request: main_models.GetRepoSourceCodeRepoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRepoSourceCodeRepoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRepoSourceCodeRepo',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRepoSourceCodeRepoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_source_code_repo_with_options_async(
        self,
        request: main_models.GetRepoSourceCodeRepoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRepoSourceCodeRepoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRepoSourceCodeRepo',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRepoSourceCodeRepoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repo_source_code_repo(
        self,
        request: main_models.GetRepoSourceCodeRepoRequest,
    ) -> main_models.GetRepoSourceCodeRepoResponse:
        runtime = RuntimeOptions()
        return self.get_repo_source_code_repo_with_options(request, runtime)

    async def get_repo_source_code_repo_async(
        self,
        request: main_models.GetRepoSourceCodeRepoRequest,
    ) -> main_models.GetRepoSourceCodeRepoResponse:
        runtime = RuntimeOptions()
        return await self.get_repo_source_code_repo_with_options_async(request, runtime)

    def get_repo_sync_task_with_options(
        self,
        request: main_models.GetRepoSyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRepoSyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sync_task_id):
            query['SyncTaskId'] = request.sync_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRepoSyncTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRepoSyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_sync_task_with_options_async(
        self,
        request: main_models.GetRepoSyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRepoSyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.sync_task_id):
            query['SyncTaskId'] = request.sync_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRepoSyncTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRepoSyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repo_sync_task(
        self,
        request: main_models.GetRepoSyncTaskRequest,
    ) -> main_models.GetRepoSyncTaskResponse:
        runtime = RuntimeOptions()
        return self.get_repo_sync_task_with_options(request, runtime)

    async def get_repo_sync_task_async(
        self,
        request: main_models.GetRepoSyncTaskRequest,
    ) -> main_models.GetRepoSyncTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_repo_sync_task_with_options_async(request, runtime)

    def get_repo_tag_with_options(
        self,
        request: main_models.GetRepoTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRepoTagResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRepoTag',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRepoTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_tag_with_options_async(
        self,
        request: main_models.GetRepoTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRepoTagResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRepoTag',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRepoTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repo_tag(
        self,
        request: main_models.GetRepoTagRequest,
    ) -> main_models.GetRepoTagResponse:
        runtime = RuntimeOptions()
        return self.get_repo_tag_with_options(request, runtime)

    async def get_repo_tag_async(
        self,
        request: main_models.GetRepoTagRequest,
    ) -> main_models.GetRepoTagResponse:
        runtime = RuntimeOptions()
        return await self.get_repo_tag_with_options_async(request, runtime)

    def get_repo_tag_scan_status_with_options(
        self,
        request: main_models.GetRepoTagScanStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRepoTagScanStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.digest):
            query['Digest'] = request.digest
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.scan_task_id):
            query['ScanTaskId'] = request.scan_task_id
        if not DaraCore.is_null(request.scan_type):
            query['ScanType'] = request.scan_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRepoTagScanStatus',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRepoTagScanStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_tag_scan_status_with_options_async(
        self,
        request: main_models.GetRepoTagScanStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRepoTagScanStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.digest):
            query['Digest'] = request.digest
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.scan_task_id):
            query['ScanTaskId'] = request.scan_task_id
        if not DaraCore.is_null(request.scan_type):
            query['ScanType'] = request.scan_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRepoTagScanStatus',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRepoTagScanStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repo_tag_scan_status(
        self,
        request: main_models.GetRepoTagScanStatusRequest,
    ) -> main_models.GetRepoTagScanStatusResponse:
        runtime = RuntimeOptions()
        return self.get_repo_tag_scan_status_with_options(request, runtime)

    async def get_repo_tag_scan_status_async(
        self,
        request: main_models.GetRepoTagScanStatusRequest,
    ) -> main_models.GetRepoTagScanStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_repo_tag_scan_status_with_options_async(request, runtime)

    def get_repo_tag_scan_summary_with_options(
        self,
        request: main_models.GetRepoTagScanSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRepoTagScanSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.digest):
            query['Digest'] = request.digest
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.scan_task_id):
            query['ScanTaskId'] = request.scan_task_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRepoTagScanSummary',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRepoTagScanSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repo_tag_scan_summary_with_options_async(
        self,
        request: main_models.GetRepoTagScanSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRepoTagScanSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.digest):
            query['Digest'] = request.digest
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.scan_task_id):
            query['ScanTaskId'] = request.scan_task_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRepoTagScanSummary',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRepoTagScanSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repo_tag_scan_summary(
        self,
        request: main_models.GetRepoTagScanSummaryRequest,
    ) -> main_models.GetRepoTagScanSummaryResponse:
        runtime = RuntimeOptions()
        return self.get_repo_tag_scan_summary_with_options(request, runtime)

    async def get_repo_tag_scan_summary_async(
        self,
        request: main_models.GetRepoTagScanSummaryRequest,
    ) -> main_models.GetRepoTagScanSummaryResponse:
        runtime = RuntimeOptions()
        return await self.get_repo_tag_scan_summary_with_options_async(request, runtime)

    def get_repository_with_options(
        self,
        request: main_models.GetRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_repository_with_options_async(
        self,
        request: main_models.GetRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_repository(
        self,
        request: main_models.GetRepositoryRequest,
    ) -> main_models.GetRepositoryResponse:
        runtime = RuntimeOptions()
        return self.get_repository_with_options(request, runtime)

    async def get_repository_async(
        self,
        request: main_models.GetRepositoryRequest,
    ) -> main_models.GetRepositoryResponse:
        runtime = RuntimeOptions()
        return await self.get_repository_with_options_async(request, runtime)

    def get_scan_rule_with_options(
        self,
        request: main_models.GetScanRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScanRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.scan_rule_id):
            query['ScanRuleId'] = request.scan_rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScanRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScanRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_scan_rule_with_options_async(
        self,
        request: main_models.GetScanRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetScanRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.scan_rule_id):
            query['ScanRuleId'] = request.scan_rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetScanRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetScanRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_scan_rule(
        self,
        request: main_models.GetScanRuleRequest,
    ) -> main_models.GetScanRuleResponse:
        runtime = RuntimeOptions()
        return self.get_scan_rule_with_options(request, runtime)

    async def get_scan_rule_async(
        self,
        request: main_models.GetScanRuleRequest,
    ) -> main_models.GetScanRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_scan_rule_with_options_async(request, runtime)

    def get_storage_domain_routing_rule_with_options(
        self,
        request: main_models.GetStorageDomainRoutingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStorageDomainRoutingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStorageDomainRoutingRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStorageDomainRoutingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_storage_domain_routing_rule_with_options_async(
        self,
        request: main_models.GetStorageDomainRoutingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStorageDomainRoutingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStorageDomainRoutingRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStorageDomainRoutingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_storage_domain_routing_rule(
        self,
        request: main_models.GetStorageDomainRoutingRuleRequest,
    ) -> main_models.GetStorageDomainRoutingRuleResponse:
        runtime = RuntimeOptions()
        return self.get_storage_domain_routing_rule_with_options(request, runtime)

    async def get_storage_domain_routing_rule_async(
        self,
        request: main_models.GetStorageDomainRoutingRuleRequest,
    ) -> main_models.GetStorageDomainRoutingRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_storage_domain_routing_rule_with_options_async(request, runtime)

    def list_artifact_build_task_log_with_options(
        self,
        request: main_models.ListArtifactBuildTaskLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactBuildTaskLogResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifactBuildTaskLog',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactBuildTaskLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_artifact_build_task_log_with_options_async(
        self,
        request: main_models.ListArtifactBuildTaskLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactBuildTaskLogResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifactBuildTaskLog',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactBuildTaskLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_artifact_build_task_log(
        self,
        request: main_models.ListArtifactBuildTaskLogRequest,
    ) -> main_models.ListArtifactBuildTaskLogResponse:
        runtime = RuntimeOptions()
        return self.list_artifact_build_task_log_with_options(request, runtime)

    async def list_artifact_build_task_log_async(
        self,
        request: main_models.ListArtifactBuildTaskLogRequest,
    ) -> main_models.ListArtifactBuildTaskLogResponse:
        runtime = RuntimeOptions()
        return await self.list_artifact_build_task_log_with_options_async(request, runtime)

    def list_artifact_lifecycle_rule_with_options(
        self,
        request: main_models.ListArtifactLifecycleRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactLifecycleRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifactLifecycleRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactLifecycleRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_artifact_lifecycle_rule_with_options_async(
        self,
        request: main_models.ListArtifactLifecycleRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactLifecycleRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifactLifecycleRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactLifecycleRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_artifact_lifecycle_rule(
        self,
        request: main_models.ListArtifactLifecycleRuleRequest,
    ) -> main_models.ListArtifactLifecycleRuleResponse:
        runtime = RuntimeOptions()
        return self.list_artifact_lifecycle_rule_with_options(request, runtime)

    async def list_artifact_lifecycle_rule_async(
        self,
        request: main_models.ListArtifactLifecycleRuleRequest,
    ) -> main_models.ListArtifactLifecycleRuleResponse:
        runtime = RuntimeOptions()
        return await self.list_artifact_lifecycle_rule_with_options_async(request, runtime)

    def list_artifact_subscription_rule_with_options(
        self,
        request: main_models.ListArtifactSubscriptionRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactSubscriptionRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifactSubscriptionRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactSubscriptionRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_artifact_subscription_rule_with_options_async(
        self,
        request: main_models.ListArtifactSubscriptionRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactSubscriptionRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifactSubscriptionRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactSubscriptionRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_artifact_subscription_rule(
        self,
        request: main_models.ListArtifactSubscriptionRuleRequest,
    ) -> main_models.ListArtifactSubscriptionRuleResponse:
        runtime = RuntimeOptions()
        return self.list_artifact_subscription_rule_with_options(request, runtime)

    async def list_artifact_subscription_rule_async(
        self,
        request: main_models.ListArtifactSubscriptionRuleRequest,
    ) -> main_models.ListArtifactSubscriptionRuleResponse:
        runtime = RuntimeOptions()
        return await self.list_artifact_subscription_rule_with_options_async(request, runtime)

    def list_artifact_subscription_task_with_options(
        self,
        request: main_models.ListArtifactSubscriptionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactSubscriptionTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifactSubscriptionTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactSubscriptionTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_artifact_subscription_task_with_options_async(
        self,
        request: main_models.ListArtifactSubscriptionTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactSubscriptionTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifactSubscriptionTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactSubscriptionTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_artifact_subscription_task(
        self,
        request: main_models.ListArtifactSubscriptionTaskRequest,
    ) -> main_models.ListArtifactSubscriptionTaskResponse:
        runtime = RuntimeOptions()
        return self.list_artifact_subscription_task_with_options(request, runtime)

    async def list_artifact_subscription_task_async(
        self,
        request: main_models.ListArtifactSubscriptionTaskRequest,
    ) -> main_models.ListArtifactSubscriptionTaskResponse:
        runtime = RuntimeOptions()
        return await self.list_artifact_subscription_task_with_options_async(request, runtime)

    def list_chain_with_options(
        self,
        request: main_models.ListChainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChain',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chain_with_options_async(
        self,
        request: main_models.ListChainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChain',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chain(
        self,
        request: main_models.ListChainRequest,
    ) -> main_models.ListChainResponse:
        runtime = RuntimeOptions()
        return self.list_chain_with_options(request, runtime)

    async def list_chain_async(
        self,
        request: main_models.ListChainRequest,
    ) -> main_models.ListChainResponse:
        runtime = RuntimeOptions()
        return await self.list_chain_with_options_async(request, runtime)

    def list_chain_instance_with_options(
        self,
        request: main_models.ListChainInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChainInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChainInstance',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChainInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chain_instance_with_options_async(
        self,
        request: main_models.ListChainInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChainInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChainInstance',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChainInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chain_instance(
        self,
        request: main_models.ListChainInstanceRequest,
    ) -> main_models.ListChainInstanceResponse:
        runtime = RuntimeOptions()
        return self.list_chain_instance_with_options(request, runtime)

    async def list_chain_instance_async(
        self,
        request: main_models.ListChainInstanceRequest,
    ) -> main_models.ListChainInstanceResponse:
        runtime = RuntimeOptions()
        return await self.list_chain_instance_with_options_async(request, runtime)

    def list_chart_namespace_with_options(
        self,
        request: main_models.ListChartNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChartNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.namespace_status):
            query['NamespaceStatus'] = request.namespace_status
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChartNamespace',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChartNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chart_namespace_with_options_async(
        self,
        request: main_models.ListChartNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChartNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.namespace_status):
            query['NamespaceStatus'] = request.namespace_status
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChartNamespace',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChartNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chart_namespace(
        self,
        request: main_models.ListChartNamespaceRequest,
    ) -> main_models.ListChartNamespaceResponse:
        runtime = RuntimeOptions()
        return self.list_chart_namespace_with_options(request, runtime)

    async def list_chart_namespace_async(
        self,
        request: main_models.ListChartNamespaceRequest,
    ) -> main_models.ListChartNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.list_chart_namespace_with_options_async(request, runtime)

    def list_chart_release_with_options(
        self,
        request: main_models.ListChartReleaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChartReleaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chart):
            query['Chart'] = request.chart
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChartRelease',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChartReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chart_release_with_options_async(
        self,
        request: main_models.ListChartReleaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChartReleaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chart):
            query['Chart'] = request.chart
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChartRelease',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChartReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chart_release(
        self,
        request: main_models.ListChartReleaseRequest,
    ) -> main_models.ListChartReleaseResponse:
        runtime = RuntimeOptions()
        return self.list_chart_release_with_options(request, runtime)

    async def list_chart_release_async(
        self,
        request: main_models.ListChartReleaseRequest,
    ) -> main_models.ListChartReleaseResponse:
        runtime = RuntimeOptions()
        return await self.list_chart_release_with_options_async(request, runtime)

    def list_chart_repository_with_options(
        self,
        request: main_models.ListChartRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChartRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not DaraCore.is_null(request.repo_status):
            query['RepoStatus'] = request.repo_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChartRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChartRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chart_repository_with_options_async(
        self,
        request: main_models.ListChartRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChartRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not DaraCore.is_null(request.repo_status):
            query['RepoStatus'] = request.repo_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChartRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChartRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chart_repository(
        self,
        request: main_models.ListChartRepositoryRequest,
    ) -> main_models.ListChartRepositoryResponse:
        runtime = RuntimeOptions()
        return self.list_chart_repository_with_options(request, runtime)

    async def list_chart_repository_async(
        self,
        request: main_models.ListChartRepositoryRequest,
    ) -> main_models.ListChartRepositoryResponse:
        runtime = RuntimeOptions()
        return await self.list_chart_repository_with_options_async(request, runtime)

    def list_event_center_record_with_options(
        self,
        request: main_models.ListEventCenterRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEventCenterRecordResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEventCenterRecord',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEventCenterRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_center_record_with_options_async(
        self,
        request: main_models.ListEventCenterRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEventCenterRecordResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEventCenterRecord',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEventCenterRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_center_record(
        self,
        request: main_models.ListEventCenterRecordRequest,
    ) -> main_models.ListEventCenterRecordResponse:
        runtime = RuntimeOptions()
        return self.list_event_center_record_with_options(request, runtime)

    async def list_event_center_record_async(
        self,
        request: main_models.ListEventCenterRecordRequest,
    ) -> main_models.ListEventCenterRecordResponse:
        runtime = RuntimeOptions()
        return await self.list_event_center_record_with_options_async(request, runtime)

    def list_event_center_rule_name_with_options(
        self,
        request: main_models.ListEventCenterRuleNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEventCenterRuleNameResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEventCenterRuleName',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEventCenterRuleNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_center_rule_name_with_options_async(
        self,
        request: main_models.ListEventCenterRuleNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEventCenterRuleNameResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEventCenterRuleName',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEventCenterRuleNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_center_rule_name(
        self,
        request: main_models.ListEventCenterRuleNameRequest,
    ) -> main_models.ListEventCenterRuleNameResponse:
        runtime = RuntimeOptions()
        return self.list_event_center_rule_name_with_options(request, runtime)

    async def list_event_center_rule_name_async(
        self,
        request: main_models.ListEventCenterRuleNameRequest,
    ) -> main_models.ListEventCenterRuleNameResponse:
        runtime = RuntimeOptions()
        return await self.list_event_center_rule_name_with_options_async(request, runtime)

    def list_instance_with_options(
        self,
        request: main_models.ListInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstance',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_with_options_async(
        self,
        request: main_models.ListInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstance',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance(
        self,
        request: main_models.ListInstanceRequest,
    ) -> main_models.ListInstanceResponse:
        runtime = RuntimeOptions()
        return self.list_instance_with_options(request, runtime)

    async def list_instance_async(
        self,
        request: main_models.ListInstanceRequest,
    ) -> main_models.ListInstanceResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_with_options_async(request, runtime)

    def list_instance_endpoint_with_options(
        self,
        request: main_models.ListInstanceEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        if not DaraCore.is_null(request.summary):
            query['Summary'] = request.summary
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceEndpoint',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_endpoint_with_options_async(
        self,
        request: main_models.ListInstanceEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        if not DaraCore.is_null(request.summary):
            query['Summary'] = request.summary
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceEndpoint',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_endpoint(
        self,
        request: main_models.ListInstanceEndpointRequest,
    ) -> main_models.ListInstanceEndpointResponse:
        runtime = RuntimeOptions()
        return self.list_instance_endpoint_with_options(request, runtime)

    async def list_instance_endpoint_async(
        self,
        request: main_models.ListInstanceEndpointRequest,
    ) -> main_models.ListInstanceEndpointResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_endpoint_with_options_async(request, runtime)

    def list_instance_region_with_options(
        self,
        request: main_models.ListInstanceRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceRegion',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_region_with_options_async(
        self,
        request: main_models.ListInstanceRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceRegion',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_region(
        self,
        request: main_models.ListInstanceRegionRequest,
    ) -> main_models.ListInstanceRegionResponse:
        runtime = RuntimeOptions()
        return self.list_instance_region_with_options(request, runtime)

    async def list_instance_region_async(
        self,
        request: main_models.ListInstanceRegionRequest,
    ) -> main_models.ListInstanceRegionResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_region_with_options_async(request, runtime)

    def list_namespace_with_options(
        self,
        request: main_models.ListNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.namespace_status):
            query['NamespaceStatus'] = request.namespace_status
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamespace',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_namespace_with_options_async(
        self,
        request: main_models.ListNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.namespace_status):
            query['NamespaceStatus'] = request.namespace_status
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNamespace',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_namespace(
        self,
        request: main_models.ListNamespaceRequest,
    ) -> main_models.ListNamespaceResponse:
        runtime = RuntimeOptions()
        return self.list_namespace_with_options(request, runtime)

    async def list_namespace_async(
        self,
        request: main_models.ListNamespaceRequest,
    ) -> main_models.ListNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.list_namespace_with_options_async(request, runtime)

    def list_repo_build_record_with_options(
        self,
        request: main_models.ListRepoBuildRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepoBuildRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepoBuildRecord',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepoBuildRecordResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repo_build_record_with_options_async(
        self,
        request: main_models.ListRepoBuildRecordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepoBuildRecordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepoBuildRecord',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepoBuildRecordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repo_build_record(
        self,
        request: main_models.ListRepoBuildRecordRequest,
    ) -> main_models.ListRepoBuildRecordResponse:
        runtime = RuntimeOptions()
        return self.list_repo_build_record_with_options(request, runtime)

    async def list_repo_build_record_async(
        self,
        request: main_models.ListRepoBuildRecordRequest,
    ) -> main_models.ListRepoBuildRecordResponse:
        runtime = RuntimeOptions()
        return await self.list_repo_build_record_with_options_async(request, runtime)

    def list_repo_build_record_log_with_options(
        self,
        request: main_models.ListRepoBuildRecordLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepoBuildRecordLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepoBuildRecordLog',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepoBuildRecordLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repo_build_record_log_with_options_async(
        self,
        request: main_models.ListRepoBuildRecordLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepoBuildRecordLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_record_id):
            query['BuildRecordId'] = request.build_record_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.offset):
            query['Offset'] = request.offset
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepoBuildRecordLog',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepoBuildRecordLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repo_build_record_log(
        self,
        request: main_models.ListRepoBuildRecordLogRequest,
    ) -> main_models.ListRepoBuildRecordLogResponse:
        runtime = RuntimeOptions()
        return self.list_repo_build_record_log_with_options(request, runtime)

    async def list_repo_build_record_log_async(
        self,
        request: main_models.ListRepoBuildRecordLogRequest,
    ) -> main_models.ListRepoBuildRecordLogResponse:
        runtime = RuntimeOptions()
        return await self.list_repo_build_record_log_with_options_async(request, runtime)

    def list_repo_build_rule_with_options(
        self,
        request: main_models.ListRepoBuildRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepoBuildRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepoBuildRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repo_build_rule_with_options_async(
        self,
        request: main_models.ListRepoBuildRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepoBuildRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepoBuildRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepoBuildRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repo_build_rule(
        self,
        request: main_models.ListRepoBuildRuleRequest,
    ) -> main_models.ListRepoBuildRuleResponse:
        runtime = RuntimeOptions()
        return self.list_repo_build_rule_with_options(request, runtime)

    async def list_repo_build_rule_async(
        self,
        request: main_models.ListRepoBuildRuleRequest,
    ) -> main_models.ListRepoBuildRuleResponse:
        runtime = RuntimeOptions()
        return await self.list_repo_build_rule_with_options_async(request, runtime)

    def list_repo_sync_rule_with_options(
        self,
        request: main_models.ListRepoSyncRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepoSyncRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        if not DaraCore.is_null(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepoSyncRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepoSyncRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repo_sync_rule_with_options_async(
        self,
        request: main_models.ListRepoSyncRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepoSyncRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        if not DaraCore.is_null(request.target_region_id):
            query['TargetRegionId'] = request.target_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepoSyncRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepoSyncRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repo_sync_rule(
        self,
        request: main_models.ListRepoSyncRuleRequest,
    ) -> main_models.ListRepoSyncRuleResponse:
        runtime = RuntimeOptions()
        return self.list_repo_sync_rule_with_options(request, runtime)

    async def list_repo_sync_rule_async(
        self,
        request: main_models.ListRepoSyncRuleRequest,
    ) -> main_models.ListRepoSyncRuleResponse:
        runtime = RuntimeOptions()
        return await self.list_repo_sync_rule_with_options_async(request, runtime)

    def list_repo_sync_task_with_options(
        self,
        request: main_models.ListRepoSyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepoSyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not DaraCore.is_null(request.sync_record_id):
            query['SyncRecordId'] = request.sync_record_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepoSyncTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepoSyncTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repo_sync_task_with_options_async(
        self,
        request: main_models.ListRepoSyncTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepoSyncTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not DaraCore.is_null(request.sync_record_id):
            query['SyncRecordId'] = request.sync_record_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepoSyncTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepoSyncTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repo_sync_task(
        self,
        request: main_models.ListRepoSyncTaskRequest,
    ) -> main_models.ListRepoSyncTaskResponse:
        runtime = RuntimeOptions()
        return self.list_repo_sync_task_with_options(request, runtime)

    async def list_repo_sync_task_async(
        self,
        request: main_models.ListRepoSyncTaskRequest,
    ) -> main_models.ListRepoSyncTaskResponse:
        runtime = RuntimeOptions()
        return await self.list_repo_sync_task_with_options_async(request, runtime)

    def list_repo_tag_with_options(
        self,
        request: main_models.ListRepoTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepoTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepoTag',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepoTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repo_tag_with_options_async(
        self,
        request: main_models.ListRepoTagRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepoTagResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepoTag',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepoTagResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repo_tag(
        self,
        request: main_models.ListRepoTagRequest,
    ) -> main_models.ListRepoTagResponse:
        runtime = RuntimeOptions()
        return self.list_repo_tag_with_options(request, runtime)

    async def list_repo_tag_async(
        self,
        request: main_models.ListRepoTagRequest,
    ) -> main_models.ListRepoTagResponse:
        runtime = RuntimeOptions()
        return await self.list_repo_tag_with_options_async(request, runtime)

    def list_repo_tag_scan_result_with_options(
        self,
        request: main_models.ListRepoTagScanResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepoTagScanResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.digest):
            query['Digest'] = request.digest
        if not DaraCore.is_null(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.scan_task_id):
            query['ScanTaskId'] = request.scan_task_id
        if not DaraCore.is_null(request.scan_type):
            query['ScanType'] = request.scan_type
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vul_query_key):
            query['VulQueryKey'] = request.vul_query_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepoTagScanResult',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepoTagScanResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repo_tag_scan_result_with_options_async(
        self,
        request: main_models.ListRepoTagScanResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepoTagScanResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.digest):
            query['Digest'] = request.digest
        if not DaraCore.is_null(request.filter_value):
            query['FilterValue'] = request.filter_value
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.scan_task_id):
            query['ScanTaskId'] = request.scan_task_id
        if not DaraCore.is_null(request.scan_type):
            query['ScanType'] = request.scan_type
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.vul_query_key):
            query['VulQueryKey'] = request.vul_query_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepoTagScanResult',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepoTagScanResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repo_tag_scan_result(
        self,
        request: main_models.ListRepoTagScanResultRequest,
    ) -> main_models.ListRepoTagScanResultResponse:
        runtime = RuntimeOptions()
        return self.list_repo_tag_scan_result_with_options(request, runtime)

    async def list_repo_tag_scan_result_async(
        self,
        request: main_models.ListRepoTagScanResultRequest,
    ) -> main_models.ListRepoTagScanResultResponse:
        runtime = RuntimeOptions()
        return await self.list_repo_tag_scan_result_with_options_async(request, runtime)

    def list_repo_trigger_with_options(
        self,
        request: main_models.ListRepoTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepoTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepoTrigger',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepoTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repo_trigger_with_options_async(
        self,
        request: main_models.ListRepoTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepoTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepoTrigger',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepoTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repo_trigger(
        self,
        request: main_models.ListRepoTriggerRequest,
    ) -> main_models.ListRepoTriggerResponse:
        runtime = RuntimeOptions()
        return self.list_repo_trigger_with_options(request, runtime)

    async def list_repo_trigger_async(
        self,
        request: main_models.ListRepoTriggerRequest,
    ) -> main_models.ListRepoTriggerResponse:
        runtime = RuntimeOptions()
        return await self.list_repo_trigger_with_options_async(request, runtime)

    def list_repository_with_options(
        self,
        request: main_models.ListRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not DaraCore.is_null(request.repo_status):
            query['RepoStatus'] = request.repo_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_repository_with_options_async(
        self,
        request: main_models.ListRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.page_no):
            query['PageNo'] = request.page_no
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not DaraCore.is_null(request.repo_status):
            query['RepoStatus'] = request.repo_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_repository(
        self,
        request: main_models.ListRepositoryRequest,
    ) -> main_models.ListRepositoryResponse:
        runtime = RuntimeOptions()
        return self.list_repository_with_options(request, runtime)

    async def list_repository_async(
        self,
        request: main_models.ListRepositoryRequest,
    ) -> main_models.ListRepositoryResponse:
        runtime = RuntimeOptions()
        return await self.list_repository_with_options_async(request, runtime)

    def list_scan_baseline_by_task_with_options(
        self,
        request: main_models.ListScanBaselineByTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScanBaselineByTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScanBaselineByTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScanBaselineByTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scan_baseline_by_task_with_options_async(
        self,
        request: main_models.ListScanBaselineByTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScanBaselineByTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScanBaselineByTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScanBaselineByTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scan_baseline_by_task(
        self,
        request: main_models.ListScanBaselineByTaskRequest,
    ) -> main_models.ListScanBaselineByTaskResponse:
        runtime = RuntimeOptions()
        return self.list_scan_baseline_by_task_with_options(request, runtime)

    async def list_scan_baseline_by_task_async(
        self,
        request: main_models.ListScanBaselineByTaskRequest,
    ) -> main_models.ListScanBaselineByTaskResponse:
        runtime = RuntimeOptions()
        return await self.list_scan_baseline_by_task_with_options_async(request, runtime)

    def list_scan_malicious_file_by_task_with_options(
        self,
        request: main_models.ListScanMaliciousFileByTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScanMaliciousFileByTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScanMaliciousFileByTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScanMaliciousFileByTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scan_malicious_file_by_task_with_options_async(
        self,
        request: main_models.ListScanMaliciousFileByTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScanMaliciousFileByTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScanMaliciousFileByTask',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScanMaliciousFileByTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scan_malicious_file_by_task(
        self,
        request: main_models.ListScanMaliciousFileByTaskRequest,
    ) -> main_models.ListScanMaliciousFileByTaskResponse:
        runtime = RuntimeOptions()
        return self.list_scan_malicious_file_by_task_with_options(request, runtime)

    async def list_scan_malicious_file_by_task_async(
        self,
        request: main_models.ListScanMaliciousFileByTaskRequest,
    ) -> main_models.ListScanMaliciousFileByTaskResponse:
        runtime = RuntimeOptions()
        return await self.list_scan_malicious_file_by_task_with_options_async(request, runtime)

    def list_scan_rule_with_options(
        self,
        request: main_models.ListScanRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScanRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScanRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScanRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scan_rule_with_options_async(
        self,
        request: main_models.ListScanRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScanRuleResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScanRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScanRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scan_rule(
        self,
        request: main_models.ListScanRuleRequest,
    ) -> main_models.ListScanRuleResponse:
        runtime = RuntimeOptions()
        return self.list_scan_rule_with_options(request, runtime)

    async def list_scan_rule_async(
        self,
        request: main_models.ListScanRuleRequest,
    ) -> main_models.ListScanRuleResponse:
        runtime = RuntimeOptions()
        return await self.list_scan_rule_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def reset_login_password_with_options(
        self,
        request: main_models.ResetLoginPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetLoginPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetLoginPassword',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetLoginPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_login_password_with_options_async(
        self,
        request: main_models.ResetLoginPasswordRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ResetLoginPasswordResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ResetLoginPassword',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ResetLoginPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_login_password(
        self,
        request: main_models.ResetLoginPasswordRequest,
    ) -> main_models.ResetLoginPasswordResponse:
        runtime = RuntimeOptions()
        return self.reset_login_password_with_options(request, runtime)

    async def reset_login_password_async(
        self,
        request: main_models.ResetLoginPasswordRequest,
    ) -> main_models.ResetLoginPasswordResponse:
        runtime = RuntimeOptions()
        return await self.reset_login_password_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_artifact_lifecycle_rule_with_options(
        self,
        request: main_models.UpdateArtifactLifecycleRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateArtifactLifecycleRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto):
            query['Auto'] = request.auto
        if not DaraCore.is_null(request.enable_delete_tag):
            query['EnableDeleteTag'] = request.enable_delete_tag
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.retention_tag_count):
            query['RetentionTagCount'] = request.retention_tag_count
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.tag_regexp):
            query['TagRegexp'] = request.tag_regexp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateArtifactLifecycleRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateArtifactLifecycleRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_artifact_lifecycle_rule_with_options_async(
        self,
        request: main_models.UpdateArtifactLifecycleRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateArtifactLifecycleRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto):
            query['Auto'] = request.auto
        if not DaraCore.is_null(request.enable_delete_tag):
            query['EnableDeleteTag'] = request.enable_delete_tag
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.retention_tag_count):
            query['RetentionTagCount'] = request.retention_tag_count
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.tag_regexp):
            query['TagRegexp'] = request.tag_regexp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateArtifactLifecycleRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateArtifactLifecycleRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_artifact_lifecycle_rule(
        self,
        request: main_models.UpdateArtifactLifecycleRuleRequest,
    ) -> main_models.UpdateArtifactLifecycleRuleResponse:
        runtime = RuntimeOptions()
        return self.update_artifact_lifecycle_rule_with_options(request, runtime)

    async def update_artifact_lifecycle_rule_async(
        self,
        request: main_models.UpdateArtifactLifecycleRuleRequest,
    ) -> main_models.UpdateArtifactLifecycleRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_artifact_lifecycle_rule_with_options_async(request, runtime)

    def update_artifact_subscription_rule_with_options(
        self,
        request: main_models.UpdateArtifactSubscriptionRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateArtifactSubscriptionRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate):
            query['Accelerate'] = request.accelerate
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.override):
            query['Override'] = request.override
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.source_namespace_name):
            query['SourceNamespaceName'] = request.source_namespace_name
        if not DaraCore.is_null(request.source_provider):
            query['SourceProvider'] = request.source_provider
        if not DaraCore.is_null(request.source_repo_name):
            query['SourceRepoName'] = request.source_repo_name
        if not DaraCore.is_null(request.tag_count):
            query['TagCount'] = request.tag_count
        if not DaraCore.is_null(request.tag_regexp):
            query['TagRegexp'] = request.tag_regexp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateArtifactSubscriptionRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateArtifactSubscriptionRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_artifact_subscription_rule_with_options_async(
        self,
        request: main_models.UpdateArtifactSubscriptionRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateArtifactSubscriptionRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accelerate):
            query['Accelerate'] = request.accelerate
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.override):
            query['Override'] = request.override
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.source_namespace_name):
            query['SourceNamespaceName'] = request.source_namespace_name
        if not DaraCore.is_null(request.source_provider):
            query['SourceProvider'] = request.source_provider
        if not DaraCore.is_null(request.source_repo_name):
            query['SourceRepoName'] = request.source_repo_name
        if not DaraCore.is_null(request.tag_count):
            query['TagCount'] = request.tag_count
        if not DaraCore.is_null(request.tag_regexp):
            query['TagRegexp'] = request.tag_regexp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateArtifactSubscriptionRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateArtifactSubscriptionRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_artifact_subscription_rule(
        self,
        request: main_models.UpdateArtifactSubscriptionRuleRequest,
    ) -> main_models.UpdateArtifactSubscriptionRuleResponse:
        runtime = RuntimeOptions()
        return self.update_artifact_subscription_rule_with_options(request, runtime)

    async def update_artifact_subscription_rule_async(
        self,
        request: main_models.UpdateArtifactSubscriptionRuleRequest,
    ) -> main_models.UpdateArtifactSubscriptionRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_artifact_subscription_rule_with_options_async(request, runtime)

    def update_chain_with_options(
        self,
        request: main_models.UpdateChainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chain_config):
            query['ChainConfig'] = request.chain_config
        if not DaraCore.is_null(request.chain_id):
            query['ChainId'] = request.chain_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.scope_exclude):
            query['ScopeExclude'] = request.scope_exclude
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChain',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChainResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_chain_with_options_async(
        self,
        request: main_models.UpdateChainRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChainResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chain_config):
            query['ChainConfig'] = request.chain_config
        if not DaraCore.is_null(request.chain_id):
            query['ChainId'] = request.chain_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.scope_exclude):
            query['ScopeExclude'] = request.scope_exclude
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChain',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChainResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_chain(
        self,
        request: main_models.UpdateChainRequest,
    ) -> main_models.UpdateChainResponse:
        runtime = RuntimeOptions()
        return self.update_chain_with_options(request, runtime)

    async def update_chain_async(
        self,
        request: main_models.UpdateChainRequest,
    ) -> main_models.UpdateChainResponse:
        runtime = RuntimeOptions()
        return await self.update_chain_with_options_async(request, runtime)

    def update_chart_namespace_with_options(
        self,
        request: main_models.UpdateChartNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChartNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not DaraCore.is_null(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChartNamespace',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChartNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_chart_namespace_with_options_async(
        self,
        request: main_models.UpdateChartNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChartNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not DaraCore.is_null(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChartNamespace',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChartNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_chart_namespace(
        self,
        request: main_models.UpdateChartNamespaceRequest,
    ) -> main_models.UpdateChartNamespaceResponse:
        runtime = RuntimeOptions()
        return self.update_chart_namespace_with_options(request, runtime)

    async def update_chart_namespace_async(
        self,
        request: main_models.UpdateChartNamespaceRequest,
    ) -> main_models.UpdateChartNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.update_chart_namespace_with_options_async(request, runtime)

    def update_chart_repository_with_options(
        self,
        request: main_models.UpdateChartRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChartRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not DaraCore.is_null(request.repo_type):
            query['RepoType'] = request.repo_type
        if not DaraCore.is_null(request.summary):
            query['Summary'] = request.summary
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChartRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChartRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_chart_repository_with_options_async(
        self,
        request: main_models.UpdateChartRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateChartRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not DaraCore.is_null(request.repo_type):
            query['RepoType'] = request.repo_type
        if not DaraCore.is_null(request.summary):
            query['Summary'] = request.summary
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateChartRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateChartRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_chart_repository(
        self,
        request: main_models.UpdateChartRepositoryRequest,
    ) -> main_models.UpdateChartRepositoryResponse:
        runtime = RuntimeOptions()
        return self.update_chart_repository_with_options(request, runtime)

    async def update_chart_repository_async(
        self,
        request: main_models.UpdateChartRepositoryRequest,
    ) -> main_models.UpdateChartRepositoryResponse:
        runtime = RuntimeOptions()
        return await self.update_chart_repository_with_options_async(request, runtime)

    def update_event_center_rule_with_options(
        self,
        tmp_req: main_models.UpdateEventCenterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEventCenterRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateEventCenterRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.namespaces):
            request.namespaces_shrink = Utils.array_to_string_with_specified_style(tmp_req.namespaces, 'Namespaces', 'json')
        if not DaraCore.is_null(tmp_req.repo_names):
            request.repo_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.repo_names, 'RepoNames', 'json')
        query = {}
        if not DaraCore.is_null(request.event_channel):
            query['EventChannel'] = request.event_channel
        if not DaraCore.is_null(request.event_config):
            query['EventConfig'] = request.event_config
        if not DaraCore.is_null(request.event_scope):
            query['EventScope'] = request.event_scope
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespaces_shrink):
            query['Namespaces'] = request.namespaces_shrink
        if not DaraCore.is_null(request.repo_names_shrink):
            query['RepoNames'] = request.repo_names_shrink
        if not DaraCore.is_null(request.repo_tag_filter_pattern):
            query['RepoTagFilterPattern'] = request.repo_tag_filter_pattern
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEventCenterRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEventCenterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_event_center_rule_with_options_async(
        self,
        tmp_req: main_models.UpdateEventCenterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEventCenterRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateEventCenterRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.namespaces):
            request.namespaces_shrink = Utils.array_to_string_with_specified_style(tmp_req.namespaces, 'Namespaces', 'json')
        if not DaraCore.is_null(tmp_req.repo_names):
            request.repo_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.repo_names, 'RepoNames', 'json')
        query = {}
        if not DaraCore.is_null(request.event_channel):
            query['EventChannel'] = request.event_channel
        if not DaraCore.is_null(request.event_config):
            query['EventConfig'] = request.event_config
        if not DaraCore.is_null(request.event_scope):
            query['EventScope'] = request.event_scope
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespaces_shrink):
            query['Namespaces'] = request.namespaces_shrink
        if not DaraCore.is_null(request.repo_names_shrink):
            query['RepoNames'] = request.repo_names_shrink
        if not DaraCore.is_null(request.repo_tag_filter_pattern):
            query['RepoTagFilterPattern'] = request.repo_tag_filter_pattern
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEventCenterRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEventCenterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_event_center_rule(
        self,
        request: main_models.UpdateEventCenterRuleRequest,
    ) -> main_models.UpdateEventCenterRuleResponse:
        runtime = RuntimeOptions()
        return self.update_event_center_rule_with_options(request, runtime)

    async def update_event_center_rule_async(
        self,
        request: main_models.UpdateEventCenterRuleRequest,
    ) -> main_models.UpdateEventCenterRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_event_center_rule_with_options_async(request, runtime)

    def update_instance_endpoint_status_with_options(
        self,
        request: main_models.UpdateInstanceEndpointStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceEndpointStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceEndpointStatus',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceEndpointStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_endpoint_status_with_options_async(
        self,
        request: main_models.UpdateInstanceEndpointStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstanceEndpointStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.endpoint_type):
            query['EndpointType'] = request.endpoint_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.module_name):
            query['ModuleName'] = request.module_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstanceEndpointStatus',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstanceEndpointStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_endpoint_status(
        self,
        request: main_models.UpdateInstanceEndpointStatusRequest,
    ) -> main_models.UpdateInstanceEndpointStatusResponse:
        runtime = RuntimeOptions()
        return self.update_instance_endpoint_status_with_options(request, runtime)

    async def update_instance_endpoint_status_async(
        self,
        request: main_models.UpdateInstanceEndpointStatusRequest,
    ) -> main_models.UpdateInstanceEndpointStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_endpoint_status_with_options_async(request, runtime)

    def update_namespace_with_options(
        self,
        tmp_req: main_models.UpdateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNamespaceResponse:
        tmp_req.validate()
        request = main_models.UpdateNamespaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.default_repo_configuration):
            request.default_repo_configuration_shrink = Utils.array_to_string_with_specified_style(tmp_req.default_repo_configuration, 'DefaultRepoConfiguration', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not DaraCore.is_null(request.default_repo_configuration_shrink):
            query['DefaultRepoConfiguration'] = request.default_repo_configuration_shrink
        if not DaraCore.is_null(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNamespace',
            version = '2018-12-01',
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
        tmp_req: main_models.UpdateNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNamespaceResponse:
        tmp_req.validate()
        request = main_models.UpdateNamespaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.default_repo_configuration):
            request.default_repo_configuration_shrink = Utils.array_to_string_with_specified_style(tmp_req.default_repo_configuration, 'DefaultRepoConfiguration', 'json')
        query = {}
        if not DaraCore.is_null(request.auto_create_repo):
            query['AutoCreateRepo'] = request.auto_create_repo
        if not DaraCore.is_null(request.default_repo_configuration_shrink):
            query['DefaultRepoConfiguration'] = request.default_repo_configuration_shrink
        if not DaraCore.is_null(request.default_repo_type):
            query['DefaultRepoType'] = request.default_repo_type
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespace_name):
            query['NamespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNamespace',
            version = '2018-12-01',
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

    def update_repo_build_rule_with_options(
        self,
        request: main_models.UpdateRepoBuildRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRepoBuildRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_args):
            query['BuildArgs'] = request.build_args
        if not DaraCore.is_null(request.build_rule_id):
            query['BuildRuleId'] = request.build_rule_id
        if not DaraCore.is_null(request.dockerfile_location):
            query['DockerfileLocation'] = request.dockerfile_location
        if not DaraCore.is_null(request.dockerfile_name):
            query['DockerfileName'] = request.dockerfile_name
        if not DaraCore.is_null(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.platforms):
            query['Platforms'] = request.platforms
        if not DaraCore.is_null(request.push_name):
            query['PushName'] = request.push_name
        if not DaraCore.is_null(request.push_type):
            query['PushType'] = request.push_type
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRepoBuildRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRepoBuildRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_repo_build_rule_with_options_async(
        self,
        request: main_models.UpdateRepoBuildRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRepoBuildRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.build_args):
            query['BuildArgs'] = request.build_args
        if not DaraCore.is_null(request.build_rule_id):
            query['BuildRuleId'] = request.build_rule_id
        if not DaraCore.is_null(request.dockerfile_location):
            query['DockerfileLocation'] = request.dockerfile_location
        if not DaraCore.is_null(request.dockerfile_name):
            query['DockerfileName'] = request.dockerfile_name
        if not DaraCore.is_null(request.image_tag):
            query['ImageTag'] = request.image_tag
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.platforms):
            query['Platforms'] = request.platforms
        if not DaraCore.is_null(request.push_name):
            query['PushName'] = request.push_name
        if not DaraCore.is_null(request.push_type):
            query['PushType'] = request.push_type
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRepoBuildRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRepoBuildRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_repo_build_rule(
        self,
        request: main_models.UpdateRepoBuildRuleRequest,
    ) -> main_models.UpdateRepoBuildRuleResponse:
        runtime = RuntimeOptions()
        return self.update_repo_build_rule_with_options(request, runtime)

    async def update_repo_build_rule_async(
        self,
        request: main_models.UpdateRepoBuildRuleRequest,
    ) -> main_models.UpdateRepoBuildRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_repo_build_rule_with_options_async(request, runtime)

    def update_repo_source_code_repo_with_options(
        self,
        request: main_models.UpdateRepoSourceCodeRepoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRepoSourceCodeRepoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_build):
            query['AutoBuild'] = request.auto_build
        if not DaraCore.is_null(request.code_repo_id):
            query['CodeRepoId'] = request.code_repo_id
        if not DaraCore.is_null(request.code_repo_name):
            query['CodeRepoName'] = request.code_repo_name
        if not DaraCore.is_null(request.code_repo_namespace_name):
            query['CodeRepoNamespaceName'] = request.code_repo_namespace_name
        if not DaraCore.is_null(request.code_repo_type):
            query['CodeRepoType'] = request.code_repo_type
        if not DaraCore.is_null(request.disable_cache_build):
            query['DisableCacheBuild'] = request.disable_cache_build
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.oversea_build):
            query['OverseaBuild'] = request.oversea_build
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRepoSourceCodeRepo',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRepoSourceCodeRepoResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_repo_source_code_repo_with_options_async(
        self,
        request: main_models.UpdateRepoSourceCodeRepoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRepoSourceCodeRepoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_build):
            query['AutoBuild'] = request.auto_build
        if not DaraCore.is_null(request.code_repo_id):
            query['CodeRepoId'] = request.code_repo_id
        if not DaraCore.is_null(request.code_repo_name):
            query['CodeRepoName'] = request.code_repo_name
        if not DaraCore.is_null(request.code_repo_namespace_name):
            query['CodeRepoNamespaceName'] = request.code_repo_namespace_name
        if not DaraCore.is_null(request.code_repo_type):
            query['CodeRepoType'] = request.code_repo_type
        if not DaraCore.is_null(request.disable_cache_build):
            query['DisableCacheBuild'] = request.disable_cache_build
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.oversea_build):
            query['OverseaBuild'] = request.oversea_build
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRepoSourceCodeRepo',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRepoSourceCodeRepoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_repo_source_code_repo(
        self,
        request: main_models.UpdateRepoSourceCodeRepoRequest,
    ) -> main_models.UpdateRepoSourceCodeRepoResponse:
        runtime = RuntimeOptions()
        return self.update_repo_source_code_repo_with_options(request, runtime)

    async def update_repo_source_code_repo_async(
        self,
        request: main_models.UpdateRepoSourceCodeRepoRequest,
    ) -> main_models.UpdateRepoSourceCodeRepoResponse:
        runtime = RuntimeOptions()
        return await self.update_repo_source_code_repo_with_options_async(request, runtime)

    def update_repo_trigger_with_options(
        self,
        request: main_models.UpdateRepoTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRepoTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.trigger_id):
            query['TriggerId'] = request.trigger_id
        if not DaraCore.is_null(request.trigger_name):
            query['TriggerName'] = request.trigger_name
        if not DaraCore.is_null(request.trigger_tag):
            query['TriggerTag'] = request.trigger_tag
        if not DaraCore.is_null(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not DaraCore.is_null(request.trigger_url):
            query['TriggerUrl'] = request.trigger_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRepoTrigger',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRepoTriggerResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_repo_trigger_with_options_async(
        self,
        request: main_models.UpdateRepoTriggerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRepoTriggerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.trigger_id):
            query['TriggerId'] = request.trigger_id
        if not DaraCore.is_null(request.trigger_name):
            query['TriggerName'] = request.trigger_name
        if not DaraCore.is_null(request.trigger_tag):
            query['TriggerTag'] = request.trigger_tag
        if not DaraCore.is_null(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        if not DaraCore.is_null(request.trigger_url):
            query['TriggerUrl'] = request.trigger_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRepoTrigger',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRepoTriggerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_repo_trigger(
        self,
        request: main_models.UpdateRepoTriggerRequest,
    ) -> main_models.UpdateRepoTriggerResponse:
        runtime = RuntimeOptions()
        return self.update_repo_trigger_with_options(request, runtime)

    async def update_repo_trigger_async(
        self,
        request: main_models.UpdateRepoTriggerRequest,
    ) -> main_models.UpdateRepoTriggerResponse:
        runtime = RuntimeOptions()
        return await self.update_repo_trigger_with_options_async(request, runtime)

    def update_repository_with_options(
        self,
        request: main_models.UpdateRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.detail):
            query['Detail'] = request.detail
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not DaraCore.is_null(request.repo_type):
            query['RepoType'] = request.repo_type
        if not DaraCore.is_null(request.summary):
            query['Summary'] = request.summary
        if not DaraCore.is_null(request.tag_immutability):
            query['TagImmutability'] = request.tag_immutability
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_repository_with_options_async(
        self,
        request: main_models.UpdateRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.detail):
            query['Detail'] = request.detail
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        if not DaraCore.is_null(request.repo_namespace_name):
            query['RepoNamespaceName'] = request.repo_namespace_name
        if not DaraCore.is_null(request.repo_type):
            query['RepoType'] = request.repo_type
        if not DaraCore.is_null(request.summary):
            query['Summary'] = request.summary
        if not DaraCore.is_null(request.tag_immutability):
            query['TagImmutability'] = request.tag_immutability
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRepository',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_repository(
        self,
        request: main_models.UpdateRepositoryRequest,
    ) -> main_models.UpdateRepositoryResponse:
        runtime = RuntimeOptions()
        return self.update_repository_with_options(request, runtime)

    async def update_repository_async(
        self,
        request: main_models.UpdateRepositoryRequest,
    ) -> main_models.UpdateRepositoryResponse:
        runtime = RuntimeOptions()
        return await self.update_repository_with_options_async(request, runtime)

    def update_scan_rule_with_options(
        self,
        tmp_req: main_models.UpdateScanRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateScanRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateScanRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.namespaces):
            request.namespaces_shrink = Utils.array_to_string_with_specified_style(tmp_req.namespaces, 'Namespaces', 'json')
        if not DaraCore.is_null(tmp_req.repo_names):
            request.repo_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.repo_names, 'RepoNames', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespaces_shrink):
            query['Namespaces'] = request.namespaces_shrink
        if not DaraCore.is_null(request.repo_names_shrink):
            query['RepoNames'] = request.repo_names_shrink
        if not DaraCore.is_null(request.repo_tag_filter_pattern):
            query['RepoTagFilterPattern'] = request.repo_tag_filter_pattern
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.scan_rule_id):
            query['ScanRuleId'] = request.scan_rule_id
        if not DaraCore.is_null(request.scan_scope):
            query['ScanScope'] = request.scan_scope
        if not DaraCore.is_null(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScanRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateScanRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_scan_rule_with_options_async(
        self,
        tmp_req: main_models.UpdateScanRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateScanRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateScanRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.namespaces):
            request.namespaces_shrink = Utils.array_to_string_with_specified_style(tmp_req.namespaces, 'Namespaces', 'json')
        if not DaraCore.is_null(tmp_req.repo_names):
            request.repo_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.repo_names, 'RepoNames', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.namespaces_shrink):
            query['Namespaces'] = request.namespaces_shrink
        if not DaraCore.is_null(request.repo_names_shrink):
            query['RepoNames'] = request.repo_names_shrink
        if not DaraCore.is_null(request.repo_tag_filter_pattern):
            query['RepoTagFilterPattern'] = request.repo_tag_filter_pattern
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.scan_rule_id):
            query['ScanRuleId'] = request.scan_rule_id
        if not DaraCore.is_null(request.scan_scope):
            query['ScanScope'] = request.scan_scope
        if not DaraCore.is_null(request.trigger_type):
            query['TriggerType'] = request.trigger_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScanRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateScanRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_scan_rule(
        self,
        request: main_models.UpdateScanRuleRequest,
    ) -> main_models.UpdateScanRuleResponse:
        runtime = RuntimeOptions()
        return self.update_scan_rule_with_options(request, runtime)

    async def update_scan_rule_async(
        self,
        request: main_models.UpdateScanRuleRequest,
    ) -> main_models.UpdateScanRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_scan_rule_with_options_async(request, runtime)

    def update_storage_domain_routing_rule_with_options(
        self,
        tmp_req: main_models.UpdateStorageDomainRoutingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStorageDomainRoutingRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateStorageDomainRoutingRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.routes):
            request.routes_shrink = Utils.array_to_string_with_specified_style(tmp_req.routes, 'Routes', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.routes_shrink):
            query['Routes'] = request.routes_shrink
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStorageDomainRoutingRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStorageDomainRoutingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_storage_domain_routing_rule_with_options_async(
        self,
        tmp_req: main_models.UpdateStorageDomainRoutingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStorageDomainRoutingRuleResponse:
        tmp_req.validate()
        request = main_models.UpdateStorageDomainRoutingRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.routes):
            request.routes_shrink = Utils.array_to_string_with_specified_style(tmp_req.routes, 'Routes', 'json')
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.routes_shrink):
            query['Routes'] = request.routes_shrink
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStorageDomainRoutingRule',
            version = '2018-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStorageDomainRoutingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_storage_domain_routing_rule(
        self,
        request: main_models.UpdateStorageDomainRoutingRuleRequest,
    ) -> main_models.UpdateStorageDomainRoutingRuleResponse:
        runtime = RuntimeOptions()
        return self.update_storage_domain_routing_rule_with_options(request, runtime)

    async def update_storage_domain_routing_rule_async(
        self,
        request: main_models.UpdateStorageDomainRoutingRuleRequest,
    ) -> main_models.UpdateStorageDomainRoutingRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_storage_domain_routing_rule_with_options_async(request, runtime)
