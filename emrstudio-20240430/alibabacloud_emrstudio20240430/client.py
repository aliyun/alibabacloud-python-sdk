# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_gateway_pop.client import Client as GatewayClientClient
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_emrstudio20240430 import models as emr_studio_20240430_models
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
        self._product_id = 'EmrStudio'
        gateway_client = GatewayClientClient()
        self._spi = gateway_client
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('emrstudio', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_workflow_with_options(
        self,
        project_id: str,
        request: emr_studio_20240430_models.CreateWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.CreateWorkflowResponse:
        """
        @summary 创建工作流
        
        @param request: CreateWorkflowRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_group_id):
            query['alertGroupId'] = request.alert_group_id
        if not UtilClient.is_unset(request.alert_strategy):
            query['alertStrategy'] = request.alert_strategy
        if not UtilClient.is_unset(request.cron_expr):
            query['cronExpr'] = request.cron_expr
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.execution_type):
            query['executionType'] = request.execution_type
        if not UtilClient.is_unset(request.failure_strategy):
            query['failureStrategy'] = request.failure_strategy
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.parent_directory_id):
            query['parentDirectoryId'] = request.parent_directory_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.schedule_end_time):
            query['scheduleEndTime'] = request.schedule_end_time
        if not UtilClient.is_unset(request.schedule_start_time):
            query['scheduleStartTime'] = request.schedule_start_time
        if not UtilClient.is_unset(request.schedule_state):
            query['scheduleState'] = request.schedule_state
        if not UtilClient.is_unset(request.task_definition_json):
            query['taskDefinitionJson'] = request.task_definition_json
        if not UtilClient.is_unset(request.task_relation_json):
            query['taskRelationJson'] = request.task_relation_json
        if not UtilClient.is_unset(request.time_zone):
            query['timeZone'] = request.time_zone
        if not UtilClient.is_unset(request.timeout):
            query['timeout'] = request.timeout
        if not UtilClient.is_unset(request.workflow_instance_priority):
            query['workflowInstancePriority'] = request.workflow_instance_priority
        if not UtilClient.is_unset(request.workflow_params):
            query['workflowParams'] = request.workflow_params
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.task_definition_json_value):
            body['taskDefinitionJsonValue'] = request.task_definition_json_value
        if not UtilClient.is_unset(request.task_relation_json_value):
            body['taskRelationJsonValue'] = request.task_relation_json_value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkflow',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.CreateWorkflowResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.CreateWorkflowResponse(),
                self.execute(params, req, runtime)
            )

    async def create_workflow_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.CreateWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.CreateWorkflowResponse:
        """
        @summary 创建工作流
        
        @param request: CreateWorkflowRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_group_id):
            query['alertGroupId'] = request.alert_group_id
        if not UtilClient.is_unset(request.alert_strategy):
            query['alertStrategy'] = request.alert_strategy
        if not UtilClient.is_unset(request.cron_expr):
            query['cronExpr'] = request.cron_expr
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.execution_type):
            query['executionType'] = request.execution_type
        if not UtilClient.is_unset(request.failure_strategy):
            query['failureStrategy'] = request.failure_strategy
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.parent_directory_id):
            query['parentDirectoryId'] = request.parent_directory_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.schedule_end_time):
            query['scheduleEndTime'] = request.schedule_end_time
        if not UtilClient.is_unset(request.schedule_start_time):
            query['scheduleStartTime'] = request.schedule_start_time
        if not UtilClient.is_unset(request.schedule_state):
            query['scheduleState'] = request.schedule_state
        if not UtilClient.is_unset(request.task_definition_json):
            query['taskDefinitionJson'] = request.task_definition_json
        if not UtilClient.is_unset(request.task_relation_json):
            query['taskRelationJson'] = request.task_relation_json
        if not UtilClient.is_unset(request.time_zone):
            query['timeZone'] = request.time_zone
        if not UtilClient.is_unset(request.timeout):
            query['timeout'] = request.timeout
        if not UtilClient.is_unset(request.workflow_instance_priority):
            query['workflowInstancePriority'] = request.workflow_instance_priority
        if not UtilClient.is_unset(request.workflow_params):
            query['workflowParams'] = request.workflow_params
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.task_definition_json_value):
            body['taskDefinitionJsonValue'] = request.task_definition_json_value
        if not UtilClient.is_unset(request.task_relation_json_value):
            body['taskRelationJsonValue'] = request.task_relation_json_value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWorkflow',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.CreateWorkflowResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.CreateWorkflowResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_workflow(
        self,
        project_id: str,
        request: emr_studio_20240430_models.CreateWorkflowRequest,
    ) -> emr_studio_20240430_models.CreateWorkflowResponse:
        """
        @summary 创建工作流
        
        @param request: CreateWorkflowRequest
        @return: CreateWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_workflow_with_options(project_id, request, headers, runtime)

    async def create_workflow_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.CreateWorkflowRequest,
    ) -> emr_studio_20240430_models.CreateWorkflowResponse:
        """
        @summary 创建工作流
        
        @param request: CreateWorkflowRequest
        @return: CreateWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_workflow_with_options_async(project_id, request, headers, runtime)

    def delete_workflow_with_options(
        self,
        project_id: str,
        workflow_id: str,
        request: emr_studio_20240430_models.DeleteWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.DeleteWorkflowResponse:
        """
        @summary 删除工作流
        
        @param request: DeleteWorkflowRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkflow',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows/{OpenApiUtilClient.get_encode_param(workflow_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.DeleteWorkflowResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.DeleteWorkflowResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_workflow_with_options_async(
        self,
        project_id: str,
        workflow_id: str,
        request: emr_studio_20240430_models.DeleteWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.DeleteWorkflowResponse:
        """
        @summary 删除工作流
        
        @param request: DeleteWorkflowRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWorkflow',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows/{OpenApiUtilClient.get_encode_param(workflow_id)}',
            method='DELETE',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.DeleteWorkflowResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.DeleteWorkflowResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_workflow(
        self,
        project_id: str,
        workflow_id: str,
        request: emr_studio_20240430_models.DeleteWorkflowRequest,
    ) -> emr_studio_20240430_models.DeleteWorkflowResponse:
        """
        @summary 删除工作流
        
        @param request: DeleteWorkflowRequest
        @return: DeleteWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_workflow_with_options(project_id, workflow_id, request, headers, runtime)

    async def delete_workflow_async(
        self,
        project_id: str,
        workflow_id: str,
        request: emr_studio_20240430_models.DeleteWorkflowRequest,
    ) -> emr_studio_20240430_models.DeleteWorkflowResponse:
        """
        @summary 删除工作流
        
        @param request: DeleteWorkflowRequest
        @return: DeleteWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_workflow_with_options_async(project_id, workflow_id, request, headers, runtime)

    def describe_manual_task_with_options(
        self,
        project_id: str,
        manual_task_id: str,
        request: emr_studio_20240430_models.DescribeManualTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.DescribeManualTaskResponse:
        """
        @summary 获取手动任务定义
        
        @param request: DescribeManualTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeManualTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeManualTask',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/manualTasks/{OpenApiUtilClient.get_encode_param(manual_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeManualTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeManualTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_manual_task_with_options_async(
        self,
        project_id: str,
        manual_task_id: str,
        request: emr_studio_20240430_models.DescribeManualTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.DescribeManualTaskResponse:
        """
        @summary 获取手动任务定义
        
        @param request: DescribeManualTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeManualTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeManualTask',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/manualTasks/{OpenApiUtilClient.get_encode_param(manual_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeManualTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeManualTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_manual_task(
        self,
        project_id: str,
        manual_task_id: str,
        request: emr_studio_20240430_models.DescribeManualTaskRequest,
    ) -> emr_studio_20240430_models.DescribeManualTaskResponse:
        """
        @summary 获取手动任务定义
        
        @param request: DescribeManualTaskRequest
        @return: DescribeManualTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_manual_task_with_options(project_id, manual_task_id, request, headers, runtime)

    async def describe_manual_task_async(
        self,
        project_id: str,
        manual_task_id: str,
        request: emr_studio_20240430_models.DescribeManualTaskRequest,
    ) -> emr_studio_20240430_models.DescribeManualTaskResponse:
        """
        @summary 获取手动任务定义
        
        @param request: DescribeManualTaskRequest
        @return: DescribeManualTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_manual_task_with_options_async(project_id, manual_task_id, request, headers, runtime)

    def describe_manual_task_instance_with_options(
        self,
        manual_task_instance_id: str,
        project_id: str,
        request: emr_studio_20240430_models.DescribeManualTaskInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.DescribeManualTaskInstanceResponse:
        """
        @summary 获取手动任务实例
        
        @param request: DescribeManualTaskInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeManualTaskInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeManualTaskInstance',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/manualTaskInstances/{OpenApiUtilClient.get_encode_param(manual_task_instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeManualTaskInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeManualTaskInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_manual_task_instance_with_options_async(
        self,
        manual_task_instance_id: str,
        project_id: str,
        request: emr_studio_20240430_models.DescribeManualTaskInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.DescribeManualTaskInstanceResponse:
        """
        @summary 获取手动任务实例
        
        @param request: DescribeManualTaskInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeManualTaskInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeManualTaskInstance',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/manualTaskInstances/{OpenApiUtilClient.get_encode_param(manual_task_instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeManualTaskInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeManualTaskInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_manual_task_instance(
        self,
        manual_task_instance_id: str,
        project_id: str,
        request: emr_studio_20240430_models.DescribeManualTaskInstanceRequest,
    ) -> emr_studio_20240430_models.DescribeManualTaskInstanceResponse:
        """
        @summary 获取手动任务实例
        
        @param request: DescribeManualTaskInstanceRequest
        @return: DescribeManualTaskInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_manual_task_instance_with_options(manual_task_instance_id, project_id, request, headers, runtime)

    async def describe_manual_task_instance_async(
        self,
        manual_task_instance_id: str,
        project_id: str,
        request: emr_studio_20240430_models.DescribeManualTaskInstanceRequest,
    ) -> emr_studio_20240430_models.DescribeManualTaskInstanceResponse:
        """
        @summary 获取手动任务实例
        
        @param request: DescribeManualTaskInstanceRequest
        @return: DescribeManualTaskInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_manual_task_instance_with_options_async(manual_task_instance_id, project_id, request, headers, runtime)

    def describe_project_with_options(
        self,
        project_id: str,
        request: emr_studio_20240430_models.DescribeProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.DescribeProjectResponse:
        """
        @summary 获取项目详情
        
        @param request: DescribeProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProject',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeProjectResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeProjectResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_project_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.DescribeProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.DescribeProjectResponse:
        """
        @summary 获取项目详情
        
        @param request: DescribeProjectRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProjectResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProject',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeProjectResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeProjectResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_project(
        self,
        project_id: str,
        request: emr_studio_20240430_models.DescribeProjectRequest,
    ) -> emr_studio_20240430_models.DescribeProjectResponse:
        """
        @summary 获取项目详情
        
        @param request: DescribeProjectRequest
        @return: DescribeProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_project_with_options(project_id, request, headers, runtime)

    async def describe_project_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.DescribeProjectRequest,
    ) -> emr_studio_20240430_models.DescribeProjectResponse:
        """
        @summary 获取项目详情
        
        @param request: DescribeProjectRequest
        @return: DescribeProjectResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_project_with_options_async(project_id, request, headers, runtime)

    def describe_task_with_options(
        self,
        workflow_id: str,
        project_id: str,
        task_id: str,
        request: emr_studio_20240430_models.DescribeTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.DescribeTaskResponse:
        """
        @summary 查询任务定义
        
        @param request: DescribeTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTask',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows/{OpenApiUtilClient.get_encode_param(workflow_id)}/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_task_with_options_async(
        self,
        workflow_id: str,
        project_id: str,
        task_id: str,
        request: emr_studio_20240430_models.DescribeTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.DescribeTaskResponse:
        """
        @summary 查询任务定义
        
        @param request: DescribeTaskRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTask',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows/{OpenApiUtilClient.get_encode_param(workflow_id)}/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_task(
        self,
        workflow_id: str,
        project_id: str,
        task_id: str,
        request: emr_studio_20240430_models.DescribeTaskRequest,
    ) -> emr_studio_20240430_models.DescribeTaskResponse:
        """
        @summary 查询任务定义
        
        @param request: DescribeTaskRequest
        @return: DescribeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_task_with_options(workflow_id, project_id, task_id, request, headers, runtime)

    async def describe_task_async(
        self,
        workflow_id: str,
        project_id: str,
        task_id: str,
        request: emr_studio_20240430_models.DescribeTaskRequest,
    ) -> emr_studio_20240430_models.DescribeTaskResponse:
        """
        @summary 查询任务定义
        
        @param request: DescribeTaskRequest
        @return: DescribeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_task_with_options_async(workflow_id, project_id, task_id, request, headers, runtime)

    def describe_task_instance_with_options(
        self,
        project_id: str,
        workflow_instance_id: str,
        task_instance_id: str,
        request: emr_studio_20240430_models.DescribeTaskInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.DescribeTaskInstanceResponse:
        """
        @summary 获取任务实例
        
        @param request: DescribeTaskInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTaskInstance',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows/{OpenApiUtilClient.get_encode_param(workflow_instance_id)}/taskInstances/{OpenApiUtilClient.get_encode_param(task_instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeTaskInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeTaskInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_task_instance_with_options_async(
        self,
        project_id: str,
        workflow_instance_id: str,
        task_instance_id: str,
        request: emr_studio_20240430_models.DescribeTaskInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.DescribeTaskInstanceResponse:
        """
        @summary 获取任务实例
        
        @param request: DescribeTaskInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTaskInstance',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows/{OpenApiUtilClient.get_encode_param(workflow_instance_id)}/taskInstances/{OpenApiUtilClient.get_encode_param(task_instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeTaskInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeTaskInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_task_instance(
        self,
        project_id: str,
        workflow_instance_id: str,
        task_instance_id: str,
        request: emr_studio_20240430_models.DescribeTaskInstanceRequest,
    ) -> emr_studio_20240430_models.DescribeTaskInstanceResponse:
        """
        @summary 获取任务实例
        
        @param request: DescribeTaskInstanceRequest
        @return: DescribeTaskInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_task_instance_with_options(project_id, workflow_instance_id, task_instance_id, request, headers, runtime)

    async def describe_task_instance_async(
        self,
        project_id: str,
        workflow_instance_id: str,
        task_instance_id: str,
        request: emr_studio_20240430_models.DescribeTaskInstanceRequest,
    ) -> emr_studio_20240430_models.DescribeTaskInstanceResponse:
        """
        @summary 获取任务实例
        
        @param request: DescribeTaskInstanceRequest
        @return: DescribeTaskInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_task_instance_with_options_async(project_id, workflow_instance_id, task_instance_id, request, headers, runtime)

    def describe_workflow_with_options(
        self,
        project_id: str,
        workflow_id: str,
        request: emr_studio_20240430_models.DescribeWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.DescribeWorkflowResponse:
        """
        @summary 获取工作流详情
        
        @param request: DescribeWorkflowRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWorkflow',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows/{OpenApiUtilClient.get_encode_param(workflow_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeWorkflowResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeWorkflowResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_workflow_with_options_async(
        self,
        project_id: str,
        workflow_id: str,
        request: emr_studio_20240430_models.DescribeWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.DescribeWorkflowResponse:
        """
        @summary 获取工作流详情
        
        @param request: DescribeWorkflowRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWorkflow',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows/{OpenApiUtilClient.get_encode_param(workflow_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeWorkflowResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeWorkflowResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_workflow(
        self,
        project_id: str,
        workflow_id: str,
        request: emr_studio_20240430_models.DescribeWorkflowRequest,
    ) -> emr_studio_20240430_models.DescribeWorkflowResponse:
        """
        @summary 获取工作流详情
        
        @param request: DescribeWorkflowRequest
        @return: DescribeWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_workflow_with_options(project_id, workflow_id, request, headers, runtime)

    async def describe_workflow_async(
        self,
        project_id: str,
        workflow_id: str,
        request: emr_studio_20240430_models.DescribeWorkflowRequest,
    ) -> emr_studio_20240430_models.DescribeWorkflowResponse:
        """
        @summary 获取工作流详情
        
        @param request: DescribeWorkflowRequest
        @return: DescribeWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_workflow_with_options_async(project_id, workflow_id, request, headers, runtime)

    def describe_workflow_instance_with_options(
        self,
        project_id: str,
        workflow_instance_id: str,
        request: emr_studio_20240430_models.DescribeWorkflowInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.DescribeWorkflowInstanceResponse:
        """
        @summary 获取工作流实例详情
        
        @param request: DescribeWorkflowInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWorkflowInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWorkflowInstance',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflowInstances/{OpenApiUtilClient.get_encode_param(workflow_instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeWorkflowInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeWorkflowInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def describe_workflow_instance_with_options_async(
        self,
        project_id: str,
        workflow_instance_id: str,
        request: emr_studio_20240430_models.DescribeWorkflowInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.DescribeWorkflowInstanceResponse:
        """
        @summary 获取工作流实例详情
        
        @param request: DescribeWorkflowInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeWorkflowInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWorkflowInstance',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflowInstances/{OpenApiUtilClient.get_encode_param(workflow_instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeWorkflowInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.DescribeWorkflowInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def describe_workflow_instance(
        self,
        project_id: str,
        workflow_instance_id: str,
        request: emr_studio_20240430_models.DescribeWorkflowInstanceRequest,
    ) -> emr_studio_20240430_models.DescribeWorkflowInstanceResponse:
        """
        @summary 获取工作流实例详情
        
        @param request: DescribeWorkflowInstanceRequest
        @return: DescribeWorkflowInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_workflow_instance_with_options(project_id, workflow_instance_id, request, headers, runtime)

    async def describe_workflow_instance_async(
        self,
        project_id: str,
        workflow_instance_id: str,
        request: emr_studio_20240430_models.DescribeWorkflowInstanceRequest,
    ) -> emr_studio_20240430_models.DescribeWorkflowInstanceResponse:
        """
        @summary 获取工作流实例详情
        
        @param request: DescribeWorkflowInstanceRequest
        @return: DescribeWorkflowInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_workflow_instance_with_options_async(project_id, workflow_instance_id, request, headers, runtime)

    def list_alert_groups_with_options(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListAlertGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListAlertGroupsResponse:
        """
        @summary 查询告警组列表
        
        @param request: ListAlertGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlertGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlertGroups',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/alert-groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListAlertGroupsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListAlertGroupsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_alert_groups_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListAlertGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListAlertGroupsResponse:
        """
        @summary 查询告警组列表
        
        @param request: ListAlertGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAlertGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlertGroups',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/alert-groups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListAlertGroupsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListAlertGroupsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_alert_groups(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListAlertGroupsRequest,
    ) -> emr_studio_20240430_models.ListAlertGroupsResponse:
        """
        @summary 查询告警组列表
        
        @param request: ListAlertGroupsRequest
        @return: ListAlertGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_alert_groups_with_options(project_id, request, headers, runtime)

    async def list_alert_groups_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListAlertGroupsRequest,
    ) -> emr_studio_20240430_models.ListAlertGroupsResponse:
        """
        @summary 查询告警组列表
        
        @param request: ListAlertGroupsRequest
        @return: ListAlertGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_alert_groups_with_options_async(project_id, request, headers, runtime)

    def list_manual_task_instances_with_options(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListManualTaskInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListManualTaskInstancesResponse:
        """
        @summary 获取手动任务实例列表
        
        @param request: ListManualTaskInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListManualTaskInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListManualTaskInstances',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/manualTaskInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListManualTaskInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListManualTaskInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_manual_task_instances_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListManualTaskInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListManualTaskInstancesResponse:
        """
        @summary 获取手动任务实例列表
        
        @param request: ListManualTaskInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListManualTaskInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListManualTaskInstances',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/manualTaskInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListManualTaskInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListManualTaskInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_manual_task_instances(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListManualTaskInstancesRequest,
    ) -> emr_studio_20240430_models.ListManualTaskInstancesResponse:
        """
        @summary 获取手动任务实例列表
        
        @param request: ListManualTaskInstancesRequest
        @return: ListManualTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_manual_task_instances_with_options(project_id, request, headers, runtime)

    async def list_manual_task_instances_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListManualTaskInstancesRequest,
    ) -> emr_studio_20240430_models.ListManualTaskInstancesResponse:
        """
        @summary 获取手动任务实例列表
        
        @param request: ListManualTaskInstancesRequest
        @return: ListManualTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_manual_task_instances_with_options_async(project_id, request, headers, runtime)

    def list_manual_tasks_with_options(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListManualTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListManualTasksResponse:
        """
        @summary 查询手动任务定义列表
        
        @param request: ListManualTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListManualTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListManualTasks',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/manualTasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListManualTasksResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListManualTasksResponse(),
                self.execute(params, req, runtime)
            )

    async def list_manual_tasks_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListManualTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListManualTasksResponse:
        """
        @summary 查询手动任务定义列表
        
        @param request: ListManualTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListManualTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListManualTasks',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/manualTasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListManualTasksResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListManualTasksResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_manual_tasks(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListManualTasksRequest,
    ) -> emr_studio_20240430_models.ListManualTasksResponse:
        """
        @summary 查询手动任务定义列表
        
        @param request: ListManualTasksRequest
        @return: ListManualTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_manual_tasks_with_options(project_id, request, headers, runtime)

    async def list_manual_tasks_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListManualTasksRequest,
    ) -> emr_studio_20240430_models.ListManualTasksResponse:
        """
        @summary 查询手动任务定义列表
        
        @param request: ListManualTasksRequest
        @return: ListManualTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_manual_tasks_with_options_async(project_id, request, headers, runtime)

    def list_projects_with_options(
        self,
        request: emr_studio_20240430_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListProjectsResponse:
        """
        @summary 获取项目详情
        
        @param request: ListProjectsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListProjectsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListProjectsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_projects_with_options_async(
        self,
        request: emr_studio_20240430_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListProjectsResponse:
        """
        @summary 获取项目详情
        
        @param request: ListProjectsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListProjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProjects',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListProjectsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListProjectsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_projects(
        self,
        request: emr_studio_20240430_models.ListProjectsRequest,
    ) -> emr_studio_20240430_models.ListProjectsResponse:
        """
        @summary 获取项目详情
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_projects_with_options(request, headers, runtime)

    async def list_projects_async(
        self,
        request: emr_studio_20240430_models.ListProjectsRequest,
    ) -> emr_studio_20240430_models.ListProjectsResponse:
        """
        @summary 获取项目详情
        
        @param request: ListProjectsRequest
        @return: ListProjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_projects_with_options_async(request, headers, runtime)

    def list_resource_groups_with_options(
        self,
        request: emr_studio_20240430_models.ListResourceGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListResourceGroupsResponse:
        """
        @summary 查询调度资源组列表
        
        @param request: ListResourceGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_name):
            query['resourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.resource_group_type):
            query['resourceGroupType'] = request.resource_group_type
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceGroups',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/resourcegroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListResourceGroupsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListResourceGroupsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_resource_groups_with_options_async(
        self,
        request: emr_studio_20240430_models.ListResourceGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListResourceGroupsResponse:
        """
        @summary 查询调度资源组列表
        
        @param request: ListResourceGroupsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_name):
            query['resourceGroupName'] = request.resource_group_name
        if not UtilClient.is_unset(request.resource_group_type):
            query['resourceGroupType'] = request.resource_group_type
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceGroups',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/resourcegroups',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListResourceGroupsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListResourceGroupsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_resource_groups(
        self,
        request: emr_studio_20240430_models.ListResourceGroupsRequest,
    ) -> emr_studio_20240430_models.ListResourceGroupsResponse:
        """
        @summary 查询调度资源组列表
        
        @param request: ListResourceGroupsRequest
        @return: ListResourceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_resource_groups_with_options(request, headers, runtime)

    async def list_resource_groups_async(
        self,
        request: emr_studio_20240430_models.ListResourceGroupsRequest,
    ) -> emr_studio_20240430_models.ListResourceGroupsResponse:
        """
        @summary 查询调度资源组列表
        
        @param request: ListResourceGroupsRequest
        @return: ListResourceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_resource_groups_with_options_async(request, headers, runtime)

    def list_task_instances_with_options(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListTaskInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListTaskInstancesResponse:
        """
        @summary 获取任务实例列表
        
        @param request: ListTaskInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.workflow_instance_id):
            query['workflowInstanceId'] = request.workflow_instance_id
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskInstances',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/taskInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListTaskInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListTaskInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_task_instances_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListTaskInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListTaskInstancesResponse:
        """
        @summary 获取任务实例列表
        
        @param request: ListTaskInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTaskInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.workflow_instance_id):
            query['workflowInstanceId'] = request.workflow_instance_id
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTaskInstances',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/taskInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListTaskInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListTaskInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_task_instances(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListTaskInstancesRequest,
    ) -> emr_studio_20240430_models.ListTaskInstancesResponse:
        """
        @summary 获取任务实例列表
        
        @param request: ListTaskInstancesRequest
        @return: ListTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_task_instances_with_options(project_id, request, headers, runtime)

    async def list_task_instances_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListTaskInstancesRequest,
    ) -> emr_studio_20240430_models.ListTaskInstancesResponse:
        """
        @summary 获取任务实例列表
        
        @param request: ListTaskInstancesRequest
        @return: ListTaskInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_task_instances_with_options_async(project_id, request, headers, runtime)

    def list_tasks_with_options(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListTasksResponse:
        """
        @summary 查询任务定义列表
        
        @param request: ListTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        if not UtilClient.is_unset(request.workflow_id):
            query['workflowId'] = request.workflow_id
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListTasksResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListTasksResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tasks_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListTasksResponse:
        """
        @summary 查询任务定义列表
        
        @param request: ListTasksRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTasksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.task_type):
            query['taskType'] = request.task_type
        if not UtilClient.is_unset(request.workflow_id):
            query['workflowId'] = request.workflow_id
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTasks',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListTasksResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListTasksResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tasks(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListTasksRequest,
    ) -> emr_studio_20240430_models.ListTasksResponse:
        """
        @summary 查询任务定义列表
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(project_id, request, headers, runtime)

    async def list_tasks_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListTasksRequest,
    ) -> emr_studio_20240430_models.ListTasksResponse:
        """
        @summary 查询任务定义列表
        
        @param request: ListTasksRequest
        @return: ListTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tasks_with_options_async(project_id, request, headers, runtime)

    def list_workflow_directories_with_options(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListWorkflowDirectoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListWorkflowDirectoriesResponse:
        """
        @summary 查询工作流目录列表
        
        @param request: ListWorkflowDirectoriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkflowDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['directoryId'] = request.directory_id
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.parent_directory_id):
            query['parentDirectoryId'] = request.parent_directory_id
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflowDirectories',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/directories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListWorkflowDirectoriesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListWorkflowDirectoriesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_workflow_directories_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListWorkflowDirectoriesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListWorkflowDirectoriesResponse:
        """
        @summary 查询工作流目录列表
        
        @param request: ListWorkflowDirectoriesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkflowDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['directoryId'] = request.directory_id
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.parent_directory_id):
            query['parentDirectoryId'] = request.parent_directory_id
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflowDirectories',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/directories',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListWorkflowDirectoriesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListWorkflowDirectoriesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_workflow_directories(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListWorkflowDirectoriesRequest,
    ) -> emr_studio_20240430_models.ListWorkflowDirectoriesResponse:
        """
        @summary 查询工作流目录列表
        
        @param request: ListWorkflowDirectoriesRequest
        @return: ListWorkflowDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workflow_directories_with_options(project_id, request, headers, runtime)

    async def list_workflow_directories_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListWorkflowDirectoriesRequest,
    ) -> emr_studio_20240430_models.ListWorkflowDirectoriesResponse:
        """
        @summary 查询工作流目录列表
        
        @param request: ListWorkflowDirectoriesRequest
        @return: ListWorkflowDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workflow_directories_with_options_async(project_id, request, headers, runtime)

    def list_workflow_instances_with_options(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListWorkflowInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListWorkflowInstancesResponse:
        """
        @summary 获取工作流实例列表
        
        @param request: ListWorkflowInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkflowInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.workflow_id):
            query['workflowId'] = request.workflow_id
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflowInstances',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflowInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListWorkflowInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListWorkflowInstancesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_workflow_instances_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListWorkflowInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListWorkflowInstancesResponse:
        """
        @summary 获取工作流实例列表
        
        @param request: ListWorkflowInstancesRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkflowInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['status'] = request.status
        if not UtilClient.is_unset(request.workflow_id):
            query['workflowId'] = request.workflow_id
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflowInstances',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflowInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListWorkflowInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListWorkflowInstancesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_workflow_instances(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListWorkflowInstancesRequest,
    ) -> emr_studio_20240430_models.ListWorkflowInstancesResponse:
        """
        @summary 获取工作流实例列表
        
        @param request: ListWorkflowInstancesRequest
        @return: ListWorkflowInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workflow_instances_with_options(project_id, request, headers, runtime)

    async def list_workflow_instances_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListWorkflowInstancesRequest,
    ) -> emr_studio_20240430_models.ListWorkflowInstancesResponse:
        """
        @summary 获取工作流实例列表
        
        @param request: ListWorkflowInstancesRequest
        @return: ListWorkflowInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workflow_instances_with_options_async(project_id, request, headers, runtime)

    def list_workflows_with_options(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListWorkflowsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListWorkflowsResponse:
        """
        @summary 获取工作流列表
        
        @param request: ListWorkflowsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkflowsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflows',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListWorkflowsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListWorkflowsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_workflows_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListWorkflowsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.ListWorkflowsResponse:
        """
        @summary 获取工作流列表
        
        @param request: ListWorkflowsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkflowsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkflows',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.ListWorkflowsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.ListWorkflowsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_workflows(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListWorkflowsRequest,
    ) -> emr_studio_20240430_models.ListWorkflowsResponse:
        """
        @summary 获取工作流列表
        
        @param request: ListWorkflowsRequest
        @return: ListWorkflowsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workflows_with_options(project_id, request, headers, runtime)

    async def list_workflows_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.ListWorkflowsRequest,
    ) -> emr_studio_20240430_models.ListWorkflowsResponse:
        """
        @summary 获取工作流列表
        
        @param request: ListWorkflowsRequest
        @return: ListWorkflowsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workflows_with_options_async(project_id, request, headers, runtime)

    def operate_workflow_instance_with_options(
        self,
        project_id: str,
        request: emr_studio_20240430_models.OperateWorkflowInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.OperateWorkflowInstanceResponse:
        """
        @summary 操作工作流实例
        
        @param request: OperateWorkflowInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateWorkflowInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.exec_type):
            body['execType'] = request.exec_type
        if not UtilClient.is_unset(request.workflow_instance_id):
            body['workflowInstanceId'] = request.workflow_instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OperateWorkflowInstance',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/executors/execute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.OperateWorkflowInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.OperateWorkflowInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def operate_workflow_instance_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.OperateWorkflowInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.OperateWorkflowInstanceResponse:
        """
        @summary 操作工作流实例
        
        @param request: OperateWorkflowInstanceRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: OperateWorkflowInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.exec_type):
            body['execType'] = request.exec_type
        if not UtilClient.is_unset(request.workflow_instance_id):
            body['workflowInstanceId'] = request.workflow_instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OperateWorkflowInstance',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/executors/execute',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.OperateWorkflowInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.OperateWorkflowInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def operate_workflow_instance(
        self,
        project_id: str,
        request: emr_studio_20240430_models.OperateWorkflowInstanceRequest,
    ) -> emr_studio_20240430_models.OperateWorkflowInstanceResponse:
        """
        @summary 操作工作流实例
        
        @param request: OperateWorkflowInstanceRequest
        @return: OperateWorkflowInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.operate_workflow_instance_with_options(project_id, request, headers, runtime)

    async def operate_workflow_instance_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.OperateWorkflowInstanceRequest,
    ) -> emr_studio_20240430_models.OperateWorkflowInstanceResponse:
        """
        @summary 操作工作流实例
        
        @param request: OperateWorkflowInstanceRequest
        @return: OperateWorkflowInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.operate_workflow_instance_with_options_async(project_id, request, headers, runtime)

    def run_workflow_with_options(
        self,
        project_id: str,
        request: emr_studio_20240430_models.RunWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.RunWorkflowResponse:
        """
        @summary 运行工作流
        
        @param request: RunWorkflowRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_group_id):
            query['alertGroupId'] = request.alert_group_id
        if not UtilClient.is_unset(request.alert_strategy):
            query['alertStrategy'] = request.alert_strategy
        if not UtilClient.is_unset(request.complement_dependent_mode):
            query['complementDependentMode'] = request.complement_dependent_mode
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        if not UtilClient.is_unset(request.exec_type):
            query['execType'] = request.exec_type
        if not UtilClient.is_unset(request.expected_parallelism_number):
            query['expectedParallelismNumber'] = request.expected_parallelism_number
        if not UtilClient.is_unset(request.failure_strategy):
            query['failureStrategy'] = request.failure_strategy
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.run_mode):
            query['runMode'] = request.run_mode
        if not UtilClient.is_unset(request.schedule_time):
            query['scheduleTime'] = request.schedule_time
        if not UtilClient.is_unset(request.start_params):
            query['startParams'] = request.start_params
        if not UtilClient.is_unset(request.workflow_id):
            query['workflowId'] = request.workflow_id
        if not UtilClient.is_unset(request.workflow_instance_priority):
            query['workflowInstancePriority'] = request.workflow_instance_priority
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunWorkflow',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/executors/run-workflow',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.RunWorkflowResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.RunWorkflowResponse(),
                self.execute(params, req, runtime)
            )

    async def run_workflow_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.RunWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.RunWorkflowResponse:
        """
        @summary 运行工作流
        
        @param request: RunWorkflowRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_group_id):
            query['alertGroupId'] = request.alert_group_id
        if not UtilClient.is_unset(request.alert_strategy):
            query['alertStrategy'] = request.alert_strategy
        if not UtilClient.is_unset(request.complement_dependent_mode):
            query['complementDependentMode'] = request.complement_dependent_mode
        if not UtilClient.is_unset(request.dry_run):
            query['dryRun'] = request.dry_run
        if not UtilClient.is_unset(request.exec_type):
            query['execType'] = request.exec_type
        if not UtilClient.is_unset(request.expected_parallelism_number):
            query['expectedParallelismNumber'] = request.expected_parallelism_number
        if not UtilClient.is_unset(request.failure_strategy):
            query['failureStrategy'] = request.failure_strategy
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.run_mode):
            query['runMode'] = request.run_mode
        if not UtilClient.is_unset(request.schedule_time):
            query['scheduleTime'] = request.schedule_time
        if not UtilClient.is_unset(request.start_params):
            query['startParams'] = request.start_params
        if not UtilClient.is_unset(request.workflow_id):
            query['workflowId'] = request.workflow_id
        if not UtilClient.is_unset(request.workflow_instance_priority):
            query['workflowInstancePriority'] = request.workflow_instance_priority
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunWorkflow',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/executors/run-workflow',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.RunWorkflowResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.RunWorkflowResponse(),
                await self.execute_async(params, req, runtime)
            )

    def run_workflow(
        self,
        project_id: str,
        request: emr_studio_20240430_models.RunWorkflowRequest,
    ) -> emr_studio_20240430_models.RunWorkflowResponse:
        """
        @summary 运行工作流
        
        @param request: RunWorkflowRequest
        @return: RunWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.run_workflow_with_options(project_id, request, headers, runtime)

    async def run_workflow_async(
        self,
        project_id: str,
        request: emr_studio_20240430_models.RunWorkflowRequest,
    ) -> emr_studio_20240430_models.RunWorkflowResponse:
        """
        @summary 运行工作流
        
        @param request: RunWorkflowRequest
        @return: RunWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.run_workflow_with_options_async(project_id, request, headers, runtime)

    def update_workflow_with_options(
        self,
        project_id: str,
        workflow_id: str,
        request: emr_studio_20240430_models.UpdateWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.UpdateWorkflowResponse:
        """
        @summary 更新工作流
        
        @param request: UpdateWorkflowRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_group_id):
            query['alertGroupId'] = request.alert_group_id
        if not UtilClient.is_unset(request.alert_strategy):
            query['alertStrategy'] = request.alert_strategy
        if not UtilClient.is_unset(request.cron_expr):
            query['cronExpr'] = request.cron_expr
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.execution_type):
            query['executionType'] = request.execution_type
        if not UtilClient.is_unset(request.failure_strategy):
            query['failureStrategy'] = request.failure_strategy
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.parent_directory_id):
            query['parentDirectoryId'] = request.parent_directory_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.schedule_end_time):
            query['scheduleEndTime'] = request.schedule_end_time
        if not UtilClient.is_unset(request.schedule_start_time):
            query['scheduleStartTime'] = request.schedule_start_time
        if not UtilClient.is_unset(request.schedule_state):
            query['scheduleState'] = request.schedule_state
        if not UtilClient.is_unset(request.task_definition_json):
            query['taskDefinitionJson'] = request.task_definition_json
        if not UtilClient.is_unset(request.task_relation_json):
            query['taskRelationJson'] = request.task_relation_json
        if not UtilClient.is_unset(request.time_zone):
            query['timeZone'] = request.time_zone
        if not UtilClient.is_unset(request.timeout):
            query['timeout'] = request.timeout
        if not UtilClient.is_unset(request.workflow_instance_priority):
            query['workflowInstancePriority'] = request.workflow_instance_priority
        if not UtilClient.is_unset(request.workflow_params):
            query['workflowParams'] = request.workflow_params
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.task_definition_json_value):
            body['taskDefinitionJsonValue'] = request.task_definition_json_value
        if not UtilClient.is_unset(request.task_relation_json_value):
            body['taskRelationJsonValue'] = request.task_relation_json_value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkflow',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows/{OpenApiUtilClient.get_encode_param(workflow_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.UpdateWorkflowResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.UpdateWorkflowResponse(),
                self.execute(params, req, runtime)
            )

    async def update_workflow_with_options_async(
        self,
        project_id: str,
        workflow_id: str,
        request: emr_studio_20240430_models.UpdateWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20240430_models.UpdateWorkflowResponse:
        """
        @summary 更新工作流
        
        @param request: UpdateWorkflowRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWorkflowResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_group_id):
            query['alertGroupId'] = request.alert_group_id
        if not UtilClient.is_unset(request.alert_strategy):
            query['alertStrategy'] = request.alert_strategy
        if not UtilClient.is_unset(request.cron_expr):
            query['cronExpr'] = request.cron_expr
        if not UtilClient.is_unset(request.description):
            query['description'] = request.description
        if not UtilClient.is_unset(request.execution_type):
            query['executionType'] = request.execution_type
        if not UtilClient.is_unset(request.failure_strategy):
            query['failureStrategy'] = request.failure_strategy
        if not UtilClient.is_unset(request.name):
            query['name'] = request.name
        if not UtilClient.is_unset(request.parent_directory_id):
            query['parentDirectoryId'] = request.parent_directory_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['resourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.schedule_end_time):
            query['scheduleEndTime'] = request.schedule_end_time
        if not UtilClient.is_unset(request.schedule_start_time):
            query['scheduleStartTime'] = request.schedule_start_time
        if not UtilClient.is_unset(request.schedule_state):
            query['scheduleState'] = request.schedule_state
        if not UtilClient.is_unset(request.task_definition_json):
            query['taskDefinitionJson'] = request.task_definition_json
        if not UtilClient.is_unset(request.task_relation_json):
            query['taskRelationJson'] = request.task_relation_json
        if not UtilClient.is_unset(request.time_zone):
            query['timeZone'] = request.time_zone
        if not UtilClient.is_unset(request.timeout):
            query['timeout'] = request.timeout
        if not UtilClient.is_unset(request.workflow_instance_priority):
            query['workflowInstancePriority'] = request.workflow_instance_priority
        if not UtilClient.is_unset(request.workflow_params):
            query['workflowParams'] = request.workflow_params
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        body = {}
        if not UtilClient.is_unset(request.task_definition_json_value):
            body['taskDefinitionJsonValue'] = request.task_definition_json_value
        if not UtilClient.is_unset(request.task_relation_json_value):
            body['taskRelationJsonValue'] = request.task_relation_json_value
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWorkflow',
            version='2024-04-30',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows/{OpenApiUtilClient.get_encode_param(workflow_id)}',
            method='PUT',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                emr_studio_20240430_models.UpdateWorkflowResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                emr_studio_20240430_models.UpdateWorkflowResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_workflow(
        self,
        project_id: str,
        workflow_id: str,
        request: emr_studio_20240430_models.UpdateWorkflowRequest,
    ) -> emr_studio_20240430_models.UpdateWorkflowResponse:
        """
        @summary 更新工作流
        
        @param request: UpdateWorkflowRequest
        @return: UpdateWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_workflow_with_options(project_id, workflow_id, request, headers, runtime)

    async def update_workflow_async(
        self,
        project_id: str,
        workflow_id: str,
        request: emr_studio_20240430_models.UpdateWorkflowRequest,
    ) -> emr_studio_20240430_models.UpdateWorkflowResponse:
        """
        @summary 更新工作流
        
        @param request: UpdateWorkflowRequest
        @return: UpdateWorkflowResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_workflow_with_options_async(project_id, workflow_id, request, headers, runtime)
