# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_iacservice20210806 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

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
        self._endpoint = self.get_endpoint('iacservice', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_shared_accounts_with_options(
        self,
        request: main_models.AddSharedAccountsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddSharedAccountsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_ids):
            body['accountIds'] = request.account_ids
        if not DaraCore.is_null(request.resource_id):
            body['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddSharedAccounts',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/sharedAccounts',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSharedAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_shared_accounts_with_options_async(
        self,
        request: main_models.AddSharedAccountsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddSharedAccountsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_ids):
            body['accountIds'] = request.account_ids
        if not DaraCore.is_null(request.resource_id):
            body['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AddSharedAccounts',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/sharedAccounts',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddSharedAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_shared_accounts(
        self,
        request: main_models.AddSharedAccountsRequest,
    ) -> main_models.AddSharedAccountsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_shared_accounts_with_options(request, headers, runtime)

    async def add_shared_accounts_async(
        self,
        request: main_models.AddSharedAccountsRequest,
    ) -> main_models.AddSharedAccountsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_shared_accounts_with_options_async(request, headers, runtime)

    def associate_group_with_options(
        self,
        group_id: str,
        request: main_models.AssociateGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AssociateGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.resource_ids):
            body['resourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociateGroup',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/group/{DaraURL.percent_encode(group_id)}/associate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_group_with_options_async(
        self,
        group_id: str,
        request: main_models.AssociateGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AssociateGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.resource_ids):
            body['resourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociateGroup',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/group/{DaraURL.percent_encode(group_id)}/associate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_group(
        self,
        group_id: str,
        request: main_models.AssociateGroupRequest,
    ) -> main_models.AssociateGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.associate_group_with_options(group_id, request, headers, runtime)

    async def associate_group_async(
        self,
        group_id: str,
        request: main_models.AssociateGroupRequest,
    ) -> main_models.AssociateGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.associate_group_with_options_async(group_id, request, headers, runtime)

    def cancel_resource_export_task_with_options(
        self,
        export_task_id: str,
        request: main_models.CancelResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelResourceExportTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelResourceExportTask',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/exportTasks/cancel/{DaraURL.percent_encode(export_task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_resource_export_task_with_options_async(
        self,
        export_task_id: str,
        request: main_models.CancelResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CancelResourceExportTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelResourceExportTask',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/exportTasks/cancel/{DaraURL.percent_encode(export_task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelResourceExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_resource_export_task(
        self,
        export_task_id: str,
        request: main_models.CancelResourceExportTaskRequest,
    ) -> main_models.CancelResourceExportTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.cancel_resource_export_task_with_options(export_task_id, request, headers, runtime)

    async def cancel_resource_export_task_async(
        self,
        export_task_id: str,
        request: main_models.CancelResourceExportTaskRequest,
    ) -> main_models.CancelResourceExportTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.cancel_resource_export_task_with_options_async(export_task_id, request, headers, runtime)

    def create_group_with_options(
        self,
        request: main_models.CreateGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not DaraCore.is_null(request.auto_trigger):
            body['autoTrigger'] = request.auto_trigger
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.forced_setting):
            body['forcedSetting'] = request.forced_setting
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.notify_config):
            body['notifyConfig'] = request.notify_config
        if not DaraCore.is_null(request.notify_operation_types):
            body['notifyOperationTypes'] = request.notify_operation_types
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.ram_role):
            body['ramRole'] = request.ram_role
        if not DaraCore.is_null(request.report_export_field):
            body['reportExportField'] = request.report_export_field
        if not DaraCore.is_null(request.report_export_path):
            body['reportExportPath'] = request.report_export_path
        if not DaraCore.is_null(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not DaraCore.is_null(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        if not DaraCore.is_null(request.trigger_resource_type):
            body['triggerResourceType'] = request.trigger_resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/group',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: main_models.CreateGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not DaraCore.is_null(request.auto_trigger):
            body['autoTrigger'] = request.auto_trigger
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.forced_setting):
            body['forcedSetting'] = request.forced_setting
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.notify_config):
            body['notifyConfig'] = request.notify_config
        if not DaraCore.is_null(request.notify_operation_types):
            body['notifyOperationTypes'] = request.notify_operation_types
        if not DaraCore.is_null(request.project_id):
            body['projectId'] = request.project_id
        if not DaraCore.is_null(request.ram_role):
            body['ramRole'] = request.ram_role
        if not DaraCore.is_null(request.report_export_field):
            body['reportExportField'] = request.report_export_field
        if not DaraCore.is_null(request.report_export_path):
            body['reportExportPath'] = request.report_export_path
        if not DaraCore.is_null(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not DaraCore.is_null(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        if not DaraCore.is_null(request.trigger_resource_type):
            body['triggerResourceType'] = request.trigger_resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroup',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/group',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group(
        self,
        request: main_models.CreateGroupRequest,
    ) -> main_models.CreateGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_group_with_options(request, headers, runtime)

    async def create_group_async(
        self,
        request: main_models.CreateGroupRequest,
    ) -> main_models.CreateGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_group_with_options_async(request, headers, runtime)

    def create_job_with_options(
        self,
        task_id: str,
        request: main_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.sub_command):
            body['subCommand'] = request.sub_command
        if not DaraCore.is_null(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateJob',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}/jobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        task_id: str,
        request: main_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.sub_command):
            body['subCommand'] = request.sub_command
        if not DaraCore.is_null(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateJob',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}/jobs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job(
        self,
        task_id: str,
        request: main_models.CreateJobRequest,
    ) -> main_models.CreateJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_job_with_options(task_id, request, headers, runtime)

    async def create_job_async(
        self,
        task_id: str,
        request: main_models.CreateJobRequest,
    ) -> main_models.CreateJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_job_with_options_async(task_id, request, headers, runtime)

    def create_module_with_options(
        self,
        request: main_models.CreateModuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.group_info):
            body['groupInfo'] = request.group_info
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        if not DaraCore.is_null(request.source_path):
            body['sourcePath'] = request.source_path
        if not DaraCore.is_null(request.state_path):
            body['statePath'] = request.state_path
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.version_strategy):
            body['versionStrategy'] = request.version_strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/modules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_module_with_options_async(
        self,
        request: main_models.CreateModuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.group_info):
            body['groupInfo'] = request.group_info
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        if not DaraCore.is_null(request.source_path):
            body['sourcePath'] = request.source_path
        if not DaraCore.is_null(request.state_path):
            body['statePath'] = request.state_path
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.version_strategy):
            body['versionStrategy'] = request.version_strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/modules',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_module(
        self,
        request: main_models.CreateModuleRequest,
    ) -> main_models.CreateModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_module_with_options(request, headers, runtime)

    async def create_module_async(
        self,
        request: main_models.CreateModuleRequest,
    ) -> main_models.CreateModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_module_with_options_async(request, headers, runtime)

    def create_module_version_with_options(
        self,
        module_id: str,
        request: main_models.CreateModuleVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModuleVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModuleVersion',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/modules/{DaraURL.percent_encode(module_id)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_module_version_with_options_async(
        self,
        module_id: str,
        request: main_models.CreateModuleVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateModuleVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateModuleVersion',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/modules/{DaraURL.percent_encode(module_id)}/versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateModuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_module_version(
        self,
        module_id: str,
        request: main_models.CreateModuleVersionRequest,
    ) -> main_models.CreateModuleVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_module_version_with_options(module_id, request, headers, runtime)

    async def create_module_version_async(
        self,
        module_id: str,
        request: main_models.CreateModuleVersionRequest,
    ) -> main_models.CreateModuleVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_module_version_with_options_async(module_id, request, headers, runtime)

    def create_project_with_options(
        self,
        request: main_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProject',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/project',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: main_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProject',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/project',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: main_models.CreateProjectRequest,
    ) -> main_models.CreateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    async def create_project_async(
        self,
        request: main_models.CreateProjectRequest,
    ) -> main_models.CreateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(request, headers, runtime)

    def create_registry_module_with_options(
        self,
        request: main_models.CreateRegistryModuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRegistryModuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.acl):
            body['acl'] = request.acl
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.module_name):
            body['moduleName'] = request.module_name
        if not DaraCore.is_null(request.namespace_name):
            body['namespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.provider):
            body['provider'] = request.provider
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRegistryModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModule',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRegistryModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_registry_module_with_options_async(
        self,
        request: main_models.CreateRegistryModuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRegistryModuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.acl):
            body['acl'] = request.acl
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.module_name):
            body['moduleName'] = request.module_name
        if not DaraCore.is_null(request.namespace_name):
            body['namespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.provider):
            body['provider'] = request.provider
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRegistryModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModule',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRegistryModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_registry_module(
        self,
        request: main_models.CreateRegistryModuleRequest,
    ) -> main_models.CreateRegistryModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_registry_module_with_options(request, headers, runtime)

    async def create_registry_module_async(
        self,
        request: main_models.CreateRegistryModuleRequest,
    ) -> main_models.CreateRegistryModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_registry_module_with_options_async(request, headers, runtime)

    def create_registry_namespace_with_options(
        self,
        request: main_models.CreateRegistryNamespaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRegistryNamespaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.acl):
            body['acl'] = request.acl
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.maintainer):
            body['maintainer'] = request.maintainer
        if not DaraCore.is_null(request.namespace_name):
            body['namespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRegistryNamespace',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryNamespace',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRegistryNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_registry_namespace_with_options_async(
        self,
        request: main_models.CreateRegistryNamespaceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRegistryNamespaceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.acl):
            body['acl'] = request.acl
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.maintainer):
            body['maintainer'] = request.maintainer
        if not DaraCore.is_null(request.namespace_name):
            body['namespaceName'] = request.namespace_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRegistryNamespace',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryNamespace',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRegistryNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_registry_namespace(
        self,
        request: main_models.CreateRegistryNamespaceRequest,
    ) -> main_models.CreateRegistryNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_registry_namespace_with_options(request, headers, runtime)

    async def create_registry_namespace_async(
        self,
        request: main_models.CreateRegistryNamespaceRequest,
    ) -> main_models.CreateRegistryNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_registry_namespace_with_options_async(request, headers, runtime)

    def create_resource_export_task_with_options(
        self,
        request: main_models.CreateResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceExportTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.export_to_module):
            body['exportToModule'] = request.export_to_module
        if not DaraCore.is_null(request.include_rules):
            body['includeRules'] = request.include_rules
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.ram_role):
            body['ramRole'] = request.ram_role
        if not DaraCore.is_null(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not DaraCore.is_null(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not DaraCore.is_null(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceExportTask',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/exportTasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_export_task_with_options_async(
        self,
        request: main_models.CreateResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceExportTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.export_to_module):
            body['exportToModule'] = request.export_to_module
        if not DaraCore.is_null(request.include_rules):
            body['includeRules'] = request.include_rules
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.ram_role):
            body['ramRole'] = request.ram_role
        if not DaraCore.is_null(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not DaraCore.is_null(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not DaraCore.is_null(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResourceExportTask',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/exportTasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_export_task(
        self,
        request: main_models.CreateResourceExportTaskRequest,
    ) -> main_models.CreateResourceExportTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_resource_export_task_with_options(request, headers, runtime)

    async def create_resource_export_task_async(
        self,
        request: main_models.CreateResourceExportTaskRequest,
    ) -> main_models.CreateResourceExportTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_resource_export_task_with_options_async(request, headers, runtime)

    def create_task_with_options(
        self,
        request: main_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not DaraCore.is_null(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.group_info):
            body['groupInfo'] = request.group_info
        if not DaraCore.is_null(request.init_module_state):
            body['initModuleState'] = request.init_module_state
        if not DaraCore.is_null(request.module_id):
            body['moduleId'] = request.module_id
        if not DaraCore.is_null(request.module_version):
            body['moduleVersion'] = request.module_version
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.protection_strategy):
            body['protectionStrategy'] = request.protection_strategy
        if not DaraCore.is_null(request.ram_role):
            body['ramRole'] = request.ram_role
        if not DaraCore.is_null(request.skip_property_validation):
            body['skipPropertyValidation'] = request.skip_property_validation
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.task_backend):
            body['taskBackend'] = request.task_backend
        if not DaraCore.is_null(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not DaraCore.is_null(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTask',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_with_options_async(
        self,
        request: main_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not DaraCore.is_null(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.group_info):
            body['groupInfo'] = request.group_info
        if not DaraCore.is_null(request.init_module_state):
            body['initModuleState'] = request.init_module_state
        if not DaraCore.is_null(request.module_id):
            body['moduleId'] = request.module_id
        if not DaraCore.is_null(request.module_version):
            body['moduleVersion'] = request.module_version
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.protection_strategy):
            body['protectionStrategy'] = request.protection_strategy
        if not DaraCore.is_null(request.ram_role):
            body['ramRole'] = request.ram_role
        if not DaraCore.is_null(request.skip_property_validation):
            body['skipPropertyValidation'] = request.skip_property_validation
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.task_backend):
            body['taskBackend'] = request.task_backend
        if not DaraCore.is_null(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not DaraCore.is_null(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTask',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task(
        self,
        request: main_models.CreateTaskRequest,
    ) -> main_models.CreateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_task_with_options(request, headers, runtime)

    async def create_task_async(
        self,
        request: main_models.CreateTaskRequest,
    ) -> main_models.CreateTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_task_with_options_async(request, headers, runtime)

    def delete_group_with_options(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroup',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/group/{DaraURL.percent_encode(group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroup',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/group/{DaraURL.percent_encode(group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group(
        self,
        group_id: str,
    ) -> main_models.DeleteGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_group_with_options(group_id, headers, runtime)

    async def delete_group_async(
        self,
        group_id: str,
    ) -> main_models.DeleteGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_group_with_options_async(group_id, headers, runtime)

    def delete_module_with_options(
        self,
        module_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/modules/{DaraURL.percent_encode(module_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_module_with_options_async(
        self,
        module_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteModuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/modules/{DaraURL.percent_encode(module_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_module(
        self,
        module_id: str,
    ) -> main_models.DeleteModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_module_with_options(module_id, headers, runtime)

    async def delete_module_async(
        self,
        module_id: str,
    ) -> main_models.DeleteModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_module_with_options_async(module_id, headers, runtime)

    def delete_project_with_options(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProjectResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteProject',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/project/{DaraURL.percent_encode(project_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProjectResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteProject',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/project/{DaraURL.percent_encode(project_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        project_id: str,
    ) -> main_models.DeleteProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(project_id, headers, runtime)

    async def delete_project_async(
        self,
        project_id: str,
    ) -> main_models.DeleteProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_project_with_options_async(project_id, headers, runtime)

    def delete_registry_module_with_options(
        self,
        namespace_name: str,
        module_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRegistryModuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteRegistryModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModule/{DaraURL.percent_encode(namespace_name)}/{DaraURL.percent_encode(module_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRegistryModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_registry_module_with_options_async(
        self,
        namespace_name: str,
        module_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRegistryModuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteRegistryModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModule/{DaraURL.percent_encode(namespace_name)}/{DaraURL.percent_encode(module_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRegistryModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_registry_module(
        self,
        namespace_name: str,
        module_name: str,
    ) -> main_models.DeleteRegistryModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_registry_module_with_options(namespace_name, module_name, headers, runtime)

    async def delete_registry_module_async(
        self,
        namespace_name: str,
        module_name: str,
    ) -> main_models.DeleteRegistryModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_registry_module_with_options_async(namespace_name, module_name, headers, runtime)

    def delete_registry_module_version_with_options(
        self,
        namespace_name: str,
        module_name: str,
        version: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRegistryModuleVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteRegistryModuleVersion',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModuleVersion/{DaraURL.percent_encode(namespace_name)}/{DaraURL.percent_encode(module_name)}/{DaraURL.percent_encode(version)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRegistryModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_registry_module_version_with_options_async(
        self,
        namespace_name: str,
        module_name: str,
        version: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRegistryModuleVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteRegistryModuleVersion',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModuleVersion/{DaraURL.percent_encode(namespace_name)}/{DaraURL.percent_encode(module_name)}/{DaraURL.percent_encode(version)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRegistryModuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_registry_module_version(
        self,
        namespace_name: str,
        module_name: str,
        version: str,
    ) -> main_models.DeleteRegistryModuleVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_registry_module_version_with_options(namespace_name, module_name, version, headers, runtime)

    async def delete_registry_module_version_async(
        self,
        namespace_name: str,
        module_name: str,
        version: str,
    ) -> main_models.DeleteRegistryModuleVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_registry_module_version_with_options_async(namespace_name, module_name, version, headers, runtime)

    def delete_registry_namespace_with_options(
        self,
        namespace_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRegistryNamespaceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteRegistryNamespace',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryNamespace/{DaraURL.percent_encode(namespace_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRegistryNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_registry_namespace_with_options_async(
        self,
        namespace_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRegistryNamespaceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteRegistryNamespace',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryNamespace/{DaraURL.percent_encode(namespace_name)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRegistryNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_registry_namespace(
        self,
        namespace_name: str,
    ) -> main_models.DeleteRegistryNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_registry_namespace_with_options(namespace_name, headers, runtime)

    async def delete_registry_namespace_async(
        self,
        namespace_name: str,
    ) -> main_models.DeleteRegistryNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_registry_namespace_with_options_async(namespace_name, headers, runtime)

    def delete_resource_export_task_with_options(
        self,
        export_task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceExportTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceExportTask',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/exportTasks/{DaraURL.percent_encode(export_task_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_export_task_with_options_async(
        self,
        export_task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceExportTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteResourceExportTask',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/exportTasks/{DaraURL.percent_encode(export_task_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_export_task(
        self,
        export_task_id: str,
    ) -> main_models.DeleteResourceExportTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_resource_export_task_with_options(export_task_id, headers, runtime)

    async def delete_resource_export_task_async(
        self,
        export_task_id: str,
    ) -> main_models.DeleteResourceExportTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_resource_export_task_with_options_async(export_task_id, headers, runtime)

    def delete_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTask',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteTask',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_task(
        self,
        task_id: str,
    ) -> main_models.DeleteTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_task_with_options(task_id, headers, runtime)

    async def delete_task_async(
        self,
        task_id: str,
    ) -> main_models.DeleteTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_task_with_options_async(task_id, headers, runtime)

    def dissociate_group_with_options(
        self,
        project_id: str,
        group_id: str,
        request: main_models.DissociateGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DissociateGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.resource_ids):
            body['resourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DissociateGroup',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/group/{DaraURL.percent_encode(group_id)}/dissociate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DissociateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_group_with_options_async(
        self,
        project_id: str,
        group_id: str,
        request: main_models.DissociateGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DissociateGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.resource_ids):
            body['resourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DissociateGroup',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/group/{DaraURL.percent_encode(group_id)}/dissociate',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DissociateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_group(
        self,
        project_id: str,
        group_id: str,
        request: main_models.DissociateGroupRequest,
    ) -> main_models.DissociateGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.dissociate_group_with_options(project_id, group_id, request, headers, runtime)

    async def dissociate_group_async(
        self,
        project_id: str,
        group_id: str,
        request: main_models.DissociateGroupRequest,
    ) -> main_models.DissociateGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.dissociate_group_with_options_async(project_id, group_id, request, headers, runtime)

    def execute_registry_module_with_options(
        self,
        namespace_name: str,
        module_name: str,
        request: main_models.ExecuteRegistryModuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteRegistryModuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteRegistryModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModule/{DaraURL.percent_encode(namespace_name)}/{DaraURL.percent_encode(module_name)}/execution',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteRegistryModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_registry_module_with_options_async(
        self,
        namespace_name: str,
        module_name: str,
        request: main_models.ExecuteRegistryModuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteRegistryModuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteRegistryModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModule/{DaraURL.percent_encode(namespace_name)}/{DaraURL.percent_encode(module_name)}/execution',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteRegistryModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_registry_module(
        self,
        namespace_name: str,
        module_name: str,
        request: main_models.ExecuteRegistryModuleRequest,
    ) -> main_models.ExecuteRegistryModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_registry_module_with_options(namespace_name, module_name, request, headers, runtime)

    async def execute_registry_module_async(
        self,
        namespace_name: str,
        module_name: str,
        request: main_models.ExecuteRegistryModuleRequest,
    ) -> main_models.ExecuteRegistryModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_registry_module_with_options_async(namespace_name, module_name, request, headers, runtime)

    def execute_resource_export_task_with_options(
        self,
        export_task_id: str,
        request: main_models.ExecuteResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteResourceExportTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteResourceExportTask',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/exportTasks/execute/{DaraURL.percent_encode(export_task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_resource_export_task_with_options_async(
        self,
        export_task_id: str,
        request: main_models.ExecuteResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteResourceExportTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteResourceExportTask',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/exportTasks/execute/{DaraURL.percent_encode(export_task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteResourceExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_resource_export_task(
        self,
        export_task_id: str,
        request: main_models.ExecuteResourceExportTaskRequest,
    ) -> main_models.ExecuteResourceExportTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_resource_export_task_with_options(export_task_id, request, headers, runtime)

    async def execute_resource_export_task_async(
        self,
        export_task_id: str,
        request: main_models.ExecuteResourceExportTaskRequest,
    ) -> main_models.ExecuteResourceExportTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_resource_export_task_with_options_async(export_task_id, request, headers, runtime)

    def execute_terraform_apply_with_options(
        self,
        request: main_models.ExecuteTerraformApplyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTerraformApplyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.state_id):
            body['stateId'] = request.state_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTerraformApply',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/terraform/execution/apply',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTerraformApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_terraform_apply_with_options_async(
        self,
        request: main_models.ExecuteTerraformApplyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTerraformApplyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.state_id):
            body['stateId'] = request.state_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTerraformApply',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/terraform/execution/apply',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTerraformApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_terraform_apply(
        self,
        request: main_models.ExecuteTerraformApplyRequest,
    ) -> main_models.ExecuteTerraformApplyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_terraform_apply_with_options(request, headers, runtime)

    async def execute_terraform_apply_async(
        self,
        request: main_models.ExecuteTerraformApplyRequest,
    ) -> main_models.ExecuteTerraformApplyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_terraform_apply_with_options_async(request, headers, runtime)

    def execute_terraform_destroy_with_options(
        self,
        request: main_models.ExecuteTerraformDestroyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTerraformDestroyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.state_id):
            body['stateId'] = request.state_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTerraformDestroy',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/terraform/execution/destroy',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTerraformDestroyResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_terraform_destroy_with_options_async(
        self,
        request: main_models.ExecuteTerraformDestroyRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTerraformDestroyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.state_id):
            body['stateId'] = request.state_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTerraformDestroy',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/terraform/execution/destroy',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTerraformDestroyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_terraform_destroy(
        self,
        request: main_models.ExecuteTerraformDestroyRequest,
    ) -> main_models.ExecuteTerraformDestroyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_terraform_destroy_with_options(request, headers, runtime)

    async def execute_terraform_destroy_async(
        self,
        request: main_models.ExecuteTerraformDestroyRequest,
    ) -> main_models.ExecuteTerraformDestroyResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_terraform_destroy_with_options_async(request, headers, runtime)

    def execute_terraform_plan_with_options(
        self,
        request: main_models.ExecuteTerraformPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTerraformPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.state_id):
            body['stateId'] = request.state_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTerraformPlan',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/terraform/execution/plan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTerraformPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_terraform_plan_with_options_async(
        self,
        request: main_models.ExecuteTerraformPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteTerraformPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.state_id):
            body['stateId'] = request.state_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteTerraformPlan',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/terraform/execution/plan',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteTerraformPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_terraform_plan(
        self,
        request: main_models.ExecuteTerraformPlanRequest,
    ) -> main_models.ExecuteTerraformPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.execute_terraform_plan_with_options(request, headers, runtime)

    async def execute_terraform_plan_async(
        self,
        request: main_models.ExecuteTerraformPlanRequest,
    ) -> main_models.ExecuteTerraformPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.execute_terraform_plan_with_options_async(request, headers, runtime)

    def generate_module_with_options(
        self,
        request: main_models.GenerateModuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateModuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.generate_source):
            body['generateSource'] = request.generate_source
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            body['regionId'] = request.region_id
        if not DaraCore.is_null(request.syntax):
            body['syntax'] = request.syntax
        if not DaraCore.is_null(request.template):
            body['template'] = request.template
        if not DaraCore.is_null(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not DaraCore.is_null(request.terraform_resource_type):
            body['terraformResourceType'] = request.terraform_resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/explorer/generate/module',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateModuleResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def generate_module_with_options_async(
        self,
        request: main_models.GenerateModuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GenerateModuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.generate_source):
            body['generateSource'] = request.generate_source
        if not DaraCore.is_null(request.parameters):
            body['parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            body['regionId'] = request.region_id
        if not DaraCore.is_null(request.syntax):
            body['syntax'] = request.syntax
        if not DaraCore.is_null(request.template):
            body['template'] = request.template
        if not DaraCore.is_null(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not DaraCore.is_null(request.terraform_resource_type):
            body['terraformResourceType'] = request.terraform_resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GenerateModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/explorer/generate/module',
            method = 'POST',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateModuleResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def generate_module(
        self,
        request: main_models.GenerateModuleRequest,
    ) -> main_models.GenerateModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.generate_module_with_options(request, headers, runtime)

    async def generate_module_async(
        self,
        request: main_models.GenerateModuleRequest,
    ) -> main_models.GenerateModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.generate_module_with_options_async(request, headers, runtime)

    def get_execute_state_with_options(
        self,
        state_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExecuteStateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetExecuteState',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/terraform/execution/{DaraURL.percent_encode(state_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExecuteStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_execute_state_with_options_async(
        self,
        state_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetExecuteStateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetExecuteState',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/terraform/execution/{DaraURL.percent_encode(state_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExecuteStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_execute_state(
        self,
        state_id: str,
    ) -> main_models.GetExecuteStateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_execute_state_with_options(state_id, headers, runtime)

    async def get_execute_state_async(
        self,
        state_id: str,
    ) -> main_models.GetExecuteStateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_execute_state_with_options_async(state_id, headers, runtime)

    def get_group_with_options(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetGroup',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/group/{DaraURL.percent_encode(group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_with_options_async(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetGroup',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/group/{DaraURL.percent_encode(group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group(
        self,
        group_id: str,
    ) -> main_models.GetGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_group_with_options(group_id, headers, runtime)

    async def get_group_async(
        self,
        group_id: str,
    ) -> main_models.GetGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_group_with_options_async(group_id, headers, runtime)

    def get_job_with_options(
        self,
        task_id: str,
        job_id: str,
        request: main_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJob',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        task_id: str,
        job_id: str,
        request: main_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetJob',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}/jobs/{DaraURL.percent_encode(job_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job(
        self,
        task_id: str,
        job_id: str,
        request: main_models.GetJobRequest,
    ) -> main_models.GetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_job_with_options(task_id, job_id, request, headers, runtime)

    async def get_job_async(
        self,
        task_id: str,
        job_id: str,
        request: main_models.GetJobRequest,
    ) -> main_models.GetJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_job_with_options_async(task_id, job_id, request, headers, runtime)

    def get_module_with_options(
        self,
        module_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/modules/{DaraURL.percent_encode(module_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_module_with_options_async(
        self,
        module_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/modules/{DaraURL.percent_encode(module_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_module(
        self,
        module_id: str,
    ) -> main_models.GetModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_module_with_options(module_id, headers, runtime)

    async def get_module_async(
        self,
        module_id: str,
    ) -> main_models.GetModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_module_with_options_async(module_id, headers, runtime)

    def get_module_version_with_options(
        self,
        module_id: str,
        module_version: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModuleVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModuleVersion',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/modules/{DaraURL.percent_encode(module_id)}/versions/{DaraURL.percent_encode(module_version)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_module_version_with_options_async(
        self,
        module_id: str,
        module_version: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetModuleVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetModuleVersion',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/modules/{DaraURL.percent_encode(module_id)}/versions/{DaraURL.percent_encode(module_version)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetModuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_module_version(
        self,
        module_id: str,
        module_version: str,
    ) -> main_models.GetModuleVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_module_version_with_options(module_id, module_version, headers, runtime)

    async def get_module_version_async(
        self,
        module_id: str,
        module_version: str,
    ) -> main_models.GetModuleVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_module_version_with_options_async(module_id, module_version, headers, runtime)

    def get_project_with_options(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetProject',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/project/{DaraURL.percent_encode(project_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProjectResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetProject',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/project/{DaraURL.percent_encode(project_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        project_id: str,
    ) -> main_models.GetProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_project_with_options(project_id, headers, runtime)

    async def get_project_async(
        self,
        project_id: str,
    ) -> main_models.GetProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_project_with_options_async(project_id, headers, runtime)

    def get_registry_module_with_options(
        self,
        namespace_name: str,
        module_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRegistryModuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRegistryModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModule/{DaraURL.percent_encode(namespace_name)}/{DaraURL.percent_encode(module_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegistryModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_registry_module_with_options_async(
        self,
        namespace_name: str,
        module_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRegistryModuleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRegistryModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModule/{DaraURL.percent_encode(namespace_name)}/{DaraURL.percent_encode(module_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegistryModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_registry_module(
        self,
        namespace_name: str,
        module_name: str,
    ) -> main_models.GetRegistryModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_registry_module_with_options(namespace_name, module_name, headers, runtime)

    async def get_registry_module_async(
        self,
        namespace_name: str,
        module_name: str,
    ) -> main_models.GetRegistryModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_registry_module_with_options_async(namespace_name, module_name, headers, runtime)

    def get_registry_module_version_with_options(
        self,
        namespace_name: str,
        module_name: str,
        version: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRegistryModuleVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRegistryModuleVersion',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModuleVersion/{DaraURL.percent_encode(namespace_name)}/{DaraURL.percent_encode(module_name)}/{DaraURL.percent_encode(version)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegistryModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_registry_module_version_with_options_async(
        self,
        namespace_name: str,
        module_name: str,
        version: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRegistryModuleVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRegistryModuleVersion',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModuleVersion/{DaraURL.percent_encode(namespace_name)}/{DaraURL.percent_encode(module_name)}/{DaraURL.percent_encode(version)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegistryModuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_registry_module_version(
        self,
        namespace_name: str,
        module_name: str,
        version: str,
    ) -> main_models.GetRegistryModuleVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_registry_module_version_with_options(namespace_name, module_name, version, headers, runtime)

    async def get_registry_module_version_async(
        self,
        namespace_name: str,
        module_name: str,
        version: str,
    ) -> main_models.GetRegistryModuleVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_registry_module_version_with_options_async(namespace_name, module_name, version, headers, runtime)

    def get_registry_namespace_with_options(
        self,
        namespace_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRegistryNamespaceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRegistryNamespace',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryNamespace/{DaraURL.percent_encode(namespace_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegistryNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_registry_namespace_with_options_async(
        self,
        namespace_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRegistryNamespaceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRegistryNamespace',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryNamespace/{DaraURL.percent_encode(namespace_name)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegistryNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_registry_namespace(
        self,
        namespace_name: str,
    ) -> main_models.GetRegistryNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_registry_namespace_with_options(namespace_name, headers, runtime)

    async def get_registry_namespace_async(
        self,
        namespace_name: str,
    ) -> main_models.GetRegistryNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_registry_namespace_with_options_async(namespace_name, headers, runtime)

    def get_resource_export_task_with_options(
        self,
        export_task_id: str,
        request: main_models.GetResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.export_version):
            query['exportVersion'] = request.export_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceExportTask',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/exportTasks/{DaraURL.percent_encode(export_task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_export_task_with_options_async(
        self,
        export_task_id: str,
        request: main_models.GetResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceExportTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.export_version):
            query['exportVersion'] = request.export_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceExportTask',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/exportTasks/{DaraURL.percent_encode(export_task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_export_task(
        self,
        export_task_id: str,
        request: main_models.GetResourceExportTaskRequest,
    ) -> main_models.GetResourceExportTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resource_export_task_with_options(export_task_id, request, headers, runtime)

    async def get_resource_export_task_async(
        self,
        export_task_id: str,
        request: main_models.GetResourceExportTaskRequest,
    ) -> main_models.GetResourceExportTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resource_export_task_with_options_async(export_task_id, request, headers, runtime)

    def get_resource_type_with_options(
        self,
        resource_type: str,
        request: main_models.GetResourceTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.filter_read_only):
            query['filterReadOnly'] = request.filter_read_only
        if not DaraCore.is_null(request.terraform_provider_version):
            query['terraformProviderVersion'] = request.terraform_provider_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceType',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/resourceType/{DaraURL.percent_encode(resource_type)}',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceTypeResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_resource_type_with_options_async(
        self,
        resource_type: str,
        request: main_models.GetResourceTypeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.filter_read_only):
            query['filterReadOnly'] = request.filter_read_only
        if not DaraCore.is_null(request.terraform_provider_version):
            query['terraformProviderVersion'] = request.terraform_provider_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceType',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/resourceType/{DaraURL.percent_encode(resource_type)}',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceTypeResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_resource_type(
        self,
        resource_type: str,
        request: main_models.GetResourceTypeRequest,
    ) -> main_models.GetResourceTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resource_type_with_options(resource_type, request, headers, runtime)

    async def get_resource_type_async(
        self,
        resource_type: str,
        request: main_models.GetResourceTypeRequest,
    ) -> main_models.GetResourceTypeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resource_type_with_options_async(resource_type, request, headers, runtime)

    def get_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTask',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTask',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        task_id: str,
    ) -> main_models.GetTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_task_with_options(task_id, headers, runtime)

    async def get_task_async(
        self,
        task_id: str,
    ) -> main_models.GetTaskResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_task_with_options_async(task_id, headers, runtime)

    def list_explorer_registry_module_examples_with_options(
        self,
        request: main_models.ListExplorerRegistryModuleExamplesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExplorerRegistryModuleExamplesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.example_name):
            query['exampleName'] = request.example_name
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.module_name):
            query['moduleName'] = request.module_name
        if not DaraCore.is_null(request.module_version):
            query['moduleVersion'] = request.module_version
        if not DaraCore.is_null(request.namespace_name):
            query['namespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExplorerRegistryModuleExamples',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/explorerRegistryModule/example',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExplorerRegistryModuleExamplesResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_explorer_registry_module_examples_with_options_async(
        self,
        request: main_models.ListExplorerRegistryModuleExamplesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExplorerRegistryModuleExamplesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.example_name):
            query['exampleName'] = request.example_name
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.module_name):
            query['moduleName'] = request.module_name
        if not DaraCore.is_null(request.module_version):
            query['moduleVersion'] = request.module_version
        if not DaraCore.is_null(request.namespace_name):
            query['namespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExplorerRegistryModuleExamples',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/explorerRegistryModule/example',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExplorerRegistryModuleExamplesResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_explorer_registry_module_examples(
        self,
        request: main_models.ListExplorerRegistryModuleExamplesRequest,
    ) -> main_models.ListExplorerRegistryModuleExamplesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_explorer_registry_module_examples_with_options(request, headers, runtime)

    async def list_explorer_registry_module_examples_async(
        self,
        request: main_models.ListExplorerRegistryModuleExamplesRequest,
    ) -> main_models.ListExplorerRegistryModuleExamplesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_explorer_registry_module_examples_with_options_async(request, headers, runtime)

    def list_explorer_registry_module_versions_with_options(
        self,
        request: main_models.ListExplorerRegistryModuleVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExplorerRegistryModuleVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.module_name):
            query['moduleName'] = request.module_name
        if not DaraCore.is_null(request.module_version):
            query['moduleVersion'] = request.module_version
        if not DaraCore.is_null(request.namespace_name):
            query['namespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExplorerRegistryModuleVersions',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/explorerRegistryModule/version',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExplorerRegistryModuleVersionsResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_explorer_registry_module_versions_with_options_async(
        self,
        request: main_models.ListExplorerRegistryModuleVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExplorerRegistryModuleVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.module_name):
            query['moduleName'] = request.module_name
        if not DaraCore.is_null(request.module_version):
            query['moduleVersion'] = request.module_version
        if not DaraCore.is_null(request.namespace_name):
            query['namespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExplorerRegistryModuleVersions',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/explorerRegistryModule/version',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExplorerRegistryModuleVersionsResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_explorer_registry_module_versions(
        self,
        request: main_models.ListExplorerRegistryModuleVersionsRequest,
    ) -> main_models.ListExplorerRegistryModuleVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_explorer_registry_module_versions_with_options(request, headers, runtime)

    async def list_explorer_registry_module_versions_async(
        self,
        request: main_models.ListExplorerRegistryModuleVersionsRequest,
    ) -> main_models.ListExplorerRegistryModuleVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_explorer_registry_module_versions_with_options_async(request, headers, runtime)

    def list_explorer_registry_modules_with_options(
        self,
        request: main_models.ListExplorerRegistryModulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExplorerRegistryModulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.module_name):
            query['moduleName'] = request.module_name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.sort):
            query['sort'] = request.sort
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExplorerRegistryModules',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/explorerRegistryModule',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExplorerRegistryModulesResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_explorer_registry_modules_with_options_async(
        self,
        request: main_models.ListExplorerRegistryModulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListExplorerRegistryModulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.module_name):
            query['moduleName'] = request.module_name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.sort):
            query['sort'] = request.sort
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExplorerRegistryModules',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/explorerRegistryModule',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExplorerRegistryModulesResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_explorer_registry_modules(
        self,
        request: main_models.ListExplorerRegistryModulesRequest,
    ) -> main_models.ListExplorerRegistryModulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_explorer_registry_modules_with_options(request, headers, runtime)

    async def list_explorer_registry_modules_async(
        self,
        request: main_models.ListExplorerRegistryModulesRequest,
    ) -> main_models.ListExplorerRegistryModulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_explorer_registry_modules_with_options_async(request, headers, runtime)

    def list_group_with_options(
        self,
        tmp_req: main_models.ListGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupResponse:
        tmp_req.validate()
        request = main_models.ListGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['projectId'] = request.project_id
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroup',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/group',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_group_with_options_async(
        self,
        tmp_req: main_models.ListGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGroupResponse:
        tmp_req.validate()
        request = main_models.ListGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['projectId'] = request.project_id
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGroup',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/group',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_group(
        self,
        request: main_models.ListGroupRequest,
    ) -> main_models.ListGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_group_with_options(request, headers, runtime)

    async def list_group_async(
        self,
        request: main_models.ListGroupRequest,
    ) -> main_models.ListGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_group_with_options_async(request, headers, runtime)

    def list_jobs_with_options(
        self,
        task_id: str,
        request: main_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_type):
            query['jobType'] = request.job_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}/jobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        task_id: str,
        request: main_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.job_type):
            query['jobType'] = request.job_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobs',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}/jobs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        task_id: str,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(task_id, request, headers, runtime)

    async def list_jobs_async(
        self,
        task_id: str,
        request: main_models.ListJobsRequest,
    ) -> main_models.ListJobsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_jobs_with_options_async(task_id, request, headers, runtime)

    def list_module_version_with_options(
        self,
        module_id: str,
        request: main_models.ListModuleVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModuleVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModuleVersion',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/modules/{DaraURL.percent_encode(module_id)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_module_version_with_options_async(
        self,
        module_id: str,
        request: main_models.ListModuleVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModuleVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModuleVersion',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/modules/{DaraURL.percent_encode(module_id)}/versions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_module_version(
        self,
        module_id: str,
        request: main_models.ListModuleVersionRequest,
    ) -> main_models.ListModuleVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_module_version_with_options(module_id, request, headers, runtime)

    async def list_module_version_async(
        self,
        module_id: str,
        request: main_models.ListModuleVersionRequest,
    ) -> main_models.ListModuleVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_module_version_with_options_async(module_id, request, headers, runtime)

    def list_modules_with_options(
        self,
        tmp_req: main_models.ListModulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModulesResponse:
        tmp_req.validate()
        request = main_models.ListModulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['groupId'] = request.group_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.module_name):
            query['moduleName'] = request.module_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['projectId'] = request.project_id
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModules',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/modules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_modules_with_options_async(
        self,
        tmp_req: main_models.ListModulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModulesResponse:
        tmp_req.validate()
        request = main_models.ListModulesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['groupId'] = request.group_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.module_name):
            query['moduleName'] = request.module_name
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['projectId'] = request.project_id
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModules',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/modules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_modules(
        self,
        request: main_models.ListModulesRequest,
    ) -> main_models.ListModulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_modules_with_options(request, headers, runtime)

    async def list_modules_async(
        self,
        request: main_models.ListModulesRequest,
    ) -> main_models.ListModulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_modules_with_options_async(request, headers, runtime)

    def list_products_with_options(
        self,
        request: main_models.ListProductsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.sort):
            query['sort'] = request.sort
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.support_terraformer):
            query['supportTerraformer'] = request.support_terraformer
        if not DaraCore.is_null(request.terraform_provider_version):
            query['terraformProviderVersion'] = request.terraform_provider_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProducts',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/products',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_products_with_options_async(
        self,
        request: main_models.ListProductsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.sort):
            query['sort'] = request.sort
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.support_terraformer):
            query['supportTerraformer'] = request.support_terraformer
        if not DaraCore.is_null(request.terraform_provider_version):
            query['terraformProviderVersion'] = request.terraform_provider_version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProducts',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/products',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_products(
        self,
        request: main_models.ListProductsRequest,
    ) -> main_models.ListProductsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_products_with_options(request, headers, runtime)

    async def list_products_async(
        self,
        request: main_models.ListProductsRequest,
    ) -> main_models.ListProductsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_products_with_options_async(request, headers, runtime)

    def list_project_with_options(
        self,
        tmp_req: main_models.ListProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectResponse:
        tmp_req.validate()
        request = main_models.ListProjectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProject',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/project',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_with_options_async(
        self,
        tmp_req: main_models.ListProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProjectResponse:
        tmp_req.validate()
        request = main_models.ListProjectShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProject',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/project',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project(
        self,
        request: main_models.ListProjectRequest,
    ) -> main_models.ListProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_project_with_options(request, headers, runtime)

    async def list_project_async(
        self,
        request: main_models.ListProjectRequest,
    ) -> main_models.ListProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_project_with_options_async(request, headers, runtime)

    def list_registry_module_versions_with_options(
        self,
        request: main_models.ListRegistryModuleVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRegistryModuleVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.module_name):
            query['moduleName'] = request.module_name
        if not DaraCore.is_null(request.namespace_name):
            query['namespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegistryModuleVersions',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModuleVersion',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegistryModuleVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_registry_module_versions_with_options_async(
        self,
        request: main_models.ListRegistryModuleVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRegistryModuleVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.module_name):
            query['moduleName'] = request.module_name
        if not DaraCore.is_null(request.namespace_name):
            query['namespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegistryModuleVersions',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModuleVersion',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegistryModuleVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_registry_module_versions(
        self,
        request: main_models.ListRegistryModuleVersionsRequest,
    ) -> main_models.ListRegistryModuleVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_registry_module_versions_with_options(request, headers, runtime)

    async def list_registry_module_versions_async(
        self,
        request: main_models.ListRegistryModuleVersionsRequest,
    ) -> main_models.ListRegistryModuleVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_registry_module_versions_with_options_async(request, headers, runtime)

    def list_registry_modules_with_options(
        self,
        request: main_models.ListRegistryModulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRegistryModulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.namespace_name):
            query['namespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegistryModules',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegistryModulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_registry_modules_with_options_async(
        self,
        request: main_models.ListRegistryModulesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRegistryModulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.namespace_name):
            query['namespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegistryModules',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModules',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegistryModulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_registry_modules(
        self,
        request: main_models.ListRegistryModulesRequest,
    ) -> main_models.ListRegistryModulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_registry_modules_with_options(request, headers, runtime)

    async def list_registry_modules_async(
        self,
        request: main_models.ListRegistryModulesRequest,
    ) -> main_models.ListRegistryModulesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_registry_modules_with_options_async(request, headers, runtime)

    def list_registry_namespaces_with_options(
        self,
        request: main_models.ListRegistryNamespacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRegistryNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegistryNamespaces',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryNamespace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegistryNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_registry_namespaces_with_options_async(
        self,
        request: main_models.ListRegistryNamespacesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRegistryNamespacesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRegistryNamespaces',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryNamespace',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegistryNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_registry_namespaces(
        self,
        request: main_models.ListRegistryNamespacesRequest,
    ) -> main_models.ListRegistryNamespacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_registry_namespaces_with_options(request, headers, runtime)

    async def list_registry_namespaces_async(
        self,
        request: main_models.ListRegistryNamespacesRequest,
    ) -> main_models.ListRegistryNamespacesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_registry_namespaces_with_options_async(request, headers, runtime)

    def list_resource_export_task_versions_with_options(
        self,
        export_task_id: str,
        request: main_models.ListResourceExportTaskVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceExportTaskVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.export_version):
            query['exportVersion'] = request.export_version
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceExportTaskVersions',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/exportTasks/{DaraURL.percent_encode(export_task_id)}/exportVersions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceExportTaskVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_export_task_versions_with_options_async(
        self,
        export_task_id: str,
        request: main_models.ListResourceExportTaskVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceExportTaskVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.export_version):
            query['exportVersion'] = request.export_version
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceExportTaskVersions',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/exportTasks/{DaraURL.percent_encode(export_task_id)}/exportVersions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceExportTaskVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_export_task_versions(
        self,
        export_task_id: str,
        request: main_models.ListResourceExportTaskVersionsRequest,
    ) -> main_models.ListResourceExportTaskVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_resource_export_task_versions_with_options(export_task_id, request, headers, runtime)

    async def list_resource_export_task_versions_async(
        self,
        export_task_id: str,
        request: main_models.ListResourceExportTaskVersionsRequest,
    ) -> main_models.ListResourceExportTaskVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_resource_export_task_versions_with_options_async(export_task_id, request, headers, runtime)

    def list_resource_export_tasks_with_options(
        self,
        request: main_models.ListResourceExportTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceExportTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.export_task_id):
            query['exportTaskId'] = request.export_task_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceExportTasks',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/exportTasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceExportTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_export_tasks_with_options_async(
        self,
        request: main_models.ListResourceExportTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceExportTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.export_task_id):
            query['exportTaskId'] = request.export_task_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceExportTasks',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/exportTasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceExportTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_export_tasks(
        self,
        request: main_models.ListResourceExportTasksRequest,
    ) -> main_models.ListResourceExportTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_resource_export_tasks_with_options(request, headers, runtime)

    async def list_resource_export_tasks_async(
        self,
        request: main_models.ListResourceExportTasksRequest,
    ) -> main_models.ListResourceExportTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_resource_export_tasks_with_options_async(request, headers, runtime)

    def list_resource_types_with_options(
        self,
        tmp_req: main_models.ListResourceTypesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceTypesResponse:
        tmp_req.validate()
        request = main_models.ListResourceTypesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.terraform_resource_types):
            request.terraform_resource_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.terraform_resource_types, 'terraformResourceTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.product):
            query['product'] = request.product
        if not DaraCore.is_null(request.sort):
            query['sort'] = request.sort
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.subcategory):
            query['subcategory'] = request.subcategory
        if not DaraCore.is_null(request.support_terraformer):
            query['supportTerraformer'] = request.support_terraformer
        if not DaraCore.is_null(request.terraform_provider_version):
            query['terraformProviderVersion'] = request.terraform_provider_version
        if not DaraCore.is_null(request.terraform_resource_types_shrink):
            query['terraformResourceTypes'] = request.terraform_resource_types_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceTypes',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/resourceTypes',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceTypesResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_resource_types_with_options_async(
        self,
        tmp_req: main_models.ListResourceTypesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceTypesResponse:
        tmp_req.validate()
        request = main_models.ListResourceTypesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.terraform_resource_types):
            request.terraform_resource_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.terraform_resource_types, 'terraformResourceTypes', 'simple')
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.product):
            query['product'] = request.product
        if not DaraCore.is_null(request.sort):
            query['sort'] = request.sort
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.subcategory):
            query['subcategory'] = request.subcategory
        if not DaraCore.is_null(request.support_terraformer):
            query['supportTerraformer'] = request.support_terraformer
        if not DaraCore.is_null(request.terraform_provider_version):
            query['terraformProviderVersion'] = request.terraform_provider_version
        if not DaraCore.is_null(request.terraform_resource_types_shrink):
            query['terraformResourceTypes'] = request.terraform_resource_types_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceTypes',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/resourceTypes',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceTypesResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_resource_types(
        self,
        request: main_models.ListResourceTypesRequest,
    ) -> main_models.ListResourceTypesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_resource_types_with_options(request, headers, runtime)

    async def list_resource_types_async(
        self,
        request: main_models.ListResourceTypesRequest,
    ) -> main_models.ListResourceTypesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_resource_types_with_options_async(request, headers, runtime)

    def list_tasks_with_options(
        self,
        tmp_req: main_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTasksResponse:
        tmp_req.validate()
        request = main_models.ListTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['groupId'] = request.group_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.module_id):
            query['moduleId'] = request.module_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['projectId'] = request.project_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTasks',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        tmp_req: main_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTasksResponse:
        tmp_req.validate()
        request = main_models.ListTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['groupId'] = request.group_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.module_id):
            query['moduleId'] = request.module_id
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.project_id):
            query['projectId'] = request.project_id
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        if not DaraCore.is_null(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not DaraCore.is_null(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTasks',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        request: main_models.ListTasksRequest,
    ) -> main_models.ListTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(request, headers, runtime)

    async def list_tasks_async(
        self,
        request: main_models.ListTasksRequest,
    ) -> main_models.ListTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tasks_with_options_async(request, headers, runtime)

    def list_terraform_provider_versions_with_options(
        self,
        request: main_models.ListTerraformProviderVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTerraformProviderVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.usage):
            query['usage'] = request.usage
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTerraformProviderVersions',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/version/terraform/provider',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTerraformProviderVersionsResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_terraform_provider_versions_with_options_async(
        self,
        request: main_models.ListTerraformProviderVersionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTerraformProviderVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        if not DaraCore.is_null(request.usage):
            query['usage'] = request.usage
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTerraformProviderVersions',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/version/terraform/provider',
            method = 'GET',
            auth_type = 'Anonymous',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTerraformProviderVersionsResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_terraform_provider_versions(
        self,
        request: main_models.ListTerraformProviderVersionsRequest,
    ) -> main_models.ListTerraformProviderVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_terraform_provider_versions_with_options(request, headers, runtime)

    async def list_terraform_provider_versions_async(
        self,
        request: main_models.ListTerraformProviderVersionsRequest,
    ) -> main_models.ListTerraformProviderVersionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_terraform_provider_versions_with_options_async(request, headers, runtime)

    def manage_terraform_state_with_options(
        self,
        request: main_models.ManageTerraformStateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ManageTerraformStateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.identifier):
            body['identifier'] = request.identifier
        if not DaraCore.is_null(request.import_resource_id):
            body['importResourceId'] = request.import_resource_id
        if not DaraCore.is_null(request.resource_identifier):
            body['resourceIdentifier'] = request.resource_identifier
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ManageTerraformState',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/terraformState/manage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManageTerraformStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def manage_terraform_state_with_options_async(
        self,
        request: main_models.ManageTerraformStateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ManageTerraformStateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.action):
            body['action'] = request.action
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.identifier):
            body['identifier'] = request.identifier
        if not DaraCore.is_null(request.import_resource_id):
            body['importResourceId'] = request.import_resource_id
        if not DaraCore.is_null(request.resource_identifier):
            body['resourceIdentifier'] = request.resource_identifier
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ManageTerraformState',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/terraformState/manage',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ManageTerraformStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manage_terraform_state(
        self,
        request: main_models.ManageTerraformStateRequest,
    ) -> main_models.ManageTerraformStateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.manage_terraform_state_with_options(request, headers, runtime)

    async def manage_terraform_state_async(
        self,
        request: main_models.ManageTerraformStateRequest,
    ) -> main_models.ManageTerraformStateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.manage_terraform_state_with_options_async(request, headers, runtime)

    def operate_job_with_options(
        self,
        task_id: str,
        job_id: str,
        operation_type: str,
        request: main_models.OperateJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OperateJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['comment'] = request.comment
        if not DaraCore.is_null(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateJob',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}/jobs/{DaraURL.percent_encode(job_id)}/operation/{DaraURL.percent_encode(operation_type)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_job_with_options_async(
        self,
        task_id: str,
        job_id: str,
        operation_type: str,
        request: main_models.OperateJobRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OperateJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comment):
            query['comment'] = request.comment
        if not DaraCore.is_null(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OperateJob',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}/jobs/{DaraURL.percent_encode(job_id)}/operation/{DaraURL.percent_encode(operation_type)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OperateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_job(
        self,
        task_id: str,
        job_id: str,
        operation_type: str,
        request: main_models.OperateJobRequest,
    ) -> main_models.OperateJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.operate_job_with_options(task_id, job_id, operation_type, request, headers, runtime)

    async def operate_job_async(
        self,
        task_id: str,
        job_id: str,
        operation_type: str,
        request: main_models.OperateJobRequest,
    ) -> main_models.OperateJobResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.operate_job_with_options_async(task_id, job_id, operation_type, request, headers, runtime)

    def publish_registry_module_version_with_options(
        self,
        request: main_models.PublishRegistryModuleVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishRegistryModuleVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.module_name):
            body['moduleName'] = request.module_name
        if not DaraCore.is_null(request.namespace_name):
            body['namespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishRegistryModuleVersion',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModuleVersion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishRegistryModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_registry_module_version_with_options_async(
        self,
        request: main_models.PublishRegistryModuleVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PublishRegistryModuleVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.module_name):
            body['moduleName'] = request.module_name
        if not DaraCore.is_null(request.namespace_name):
            body['namespaceName'] = request.namespace_name
        if not DaraCore.is_null(request.version):
            body['version'] = request.version
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PublishRegistryModuleVersion',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModuleVersion',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PublishRegistryModuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_registry_module_version(
        self,
        request: main_models.PublishRegistryModuleVersionRequest,
    ) -> main_models.PublishRegistryModuleVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.publish_registry_module_version_with_options(request, headers, runtime)

    async def publish_registry_module_version_async(
        self,
        request: main_models.PublishRegistryModuleVersionRequest,
    ) -> main_models.PublishRegistryModuleVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.publish_registry_module_version_with_options_async(request, headers, runtime)

    def remove_shared_accounts_with_options(
        self,
        tmp_req: main_models.RemoveSharedAccountsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveSharedAccountsResponse:
        tmp_req.validate()
        request = main_models.RemoveSharedAccountsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'accountIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            query['accountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveSharedAccounts',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/sharedAccounts',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveSharedAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_shared_accounts_with_options_async(
        self,
        tmp_req: main_models.RemoveSharedAccountsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveSharedAccountsResponse:
        tmp_req.validate()
        request = main_models.RemoveSharedAccountsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'accountIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            query['accountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.resource_id):
            query['resourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveSharedAccounts',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/sharedAccounts',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveSharedAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_shared_accounts(
        self,
        request: main_models.RemoveSharedAccountsRequest,
    ) -> main_models.RemoveSharedAccountsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_shared_accounts_with_options(request, headers, runtime)

    async def remove_shared_accounts_async(
        self,
        request: main_models.RemoveSharedAccountsRequest,
    ) -> main_models.RemoveSharedAccountsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_shared_accounts_with_options_async(request, headers, runtime)

    def update_explorer_module_attribute_with_options(
        self,
        explorer_module_id: str,
        request: main_models.UpdateExplorerModuleAttributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExplorerModuleAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExplorerModuleAttribute',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/explorerModule/{DaraURL.percent_encode(explorer_module_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExplorerModuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_explorer_module_attribute_with_options_async(
        self,
        explorer_module_id: str,
        request: main_models.UpdateExplorerModuleAttributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateExplorerModuleAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateExplorerModuleAttribute',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/explorerModule/{DaraURL.percent_encode(explorer_module_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateExplorerModuleAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_explorer_module_attribute(
        self,
        explorer_module_id: str,
        request: main_models.UpdateExplorerModuleAttributeRequest,
    ) -> main_models.UpdateExplorerModuleAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_explorer_module_attribute_with_options(explorer_module_id, request, headers, runtime)

    async def update_explorer_module_attribute_async(
        self,
        explorer_module_id: str,
        request: main_models.UpdateExplorerModuleAttributeRequest,
    ) -> main_models.UpdateExplorerModuleAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_explorer_module_attribute_with_options_async(explorer_module_id, request, headers, runtime)

    def update_group_with_options(
        self,
        group_id: str,
        request: main_models.UpdateGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not DaraCore.is_null(request.auto_trigger):
            body['autoTrigger'] = request.auto_trigger
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.forced_setting):
            body['forcedSetting'] = request.forced_setting
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.notify_config):
            body['notifyConfig'] = request.notify_config
        if not DaraCore.is_null(request.notify_operation_types):
            body['notifyOperationTypes'] = request.notify_operation_types
        if not DaraCore.is_null(request.ram_role):
            body['ramRole'] = request.ram_role
        if not DaraCore.is_null(request.report_export_field):
            body['reportExportField'] = request.report_export_field
        if not DaraCore.is_null(request.report_export_path):
            body['reportExportPath'] = request.report_export_path
        if not DaraCore.is_null(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not DaraCore.is_null(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        if not DaraCore.is_null(request.trigger_resource_type):
            body['triggerResourceType'] = request.trigger_resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroup',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/group/{DaraURL.percent_encode(group_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_with_options_async(
        self,
        group_id: str,
        request: main_models.UpdateGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not DaraCore.is_null(request.auto_trigger):
            body['autoTrigger'] = request.auto_trigger
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.forced_setting):
            body['forcedSetting'] = request.forced_setting
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.notify_config):
            body['notifyConfig'] = request.notify_config
        if not DaraCore.is_null(request.notify_operation_types):
            body['notifyOperationTypes'] = request.notify_operation_types
        if not DaraCore.is_null(request.ram_role):
            body['ramRole'] = request.ram_role
        if not DaraCore.is_null(request.report_export_field):
            body['reportExportField'] = request.report_export_field
        if not DaraCore.is_null(request.report_export_path):
            body['reportExportPath'] = request.report_export_path
        if not DaraCore.is_null(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not DaraCore.is_null(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        if not DaraCore.is_null(request.trigger_resource_type):
            body['triggerResourceType'] = request.trigger_resource_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGroup',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/group/{DaraURL.percent_encode(group_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group(
        self,
        group_id: str,
        request: main_models.UpdateGroupRequest,
    ) -> main_models.UpdateGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_group_with_options(group_id, request, headers, runtime)

    async def update_group_async(
        self,
        group_id: str,
        request: main_models.UpdateGroupRequest,
    ) -> main_models.UpdateGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_group_with_options_async(group_id, request, headers, runtime)

    def update_module_attribute_with_options(
        self,
        module_id: str,
        request: main_models.UpdateModuleAttributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModuleAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.group_info):
            body['groupInfo'] = request.group_info
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.source_path):
            body['sourcePath'] = request.source_path
        if not DaraCore.is_null(request.state_path):
            body['statePath'] = request.state_path
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.version_strategy):
            body['versionStrategy'] = request.version_strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModuleAttribute',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/modules/{DaraURL.percent_encode(module_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_module_attribute_with_options_async(
        self,
        module_id: str,
        request: main_models.UpdateModuleAttributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateModuleAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.group_info):
            body['groupInfo'] = request.group_info
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.source_path):
            body['sourcePath'] = request.source_path
        if not DaraCore.is_null(request.state_path):
            body['statePath'] = request.state_path
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.version_strategy):
            body['versionStrategy'] = request.version_strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateModuleAttribute',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/modules/{DaraURL.percent_encode(module_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateModuleAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_module_attribute(
        self,
        module_id: str,
        request: main_models.UpdateModuleAttributeRequest,
    ) -> main_models.UpdateModuleAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_module_attribute_with_options(module_id, request, headers, runtime)

    async def update_module_attribute_async(
        self,
        module_id: str,
        request: main_models.UpdateModuleAttributeRequest,
    ) -> main_models.UpdateModuleAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_module_attribute_with_options_async(module_id, request, headers, runtime)

    def update_project_with_options(
        self,
        project_id: str,
        request: main_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProject',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/project/{DaraURL.percent_encode(project_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        project_id: str,
        request: main_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProjectResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProject',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/project/{DaraURL.percent_encode(project_id)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        project_id: str,
        request: main_models.UpdateProjectRequest,
    ) -> main_models.UpdateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_project_with_options(project_id, request, headers, runtime)

    async def update_project_async(
        self,
        project_id: str,
        request: main_models.UpdateProjectRequest,
    ) -> main_models.UpdateProjectResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_project_with_options_async(project_id, request, headers, runtime)

    def update_registry_module_attribute_with_options(
        self,
        namespace_name: str,
        module_name: str,
        request: main_models.UpdateRegistryModuleAttributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRegistryModuleAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.acl):
            body['acl'] = request.acl
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRegistryModuleAttribute',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModule/{DaraURL.percent_encode(namespace_name)}/{DaraURL.percent_encode(module_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRegistryModuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_registry_module_attribute_with_options_async(
        self,
        namespace_name: str,
        module_name: str,
        request: main_models.UpdateRegistryModuleAttributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRegistryModuleAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.acl):
            body['acl'] = request.acl
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRegistryModuleAttribute',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryModule/{DaraURL.percent_encode(namespace_name)}/{DaraURL.percent_encode(module_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRegistryModuleAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_registry_module_attribute(
        self,
        namespace_name: str,
        module_name: str,
        request: main_models.UpdateRegistryModuleAttributeRequest,
    ) -> main_models.UpdateRegistryModuleAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_registry_module_attribute_with_options(namespace_name, module_name, request, headers, runtime)

    async def update_registry_module_attribute_async(
        self,
        namespace_name: str,
        module_name: str,
        request: main_models.UpdateRegistryModuleAttributeRequest,
    ) -> main_models.UpdateRegistryModuleAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_registry_module_attribute_with_options_async(namespace_name, module_name, request, headers, runtime)

    def update_registry_namespace_attribute_with_options(
        self,
        namespace_name: str,
        request: main_models.UpdateRegistryNamespaceAttributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRegistryNamespaceAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.acl):
            body['acl'] = request.acl
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRegistryNamespaceAttribute',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryNamespace/{DaraURL.percent_encode(namespace_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRegistryNamespaceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_registry_namespace_attribute_with_options_async(
        self,
        namespace_name: str,
        request: main_models.UpdateRegistryNamespaceAttributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRegistryNamespaceAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.acl):
            body['acl'] = request.acl
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRegistryNamespaceAttribute',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/registryNamespace/{DaraURL.percent_encode(namespace_name)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRegistryNamespaceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_registry_namespace_attribute(
        self,
        namespace_name: str,
        request: main_models.UpdateRegistryNamespaceAttributeRequest,
    ) -> main_models.UpdateRegistryNamespaceAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_registry_namespace_attribute_with_options(namespace_name, request, headers, runtime)

    async def update_registry_namespace_attribute_async(
        self,
        namespace_name: str,
        request: main_models.UpdateRegistryNamespaceAttributeRequest,
    ) -> main_models.UpdateRegistryNamespaceAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_registry_namespace_attribute_with_options_async(namespace_name, request, headers, runtime)

    def update_resource_export_task_attribute_with_options(
        self,
        export_task_id: str,
        request: main_models.UpdateResourceExportTaskAttributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceExportTaskAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.export_to_module):
            body['exportToModule'] = request.export_to_module
        if not DaraCore.is_null(request.include_rules):
            body['includeRules'] = request.include_rules
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.ram_role):
            body['ramRole'] = request.ram_role
        if not DaraCore.is_null(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not DaraCore.is_null(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not DaraCore.is_null(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceExportTaskAttribute',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/exportTasks/{DaraURL.percent_encode(export_task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceExportTaskAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_export_task_attribute_with_options_async(
        self,
        export_task_id: str,
        request: main_models.UpdateResourceExportTaskAttributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceExportTaskAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.export_to_module):
            body['exportToModule'] = request.export_to_module
        if not DaraCore.is_null(request.include_rules):
            body['includeRules'] = request.include_rules
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.ram_role):
            body['ramRole'] = request.ram_role
        if not DaraCore.is_null(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not DaraCore.is_null(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not DaraCore.is_null(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not DaraCore.is_null(request.variables):
            body['variables'] = request.variables
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResourceExportTaskAttribute',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/exportTasks/{DaraURL.percent_encode(export_task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceExportTaskAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_export_task_attribute(
        self,
        export_task_id: str,
        request: main_models.UpdateResourceExportTaskAttributeRequest,
    ) -> main_models.UpdateResourceExportTaskAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_resource_export_task_attribute_with_options(export_task_id, request, headers, runtime)

    async def update_resource_export_task_attribute_async(
        self,
        export_task_id: str,
        request: main_models.UpdateResourceExportTaskAttributeRequest,
    ) -> main_models.UpdateResourceExportTaskAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_resource_export_task_attribute_with_options_async(export_task_id, request, headers, runtime)

    def update_task_attribute_with_options(
        self,
        task_id: str,
        request: main_models.UpdateTaskAttributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTaskAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not DaraCore.is_null(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.group_info):
            body['groupInfo'] = request.group_info
        if not DaraCore.is_null(request.init_module_state):
            body['initModuleState'] = request.init_module_state
        if not DaraCore.is_null(request.module_version):
            body['moduleVersion'] = request.module_version
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.protection_strategy):
            body['protectionStrategy'] = request.protection_strategy
        if not DaraCore.is_null(request.ram_role):
            body['ramRole'] = request.ram_role
        if not DaraCore.is_null(request.skip_property_validation):
            body['skipPropertyValidation'] = request.skip_property_validation
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not DaraCore.is_null(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTaskAttribute',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTaskAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_task_attribute_with_options_async(
        self,
        task_id: str,
        request: main_models.UpdateTaskAttributeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTaskAttributeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not DaraCore.is_null(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.group_info):
            body['groupInfo'] = request.group_info
        if not DaraCore.is_null(request.init_module_state):
            body['initModuleState'] = request.init_module_state
        if not DaraCore.is_null(request.module_version):
            body['moduleVersion'] = request.module_version
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.protection_strategy):
            body['protectionStrategy'] = request.protection_strategy
        if not DaraCore.is_null(request.ram_role):
            body['ramRole'] = request.ram_role
        if not DaraCore.is_null(request.skip_property_validation):
            body['skipPropertyValidation'] = request.skip_property_validation
        if not DaraCore.is_null(request.tags):
            body['tags'] = request.tags
        if not DaraCore.is_null(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not DaraCore.is_null(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTaskAttribute',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/tasks/{DaraURL.percent_encode(task_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTaskAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_task_attribute(
        self,
        task_id: str,
        request: main_models.UpdateTaskAttributeRequest,
    ) -> main_models.UpdateTaskAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_task_attribute_with_options(task_id, request, headers, runtime)

    async def update_task_attribute_async(
        self,
        task_id: str,
        request: main_models.UpdateTaskAttributeRequest,
    ) -> main_models.UpdateTaskAttributeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_task_attribute_with_options_async(task_id, request, headers, runtime)

    def validate_module_with_sse(
        self,
        request: main_models.ValidateModuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> Generator[main_models.ValidateModuleResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.code_map):
            body['codeMap'] = request.code_map
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        if not DaraCore.is_null(request.source_path):
            body['sourcePath'] = request.source_path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/module/validation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.ValidateModuleResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def validate_module_with_sse_async(
        self,
        request: main_models.ValidateModuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.ValidateModuleResponse, None, None]:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.code_map):
            body['codeMap'] = request.code_map
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        if not DaraCore.is_null(request.source_path):
            body['sourcePath'] = request.source_path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/module/validation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.ValidateModuleResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def validate_module_with_options(
        self,
        request: main_models.ValidateModuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidateModuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.code_map):
            body['codeMap'] = request.code_map
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        if not DaraCore.is_null(request.source_path):
            body['sourcePath'] = request.source_path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/module/validation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_module_with_options_async(
        self,
        request: main_models.ValidateModuleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ValidateModuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['clientToken'] = request.client_token
        if not DaraCore.is_null(request.code):
            body['code'] = request.code
        if not DaraCore.is_null(request.code_map):
            body['codeMap'] = request.code_map
        if not DaraCore.is_null(request.source):
            body['source'] = request.source
        if not DaraCore.is_null(request.source_path):
            body['sourcePath'] = request.source_path
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateModule',
            version = '2021-08-06',
            protocol = 'HTTPS',
            pathname = f'/module/validation',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_module(
        self,
        request: main_models.ValidateModuleRequest,
    ) -> main_models.ValidateModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.validate_module_with_options(request, headers, runtime)

    async def validate_module_async(
        self,
        request: main_models.ValidateModuleRequest,
    ) -> main_models.ValidateModuleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.validate_module_with_options_async(request, headers, runtime)
