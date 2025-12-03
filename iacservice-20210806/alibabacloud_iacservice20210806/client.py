# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_iacservice20210806 import models as ia_cservice_20210806_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_shared_accounts_with_options(
        self,
        request: ia_cservice_20210806_models.AddSharedAccountsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.AddSharedAccountsResponse:
        """
        @summary 新增共享账号信息
        
        @param request: AddSharedAccountsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSharedAccountsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_ids):
            body['accountIds'] = request.account_ids
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddSharedAccounts',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/sharedAccounts',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.AddSharedAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_shared_accounts_with_options_async(
        self,
        request: ia_cservice_20210806_models.AddSharedAccountsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.AddSharedAccountsResponse:
        """
        @summary 新增共享账号信息
        
        @param request: AddSharedAccountsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddSharedAccountsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_ids):
            body['accountIds'] = request.account_ids
        if not UtilClient.is_unset(request.resource_id):
            body['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddSharedAccounts',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/sharedAccounts',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.AddSharedAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_shared_accounts(
        self,
        request: ia_cservice_20210806_models.AddSharedAccountsRequest,
    ) -> ia_cservice_20210806_models.AddSharedAccountsResponse:
        """
        @summary 新增共享账号信息
        
        @param request: AddSharedAccountsRequest
        @return: AddSharedAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_shared_accounts_with_options(request, headers, runtime)

    async def add_shared_accounts_async(
        self,
        request: ia_cservice_20210806_models.AddSharedAccountsRequest,
    ) -> ia_cservice_20210806_models.AddSharedAccountsResponse:
        """
        @summary 新增共享账号信息
        
        @param request: AddSharedAccountsRequest
        @return: AddSharedAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_shared_accounts_with_options_async(request, headers, runtime)

    def associate_group_with_options(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.AssociateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.AssociateGroupResponse:
        """
        @summary 分组关联
        
        @param request: AssociateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_ids):
            body['resourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}/associate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.AssociateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_group_with_options_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.AssociateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.AssociateGroupResponse:
        """
        @summary 分组关联
        
        @param request: AssociateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: AssociateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.resource_ids):
            body['resourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssociateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}/associate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.AssociateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_group(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.AssociateGroupRequest,
    ) -> ia_cservice_20210806_models.AssociateGroupResponse:
        """
        @summary 分组关联
        
        @param request: AssociateGroupRequest
        @return: AssociateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.associate_group_with_options(group_id, request, headers, runtime)

    async def associate_group_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.AssociateGroupRequest,
    ) -> ia_cservice_20210806_models.AssociateGroupResponse:
        """
        @summary 分组关联
        
        @param request: AssociateGroupRequest
        @return: AssociateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.associate_group_with_options_async(group_id, request, headers, runtime)

    def cancel_resource_export_task_with_options(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.CancelResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CancelResourceExportTaskResponse:
        """
        @summary 取消资源导出任务
        
        @param request: CancelResourceExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelResourceExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/cancel/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CancelResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_resource_export_task_with_options_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.CancelResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CancelResourceExportTaskResponse:
        """
        @summary 取消资源导出任务
        
        @param request: CancelResourceExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelResourceExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/cancel/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CancelResourceExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_resource_export_task(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.CancelResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.CancelResourceExportTaskResponse:
        """
        @summary 取消资源导出任务
        
        @param request: CancelResourceExportTaskRequest
        @return: CancelResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_resource_export_task_with_options(export_task_id, request, headers, runtime)

    async def cancel_resource_export_task_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.CancelResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.CancelResourceExportTaskResponse:
        """
        @summary 取消资源导出任务
        
        @param request: CancelResourceExportTaskRequest
        @return: CancelResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_resource_export_task_with_options_async(export_task_id, request, headers, runtime)

    def create_group_with_options(
        self,
        request: ia_cservice_20210806_models.CreateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateGroupResponse:
        """
        @summary 创建分组
        
        @param request: CreateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.auto_trigger):
            body['autoTrigger'] = request.auto_trigger
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.forced_setting):
            body['forcedSetting'] = request.forced_setting
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.notify_config):
            body['notifyConfig'] = request.notify_config
        if not UtilClient.is_unset(request.notify_operation_types):
            body['notifyOperationTypes'] = request.notify_operation_types
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.report_export_field):
            body['reportExportField'] = request.report_export_field
        if not UtilClient.is_unset(request.report_export_path):
            body['reportExportPath'] = request.report_export_path
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.trigger_resource_type):
            body['triggerResourceType'] = request.trigger_resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateGroupResponse:
        """
        @summary 创建分组
        
        @param request: CreateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.auto_trigger):
            body['autoTrigger'] = request.auto_trigger
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.forced_setting):
            body['forcedSetting'] = request.forced_setting
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.notify_config):
            body['notifyConfig'] = request.notify_config
        if not UtilClient.is_unset(request.notify_operation_types):
            body['notifyOperationTypes'] = request.notify_operation_types
        if not UtilClient.is_unset(request.project_id):
            body['projectId'] = request.project_id
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.report_export_field):
            body['reportExportField'] = request.report_export_field
        if not UtilClient.is_unset(request.report_export_path):
            body['reportExportPath'] = request.report_export_path
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.trigger_resource_type):
            body['triggerResourceType'] = request.trigger_resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group(
        self,
        request: ia_cservice_20210806_models.CreateGroupRequest,
    ) -> ia_cservice_20210806_models.CreateGroupResponse:
        """
        @summary 创建分组
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_group_with_options(request, headers, runtime)

    async def create_group_async(
        self,
        request: ia_cservice_20210806_models.CreateGroupRequest,
    ) -> ia_cservice_20210806_models.CreateGroupResponse:
        """
        @summary 创建分组
        
        @param request: CreateGroupRequest
        @return: CreateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_group_with_options_async(request, headers, runtime)

    def create_job_with_options(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateJobResponse:
        """
        @summary 创建作业
        
        @param request: CreateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.sub_command):
            body['subCommand'] = request.sub_command
        if not UtilClient.is_unset(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.CreateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateJobResponse:
        """
        @summary 创建作业
        
        @param request: CreateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateJobResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.sub_command):
            body['subCommand'] = request.sub_command
        if not UtilClient.is_unset(request.task_type):
            body['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/jobs',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.CreateJobRequest,
    ) -> ia_cservice_20210806_models.CreateJobResponse:
        """
        @summary 创建作业
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_job_with_options(task_id, request, headers, runtime)

    async def create_job_async(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.CreateJobRequest,
    ) -> ia_cservice_20210806_models.CreateJobResponse:
        """
        @summary 创建作业
        
        @param request: CreateJobRequest
        @return: CreateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_job_with_options_async(task_id, request, headers, runtime)

    def create_module_with_options(
        self,
        request: ia_cservice_20210806_models.CreateModuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateModuleResponse:
        """
        @summary 创建模板
        
        @param request: CreateModuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.source_path):
            body['sourcePath'] = request.source_path
        if not UtilClient.is_unset(request.state_path):
            body['statePath'] = request.state_path
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.version_strategy):
            body['versionStrategy'] = request.version_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_module_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateModuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateModuleResponse:
        """
        @summary 创建模板
        
        @param request: CreateModuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.source_path):
            body['sourcePath'] = request.source_path
        if not UtilClient.is_unset(request.state_path):
            body['statePath'] = request.state_path
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.version_strategy):
            body['versionStrategy'] = request.version_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_module(
        self,
        request: ia_cservice_20210806_models.CreateModuleRequest,
    ) -> ia_cservice_20210806_models.CreateModuleResponse:
        """
        @summary 创建模板
        
        @param request: CreateModuleRequest
        @return: CreateModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_module_with_options(request, headers, runtime)

    async def create_module_async(
        self,
        request: ia_cservice_20210806_models.CreateModuleRequest,
    ) -> ia_cservice_20210806_models.CreateModuleResponse:
        """
        @summary 创建模板
        
        @param request: CreateModuleRequest
        @return: CreateModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_module_with_options_async(request, headers, runtime)

    def create_module_version_with_options(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.CreateModuleVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateModuleVersionResponse:
        """
        @summary 创建模板版本
        
        @param request: CreateModuleVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModuleVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_module_version_with_options_async(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.CreateModuleVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateModuleVersionResponse:
        """
        @summary 创建模板版本
        
        @param request: CreateModuleVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateModuleVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}/versions',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateModuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_module_version(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.CreateModuleVersionRequest,
    ) -> ia_cservice_20210806_models.CreateModuleVersionResponse:
        """
        @summary 创建模板版本
        
        @param request: CreateModuleVersionRequest
        @return: CreateModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_module_version_with_options(module_id, request, headers, runtime)

    async def create_module_version_async(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.CreateModuleVersionRequest,
    ) -> ia_cservice_20210806_models.CreateModuleVersionResponse:
        """
        @summary 创建模板版本
        
        @param request: CreateModuleVersionRequest
        @return: CreateModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_module_version_with_options_async(module_id, request, headers, runtime)

    def create_project_with_options(
        self,
        request: ia_cservice_20210806_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param request: CreateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_project_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param request: CreateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_project(
        self,
        request: ia_cservice_20210806_models.CreateProjectRequest,
    ) -> ia_cservice_20210806_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_project_with_options(request, headers, runtime)

    async def create_project_async(
        self,
        request: ia_cservice_20210806_models.CreateProjectRequest,
    ) -> ia_cservice_20210806_models.CreateProjectResponse:
        """
        @summary 创建项目
        
        @param request: CreateProjectRequest
        @return: CreateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_project_with_options_async(request, headers, runtime)

    def create_registry_module_with_options(
        self,
        request: ia_cservice_20210806_models.CreateRegistryModuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateRegistryModuleResponse:
        """
        @summary 创建RegistryModule
        
        @param request: CreateRegistryModuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRegistryModuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.acl):
            body['acl'] = request.acl
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.module_name):
            body['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.namespace_name):
            body['namespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.provider):
            body['provider'] = request.provider
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRegistryModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateRegistryModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_registry_module_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateRegistryModuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateRegistryModuleResponse:
        """
        @summary 创建RegistryModule
        
        @param request: CreateRegistryModuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRegistryModuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.acl):
            body['acl'] = request.acl
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.module_name):
            body['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.namespace_name):
            body['namespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.provider):
            body['provider'] = request.provider
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRegistryModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModule',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateRegistryModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_registry_module(
        self,
        request: ia_cservice_20210806_models.CreateRegistryModuleRequest,
    ) -> ia_cservice_20210806_models.CreateRegistryModuleResponse:
        """
        @summary 创建RegistryModule
        
        @param request: CreateRegistryModuleRequest
        @return: CreateRegistryModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_registry_module_with_options(request, headers, runtime)

    async def create_registry_module_async(
        self,
        request: ia_cservice_20210806_models.CreateRegistryModuleRequest,
    ) -> ia_cservice_20210806_models.CreateRegistryModuleResponse:
        """
        @summary 创建RegistryModule
        
        @param request: CreateRegistryModuleRequest
        @return: CreateRegistryModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_registry_module_with_options_async(request, headers, runtime)

    def create_registry_namespace_with_options(
        self,
        request: ia_cservice_20210806_models.CreateRegistryNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateRegistryNamespaceResponse:
        """
        @summary 创建工作空间
        
        @param request: CreateRegistryNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRegistryNamespaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.acl):
            body['acl'] = request.acl
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.maintainer):
            body['maintainer'] = request.maintainer
        if not UtilClient.is_unset(request.namespace_name):
            body['namespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRegistryNamespace',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryNamespace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateRegistryNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_registry_namespace_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateRegistryNamespaceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateRegistryNamespaceResponse:
        """
        @summary 创建工作空间
        
        @param request: CreateRegistryNamespaceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRegistryNamespaceResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.acl):
            body['acl'] = request.acl
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.maintainer):
            body['maintainer'] = request.maintainer
        if not UtilClient.is_unset(request.namespace_name):
            body['namespaceName'] = request.namespace_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRegistryNamespace',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryNamespace',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateRegistryNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_registry_namespace(
        self,
        request: ia_cservice_20210806_models.CreateRegistryNamespaceRequest,
    ) -> ia_cservice_20210806_models.CreateRegistryNamespaceResponse:
        """
        @summary 创建工作空间
        
        @param request: CreateRegistryNamespaceRequest
        @return: CreateRegistryNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_registry_namespace_with_options(request, headers, runtime)

    async def create_registry_namespace_async(
        self,
        request: ia_cservice_20210806_models.CreateRegistryNamespaceRequest,
    ) -> ia_cservice_20210806_models.CreateRegistryNamespaceResponse:
        """
        @summary 创建工作空间
        
        @param request: CreateRegistryNamespaceRequest
        @return: CreateRegistryNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_registry_namespace_with_options_async(request, headers, runtime)

    def create_resource_export_task_with_options(
        self,
        request: ia_cservice_20210806_models.CreateResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateResourceExportTaskResponse:
        """
        @summary 创建导出任务
        
        @param request: CreateResourceExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.export_to_module):
            body['exportToModule'] = request.export_to_module
        if not UtilClient.is_unset(request.include_rules):
            body['includeRules'] = request.include_rules
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_export_task_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateResourceExportTaskResponse:
        """
        @summary 创建导出任务
        
        @param request: CreateResourceExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.export_to_module):
            body['exportToModule'] = request.export_to_module
        if not UtilClient.is_unset(request.include_rules):
            body['includeRules'] = request.include_rules
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateResourceExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource_export_task(
        self,
        request: ia_cservice_20210806_models.CreateResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.CreateResourceExportTaskResponse:
        """
        @summary 创建导出任务
        
        @param request: CreateResourceExportTaskRequest
        @return: CreateResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_resource_export_task_with_options(request, headers, runtime)

    async def create_resource_export_task_async(
        self,
        request: ia_cservice_20210806_models.CreateResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.CreateResourceExportTaskResponse:
        """
        @summary 创建导出任务
        
        @param request: CreateResourceExportTaskRequest
        @return: CreateResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_resource_export_task_with_options_async(request, headers, runtime)

    def create_task_with_options(
        self,
        request: ia_cservice_20210806_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.init_module_state):
            body['initModuleState'] = request.init_module_state
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protection_strategy):
            body['protectionStrategy'] = request.protection_strategy
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.skip_property_validation):
            body['skipPropertyValidation'] = request.skip_property_validation
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.task_backend):
            body['taskBackend'] = request.task_backend
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_task_with_options_async(
        self,
        request: ia_cservice_20210806_models.CreateTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.CreateTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.init_module_state):
            body['initModuleState'] = request.init_module_state
        if not UtilClient.is_unset(request.module_id):
            body['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protection_strategy):
            body['protectionStrategy'] = request.protection_strategy
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.skip_property_validation):
            body['skipPropertyValidation'] = request.skip_property_validation
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.task_backend):
            body['taskBackend'] = request.task_backend
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.CreateTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_task(
        self,
        request: ia_cservice_20210806_models.CreateTaskRequest,
    ) -> ia_cservice_20210806_models.CreateTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateTaskRequest
        @return: CreateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_task_with_options(request, headers, runtime)

    async def create_task_async(
        self,
        request: ia_cservice_20210806_models.CreateTaskRequest,
    ) -> ia_cservice_20210806_models.CreateTaskResponse:
        """
        @summary 创建任务
        
        @param request: CreateTaskRequest
        @return: CreateTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_task_with_options_async(request, headers, runtime)

    def delete_group_with_options(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteGroupResponse:
        """
        @summary 删除分组
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_with_options_async(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteGroupResponse:
        """
        @summary 删除分组
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group(
        self,
        group_id: str,
    ) -> ia_cservice_20210806_models.DeleteGroupResponse:
        """
        @summary 删除分组
        
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_group_with_options(group_id, headers, runtime)

    async def delete_group_async(
        self,
        group_id: str,
    ) -> ia_cservice_20210806_models.DeleteGroupResponse:
        """
        @summary 删除分组
        
        @return: DeleteGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_group_with_options_async(group_id, headers, runtime)

    def delete_module_with_options(
        self,
        module_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteModuleResponse:
        """
        @summary 删除模板
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_module_with_options_async(
        self,
        module_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteModuleResponse:
        """
        @summary 删除模板
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteModuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_module(
        self,
        module_id: str,
    ) -> ia_cservice_20210806_models.DeleteModuleResponse:
        """
        @summary 删除模板
        
        @return: DeleteModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_module_with_options(module_id, headers, runtime)

    async def delete_module_async(
        self,
        module_id: str,
    ) -> ia_cservice_20210806_models.DeleteModuleResponse:
        """
        @summary 删除模板
        
        @return: DeleteModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_module_with_options_async(module_id, headers, runtime)

    def delete_project_with_options(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_project_with_options_async(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_project(
        self,
        project_id: str,
    ) -> ia_cservice_20210806_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_project_with_options(project_id, headers, runtime)

    async def delete_project_async(
        self,
        project_id: str,
    ) -> ia_cservice_20210806_models.DeleteProjectResponse:
        """
        @summary 删除项目
        
        @return: DeleteProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_project_with_options_async(project_id, headers, runtime)

    def delete_registry_module_with_options(
        self,
        namespace_name: str,
        module_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteRegistryModuleResponse:
        """
        @summary 删除RegistryModule
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRegistryModuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRegistryModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModule/{OpenApiUtilClient.get_encode_param(namespace_name)}/{OpenApiUtilClient.get_encode_param(module_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteRegistryModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_registry_module_with_options_async(
        self,
        namespace_name: str,
        module_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteRegistryModuleResponse:
        """
        @summary 删除RegistryModule
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRegistryModuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRegistryModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModule/{OpenApiUtilClient.get_encode_param(namespace_name)}/{OpenApiUtilClient.get_encode_param(module_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteRegistryModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_registry_module(
        self,
        namespace_name: str,
        module_name: str,
    ) -> ia_cservice_20210806_models.DeleteRegistryModuleResponse:
        """
        @summary 删除RegistryModule
        
        @return: DeleteRegistryModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_registry_module_with_options(namespace_name, module_name, headers, runtime)

    async def delete_registry_module_async(
        self,
        namespace_name: str,
        module_name: str,
    ) -> ia_cservice_20210806_models.DeleteRegistryModuleResponse:
        """
        @summary 删除RegistryModule
        
        @return: DeleteRegistryModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_registry_module_with_options_async(namespace_name, module_name, headers, runtime)

    def delete_registry_module_version_with_options(
        self,
        namespace_name: str,
        module_name: str,
        version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteRegistryModuleVersionResponse:
        """
        @summary 删除RegistryModule版本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRegistryModuleVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRegistryModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModuleVersion/{OpenApiUtilClient.get_encode_param(namespace_name)}/{OpenApiUtilClient.get_encode_param(module_name)}/{OpenApiUtilClient.get_encode_param(version)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteRegistryModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_registry_module_version_with_options_async(
        self,
        namespace_name: str,
        module_name: str,
        version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteRegistryModuleVersionResponse:
        """
        @summary 删除RegistryModule版本
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRegistryModuleVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRegistryModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModuleVersion/{OpenApiUtilClient.get_encode_param(namespace_name)}/{OpenApiUtilClient.get_encode_param(module_name)}/{OpenApiUtilClient.get_encode_param(version)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteRegistryModuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_registry_module_version(
        self,
        namespace_name: str,
        module_name: str,
        version: str,
    ) -> ia_cservice_20210806_models.DeleteRegistryModuleVersionResponse:
        """
        @summary 删除RegistryModule版本
        
        @return: DeleteRegistryModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_registry_module_version_with_options(namespace_name, module_name, version, headers, runtime)

    async def delete_registry_module_version_async(
        self,
        namespace_name: str,
        module_name: str,
        version: str,
    ) -> ia_cservice_20210806_models.DeleteRegistryModuleVersionResponse:
        """
        @summary 删除RegistryModule版本
        
        @return: DeleteRegistryModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_registry_module_version_with_options_async(namespace_name, module_name, version, headers, runtime)

    def delete_registry_namespace_with_options(
        self,
        namespace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteRegistryNamespaceResponse:
        """
        @summary 删除工作空间
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRegistryNamespaceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRegistryNamespace',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryNamespace/{OpenApiUtilClient.get_encode_param(namespace_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteRegistryNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_registry_namespace_with_options_async(
        self,
        namespace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteRegistryNamespaceResponse:
        """
        @summary 删除工作空间
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteRegistryNamespaceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteRegistryNamespace',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryNamespace/{OpenApiUtilClient.get_encode_param(namespace_name)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteRegistryNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_registry_namespace(
        self,
        namespace_name: str,
    ) -> ia_cservice_20210806_models.DeleteRegistryNamespaceResponse:
        """
        @summary 删除工作空间
        
        @return: DeleteRegistryNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_registry_namespace_with_options(namespace_name, headers, runtime)

    async def delete_registry_namespace_async(
        self,
        namespace_name: str,
    ) -> ia_cservice_20210806_models.DeleteRegistryNamespaceResponse:
        """
        @summary 删除工作空间
        
        @return: DeleteRegistryNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_registry_namespace_with_options_async(namespace_name, headers, runtime)

    def delete_resource_export_task_with_options(
        self,
        export_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteResourceExportTaskResponse:
        """
        @summary 删除资源导出任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceExportTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_export_task_with_options_async(
        self,
        export_task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteResourceExportTaskResponse:
        """
        @summary 删除资源导出任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteResourceExportTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteResourceExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource_export_task(
        self,
        export_task_id: str,
    ) -> ia_cservice_20210806_models.DeleteResourceExportTaskResponse:
        """
        @summary 删除资源导出任务
        
        @return: DeleteResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_resource_export_task_with_options(export_task_id, headers, runtime)

    async def delete_resource_export_task_async(
        self,
        export_task_id: str,
    ) -> ia_cservice_20210806_models.DeleteResourceExportTaskResponse:
        """
        @summary 删除资源导出任务
        
        @return: DeleteResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_resource_export_task_with_options_async(export_task_id, headers, runtime)

    def delete_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteTaskResponse:
        """
        @summary 删除任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DeleteTaskResponse:
        """
        @summary 删除任务
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DeleteTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_task(
        self,
        task_id: str,
    ) -> ia_cservice_20210806_models.DeleteTaskResponse:
        """
        @summary 删除任务
        
        @return: DeleteTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_task_with_options(task_id, headers, runtime)

    async def delete_task_async(
        self,
        task_id: str,
    ) -> ia_cservice_20210806_models.DeleteTaskResponse:
        """
        @summary 删除任务
        
        @return: DeleteTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_task_with_options_async(task_id, headers, runtime)

    def dissociate_group_with_options(
        self,
        project_id: str,
        group_id: str,
        request: ia_cservice_20210806_models.DissociateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DissociateGroupResponse:
        """
        @summary 取消关联分组
        
        @param request: DissociateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DissociateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.resource_ids):
            body['resourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DissociateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}/dissociate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DissociateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def dissociate_group_with_options_async(
        self,
        project_id: str,
        group_id: str,
        request: ia_cservice_20210806_models.DissociateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.DissociateGroupResponse:
        """
        @summary 取消关联分组
        
        @param request: DissociateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DissociateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.resource_ids):
            body['resourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            body['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DissociateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}/dissociate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.DissociateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dissociate_group(
        self,
        project_id: str,
        group_id: str,
        request: ia_cservice_20210806_models.DissociateGroupRequest,
    ) -> ia_cservice_20210806_models.DissociateGroupResponse:
        """
        @summary 取消关联分组
        
        @param request: DissociateGroupRequest
        @return: DissociateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.dissociate_group_with_options(project_id, group_id, request, headers, runtime)

    async def dissociate_group_async(
        self,
        project_id: str,
        group_id: str,
        request: ia_cservice_20210806_models.DissociateGroupRequest,
    ) -> ia_cservice_20210806_models.DissociateGroupResponse:
        """
        @summary 取消关联分组
        
        @param request: DissociateGroupRequest
        @return: DissociateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.dissociate_group_with_options_async(project_id, group_id, request, headers, runtime)

    def execute_registry_module_with_options(
        self,
        namespace_name: str,
        module_name: str,
        request: ia_cservice_20210806_models.ExecuteRegistryModuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ExecuteRegistryModuleResponse:
        """
        @summary 执行RegistryModule
        
        @param request: ExecuteRegistryModuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteRegistryModuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteRegistryModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModule/{OpenApiUtilClient.get_encode_param(namespace_name)}/{OpenApiUtilClient.get_encode_param(module_name)}/execution',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ExecuteRegistryModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_registry_module_with_options_async(
        self,
        namespace_name: str,
        module_name: str,
        request: ia_cservice_20210806_models.ExecuteRegistryModuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ExecuteRegistryModuleResponse:
        """
        @summary 执行RegistryModule
        
        @param request: ExecuteRegistryModuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteRegistryModuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteRegistryModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModule/{OpenApiUtilClient.get_encode_param(namespace_name)}/{OpenApiUtilClient.get_encode_param(module_name)}/execution',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ExecuteRegistryModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_registry_module(
        self,
        namespace_name: str,
        module_name: str,
        request: ia_cservice_20210806_models.ExecuteRegistryModuleRequest,
    ) -> ia_cservice_20210806_models.ExecuteRegistryModuleResponse:
        """
        @summary 执行RegistryModule
        
        @param request: ExecuteRegistryModuleRequest
        @return: ExecuteRegistryModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_registry_module_with_options(namespace_name, module_name, request, headers, runtime)

    async def execute_registry_module_async(
        self,
        namespace_name: str,
        module_name: str,
        request: ia_cservice_20210806_models.ExecuteRegistryModuleRequest,
    ) -> ia_cservice_20210806_models.ExecuteRegistryModuleResponse:
        """
        @summary 执行RegistryModule
        
        @param request: ExecuteRegistryModuleRequest
        @return: ExecuteRegistryModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_registry_module_with_options_async(namespace_name, module_name, request, headers, runtime)

    def execute_resource_export_task_with_options(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ExecuteResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ExecuteResourceExportTaskResponse:
        """
        @summary 执行资源导出任务
        
        @param request: ExecuteResourceExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteResourceExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/execute/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ExecuteResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_resource_export_task_with_options_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ExecuteResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ExecuteResourceExportTaskResponse:
        """
        @summary 执行资源导出任务
        
        @param request: ExecuteResourceExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteResourceExportTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/execute/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ExecuteResourceExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_resource_export_task(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ExecuteResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.ExecuteResourceExportTaskResponse:
        """
        @summary 执行资源导出任务
        
        @param request: ExecuteResourceExportTaskRequest
        @return: ExecuteResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_resource_export_task_with_options(export_task_id, request, headers, runtime)

    async def execute_resource_export_task_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ExecuteResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.ExecuteResourceExportTaskResponse:
        """
        @summary 执行资源导出任务
        
        @param request: ExecuteResourceExportTaskRequest
        @return: ExecuteResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_resource_export_task_with_options_async(export_task_id, request, headers, runtime)

    def execute_terraform_apply_with_options(
        self,
        request: ia_cservice_20210806_models.ExecuteTerraformApplyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ExecuteTerraformApplyResponse:
        """
        @summary 执行TerraformApply
        
        @param request: ExecuteTerraformApplyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTerraformApplyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.state_id):
            body['stateId'] = request.state_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTerraformApply',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/terraform/execution/apply',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ExecuteTerraformApplyResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_terraform_apply_with_options_async(
        self,
        request: ia_cservice_20210806_models.ExecuteTerraformApplyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ExecuteTerraformApplyResponse:
        """
        @summary 执行TerraformApply
        
        @param request: ExecuteTerraformApplyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTerraformApplyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.state_id):
            body['stateId'] = request.state_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTerraformApply',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/terraform/execution/apply',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ExecuteTerraformApplyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_terraform_apply(
        self,
        request: ia_cservice_20210806_models.ExecuteTerraformApplyRequest,
    ) -> ia_cservice_20210806_models.ExecuteTerraformApplyResponse:
        """
        @summary 执行TerraformApply
        
        @param request: ExecuteTerraformApplyRequest
        @return: ExecuteTerraformApplyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_terraform_apply_with_options(request, headers, runtime)

    async def execute_terraform_apply_async(
        self,
        request: ia_cservice_20210806_models.ExecuteTerraformApplyRequest,
    ) -> ia_cservice_20210806_models.ExecuteTerraformApplyResponse:
        """
        @summary 执行TerraformApply
        
        @param request: ExecuteTerraformApplyRequest
        @return: ExecuteTerraformApplyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_terraform_apply_with_options_async(request, headers, runtime)

    def execute_terraform_destroy_with_options(
        self,
        request: ia_cservice_20210806_models.ExecuteTerraformDestroyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ExecuteTerraformDestroyResponse:
        """
        @summary 执行TerraformDestroy
        
        @param request: ExecuteTerraformDestroyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTerraformDestroyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.state_id):
            body['stateId'] = request.state_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTerraformDestroy',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/terraform/execution/destroy',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ExecuteTerraformDestroyResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_terraform_destroy_with_options_async(
        self,
        request: ia_cservice_20210806_models.ExecuteTerraformDestroyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ExecuteTerraformDestroyResponse:
        """
        @summary 执行TerraformDestroy
        
        @param request: ExecuteTerraformDestroyRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTerraformDestroyResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.state_id):
            body['stateId'] = request.state_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTerraformDestroy',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/terraform/execution/destroy',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ExecuteTerraformDestroyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_terraform_destroy(
        self,
        request: ia_cservice_20210806_models.ExecuteTerraformDestroyRequest,
    ) -> ia_cservice_20210806_models.ExecuteTerraformDestroyResponse:
        """
        @summary 执行TerraformDestroy
        
        @param request: ExecuteTerraformDestroyRequest
        @return: ExecuteTerraformDestroyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_terraform_destroy_with_options(request, headers, runtime)

    async def execute_terraform_destroy_async(
        self,
        request: ia_cservice_20210806_models.ExecuteTerraformDestroyRequest,
    ) -> ia_cservice_20210806_models.ExecuteTerraformDestroyResponse:
        """
        @summary 执行TerraformDestroy
        
        @param request: ExecuteTerraformDestroyRequest
        @return: ExecuteTerraformDestroyResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_terraform_destroy_with_options_async(request, headers, runtime)

    def execute_terraform_plan_with_options(
        self,
        request: ia_cservice_20210806_models.ExecuteTerraformPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ExecuteTerraformPlanResponse:
        """
        @summary 执行TerraformPlan
        
        @param request: ExecuteTerraformPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTerraformPlanResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.state_id):
            body['stateId'] = request.state_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTerraformPlan',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/terraform/execution/plan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ExecuteTerraformPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_terraform_plan_with_options_async(
        self,
        request: ia_cservice_20210806_models.ExecuteTerraformPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ExecuteTerraformPlanResponse:
        """
        @summary 执行TerraformPlan
        
        @param request: ExecuteTerraformPlanRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteTerraformPlanResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.state_id):
            body['stateId'] = request.state_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteTerraformPlan',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/terraform/execution/plan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ExecuteTerraformPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_terraform_plan(
        self,
        request: ia_cservice_20210806_models.ExecuteTerraformPlanRequest,
    ) -> ia_cservice_20210806_models.ExecuteTerraformPlanResponse:
        """
        @summary 执行TerraformPlan
        
        @param request: ExecuteTerraformPlanRequest
        @return: ExecuteTerraformPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.execute_terraform_plan_with_options(request, headers, runtime)

    async def execute_terraform_plan_async(
        self,
        request: ia_cservice_20210806_models.ExecuteTerraformPlanRequest,
    ) -> ia_cservice_20210806_models.ExecuteTerraformPlanResponse:
        """
        @summary 执行TerraformPlan
        
        @param request: ExecuteTerraformPlanRequest
        @return: ExecuteTerraformPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.execute_terraform_plan_with_options_async(request, headers, runtime)

    def generate_module_with_options(
        self,
        request: ia_cservice_20210806_models.GenerateModuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GenerateModuleResponse:
        """
        @summary 生成模板
        
        @param request: GenerateModuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateModuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.generate_source):
            body['generateSource'] = request.generate_source
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            body['regionId'] = request.region_id
        if not UtilClient.is_unset(request.syntax):
            body['syntax'] = request.syntax
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.terraform_resource_type):
            body['terraformResourceType'] = request.terraform_resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorer/generate/module',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GenerateModuleResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def generate_module_with_options_async(
        self,
        request: ia_cservice_20210806_models.GenerateModuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GenerateModuleResponse:
        """
        @summary 生成模板
        
        @param request: GenerateModuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateModuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.generate_source):
            body['generateSource'] = request.generate_source
        if not UtilClient.is_unset(request.parameters):
            body['parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            body['regionId'] = request.region_id
        if not UtilClient.is_unset(request.syntax):
            body['syntax'] = request.syntax
        if not UtilClient.is_unset(request.template):
            body['template'] = request.template
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.terraform_resource_type):
            body['terraformResourceType'] = request.terraform_resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorer/generate/module',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GenerateModuleResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def generate_module(
        self,
        request: ia_cservice_20210806_models.GenerateModuleRequest,
    ) -> ia_cservice_20210806_models.GenerateModuleResponse:
        """
        @summary 生成模板
        
        @param request: GenerateModuleRequest
        @return: GenerateModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_module_with_options(request, headers, runtime)

    async def generate_module_async(
        self,
        request: ia_cservice_20210806_models.GenerateModuleRequest,
    ) -> ia_cservice_20210806_models.GenerateModuleResponse:
        """
        @summary 生成模板
        
        @param request: GenerateModuleRequest
        @return: GenerateModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_module_with_options_async(request, headers, runtime)

    def get_execute_state_with_options(
        self,
        state_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetExecuteStateResponse:
        """
        @summary 获取Terraform运行结果
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExecuteStateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetExecuteState',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/terraform/execution/{OpenApiUtilClient.get_encode_param(state_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetExecuteStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_execute_state_with_options_async(
        self,
        state_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetExecuteStateResponse:
        """
        @summary 获取Terraform运行结果
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExecuteStateResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetExecuteState',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/terraform/execution/{OpenApiUtilClient.get_encode_param(state_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetExecuteStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_execute_state(
        self,
        state_id: str,
    ) -> ia_cservice_20210806_models.GetExecuteStateResponse:
        """
        @summary 获取Terraform运行结果
        
        @return: GetExecuteStateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_execute_state_with_options(state_id, headers, runtime)

    async def get_execute_state_async(
        self,
        state_id: str,
    ) -> ia_cservice_20210806_models.GetExecuteStateResponse:
        """
        @summary 获取Terraform运行结果
        
        @return: GetExecuteStateResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_execute_state_with_options_async(state_id, headers, runtime)

    def get_group_with_options(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetGroupResponse:
        """
        @summary 查询分组
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_group_with_options_async(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetGroupResponse:
        """
        @summary 查询分组
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetGroupResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_group(
        self,
        group_id: str,
    ) -> ia_cservice_20210806_models.GetGroupResponse:
        """
        @summary 查询分组
        
        @return: GetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_group_with_options(group_id, headers, runtime)

    async def get_group_async(
        self,
        group_id: str,
    ) -> ia_cservice_20210806_models.GetGroupResponse:
        """
        @summary 查询分组
        
        @return: GetGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_group_with_options_async(group_id, headers, runtime)

    def get_job_with_options(
        self,
        task_id: str,
        job_id: str,
        request: ia_cservice_20210806_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetJobResponse:
        """
        @summary 作业详情
        
        @param request: GetJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_with_options_async(
        self,
        task_id: str,
        job_id: str,
        request: ia_cservice_20210806_models.GetJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetJobResponse:
        """
        @summary 作业详情
        
        @param request: GetJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetJob',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job(
        self,
        task_id: str,
        job_id: str,
        request: ia_cservice_20210806_models.GetJobRequest,
    ) -> ia_cservice_20210806_models.GetJobResponse:
        """
        @summary 作业详情
        
        @param request: GetJobRequest
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_job_with_options(task_id, job_id, request, headers, runtime)

    async def get_job_async(
        self,
        task_id: str,
        job_id: str,
        request: ia_cservice_20210806_models.GetJobRequest,
    ) -> ia_cservice_20210806_models.GetJobResponse:
        """
        @summary 作业详情
        
        @param request: GetJobRequest
        @return: GetJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_job_with_options_async(task_id, job_id, request, headers, runtime)

    def get_module_with_options(
        self,
        module_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetModuleResponse:
        """
        @summary 获取模板详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_module_with_options_async(
        self,
        module_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetModuleResponse:
        """
        @summary 获取模板详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_module(
        self,
        module_id: str,
    ) -> ia_cservice_20210806_models.GetModuleResponse:
        """
        @summary 获取模板详情
        
        @return: GetModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_module_with_options(module_id, headers, runtime)

    async def get_module_async(
        self,
        module_id: str,
    ) -> ia_cservice_20210806_models.GetModuleResponse:
        """
        @summary 获取模板详情
        
        @return: GetModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_module_with_options_async(module_id, headers, runtime)

    def get_module_version_with_options(
        self,
        module_id: str,
        module_version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetModuleVersionResponse:
        """
        @summary 模板版本详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModuleVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}/versions/{OpenApiUtilClient.get_encode_param(module_version)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_module_version_with_options_async(
        self,
        module_id: str,
        module_version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetModuleVersionResponse:
        """
        @summary 模板版本详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetModuleVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}/versions/{OpenApiUtilClient.get_encode_param(module_version)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetModuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_module_version(
        self,
        module_id: str,
        module_version: str,
    ) -> ia_cservice_20210806_models.GetModuleVersionResponse:
        """
        @summary 模板版本详情
        
        @return: GetModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_module_version_with_options(module_id, module_version, headers, runtime)

    async def get_module_version_async(
        self,
        module_id: str,
        module_version: str,
    ) -> ia_cservice_20210806_models.GetModuleVersionResponse:
        """
        @summary 模板版本详情
        
        @return: GetModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_module_version_with_options_async(module_id, module_version, headers, runtime)

    def get_project_with_options(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetProjectResponse:
        """
        @summary 查询项目
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_project_with_options_async(
        self,
        project_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetProjectResponse:
        """
        @summary 查询项目
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetProjectResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_project(
        self,
        project_id: str,
    ) -> ia_cservice_20210806_models.GetProjectResponse:
        """
        @summary 查询项目
        
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_project_with_options(project_id, headers, runtime)

    async def get_project_async(
        self,
        project_id: str,
    ) -> ia_cservice_20210806_models.GetProjectResponse:
        """
        @summary 查询项目
        
        @return: GetProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_project_with_options_async(project_id, headers, runtime)

    def get_registry_module_with_options(
        self,
        namespace_name: str,
        module_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetRegistryModuleResponse:
        """
        @summary 获取RegistryModule信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRegistryModuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRegistryModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModule/{OpenApiUtilClient.get_encode_param(namespace_name)}/{OpenApiUtilClient.get_encode_param(module_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetRegistryModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_registry_module_with_options_async(
        self,
        namespace_name: str,
        module_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetRegistryModuleResponse:
        """
        @summary 获取RegistryModule信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRegistryModuleResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRegistryModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModule/{OpenApiUtilClient.get_encode_param(namespace_name)}/{OpenApiUtilClient.get_encode_param(module_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetRegistryModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_registry_module(
        self,
        namespace_name: str,
        module_name: str,
    ) -> ia_cservice_20210806_models.GetRegistryModuleResponse:
        """
        @summary 获取RegistryModule信息
        
        @return: GetRegistryModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_registry_module_with_options(namespace_name, module_name, headers, runtime)

    async def get_registry_module_async(
        self,
        namespace_name: str,
        module_name: str,
    ) -> ia_cservice_20210806_models.GetRegistryModuleResponse:
        """
        @summary 获取RegistryModule信息
        
        @return: GetRegistryModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_registry_module_with_options_async(namespace_name, module_name, headers, runtime)

    def get_registry_module_version_with_options(
        self,
        namespace_name: str,
        module_name: str,
        version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetRegistryModuleVersionResponse:
        """
        @summary 获取RegistryModule版本信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRegistryModuleVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRegistryModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModuleVersion/{OpenApiUtilClient.get_encode_param(namespace_name)}/{OpenApiUtilClient.get_encode_param(module_name)}/{OpenApiUtilClient.get_encode_param(version)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetRegistryModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_registry_module_version_with_options_async(
        self,
        namespace_name: str,
        module_name: str,
        version: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetRegistryModuleVersionResponse:
        """
        @summary 获取RegistryModule版本信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRegistryModuleVersionResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRegistryModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModuleVersion/{OpenApiUtilClient.get_encode_param(namespace_name)}/{OpenApiUtilClient.get_encode_param(module_name)}/{OpenApiUtilClient.get_encode_param(version)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetRegistryModuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_registry_module_version(
        self,
        namespace_name: str,
        module_name: str,
        version: str,
    ) -> ia_cservice_20210806_models.GetRegistryModuleVersionResponse:
        """
        @summary 获取RegistryModule版本信息
        
        @return: GetRegistryModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_registry_module_version_with_options(namespace_name, module_name, version, headers, runtime)

    async def get_registry_module_version_async(
        self,
        namespace_name: str,
        module_name: str,
        version: str,
    ) -> ia_cservice_20210806_models.GetRegistryModuleVersionResponse:
        """
        @summary 获取RegistryModule版本信息
        
        @return: GetRegistryModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_registry_module_version_with_options_async(namespace_name, module_name, version, headers, runtime)

    def get_registry_namespace_with_options(
        self,
        namespace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetRegistryNamespaceResponse:
        """
        @summary 获取工作空间信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRegistryNamespaceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRegistryNamespace',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryNamespace/{OpenApiUtilClient.get_encode_param(namespace_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetRegistryNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_registry_namespace_with_options_async(
        self,
        namespace_name: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetRegistryNamespaceResponse:
        """
        @summary 获取工作空间信息
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRegistryNamespaceResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetRegistryNamespace',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryNamespace/{OpenApiUtilClient.get_encode_param(namespace_name)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetRegistryNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_registry_namespace(
        self,
        namespace_name: str,
    ) -> ia_cservice_20210806_models.GetRegistryNamespaceResponse:
        """
        @summary 获取工作空间信息
        
        @return: GetRegistryNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_registry_namespace_with_options(namespace_name, headers, runtime)

    async def get_registry_namespace_async(
        self,
        namespace_name: str,
    ) -> ia_cservice_20210806_models.GetRegistryNamespaceResponse:
        """
        @summary 获取工作空间信息
        
        @return: GetRegistryNamespaceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_registry_namespace_with_options_async(namespace_name, headers, runtime)

    def get_resource_export_task_with_options(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.GetResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetResourceExportTaskResponse:
        """
        @summary 查询导出任务详情
        
        @param request: GetResourceExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceExportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_version):
            query['exportVersion'] = request.export_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetResourceExportTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_export_task_with_options_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.GetResourceExportTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetResourceExportTaskResponse:
        """
        @summary 查询导出任务详情
        
        @param request: GetResourceExportTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceExportTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_version):
            query['exportVersion'] = request.export_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceExportTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetResourceExportTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_export_task(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.GetResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.GetResourceExportTaskResponse:
        """
        @summary 查询导出任务详情
        
        @param request: GetResourceExportTaskRequest
        @return: GetResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_export_task_with_options(export_task_id, request, headers, runtime)

    async def get_resource_export_task_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.GetResourceExportTaskRequest,
    ) -> ia_cservice_20210806_models.GetResourceExportTaskResponse:
        """
        @summary 查询导出任务详情
        
        @param request: GetResourceExportTaskRequest
        @return: GetResourceExportTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_export_task_with_options_async(export_task_id, request, headers, runtime)

    def get_resource_type_with_options(
        self,
        resource_type: str,
        request: ia_cservice_20210806_models.GetResourceTypeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetResourceTypeResponse:
        """
        @summary 获取资源类型信息
        
        @param request: GetResourceTypeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.filter_read_only):
            query['filterReadOnly'] = request.filter_read_only
        if not UtilClient.is_unset(request.terraform_provider_version):
            query['terraformProviderVersion'] = request.terraform_provider_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceType',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/resourceType/{OpenApiUtilClient.get_encode_param(resource_type)}',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetResourceTypeResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def get_resource_type_with_options_async(
        self,
        resource_type: str,
        request: ia_cservice_20210806_models.GetResourceTypeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetResourceTypeResponse:
        """
        @summary 获取资源类型信息
        
        @param request: GetResourceTypeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.filter_read_only):
            query['filterReadOnly'] = request.filter_read_only
        if not UtilClient.is_unset(request.terraform_provider_version):
            query['terraformProviderVersion'] = request.terraform_provider_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceType',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/resourceType/{OpenApiUtilClient.get_encode_param(resource_type)}',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetResourceTypeResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def get_resource_type(
        self,
        resource_type: str,
        request: ia_cservice_20210806_models.GetResourceTypeRequest,
    ) -> ia_cservice_20210806_models.GetResourceTypeResponse:
        """
        @summary 获取资源类型信息
        
        @param request: GetResourceTypeRequest
        @return: GetResourceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_type_with_options(resource_type, request, headers, runtime)

    async def get_resource_type_async(
        self,
        resource_type: str,
        request: ia_cservice_20210806_models.GetResourceTypeRequest,
    ) -> ia_cservice_20210806_models.GetResourceTypeResponse:
        """
        @summary 获取资源类型信息
        
        @param request: GetResourceTypeRequest
        @return: GetResourceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_type_with_options_async(resource_type, request, headers, runtime)

    def get_task_with_options(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetTaskResponse:
        """
        @summary 查询任务详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        task_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.GetTaskResponse:
        """
        @summary 查询任务详情
        
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTaskResponse
        """
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='GetTask',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        task_id: str,
    ) -> ia_cservice_20210806_models.GetTaskResponse:
        """
        @summary 查询任务详情
        
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_task_with_options(task_id, headers, runtime)

    async def get_task_async(
        self,
        task_id: str,
    ) -> ia_cservice_20210806_models.GetTaskResponse:
        """
        @summary 查询任务详情
        
        @return: GetTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_task_with_options_async(task_id, headers, runtime)

    def list_explorer_registry_module_examples_with_options(
        self,
        request: ia_cservice_20210806_models.ListExplorerRegistryModuleExamplesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListExplorerRegistryModuleExamplesResponse:
        """
        @summary 获取Explorer的egistryModule版本示例列表
        
        @param request: ListExplorerRegistryModuleExamplesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExplorerRegistryModuleExamplesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.example_name):
            query['exampleName'] = request.example_name
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.module_name):
            query['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.module_version):
            query['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.namespace_name):
            query['namespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExplorerRegistryModuleExamples',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorerRegistryModule/example',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListExplorerRegistryModuleExamplesResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_explorer_registry_module_examples_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListExplorerRegistryModuleExamplesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListExplorerRegistryModuleExamplesResponse:
        """
        @summary 获取Explorer的egistryModule版本示例列表
        
        @param request: ListExplorerRegistryModuleExamplesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExplorerRegistryModuleExamplesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.example_name):
            query['exampleName'] = request.example_name
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.module_name):
            query['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.module_version):
            query['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.namespace_name):
            query['namespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExplorerRegistryModuleExamples',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorerRegistryModule/example',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListExplorerRegistryModuleExamplesResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_explorer_registry_module_examples(
        self,
        request: ia_cservice_20210806_models.ListExplorerRegistryModuleExamplesRequest,
    ) -> ia_cservice_20210806_models.ListExplorerRegistryModuleExamplesResponse:
        """
        @summary 获取Explorer的egistryModule版本示例列表
        
        @param request: ListExplorerRegistryModuleExamplesRequest
        @return: ListExplorerRegistryModuleExamplesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_explorer_registry_module_examples_with_options(request, headers, runtime)

    async def list_explorer_registry_module_examples_async(
        self,
        request: ia_cservice_20210806_models.ListExplorerRegistryModuleExamplesRequest,
    ) -> ia_cservice_20210806_models.ListExplorerRegistryModuleExamplesResponse:
        """
        @summary 获取Explorer的egistryModule版本示例列表
        
        @param request: ListExplorerRegistryModuleExamplesRequest
        @return: ListExplorerRegistryModuleExamplesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_explorer_registry_module_examples_with_options_async(request, headers, runtime)

    def list_explorer_registry_module_versions_with_options(
        self,
        request: ia_cservice_20210806_models.ListExplorerRegistryModuleVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListExplorerRegistryModuleVersionsResponse:
        """
        @summary 获取Explorer的egistryModule版本列表
        
        @param request: ListExplorerRegistryModuleVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExplorerRegistryModuleVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.module_name):
            query['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.module_version):
            query['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.namespace_name):
            query['namespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExplorerRegistryModuleVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorerRegistryModule/version',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListExplorerRegistryModuleVersionsResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_explorer_registry_module_versions_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListExplorerRegistryModuleVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListExplorerRegistryModuleVersionsResponse:
        """
        @summary 获取Explorer的egistryModule版本列表
        
        @param request: ListExplorerRegistryModuleVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExplorerRegistryModuleVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.module_name):
            query['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.module_version):
            query['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.namespace_name):
            query['namespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExplorerRegistryModuleVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorerRegistryModule/version',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListExplorerRegistryModuleVersionsResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_explorer_registry_module_versions(
        self,
        request: ia_cservice_20210806_models.ListExplorerRegistryModuleVersionsRequest,
    ) -> ia_cservice_20210806_models.ListExplorerRegistryModuleVersionsResponse:
        """
        @summary 获取Explorer的egistryModule版本列表
        
        @param request: ListExplorerRegistryModuleVersionsRequest
        @return: ListExplorerRegistryModuleVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_explorer_registry_module_versions_with_options(request, headers, runtime)

    async def list_explorer_registry_module_versions_async(
        self,
        request: ia_cservice_20210806_models.ListExplorerRegistryModuleVersionsRequest,
    ) -> ia_cservice_20210806_models.ListExplorerRegistryModuleVersionsResponse:
        """
        @summary 获取Explorer的egistryModule版本列表
        
        @param request: ListExplorerRegistryModuleVersionsRequest
        @return: ListExplorerRegistryModuleVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_explorer_registry_module_versions_with_options_async(request, headers, runtime)

    def list_explorer_registry_modules_with_options(
        self,
        request: ia_cservice_20210806_models.ListExplorerRegistryModulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListExplorerRegistryModulesResponse:
        """
        @summary 获取Explorer的Registry Module列表
        
        @param request: ListExplorerRegistryModulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExplorerRegistryModulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.module_name):
            query['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExplorerRegistryModules',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorerRegistryModule',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListExplorerRegistryModulesResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_explorer_registry_modules_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListExplorerRegistryModulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListExplorerRegistryModulesResponse:
        """
        @summary 获取Explorer的Registry Module列表
        
        @param request: ListExplorerRegistryModulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExplorerRegistryModulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.module_name):
            query['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExplorerRegistryModules',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorerRegistryModule',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListExplorerRegistryModulesResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_explorer_registry_modules(
        self,
        request: ia_cservice_20210806_models.ListExplorerRegistryModulesRequest,
    ) -> ia_cservice_20210806_models.ListExplorerRegistryModulesResponse:
        """
        @summary 获取Explorer的Registry Module列表
        
        @param request: ListExplorerRegistryModulesRequest
        @return: ListExplorerRegistryModulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_explorer_registry_modules_with_options(request, headers, runtime)

    async def list_explorer_registry_modules_async(
        self,
        request: ia_cservice_20210806_models.ListExplorerRegistryModulesRequest,
    ) -> ia_cservice_20210806_models.ListExplorerRegistryModulesResponse:
        """
        @summary 获取Explorer的Registry Module列表
        
        @param request: ListExplorerRegistryModulesRequest
        @return: ListExplorerRegistryModulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_explorer_registry_modules_with_options_async(request, headers, runtime)

    def list_group_with_options(
        self,
        tmp_req: ia_cservice_20210806_models.ListGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListGroupResponse:
        """
        @summary 查询分组列表
        
        @param tmp_req: ListGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_group_with_options_async(
        self,
        tmp_req: ia_cservice_20210806_models.ListGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListGroupResponse:
        """
        @summary 查询分组列表
        
        @param tmp_req: ListGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_group(
        self,
        request: ia_cservice_20210806_models.ListGroupRequest,
    ) -> ia_cservice_20210806_models.ListGroupResponse:
        """
        @summary 查询分组列表
        
        @param request: ListGroupRequest
        @return: ListGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_group_with_options(request, headers, runtime)

    async def list_group_async(
        self,
        request: ia_cservice_20210806_models.ListGroupRequest,
    ) -> ia_cservice_20210806_models.ListGroupResponse:
        """
        @summary 查询分组列表
        
        @param request: ListGroupRequest
        @return: ListGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_group_with_options_async(request, headers, runtime)

    def list_jobs_with_options(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListJobsResponse:
        """
        @summary 作业列表
        
        @param request: ListJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.ListJobsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListJobsResponse:
        """
        @summary 作业列表
        
        @param request: ListJobsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/jobs',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_jobs(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.ListJobsRequest,
    ) -> ia_cservice_20210806_models.ListJobsResponse:
        """
        @summary 作业列表
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_jobs_with_options(task_id, request, headers, runtime)

    async def list_jobs_async(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.ListJobsRequest,
    ) -> ia_cservice_20210806_models.ListJobsResponse:
        """
        @summary 作业列表
        
        @param request: ListJobsRequest
        @return: ListJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_jobs_with_options_async(task_id, request, headers, runtime)

    def list_module_version_with_options(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.ListModuleVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListModuleVersionResponse:
        """
        @summary 模板版本列表
        
        @param request: ListModuleVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModuleVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_module_version_with_options_async(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.ListModuleVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListModuleVersionResponse:
        """
        @summary 模板版本列表
        
        @param request: ListModuleVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModuleVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}/versions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListModuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_module_version(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.ListModuleVersionRequest,
    ) -> ia_cservice_20210806_models.ListModuleVersionResponse:
        """
        @summary 模板版本列表
        
        @param request: ListModuleVersionRequest
        @return: ListModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_module_version_with_options(module_id, request, headers, runtime)

    async def list_module_version_async(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.ListModuleVersionRequest,
    ) -> ia_cservice_20210806_models.ListModuleVersionResponse:
        """
        @summary 模板版本列表
        
        @param request: ListModuleVersionRequest
        @return: ListModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_module_version_with_options_async(module_id, request, headers, runtime)

    def list_modules_with_options(
        self,
        tmp_req: ia_cservice_20210806_models.ListModulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListModulesResponse:
        """
        @summary 列举模板
        
        @param tmp_req: ListModulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListModulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.module_name):
            query['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModules',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListModulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_modules_with_options_async(
        self,
        tmp_req: ia_cservice_20210806_models.ListModulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListModulesResponse:
        """
        @summary 列举模板
        
        @param tmp_req: ListModulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListModulesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListModulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.module_name):
            query['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListModules',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListModulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_modules(
        self,
        request: ia_cservice_20210806_models.ListModulesRequest,
    ) -> ia_cservice_20210806_models.ListModulesResponse:
        """
        @summary 列举模板
        
        @param request: ListModulesRequest
        @return: ListModulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_modules_with_options(request, headers, runtime)

    async def list_modules_async(
        self,
        request: ia_cservice_20210806_models.ListModulesRequest,
    ) -> ia_cservice_20210806_models.ListModulesResponse:
        """
        @summary 列举模板
        
        @param request: ListModulesRequest
        @return: ListModulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_modules_with_options_async(request, headers, runtime)

    def list_products_with_options(
        self,
        request: ia_cservice_20210806_models.ListProductsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListProductsResponse:
        """
        @summary 所有产品列表
        
        @param request: ListProductsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.support_terraformer):
            query['supportTerraformer'] = request.support_terraformer
        if not UtilClient.is_unset(request.terraform_provider_version):
            query['terraformProviderVersion'] = request.terraform_provider_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/products',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListProductsResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_products_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListProductsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListProductsResponse:
        """
        @summary 所有产品列表
        
        @param request: ListProductsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProductsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.support_terraformer):
            query['supportTerraformer'] = request.support_terraformer
        if not UtilClient.is_unset(request.terraform_provider_version):
            query['terraformProviderVersion'] = request.terraform_provider_version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProducts',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/products',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListProductsResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_products(
        self,
        request: ia_cservice_20210806_models.ListProductsRequest,
    ) -> ia_cservice_20210806_models.ListProductsResponse:
        """
        @summary 所有产品列表
        
        @param request: ListProductsRequest
        @return: ListProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_products_with_options(request, headers, runtime)

    async def list_products_async(
        self,
        request: ia_cservice_20210806_models.ListProductsRequest,
    ) -> ia_cservice_20210806_models.ListProductsResponse:
        """
        @summary 所有产品列表
        
        @param request: ListProductsRequest
        @return: ListProductsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_products_with_options_async(request, headers, runtime)

    def list_project_with_options(
        self,
        tmp_req: ia_cservice_20210806_models.ListProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListProjectResponse:
        """
        @summary 查询项目列表
        
        @param tmp_req: ListProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_project_with_options_async(
        self,
        tmp_req: ia_cservice_20210806_models.ListProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListProjectResponse:
        """
        @summary 查询项目列表
        
        @param tmp_req: ListProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListProjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_project(
        self,
        request: ia_cservice_20210806_models.ListProjectRequest,
    ) -> ia_cservice_20210806_models.ListProjectResponse:
        """
        @summary 查询项目列表
        
        @param request: ListProjectRequest
        @return: ListProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_project_with_options(request, headers, runtime)

    async def list_project_async(
        self,
        request: ia_cservice_20210806_models.ListProjectRequest,
    ) -> ia_cservice_20210806_models.ListProjectResponse:
        """
        @summary 查询项目列表
        
        @param request: ListProjectRequest
        @return: ListProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_project_with_options_async(request, headers, runtime)

    def list_registry_module_versions_with_options(
        self,
        request: ia_cservice_20210806_models.ListRegistryModuleVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListRegistryModuleVersionsResponse:
        """
        @summary 获取RegistryModule版本列表
        
        @param request: ListRegistryModuleVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegistryModuleVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.module_name):
            query['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.namespace_name):
            query['namespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegistryModuleVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModuleVersion',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListRegistryModuleVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_registry_module_versions_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListRegistryModuleVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListRegistryModuleVersionsResponse:
        """
        @summary 获取RegistryModule版本列表
        
        @param request: ListRegistryModuleVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegistryModuleVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.module_name):
            query['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.namespace_name):
            query['namespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegistryModuleVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModuleVersion',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListRegistryModuleVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_registry_module_versions(
        self,
        request: ia_cservice_20210806_models.ListRegistryModuleVersionsRequest,
    ) -> ia_cservice_20210806_models.ListRegistryModuleVersionsResponse:
        """
        @summary 获取RegistryModule版本列表
        
        @param request: ListRegistryModuleVersionsRequest
        @return: ListRegistryModuleVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_registry_module_versions_with_options(request, headers, runtime)

    async def list_registry_module_versions_async(
        self,
        request: ia_cservice_20210806_models.ListRegistryModuleVersionsRequest,
    ) -> ia_cservice_20210806_models.ListRegistryModuleVersionsResponse:
        """
        @summary 获取RegistryModule版本列表
        
        @param request: ListRegistryModuleVersionsRequest
        @return: ListRegistryModuleVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_registry_module_versions_with_options_async(request, headers, runtime)

    def list_registry_modules_with_options(
        self,
        request: ia_cservice_20210806_models.ListRegistryModulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListRegistryModulesResponse:
        """
        @summary 获取RegistryModule列表
        
        @param request: ListRegistryModulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegistryModulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.namespace_name):
            query['namespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegistryModules',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListRegistryModulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_registry_modules_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListRegistryModulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListRegistryModulesResponse:
        """
        @summary 获取RegistryModule列表
        
        @param request: ListRegistryModulesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegistryModulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.namespace_name):
            query['namespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegistryModules',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModules',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListRegistryModulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_registry_modules(
        self,
        request: ia_cservice_20210806_models.ListRegistryModulesRequest,
    ) -> ia_cservice_20210806_models.ListRegistryModulesResponse:
        """
        @summary 获取RegistryModule列表
        
        @param request: ListRegistryModulesRequest
        @return: ListRegistryModulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_registry_modules_with_options(request, headers, runtime)

    async def list_registry_modules_async(
        self,
        request: ia_cservice_20210806_models.ListRegistryModulesRequest,
    ) -> ia_cservice_20210806_models.ListRegistryModulesResponse:
        """
        @summary 获取RegistryModule列表
        
        @param request: ListRegistryModulesRequest
        @return: ListRegistryModulesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_registry_modules_with_options_async(request, headers, runtime)

    def list_registry_namespaces_with_options(
        self,
        request: ia_cservice_20210806_models.ListRegistryNamespacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListRegistryNamespacesResponse:
        """
        @summary 获取工作空间列表
        
        @param request: ListRegistryNamespacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegistryNamespacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegistryNamespaces',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryNamespace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListRegistryNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_registry_namespaces_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListRegistryNamespacesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListRegistryNamespacesResponse:
        """
        @summary 获取工作空间列表
        
        @param request: ListRegistryNamespacesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRegistryNamespacesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRegistryNamespaces',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryNamespace',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListRegistryNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_registry_namespaces(
        self,
        request: ia_cservice_20210806_models.ListRegistryNamespacesRequest,
    ) -> ia_cservice_20210806_models.ListRegistryNamespacesResponse:
        """
        @summary 获取工作空间列表
        
        @param request: ListRegistryNamespacesRequest
        @return: ListRegistryNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_registry_namespaces_with_options(request, headers, runtime)

    async def list_registry_namespaces_async(
        self,
        request: ia_cservice_20210806_models.ListRegistryNamespacesRequest,
    ) -> ia_cservice_20210806_models.ListRegistryNamespacesResponse:
        """
        @summary 获取工作空间列表
        
        @param request: ListRegistryNamespacesRequest
        @return: ListRegistryNamespacesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_registry_namespaces_with_options_async(request, headers, runtime)

    def list_resource_export_task_versions_with_options(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ListResourceExportTaskVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListResourceExportTaskVersionsResponse:
        """
        @summary 获取任务版本列表
        
        @param request: ListResourceExportTaskVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceExportTaskVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_version):
            query['exportVersion'] = request.export_version
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceExportTaskVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}/exportVersions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListResourceExportTaskVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_export_task_versions_with_options_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ListResourceExportTaskVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListResourceExportTaskVersionsResponse:
        """
        @summary 获取任务版本列表
        
        @param request: ListResourceExportTaskVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceExportTaskVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_version):
            query['exportVersion'] = request.export_version
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceExportTaskVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}/exportVersions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListResourceExportTaskVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_export_task_versions(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ListResourceExportTaskVersionsRequest,
    ) -> ia_cservice_20210806_models.ListResourceExportTaskVersionsResponse:
        """
        @summary 获取任务版本列表
        
        @param request: ListResourceExportTaskVersionsRequest
        @return: ListResourceExportTaskVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_export_task_versions_with_options(export_task_id, request, headers, runtime)

    async def list_resource_export_task_versions_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.ListResourceExportTaskVersionsRequest,
    ) -> ia_cservice_20210806_models.ListResourceExportTaskVersionsResponse:
        """
        @summary 获取任务版本列表
        
        @param request: ListResourceExportTaskVersionsRequest
        @return: ListResourceExportTaskVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_export_task_versions_with_options_async(export_task_id, request, headers, runtime)

    def list_resource_export_tasks_with_options(
        self,
        request: ia_cservice_20210806_models.ListResourceExportTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListResourceExportTasksResponse:
        """
        @summary 查询导出任务列表
        
        @param request: ListResourceExportTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceExportTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_task_id):
            query['exportTaskId'] = request.export_task_id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceExportTasks',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListResourceExportTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_export_tasks_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListResourceExportTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListResourceExportTasksResponse:
        """
        @summary 查询导出任务列表
        
        @param request: ListResourceExportTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceExportTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.export_task_id):
            query['exportTaskId'] = request.export_task_id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceExportTasks',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListResourceExportTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_export_tasks(
        self,
        request: ia_cservice_20210806_models.ListResourceExportTasksRequest,
    ) -> ia_cservice_20210806_models.ListResourceExportTasksResponse:
        """
        @summary 查询导出任务列表
        
        @param request: ListResourceExportTasksRequest
        @return: ListResourceExportTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_export_tasks_with_options(request, headers, runtime)

    async def list_resource_export_tasks_async(
        self,
        request: ia_cservice_20210806_models.ListResourceExportTasksRequest,
    ) -> ia_cservice_20210806_models.ListResourceExportTasksResponse:
        """
        @summary 查询导出任务列表
        
        @param request: ListResourceExportTasksRequest
        @return: ListResourceExportTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_export_tasks_with_options_async(request, headers, runtime)

    def list_resource_types_with_options(
        self,
        tmp_req: ia_cservice_20210806_models.ListResourceTypesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListResourceTypesResponse:
        """
        @summary 资源类型列表
        
        @param tmp_req: ListResourceTypesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceTypesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListResourceTypesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.terraform_resource_types):
            request.terraform_resource_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.terraform_resource_types, 'terraformResourceTypes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.subcategory):
            query['subcategory'] = request.subcategory
        if not UtilClient.is_unset(request.support_terraformer):
            query['supportTerraformer'] = request.support_terraformer
        if not UtilClient.is_unset(request.terraform_provider_version):
            query['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.terraform_resource_types_shrink):
            query['terraformResourceTypes'] = request.terraform_resource_types_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypes',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/resourceTypes',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListResourceTypesResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_resource_types_with_options_async(
        self,
        tmp_req: ia_cservice_20210806_models.ListResourceTypesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListResourceTypesResponse:
        """
        @summary 资源类型列表
        
        @param tmp_req: ListResourceTypesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceTypesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListResourceTypesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.terraform_resource_types):
            request.terraform_resource_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.terraform_resource_types, 'terraformResourceTypes', 'simple')
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['acceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.product):
            query['product'] = request.product
        if not UtilClient.is_unset(request.sort):
            query['sort'] = request.sort
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.subcategory):
            query['subcategory'] = request.subcategory
        if not UtilClient.is_unset(request.support_terraformer):
            query['supportTerraformer'] = request.support_terraformer
        if not UtilClient.is_unset(request.terraform_provider_version):
            query['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.terraform_resource_types_shrink):
            query['terraformResourceTypes'] = request.terraform_resource_types_shrink
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypes',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/resourceTypes',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListResourceTypesResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_resource_types(
        self,
        request: ia_cservice_20210806_models.ListResourceTypesRequest,
    ) -> ia_cservice_20210806_models.ListResourceTypesResponse:
        """
        @summary 资源类型列表
        
        @param request: ListResourceTypesRequest
        @return: ListResourceTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_types_with_options(request, headers, runtime)

    async def list_resource_types_async(
        self,
        request: ia_cservice_20210806_models.ListResourceTypesRequest,
    ) -> ia_cservice_20210806_models.ListResourceTypesResponse:
        """
        @summary 资源类型列表
        
        @param request: ListResourceTypesRequest
        @return: ListResourceTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_types_with_options_async(request, headers, runtime)

    def list_tasks_with_options(
        self,
        tmp_req: ia_cservice_20210806_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListTasksResponse:
        """
        @summary 任务列表
        
        @param tmp_req: ListTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.module_id):
            query['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        tmp_req: ia_cservice_20210806_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListTasksResponse:
        """
        @summary 任务列表
        
        @param tmp_req: ListTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.ListTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['groupId'] = request.group_id
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.module_id):
            query['moduleId'] = request.module_id
        if not UtilClient.is_unset(request.page_number):
            query['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['projectId'] = request.project_id
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.tag_shrink):
            query['tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.task_id):
            query['taskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        request: ia_cservice_20210806_models.ListTasksRequest,
    ) -> ia_cservice_20210806_models.ListTasksResponse:
        """
        @summary 任务列表
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(request, headers, runtime)

    async def list_tasks_async(
        self,
        request: ia_cservice_20210806_models.ListTasksRequest,
    ) -> ia_cservice_20210806_models.ListTasksResponse:
        """
        @summary 任务列表
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tasks_with_options_async(request, headers, runtime)

    def list_terraform_provider_versions_with_options(
        self,
        request: ia_cservice_20210806_models.ListTerraformProviderVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListTerraformProviderVersionsResponse:
        """
        @summary terraformProvider版本
        
        @param request: ListTerraformProviderVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTerraformProviderVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.usage):
            query['usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTerraformProviderVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/version/terraform/provider',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListTerraformProviderVersionsResponse(),
            self.do_roarequest(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    async def list_terraform_provider_versions_with_options_async(
        self,
        request: ia_cservice_20210806_models.ListTerraformProviderVersionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ListTerraformProviderVersionsResponse:
        """
        @summary terraformProvider版本
        
        @param request: ListTerraformProviderVersionsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTerraformProviderVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['keyword'] = request.keyword
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.usage):
            query['usage'] = request.usage
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTerraformProviderVersions',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/version/terraform/provider',
            method='GET',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ListTerraformProviderVersionsResponse(),
            await self.do_roarequest_async(params.action, params.version, params.protocol, params.method, params.auth_type, params.pathname, params.body_type, req, runtime)
        )

    def list_terraform_provider_versions(
        self,
        request: ia_cservice_20210806_models.ListTerraformProviderVersionsRequest,
    ) -> ia_cservice_20210806_models.ListTerraformProviderVersionsResponse:
        """
        @summary terraformProvider版本
        
        @param request: ListTerraformProviderVersionsRequest
        @return: ListTerraformProviderVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_terraform_provider_versions_with_options(request, headers, runtime)

    async def list_terraform_provider_versions_async(
        self,
        request: ia_cservice_20210806_models.ListTerraformProviderVersionsRequest,
    ) -> ia_cservice_20210806_models.ListTerraformProviderVersionsResponse:
        """
        @summary terraformProvider版本
        
        @param request: ListTerraformProviderVersionsRequest
        @return: ListTerraformProviderVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_terraform_provider_versions_with_options_async(request, headers, runtime)

    def operate_job_with_options(
        self,
        task_id: str,
        job_id: str,
        operation_type: str,
        request: ia_cservice_20210806_models.OperateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.OperateJobResponse:
        """
        @summary 控制作业
        
        @param request: OperateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['comment'] = request.comment
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateJob',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/operation/{OpenApiUtilClient.get_encode_param(operation_type)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.OperateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def operate_job_with_options_async(
        self,
        task_id: str,
        job_id: str,
        operation_type: str,
        request: ia_cservice_20210806_models.OperateJobRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.OperateJobResponse:
        """
        @summary 控制作业
        
        @param request: OperateJobRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['comment'] = request.comment
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateJob',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}/jobs/{OpenApiUtilClient.get_encode_param(job_id)}/operation/{OpenApiUtilClient.get_encode_param(operation_type)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.OperateJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def operate_job(
        self,
        task_id: str,
        job_id: str,
        operation_type: str,
        request: ia_cservice_20210806_models.OperateJobRequest,
    ) -> ia_cservice_20210806_models.OperateJobResponse:
        """
        @summary 控制作业
        
        @param request: OperateJobRequest
        @return: OperateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.operate_job_with_options(task_id, job_id, operation_type, request, headers, runtime)

    async def operate_job_async(
        self,
        task_id: str,
        job_id: str,
        operation_type: str,
        request: ia_cservice_20210806_models.OperateJobRequest,
    ) -> ia_cservice_20210806_models.OperateJobResponse:
        """
        @summary 控制作业
        
        @param request: OperateJobRequest
        @return: OperateJobResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.operate_job_with_options_async(task_id, job_id, operation_type, request, headers, runtime)

    def publish_registry_module_version_with_options(
        self,
        request: ia_cservice_20210806_models.PublishRegistryModuleVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.PublishRegistryModuleVersionResponse:
        """
        @summary 发布RegistryModule版本
        
        @param request: PublishRegistryModuleVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishRegistryModuleVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.module_name):
            body['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.namespace_name):
            body['namespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishRegistryModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModuleVersion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.PublishRegistryModuleVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def publish_registry_module_version_with_options_async(
        self,
        request: ia_cservice_20210806_models.PublishRegistryModuleVersionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.PublishRegistryModuleVersionResponse:
        """
        @summary 发布RegistryModule版本
        
        @param request: PublishRegistryModuleVersionRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: PublishRegistryModuleVersionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.module_name):
            body['moduleName'] = request.module_name
        if not UtilClient.is_unset(request.namespace_name):
            body['namespaceName'] = request.namespace_name
        if not UtilClient.is_unset(request.version):
            body['version'] = request.version
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishRegistryModuleVersion',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModuleVersion',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.PublishRegistryModuleVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def publish_registry_module_version(
        self,
        request: ia_cservice_20210806_models.PublishRegistryModuleVersionRequest,
    ) -> ia_cservice_20210806_models.PublishRegistryModuleVersionResponse:
        """
        @summary 发布RegistryModule版本
        
        @param request: PublishRegistryModuleVersionRequest
        @return: PublishRegistryModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.publish_registry_module_version_with_options(request, headers, runtime)

    async def publish_registry_module_version_async(
        self,
        request: ia_cservice_20210806_models.PublishRegistryModuleVersionRequest,
    ) -> ia_cservice_20210806_models.PublishRegistryModuleVersionResponse:
        """
        @summary 发布RegistryModule版本
        
        @param request: PublishRegistryModuleVersionRequest
        @return: PublishRegistryModuleVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.publish_registry_module_version_with_options_async(request, headers, runtime)

    def remove_shared_accounts_with_options(
        self,
        tmp_req: ia_cservice_20210806_models.RemoveSharedAccountsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.RemoveSharedAccountsResponse:
        """
        @summary 删除共享账号信息
        
        @param tmp_req: RemoveSharedAccountsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveSharedAccountsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.RemoveSharedAccountsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'accountIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['accountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSharedAccounts',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/sharedAccounts',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.RemoveSharedAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_shared_accounts_with_options_async(
        self,
        tmp_req: ia_cservice_20210806_models.RemoveSharedAccountsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.RemoveSharedAccountsResponse:
        """
        @summary 删除共享账号信息
        
        @param tmp_req: RemoveSharedAccountsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveSharedAccountsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ia_cservice_20210806_models.RemoveSharedAccountsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'accountIds', 'simple')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['accountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.resource_id):
            query['resourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['resourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSharedAccounts',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/sharedAccounts',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.RemoveSharedAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_shared_accounts(
        self,
        request: ia_cservice_20210806_models.RemoveSharedAccountsRequest,
    ) -> ia_cservice_20210806_models.RemoveSharedAccountsResponse:
        """
        @summary 删除共享账号信息
        
        @param request: RemoveSharedAccountsRequest
        @return: RemoveSharedAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_shared_accounts_with_options(request, headers, runtime)

    async def remove_shared_accounts_async(
        self,
        request: ia_cservice_20210806_models.RemoveSharedAccountsRequest,
    ) -> ia_cservice_20210806_models.RemoveSharedAccountsResponse:
        """
        @summary 删除共享账号信息
        
        @param request: RemoveSharedAccountsRequest
        @return: RemoveSharedAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_shared_accounts_with_options_async(request, headers, runtime)

    def update_explorer_module_attribute_with_options(
        self,
        explorer_module_id: str,
        request: ia_cservice_20210806_models.UpdateExplorerModuleAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateExplorerModuleAttributeResponse:
        """
        @summary 修改ExplorerModule
        
        @param request: UpdateExplorerModuleAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExplorerModuleAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExplorerModuleAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorerModule/{OpenApiUtilClient.get_encode_param(explorer_module_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateExplorerModuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_explorer_module_attribute_with_options_async(
        self,
        explorer_module_id: str,
        request: ia_cservice_20210806_models.UpdateExplorerModuleAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateExplorerModuleAttributeResponse:
        """
        @summary 修改ExplorerModule
        
        @param request: UpdateExplorerModuleAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExplorerModuleAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExplorerModuleAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/explorerModule/{OpenApiUtilClient.get_encode_param(explorer_module_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateExplorerModuleAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_explorer_module_attribute(
        self,
        explorer_module_id: str,
        request: ia_cservice_20210806_models.UpdateExplorerModuleAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateExplorerModuleAttributeResponse:
        """
        @summary 修改ExplorerModule
        
        @param request: UpdateExplorerModuleAttributeRequest
        @return: UpdateExplorerModuleAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_explorer_module_attribute_with_options(explorer_module_id, request, headers, runtime)

    async def update_explorer_module_attribute_async(
        self,
        explorer_module_id: str,
        request: ia_cservice_20210806_models.UpdateExplorerModuleAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateExplorerModuleAttributeResponse:
        """
        @summary 修改ExplorerModule
        
        @param request: UpdateExplorerModuleAttributeRequest
        @return: UpdateExplorerModuleAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_explorer_module_attribute_with_options_async(explorer_module_id, request, headers, runtime)

    def update_group_with_options(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.UpdateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateGroupResponse:
        """
        @summary 修改分组
        
        @param request: UpdateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.auto_trigger):
            body['autoTrigger'] = request.auto_trigger
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.forced_setting):
            body['forcedSetting'] = request.forced_setting
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.notify_config):
            body['notifyConfig'] = request.notify_config
        if not UtilClient.is_unset(request.notify_operation_types):
            body['notifyOperationTypes'] = request.notify_operation_types
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.report_export_field):
            body['reportExportField'] = request.report_export_field
        if not UtilClient.is_unset(request.report_export_path):
            body['reportExportPath'] = request.report_export_path
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.trigger_resource_type):
            body['triggerResourceType'] = request.trigger_resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_group_with_options_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.UpdateGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateGroupResponse:
        """
        @summary 修改分组
        
        @param request: UpdateGroupRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.auto_trigger):
            body['autoTrigger'] = request.auto_trigger
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.forced_setting):
            body['forcedSetting'] = request.forced_setting
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.notify_config):
            body['notifyConfig'] = request.notify_config
        if not UtilClient.is_unset(request.notify_operation_types):
            body['notifyOperationTypes'] = request.notify_operation_types
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.report_export_field):
            body['reportExportField'] = request.report_export_field
        if not UtilClient.is_unset(request.report_export_path):
            body['reportExportPath'] = request.report_export_path
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.trigger_config):
            body['triggerConfig'] = request.trigger_config
        if not UtilClient.is_unset(request.trigger_resource_type):
            body['triggerResourceType'] = request.trigger_resource_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateGroup',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/group/{OpenApiUtilClient.get_encode_param(group_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_group(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.UpdateGroupRequest,
    ) -> ia_cservice_20210806_models.UpdateGroupResponse:
        """
        @summary 修改分组
        
        @param request: UpdateGroupRequest
        @return: UpdateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_group_with_options(group_id, request, headers, runtime)

    async def update_group_async(
        self,
        group_id: str,
        request: ia_cservice_20210806_models.UpdateGroupRequest,
    ) -> ia_cservice_20210806_models.UpdateGroupResponse:
        """
        @summary 修改分组
        
        @param request: UpdateGroupRequest
        @return: UpdateGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_group_with_options_async(group_id, request, headers, runtime)

    def update_module_attribute_with_options(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.UpdateModuleAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateModuleAttributeResponse:
        """
        @summary 更新模板
        
        @param request: UpdateModuleAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModuleAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.source_path):
            body['sourcePath'] = request.source_path
        if not UtilClient.is_unset(request.state_path):
            body['statePath'] = request.state_path
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.version_strategy):
            body['versionStrategy'] = request.version_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModuleAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateModuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_module_attribute_with_options_async(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.UpdateModuleAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateModuleAttributeResponse:
        """
        @summary 更新模板
        
        @param request: UpdateModuleAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateModuleAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.source_path):
            body['sourcePath'] = request.source_path
        if not UtilClient.is_unset(request.state_path):
            body['statePath'] = request.state_path
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.version_strategy):
            body['versionStrategy'] = request.version_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModuleAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/modules/{OpenApiUtilClient.get_encode_param(module_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateModuleAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_module_attribute(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.UpdateModuleAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateModuleAttributeResponse:
        """
        @summary 更新模板
        
        @param request: UpdateModuleAttributeRequest
        @return: UpdateModuleAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_module_attribute_with_options(module_id, request, headers, runtime)

    async def update_module_attribute_async(
        self,
        module_id: str,
        request: ia_cservice_20210806_models.UpdateModuleAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateModuleAttributeResponse:
        """
        @summary 更新模板
        
        @param request: UpdateModuleAttributeRequest
        @return: UpdateModuleAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_module_attribute_with_options_async(module_id, request, headers, runtime)

    def update_project_with_options(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateProjectResponse:
        """
        @summary 修改项目
        
        @param request: UpdateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_project_with_options_async(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.UpdateProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateProjectResponse:
        """
        @summary 修改项目
        
        @param request: UpdateProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateProjectResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProject',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/project/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_project(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.UpdateProjectRequest,
    ) -> ia_cservice_20210806_models.UpdateProjectResponse:
        """
        @summary 修改项目
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_project_with_options(project_id, request, headers, runtime)

    async def update_project_async(
        self,
        project_id: str,
        request: ia_cservice_20210806_models.UpdateProjectRequest,
    ) -> ia_cservice_20210806_models.UpdateProjectResponse:
        """
        @summary 修改项目
        
        @param request: UpdateProjectRequest
        @return: UpdateProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_project_with_options_async(project_id, request, headers, runtime)

    def update_registry_module_attribute_with_options(
        self,
        namespace_name: str,
        module_name: str,
        request: ia_cservice_20210806_models.UpdateRegistryModuleAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateRegistryModuleAttributeResponse:
        """
        @summary 修改RegistryModule
        
        @param request: UpdateRegistryModuleAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRegistryModuleAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.acl):
            body['acl'] = request.acl
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRegistryModuleAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModule/{OpenApiUtilClient.get_encode_param(namespace_name)}/{OpenApiUtilClient.get_encode_param(module_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateRegistryModuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_registry_module_attribute_with_options_async(
        self,
        namespace_name: str,
        module_name: str,
        request: ia_cservice_20210806_models.UpdateRegistryModuleAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateRegistryModuleAttributeResponse:
        """
        @summary 修改RegistryModule
        
        @param request: UpdateRegistryModuleAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRegistryModuleAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.acl):
            body['acl'] = request.acl
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRegistryModuleAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryModule/{OpenApiUtilClient.get_encode_param(namespace_name)}/{OpenApiUtilClient.get_encode_param(module_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateRegistryModuleAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_registry_module_attribute(
        self,
        namespace_name: str,
        module_name: str,
        request: ia_cservice_20210806_models.UpdateRegistryModuleAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateRegistryModuleAttributeResponse:
        """
        @summary 修改RegistryModule
        
        @param request: UpdateRegistryModuleAttributeRequest
        @return: UpdateRegistryModuleAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_registry_module_attribute_with_options(namespace_name, module_name, request, headers, runtime)

    async def update_registry_module_attribute_async(
        self,
        namespace_name: str,
        module_name: str,
        request: ia_cservice_20210806_models.UpdateRegistryModuleAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateRegistryModuleAttributeResponse:
        """
        @summary 修改RegistryModule
        
        @param request: UpdateRegistryModuleAttributeRequest
        @return: UpdateRegistryModuleAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_registry_module_attribute_with_options_async(namespace_name, module_name, request, headers, runtime)

    def update_registry_namespace_attribute_with_options(
        self,
        namespace_name: str,
        request: ia_cservice_20210806_models.UpdateRegistryNamespaceAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateRegistryNamespaceAttributeResponse:
        """
        @summary 修改工作空间
        
        @param request: UpdateRegistryNamespaceAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRegistryNamespaceAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.acl):
            body['acl'] = request.acl
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRegistryNamespaceAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryNamespace/{OpenApiUtilClient.get_encode_param(namespace_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateRegistryNamespaceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_registry_namespace_attribute_with_options_async(
        self,
        namespace_name: str,
        request: ia_cservice_20210806_models.UpdateRegistryNamespaceAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateRegistryNamespaceAttributeResponse:
        """
        @summary 修改工作空间
        
        @param request: UpdateRegistryNamespaceAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateRegistryNamespaceAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.acl):
            body['acl'] = request.acl
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRegistryNamespaceAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/registryNamespace/{OpenApiUtilClient.get_encode_param(namespace_name)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateRegistryNamespaceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_registry_namespace_attribute(
        self,
        namespace_name: str,
        request: ia_cservice_20210806_models.UpdateRegistryNamespaceAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateRegistryNamespaceAttributeResponse:
        """
        @summary 修改工作空间
        
        @param request: UpdateRegistryNamespaceAttributeRequest
        @return: UpdateRegistryNamespaceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_registry_namespace_attribute_with_options(namespace_name, request, headers, runtime)

    async def update_registry_namespace_attribute_async(
        self,
        namespace_name: str,
        request: ia_cservice_20210806_models.UpdateRegistryNamespaceAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateRegistryNamespaceAttributeResponse:
        """
        @summary 修改工作空间
        
        @param request: UpdateRegistryNamespaceAttributeRequest
        @return: UpdateRegistryNamespaceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_registry_namespace_attribute_with_options_async(namespace_name, request, headers, runtime)

    def update_resource_export_task_attribute_with_options(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.UpdateResourceExportTaskAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateResourceExportTaskAttributeResponse:
        """
        @summary 更新导出任务
        
        @param request: UpdateResourceExportTaskAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceExportTaskAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.export_to_module):
            body['exportToModule'] = request.export_to_module
        if not UtilClient.is_unset(request.include_rules):
            body['includeRules'] = request.include_rules
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceExportTaskAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateResourceExportTaskAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_export_task_attribute_with_options_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.UpdateResourceExportTaskAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateResourceExportTaskAttributeResponse:
        """
        @summary 更新导出任务
        
        @param request: UpdateResourceExportTaskAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateResourceExportTaskAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.export_to_module):
            body['exportToModule'] = request.export_to_module
        if not UtilClient.is_unset(request.include_rules):
            body['includeRules'] = request.include_rules
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.terraform_provider_version):
            body['terraformProviderVersion'] = request.terraform_provider_version
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        if not UtilClient.is_unset(request.variables):
            body['variables'] = request.variables
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateResourceExportTaskAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/exportTasks/{OpenApiUtilClient.get_encode_param(export_task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateResourceExportTaskAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource_export_task_attribute(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.UpdateResourceExportTaskAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateResourceExportTaskAttributeResponse:
        """
        @summary 更新导出任务
        
        @param request: UpdateResourceExportTaskAttributeRequest
        @return: UpdateResourceExportTaskAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_resource_export_task_attribute_with_options(export_task_id, request, headers, runtime)

    async def update_resource_export_task_attribute_async(
        self,
        export_task_id: str,
        request: ia_cservice_20210806_models.UpdateResourceExportTaskAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateResourceExportTaskAttributeResponse:
        """
        @summary 更新导出任务
        
        @param request: UpdateResourceExportTaskAttributeRequest
        @return: UpdateResourceExportTaskAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_resource_export_task_attribute_with_options_async(export_task_id, request, headers, runtime)

    def update_task_attribute_with_options(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.UpdateTaskAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateTaskAttributeResponse:
        """
        @summary 修改任务
        
        @param request: UpdateTaskAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTaskAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.init_module_state):
            body['initModuleState'] = request.init_module_state
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protection_strategy):
            body['protectionStrategy'] = request.protection_strategy
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.skip_property_validation):
            body['skipPropertyValidation'] = request.skip_property_validation
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTaskAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateTaskAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_task_attribute_with_options_async(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.UpdateTaskAttributeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.UpdateTaskAttributeResponse:
        """
        @summary 修改任务
        
        @param request: UpdateTaskAttributeRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTaskAttributeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_apply):
            body['autoApply'] = request.auto_apply
        if not UtilClient.is_unset(request.auto_destroy):
            body['autoDestroy'] = request.auto_destroy
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.group_info):
            body['groupInfo'] = request.group_info
        if not UtilClient.is_unset(request.init_module_state):
            body['initModuleState'] = request.init_module_state
        if not UtilClient.is_unset(request.module_version):
            body['moduleVersion'] = request.module_version
        if not UtilClient.is_unset(request.name):
            body['name'] = request.name
        if not UtilClient.is_unset(request.protection_strategy):
            body['protectionStrategy'] = request.protection_strategy
        if not UtilClient.is_unset(request.ram_role):
            body['ramRole'] = request.ram_role
        if not UtilClient.is_unset(request.skip_property_validation):
            body['skipPropertyValidation'] = request.skip_property_validation
        if not UtilClient.is_unset(request.tags):
            body['tags'] = request.tags
        if not UtilClient.is_unset(request.terraform_version):
            body['terraformVersion'] = request.terraform_version
        if not UtilClient.is_unset(request.trigger_strategy):
            body['triggerStrategy'] = request.trigger_strategy
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateTaskAttribute',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.UpdateTaskAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_task_attribute(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.UpdateTaskAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateTaskAttributeResponse:
        """
        @summary 修改任务
        
        @param request: UpdateTaskAttributeRequest
        @return: UpdateTaskAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_task_attribute_with_options(task_id, request, headers, runtime)

    async def update_task_attribute_async(
        self,
        task_id: str,
        request: ia_cservice_20210806_models.UpdateTaskAttributeRequest,
    ) -> ia_cservice_20210806_models.UpdateTaskAttributeResponse:
        """
        @summary 修改任务
        
        @param request: UpdateTaskAttributeRequest
        @return: UpdateTaskAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_task_attribute_with_options_async(task_id, request, headers, runtime)

    def validate_module_with_options(
        self,
        request: ia_cservice_20210806_models.ValidateModuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ValidateModuleResponse:
        """
        @summary 模版预检
        
        @param request: ValidateModuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateModuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.code_map):
            body['codeMap'] = request.code_map
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.source_path):
            body['sourcePath'] = request.source_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/module/validation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ValidateModuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_module_with_options_async(
        self,
        request: ia_cservice_20210806_models.ValidateModuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> ia_cservice_20210806_models.ValidateModuleResponse:
        """
        @summary 模版预检
        
        @param request: ValidateModuleRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateModuleResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.code):
            body['code'] = request.code
        if not UtilClient.is_unset(request.code_map):
            body['codeMap'] = request.code_map
        if not UtilClient.is_unset(request.source):
            body['source'] = request.source
        if not UtilClient.is_unset(request.source_path):
            body['sourcePath'] = request.source_path
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateModule',
            version='2021-08-06',
            protocol='HTTPS',
            pathname=f'/module/validation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            ia_cservice_20210806_models.ValidateModuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_module(
        self,
        request: ia_cservice_20210806_models.ValidateModuleRequest,
    ) -> ia_cservice_20210806_models.ValidateModuleResponse:
        """
        @summary 模版预检
        
        @param request: ValidateModuleRequest
        @return: ValidateModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.validate_module_with_options(request, headers, runtime)

    async def validate_module_async(
        self,
        request: ia_cservice_20210806_models.ValidateModuleRequest,
    ) -> ia_cservice_20210806_models.ValidateModuleResponse:
        """
        @summary 模版预检
        
        @param request: ValidateModuleRequest
        @return: ValidateModuleResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.validate_module_with_options_async(request, headers, runtime)
