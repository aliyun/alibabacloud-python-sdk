# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eflo_controller20221215 import models as eflo_controller_20221215_models
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
        self._endpoint = self.get_endpoint('eflo-controller', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def approve_operation_with_options(
        self,
        request: eflo_controller_20221215_models.ApproveOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ApproveOperationResponse:
        """
        @summary Approves an O\\&M operation.
        
        @param request: ApproveOperationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApproveOperationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApproveOperation',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ApproveOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def approve_operation_with_options_async(
        self,
        request: eflo_controller_20221215_models.ApproveOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ApproveOperationResponse:
        """
        @summary Approves an O\\&M operation.
        
        @param request: ApproveOperationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApproveOperationResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApproveOperation',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ApproveOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def approve_operation(
        self,
        request: eflo_controller_20221215_models.ApproveOperationRequest,
    ) -> eflo_controller_20221215_models.ApproveOperationResponse:
        """
        @summary Approves an O\\&M operation.
        
        @param request: ApproveOperationRequest
        @return: ApproveOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.approve_operation_with_options(request, runtime)

    async def approve_operation_async(
        self,
        request: eflo_controller_20221215_models.ApproveOperationRequest,
    ) -> eflo_controller_20221215_models.ApproveOperationResponse:
        """
        @summary Approves an O\\&M operation.
        
        @param request: ApproveOperationRequest
        @return: ApproveOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.approve_operation_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: eflo_controller_20221215_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ChangeResourceGroupResponse:
        """
        @summary Moves a resource from one resource group to another.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: eflo_controller_20221215_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ChangeResourceGroupResponse:
        """
        @summary Moves a resource from one resource group to another.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: eflo_controller_20221215_models.ChangeResourceGroupRequest,
    ) -> eflo_controller_20221215_models.ChangeResourceGroupResponse:
        """
        @summary Moves a resource from one resource group to another.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: eflo_controller_20221215_models.ChangeResourceGroupRequest,
    ) -> eflo_controller_20221215_models.ChangeResourceGroupResponse:
        """
        @summary Moves a resource from one resource group to another.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def close_session_with_options(
        self,
        request: eflo_controller_20221215_models.CloseSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.CloseSessionResponse:
        """
        @summary Disconnect Connection
        
        @param request: CloseSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.session_token):
            body['SessionToken'] = request.session_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseSession',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.CloseSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_session_with_options_async(
        self,
        request: eflo_controller_20221215_models.CloseSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.CloseSessionResponse:
        """
        @summary Disconnect Connection
        
        @param request: CloseSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CloseSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.session_token):
            body['SessionToken'] = request.session_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseSession',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.CloseSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_session(
        self,
        request: eflo_controller_20221215_models.CloseSessionRequest,
    ) -> eflo_controller_20221215_models.CloseSessionResponse:
        """
        @summary Disconnect Connection
        
        @param request: CloseSessionRequest
        @return: CloseSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.close_session_with_options(request, runtime)

    async def close_session_async(
        self,
        request: eflo_controller_20221215_models.CloseSessionRequest,
    ) -> eflo_controller_20221215_models.CloseSessionResponse:
        """
        @summary Disconnect Connection
        
        @param request: CloseSessionRequest
        @return: CloseSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.close_session_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.CreateClusterResponse:
        """
        @summary Create a large-scale computing cluster
        
        @param tmp_req: CreateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.CreateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.components):
            request.components_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not UtilClient.is_unset(tmp_req.networks):
            request.networks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.networks, 'Networks', 'json')
        if not UtilClient.is_unset(tmp_req.nimiz_vswitches):
            request.nimiz_vswitches_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.nimiz_vswitches, 'NimizVSwitches', 'json')
        if not UtilClient.is_unset(tmp_req.node_groups):
            request.node_groups_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_groups, 'NodeGroups', 'json')
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.cluster_description):
            body['ClusterDescription'] = request.cluster_description
        if not UtilClient.is_unset(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_type):
            body['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.components_shrink):
            body['Components'] = request.components_shrink
        if not UtilClient.is_unset(request.hpn_zone):
            body['HpnZone'] = request.hpn_zone
        if not UtilClient.is_unset(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not UtilClient.is_unset(request.networks_shrink):
            body['Networks'] = request.networks_shrink
        if not UtilClient.is_unset(request.nimiz_vswitches_shrink):
            body['NimizVSwitches'] = request.nimiz_vswitches_shrink
        if not UtilClient.is_unset(request.node_groups_shrink):
            body['NodeGroups'] = request.node_groups_shrink
        if not UtilClient.is_unset(request.open_eni_jumbo_frame):
            body['OpenEniJumboFrame'] = request.open_eni_jumbo_frame
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        tmp_req: eflo_controller_20221215_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.CreateClusterResponse:
        """
        @summary Create a large-scale computing cluster
        
        @param tmp_req: CreateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.CreateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.components):
            request.components_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not UtilClient.is_unset(tmp_req.networks):
            request.networks_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.networks, 'Networks', 'json')
        if not UtilClient.is_unset(tmp_req.nimiz_vswitches):
            request.nimiz_vswitches_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.nimiz_vswitches, 'NimizVSwitches', 'json')
        if not UtilClient.is_unset(tmp_req.node_groups):
            request.node_groups_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_groups, 'NodeGroups', 'json')
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.cluster_description):
            body['ClusterDescription'] = request.cluster_description
        if not UtilClient.is_unset(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_type):
            body['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.components_shrink):
            body['Components'] = request.components_shrink
        if not UtilClient.is_unset(request.hpn_zone):
            body['HpnZone'] = request.hpn_zone
        if not UtilClient.is_unset(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not UtilClient.is_unset(request.networks_shrink):
            body['Networks'] = request.networks_shrink
        if not UtilClient.is_unset(request.nimiz_vswitches_shrink):
            body['NimizVSwitches'] = request.nimiz_vswitches_shrink
        if not UtilClient.is_unset(request.node_groups_shrink):
            body['NodeGroups'] = request.node_groups_shrink
        if not UtilClient.is_unset(request.open_eni_jumbo_frame):
            body['OpenEniJumboFrame'] = request.open_eni_jumbo_frame
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: eflo_controller_20221215_models.CreateClusterRequest,
    ) -> eflo_controller_20221215_models.CreateClusterResponse:
        """
        @summary Create a large-scale computing cluster
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: eflo_controller_20221215_models.CreateClusterRequest,
    ) -> eflo_controller_20221215_models.CreateClusterResponse:
        """
        @summary Create a large-scale computing cluster
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_diagnostic_task_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.CreateDiagnosticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.CreateDiagnosticTaskResponse:
        """
        @summary Creates a diagnostics task.
        
        @param tmp_req: CreateDiagnosticTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDiagnosticTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.CreateDiagnosticTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ai_job_log_info):
            request.ai_job_log_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ai_job_log_info, 'AiJobLogInfo', 'json')
        if not UtilClient.is_unset(tmp_req.node_ids):
            request.node_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_ids, 'NodeIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.ai_job_log_info_shrink):
            body['AiJobLogInfo'] = request.ai_job_log_info_shrink
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.diagnostic_type):
            body['DiagnosticType'] = request.diagnostic_type
        if not UtilClient.is_unset(request.node_ids_shrink):
            body['NodeIds'] = request.node_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDiagnosticTask',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.CreateDiagnosticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_diagnostic_task_with_options_async(
        self,
        tmp_req: eflo_controller_20221215_models.CreateDiagnosticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.CreateDiagnosticTaskResponse:
        """
        @summary Creates a diagnostics task.
        
        @param tmp_req: CreateDiagnosticTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDiagnosticTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.CreateDiagnosticTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ai_job_log_info):
            request.ai_job_log_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ai_job_log_info, 'AiJobLogInfo', 'json')
        if not UtilClient.is_unset(tmp_req.node_ids):
            request.node_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_ids, 'NodeIds', 'simple')
        body = {}
        if not UtilClient.is_unset(request.ai_job_log_info_shrink):
            body['AiJobLogInfo'] = request.ai_job_log_info_shrink
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.diagnostic_type):
            body['DiagnosticType'] = request.diagnostic_type
        if not UtilClient.is_unset(request.node_ids_shrink):
            body['NodeIds'] = request.node_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDiagnosticTask',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.CreateDiagnosticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_diagnostic_task(
        self,
        request: eflo_controller_20221215_models.CreateDiagnosticTaskRequest,
    ) -> eflo_controller_20221215_models.CreateDiagnosticTaskResponse:
        """
        @summary Creates a diagnostics task.
        
        @param request: CreateDiagnosticTaskRequest
        @return: CreateDiagnosticTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_diagnostic_task_with_options(request, runtime)

    async def create_diagnostic_task_async(
        self,
        request: eflo_controller_20221215_models.CreateDiagnosticTaskRequest,
    ) -> eflo_controller_20221215_models.CreateDiagnosticTaskResponse:
        """
        @summary Creates a diagnostics task.
        
        @param request: CreateDiagnosticTaskRequest
        @return: CreateDiagnosticTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_diagnostic_task_with_options_async(request, runtime)

    def create_net_test_task_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.CreateNetTestTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.CreateNetTestTaskResponse:
        """
        @summary Creates a network test task.
        
        @description The API creates a session, returns the frontend endpoint, and starts a periodic task to track the session status.
        
        @param tmp_req: CreateNetTestTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetTestTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.CreateNetTestTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.comm_test):
            request.comm_test_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.comm_test, 'CommTest', 'json')
        if not UtilClient.is_unset(tmp_req.delay_test):
            request.delay_test_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.delay_test, 'DelayTest', 'json')
        if not UtilClient.is_unset(tmp_req.traffic_test):
            request.traffic_test_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.traffic_test, 'TrafficTest', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.comm_test_shrink):
            body['CommTest'] = request.comm_test_shrink
        if not UtilClient.is_unset(request.delay_test_shrink):
            body['DelayTest'] = request.delay_test_shrink
        if not UtilClient.is_unset(request.net_test_type):
            body['NetTestType'] = request.net_test_type
        if not UtilClient.is_unset(request.network_mode):
            body['NetworkMode'] = request.network_mode
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.traffic_test_shrink):
            body['TrafficTest'] = request.traffic_test_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNetTestTask',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.CreateNetTestTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_net_test_task_with_options_async(
        self,
        tmp_req: eflo_controller_20221215_models.CreateNetTestTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.CreateNetTestTaskResponse:
        """
        @summary Creates a network test task.
        
        @description The API creates a session, returns the frontend endpoint, and starts a periodic task to track the session status.
        
        @param tmp_req: CreateNetTestTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNetTestTaskResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.CreateNetTestTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.comm_test):
            request.comm_test_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.comm_test, 'CommTest', 'json')
        if not UtilClient.is_unset(tmp_req.delay_test):
            request.delay_test_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.delay_test, 'DelayTest', 'json')
        if not UtilClient.is_unset(tmp_req.traffic_test):
            request.traffic_test_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.traffic_test, 'TrafficTest', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.comm_test_shrink):
            body['CommTest'] = request.comm_test_shrink
        if not UtilClient.is_unset(request.delay_test_shrink):
            body['DelayTest'] = request.delay_test_shrink
        if not UtilClient.is_unset(request.net_test_type):
            body['NetTestType'] = request.net_test_type
        if not UtilClient.is_unset(request.network_mode):
            body['NetworkMode'] = request.network_mode
        if not UtilClient.is_unset(request.port):
            body['Port'] = request.port
        if not UtilClient.is_unset(request.traffic_test_shrink):
            body['TrafficTest'] = request.traffic_test_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNetTestTask',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.CreateNetTestTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_net_test_task(
        self,
        request: eflo_controller_20221215_models.CreateNetTestTaskRequest,
    ) -> eflo_controller_20221215_models.CreateNetTestTaskResponse:
        """
        @summary Creates a network test task.
        
        @description The API creates a session, returns the frontend endpoint, and starts a periodic task to track the session status.
        
        @param request: CreateNetTestTaskRequest
        @return: CreateNetTestTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_net_test_task_with_options(request, runtime)

    async def create_net_test_task_async(
        self,
        request: eflo_controller_20221215_models.CreateNetTestTaskRequest,
    ) -> eflo_controller_20221215_models.CreateNetTestTaskResponse:
        """
        @summary Creates a network test task.
        
        @description The API creates a session, returns the frontend endpoint, and starts a periodic task to track the session status.
        
        @param request: CreateNetTestTaskRequest
        @return: CreateNetTestTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_net_test_task_with_options_async(request, runtime)

    def create_node_group_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.CreateNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.CreateNodeGroupResponse:
        """
        @summary Create Node Group under Cluster
        
        @param tmp_req: CreateNodeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNodeGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.CreateNodeGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_group):
            request.node_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_group, 'NodeGroup', 'json')
        if not UtilClient.is_unset(tmp_req.node_unit):
            request.node_unit_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_unit, 'NodeUnit', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_group_shrink):
            body['NodeGroup'] = request.node_group_shrink
        if not UtilClient.is_unset(request.node_unit_shrink):
            body['NodeUnit'] = request.node_unit_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNodeGroup',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.CreateNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_node_group_with_options_async(
        self,
        tmp_req: eflo_controller_20221215_models.CreateNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.CreateNodeGroupResponse:
        """
        @summary Create Node Group under Cluster
        
        @param tmp_req: CreateNodeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNodeGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.CreateNodeGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_group):
            request.node_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_group, 'NodeGroup', 'json')
        if not UtilClient.is_unset(tmp_req.node_unit):
            request.node_unit_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_unit, 'NodeUnit', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_group_shrink):
            body['NodeGroup'] = request.node_group_shrink
        if not UtilClient.is_unset(request.node_unit_shrink):
            body['NodeUnit'] = request.node_unit_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNodeGroup',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.CreateNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_node_group(
        self,
        request: eflo_controller_20221215_models.CreateNodeGroupRequest,
    ) -> eflo_controller_20221215_models.CreateNodeGroupResponse:
        """
        @summary Create Node Group under Cluster
        
        @param request: CreateNodeGroupRequest
        @return: CreateNodeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_node_group_with_options(request, runtime)

    async def create_node_group_async(
        self,
        request: eflo_controller_20221215_models.CreateNodeGroupRequest,
    ) -> eflo_controller_20221215_models.CreateNodeGroupResponse:
        """
        @summary Create Node Group under Cluster
        
        @param request: CreateNodeGroupRequest
        @return: CreateNodeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_node_group_with_options_async(request, runtime)

    def create_session_with_options(
        self,
        request: eflo_controller_20221215_models.CreateSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.CreateSessionResponse:
        """
        @summary Creates a Web Terminal session.
        
        @description The API creates a session, returns the frontend endpoint, and starts a periodic task to track the session status.
        
        @param request: CreateSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.session_type):
            body['SessionType'] = request.session_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSession',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.CreateSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_session_with_options_async(
        self,
        request: eflo_controller_20221215_models.CreateSessionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.CreateSessionResponse:
        """
        @summary Creates a Web Terminal session.
        
        @description The API creates a session, returns the frontend endpoint, and starts a periodic task to track the session status.
        
        @param request: CreateSessionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSessionResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.session_type):
            body['SessionType'] = request.session_type
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSession',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.CreateSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_session(
        self,
        request: eflo_controller_20221215_models.CreateSessionRequest,
    ) -> eflo_controller_20221215_models.CreateSessionResponse:
        """
        @summary Creates a Web Terminal session.
        
        @description The API creates a session, returns the frontend endpoint, and starts a periodic task to track the session status.
        
        @param request: CreateSessionRequest
        @return: CreateSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_session_with_options(request, runtime)

    async def create_session_async(
        self,
        request: eflo_controller_20221215_models.CreateSessionRequest,
    ) -> eflo_controller_20221215_models.CreateSessionResponse:
        """
        @summary Creates a Web Terminal session.
        
        @description The API creates a session, returns the frontend endpoint, and starts a periodic task to track the session status.
        
        @param request: CreateSessionRequest
        @return: CreateSessionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_session_with_options_async(request, runtime)

    def create_vsc_with_options(
        self,
        request: eflo_controller_20221215_models.CreateVscRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.CreateVscResponse:
        """
        @summary Creates a virtual storage channel (VSC).
        
        @param request: CreateVscRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVscResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vsc_name):
            body['VscName'] = request.vsc_name
        if not UtilClient.is_unset(request.vsc_type):
            body['VscType'] = request.vsc_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVsc',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.CreateVscResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vsc_with_options_async(
        self,
        request: eflo_controller_20221215_models.CreateVscRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.CreateVscResponse:
        """
        @summary Creates a virtual storage channel (VSC).
        
        @param request: CreateVscRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateVscResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.vsc_name):
            body['VscName'] = request.vsc_name
        if not UtilClient.is_unset(request.vsc_type):
            body['VscType'] = request.vsc_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVsc',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.CreateVscResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vsc(
        self,
        request: eflo_controller_20221215_models.CreateVscRequest,
    ) -> eflo_controller_20221215_models.CreateVscResponse:
        """
        @summary Creates a virtual storage channel (VSC).
        
        @param request: CreateVscRequest
        @return: CreateVscResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_vsc_with_options(request, runtime)

    async def create_vsc_async(
        self,
        request: eflo_controller_20221215_models.CreateVscRequest,
    ) -> eflo_controller_20221215_models.CreateVscResponse:
        """
        @summary Creates a virtual storage channel (VSC).
        
        @param request: CreateVscRequest
        @return: CreateVscResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_vsc_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: eflo_controller_20221215_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DeleteClusterResponse:
        """
        @summary Deletes a Lingjun cluster.
        
        @param request: DeleteClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: eflo_controller_20221215_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DeleteClusterResponse:
        """
        @summary Deletes a Lingjun cluster.
        
        @param request: DeleteClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        request: eflo_controller_20221215_models.DeleteClusterRequest,
    ) -> eflo_controller_20221215_models.DeleteClusterResponse:
        """
        @summary Deletes a Lingjun cluster.
        
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: eflo_controller_20221215_models.DeleteClusterRequest,
    ) -> eflo_controller_20221215_models.DeleteClusterResponse:
        """
        @summary Deletes a Lingjun cluster.
        
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def delete_node_group_with_options(
        self,
        request: eflo_controller_20221215_models.DeleteNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DeleteNodeGroupResponse:
        """
        @summary 删除节点分组
        
        @param request: DeleteNodeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNodeGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteNodeGroup',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DeleteNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_node_group_with_options_async(
        self,
        request: eflo_controller_20221215_models.DeleteNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DeleteNodeGroupResponse:
        """
        @summary 删除节点分组
        
        @param request: DeleteNodeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteNodeGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteNodeGroup',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DeleteNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_node_group(
        self,
        request: eflo_controller_20221215_models.DeleteNodeGroupRequest,
    ) -> eflo_controller_20221215_models.DeleteNodeGroupResponse:
        """
        @summary 删除节点分组
        
        @param request: DeleteNodeGroupRequest
        @return: DeleteNodeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_node_group_with_options(request, runtime)

    async def delete_node_group_async(
        self,
        request: eflo_controller_20221215_models.DeleteNodeGroupRequest,
    ) -> eflo_controller_20221215_models.DeleteNodeGroupResponse:
        """
        @summary 删除节点分组
        
        @param request: DeleteNodeGroupRequest
        @return: DeleteNodeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_node_group_with_options_async(request, runtime)

    def delete_vsc_with_options(
        self,
        request: eflo_controller_20221215_models.DeleteVscRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DeleteVscResponse:
        """
        @summary Deletes a virtual storage channel (VSC).
        
        @param request: DeleteVscRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVscResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.vsc_id):
            body['VscId'] = request.vsc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVsc',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DeleteVscResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vsc_with_options_async(
        self,
        request: eflo_controller_20221215_models.DeleteVscRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DeleteVscResponse:
        """
        @summary Deletes a virtual storage channel (VSC).
        
        @param request: DeleteVscRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteVscResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not UtilClient.is_unset(request.vsc_id):
            body['VscId'] = request.vsc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVsc',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DeleteVscResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vsc(
        self,
        request: eflo_controller_20221215_models.DeleteVscRequest,
    ) -> eflo_controller_20221215_models.DeleteVscResponse:
        """
        @summary Deletes a virtual storage channel (VSC).
        
        @param request: DeleteVscRequest
        @return: DeleteVscResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_vsc_with_options(request, runtime)

    async def delete_vsc_async(
        self,
        request: eflo_controller_20221215_models.DeleteVscRequest,
    ) -> eflo_controller_20221215_models.DeleteVscResponse:
        """
        @summary Deletes a virtual storage channel (VSC).
        
        @param request: DeleteVscRequest
        @return: DeleteVscResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_vsc_with_options_async(request, runtime)

    def describe_cluster_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeClusterResponse:
        """
        @summary Queries information about a Lingjun cluster.
        
        @param request: DescribeClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCluster',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_with_options_async(
        self,
        request: eflo_controller_20221215_models.DescribeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeClusterResponse:
        """
        @summary Queries information about a Lingjun cluster.
        
        @param request: DescribeClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeClusterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCluster',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster(
        self,
        request: eflo_controller_20221215_models.DescribeClusterRequest,
    ) -> eflo_controller_20221215_models.DescribeClusterResponse:
        """
        @summary Queries information about a Lingjun cluster.
        
        @param request: DescribeClusterRequest
        @return: DescribeClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_with_options(request, runtime)

    async def describe_cluster_async(
        self,
        request: eflo_controller_20221215_models.DescribeClusterRequest,
    ) -> eflo_controller_20221215_models.DescribeClusterResponse:
        """
        @summary Queries information about a Lingjun cluster.
        
        @param request: DescribeClusterRequest
        @return: DescribeClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_with_options_async(request, runtime)

    def describe_diagnostic_result_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeDiagnosticResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeDiagnosticResultResponse:
        """
        @summary Queries the results of a diagnostic task.
        
        @description The API creates a session, returns the frontend endpoint, and starts a periodic task to track the session status.
        
        @param request: DescribeDiagnosticResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosticResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.diagnostic_id):
            body['DiagnosticId'] = request.diagnostic_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosticResult',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeDiagnosticResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnostic_result_with_options_async(
        self,
        request: eflo_controller_20221215_models.DescribeDiagnosticResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeDiagnosticResultResponse:
        """
        @summary Queries the results of a diagnostic task.
        
        @description The API creates a session, returns the frontend endpoint, and starts a periodic task to track the session status.
        
        @param request: DescribeDiagnosticResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDiagnosticResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.diagnostic_id):
            body['DiagnosticId'] = request.diagnostic_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDiagnosticResult',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeDiagnosticResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnostic_result(
        self,
        request: eflo_controller_20221215_models.DescribeDiagnosticResultRequest,
    ) -> eflo_controller_20221215_models.DescribeDiagnosticResultResponse:
        """
        @summary Queries the results of a diagnostic task.
        
        @description The API creates a session, returns the frontend endpoint, and starts a periodic task to track the session status.
        
        @param request: DescribeDiagnosticResultRequest
        @return: DescribeDiagnosticResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_diagnostic_result_with_options(request, runtime)

    async def describe_diagnostic_result_async(
        self,
        request: eflo_controller_20221215_models.DescribeDiagnosticResultRequest,
    ) -> eflo_controller_20221215_models.DescribeDiagnosticResultResponse:
        """
        @summary Queries the results of a diagnostic task.
        
        @description The API creates a session, returns the frontend endpoint, and starts a periodic task to track the session status.
        
        @param request: DescribeDiagnosticResultRequest
        @return: DescribeDiagnosticResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_diagnostic_result_with_options_async(request, runtime)

    def describe_invocations_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeInvocationsResponse:
        """
        @summary Queries the execution list and status of O\\&M Assistant commands.
        
        @param request: DescribeInvocationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInvocationsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content_encoding):
            body['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.include_output):
            body['IncludeOutput'] = request.include_output
        if not UtilClient.is_unset(request.invoke_id):
            body['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInvocations',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeInvocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invocations_with_options_async(
        self,
        request: eflo_controller_20221215_models.DescribeInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeInvocationsResponse:
        """
        @summary Queries the execution list and status of O\\&M Assistant commands.
        
        @param request: DescribeInvocationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeInvocationsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content_encoding):
            body['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.include_output):
            body['IncludeOutput'] = request.include_output
        if not UtilClient.is_unset(request.invoke_id):
            body['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeInvocations',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeInvocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invocations(
        self,
        request: eflo_controller_20221215_models.DescribeInvocationsRequest,
    ) -> eflo_controller_20221215_models.DescribeInvocationsResponse:
        """
        @summary Queries the execution list and status of O\\&M Assistant commands.
        
        @param request: DescribeInvocationsRequest
        @return: DescribeInvocationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_invocations_with_options(request, runtime)

    async def describe_invocations_async(
        self,
        request: eflo_controller_20221215_models.DescribeInvocationsRequest,
    ) -> eflo_controller_20221215_models.DescribeInvocationsResponse:
        """
        @summary Queries the execution list and status of O\\&M Assistant commands.
        
        @param request: DescribeInvocationsRequest
        @return: DescribeInvocationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_invocations_with_options_async(request, runtime)

    def describe_net_test_result_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeNetTestResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeNetTestResultResponse:
        """
        @summary Query Network Test Result
        
        @param request: DescribeNetTestResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNetTestResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.test_id):
            body['TestId'] = request.test_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNetTestResult',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeNetTestResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_net_test_result_with_options_async(
        self,
        request: eflo_controller_20221215_models.DescribeNetTestResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeNetTestResultResponse:
        """
        @summary Query Network Test Result
        
        @param request: DescribeNetTestResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNetTestResultResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.test_id):
            body['TestId'] = request.test_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNetTestResult',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeNetTestResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_net_test_result(
        self,
        request: eflo_controller_20221215_models.DescribeNetTestResultRequest,
    ) -> eflo_controller_20221215_models.DescribeNetTestResultResponse:
        """
        @summary Query Network Test Result
        
        @param request: DescribeNetTestResultRequest
        @return: DescribeNetTestResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_net_test_result_with_options(request, runtime)

    async def describe_net_test_result_async(
        self,
        request: eflo_controller_20221215_models.DescribeNetTestResultRequest,
    ) -> eflo_controller_20221215_models.DescribeNetTestResultResponse:
        """
        @summary Query Network Test Result
        
        @param request: DescribeNetTestResultRequest
        @return: DescribeNetTestResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_net_test_result_with_options_async(request, runtime)

    def describe_node_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeNodeResponse:
        """
        @summary Queries a list of nodes.
        
        @param request: DescribeNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNode',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_node_with_options_async(
        self,
        request: eflo_controller_20221215_models.DescribeNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeNodeResponse:
        """
        @summary Queries a list of nodes.
        
        @param request: DescribeNodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNode',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_node(
        self,
        request: eflo_controller_20221215_models.DescribeNodeRequest,
    ) -> eflo_controller_20221215_models.DescribeNodeResponse:
        """
        @summary Queries a list of nodes.
        
        @param request: DescribeNodeRequest
        @return: DescribeNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_node_with_options(request, runtime)

    async def describe_node_async(
        self,
        request: eflo_controller_20221215_models.DescribeNodeRequest,
    ) -> eflo_controller_20221215_models.DescribeNodeResponse:
        """
        @summary Queries a list of nodes.
        
        @param request: DescribeNodeRequest
        @return: DescribeNodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_node_with_options_async(request, runtime)

    def describe_node_type_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeNodeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeNodeTypeResponse:
        """
        @summary 创建Web Terminal会话
        
        @param request: DescribeNodeTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodeTypeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_type):
            body['NodeType'] = request.node_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNodeType',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeNodeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_node_type_with_options_async(
        self,
        request: eflo_controller_20221215_models.DescribeNodeTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeNodeTypeResponse:
        """
        @summary 创建Web Terminal会话
        
        @param request: DescribeNodeTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodeTypeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.node_type):
            body['NodeType'] = request.node_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNodeType',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeNodeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_node_type(
        self,
        request: eflo_controller_20221215_models.DescribeNodeTypeRequest,
    ) -> eflo_controller_20221215_models.DescribeNodeTypeResponse:
        """
        @summary 创建Web Terminal会话
        
        @param request: DescribeNodeTypeRequest
        @return: DescribeNodeTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_node_type_with_options(request, runtime)

    async def describe_node_type_async(
        self,
        request: eflo_controller_20221215_models.DescribeNodeTypeRequest,
    ) -> eflo_controller_20221215_models.DescribeNodeTypeResponse:
        """
        @summary 创建Web Terminal会话
        
        @param request: DescribeNodeTypeRequest
        @return: DescribeNodeTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_node_type_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeRegionsResponse:
        """
        @summary Queries a list of regions.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: eflo_controller_20221215_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeRegionsResponse:
        """
        @summary Queries a list of regions.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: eflo_controller_20221215_models.DescribeRegionsRequest,
    ) -> eflo_controller_20221215_models.DescribeRegionsResponse:
        """
        @summary Queries a list of regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: eflo_controller_20221215_models.DescribeRegionsRequest,
    ) -> eflo_controller_20221215_models.DescribeRegionsResponse:
        """
        @summary Queries a list of regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_send_file_results_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeSendFileResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeSendFileResultsResponse:
        """
        @summary Queries the files that are sent by an O\\&M assistant and the status of the files.
        
        @param request: DescribeSendFileResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSendFileResultsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.invoke_id):
            body['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSendFileResults',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeSendFileResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_send_file_results_with_options_async(
        self,
        request: eflo_controller_20221215_models.DescribeSendFileResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeSendFileResultsResponse:
        """
        @summary Queries the files that are sent by an O\\&M assistant and the status of the files.
        
        @param request: DescribeSendFileResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSendFileResultsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.invoke_id):
            body['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSendFileResults',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeSendFileResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_send_file_results(
        self,
        request: eflo_controller_20221215_models.DescribeSendFileResultsRequest,
    ) -> eflo_controller_20221215_models.DescribeSendFileResultsResponse:
        """
        @summary Queries the files that are sent by an O\\&M assistant and the status of the files.
        
        @param request: DescribeSendFileResultsRequest
        @return: DescribeSendFileResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_send_file_results_with_options(request, runtime)

    async def describe_send_file_results_async(
        self,
        request: eflo_controller_20221215_models.DescribeSendFileResultsRequest,
    ) -> eflo_controller_20221215_models.DescribeSendFileResultsResponse:
        """
        @summary Queries the files that are sent by an O\\&M assistant and the status of the files.
        
        @param request: DescribeSendFileResultsRequest
        @return: DescribeSendFileResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_send_file_results_with_options_async(request, runtime)

    def describe_task_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeTaskResponse:
        """
        @summary Queries the details of a task.
        
        @param request: DescribeTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTask',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_task_with_options_async(
        self,
        request: eflo_controller_20221215_models.DescribeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeTaskResponse:
        """
        @summary Queries the details of a task.
        
        @param request: DescribeTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeTaskResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTask',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_task(
        self,
        request: eflo_controller_20221215_models.DescribeTaskRequest,
    ) -> eflo_controller_20221215_models.DescribeTaskResponse:
        """
        @summary Queries the details of a task.
        
        @param request: DescribeTaskRequest
        @return: DescribeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_task_with_options(request, runtime)

    async def describe_task_async(
        self,
        request: eflo_controller_20221215_models.DescribeTaskRequest,
    ) -> eflo_controller_20221215_models.DescribeTaskResponse:
        """
        @summary Queries the details of a task.
        
        @param request: DescribeTaskRequest
        @return: DescribeTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_task_with_options_async(request, runtime)

    def describe_vsc_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeVscRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeVscResponse:
        """
        @summary Queries information about a virtual storage channel (VSC).
        
        @param request: DescribeVscRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVscResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.vsc_id):
            body['VscId'] = request.vsc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeVsc',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeVscResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vsc_with_options_async(
        self,
        request: eflo_controller_20221215_models.DescribeVscRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeVscResponse:
        """
        @summary Queries information about a virtual storage channel (VSC).
        
        @param request: DescribeVscRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeVscResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.vsc_id):
            body['VscId'] = request.vsc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeVsc',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeVscResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vsc(
        self,
        request: eflo_controller_20221215_models.DescribeVscRequest,
    ) -> eflo_controller_20221215_models.DescribeVscResponse:
        """
        @summary Queries information about a virtual storage channel (VSC).
        
        @param request: DescribeVscRequest
        @return: DescribeVscResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_vsc_with_options(request, runtime)

    async def describe_vsc_async(
        self,
        request: eflo_controller_20221215_models.DescribeVscRequest,
    ) -> eflo_controller_20221215_models.DescribeVscResponse:
        """
        @summary Queries information about a virtual storage channel (VSC).
        
        @param request: DescribeVscRequest
        @return: DescribeVscResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_vsc_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeZonesResponse:
        """
        @summary Queries a list of zones.
        
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: eflo_controller_20221215_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeZonesResponse:
        """
        @summary Queries a list of zones.
        
        @param request: DescribeZonesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeZonesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: eflo_controller_20221215_models.DescribeZonesRequest,
    ) -> eflo_controller_20221215_models.DescribeZonesResponse:
        """
        @summary Queries a list of zones.
        
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: eflo_controller_20221215_models.DescribeZonesRequest,
    ) -> eflo_controller_20221215_models.DescribeZonesResponse:
        """
        @summary Queries a list of zones.
        
        @param request: DescribeZonesRequest
        @return: DescribeZonesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def extend_cluster_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.ExtendClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ExtendClusterResponse:
        """
        @summary Cluster Scaling
        
        @param tmp_req: ExtendClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExtendClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.ExtendClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ip_allocation_policy):
            request.ip_allocation_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip_allocation_policy, 'IpAllocationPolicy', 'json')
        if not UtilClient.is_unset(tmp_req.node_groups):
            request.node_groups_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_groups, 'NodeGroups', 'json')
        if not UtilClient.is_unset(tmp_req.vpd_subnets):
            request.vpd_subnets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vpd_subnets, 'VpdSubnets', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not UtilClient.is_unset(request.ip_allocation_policy_shrink):
            body['IpAllocationPolicy'] = request.ip_allocation_policy_shrink
        if not UtilClient.is_unset(request.node_groups_shrink):
            body['NodeGroups'] = request.node_groups_shrink
        if not UtilClient.is_unset(request.v_switch_zone_id):
            body['VSwitchZoneId'] = request.v_switch_zone_id
        if not UtilClient.is_unset(request.vpd_subnets_shrink):
            body['VpdSubnets'] = request.vpd_subnets_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtendCluster',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ExtendClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def extend_cluster_with_options_async(
        self,
        tmp_req: eflo_controller_20221215_models.ExtendClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ExtendClusterResponse:
        """
        @summary Cluster Scaling
        
        @param tmp_req: ExtendClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExtendClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.ExtendClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.ip_allocation_policy):
            request.ip_allocation_policy_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.ip_allocation_policy, 'IpAllocationPolicy', 'json')
        if not UtilClient.is_unset(tmp_req.node_groups):
            request.node_groups_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_groups, 'NodeGroups', 'json')
        if not UtilClient.is_unset(tmp_req.vpd_subnets):
            request.vpd_subnets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vpd_subnets, 'VpdSubnets', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not UtilClient.is_unset(request.ip_allocation_policy_shrink):
            body['IpAllocationPolicy'] = request.ip_allocation_policy_shrink
        if not UtilClient.is_unset(request.node_groups_shrink):
            body['NodeGroups'] = request.node_groups_shrink
        if not UtilClient.is_unset(request.v_switch_zone_id):
            body['VSwitchZoneId'] = request.v_switch_zone_id
        if not UtilClient.is_unset(request.vpd_subnets_shrink):
            body['VpdSubnets'] = request.vpd_subnets_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExtendCluster',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ExtendClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def extend_cluster(
        self,
        request: eflo_controller_20221215_models.ExtendClusterRequest,
    ) -> eflo_controller_20221215_models.ExtendClusterResponse:
        """
        @summary Cluster Scaling
        
        @param request: ExtendClusterRequest
        @return: ExtendClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.extend_cluster_with_options(request, runtime)

    async def extend_cluster_async(
        self,
        request: eflo_controller_20221215_models.ExtendClusterRequest,
    ) -> eflo_controller_20221215_models.ExtendClusterResponse:
        """
        @summary Cluster Scaling
        
        @param request: ExtendClusterRequest
        @return: ExtendClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.extend_cluster_with_options_async(request, runtime)

    def list_cluster_nodes_with_options(
        self,
        request: eflo_controller_20221215_models.ListClusterNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListClusterNodesResponse:
        """
        @summary Queries a list of nodes in a cluster.
        
        @param request: ListClusterNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterNodes',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListClusterNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_nodes_with_options_async(
        self,
        request: eflo_controller_20221215_models.ListClusterNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListClusterNodesResponse:
        """
        @summary Queries a list of nodes in a cluster.
        
        @param request: ListClusterNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClusterNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterNodes',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListClusterNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_nodes(
        self,
        request: eflo_controller_20221215_models.ListClusterNodesRequest,
    ) -> eflo_controller_20221215_models.ListClusterNodesResponse:
        """
        @summary Queries a list of nodes in a cluster.
        
        @param request: ListClusterNodesRequest
        @return: ListClusterNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_nodes_with_options(request, runtime)

    async def list_cluster_nodes_async(
        self,
        request: eflo_controller_20221215_models.ListClusterNodesRequest,
    ) -> eflo_controller_20221215_models.ListClusterNodesResponse:
        """
        @summary Queries a list of nodes in a cluster.
        
        @param request: ListClusterNodesRequest
        @return: ListClusterNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_nodes_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: eflo_controller_20221215_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListClustersResponse:
        """
        @summary Queries a list of clusters.
        
        @param request: ListClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: eflo_controller_20221215_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListClustersResponse:
        """
        @summary Queries a list of clusters.
        
        @param request: ListClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        request: eflo_controller_20221215_models.ListClustersRequest,
    ) -> eflo_controller_20221215_models.ListClustersResponse:
        """
        @summary Queries a list of clusters.
        
        @param request: ListClustersRequest
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: eflo_controller_20221215_models.ListClustersRequest,
    ) -> eflo_controller_20221215_models.ListClustersResponse:
        """
        @summary Queries a list of clusters.
        
        @param request: ListClustersRequest
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_diagnostic_results_with_options(
        self,
        request: eflo_controller_20221215_models.ListDiagnosticResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListDiagnosticResultsResponse:
        """
        @summary List of Diagnostic Tasks
        
        @param request: ListDiagnosticResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDiagnosticResultsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.diag_type):
            body['DiagType'] = request.diag_type
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDiagnosticResults',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListDiagnosticResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_diagnostic_results_with_options_async(
        self,
        request: eflo_controller_20221215_models.ListDiagnosticResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListDiagnosticResultsResponse:
        """
        @summary List of Diagnostic Tasks
        
        @param request: ListDiagnosticResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDiagnosticResultsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.diag_type):
            body['DiagType'] = request.diag_type
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDiagnosticResults',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListDiagnosticResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_diagnostic_results(
        self,
        request: eflo_controller_20221215_models.ListDiagnosticResultsRequest,
    ) -> eflo_controller_20221215_models.ListDiagnosticResultsResponse:
        """
        @summary List of Diagnostic Tasks
        
        @param request: ListDiagnosticResultsRequest
        @return: ListDiagnosticResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_diagnostic_results_with_options(request, runtime)

    async def list_diagnostic_results_async(
        self,
        request: eflo_controller_20221215_models.ListDiagnosticResultsRequest,
    ) -> eflo_controller_20221215_models.ListDiagnosticResultsResponse:
        """
        @summary List of Diagnostic Tasks
        
        @param request: ListDiagnosticResultsRequest
        @return: ListDiagnosticResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_diagnostic_results_with_options_async(request, runtime)

    def list_free_nodes_with_options(
        self,
        request: eflo_controller_20221215_models.ListFreeNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListFreeNodesResponse:
        """
        @summary Queries a list of nodes that are not used.
        
        @param request: ListFreeNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFreeNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not UtilClient.is_unset(request.hpn_zone):
            body['HpnZone'] = request.hpn_zone
        if not UtilClient.is_unset(request.machine_type):
            body['MachineType'] = request.machine_type
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.operating_states):
            body['OperatingStates'] = request.operating_states
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFreeNodes',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListFreeNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_free_nodes_with_options_async(
        self,
        request: eflo_controller_20221215_models.ListFreeNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListFreeNodesResponse:
        """
        @summary Queries a list of nodes that are not used.
        
        @param request: ListFreeNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListFreeNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not UtilClient.is_unset(request.hpn_zone):
            body['HpnZone'] = request.hpn_zone
        if not UtilClient.is_unset(request.machine_type):
            body['MachineType'] = request.machine_type
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.operating_states):
            body['OperatingStates'] = request.operating_states
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFreeNodes',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListFreeNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_free_nodes(
        self,
        request: eflo_controller_20221215_models.ListFreeNodesRequest,
    ) -> eflo_controller_20221215_models.ListFreeNodesResponse:
        """
        @summary Queries a list of nodes that are not used.
        
        @param request: ListFreeNodesRequest
        @return: ListFreeNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_free_nodes_with_options(request, runtime)

    async def list_free_nodes_async(
        self,
        request: eflo_controller_20221215_models.ListFreeNodesRequest,
    ) -> eflo_controller_20221215_models.ListFreeNodesResponse:
        """
        @summary Queries a list of nodes that are not used.
        
        @param request: ListFreeNodesRequest
        @return: ListFreeNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_free_nodes_with_options_async(request, runtime)

    def list_images_with_options(
        self,
        request: eflo_controller_20221215_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListImagesResponse:
        """
        @summary Lists available images.
        
        @param request: ListImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImagesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.architecture):
            body['Architecture'] = request.architecture
        if not UtilClient.is_unset(request.image_version):
            body['ImageVersion'] = request.image_version
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: eflo_controller_20221215_models.ListImagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListImagesResponse:
        """
        @summary Lists available images.
        
        @param request: ListImagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListImagesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.architecture):
            body['Architecture'] = request.architecture
        if not UtilClient.is_unset(request.image_version):
            body['ImageVersion'] = request.image_version
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListImages',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images(
        self,
        request: eflo_controller_20221215_models.ListImagesRequest,
    ) -> eflo_controller_20221215_models.ListImagesResponse:
        """
        @summary Lists available images.
        
        @param request: ListImagesRequest
        @return: ListImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    async def list_images_async(
        self,
        request: eflo_controller_20221215_models.ListImagesRequest,
    ) -> eflo_controller_20221215_models.ListImagesResponse:
        """
        @summary Lists available images.
        
        @param request: ListImagesRequest
        @return: ListImagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_images_with_options_async(request, runtime)

    def list_machine_network_info_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.ListMachineNetworkInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListMachineNetworkInfoResponse:
        """
        @summary Query machine network configuration using HPNZone and machine type
        
        @param tmp_req: ListMachineNetworkInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMachineNetworkInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.ListMachineNetworkInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.machine_hpn_info):
            request.machine_hpn_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.machine_hpn_info, 'MachineHpnInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.machine_hpn_info_shrink):
            body['MachineHpnInfo'] = request.machine_hpn_info_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMachineNetworkInfo',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListMachineNetworkInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_machine_network_info_with_options_async(
        self,
        tmp_req: eflo_controller_20221215_models.ListMachineNetworkInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListMachineNetworkInfoResponse:
        """
        @summary Query machine network configuration using HPNZone and machine type
        
        @param tmp_req: ListMachineNetworkInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMachineNetworkInfoResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.ListMachineNetworkInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.machine_hpn_info):
            request.machine_hpn_info_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.machine_hpn_info, 'MachineHpnInfo', 'json')
        body = {}
        if not UtilClient.is_unset(request.machine_hpn_info_shrink):
            body['MachineHpnInfo'] = request.machine_hpn_info_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMachineNetworkInfo',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListMachineNetworkInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_machine_network_info(
        self,
        request: eflo_controller_20221215_models.ListMachineNetworkInfoRequest,
    ) -> eflo_controller_20221215_models.ListMachineNetworkInfoResponse:
        """
        @summary Query machine network configuration using HPNZone and machine type
        
        @param request: ListMachineNetworkInfoRequest
        @return: ListMachineNetworkInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_machine_network_info_with_options(request, runtime)

    async def list_machine_network_info_async(
        self,
        request: eflo_controller_20221215_models.ListMachineNetworkInfoRequest,
    ) -> eflo_controller_20221215_models.ListMachineNetworkInfoResponse:
        """
        @summary Query machine network configuration using HPNZone and machine type
        
        @param request: ListMachineNetworkInfoRequest
        @return: ListMachineNetworkInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_machine_network_info_with_options_async(request, runtime)

    def list_machine_types_with_options(
        self,
        request: eflo_controller_20221215_models.ListMachineTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListMachineTypesResponse:
        """
        @summary Queries a list of instance types that are available to users.
        
        @param request: ListMachineTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMachineTypesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMachineTypes',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListMachineTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_machine_types_with_options_async(
        self,
        request: eflo_controller_20221215_models.ListMachineTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListMachineTypesResponse:
        """
        @summary Queries a list of instance types that are available to users.
        
        @param request: ListMachineTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListMachineTypesResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMachineTypes',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListMachineTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_machine_types(
        self,
        request: eflo_controller_20221215_models.ListMachineTypesRequest,
    ) -> eflo_controller_20221215_models.ListMachineTypesResponse:
        """
        @summary Queries a list of instance types that are available to users.
        
        @param request: ListMachineTypesRequest
        @return: ListMachineTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_machine_types_with_options(request, runtime)

    async def list_machine_types_async(
        self,
        request: eflo_controller_20221215_models.ListMachineTypesRequest,
    ) -> eflo_controller_20221215_models.ListMachineTypesResponse:
        """
        @summary Queries a list of instance types that are available to users.
        
        @param request: ListMachineTypesRequest
        @return: ListMachineTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_machine_types_with_options_async(request, runtime)

    def list_net_test_results_with_options(
        self,
        request: eflo_controller_20221215_models.ListNetTestResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListNetTestResultsResponse:
        """
        @summary Lists the results of network test results.
        
        @description The API creates a session, returns the frontend endpoint, and starts a periodic task to track the session status.
        
        @param request: ListNetTestResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetTestResultsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.net_test_type):
            body['NetTestType'] = request.net_test_type
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNetTestResults',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListNetTestResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_net_test_results_with_options_async(
        self,
        request: eflo_controller_20221215_models.ListNetTestResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListNetTestResultsResponse:
        """
        @summary Lists the results of network test results.
        
        @description The API creates a session, returns the frontend endpoint, and starts a periodic task to track the session status.
        
        @param request: ListNetTestResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNetTestResultsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.net_test_type):
            body['NetTestType'] = request.net_test_type
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNetTestResults',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListNetTestResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_net_test_results(
        self,
        request: eflo_controller_20221215_models.ListNetTestResultsRequest,
    ) -> eflo_controller_20221215_models.ListNetTestResultsResponse:
        """
        @summary Lists the results of network test results.
        
        @description The API creates a session, returns the frontend endpoint, and starts a periodic task to track the session status.
        
        @param request: ListNetTestResultsRequest
        @return: ListNetTestResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_net_test_results_with_options(request, runtime)

    async def list_net_test_results_async(
        self,
        request: eflo_controller_20221215_models.ListNetTestResultsRequest,
    ) -> eflo_controller_20221215_models.ListNetTestResultsResponse:
        """
        @summary Lists the results of network test results.
        
        @description The API creates a session, returns the frontend endpoint, and starts a periodic task to track the session status.
        
        @param request: ListNetTestResultsRequest
        @return: ListNetTestResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_net_test_results_with_options_async(request, runtime)

    def list_node_groups_with_options(
        self,
        request: eflo_controller_20221215_models.ListNodeGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListNodeGroupsResponse:
        """
        @summary Queries node groups in a cluster.
        
        @param request: ListNodeGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodeGroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodeGroups',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListNodeGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_groups_with_options_async(
        self,
        request: eflo_controller_20221215_models.ListNodeGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListNodeGroupsResponse:
        """
        @summary Queries node groups in a cluster.
        
        @param request: ListNodeGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodeGroupsResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodeGroups',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListNodeGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_groups(
        self,
        request: eflo_controller_20221215_models.ListNodeGroupsRequest,
    ) -> eflo_controller_20221215_models.ListNodeGroupsResponse:
        """
        @summary Queries node groups in a cluster.
        
        @param request: ListNodeGroupsRequest
        @return: ListNodeGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_node_groups_with_options(request, runtime)

    async def list_node_groups_async(
        self,
        request: eflo_controller_20221215_models.ListNodeGroupsRequest,
    ) -> eflo_controller_20221215_models.ListNodeGroupsResponse:
        """
        @summary Queries node groups in a cluster.
        
        @param request: ListNodeGroupsRequest
        @return: ListNodeGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_node_groups_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: eflo_controller_20221215_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of resources.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: eflo_controller_20221215_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of resources.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: eflo_controller_20221215_models.ListTagResourcesRequest,
    ) -> eflo_controller_20221215_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: eflo_controller_20221215_models.ListTagResourcesRequest,
    ) -> eflo_controller_20221215_models.ListTagResourcesResponse:
        """
        @summary Queries the tags of resources.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_user_cluster_types_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListUserClusterTypesResponse:
        """
        @summary Query the cluster types available to the user
        
        @param request: ListUserClusterTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserClusterTypesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListUserClusterTypes',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListUserClusterTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_cluster_types_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListUserClusterTypesResponse:
        """
        @summary Query the cluster types available to the user
        
        @param request: ListUserClusterTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUserClusterTypesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListUserClusterTypes',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListUserClusterTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_cluster_types(self) -> eflo_controller_20221215_models.ListUserClusterTypesResponse:
        """
        @summary Query the cluster types available to the user
        
        @return: ListUserClusterTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_user_cluster_types_with_options(runtime)

    async def list_user_cluster_types_async(self) -> eflo_controller_20221215_models.ListUserClusterTypesResponse:
        """
        @summary Query the cluster types available to the user
        
        @return: ListUserClusterTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_user_cluster_types_with_options_async(runtime)

    def list_vscs_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.ListVscsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListVscsResponse:
        """
        @summary Queries a list of virtual storage channels (VSC).
        
        @param tmp_req: ListVscsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVscsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.ListVscsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_ids):
            request.node_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_ids, 'NodeIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_ids_shrink):
            body['NodeIds'] = request.node_ids_shrink
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vsc_name):
            body['VscName'] = request.vsc_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVscs',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListVscsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vscs_with_options_async(
        self,
        tmp_req: eflo_controller_20221215_models.ListVscsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListVscsResponse:
        """
        @summary Queries a list of virtual storage channels (VSC).
        
        @param tmp_req: ListVscsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListVscsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.ListVscsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_ids):
            request.node_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_ids, 'NodeIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not UtilClient.is_unset(request.max_results):
            body['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            body['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_ids_shrink):
            body['NodeIds'] = request.node_ids_shrink
        if not UtilClient.is_unset(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vsc_name):
            body['VscName'] = request.vsc_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListVscs',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ListVscsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vscs(
        self,
        request: eflo_controller_20221215_models.ListVscsRequest,
    ) -> eflo_controller_20221215_models.ListVscsResponse:
        """
        @summary Queries a list of virtual storage channels (VSC).
        
        @param request: ListVscsRequest
        @return: ListVscsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_vscs_with_options(request, runtime)

    async def list_vscs_async(
        self,
        request: eflo_controller_20221215_models.ListVscsRequest,
    ) -> eflo_controller_20221215_models.ListVscsResponse:
        """
        @summary Queries a list of virtual storage channels (VSC).
        
        @param request: ListVscsRequest
        @return: ListVscsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_vscs_with_options_async(request, runtime)

    def reboot_nodes_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.RebootNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.RebootNodesResponse:
        """
        @summary Restarts nodes.
        
        @param tmp_req: RebootNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebootNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.RebootNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.nodes):
            request.nodes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.nodes, 'Nodes', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not UtilClient.is_unset(request.nodes_shrink):
            body['Nodes'] = request.nodes_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RebootNodes',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.RebootNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_nodes_with_options_async(
        self,
        tmp_req: eflo_controller_20221215_models.RebootNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.RebootNodesResponse:
        """
        @summary Restarts nodes.
        
        @param tmp_req: RebootNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RebootNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.RebootNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.nodes):
            request.nodes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.nodes, 'Nodes', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not UtilClient.is_unset(request.nodes_shrink):
            body['Nodes'] = request.nodes_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RebootNodes',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.RebootNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_nodes(
        self,
        request: eflo_controller_20221215_models.RebootNodesRequest,
    ) -> eflo_controller_20221215_models.RebootNodesResponse:
        """
        @summary Restarts nodes.
        
        @param request: RebootNodesRequest
        @return: RebootNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reboot_nodes_with_options(request, runtime)

    async def reboot_nodes_async(
        self,
        request: eflo_controller_20221215_models.RebootNodesRequest,
    ) -> eflo_controller_20221215_models.RebootNodesResponse:
        """
        @summary Restarts nodes.
        
        @param request: RebootNodesRequest
        @return: RebootNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reboot_nodes_with_options_async(request, runtime)

    def reimage_nodes_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.ReimageNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ReimageNodesResponse:
        """
        @summary Reinstall a node.
        
        @param tmp_req: ReimageNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReimageNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.ReimageNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.nodes):
            request.nodes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.nodes, 'Nodes', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not UtilClient.is_unset(request.nodes_shrink):
            body['Nodes'] = request.nodes_shrink
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReimageNodes',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ReimageNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def reimage_nodes_with_options_async(
        self,
        tmp_req: eflo_controller_20221215_models.ReimageNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ReimageNodesResponse:
        """
        @summary Reinstall a node.
        
        @param tmp_req: ReimageNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReimageNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.ReimageNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.nodes):
            request.nodes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.nodes, 'Nodes', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not UtilClient.is_unset(request.nodes_shrink):
            body['Nodes'] = request.nodes_shrink
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReimageNodes',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ReimageNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reimage_nodes(
        self,
        request: eflo_controller_20221215_models.ReimageNodesRequest,
    ) -> eflo_controller_20221215_models.ReimageNodesResponse:
        """
        @summary Reinstall a node.
        
        @param request: ReimageNodesRequest
        @return: ReimageNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reimage_nodes_with_options(request, runtime)

    async def reimage_nodes_async(
        self,
        request: eflo_controller_20221215_models.ReimageNodesRequest,
    ) -> eflo_controller_20221215_models.ReimageNodesResponse:
        """
        @summary Reinstall a node.
        
        @param request: ReimageNodesRequest
        @return: ReimageNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reimage_nodes_with_options_async(request, runtime)

    def run_command_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.RunCommandResponse:
        """
        @summary Runs a Shell script on one or more Lingjun nodes.
        
        @param tmp_req: RunCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCommandResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.RunCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_id_list):
            request.node_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_id_list, 'NodeIdList', 'json')
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.command_content):
            body['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.command_id):
            body['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.content_encoding):
            body['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable_parameter):
            body['EnableParameter'] = request.enable_parameter
        if not UtilClient.is_unset(request.frequency):
            body['Frequency'] = request.frequency
        if not UtilClient.is_unset(request.launcher):
            body['Launcher'] = request.launcher
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.node_id_list_shrink):
            body['NodeIdList'] = request.node_id_list_shrink
        if not UtilClient.is_unset(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.repeat_mode):
            body['RepeatMode'] = request.repeat_mode
        if not UtilClient.is_unset(request.termination_mode):
            body['TerminationMode'] = request.termination_mode
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        if not UtilClient.is_unset(request.working_dir):
            body['WorkingDir'] = request.working_dir
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCommand',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.RunCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_command_with_options_async(
        self,
        tmp_req: eflo_controller_20221215_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.RunCommandResponse:
        """
        @summary Runs a Shell script on one or more Lingjun nodes.
        
        @param tmp_req: RunCommandRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunCommandResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.RunCommandShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_id_list):
            request.node_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_id_list, 'NodeIdList', 'json')
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.command_content):
            body['CommandContent'] = request.command_content
        if not UtilClient.is_unset(request.command_id):
            body['CommandId'] = request.command_id
        if not UtilClient.is_unset(request.content_encoding):
            body['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable_parameter):
            body['EnableParameter'] = request.enable_parameter
        if not UtilClient.is_unset(request.frequency):
            body['Frequency'] = request.frequency
        if not UtilClient.is_unset(request.launcher):
            body['Launcher'] = request.launcher
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.node_id_list_shrink):
            body['NodeIdList'] = request.node_id_list_shrink
        if not UtilClient.is_unset(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.repeat_mode):
            body['RepeatMode'] = request.repeat_mode
        if not UtilClient.is_unset(request.termination_mode):
            body['TerminationMode'] = request.termination_mode
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.username):
            body['Username'] = request.username
        if not UtilClient.is_unset(request.working_dir):
            body['WorkingDir'] = request.working_dir
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunCommand',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.RunCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_command(
        self,
        request: eflo_controller_20221215_models.RunCommandRequest,
    ) -> eflo_controller_20221215_models.RunCommandResponse:
        """
        @summary Runs a Shell script on one or more Lingjun nodes.
        
        @param request: RunCommandRequest
        @return: RunCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    async def run_command_async(
        self,
        request: eflo_controller_20221215_models.RunCommandRequest,
    ) -> eflo_controller_20221215_models.RunCommandResponse:
        """
        @summary Runs a Shell script on one or more Lingjun nodes.
        
        @param request: RunCommandRequest
        @return: RunCommandResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_command_with_options_async(request, runtime)

    def send_file_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.SendFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.SendFileResponse:
        """
        @summary Sends a file to one or more Lingjun nodes.
        
        @param tmp_req: SendFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendFileResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.SendFileShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_id_list):
            request.node_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_id_list, 'NodeIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_type):
            body['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.file_group):
            body['FileGroup'] = request.file_group
        if not UtilClient.is_unset(request.file_mode):
            body['FileMode'] = request.file_mode
        if not UtilClient.is_unset(request.file_owner):
            body['FileOwner'] = request.file_owner
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.node_id_list_shrink):
            body['NodeIdList'] = request.node_id_list_shrink
        if not UtilClient.is_unset(request.overwrite):
            body['Overwrite'] = request.overwrite
        if not UtilClient.is_unset(request.target_dir):
            body['TargetDir'] = request.target_dir
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendFile',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.SendFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_file_with_options_async(
        self,
        tmp_req: eflo_controller_20221215_models.SendFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.SendFileResponse:
        """
        @summary Sends a file to one or more Lingjun nodes.
        
        @param tmp_req: SendFileRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendFileResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.SendFileShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_id_list):
            request.node_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_id_list, 'NodeIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.content_type):
            body['ContentType'] = request.content_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.file_group):
            body['FileGroup'] = request.file_group
        if not UtilClient.is_unset(request.file_mode):
            body['FileMode'] = request.file_mode
        if not UtilClient.is_unset(request.file_owner):
            body['FileOwner'] = request.file_owner
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.node_id_list_shrink):
            body['NodeIdList'] = request.node_id_list_shrink
        if not UtilClient.is_unset(request.overwrite):
            body['Overwrite'] = request.overwrite
        if not UtilClient.is_unset(request.target_dir):
            body['TargetDir'] = request.target_dir
        if not UtilClient.is_unset(request.timeout):
            body['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendFile',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.SendFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_file(
        self,
        request: eflo_controller_20221215_models.SendFileRequest,
    ) -> eflo_controller_20221215_models.SendFileResponse:
        """
        @summary Sends a file to one or more Lingjun nodes.
        
        @param request: SendFileRequest
        @return: SendFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_file_with_options(request, runtime)

    async def send_file_async(
        self,
        request: eflo_controller_20221215_models.SendFileRequest,
    ) -> eflo_controller_20221215_models.SendFileResponse:
        """
        @summary Sends a file to one or more Lingjun nodes.
        
        @param request: SendFileRequest
        @return: SendFileResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_file_with_options_async(request, runtime)

    def shrink_cluster_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.ShrinkClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ShrinkClusterResponse:
        """
        @summary Scales in a cluster.
        
        @param tmp_req: ShrinkClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ShrinkClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.ShrinkClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_groups):
            request.node_groups_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_groups, 'NodeGroups', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not UtilClient.is_unset(request.node_groups_shrink):
            body['NodeGroups'] = request.node_groups_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ShrinkCluster',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ShrinkClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def shrink_cluster_with_options_async(
        self,
        tmp_req: eflo_controller_20221215_models.ShrinkClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ShrinkClusterResponse:
        """
        @summary Scales in a cluster.
        
        @param tmp_req: ShrinkClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ShrinkClusterResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.ShrinkClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_groups):
            request.node_groups_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_groups, 'NodeGroups', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not UtilClient.is_unset(request.node_groups_shrink):
            body['NodeGroups'] = request.node_groups_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ShrinkCluster',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.ShrinkClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def shrink_cluster(
        self,
        request: eflo_controller_20221215_models.ShrinkClusterRequest,
    ) -> eflo_controller_20221215_models.ShrinkClusterResponse:
        """
        @summary Scales in a cluster.
        
        @param request: ShrinkClusterRequest
        @return: ShrinkClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.shrink_cluster_with_options(request, runtime)

    async def shrink_cluster_async(
        self,
        request: eflo_controller_20221215_models.ShrinkClusterRequest,
    ) -> eflo_controller_20221215_models.ShrinkClusterResponse:
        """
        @summary Scales in a cluster.
        
        @param request: ShrinkClusterRequest
        @return: ShrinkClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.shrink_cluster_with_options_async(request, runtime)

    def stop_invocation_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.StopInvocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.StopInvocationResponse:
        """
        @summary Stops the O\\&M assistant command execution.
        
        @param tmp_req: StopInvocationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInvocationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.StopInvocationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_id_list):
            request.node_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_id_list, 'NodeIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.invoke_id):
            body['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.node_id_list_shrink):
            body['NodeIdList'] = request.node_id_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopInvocation',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.StopInvocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_invocation_with_options_async(
        self,
        tmp_req: eflo_controller_20221215_models.StopInvocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.StopInvocationResponse:
        """
        @summary Stops the O\\&M assistant command execution.
        
        @param tmp_req: StopInvocationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopInvocationResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.StopInvocationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.node_id_list):
            request.node_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.node_id_list, 'NodeIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.invoke_id):
            body['InvokeId'] = request.invoke_id
        if not UtilClient.is_unset(request.node_id_list_shrink):
            body['NodeIdList'] = request.node_id_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopInvocation',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.StopInvocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_invocation(
        self,
        request: eflo_controller_20221215_models.StopInvocationRequest,
    ) -> eflo_controller_20221215_models.StopInvocationResponse:
        """
        @summary Stops the O\\&M assistant command execution.
        
        @param request: StopInvocationRequest
        @return: StopInvocationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_invocation_with_options(request, runtime)

    async def stop_invocation_async(
        self,
        request: eflo_controller_20221215_models.StopInvocationRequest,
    ) -> eflo_controller_20221215_models.StopInvocationResponse:
        """
        @summary Stops the O\\&M assistant command execution.
        
        @param request: StopInvocationRequest
        @return: StopInvocationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_invocation_with_options_async(request, runtime)

    def stop_nodes_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.StopNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.StopNodesResponse:
        """
        @summary Stops nodes.
        
        @param tmp_req: StopNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.StopNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.nodes):
            request.nodes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.nodes, 'Nodes', 'json')
        body = {}
        if not UtilClient.is_unset(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not UtilClient.is_unset(request.nodes_shrink):
            body['Nodes'] = request.nodes_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopNodes',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.StopNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_nodes_with_options_async(
        self,
        tmp_req: eflo_controller_20221215_models.StopNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.StopNodesResponse:
        """
        @summary Stops nodes.
        
        @param tmp_req: StopNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopNodesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_controller_20221215_models.StopNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.nodes):
            request.nodes_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.nodes, 'Nodes', 'json')
        body = {}
        if not UtilClient.is_unset(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not UtilClient.is_unset(request.nodes_shrink):
            body['Nodes'] = request.nodes_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopNodes',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.StopNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_nodes(
        self,
        request: eflo_controller_20221215_models.StopNodesRequest,
    ) -> eflo_controller_20221215_models.StopNodesResponse:
        """
        @summary Stops nodes.
        
        @param request: StopNodesRequest
        @return: StopNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_nodes_with_options(request, runtime)

    async def stop_nodes_async(
        self,
        request: eflo_controller_20221215_models.StopNodesRequest,
    ) -> eflo_controller_20221215_models.StopNodesResponse:
        """
        @summary Stops nodes.
        
        @param request: StopNodesRequest
        @return: StopNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_nodes_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: eflo_controller_20221215_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.TagResourcesResponse:
        """
        @summary Tags resources.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: eflo_controller_20221215_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.TagResourcesResponse:
        """
        @summary Tags resources.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: eflo_controller_20221215_models.TagResourcesRequest,
    ) -> eflo_controller_20221215_models.TagResourcesResponse:
        """
        @summary Tags resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: eflo_controller_20221215_models.TagResourcesRequest,
    ) -> eflo_controller_20221215_models.TagResourcesResponse:
        """
        @summary Tags resources.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: eflo_controller_20221215_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.UntagResourcesResponse:
        """
        @summary Deletes a custom tag from a resource.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: eflo_controller_20221215_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.UntagResourcesResponse:
        """
        @summary Deletes a custom tag from a resource.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: eflo_controller_20221215_models.UntagResourcesRequest,
    ) -> eflo_controller_20221215_models.UntagResourcesResponse:
        """
        @summary Deletes a custom tag from a resource.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: eflo_controller_20221215_models.UntagResourcesRequest,
    ) -> eflo_controller_20221215_models.UntagResourcesResponse:
        """
        @summary Deletes a custom tag from a resource.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_node_group_with_options(
        self,
        request: eflo_controller_20221215_models.UpdateNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.UpdateNodeGroupResponse:
        """
        @summary Update Node Group
        
        @param request: UpdateNodeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNodeGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_system_mount_enabled):
            body['FileSystemMountEnabled'] = request.file_system_mount_enabled
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.key_pair_name):
            body['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.login_password):
            body['LoginPassword'] = request.login_password
        if not UtilClient.is_unset(request.new_node_group_name):
            body['NewNodeGroupName'] = request.new_node_group_name
        if not UtilClient.is_unset(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNodeGroup',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.UpdateNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_node_group_with_options_async(
        self,
        request: eflo_controller_20221215_models.UpdateNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.UpdateNodeGroupResponse:
        """
        @summary Update Node Group
        
        @param request: UpdateNodeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateNodeGroupResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_system_mount_enabled):
            body['FileSystemMountEnabled'] = request.file_system_mount_enabled
        if not UtilClient.is_unset(request.image_id):
            body['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.key_pair_name):
            body['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.login_password):
            body['LoginPassword'] = request.login_password
        if not UtilClient.is_unset(request.new_node_group_name):
            body['NewNodeGroupName'] = request.new_node_group_name
        if not UtilClient.is_unset(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateNodeGroup',
            version='2022-12-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_controller_20221215_models.UpdateNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_node_group(
        self,
        request: eflo_controller_20221215_models.UpdateNodeGroupRequest,
    ) -> eflo_controller_20221215_models.UpdateNodeGroupResponse:
        """
        @summary Update Node Group
        
        @param request: UpdateNodeGroupRequest
        @return: UpdateNodeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_node_group_with_options(request, runtime)

    async def update_node_group_async(
        self,
        request: eflo_controller_20221215_models.UpdateNodeGroupRequest,
    ) -> eflo_controller_20221215_models.UpdateNodeGroupResponse:
        """
        @summary Update Node Group
        
        @param request: UpdateNodeGroupRequest
        @return: UpdateNodeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_node_group_with_options_async(request, runtime)
