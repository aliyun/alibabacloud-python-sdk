# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_oos20190601 import models as main_models
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
        self._endpoint = self.get_endpoint('oos', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def analyze_git_repository_with_options(
        self,
        request: main_models.AnalyzeGitRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AnalyzeGitRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.branch):
            query['Branch'] = request.branch
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_full_name):
            query['RepoFullName'] = request.repo_full_name
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeGitRepository',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnalyzeGitRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def analyze_git_repository_with_options_async(
        self,
        request: main_models.AnalyzeGitRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AnalyzeGitRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.branch):
            query['Branch'] = request.branch
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_full_name):
            query['RepoFullName'] = request.repo_full_name
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AnalyzeGitRepository',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AnalyzeGitRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def analyze_git_repository(
        self,
        request: main_models.AnalyzeGitRepositoryRequest,
    ) -> main_models.AnalyzeGitRepositoryResponse:
        runtime = RuntimeOptions()
        return self.analyze_git_repository_with_options(request, runtime)

    async def analyze_git_repository_async(
        self,
        request: main_models.AnalyzeGitRepositoryRequest,
    ) -> main_models.AnalyzeGitRepositoryResponse:
        runtime = RuntimeOptions()
        return await self.analyze_git_repository_with_options_async(request, runtime)

    def cancel_execution_with_options(
        self,
        request: main_models.CancelExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelExecution',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_execution_with_options_async(
        self,
        request: main_models.CancelExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelExecution',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_execution(
        self,
        request: main_models.CancelExecutionRequest,
    ) -> main_models.CancelExecutionResponse:
        runtime = RuntimeOptions()
        return self.cancel_execution_with_options(request, runtime)

    async def cancel_execution_async(
        self,
        request: main_models.CancelExecutionRequest,
    ) -> main_models.CancelExecutionResponse:
        runtime = RuntimeOptions()
        return await self.cancel_execution_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2019-06-01',
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
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2019-06-01',
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

    def check_git_repo_file_exists_with_options(
        self,
        request: main_models.CheckGitRepoFileExistsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckGitRepoFileExistsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.branch):
            query['Branch'] = request.branch
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_full_name):
            query['RepoFullName'] = request.repo_full_name
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckGitRepoFileExists',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckGitRepoFileExistsResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_git_repo_file_exists_with_options_async(
        self,
        request: main_models.CheckGitRepoFileExistsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckGitRepoFileExistsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.branch):
            query['Branch'] = request.branch
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.file_path):
            query['FilePath'] = request.file_path
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_full_name):
            query['RepoFullName'] = request.repo_full_name
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckGitRepoFileExists',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckGitRepoFileExistsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_git_repo_file_exists(
        self,
        request: main_models.CheckGitRepoFileExistsRequest,
    ) -> main_models.CheckGitRepoFileExistsResponse:
        runtime = RuntimeOptions()
        return self.check_git_repo_file_exists_with_options(request, runtime)

    async def check_git_repo_file_exists_async(
        self,
        request: main_models.CheckGitRepoFileExistsRequest,
    ) -> main_models.CheckGitRepoFileExistsResponse:
        runtime = RuntimeOptions()
        return await self.check_git_repo_file_exists_with_options_async(request, runtime)

    def check_git_repository_exists_with_options(
        self,
        request: main_models.CheckGitRepositoryExistsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckGitRepositoryExistsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_full_name):
            query['RepoFullName'] = request.repo_full_name
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckGitRepositoryExists',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckGitRepositoryExistsResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_git_repository_exists_with_options_async(
        self,
        request: main_models.CheckGitRepositoryExistsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckGitRepositoryExistsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_full_name):
            query['RepoFullName'] = request.repo_full_name
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckGitRepositoryExists',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckGitRepositoryExistsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_git_repository_exists(
        self,
        request: main_models.CheckGitRepositoryExistsRequest,
    ) -> main_models.CheckGitRepositoryExistsResponse:
        runtime = RuntimeOptions()
        return self.check_git_repository_exists_with_options(request, runtime)

    async def check_git_repository_exists_async(
        self,
        request: main_models.CheckGitRepositoryExistsRequest,
    ) -> main_models.CheckGitRepositoryExistsResponse:
        runtime = RuntimeOptions()
        return await self.check_git_repository_exists_with_options_async(request, runtime)

    def continue_deploy_application_group_with_options(
        self,
        request: main_models.ContinueDeployApplicationGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContinueDeployApplicationGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.deploy_parameters):
            query['DeployParameters'] = request.deploy_parameters
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ContinueDeployApplicationGroup',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinueDeployApplicationGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def continue_deploy_application_group_with_options_async(
        self,
        request: main_models.ContinueDeployApplicationGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContinueDeployApplicationGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.deploy_parameters):
            query['DeployParameters'] = request.deploy_parameters
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ContinueDeployApplicationGroup',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinueDeployApplicationGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continue_deploy_application_group(
        self,
        request: main_models.ContinueDeployApplicationGroupRequest,
    ) -> main_models.ContinueDeployApplicationGroupResponse:
        runtime = RuntimeOptions()
        return self.continue_deploy_application_group_with_options(request, runtime)

    async def continue_deploy_application_group_async(
        self,
        request: main_models.ContinueDeployApplicationGroupRequest,
    ) -> main_models.ContinueDeployApplicationGroupResponse:
        runtime = RuntimeOptions()
        return await self.continue_deploy_application_group_with_options_async(request, runtime)

    def create_application_with_options(
        self,
        tmp_req: main_models.CreateApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationResponse:
        tmp_req.validate()
        request = main_models.CreateApplicationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.alarm_config):
            request.alarm_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.alarm_config, 'AlarmConfig', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.alarm_config_shrink):
            query['AlarmConfig'] = request.alarm_config_shrink
        if not DaraCore.is_null(request.application_source):
            query['ApplicationSource'] = request.application_source
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplication',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_with_options_async(
        self,
        tmp_req: main_models.CreateApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationResponse:
        tmp_req.validate()
        request = main_models.CreateApplicationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.alarm_config):
            request.alarm_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.alarm_config, 'AlarmConfig', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.alarm_config_shrink):
            query['AlarmConfig'] = request.alarm_config_shrink
        if not DaraCore.is_null(request.application_source):
            query['ApplicationSource'] = request.application_source
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplication',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application(
        self,
        request: main_models.CreateApplicationRequest,
    ) -> main_models.CreateApplicationResponse:
        runtime = RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    async def create_application_async(
        self,
        request: main_models.CreateApplicationRequest,
    ) -> main_models.CreateApplicationResponse:
        runtime = RuntimeOptions()
        return await self.create_application_with_options_async(request, runtime)

    def create_application_group_with_options(
        self,
        request: main_models.CreateApplicationGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cms_group_id):
            query['CmsGroupId'] = request.cms_group_id
        if not DaraCore.is_null(request.deploy_region_id):
            query['DeployRegionId'] = request.deploy_region_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.import_tag_key):
            query['ImportTagKey'] = request.import_tag_key
        if not DaraCore.is_null(request.import_tag_value):
            query['ImportTagValue'] = request.import_tag_value
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationGroup',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_group_with_options_async(
        self,
        request: main_models.CreateApplicationGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApplicationGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cms_group_id):
            query['CmsGroupId'] = request.cms_group_id
        if not DaraCore.is_null(request.deploy_region_id):
            query['DeployRegionId'] = request.deploy_region_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.import_tag_key):
            query['ImportTagKey'] = request.import_tag_key
        if not DaraCore.is_null(request.import_tag_value):
            query['ImportTagValue'] = request.import_tag_value
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApplicationGroup',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApplicationGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application_group(
        self,
        request: main_models.CreateApplicationGroupRequest,
    ) -> main_models.CreateApplicationGroupResponse:
        runtime = RuntimeOptions()
        return self.create_application_group_with_options(request, runtime)

    async def create_application_group_async(
        self,
        request: main_models.CreateApplicationGroupRequest,
    ) -> main_models.CreateApplicationGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_application_group_with_options_async(request, runtime)

    def create_git_repository_with_options(
        self,
        request: main_models.CreateGitRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGitRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.is_private):
            query['IsPrivate'] = request.is_private
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source_repo_branch):
            query['SourceRepoBranch'] = request.source_repo_branch
        if not DaraCore.is_null(request.source_repo_name):
            query['SourceRepoName'] = request.source_repo_name
        if not DaraCore.is_null(request.source_repo_owner):
            query['SourceRepoOwner'] = request.source_repo_owner
        if not DaraCore.is_null(request.target_repo_name):
            query['TargetRepoName'] = request.target_repo_name
        if not DaraCore.is_null(request.target_repo_owner):
            query['TargetRepoOwner'] = request.target_repo_owner
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGitRepository',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGitRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_git_repository_with_options_async(
        self,
        request: main_models.CreateGitRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGitRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.is_private):
            query['IsPrivate'] = request.is_private
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source_repo_branch):
            query['SourceRepoBranch'] = request.source_repo_branch
        if not DaraCore.is_null(request.source_repo_name):
            query['SourceRepoName'] = request.source_repo_name
        if not DaraCore.is_null(request.source_repo_owner):
            query['SourceRepoOwner'] = request.source_repo_owner
        if not DaraCore.is_null(request.target_repo_name):
            query['TargetRepoName'] = request.target_repo_name
        if not DaraCore.is_null(request.target_repo_owner):
            query['TargetRepoOwner'] = request.target_repo_owner
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGitRepository',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGitRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_git_repository(
        self,
        request: main_models.CreateGitRepositoryRequest,
    ) -> main_models.CreateGitRepositoryResponse:
        runtime = RuntimeOptions()
        return self.create_git_repository_with_options(request, runtime)

    async def create_git_repository_async(
        self,
        request: main_models.CreateGitRepositoryRequest,
    ) -> main_models.CreateGitRepositoryResponse:
        runtime = RuntimeOptions()
        return await self.create_git_repository_with_options_async(request, runtime)

    def create_ops_item_with_options(
        self,
        tmp_req: main_models.CreateOpsItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOpsItemResponse:
        tmp_req.validate()
        request = main_models.CreateOpsItemShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dedup_string):
            query['DedupString'] = request.dedup_string
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.solutions):
            query['Solutions'] = request.solutions
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOpsItem',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOpsItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ops_item_with_options_async(
        self,
        tmp_req: main_models.CreateOpsItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOpsItemResponse:
        tmp_req.validate()
        request = main_models.CreateOpsItemShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dedup_string):
            query['DedupString'] = request.dedup_string
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.solutions):
            query['Solutions'] = request.solutions
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOpsItem',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOpsItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ops_item(
        self,
        request: main_models.CreateOpsItemRequest,
    ) -> main_models.CreateOpsItemResponse:
        runtime = RuntimeOptions()
        return self.create_ops_item_with_options(request, runtime)

    async def create_ops_item_async(
        self,
        request: main_models.CreateOpsItemRequest,
    ) -> main_models.CreateOpsItemResponse:
        runtime = RuntimeOptions()
        return await self.create_ops_item_with_options_async(request, runtime)

    def create_parameter_with_options(
        self,
        tmp_req: main_models.CreateParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateParameterResponse:
        tmp_req.validate()
        request = main_models.CreateParameterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.constraints):
            query['Constraints'] = request.constraints
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateParameter',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_parameter_with_options_async(
        self,
        tmp_req: main_models.CreateParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateParameterResponse:
        tmp_req.validate()
        request = main_models.CreateParameterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.constraints):
            query['Constraints'] = request.constraints
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateParameter',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_parameter(
        self,
        request: main_models.CreateParameterRequest,
    ) -> main_models.CreateParameterResponse:
        runtime = RuntimeOptions()
        return self.create_parameter_with_options(request, runtime)

    async def create_parameter_async(
        self,
        request: main_models.CreateParameterRequest,
    ) -> main_models.CreateParameterResponse:
        runtime = RuntimeOptions()
        return await self.create_parameter_with_options_async(request, runtime)

    def create_patch_baseline_with_options(
        self,
        tmp_req: main_models.CreatePatchBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePatchBaselineResponse:
        tmp_req.validate()
        request = main_models.CreatePatchBaselineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.approved_patches):
            request.approved_patches_shrink = Utils.array_to_string_with_specified_style(tmp_req.approved_patches, 'ApprovedPatches', 'json')
        if not DaraCore.is_null(tmp_req.rejected_patches):
            request.rejected_patches_shrink = Utils.array_to_string_with_specified_style(tmp_req.rejected_patches, 'RejectedPatches', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.approval_rules):
            query['ApprovalRules'] = request.approval_rules
        if not DaraCore.is_null(request.approved_patches_shrink):
            query['ApprovedPatches'] = request.approved_patches_shrink
        if not DaraCore.is_null(request.approved_patches_enable_non_security):
            query['ApprovedPatchesEnableNonSecurity'] = request.approved_patches_enable_non_security
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.operation_system):
            query['OperationSystem'] = request.operation_system
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rejected_patches_shrink):
            query['RejectedPatches'] = request.rejected_patches_shrink
        if not DaraCore.is_null(request.rejected_patches_action):
            query['RejectedPatchesAction'] = request.rejected_patches_action
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePatchBaseline',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePatchBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_patch_baseline_with_options_async(
        self,
        tmp_req: main_models.CreatePatchBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePatchBaselineResponse:
        tmp_req.validate()
        request = main_models.CreatePatchBaselineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.approved_patches):
            request.approved_patches_shrink = Utils.array_to_string_with_specified_style(tmp_req.approved_patches, 'ApprovedPatches', 'json')
        if not DaraCore.is_null(tmp_req.rejected_patches):
            request.rejected_patches_shrink = Utils.array_to_string_with_specified_style(tmp_req.rejected_patches, 'RejectedPatches', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.approval_rules):
            query['ApprovalRules'] = request.approval_rules
        if not DaraCore.is_null(request.approved_patches_shrink):
            query['ApprovedPatches'] = request.approved_patches_shrink
        if not DaraCore.is_null(request.approved_patches_enable_non_security):
            query['ApprovedPatchesEnableNonSecurity'] = request.approved_patches_enable_non_security
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.operation_system):
            query['OperationSystem'] = request.operation_system
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rejected_patches_shrink):
            query['RejectedPatches'] = request.rejected_patches_shrink
        if not DaraCore.is_null(request.rejected_patches_action):
            query['RejectedPatchesAction'] = request.rejected_patches_action
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePatchBaseline',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePatchBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_patch_baseline(
        self,
        request: main_models.CreatePatchBaselineRequest,
    ) -> main_models.CreatePatchBaselineResponse:
        runtime = RuntimeOptions()
        return self.create_patch_baseline_with_options(request, runtime)

    async def create_patch_baseline_async(
        self,
        request: main_models.CreatePatchBaselineRequest,
    ) -> main_models.CreatePatchBaselineResponse:
        runtime = RuntimeOptions()
        return await self.create_patch_baseline_with_options_async(request, runtime)

    def create_secret_parameter_with_options(
        self,
        tmp_req: main_models.CreateSecretParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecretParameterResponse:
        tmp_req.validate()
        request = main_models.CreateSecretParameterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.constraints):
            query['Constraints'] = request.constraints
        if not DaraCore.is_null(request.dkmsinstance_id):
            query['DKMSInstanceId'] = request.dkmsinstance_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecretParameter',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecretParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_secret_parameter_with_options_async(
        self,
        tmp_req: main_models.CreateSecretParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSecretParameterResponse:
        tmp_req.validate()
        request = main_models.CreateSecretParameterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.constraints):
            query['Constraints'] = request.constraints
        if not DaraCore.is_null(request.dkmsinstance_id):
            query['DKMSInstanceId'] = request.dkmsinstance_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.key_id):
            query['KeyId'] = request.key_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSecretParameter',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSecretParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_secret_parameter(
        self,
        request: main_models.CreateSecretParameterRequest,
    ) -> main_models.CreateSecretParameterResponse:
        runtime = RuntimeOptions()
        return self.create_secret_parameter_with_options(request, runtime)

    async def create_secret_parameter_async(
        self,
        request: main_models.CreateSecretParameterRequest,
    ) -> main_models.CreateSecretParameterResponse:
        runtime = RuntimeOptions()
        return await self.create_secret_parameter_with_options_async(request, runtime)

    def create_state_configuration_with_options(
        self,
        tmp_req: main_models.CreateStateConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStateConfigurationResponse:
        tmp_req.validate()
        request = main_models.CreateStateConfigurationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.configure_mode):
            query['ConfigureMode'] = request.configure_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.schedule_expression):
            query['ScheduleExpression'] = request.schedule_expression
        if not DaraCore.is_null(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.targets):
            query['Targets'] = request.targets
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStateConfiguration',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStateConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_state_configuration_with_options_async(
        self,
        tmp_req: main_models.CreateStateConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStateConfigurationResponse:
        tmp_req.validate()
        request = main_models.CreateStateConfigurationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.configure_mode):
            query['ConfigureMode'] = request.configure_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.schedule_expression):
            query['ScheduleExpression'] = request.schedule_expression
        if not DaraCore.is_null(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.targets):
            query['Targets'] = request.targets
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStateConfiguration',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStateConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_state_configuration(
        self,
        request: main_models.CreateStateConfigurationRequest,
    ) -> main_models.CreateStateConfigurationResponse:
        runtime = RuntimeOptions()
        return self.create_state_configuration_with_options(request, runtime)

    async def create_state_configuration_async(
        self,
        request: main_models.CreateStateConfigurationRequest,
    ) -> main_models.CreateStateConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.create_state_configuration_with_options_async(request, runtime)

    def create_template_with_options(
        self,
        tmp_req: main_models.CreateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        tmp_req: main_models.CreateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        tmp_req.validate()
        request = main_models.CreateTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    async def create_template_async(
        self,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_template_with_options_async(request, runtime)

    def delete_application_with_options(
        self,
        request: main_models.DeleteApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.retain_resource):
            query['RetainResource'] = request.retain_resource
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplication',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_with_options_async(
        self,
        request: main_models.DeleteApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.retain_resource):
            query['RetainResource'] = request.retain_resource
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplication',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application(
        self,
        request: main_models.DeleteApplicationRequest,
    ) -> main_models.DeleteApplicationResponse:
        runtime = RuntimeOptions()
        return self.delete_application_with_options(request, runtime)

    async def delete_application_async(
        self,
        request: main_models.DeleteApplicationRequest,
    ) -> main_models.DeleteApplicationResponse:
        runtime = RuntimeOptions()
        return await self.delete_application_with_options_async(request, runtime)

    def delete_application_group_with_options(
        self,
        request: main_models.DeleteApplicationGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.retain_resource):
            query['RetainResource'] = request.retain_resource
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationGroup',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_application_group_with_options_async(
        self,
        request: main_models.DeleteApplicationGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApplicationGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.retain_resource):
            query['RetainResource'] = request.retain_resource
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApplicationGroup',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApplicationGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_application_group(
        self,
        request: main_models.DeleteApplicationGroupRequest,
    ) -> main_models.DeleteApplicationGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_application_group_with_options(request, runtime)

    async def delete_application_group_async(
        self,
        request: main_models.DeleteApplicationGroupRequest,
    ) -> main_models.DeleteApplicationGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_application_group_with_options_async(request, runtime)

    def delete_executions_with_options(
        self,
        request: main_models.DeleteExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExecutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.execution_ids):
            query['ExecutionIds'] = request.execution_ids
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExecutions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_executions_with_options_async(
        self,
        request: main_models.DeleteExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExecutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.execution_ids):
            query['ExecutionIds'] = request.execution_ids
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExecutions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_executions(
        self,
        request: main_models.DeleteExecutionsRequest,
    ) -> main_models.DeleteExecutionsResponse:
        runtime = RuntimeOptions()
        return self.delete_executions_with_options(request, runtime)

    async def delete_executions_async(
        self,
        request: main_models.DeleteExecutionsRequest,
    ) -> main_models.DeleteExecutionsResponse:
        runtime = RuntimeOptions()
        return await self.delete_executions_with_options_async(request, runtime)

    def delete_ops_items_with_options(
        self,
        request: main_models.DeleteOpsItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOpsItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ops_item_ids):
            query['OpsItemIds'] = request.ops_item_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOpsItems',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOpsItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_ops_items_with_options_async(
        self,
        request: main_models.DeleteOpsItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteOpsItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ops_item_ids):
            query['OpsItemIds'] = request.ops_item_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteOpsItems',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteOpsItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_ops_items(
        self,
        request: main_models.DeleteOpsItemsRequest,
    ) -> main_models.DeleteOpsItemsResponse:
        runtime = RuntimeOptions()
        return self.delete_ops_items_with_options(request, runtime)

    async def delete_ops_items_async(
        self,
        request: main_models.DeleteOpsItemsRequest,
    ) -> main_models.DeleteOpsItemsResponse:
        runtime = RuntimeOptions()
        return await self.delete_ops_items_with_options_async(request, runtime)

    def delete_parameter_with_options(
        self,
        request: main_models.DeleteParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteParameterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteParameter',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_parameter_with_options_async(
        self,
        request: main_models.DeleteParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteParameterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteParameter',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_parameter(
        self,
        request: main_models.DeleteParameterRequest,
    ) -> main_models.DeleteParameterResponse:
        runtime = RuntimeOptions()
        return self.delete_parameter_with_options(request, runtime)

    async def delete_parameter_async(
        self,
        request: main_models.DeleteParameterRequest,
    ) -> main_models.DeleteParameterResponse:
        runtime = RuntimeOptions()
        return await self.delete_parameter_with_options_async(request, runtime)

    def delete_patch_baseline_with_options(
        self,
        request: main_models.DeletePatchBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePatchBaselineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePatchBaseline',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePatchBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_patch_baseline_with_options_async(
        self,
        request: main_models.DeletePatchBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePatchBaselineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePatchBaseline',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePatchBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_patch_baseline(
        self,
        request: main_models.DeletePatchBaselineRequest,
    ) -> main_models.DeletePatchBaselineResponse:
        runtime = RuntimeOptions()
        return self.delete_patch_baseline_with_options(request, runtime)

    async def delete_patch_baseline_async(
        self,
        request: main_models.DeletePatchBaselineRequest,
    ) -> main_models.DeletePatchBaselineResponse:
        runtime = RuntimeOptions()
        return await self.delete_patch_baseline_with_options_async(request, runtime)

    def delete_secret_parameter_with_options(
        self,
        request: main_models.DeleteSecretParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecretParameterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecretParameter',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecretParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_secret_parameter_with_options_async(
        self,
        request: main_models.DeleteSecretParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSecretParameterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSecretParameter',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSecretParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_secret_parameter(
        self,
        request: main_models.DeleteSecretParameterRequest,
    ) -> main_models.DeleteSecretParameterResponse:
        runtime = RuntimeOptions()
        return self.delete_secret_parameter_with_options(request, runtime)

    async def delete_secret_parameter_async(
        self,
        request: main_models.DeleteSecretParameterRequest,
    ) -> main_models.DeleteSecretParameterResponse:
        runtime = RuntimeOptions()
        return await self.delete_secret_parameter_with_options_async(request, runtime)

    def delete_state_configurations_with_options(
        self,
        request: main_models.DeleteStateConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStateConfigurationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.state_configuration_ids):
            query['StateConfigurationIds'] = request.state_configuration_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStateConfigurations',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStateConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_state_configurations_with_options_async(
        self,
        request: main_models.DeleteStateConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStateConfigurationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.state_configuration_ids):
            query['StateConfigurationIds'] = request.state_configuration_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStateConfigurations',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStateConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_state_configurations(
        self,
        request: main_models.DeleteStateConfigurationsRequest,
    ) -> main_models.DeleteStateConfigurationsResponse:
        runtime = RuntimeOptions()
        return self.delete_state_configurations_with_options(request, runtime)

    async def delete_state_configurations_async(
        self,
        request: main_models.DeleteStateConfigurationsRequest,
    ) -> main_models.DeleteStateConfigurationsResponse:
        runtime = RuntimeOptions()
        return await self.delete_state_configurations_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: main_models.DeleteTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_delete_executions):
            query['AutoDeleteExecutions'] = request.auto_delete_executions
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: main_models.DeleteTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_delete_executions):
            query['AutoDeleteExecutions'] = request.auto_delete_executions
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        request: main_models.DeleteTemplateRequest,
    ) -> main_models.DeleteTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: main_models.DeleteTemplateRequest,
    ) -> main_models.DeleteTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def delete_templates_with_options(
        self,
        request: main_models.DeleteTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_delete_executions):
            query['AutoDeleteExecutions'] = request.auto_delete_executions
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_names):
            query['TemplateNames'] = request.template_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplates',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_templates_with_options_async(
        self,
        request: main_models.DeleteTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_delete_executions):
            query['AutoDeleteExecutions'] = request.auto_delete_executions
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_names):
            query['TemplateNames'] = request.template_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplates',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_templates(
        self,
        request: main_models.DeleteTemplatesRequest,
    ) -> main_models.DeleteTemplatesResponse:
        runtime = RuntimeOptions()
        return self.delete_templates_with_options(request, runtime)

    async def delete_templates_async(
        self,
        request: main_models.DeleteTemplatesRequest,
    ) -> main_models.DeleteTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.delete_templates_with_options_async(request, runtime)

    def deploy_application_group_with_options(
        self,
        request: main_models.DeployApplicationGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeployApplicationGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.deploy_parameters):
            query['DeployParameters'] = request.deploy_parameters
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.revision_id):
            query['RevisionId'] = request.revision_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeployApplicationGroup',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployApplicationGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_application_group_with_options_async(
        self,
        request: main_models.DeployApplicationGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeployApplicationGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.deploy_parameters):
            query['DeployParameters'] = request.deploy_parameters
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.revision_id):
            query['RevisionId'] = request.revision_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeployApplicationGroup',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployApplicationGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_application_group(
        self,
        request: main_models.DeployApplicationGroupRequest,
    ) -> main_models.DeployApplicationGroupResponse:
        runtime = RuntimeOptions()
        return self.deploy_application_group_with_options(request, runtime)

    async def deploy_application_group_async(
        self,
        request: main_models.DeployApplicationGroupRequest,
    ) -> main_models.DeployApplicationGroupResponse:
        runtime = RuntimeOptions()
        return await self.deploy_application_group_with_options_async(request, runtime)

    def describe_application_group_bill_with_options(
        self,
        request: main_models.DescribeApplicationGroupBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationGroupBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationGroupBill',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationGroupBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_application_group_bill_with_options_async(
        self,
        request: main_models.DescribeApplicationGroupBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeApplicationGroupBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeApplicationGroupBill',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeApplicationGroupBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_application_group_bill(
        self,
        request: main_models.DescribeApplicationGroupBillRequest,
    ) -> main_models.DescribeApplicationGroupBillResponse:
        runtime = RuntimeOptions()
        return self.describe_application_group_bill_with_options(request, runtime)

    async def describe_application_group_bill_async(
        self,
        request: main_models.DescribeApplicationGroupBillRequest,
    ) -> main_models.DescribeApplicationGroupBillResponse:
        runtime = RuntimeOptions()
        return await self.describe_application_group_bill_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def generate_execution_policy_with_options(
        self,
        request: main_models.GenerateExecutionPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateExecutionPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ram_role):
            query['RamRole'] = request.ram_role
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_content):
            query['TemplateContent'] = request.template_content
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateExecutionPolicy',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateExecutionPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_execution_policy_with_options_async(
        self,
        request: main_models.GenerateExecutionPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateExecutionPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ram_role):
            query['RamRole'] = request.ram_role
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_content):
            query['TemplateContent'] = request.template_content
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateExecutionPolicy',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateExecutionPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_execution_policy(
        self,
        request: main_models.GenerateExecutionPolicyRequest,
    ) -> main_models.GenerateExecutionPolicyResponse:
        runtime = RuntimeOptions()
        return self.generate_execution_policy_with_options(request, runtime)

    async def generate_execution_policy_async(
        self,
        request: main_models.GenerateExecutionPolicyRequest,
    ) -> main_models.GenerateExecutionPolicyResponse:
        runtime = RuntimeOptions()
        return await self.generate_execution_policy_with_options_async(request, runtime)

    def generate_ops_item_with_options(
        self,
        request: main_models.GenerateOpsItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateOpsItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.configuration_id):
            query['ConfigurationId'] = request.configuration_id
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.data_source):
            query['DataSource'] = request.data_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateOpsItem',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateOpsItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_ops_item_with_options_async(
        self,
        request: main_models.GenerateOpsItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateOpsItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.configuration_id):
            query['ConfigurationId'] = request.configuration_id
        if not DaraCore.is_null(request.data):
            query['Data'] = request.data
        if not DaraCore.is_null(request.data_source):
            query['DataSource'] = request.data_source
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateOpsItem',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateOpsItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_ops_item(
        self,
        request: main_models.GenerateOpsItemRequest,
    ) -> main_models.GenerateOpsItemResponse:
        runtime = RuntimeOptions()
        return self.generate_ops_item_with_options(request, runtime)

    async def generate_ops_item_async(
        self,
        request: main_models.GenerateOpsItemRequest,
    ) -> main_models.GenerateOpsItemResponse:
        runtime = RuntimeOptions()
        return await self.generate_ops_item_with_options_async(request, runtime)

    def get_application_with_options(
        self,
        request: main_models.GetApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplication',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_with_options_async(
        self,
        request: main_models.GetApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplication',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application(
        self,
        request: main_models.GetApplicationRequest,
    ) -> main_models.GetApplicationResponse:
        runtime = RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    async def get_application_async(
        self,
        request: main_models.GetApplicationRequest,
    ) -> main_models.GetApplicationResponse:
        runtime = RuntimeOptions()
        return await self.get_application_with_options_async(request, runtime)

    def get_application_group_with_options(
        self,
        request: main_models.GetApplicationGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationGroup',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_group_with_options_async(
        self,
        request: main_models.GetApplicationGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplicationGroup',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApplicationGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_group(
        self,
        request: main_models.GetApplicationGroupRequest,
    ) -> main_models.GetApplicationGroupResponse:
        runtime = RuntimeOptions()
        return self.get_application_group_with_options(request, runtime)

    async def get_application_group_async(
        self,
        request: main_models.GetApplicationGroupRequest,
    ) -> main_models.GetApplicationGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_application_group_with_options_async(request, runtime)

    def get_execution_template_with_options(
        self,
        request: main_models.GetExecutionTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExecutionTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExecutionTemplate',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExecutionTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_execution_template_with_options_async(
        self,
        request: main_models.GetExecutionTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExecutionTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExecutionTemplate',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExecutionTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_execution_template(
        self,
        request: main_models.GetExecutionTemplateRequest,
    ) -> main_models.GetExecutionTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_execution_template_with_options(request, runtime)

    async def get_execution_template_async(
        self,
        request: main_models.GetExecutionTemplateRequest,
    ) -> main_models.GetExecutionTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_execution_template_with_options_async(request, runtime)

    def get_git_branch_with_options(
        self,
        request: main_models.GetGitBranchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGitBranchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.branch):
            query['Branch'] = request.branch
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_full_name):
            query['RepoFullName'] = request.repo_full_name
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGitBranch',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGitBranchResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_git_branch_with_options_async(
        self,
        request: main_models.GetGitBranchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGitBranchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.branch):
            query['Branch'] = request.branch
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_full_name):
            query['RepoFullName'] = request.repo_full_name
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGitBranch',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGitBranchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_git_branch(
        self,
        request: main_models.GetGitBranchRequest,
    ) -> main_models.GetGitBranchResponse:
        runtime = RuntimeOptions()
        return self.get_git_branch_with_options(request, runtime)

    async def get_git_branch_async(
        self,
        request: main_models.GetGitBranchRequest,
    ) -> main_models.GetGitBranchResponse:
        runtime = RuntimeOptions()
        return await self.get_git_branch_with_options_async(request, runtime)

    def get_git_repository_with_options(
        self,
        request: main_models.GetGitRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGitRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_full_name):
            query['RepoFullName'] = request.repo_full_name
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGitRepository',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGitRepositoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_git_repository_with_options_async(
        self,
        request: main_models.GetGitRepositoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGitRepositoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_full_name):
            query['RepoFullName'] = request.repo_full_name
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGitRepository',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGitRepositoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_git_repository(
        self,
        request: main_models.GetGitRepositoryRequest,
    ) -> main_models.GetGitRepositoryResponse:
        runtime = RuntimeOptions()
        return self.get_git_repository_with_options(request, runtime)

    async def get_git_repository_async(
        self,
        request: main_models.GetGitRepositoryRequest,
    ) -> main_models.GetGitRepositoryResponse:
        runtime = RuntimeOptions()
        return await self.get_git_repository_with_options_async(request, runtime)

    def get_inventory_schema_with_options(
        self,
        request: main_models.GetInventorySchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInventorySchemaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator):
            query['Aggregator'] = request.aggregator
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type_name):
            query['TypeName'] = request.type_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInventorySchema',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInventorySchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_inventory_schema_with_options_async(
        self,
        request: main_models.GetInventorySchemaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetInventorySchemaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator):
            query['Aggregator'] = request.aggregator
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type_name):
            query['TypeName'] = request.type_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetInventorySchema',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetInventorySchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_inventory_schema(
        self,
        request: main_models.GetInventorySchemaRequest,
    ) -> main_models.GetInventorySchemaResponse:
        runtime = RuntimeOptions()
        return self.get_inventory_schema_with_options(request, runtime)

    async def get_inventory_schema_async(
        self,
        request: main_models.GetInventorySchemaRequest,
    ) -> main_models.GetInventorySchemaResponse:
        runtime = RuntimeOptions()
        return await self.get_inventory_schema_with_options_async(request, runtime)

    def get_ops_item_with_options(
        self,
        request: main_models.GetOpsItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOpsItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ops_item_id):
            query['OpsItemId'] = request.ops_item_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOpsItem',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOpsItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ops_item_with_options_async(
        self,
        request: main_models.GetOpsItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOpsItemResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ops_item_id):
            query['OpsItemId'] = request.ops_item_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOpsItem',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOpsItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ops_item(
        self,
        request: main_models.GetOpsItemRequest,
    ) -> main_models.GetOpsItemResponse:
        runtime = RuntimeOptions()
        return self.get_ops_item_with_options(request, runtime)

    async def get_ops_item_async(
        self,
        request: main_models.GetOpsItemRequest,
    ) -> main_models.GetOpsItemResponse:
        runtime = RuntimeOptions()
        return await self.get_ops_item_with_options_async(request, runtime)

    def get_parameter_with_options(
        self,
        request: main_models.GetParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetParameterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parameter_version):
            query['ParameterVersion'] = request.parameter_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetParameter',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_parameter_with_options_async(
        self,
        request: main_models.GetParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetParameterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parameter_version):
            query['ParameterVersion'] = request.parameter_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetParameter',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_parameter(
        self,
        request: main_models.GetParameterRequest,
    ) -> main_models.GetParameterResponse:
        runtime = RuntimeOptions()
        return self.get_parameter_with_options(request, runtime)

    async def get_parameter_async(
        self,
        request: main_models.GetParameterRequest,
    ) -> main_models.GetParameterResponse:
        runtime = RuntimeOptions()
        return await self.get_parameter_with_options_async(request, runtime)

    def get_parameters_with_options(
        self,
        request: main_models.GetParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.names):
            query['Names'] = request.names
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetParameters',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_parameters_with_options_async(
        self,
        request: main_models.GetParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.names):
            query['Names'] = request.names
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetParameters',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_parameters(
        self,
        request: main_models.GetParametersRequest,
    ) -> main_models.GetParametersResponse:
        runtime = RuntimeOptions()
        return self.get_parameters_with_options(request, runtime)

    async def get_parameters_async(
        self,
        request: main_models.GetParametersRequest,
    ) -> main_models.GetParametersResponse:
        runtime = RuntimeOptions()
        return await self.get_parameters_with_options_async(request, runtime)

    def get_parameters_by_path_with_options(
        self,
        request: main_models.GetParametersByPathRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetParametersByPathResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.recursive):
            query['Recursive'] = request.recursive
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetParametersByPath',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetParametersByPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_parameters_by_path_with_options_async(
        self,
        request: main_models.GetParametersByPathRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetParametersByPathResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.recursive):
            query['Recursive'] = request.recursive
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetParametersByPath',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetParametersByPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_parameters_by_path(
        self,
        request: main_models.GetParametersByPathRequest,
    ) -> main_models.GetParametersByPathResponse:
        runtime = RuntimeOptions()
        return self.get_parameters_by_path_with_options(request, runtime)

    async def get_parameters_by_path_async(
        self,
        request: main_models.GetParametersByPathRequest,
    ) -> main_models.GetParametersByPathResponse:
        runtime = RuntimeOptions()
        return await self.get_parameters_by_path_with_options_async(request, runtime)

    def get_patch_baseline_with_options(
        self,
        request: main_models.GetPatchBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPatchBaselineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPatchBaseline',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPatchBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_patch_baseline_with_options_async(
        self,
        request: main_models.GetPatchBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPatchBaselineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPatchBaseline',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPatchBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_patch_baseline(
        self,
        request: main_models.GetPatchBaselineRequest,
    ) -> main_models.GetPatchBaselineResponse:
        runtime = RuntimeOptions()
        return self.get_patch_baseline_with_options(request, runtime)

    async def get_patch_baseline_async(
        self,
        request: main_models.GetPatchBaselineRequest,
    ) -> main_models.GetPatchBaselineResponse:
        runtime = RuntimeOptions()
        return await self.get_patch_baseline_with_options_async(request, runtime)

    def get_secret_parameter_with_options(
        self,
        request: main_models.GetSecretParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretParameterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parameter_version):
            query['ParameterVersion'] = request.parameter_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.with_decryption):
            query['WithDecryption'] = request.with_decryption
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecretParameter',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secret_parameter_with_options_async(
        self,
        request: main_models.GetSecretParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretParameterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parameter_version):
            query['ParameterVersion'] = request.parameter_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.with_decryption):
            query['WithDecryption'] = request.with_decryption
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecretParameter',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secret_parameter(
        self,
        request: main_models.GetSecretParameterRequest,
    ) -> main_models.GetSecretParameterResponse:
        runtime = RuntimeOptions()
        return self.get_secret_parameter_with_options(request, runtime)

    async def get_secret_parameter_async(
        self,
        request: main_models.GetSecretParameterRequest,
    ) -> main_models.GetSecretParameterResponse:
        runtime = RuntimeOptions()
        return await self.get_secret_parameter_with_options_async(request, runtime)

    def get_secret_parameters_with_options(
        self,
        request: main_models.GetSecretParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.names):
            query['Names'] = request.names
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.with_decryption):
            query['WithDecryption'] = request.with_decryption
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecretParameters',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secret_parameters_with_options_async(
        self,
        request: main_models.GetSecretParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.names):
            query['Names'] = request.names
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.with_decryption):
            query['WithDecryption'] = request.with_decryption
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecretParameters',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secret_parameters(
        self,
        request: main_models.GetSecretParametersRequest,
    ) -> main_models.GetSecretParametersResponse:
        runtime = RuntimeOptions()
        return self.get_secret_parameters_with_options(request, runtime)

    async def get_secret_parameters_async(
        self,
        request: main_models.GetSecretParametersRequest,
    ) -> main_models.GetSecretParametersResponse:
        runtime = RuntimeOptions()
        return await self.get_secret_parameters_with_options_async(request, runtime)

    def get_secret_parameters_by_path_with_options(
        self,
        request: main_models.GetSecretParametersByPathRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretParametersByPathResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.recursive):
            query['Recursive'] = request.recursive
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.with_decryption):
            query['WithDecryption'] = request.with_decryption
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecretParametersByPath',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretParametersByPathResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_secret_parameters_by_path_with_options_async(
        self,
        request: main_models.GetSecretParametersByPathRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSecretParametersByPathResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.recursive):
            query['Recursive'] = request.recursive
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.with_decryption):
            query['WithDecryption'] = request.with_decryption
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSecretParametersByPath',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSecretParametersByPathResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_secret_parameters_by_path(
        self,
        request: main_models.GetSecretParametersByPathRequest,
    ) -> main_models.GetSecretParametersByPathResponse:
        runtime = RuntimeOptions()
        return self.get_secret_parameters_by_path_with_options(request, runtime)

    async def get_secret_parameters_by_path_async(
        self,
        request: main_models.GetSecretParametersByPathRequest,
    ) -> main_models.GetSecretParametersByPathResponse:
        runtime = RuntimeOptions()
        return await self.get_secret_parameters_by_path_with_options_async(request, runtime)

    def get_service_settings_with_options(
        self,
        request: main_models.GetServiceSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceSettingsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceSettings',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_settings_with_options_async(
        self,
        request: main_models.GetServiceSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceSettingsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceSettings',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_settings(
        self,
        request: main_models.GetServiceSettingsRequest,
    ) -> main_models.GetServiceSettingsResponse:
        runtime = RuntimeOptions()
        return self.get_service_settings_with_options(request, runtime)

    async def get_service_settings_async(
        self,
        request: main_models.GetServiceSettingsRequest,
    ) -> main_models.GetServiceSettingsResponse:
        runtime = RuntimeOptions()
        return await self.get_service_settings_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: main_models.GetTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplate',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: main_models.GetTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplate',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        request: main_models.GetTemplateRequest,
    ) -> main_models.GetTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: main_models.GetTemplateRequest,
    ) -> main_models.GetTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def get_template_parameter_constraints_with_options(
        self,
        request: main_models.GetTemplateParameterConstraintsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateParameterConstraintsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_content):
            query['TemplateContent'] = request.template_content
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplateParameterConstraints',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateParameterConstraintsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_parameter_constraints_with_options_async(
        self,
        request: main_models.GetTemplateParameterConstraintsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateParameterConstraintsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_content):
            query['TemplateContent'] = request.template_content
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplateParameterConstraints',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateParameterConstraintsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_parameter_constraints(
        self,
        request: main_models.GetTemplateParameterConstraintsRequest,
    ) -> main_models.GetTemplateParameterConstraintsResponse:
        runtime = RuntimeOptions()
        return self.get_template_parameter_constraints_with_options(request, runtime)

    async def get_template_parameter_constraints_async(
        self,
        request: main_models.GetTemplateParameterConstraintsRequest,
    ) -> main_models.GetTemplateParameterConstraintsResponse:
        runtime = RuntimeOptions()
        return await self.get_template_parameter_constraints_with_options_async(request, runtime)

    def list_actions_with_options(
        self,
        request: main_models.ListActionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListActionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.oosaction_name):
            query['OOSActionName'] = request.oosaction_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListActions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_actions_with_options_async(
        self,
        request: main_models.ListActionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListActionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.oosaction_name):
            query['OOSActionName'] = request.oosaction_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListActions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_actions(
        self,
        request: main_models.ListActionsRequest,
    ) -> main_models.ListActionsResponse:
        runtime = RuntimeOptions()
        return self.list_actions_with_options(request, runtime)

    async def list_actions_async(
        self,
        request: main_models.ListActionsRequest,
    ) -> main_models.ListActionsResponse:
        runtime = RuntimeOptions()
        return await self.list_actions_with_options_async(request, runtime)

    def list_application_groups_with_options(
        self,
        request: main_models.ListApplicationGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.deploy_region_id):
            query['DeployRegionId'] = request.deploy_region_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationGroups',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_groups_with_options_async(
        self,
        request: main_models.ListApplicationGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.deploy_region_id):
            query['DeployRegionId'] = request.deploy_region_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_product):
            query['ResourceProduct'] = request.resource_product
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationGroups',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_groups(
        self,
        request: main_models.ListApplicationGroupsRequest,
    ) -> main_models.ListApplicationGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_application_groups_with_options(request, runtime)

    async def list_application_groups_async(
        self,
        request: main_models.ListApplicationGroupsRequest,
    ) -> main_models.ListApplicationGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_application_groups_with_options_async(request, runtime)

    def list_applications_with_options(
        self,
        tmp_req: main_models.ListApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsResponse:
        tmp_req.validate()
        request = main_models.ListApplicationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.application_type):
            query['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.names):
            query['Names'] = request.names
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplications',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_with_options_async(
        self,
        tmp_req: main_models.ListApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsResponse:
        tmp_req.validate()
        request = main_models.ListApplicationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.application_type):
            query['ApplicationType'] = request.application_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.names):
            query['Names'] = request.names
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplications',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications(
        self,
        request: main_models.ListApplicationsRequest,
    ) -> main_models.ListApplicationsResponse:
        runtime = RuntimeOptions()
        return self.list_applications_with_options(request, runtime)

    async def list_applications_async(
        self,
        request: main_models.ListApplicationsRequest,
    ) -> main_models.ListApplicationsResponse:
        runtime = RuntimeOptions()
        return await self.list_applications_with_options_async(request, runtime)

    def list_execution_logs_with_options(
        self,
        request: main_models.ListExecutionLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExecutionLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_execution_id):
            query['TaskExecutionId'] = request.task_execution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExecutionLogs',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExecutionLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_execution_logs_with_options_async(
        self,
        request: main_models.ListExecutionLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExecutionLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.log_type):
            query['LogType'] = request.log_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_execution_id):
            query['TaskExecutionId'] = request.task_execution_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExecutionLogs',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExecutionLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_execution_logs(
        self,
        request: main_models.ListExecutionLogsRequest,
    ) -> main_models.ListExecutionLogsResponse:
        runtime = RuntimeOptions()
        return self.list_execution_logs_with_options(request, runtime)

    async def list_execution_logs_async(
        self,
        request: main_models.ListExecutionLogsRequest,
    ) -> main_models.ListExecutionLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_execution_logs_with_options_async(request, runtime)

    def list_execution_risky_tasks_with_options(
        self,
        request: main_models.ListExecutionRiskyTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExecutionRiskyTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExecutionRiskyTasks',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExecutionRiskyTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_execution_risky_tasks_with_options_async(
        self,
        request: main_models.ListExecutionRiskyTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExecutionRiskyTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExecutionRiskyTasks',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExecutionRiskyTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_execution_risky_tasks(
        self,
        request: main_models.ListExecutionRiskyTasksRequest,
    ) -> main_models.ListExecutionRiskyTasksResponse:
        runtime = RuntimeOptions()
        return self.list_execution_risky_tasks_with_options(request, runtime)

    async def list_execution_risky_tasks_async(
        self,
        request: main_models.ListExecutionRiskyTasksRequest,
    ) -> main_models.ListExecutionRiskyTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_execution_risky_tasks_with_options_async(request, runtime)

    def list_executions_with_options(
        self,
        tmp_req: main_models.ListExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExecutionsResponse:
        tmp_req.validate()
        request = main_models.ListExecutionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.categories):
            query['Categories'] = request.categories
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.depth):
            query['Depth'] = request.depth
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.end_date_after):
            query['EndDateAfter'] = request.end_date_after
        if not DaraCore.is_null(request.end_date_before):
            query['EndDateBefore'] = request.end_date_before
        if not DaraCore.is_null(request.executed_by):
            query['ExecutedBy'] = request.executed_by
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.include_child_execution):
            query['IncludeChildExecution'] = request.include_child_execution
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.parent_execution_id):
            query['ParentExecutionId'] = request.parent_execution_id
        if not DaraCore.is_null(request.ram_role):
            query['RamRole'] = request.ram_role
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_template_name):
            query['ResourceTemplateName'] = request.resource_template_name
        if not DaraCore.is_null(request.sort_field):
            query['SortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.start_date_after):
            query['StartDateAfter'] = request.start_date_after
        if not DaraCore.is_null(request.start_date_before):
            query['StartDateBefore'] = request.start_date_before
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExecutions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_executions_with_options_async(
        self,
        tmp_req: main_models.ListExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExecutionsResponse:
        tmp_req.validate()
        request = main_models.ListExecutionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.categories):
            query['Categories'] = request.categories
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.depth):
            query['Depth'] = request.depth
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.end_date_after):
            query['EndDateAfter'] = request.end_date_after
        if not DaraCore.is_null(request.end_date_before):
            query['EndDateBefore'] = request.end_date_before
        if not DaraCore.is_null(request.executed_by):
            query['ExecutedBy'] = request.executed_by
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.include_child_execution):
            query['IncludeChildExecution'] = request.include_child_execution
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.parent_execution_id):
            query['ParentExecutionId'] = request.parent_execution_id
        if not DaraCore.is_null(request.ram_role):
            query['RamRole'] = request.ram_role
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_template_name):
            query['ResourceTemplateName'] = request.resource_template_name
        if not DaraCore.is_null(request.sort_field):
            query['SortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.start_date_after):
            query['StartDateAfter'] = request.start_date_after
        if not DaraCore.is_null(request.start_date_before):
            query['StartDateBefore'] = request.start_date_before
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExecutions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_executions(
        self,
        request: main_models.ListExecutionsRequest,
    ) -> main_models.ListExecutionsResponse:
        runtime = RuntimeOptions()
        return self.list_executions_with_options(request, runtime)

    async def list_executions_async(
        self,
        request: main_models.ListExecutionsRequest,
    ) -> main_models.ListExecutionsResponse:
        runtime = RuntimeOptions()
        return await self.list_executions_with_options_async(request, runtime)

    def list_git_accounts_with_options(
        self,
        request: main_models.ListGitAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGitAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_type):
            query['BindType'] = request.bind_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGitAccounts',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGitAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_git_accounts_with_options_async(
        self,
        request: main_models.ListGitAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGitAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_type):
            query['BindType'] = request.bind_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGitAccounts',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGitAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_git_accounts(
        self,
        request: main_models.ListGitAccountsRequest,
    ) -> main_models.ListGitAccountsResponse:
        runtime = RuntimeOptions()
        return self.list_git_accounts_with_options(request, runtime)

    async def list_git_accounts_async(
        self,
        request: main_models.ListGitAccountsRequest,
    ) -> main_models.ListGitAccountsResponse:
        runtime = RuntimeOptions()
        return await self.list_git_accounts_with_options_async(request, runtime)

    def list_git_branches_with_options(
        self,
        request: main_models.ListGitBranchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGitBranchesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_full_name):
            query['RepoFullName'] = request.repo_full_name
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGitBranches',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGitBranchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_git_branches_with_options_async(
        self,
        request: main_models.ListGitBranchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGitBranchesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_full_name):
            query['RepoFullName'] = request.repo_full_name
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGitBranches',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGitBranchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_git_branches(
        self,
        request: main_models.ListGitBranchesRequest,
    ) -> main_models.ListGitBranchesResponse:
        runtime = RuntimeOptions()
        return self.list_git_branches_with_options(request, runtime)

    async def list_git_branches_async(
        self,
        request: main_models.ListGitBranchesRequest,
    ) -> main_models.ListGitBranchesResponse:
        runtime = RuntimeOptions()
        return await self.list_git_branches_with_options_async(request, runtime)

    def list_git_organizations_with_options(
        self,
        request: main_models.ListGitOrganizationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGitOrganizationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_type):
            query['BindType'] = request.bind_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGitOrganizations',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGitOrganizationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_git_organizations_with_options_async(
        self,
        request: main_models.ListGitOrganizationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGitOrganizationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.bind_type):
            query['BindType'] = request.bind_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGitOrganizations',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGitOrganizationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_git_organizations(
        self,
        request: main_models.ListGitOrganizationsRequest,
    ) -> main_models.ListGitOrganizationsResponse:
        runtime = RuntimeOptions()
        return self.list_git_organizations_with_options(request, runtime)

    async def list_git_organizations_async(
        self,
        request: main_models.ListGitOrganizationsRequest,
    ) -> main_models.ListGitOrganizationsResponse:
        runtime = RuntimeOptions()
        return await self.list_git_organizations_with_options_async(request, runtime)

    def list_git_repositories_with_options(
        self,
        request: main_models.ListGitRepositoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGitRepositoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.org_name):
            query['OrgName'] = request.org_name
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGitRepositories',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGitRepositoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_git_repositories_with_options_async(
        self,
        request: main_models.ListGitRepositoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGitRepositoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.org_name):
            query['OrgName'] = request.org_name
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGitRepositories',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGitRepositoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_git_repositories(
        self,
        request: main_models.ListGitRepositoriesRequest,
    ) -> main_models.ListGitRepositoriesResponse:
        runtime = RuntimeOptions()
        return self.list_git_repositories_with_options(request, runtime)

    async def list_git_repositories_async(
        self,
        request: main_models.ListGitRepositoriesRequest,
    ) -> main_models.ListGitRepositoriesResponse:
        runtime = RuntimeOptions()
        return await self.list_git_repositories_with_options_async(request, runtime)

    def list_git_repository_contents_with_options(
        self,
        request: main_models.ListGitRepositoryContentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGitRepositoryContentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.branch):
            query['Branch'] = request.branch
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.content_type):
            query['ContentType'] = request.content_type
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_full_name):
            query['RepoFullName'] = request.repo_full_name
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGitRepositoryContents',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGitRepositoryContentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_git_repository_contents_with_options_async(
        self,
        request: main_models.ListGitRepositoryContentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGitRepositoryContentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.branch):
            query['Branch'] = request.branch
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.content_type):
            query['ContentType'] = request.content_type
        if not DaraCore.is_null(request.org_id):
            query['OrgId'] = request.org_id
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.platform):
            query['Platform'] = request.platform
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_full_name):
            query['RepoFullName'] = request.repo_full_name
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGitRepositoryContents',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGitRepositoryContentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_git_repository_contents(
        self,
        request: main_models.ListGitRepositoryContentsRequest,
    ) -> main_models.ListGitRepositoryContentsResponse:
        runtime = RuntimeOptions()
        return self.list_git_repository_contents_with_options(request, runtime)

    async def list_git_repository_contents_async(
        self,
        request: main_models.ListGitRepositoryContentsRequest,
    ) -> main_models.ListGitRepositoryContentsResponse:
        runtime = RuntimeOptions()
        return await self.list_git_repository_contents_with_options_async(request, runtime)

    def list_instance_package_states_with_options(
        self,
        request: main_models.ListInstancePackageStatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancePackageStatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_names):
            query['TemplateNames'] = request.template_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstancePackageStates',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancePackageStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_package_states_with_options_async(
        self,
        request: main_models.ListInstancePackageStatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancePackageStatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_names):
            query['TemplateNames'] = request.template_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstancePackageStates',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancePackageStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_package_states(
        self,
        request: main_models.ListInstancePackageStatesRequest,
    ) -> main_models.ListInstancePackageStatesResponse:
        runtime = RuntimeOptions()
        return self.list_instance_package_states_with_options(request, runtime)

    async def list_instance_package_states_async(
        self,
        request: main_models.ListInstancePackageStatesRequest,
    ) -> main_models.ListInstancePackageStatesResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_package_states_with_options_async(request, runtime)

    def list_instance_patch_states_with_options(
        self,
        request: main_models.ListInstancePatchStatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancePatchStatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstancePatchStates',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancePatchStatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_patch_states_with_options_async(
        self,
        request: main_models.ListInstancePatchStatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancePatchStatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstancePatchStates',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancePatchStatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_patch_states(
        self,
        request: main_models.ListInstancePatchStatesRequest,
    ) -> main_models.ListInstancePatchStatesResponse:
        runtime = RuntimeOptions()
        return self.list_instance_patch_states_with_options(request, runtime)

    async def list_instance_patch_states_async(
        self,
        request: main_models.ListInstancePatchStatesRequest,
    ) -> main_models.ListInstancePatchStatesResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_patch_states_with_options_async(request, runtime)

    def list_instance_patches_with_options(
        self,
        request: main_models.ListInstancePatchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancePatchesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.patch_statuses):
            query['PatchStatuses'] = request.patch_statuses
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstancePatches',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancePatchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_patches_with_options_async(
        self,
        request: main_models.ListInstancePatchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstancePatchesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.patch_statuses):
            query['PatchStatuses'] = request.patch_statuses
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstancePatches',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstancePatchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_patches(
        self,
        request: main_models.ListInstancePatchesRequest,
    ) -> main_models.ListInstancePatchesResponse:
        runtime = RuntimeOptions()
        return self.list_instance_patches_with_options(request, runtime)

    async def list_instance_patches_async(
        self,
        request: main_models.ListInstancePatchesRequest,
    ) -> main_models.ListInstancePatchesResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_patches_with_options_async(request, runtime)

    def list_inventory_entries_with_options(
        self,
        request: main_models.ListInventoryEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInventoryEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type_name):
            query['TypeName'] = request.type_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInventoryEntries',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInventoryEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_inventory_entries_with_options_async(
        self,
        request: main_models.ListInventoryEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInventoryEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type_name):
            query['TypeName'] = request.type_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInventoryEntries',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInventoryEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_inventory_entries(
        self,
        request: main_models.ListInventoryEntriesRequest,
    ) -> main_models.ListInventoryEntriesResponse:
        runtime = RuntimeOptions()
        return self.list_inventory_entries_with_options(request, runtime)

    async def list_inventory_entries_async(
        self,
        request: main_models.ListInventoryEntriesRequest,
    ) -> main_models.ListInventoryEntriesResponse:
        runtime = RuntimeOptions()
        return await self.list_inventory_entries_with_options_async(request, runtime)

    def list_ops_items_with_options(
        self,
        tmp_req: main_models.ListOpsItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOpsItemsResponse:
        tmp_req.validate()
        request = main_models.ListOpsItemsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_tags):
            request.resource_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_tags, 'ResourceTags', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_tags_shrink):
            query['ResourceTags'] = request.resource_tags_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOpsItems',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOpsItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ops_items_with_options_async(
        self,
        tmp_req: main_models.ListOpsItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOpsItemsResponse:
        tmp_req.validate()
        request = main_models.ListOpsItemsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_tags):
            request.resource_tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_tags, 'ResourceTags', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_tags_shrink):
            query['ResourceTags'] = request.resource_tags_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOpsItems',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOpsItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ops_items(
        self,
        request: main_models.ListOpsItemsRequest,
    ) -> main_models.ListOpsItemsResponse:
        runtime = RuntimeOptions()
        return self.list_ops_items_with_options(request, runtime)

    async def list_ops_items_async(
        self,
        request: main_models.ListOpsItemsRequest,
    ) -> main_models.ListOpsItemsResponse:
        runtime = RuntimeOptions()
        return await self.list_ops_items_with_options_async(request, runtime)

    def list_parameter_versions_with_options(
        self,
        request: main_models.ListParameterVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListParameterVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListParameterVersions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListParameterVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_parameter_versions_with_options_async(
        self,
        request: main_models.ListParameterVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListParameterVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListParameterVersions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListParameterVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_parameter_versions(
        self,
        request: main_models.ListParameterVersionsRequest,
    ) -> main_models.ListParameterVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_parameter_versions_with_options(request, runtime)

    async def list_parameter_versions_async(
        self,
        request: main_models.ListParameterVersionsRequest,
    ) -> main_models.ListParameterVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_parameter_versions_with_options_async(request, runtime)

    def list_parameters_with_options(
        self,
        tmp_req: main_models.ListParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListParametersResponse:
        tmp_req.validate()
        request = main_models.ListParametersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.recursive):
            query['Recursive'] = request.recursive
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        if not DaraCore.is_null(request.sort_field):
            query['SortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListParameters',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_parameters_with_options_async(
        self,
        tmp_req: main_models.ListParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListParametersResponse:
        tmp_req.validate()
        request = main_models.ListParametersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.recursive):
            query['Recursive'] = request.recursive
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        if not DaraCore.is_null(request.sort_field):
            query['SortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListParameters',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_parameters(
        self,
        request: main_models.ListParametersRequest,
    ) -> main_models.ListParametersResponse:
        runtime = RuntimeOptions()
        return self.list_parameters_with_options(request, runtime)

    async def list_parameters_async(
        self,
        request: main_models.ListParametersRequest,
    ) -> main_models.ListParametersResponse:
        runtime = RuntimeOptions()
        return await self.list_parameters_with_options_async(request, runtime)

    def list_patch_baselines_with_options(
        self,
        tmp_req: main_models.ListPatchBaselinesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPatchBaselinesResponse:
        tmp_req.validate()
        request = main_models.ListPatchBaselinesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.approved_patches):
            request.approved_patches_shrink = Utils.array_to_string_with_specified_style(tmp_req.approved_patches, 'ApprovedPatches', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.approved_patches_shrink):
            query['ApprovedPatches'] = request.approved_patches_shrink
        if not DaraCore.is_null(request.approved_patches_enable_non_security):
            query['ApprovedPatchesEnableNonSecurity'] = request.approved_patches_enable_non_security
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.operation_system):
            query['OperationSystem'] = request.operation_system
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        if not DaraCore.is_null(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPatchBaselines',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPatchBaselinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_patch_baselines_with_options_async(
        self,
        tmp_req: main_models.ListPatchBaselinesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPatchBaselinesResponse:
        tmp_req.validate()
        request = main_models.ListPatchBaselinesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.approved_patches):
            request.approved_patches_shrink = Utils.array_to_string_with_specified_style(tmp_req.approved_patches, 'ApprovedPatches', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.approved_patches_shrink):
            query['ApprovedPatches'] = request.approved_patches_shrink
        if not DaraCore.is_null(request.approved_patches_enable_non_security):
            query['ApprovedPatchesEnableNonSecurity'] = request.approved_patches_enable_non_security
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.operation_system):
            query['OperationSystem'] = request.operation_system
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        if not DaraCore.is_null(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPatchBaselines',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPatchBaselinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_patch_baselines(
        self,
        request: main_models.ListPatchBaselinesRequest,
    ) -> main_models.ListPatchBaselinesResponse:
        runtime = RuntimeOptions()
        return self.list_patch_baselines_with_options(request, runtime)

    async def list_patch_baselines_async(
        self,
        request: main_models.ListPatchBaselinesRequest,
    ) -> main_models.ListPatchBaselinesResponse:
        runtime = RuntimeOptions()
        return await self.list_patch_baselines_with_options_async(request, runtime)

    def list_resource_execution_status_with_options(
        self,
        request: main_models.ListResourceExecutionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceExecutionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceExecutionStatus',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceExecutionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_execution_status_with_options_async(
        self,
        request: main_models.ListResourceExecutionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceExecutionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceExecutionStatus',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceExecutionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_execution_status(
        self,
        request: main_models.ListResourceExecutionStatusRequest,
    ) -> main_models.ListResourceExecutionStatusResponse:
        runtime = RuntimeOptions()
        return self.list_resource_execution_status_with_options(request, runtime)

    async def list_resource_execution_status_async(
        self,
        request: main_models.ListResourceExecutionStatusRequest,
    ) -> main_models.ListResourceExecutionStatusResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_execution_status_with_options_async(request, runtime)

    def list_secret_parameter_versions_with_options(
        self,
        request: main_models.ListSecretParameterVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecretParameterVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        if not DaraCore.is_null(request.with_decryption):
            query['WithDecryption'] = request.with_decryption
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecretParameterVersions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecretParameterVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_secret_parameter_versions_with_options_async(
        self,
        request: main_models.ListSecretParameterVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecretParameterVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        if not DaraCore.is_null(request.with_decryption):
            query['WithDecryption'] = request.with_decryption
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecretParameterVersions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecretParameterVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_secret_parameter_versions(
        self,
        request: main_models.ListSecretParameterVersionsRequest,
    ) -> main_models.ListSecretParameterVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_secret_parameter_versions_with_options(request, runtime)

    async def list_secret_parameter_versions_async(
        self,
        request: main_models.ListSecretParameterVersionsRequest,
    ) -> main_models.ListSecretParameterVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_secret_parameter_versions_with_options_async(request, runtime)

    def list_secret_parameters_with_options(
        self,
        tmp_req: main_models.ListSecretParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecretParametersResponse:
        tmp_req.validate()
        request = main_models.ListSecretParametersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.recursive):
            query['Recursive'] = request.recursive
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sort_field):
            query['SortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecretParameters',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecretParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_secret_parameters_with_options_async(
        self,
        tmp_req: main_models.ListSecretParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSecretParametersResponse:
        tmp_req.validate()
        request = main_models.ListSecretParametersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.path):
            query['Path'] = request.path
        if not DaraCore.is_null(request.recursive):
            query['Recursive'] = request.recursive
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sort_field):
            query['SortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSecretParameters',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSecretParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_secret_parameters(
        self,
        request: main_models.ListSecretParametersRequest,
    ) -> main_models.ListSecretParametersResponse:
        runtime = RuntimeOptions()
        return self.list_secret_parameters_with_options(request, runtime)

    async def list_secret_parameters_async(
        self,
        request: main_models.ListSecretParametersRequest,
    ) -> main_models.ListSecretParametersResponse:
        runtime = RuntimeOptions()
        return await self.list_secret_parameters_with_options_async(request, runtime)

    def list_state_configurations_with_options(
        self,
        tmp_req: main_models.ListStateConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStateConfigurationsResponse:
        tmp_req.validate()
        request = main_models.ListStateConfigurationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state_configuration_ids):
            query['StateConfigurationIds'] = request.state_configuration_ids
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStateConfigurations',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStateConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_state_configurations_with_options_async(
        self,
        tmp_req: main_models.ListStateConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStateConfigurationsResponse:
        tmp_req.validate()
        request = main_models.ListStateConfigurationsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.state_configuration_ids):
            query['StateConfigurationIds'] = request.state_configuration_ids
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStateConfigurations',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStateConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_state_configurations(
        self,
        request: main_models.ListStateConfigurationsRequest,
    ) -> main_models.ListStateConfigurationsResponse:
        runtime = RuntimeOptions()
        return self.list_state_configurations_with_options(request, runtime)

    async def list_state_configurations_async(
        self,
        request: main_models.ListStateConfigurationsRequest,
    ) -> main_models.ListStateConfigurationsResponse:
        runtime = RuntimeOptions()
        return await self.list_state_configurations_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        tmp_req: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-06-01',
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
        tmp_req: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        tmp_req.validate()
        request = main_models.ListTagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-06-01',
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

    def list_tag_values_with_options(
        self,
        request: main_models.ListTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagValues',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: main_models.ListTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagValues',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: main_models.ListTagValuesRequest,
    ) -> main_models.ListTagValuesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: main_models.ListTagValuesRequest,
    ) -> main_models.ListTagValuesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def list_task_executions_with_options(
        self,
        request: main_models.ListTaskExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTaskExecutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date_after):
            query['EndDateAfter'] = request.end_date_after
        if not DaraCore.is_null(request.end_date_before):
            query['EndDateBefore'] = request.end_date_before
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.include_child_task_execution):
            query['IncludeChildTaskExecution'] = request.include_child_task_execution
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.parent_task_execution_id):
            query['ParentTaskExecutionId'] = request.parent_task_execution_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort_field):
            query['SortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.start_date_after):
            query['StartDateAfter'] = request.start_date_after
        if not DaraCore.is_null(request.start_date_before):
            query['StartDateBefore'] = request.start_date_before
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_action):
            query['TaskAction'] = request.task_action
        if not DaraCore.is_null(request.task_execution_id):
            query['TaskExecutionId'] = request.task_execution_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTaskExecutions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTaskExecutionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_executions_with_options_async(
        self,
        request: main_models.ListTaskExecutionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTaskExecutionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date_after):
            query['EndDateAfter'] = request.end_date_after
        if not DaraCore.is_null(request.end_date_before):
            query['EndDateBefore'] = request.end_date_before
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.include_child_task_execution):
            query['IncludeChildTaskExecution'] = request.include_child_task_execution
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.parent_task_execution_id):
            query['ParentTaskExecutionId'] = request.parent_task_execution_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort_field):
            query['SortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.start_date_after):
            query['StartDateAfter'] = request.start_date_after
        if not DaraCore.is_null(request.start_date_before):
            query['StartDateBefore'] = request.start_date_before
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.task_action):
            query['TaskAction'] = request.task_action
        if not DaraCore.is_null(request.task_execution_id):
            query['TaskExecutionId'] = request.task_execution_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTaskExecutions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTaskExecutionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_executions(
        self,
        request: main_models.ListTaskExecutionsRequest,
    ) -> main_models.ListTaskExecutionsResponse:
        runtime = RuntimeOptions()
        return self.list_task_executions_with_options(request, runtime)

    async def list_task_executions_async(
        self,
        request: main_models.ListTaskExecutionsRequest,
    ) -> main_models.ListTaskExecutionsResponse:
        runtime = RuntimeOptions()
        return await self.list_task_executions_with_options_async(request, runtime)

    def list_template_versions_with_options(
        self,
        request: main_models.ListTemplateVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplateVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplateVersions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplateVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_template_versions_with_options_async(
        self,
        request: main_models.ListTemplateVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplateVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplateVersions',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplateVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_template_versions(
        self,
        request: main_models.ListTemplateVersionsRequest,
    ) -> main_models.ListTemplateVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_template_versions_with_options(request, runtime)

    async def list_template_versions_async(
        self,
        request: main_models.ListTemplateVersionsRequest,
    ) -> main_models.ListTemplateVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_template_versions_with_options_async(request, runtime)

    def list_templates_with_options(
        self,
        tmp_req: main_models.ListTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplatesResponse:
        tmp_req.validate()
        request = main_models.ListTemplatesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.created_by):
            query['CreatedBy'] = request.created_by
        if not DaraCore.is_null(request.created_date_after):
            query['CreatedDateAfter'] = request.created_date_after
        if not DaraCore.is_null(request.created_date_before):
            query['CreatedDateBefore'] = request.created_date_before
        if not DaraCore.is_null(request.has_trigger):
            query['HasTrigger'] = request.has_trigger
        if not DaraCore.is_null(request.is_example):
            query['IsExample'] = request.is_example
        if not DaraCore.is_null(request.is_favorite):
            query['IsFavorite'] = request.is_favorite
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        if not DaraCore.is_null(request.sort_field):
            query['SortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.template_format):
            query['TemplateFormat'] = request.template_format
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplates',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        tmp_req: main_models.ListTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplatesResponse:
        tmp_req.validate()
        request = main_models.ListTemplatesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.created_by):
            query['CreatedBy'] = request.created_by
        if not DaraCore.is_null(request.created_date_after):
            query['CreatedDateAfter'] = request.created_date_after
        if not DaraCore.is_null(request.created_date_before):
            query['CreatedDateBefore'] = request.created_date_before
        if not DaraCore.is_null(request.has_trigger):
            query['HasTrigger'] = request.has_trigger
        if not DaraCore.is_null(request.is_example):
            query['IsExample'] = request.is_example
        if not DaraCore.is_null(request.is_favorite):
            query['IsFavorite'] = request.is_favorite
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        if not DaraCore.is_null(request.sort_field):
            query['SortField'] = request.sort_field
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.template_format):
            query['TemplateFormat'] = request.template_format
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplates',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_templates(
        self,
        request: main_models.ListTemplatesRequest,
    ) -> main_models.ListTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    async def list_templates_async(
        self,
        request: main_models.ListTemplatesRequest,
    ) -> main_models.ListTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_templates_with_options_async(request, runtime)

    def notify_execution_with_options(
        self,
        request: main_models.NotifyExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.NotifyExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.execution_status):
            query['ExecutionStatus'] = request.execution_status
        if not DaraCore.is_null(request.loop_item):
            query['LoopItem'] = request.loop_item
        if not DaraCore.is_null(request.notify_note):
            query['NotifyNote'] = request.notify_note
        if not DaraCore.is_null(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_execution_id):
            query['TaskExecutionId'] = request.task_execution_id
        if not DaraCore.is_null(request.task_execution_ids):
            query['TaskExecutionIds'] = request.task_execution_ids
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'NotifyExecution',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.NotifyExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def notify_execution_with_options_async(
        self,
        request: main_models.NotifyExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.NotifyExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.execution_status):
            query['ExecutionStatus'] = request.execution_status
        if not DaraCore.is_null(request.loop_item):
            query['LoopItem'] = request.loop_item
        if not DaraCore.is_null(request.notify_note):
            query['NotifyNote'] = request.notify_note
        if not DaraCore.is_null(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_execution_id):
            query['TaskExecutionId'] = request.task_execution_id
        if not DaraCore.is_null(request.task_execution_ids):
            query['TaskExecutionIds'] = request.task_execution_ids
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'NotifyExecution',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.NotifyExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def notify_execution(
        self,
        request: main_models.NotifyExecutionRequest,
    ) -> main_models.NotifyExecutionResponse:
        runtime = RuntimeOptions()
        return self.notify_execution_with_options(request, runtime)

    async def notify_execution_async(
        self,
        request: main_models.NotifyExecutionRequest,
    ) -> main_models.NotifyExecutionResponse:
        runtime = RuntimeOptions()
        return await self.notify_execution_with_options_async(request, runtime)

    def register_default_patch_baseline_with_options(
        self,
        request: main_models.RegisterDefaultPatchBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterDefaultPatchBaselineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterDefaultPatchBaseline',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterDefaultPatchBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_default_patch_baseline_with_options_async(
        self,
        request: main_models.RegisterDefaultPatchBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterDefaultPatchBaselineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterDefaultPatchBaseline',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterDefaultPatchBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_default_patch_baseline(
        self,
        request: main_models.RegisterDefaultPatchBaselineRequest,
    ) -> main_models.RegisterDefaultPatchBaselineResponse:
        runtime = RuntimeOptions()
        return self.register_default_patch_baseline_with_options(request, runtime)

    async def register_default_patch_baseline_async(
        self,
        request: main_models.RegisterDefaultPatchBaselineRequest,
    ) -> main_models.RegisterDefaultPatchBaselineResponse:
        runtime = RuntimeOptions()
        return await self.register_default_patch_baseline_with_options_async(request, runtime)

    def search_inventory_with_options(
        self,
        request: main_models.SearchInventoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchInventoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator):
            query['Aggregator'] = request.aggregator
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchInventory',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchInventoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_inventory_with_options_async(
        self,
        request: main_models.SearchInventoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchInventoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregator):
            query['Aggregator'] = request.aggregator
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchInventory',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchInventoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_inventory(
        self,
        request: main_models.SearchInventoryRequest,
    ) -> main_models.SearchInventoryResponse:
        runtime = RuntimeOptions()
        return self.search_inventory_with_options(request, runtime)

    async def search_inventory_async(
        self,
        request: main_models.SearchInventoryRequest,
    ) -> main_models.SearchInventoryResponse:
        runtime = RuntimeOptions()
        return await self.search_inventory_with_options_async(request, runtime)

    def set_service_settings_with_options(
        self,
        request: main_models.SetServiceSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetServiceSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_oss_bucket_name):
            query['DeliveryOssBucketName'] = request.delivery_oss_bucket_name
        if not DaraCore.is_null(request.delivery_oss_enabled):
            query['DeliveryOssEnabled'] = request.delivery_oss_enabled
        if not DaraCore.is_null(request.delivery_oss_key_prefix):
            query['DeliveryOssKeyPrefix'] = request.delivery_oss_key_prefix
        if not DaraCore.is_null(request.delivery_sls_enabled):
            query['DeliverySlsEnabled'] = request.delivery_sls_enabled
        if not DaraCore.is_null(request.delivery_sls_project_name):
            query['DeliverySlsProjectName'] = request.delivery_sls_project_name
        if not DaraCore.is_null(request.rdc_enterprise_id):
            query['RdcEnterpriseId'] = request.rdc_enterprise_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetServiceSettings',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetServiceSettingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_service_settings_with_options_async(
        self,
        request: main_models.SetServiceSettingsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetServiceSettingsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_oss_bucket_name):
            query['DeliveryOssBucketName'] = request.delivery_oss_bucket_name
        if not DaraCore.is_null(request.delivery_oss_enabled):
            query['DeliveryOssEnabled'] = request.delivery_oss_enabled
        if not DaraCore.is_null(request.delivery_oss_key_prefix):
            query['DeliveryOssKeyPrefix'] = request.delivery_oss_key_prefix
        if not DaraCore.is_null(request.delivery_sls_enabled):
            query['DeliverySlsEnabled'] = request.delivery_sls_enabled
        if not DaraCore.is_null(request.delivery_sls_project_name):
            query['DeliverySlsProjectName'] = request.delivery_sls_project_name
        if not DaraCore.is_null(request.rdc_enterprise_id):
            query['RdcEnterpriseId'] = request.rdc_enterprise_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetServiceSettings',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetServiceSettingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_service_settings(
        self,
        request: main_models.SetServiceSettingsRequest,
    ) -> main_models.SetServiceSettingsResponse:
        runtime = RuntimeOptions()
        return self.set_service_settings_with_options(request, runtime)

    async def set_service_settings_async(
        self,
        request: main_models.SetServiceSettingsRequest,
    ) -> main_models.SetServiceSettingsResponse:
        runtime = RuntimeOptions()
        return await self.set_service_settings_with_options_async(request, runtime)

    def start_debug_execution_with_options(
        self,
        request: main_models.StartDebugExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDebugExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.properties):
            query['Properties'] = request.properties
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDebugExecution',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDebugExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_debug_execution_with_options_async(
        self,
        request: main_models.StartDebugExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartDebugExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.properties):
            query['Properties'] = request.properties
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartDebugExecution',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartDebugExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_debug_execution(
        self,
        request: main_models.StartDebugExecutionRequest,
    ) -> main_models.StartDebugExecutionResponse:
        runtime = RuntimeOptions()
        return self.start_debug_execution_with_options(request, runtime)

    async def start_debug_execution_async(
        self,
        request: main_models.StartDebugExecutionRequest,
    ) -> main_models.StartDebugExecutionResponse:
        runtime = RuntimeOptions()
        return await self.start_debug_execution_with_options_async(request, runtime)

    def start_execution_with_options(
        self,
        tmp_req: main_models.StartExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartExecutionResponse:
        tmp_req.validate()
        request = main_models.StartExecutionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.loop_mode):
            query['LoopMode'] = request.loop_mode
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.parent_execution_id):
            query['ParentExecutionId'] = request.parent_execution_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.safety_check):
            query['SafetyCheck'] = request.safety_check
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.template_content):
            query['TemplateContent'] = request.template_content
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartExecution',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_execution_with_options_async(
        self,
        tmp_req: main_models.StartExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartExecutionResponse:
        tmp_req.validate()
        request = main_models.StartExecutionShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.loop_mode):
            query['LoopMode'] = request.loop_mode
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.parent_execution_id):
            query['ParentExecutionId'] = request.parent_execution_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.safety_check):
            query['SafetyCheck'] = request.safety_check
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.template_content):
            query['TemplateContent'] = request.template_content
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartExecution',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_execution(
        self,
        request: main_models.StartExecutionRequest,
    ) -> main_models.StartExecutionResponse:
        runtime = RuntimeOptions()
        return self.start_execution_with_options(request, runtime)

    async def start_execution_async(
        self,
        request: main_models.StartExecutionRequest,
    ) -> main_models.StartExecutionResponse:
        runtime = RuntimeOptions()
        return await self.start_execution_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        tmp_req: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        tmp_req.validate()
        request = main_models.TagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-06-01',
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
        tmp_req: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        tmp_req.validate()
        request = main_models.TagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-06-01',
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

    def trigger_execution_with_options(
        self,
        request: main_models.TriggerExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TriggerExecution',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_execution_with_options_async(
        self,
        request: main_models.TriggerExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TriggerExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TriggerExecution',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_execution(
        self,
        request: main_models.TriggerExecutionRequest,
    ) -> main_models.TriggerExecutionResponse:
        runtime = RuntimeOptions()
        return self.trigger_execution_with_options(request, runtime)

    async def trigger_execution_async(
        self,
        request: main_models.TriggerExecutionRequest,
    ) -> main_models.TriggerExecutionResponse:
        runtime = RuntimeOptions()
        return await self.trigger_execution_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        tmp_req: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not DaraCore.is_null(tmp_req.tag_keys):
            request.tag_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-06-01',
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
        tmp_req: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        tmp_req.validate()
        request = main_models.UntagResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.resource_ids):
            request.resource_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_ids, 'ResourceIds', 'json')
        if not DaraCore.is_null(tmp_req.tag_keys):
            request.tag_keys_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag_keys, 'TagKeys', 'json')
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids_shrink):
            query['ResourceIds'] = request.resource_ids_shrink
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys_shrink):
            query['TagKeys'] = request.tag_keys_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-06-01',
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

    def update_application_with_options(
        self,
        tmp_req: main_models.UpdateApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationResponse:
        tmp_req.validate()
        request = main_models.UpdateApplicationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.alarm_config):
            request.alarm_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.alarm_config, 'AlarmConfig', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.alarm_config_shrink):
            query['AlarmConfig'] = request.alarm_config_shrink
        if not DaraCore.is_null(request.delete_alarm_rules_before_update):
            query['DeleteAlarmRulesBeforeUpdate'] = request.delete_alarm_rules_before_update
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplication',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_with_options_async(
        self,
        tmp_req: main_models.UpdateApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationResponse:
        tmp_req.validate()
        request = main_models.UpdateApplicationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.alarm_config):
            request.alarm_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.alarm_config, 'AlarmConfig', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.alarm_config_shrink):
            query['AlarmConfig'] = request.alarm_config_shrink
        if not DaraCore.is_null(request.delete_alarm_rules_before_update):
            query['DeleteAlarmRulesBeforeUpdate'] = request.delete_alarm_rules_before_update
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplication',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application(
        self,
        request: main_models.UpdateApplicationRequest,
    ) -> main_models.UpdateApplicationResponse:
        runtime = RuntimeOptions()
        return self.update_application_with_options(request, runtime)

    async def update_application_async(
        self,
        request: main_models.UpdateApplicationRequest,
    ) -> main_models.UpdateApplicationResponse:
        runtime = RuntimeOptions()
        return await self.update_application_with_options_async(request, runtime)

    def update_application_group_with_options(
        self,
        tmp_req: main_models.UpdateApplicationGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationGroupResponse:
        tmp_req.validate()
        request = main_models.UpdateApplicationGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.deployed_revision_id):
            query['DeployedRevisionId'] = request.deployed_revision_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.new_name):
            query['NewName'] = request.new_name
        if not DaraCore.is_null(request.operation_name):
            query['OperationName'] = request.operation_name
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationGroup',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_group_with_options_async(
        self,
        tmp_req: main_models.UpdateApplicationGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationGroupResponse:
        tmp_req.validate()
        request = main_models.UpdateApplicationGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.deployed_revision_id):
            query['DeployedRevisionId'] = request.deployed_revision_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.new_name):
            query['NewName'] = request.new_name
        if not DaraCore.is_null(request.operation_name):
            query['OperationName'] = request.operation_name
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationGroup',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_group(
        self,
        request: main_models.UpdateApplicationGroupRequest,
    ) -> main_models.UpdateApplicationGroupResponse:
        runtime = RuntimeOptions()
        return self.update_application_group_with_options(request, runtime)

    async def update_application_group_async(
        self,
        request: main_models.UpdateApplicationGroupRequest,
    ) -> main_models.UpdateApplicationGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_application_group_with_options_async(request, runtime)

    def update_execution_with_options(
        self,
        request: main_models.UpdateExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExecution',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExecutionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_execution_with_options_async(
        self,
        request: main_models.UpdateExecutionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExecutionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_id):
            query['ExecutionId'] = request.execution_id
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExecution',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExecutionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_execution(
        self,
        request: main_models.UpdateExecutionRequest,
    ) -> main_models.UpdateExecutionResponse:
        runtime = RuntimeOptions()
        return self.update_execution_with_options(request, runtime)

    async def update_execution_async(
        self,
        request: main_models.UpdateExecutionRequest,
    ) -> main_models.UpdateExecutionResponse:
        runtime = RuntimeOptions()
        return await self.update_execution_with_options_async(request, runtime)

    def update_instance_package_state_with_options(
        self,
        tmp_req: main_models.UpdateInstancePackageStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstancePackageStateResponse:
        tmp_req.validate()
        request = main_models.UpdateInstancePackageStateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.configuration_info):
            query['ConfigurationInfo'] = request.configuration_info
        if not DaraCore.is_null(request.configure_action):
            query['ConfigureAction'] = request.configure_action
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstancePackageState',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstancePackageStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_instance_package_state_with_options_async(
        self,
        tmp_req: main_models.UpdateInstancePackageStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateInstancePackageStateResponse:
        tmp_req.validate()
        request = main_models.UpdateInstancePackageStateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.configuration_info):
            query['ConfigurationInfo'] = request.configuration_info
        if not DaraCore.is_null(request.configure_action):
            query['ConfigureAction'] = request.configure_action
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateInstancePackageState',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateInstancePackageStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_instance_package_state(
        self,
        request: main_models.UpdateInstancePackageStateRequest,
    ) -> main_models.UpdateInstancePackageStateResponse:
        runtime = RuntimeOptions()
        return self.update_instance_package_state_with_options(request, runtime)

    async def update_instance_package_state_async(
        self,
        request: main_models.UpdateInstancePackageStateRequest,
    ) -> main_models.UpdateInstancePackageStateResponse:
        runtime = RuntimeOptions()
        return await self.update_instance_package_state_with_options_async(request, runtime)

    def update_ops_item_with_options(
        self,
        tmp_req: main_models.UpdateOpsItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOpsItemResponse:
        tmp_req.validate()
        request = main_models.UpdateOpsItemShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dedup_string):
            query['DedupString'] = request.dedup_string
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ops_item_id):
            query['OpsItemId'] = request.ops_item_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.solutions):
            query['Solutions'] = request.solutions
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOpsItem',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOpsItemResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ops_item_with_options_async(
        self,
        tmp_req: main_models.UpdateOpsItemRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateOpsItemResponse:
        tmp_req.validate()
        request = main_models.UpdateOpsItemShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dedup_string):
            query['DedupString'] = request.dedup_string
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ops_item_id):
            query['OpsItemId'] = request.ops_item_id
        if not DaraCore.is_null(request.priority):
            query['Priority'] = request.priority
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.solutions):
            query['Solutions'] = request.solutions
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateOpsItem',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateOpsItemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ops_item(
        self,
        request: main_models.UpdateOpsItemRequest,
    ) -> main_models.UpdateOpsItemResponse:
        runtime = RuntimeOptions()
        return self.update_ops_item_with_options(request, runtime)

    async def update_ops_item_async(
        self,
        request: main_models.UpdateOpsItemRequest,
    ) -> main_models.UpdateOpsItemResponse:
        runtime = RuntimeOptions()
        return await self.update_ops_item_with_options_async(request, runtime)

    def update_parameter_with_options(
        self,
        request: main_models.UpdateParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateParameterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateParameter',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_parameter_with_options_async(
        self,
        request: main_models.UpdateParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateParameterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateParameter',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_parameter(
        self,
        request: main_models.UpdateParameterRequest,
    ) -> main_models.UpdateParameterResponse:
        runtime = RuntimeOptions()
        return self.update_parameter_with_options(request, runtime)

    async def update_parameter_async(
        self,
        request: main_models.UpdateParameterRequest,
    ) -> main_models.UpdateParameterResponse:
        runtime = RuntimeOptions()
        return await self.update_parameter_with_options_async(request, runtime)

    def update_patch_baseline_with_options(
        self,
        tmp_req: main_models.UpdatePatchBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePatchBaselineResponse:
        tmp_req.validate()
        request = main_models.UpdatePatchBaselineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.approved_patches):
            request.approved_patches_shrink = Utils.array_to_string_with_specified_style(tmp_req.approved_patches, 'ApprovedPatches', 'json')
        if not DaraCore.is_null(tmp_req.rejected_patches):
            request.rejected_patches_shrink = Utils.array_to_string_with_specified_style(tmp_req.rejected_patches, 'RejectedPatches', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.approval_rules):
            query['ApprovalRules'] = request.approval_rules
        if not DaraCore.is_null(request.approved_patches_shrink):
            query['ApprovedPatches'] = request.approved_patches_shrink
        if not DaraCore.is_null(request.approved_patches_enable_non_security):
            query['ApprovedPatchesEnableNonSecurity'] = request.approved_patches_enable_non_security
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rejected_patches_shrink):
            query['RejectedPatches'] = request.rejected_patches_shrink
        if not DaraCore.is_null(request.rejected_patches_action):
            query['RejectedPatchesAction'] = request.rejected_patches_action
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePatchBaseline',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePatchBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_patch_baseline_with_options_async(
        self,
        tmp_req: main_models.UpdatePatchBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePatchBaselineResponse:
        tmp_req.validate()
        request = main_models.UpdatePatchBaselineShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.approved_patches):
            request.approved_patches_shrink = Utils.array_to_string_with_specified_style(tmp_req.approved_patches, 'ApprovedPatches', 'json')
        if not DaraCore.is_null(tmp_req.rejected_patches):
            request.rejected_patches_shrink = Utils.array_to_string_with_specified_style(tmp_req.rejected_patches, 'RejectedPatches', 'json')
        if not DaraCore.is_null(tmp_req.sources):
            request.sources_shrink = Utils.array_to_string_with_specified_style(tmp_req.sources, 'Sources', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.approval_rules):
            query['ApprovalRules'] = request.approval_rules
        if not DaraCore.is_null(request.approved_patches_shrink):
            query['ApprovedPatches'] = request.approved_patches_shrink
        if not DaraCore.is_null(request.approved_patches_enable_non_security):
            query['ApprovedPatchesEnableNonSecurity'] = request.approved_patches_enable_non_security
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rejected_patches_shrink):
            query['RejectedPatches'] = request.rejected_patches_shrink
        if not DaraCore.is_null(request.rejected_patches_action):
            query['RejectedPatchesAction'] = request.rejected_patches_action
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sources_shrink):
            query['Sources'] = request.sources_shrink
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePatchBaseline',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePatchBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_patch_baseline(
        self,
        request: main_models.UpdatePatchBaselineRequest,
    ) -> main_models.UpdatePatchBaselineResponse:
        runtime = RuntimeOptions()
        return self.update_patch_baseline_with_options(request, runtime)

    async def update_patch_baseline_async(
        self,
        request: main_models.UpdatePatchBaselineRequest,
    ) -> main_models.UpdatePatchBaselineResponse:
        runtime = RuntimeOptions()
        return await self.update_patch_baseline_with_options_async(request, runtime)

    def update_secret_parameter_with_options(
        self,
        tmp_req: main_models.UpdateSecretParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecretParameterResponse:
        tmp_req.validate()
        request = main_models.UpdateSecretParameterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecretParameter',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecretParameterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_secret_parameter_with_options_async(
        self,
        tmp_req: main_models.UpdateSecretParameterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSecretParameterResponse:
        tmp_req.validate()
        request = main_models.UpdateSecretParameterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.value):
            query['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSecretParameter',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSecretParameterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_secret_parameter(
        self,
        request: main_models.UpdateSecretParameterRequest,
    ) -> main_models.UpdateSecretParameterResponse:
        runtime = RuntimeOptions()
        return self.update_secret_parameter_with_options(request, runtime)

    async def update_secret_parameter_async(
        self,
        request: main_models.UpdateSecretParameterRequest,
    ) -> main_models.UpdateSecretParameterResponse:
        runtime = RuntimeOptions()
        return await self.update_secret_parameter_with_options_async(request, runtime)

    def update_state_configuration_with_options(
        self,
        tmp_req: main_models.UpdateStateConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStateConfigurationResponse:
        tmp_req.validate()
        request = main_models.UpdateStateConfigurationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.configure_mode):
            query['ConfigureMode'] = request.configure_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.schedule_expression):
            query['ScheduleExpression'] = request.schedule_expression
        if not DaraCore.is_null(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not DaraCore.is_null(request.state_configuration_id):
            query['StateConfigurationId'] = request.state_configuration_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.targets):
            query['Targets'] = request.targets
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStateConfiguration',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStateConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_state_configuration_with_options_async(
        self,
        tmp_req: main_models.UpdateStateConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStateConfigurationResponse:
        tmp_req.validate()
        request = main_models.UpdateStateConfigurationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.configure_mode):
            query['ConfigureMode'] = request.configure_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.schedule_expression):
            query['ScheduleExpression'] = request.schedule_expression
        if not DaraCore.is_null(request.schedule_type):
            query['ScheduleType'] = request.schedule_type
        if not DaraCore.is_null(request.state_configuration_id):
            query['StateConfigurationId'] = request.state_configuration_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.targets):
            query['Targets'] = request.targets
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStateConfiguration',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStateConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_state_configuration(
        self,
        request: main_models.UpdateStateConfigurationRequest,
    ) -> main_models.UpdateStateConfigurationResponse:
        runtime = RuntimeOptions()
        return self.update_state_configuration_with_options(request, runtime)

    async def update_state_configuration_async(
        self,
        request: main_models.UpdateStateConfigurationRequest,
    ) -> main_models.UpdateStateConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.update_state_configuration_with_options_async(request, runtime)

    def update_template_with_options(
        self,
        tmp_req: main_models.UpdateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateResponse:
        tmp_req.validate()
        request = main_models.UpdateTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplate',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_with_options_async(
        self,
        tmp_req: main_models.UpdateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateResponse:
        tmp_req.validate()
        request = main_models.UpdateTemplateShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplate',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template(
        self,
        request: main_models.UpdateTemplateRequest,
    ) -> main_models.UpdateTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    async def update_template_async(
        self,
        request: main_models.UpdateTemplateRequest,
    ) -> main_models.UpdateTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_template_with_options_async(request, runtime)

    def validate_template_content_with_options(
        self,
        request: main_models.ValidateTemplateContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateTemplateContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateTemplateContent',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateTemplateContentResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_template_content_with_options_async(
        self,
        request: main_models.ValidateTemplateContentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateTemplateContentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateTemplateContent',
            version = '2019-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateTemplateContentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_template_content(
        self,
        request: main_models.ValidateTemplateContentRequest,
    ) -> main_models.ValidateTemplateContentResponse:
        runtime = RuntimeOptions()
        return self.validate_template_content_with_options(request, runtime)

    async def validate_template_content_async(
        self,
        request: main_models.ValidateTemplateContentRequest,
    ) -> main_models.ValidateTemplateContentResponse:
        runtime = RuntimeOptions()
        return await self.validate_template_content_with_options_async(request, runtime)
