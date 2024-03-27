# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_emrstudio20231009 import models as emr_studio_20231009_models
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

    def describe_manual_task_with_options(
        self,
        project_id: str,
        manual_task_id: str,
        request: emr_studio_20231009_models.DescribeManualTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.DescribeManualTaskResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/manualTasks/{OpenApiUtilClient.get_encode_param(manual_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeManualTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_manual_task_with_options_async(
        self,
        project_id: str,
        manual_task_id: str,
        request: emr_studio_20231009_models.DescribeManualTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.DescribeManualTaskResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/manualTasks/{OpenApiUtilClient.get_encode_param(manual_task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeManualTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_manual_task(
        self,
        project_id: str,
        manual_task_id: str,
        request: emr_studio_20231009_models.DescribeManualTaskRequest,
    ) -> emr_studio_20231009_models.DescribeManualTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_manual_task_with_options(project_id, manual_task_id, request, headers, runtime)

    async def describe_manual_task_async(
        self,
        project_id: str,
        manual_task_id: str,
        request: emr_studio_20231009_models.DescribeManualTaskRequest,
    ) -> emr_studio_20231009_models.DescribeManualTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_manual_task_with_options_async(project_id, manual_task_id, request, headers, runtime)

    def describe_manual_task_instance_with_options(
        self,
        manual_task_instance_id: str,
        project_id: str,
        request: emr_studio_20231009_models.DescribeManualTaskInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.DescribeManualTaskInstanceResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/manualTaskInstances/{OpenApiUtilClient.get_encode_param(manual_task_instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeManualTaskInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_manual_task_instance_with_options_async(
        self,
        manual_task_instance_id: str,
        project_id: str,
        request: emr_studio_20231009_models.DescribeManualTaskInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.DescribeManualTaskInstanceResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/manualTaskInstances/{OpenApiUtilClient.get_encode_param(manual_task_instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeManualTaskInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_manual_task_instance(
        self,
        manual_task_instance_id: str,
        project_id: str,
        request: emr_studio_20231009_models.DescribeManualTaskInstanceRequest,
    ) -> emr_studio_20231009_models.DescribeManualTaskInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_manual_task_instance_with_options(manual_task_instance_id, project_id, request, headers, runtime)

    async def describe_manual_task_instance_async(
        self,
        manual_task_instance_id: str,
        project_id: str,
        request: emr_studio_20231009_models.DescribeManualTaskInstanceRequest,
    ) -> emr_studio_20231009_models.DescribeManualTaskInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_manual_task_instance_with_options_async(manual_task_instance_id, project_id, request, headers, runtime)

    def describe_project_with_options(
        self,
        code: str,
        request: emr_studio_20231009_models.DescribeProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.DescribeProjectResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(code)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_with_options_async(
        self,
        code: str,
        request: emr_studio_20231009_models.DescribeProjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.DescribeProjectResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(code)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeProjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project(
        self,
        code: str,
        request: emr_studio_20231009_models.DescribeProjectRequest,
    ) -> emr_studio_20231009_models.DescribeProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_project_with_options(code, request, headers, runtime)

    async def describe_project_async(
        self,
        code: str,
        request: emr_studio_20231009_models.DescribeProjectRequest,
    ) -> emr_studio_20231009_models.DescribeProjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_project_with_options_async(code, request, headers, runtime)

    def describe_task_with_options(
        self,
        workflow_id: str,
        project_id: str,
        task_id: str,
        request: emr_studio_20231009_models.DescribeTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.DescribeTaskResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows/{OpenApiUtilClient.get_encode_param(workflow_id)}/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_task_with_options_async(
        self,
        workflow_id: str,
        project_id: str,
        task_id: str,
        request: emr_studio_20231009_models.DescribeTaskRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.DescribeTaskResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows/{OpenApiUtilClient.get_encode_param(workflow_id)}/tasks/{OpenApiUtilClient.get_encode_param(task_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_task(
        self,
        workflow_id: str,
        project_id: str,
        task_id: str,
        request: emr_studio_20231009_models.DescribeTaskRequest,
    ) -> emr_studio_20231009_models.DescribeTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_task_with_options(workflow_id, project_id, task_id, request, headers, runtime)

    async def describe_task_async(
        self,
        workflow_id: str,
        project_id: str,
        task_id: str,
        request: emr_studio_20231009_models.DescribeTaskRequest,
    ) -> emr_studio_20231009_models.DescribeTaskResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_task_with_options_async(workflow_id, project_id, task_id, request, headers, runtime)

    def describe_task_instance_with_options(
        self,
        project_id: str,
        workflow_instance_id: str,
        task_instance_id: str,
        request: emr_studio_20231009_models.DescribeTaskInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.DescribeTaskInstanceResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows/{OpenApiUtilClient.get_encode_param(workflow_instance_id)}/taskInstances/{OpenApiUtilClient.get_encode_param(task_instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeTaskInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_task_instance_with_options_async(
        self,
        project_id: str,
        workflow_instance_id: str,
        task_instance_id: str,
        request: emr_studio_20231009_models.DescribeTaskInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.DescribeTaskInstanceResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/workflows/{OpenApiUtilClient.get_encode_param(workflow_instance_id)}/taskInstances/{OpenApiUtilClient.get_encode_param(task_instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeTaskInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_task_instance(
        self,
        project_id: str,
        workflow_instance_id: str,
        task_instance_id: str,
        request: emr_studio_20231009_models.DescribeTaskInstanceRequest,
    ) -> emr_studio_20231009_models.DescribeTaskInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_task_instance_with_options(project_id, workflow_instance_id, task_instance_id, request, headers, runtime)

    async def describe_task_instance_async(
        self,
        project_id: str,
        workflow_instance_id: str,
        task_instance_id: str,
        request: emr_studio_20231009_models.DescribeTaskInstanceRequest,
    ) -> emr_studio_20231009_models.DescribeTaskInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_task_instance_with_options_async(project_id, workflow_instance_id, task_instance_id, request, headers, runtime)

    def describe_workflow_with_options(
        self,
        project_id: str,
        workflow_id: str,
        request: emr_studio_20231009_models.DescribeWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.DescribeWorkflowResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/processDefinitions/{OpenApiUtilClient.get_encode_param(workflow_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeWorkflowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_workflow_with_options_async(
        self,
        project_id: str,
        workflow_id: str,
        request: emr_studio_20231009_models.DescribeWorkflowRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.DescribeWorkflowResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/processDefinitions/{OpenApiUtilClient.get_encode_param(workflow_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeWorkflowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_workflow(
        self,
        project_id: str,
        workflow_id: str,
        request: emr_studio_20231009_models.DescribeWorkflowRequest,
    ) -> emr_studio_20231009_models.DescribeWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_workflow_with_options(project_id, workflow_id, request, headers, runtime)

    async def describe_workflow_async(
        self,
        project_id: str,
        workflow_id: str,
        request: emr_studio_20231009_models.DescribeWorkflowRequest,
    ) -> emr_studio_20231009_models.DescribeWorkflowResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_workflow_with_options_async(project_id, workflow_id, request, headers, runtime)

    def describe_workflow_instance_with_options(
        self,
        project_id: str,
        workflow_instance_id: str,
        request: emr_studio_20231009_models.DescribeWorkflowInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.DescribeWorkflowInstanceResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/processInstances/{OpenApiUtilClient.get_encode_param(workflow_instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_workflow_instance_with_options_async(
        self,
        project_id: str,
        workflow_instance_id: str,
        request: emr_studio_20231009_models.DescribeWorkflowInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.DescribeWorkflowInstanceResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/processInstances/{OpenApiUtilClient.get_encode_param(workflow_instance_id)}',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.DescribeWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_workflow_instance(
        self,
        project_id: str,
        workflow_instance_id: str,
        request: emr_studio_20231009_models.DescribeWorkflowInstanceRequest,
    ) -> emr_studio_20231009_models.DescribeWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.describe_workflow_instance_with_options(project_id, workflow_instance_id, request, headers, runtime)

    async def describe_workflow_instance_async(
        self,
        project_id: str,
        workflow_instance_id: str,
        request: emr_studio_20231009_models.DescribeWorkflowInstanceRequest,
    ) -> emr_studio_20231009_models.DescribeWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.describe_workflow_instance_with_options_async(project_id, workflow_instance_id, request, headers, runtime)

    def list_manual_task_instances_with_options(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListManualTaskInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.ListManualTaskInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.execution_status):
            query['executionStatus'] = request.execution_status
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListManualTaskInstances',
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/manualTaskInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListManualTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_manual_task_instances_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListManualTaskInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.ListManualTaskInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.execution_status):
            query['executionStatus'] = request.execution_status
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
        if not UtilClient.is_unset(request.workspace_id):
            query['workspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListManualTaskInstances',
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/manualTaskInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListManualTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_manual_task_instances(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListManualTaskInstancesRequest,
    ) -> emr_studio_20231009_models.ListManualTaskInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_manual_task_instances_with_options(project_id, request, headers, runtime)

    async def list_manual_task_instances_async(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListManualTaskInstancesRequest,
    ) -> emr_studio_20231009_models.ListManualTaskInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_manual_task_instances_with_options_async(project_id, request, headers, runtime)

    def list_manual_tasks_with_options(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListManualTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.ListManualTasksResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/manualTasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListManualTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_manual_tasks_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListManualTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.ListManualTasksResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/manualTasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListManualTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_manual_tasks(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListManualTasksRequest,
    ) -> emr_studio_20231009_models.ListManualTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_manual_tasks_with_options(project_id, request, headers, runtime)

    async def list_manual_tasks_async(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListManualTasksRequest,
    ) -> emr_studio_20231009_models.ListManualTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_manual_tasks_with_options_async(project_id, request, headers, runtime)

    def list_projects_with_options(
        self,
        request: emr_studio_20231009_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.ListProjectsResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_projects_with_options_async(
        self,
        request: emr_studio_20231009_models.ListProjectsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.ListProjectsResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListProjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_projects(
        self,
        request: emr_studio_20231009_models.ListProjectsRequest,
    ) -> emr_studio_20231009_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_projects_with_options(request, headers, runtime)

    async def list_projects_async(
        self,
        request: emr_studio_20231009_models.ListProjectsRequest,
    ) -> emr_studio_20231009_models.ListProjectsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_projects_with_options_async(request, headers, runtime)

    def list_task_instances_with_options(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListTaskInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.ListTaskInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.execution_status):
            query['executionStatus'] = request.execution_status
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/taskInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListTaskInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_task_instances_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListTaskInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.ListTaskInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['endTime'] = request.end_time
        if not UtilClient.is_unset(request.execution_status):
            query['executionStatus'] = request.execution_status
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.search_val):
            query['searchVal'] = request.search_val
        if not UtilClient.is_unset(request.start_time):
            query['startTime'] = request.start_time
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/taskInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListTaskInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_task_instances(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListTaskInstancesRequest,
    ) -> emr_studio_20231009_models.ListTaskInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_task_instances_with_options(project_id, request, headers, runtime)

    async def list_task_instances_async(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListTaskInstancesRequest,
    ) -> emr_studio_20231009_models.ListTaskInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_task_instances_with_options_async(project_id, request, headers, runtime)

    def list_tasks_with_options(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.ListTasksResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListTasksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.ListTasksResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/tasks',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListTasksRequest,
    ) -> emr_studio_20231009_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_tasks_with_options(project_id, request, headers, runtime)

    async def list_tasks_async(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListTasksRequest,
    ) -> emr_studio_20231009_models.ListTasksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_tasks_with_options_async(project_id, request, headers, runtime)

    def list_workflow_instances_with_options(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListWorkflowInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.ListWorkflowInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_date):
            query['startDate'] = request.start_date
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/processInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListWorkflowInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workflow_instances_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListWorkflowInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.ListWorkflowInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        if not UtilClient.is_unset(request.max_results):
            query['maxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['nextToken'] = request.next_token
        if not UtilClient.is_unset(request.start_date):
            query['startDate'] = request.start_date
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/processInstances',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListWorkflowInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workflow_instances(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListWorkflowInstancesRequest,
    ) -> emr_studio_20231009_models.ListWorkflowInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workflow_instances_with_options(project_id, request, headers, runtime)

    async def list_workflow_instances_async(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListWorkflowInstancesRequest,
    ) -> emr_studio_20231009_models.ListWorkflowInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workflow_instances_with_options_async(project_id, request, headers, runtime)

    def list_workflows_with_options(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListWorkflowsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.ListWorkflowsResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/processDefinitions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListWorkflowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workflows_with_options_async(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListWorkflowsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> emr_studio_20231009_models.ListWorkflowsResponse:
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
            version='2023-10-09',
            protocol='HTTPS',
            pathname=f'/dolphinscheduler/v3/projects/{OpenApiUtilClient.get_encode_param(project_id)}/processDefinitions',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_studio_20231009_models.ListWorkflowsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workflows(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListWorkflowsRequest,
    ) -> emr_studio_20231009_models.ListWorkflowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_workflows_with_options(project_id, request, headers, runtime)

    async def list_workflows_async(
        self,
        project_id: str,
        request: emr_studio_20231009_models.ListWorkflowsRequest,
    ) -> emr_studio_20231009_models.ListWorkflowsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_workflows_with_options_async(project_id, request, headers, runtime)
