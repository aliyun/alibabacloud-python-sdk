# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_eflo_controller20221215 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def approve_operation_with_options(
        self,
        request: main_models.ApproveOperationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApproveOperationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.operation_type):
            body['OperationType'] = request.operation_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ApproveOperation',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApproveOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def approve_operation_with_options_async(
        self,
        request: main_models.ApproveOperationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApproveOperationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.operation_type):
            body['OperationType'] = request.operation_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ApproveOperation',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApproveOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def approve_operation(
        self,
        request: main_models.ApproveOperationRequest,
    ) -> main_models.ApproveOperationResponse:
        runtime = RuntimeOptions()
        return self.approve_operation_with_options(request, runtime)

    async def approve_operation_async(
        self,
        request: main_models.ApproveOperationRequest,
    ) -> main_models.ApproveOperationResponse:
        runtime = RuntimeOptions()
        return await self.approve_operation_with_options_async(request, runtime)

    def change_node_group_with_options(
        self,
        tmp_req: main_models.ChangeNodeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeNodeGroupResponse:
        tmp_req.validate()
        request = main_models.ChangeNodeGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.nodes):
            request.nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.nodes, 'Nodes', 'json')
        query = {}
        if not DaraCore.is_null(request.ignore_failed_node_tasks):
            query['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not DaraCore.is_null(request.target_node_group_id):
            query['TargetNodeGroupId'] = request.target_node_group_id
        body = {}
        if not DaraCore.is_null(request.nodes_shrink):
            body['Nodes'] = request.nodes_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeNodeGroup',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_node_group_with_options_async(
        self,
        tmp_req: main_models.ChangeNodeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeNodeGroupResponse:
        tmp_req.validate()
        request = main_models.ChangeNodeGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.nodes):
            request.nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.nodes, 'Nodes', 'json')
        query = {}
        if not DaraCore.is_null(request.ignore_failed_node_tasks):
            query['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not DaraCore.is_null(request.target_node_group_id):
            query['TargetNodeGroupId'] = request.target_node_group_id
        body = {}
        if not DaraCore.is_null(request.nodes_shrink):
            body['Nodes'] = request.nodes_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeNodeGroup',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_node_group(
        self,
        request: main_models.ChangeNodeGroupRequest,
    ) -> main_models.ChangeNodeGroupResponse:
        runtime = RuntimeOptions()
        return self.change_node_group_with_options(request, runtime)

    async def change_node_group_async(
        self,
        request: main_models.ChangeNodeGroupRequest,
    ) -> main_models.ChangeNodeGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_node_group_with_options_async(request, runtime)

    def change_node_types_with_options(
        self,
        tmp_req: main_models.ChangeNodeTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeNodeTypesResponse:
        tmp_req.validate()
        request = main_models.ChangeNodeTypesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_ids):
            request.node_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_ids, 'NodeIds', 'json')
        body = {}
        if not DaraCore.is_null(request.node_ids_shrink):
            body['NodeIds'] = request.node_ids_shrink
        if not DaraCore.is_null(request.node_type):
            body['NodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeNodeTypes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeNodeTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_node_types_with_options_async(
        self,
        tmp_req: main_models.ChangeNodeTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeNodeTypesResponse:
        tmp_req.validate()
        request = main_models.ChangeNodeTypesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_ids):
            request.node_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_ids, 'NodeIds', 'json')
        body = {}
        if not DaraCore.is_null(request.node_ids_shrink):
            body['NodeIds'] = request.node_ids_shrink
        if not DaraCore.is_null(request.node_type):
            body['NodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ChangeNodeTypes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeNodeTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_node_types(
        self,
        request: main_models.ChangeNodeTypesRequest,
    ) -> main_models.ChangeNodeTypesResponse:
        runtime = RuntimeOptions()
        return self.change_node_types_with_options(request, runtime)

    async def change_node_types_async(
        self,
        request: main_models.ChangeNodeTypesRequest,
    ) -> main_models.ChangeNodeTypesResponse:
        runtime = RuntimeOptions()
        return await self.change_node_types_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2022-12-15',
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
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2022-12-15',
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

    def close_session_with_options(
        self,
        request: main_models.CloseSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.session_token):
            body['SessionToken'] = request.session_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloseSession',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_session_with_options_async(
        self,
        request: main_models.CloseSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.session_id):
            body['SessionId'] = request.session_id
        if not DaraCore.is_null(request.session_token):
            body['SessionToken'] = request.session_token
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CloseSession',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_session(
        self,
        request: main_models.CloseSessionRequest,
    ) -> main_models.CloseSessionResponse:
        runtime = RuntimeOptions()
        return self.close_session_with_options(request, runtime)

    async def close_session_async(
        self,
        request: main_models.CloseSessionRequest,
    ) -> main_models.CloseSessionResponse:
        runtime = RuntimeOptions()
        return await self.close_session_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        tmp_req: main_models.CreateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterResponse:
        tmp_req.validate()
        request = main_models.CreateClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.components):
            request.components_shrink = Utils.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not DaraCore.is_null(tmp_req.networks):
            request.networks_shrink = Utils.array_to_string_with_specified_style(tmp_req.networks, 'Networks', 'json')
        if not DaraCore.is_null(tmp_req.nimiz_vswitches):
            request.nimiz_vswitches_shrink = Utils.array_to_string_with_specified_style(tmp_req.nimiz_vswitches, 'NimizVSwitches', 'json')
        if not DaraCore.is_null(tmp_req.node_groups):
            request.node_groups_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_groups, 'NodeGroups', 'json')
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.cluster_description):
            body['ClusterDescription'] = request.cluster_description
        if not DaraCore.is_null(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_type):
            body['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.components_shrink):
            body['Components'] = request.components_shrink
        if not DaraCore.is_null(request.hpn_zone):
            body['HpnZone'] = request.hpn_zone
        if not DaraCore.is_null(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not DaraCore.is_null(request.networks_shrink):
            body['Networks'] = request.networks_shrink
        if not DaraCore.is_null(request.nimiz_vswitches_shrink):
            body['NimizVSwitches'] = request.nimiz_vswitches_shrink
        if not DaraCore.is_null(request.node_groups_shrink):
            body['NodeGroups'] = request.node_groups_shrink
        if not DaraCore.is_null(request.open_eni_jumbo_frame):
            body['OpenEniJumboFrame'] = request.open_eni_jumbo_frame
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCluster',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        tmp_req: main_models.CreateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterResponse:
        tmp_req.validate()
        request = main_models.CreateClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.components):
            request.components_shrink = Utils.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not DaraCore.is_null(tmp_req.networks):
            request.networks_shrink = Utils.array_to_string_with_specified_style(tmp_req.networks, 'Networks', 'json')
        if not DaraCore.is_null(tmp_req.nimiz_vswitches):
            request.nimiz_vswitches_shrink = Utils.array_to_string_with_specified_style(tmp_req.nimiz_vswitches, 'NimizVSwitches', 'json')
        if not DaraCore.is_null(tmp_req.node_groups):
            request.node_groups_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_groups, 'NodeGroups', 'json')
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.cluster_description):
            body['ClusterDescription'] = request.cluster_description
        if not DaraCore.is_null(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_type):
            body['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.components_shrink):
            body['Components'] = request.components_shrink
        if not DaraCore.is_null(request.hpn_zone):
            body['HpnZone'] = request.hpn_zone
        if not DaraCore.is_null(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not DaraCore.is_null(request.networks_shrink):
            body['Networks'] = request.networks_shrink
        if not DaraCore.is_null(request.nimiz_vswitches_shrink):
            body['NimizVSwitches'] = request.nimiz_vswitches_shrink
        if not DaraCore.is_null(request.node_groups_shrink):
            body['NodeGroups'] = request.node_groups_shrink
        if not DaraCore.is_null(request.open_eni_jumbo_frame):
            body['OpenEniJumboFrame'] = request.open_eni_jumbo_frame
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCluster',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: main_models.CreateClusterRequest,
    ) -> main_models.CreateClusterResponse:
        runtime = RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: main_models.CreateClusterRequest,
    ) -> main_models.CreateClusterResponse:
        runtime = RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_diagnostic_task_with_options(
        self,
        tmp_req: main_models.CreateDiagnosticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDiagnosticTaskResponse:
        tmp_req.validate()
        request = main_models.CreateDiagnosticTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ai_job_log_info):
            request.ai_job_log_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.ai_job_log_info, 'AiJobLogInfo', 'json')
        if not DaraCore.is_null(tmp_req.node_ids):
            request.node_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_ids, 'NodeIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.ai_job_log_info_shrink):
            body['AiJobLogInfo'] = request.ai_job_log_info_shrink
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.diagnostic_type):
            body['DiagnosticType'] = request.diagnostic_type
        if not DaraCore.is_null(request.node_ids_shrink):
            body['NodeIds'] = request.node_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDiagnosticTask',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDiagnosticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_diagnostic_task_with_options_async(
        self,
        tmp_req: main_models.CreateDiagnosticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDiagnosticTaskResponse:
        tmp_req.validate()
        request = main_models.CreateDiagnosticTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ai_job_log_info):
            request.ai_job_log_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.ai_job_log_info, 'AiJobLogInfo', 'json')
        if not DaraCore.is_null(tmp_req.node_ids):
            request.node_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_ids, 'NodeIds', 'simple')
        body = {}
        if not DaraCore.is_null(request.ai_job_log_info_shrink):
            body['AiJobLogInfo'] = request.ai_job_log_info_shrink
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.diagnostic_type):
            body['DiagnosticType'] = request.diagnostic_type
        if not DaraCore.is_null(request.node_ids_shrink):
            body['NodeIds'] = request.node_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDiagnosticTask',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDiagnosticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_diagnostic_task(
        self,
        request: main_models.CreateDiagnosticTaskRequest,
    ) -> main_models.CreateDiagnosticTaskResponse:
        runtime = RuntimeOptions()
        return self.create_diagnostic_task_with_options(request, runtime)

    async def create_diagnostic_task_async(
        self,
        request: main_models.CreateDiagnosticTaskRequest,
    ) -> main_models.CreateDiagnosticTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_diagnostic_task_with_options_async(request, runtime)

    def create_net_test_task_with_options(
        self,
        tmp_req: main_models.CreateNetTestTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetTestTaskResponse:
        tmp_req.validate()
        request = main_models.CreateNetTestTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.comm_test):
            request.comm_test_shrink = Utils.array_to_string_with_specified_style(tmp_req.comm_test, 'CommTest', 'json')
        if not DaraCore.is_null(tmp_req.delay_test):
            request.delay_test_shrink = Utils.array_to_string_with_specified_style(tmp_req.delay_test, 'DelayTest', 'json')
        if not DaraCore.is_null(tmp_req.traffic_test):
            request.traffic_test_shrink = Utils.array_to_string_with_specified_style(tmp_req.traffic_test, 'TrafficTest', 'json')
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.comm_test_shrink):
            body['CommTest'] = request.comm_test_shrink
        if not DaraCore.is_null(request.delay_test_shrink):
            body['DelayTest'] = request.delay_test_shrink
        if not DaraCore.is_null(request.net_test_type):
            body['NetTestType'] = request.net_test_type
        if not DaraCore.is_null(request.network_mode):
            body['NetworkMode'] = request.network_mode
        if not DaraCore.is_null(request.port):
            body['Port'] = request.port
        if not DaraCore.is_null(request.traffic_test_shrink):
            body['TrafficTest'] = request.traffic_test_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetTestTask',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetTestTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_net_test_task_with_options_async(
        self,
        tmp_req: main_models.CreateNetTestTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNetTestTaskResponse:
        tmp_req.validate()
        request = main_models.CreateNetTestTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.comm_test):
            request.comm_test_shrink = Utils.array_to_string_with_specified_style(tmp_req.comm_test, 'CommTest', 'json')
        if not DaraCore.is_null(tmp_req.delay_test):
            request.delay_test_shrink = Utils.array_to_string_with_specified_style(tmp_req.delay_test, 'DelayTest', 'json')
        if not DaraCore.is_null(tmp_req.traffic_test):
            request.traffic_test_shrink = Utils.array_to_string_with_specified_style(tmp_req.traffic_test, 'TrafficTest', 'json')
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.comm_test_shrink):
            body['CommTest'] = request.comm_test_shrink
        if not DaraCore.is_null(request.delay_test_shrink):
            body['DelayTest'] = request.delay_test_shrink
        if not DaraCore.is_null(request.net_test_type):
            body['NetTestType'] = request.net_test_type
        if not DaraCore.is_null(request.network_mode):
            body['NetworkMode'] = request.network_mode
        if not DaraCore.is_null(request.port):
            body['Port'] = request.port
        if not DaraCore.is_null(request.traffic_test_shrink):
            body['TrafficTest'] = request.traffic_test_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNetTestTask',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNetTestTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_net_test_task(
        self,
        request: main_models.CreateNetTestTaskRequest,
    ) -> main_models.CreateNetTestTaskResponse:
        runtime = RuntimeOptions()
        return self.create_net_test_task_with_options(request, runtime)

    async def create_net_test_task_async(
        self,
        request: main_models.CreateNetTestTaskRequest,
    ) -> main_models.CreateNetTestTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_net_test_task_with_options_async(request, runtime)

    def create_node_group_with_options(
        self,
        tmp_req: main_models.CreateNodeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNodeGroupResponse:
        tmp_req.validate()
        request = main_models.CreateNodeGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_group):
            request.node_group_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_group, 'NodeGroup', 'json')
        if not DaraCore.is_null(tmp_req.node_unit):
            request.node_unit_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_unit, 'NodeUnit', 'json')
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_group_shrink):
            body['NodeGroup'] = request.node_group_shrink
        if not DaraCore.is_null(request.node_unit_shrink):
            body['NodeUnit'] = request.node_unit_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNodeGroup',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_node_group_with_options_async(
        self,
        tmp_req: main_models.CreateNodeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNodeGroupResponse:
        tmp_req.validate()
        request = main_models.CreateNodeGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_group):
            request.node_group_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_group, 'NodeGroup', 'json')
        if not DaraCore.is_null(tmp_req.node_unit):
            request.node_unit_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_unit, 'NodeUnit', 'json')
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_group_shrink):
            body['NodeGroup'] = request.node_group_shrink
        if not DaraCore.is_null(request.node_unit_shrink):
            body['NodeUnit'] = request.node_unit_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateNodeGroup',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_node_group(
        self,
        request: main_models.CreateNodeGroupRequest,
    ) -> main_models.CreateNodeGroupResponse:
        runtime = RuntimeOptions()
        return self.create_node_group_with_options(request, runtime)

    async def create_node_group_async(
        self,
        request: main_models.CreateNodeGroupRequest,
    ) -> main_models.CreateNodeGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_node_group_with_options_async(request, runtime)

    def create_session_with_options(
        self,
        request: main_models.CreateSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.session_type):
            body['SessionType'] = request.session_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSession',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSessionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_session_with_options_async(
        self,
        request: main_models.CreateSessionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSessionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.session_type):
            body['SessionType'] = request.session_type
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSession',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSessionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_session(
        self,
        request: main_models.CreateSessionRequest,
    ) -> main_models.CreateSessionResponse:
        runtime = RuntimeOptions()
        return self.create_session_with_options(request, runtime)

    async def create_session_async(
        self,
        request: main_models.CreateSessionRequest,
    ) -> main_models.CreateSessionResponse:
        runtime = RuntimeOptions()
        return await self.create_session_with_options_async(request, runtime)

    def create_vsc_with_options(
        self,
        request: main_models.CreateVscRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVscResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.vsc_name):
            body['VscName'] = request.vsc_name
        if not DaraCore.is_null(request.vsc_type):
            body['VscType'] = request.vsc_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVsc',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVscResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_vsc_with_options_async(
        self,
        request: main_models.CreateVscRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateVscResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.vsc_name):
            body['VscName'] = request.vsc_name
        if not DaraCore.is_null(request.vsc_type):
            body['VscType'] = request.vsc_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateVsc',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateVscResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_vsc(
        self,
        request: main_models.CreateVscRequest,
    ) -> main_models.CreateVscResponse:
        runtime = RuntimeOptions()
        return self.create_vsc_with_options(request, runtime)

    async def create_vsc_async(
        self,
        request: main_models.CreateVscRequest,
    ) -> main_models.CreateVscResponse:
        runtime = RuntimeOptions()
        return await self.create_vsc_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: main_models.DeleteClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCluster',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: main_models.DeleteClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCluster',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        request: main_models.DeleteClusterRequest,
    ) -> main_models.DeleteClusterResponse:
        runtime = RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: main_models.DeleteClusterRequest,
    ) -> main_models.DeleteClusterResponse:
        runtime = RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def delete_hyper_node_with_options(
        self,
        request: main_models.DeleteHyperNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHyperNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hyper_node_id):
            body['HyperNodeId'] = request.hyper_node_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHyperNode',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHyperNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hyper_node_with_options_async(
        self,
        request: main_models.DeleteHyperNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHyperNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hyper_node_id):
            body['HyperNodeId'] = request.hyper_node_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHyperNode',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHyperNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hyper_node(
        self,
        request: main_models.DeleteHyperNodeRequest,
    ) -> main_models.DeleteHyperNodeResponse:
        runtime = RuntimeOptions()
        return self.delete_hyper_node_with_options(request, runtime)

    async def delete_hyper_node_async(
        self,
        request: main_models.DeleteHyperNodeRequest,
    ) -> main_models.DeleteHyperNodeResponse:
        runtime = RuntimeOptions()
        return await self.delete_hyper_node_with_options_async(request, runtime)

    def delete_node_with_options(
        self,
        request: main_models.DeleteNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNode',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_node_with_options_async(
        self,
        request: main_models.DeleteNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNode',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_node(
        self,
        request: main_models.DeleteNodeRequest,
    ) -> main_models.DeleteNodeResponse:
        runtime = RuntimeOptions()
        return self.delete_node_with_options(request, runtime)

    async def delete_node_async(
        self,
        request: main_models.DeleteNodeRequest,
    ) -> main_models.DeleteNodeResponse:
        runtime = RuntimeOptions()
        return await self.delete_node_with_options_async(request, runtime)

    def delete_node_group_with_options(
        self,
        request: main_models.DeleteNodeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNodeGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNodeGroup',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_node_group_with_options_async(
        self,
        request: main_models.DeleteNodeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNodeGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNodeGroup',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_node_group(
        self,
        request: main_models.DeleteNodeGroupRequest,
    ) -> main_models.DeleteNodeGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_node_group_with_options(request, runtime)

    async def delete_node_group_async(
        self,
        request: main_models.DeleteNodeGroupRequest,
    ) -> main_models.DeleteNodeGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_node_group_with_options_async(request, runtime)

    def delete_vsc_with_options(
        self,
        request: main_models.DeleteVscRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVscResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.vsc_id):
            body['VscId'] = request.vsc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVsc',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVscResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_vsc_with_options_async(
        self,
        request: main_models.DeleteVscRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteVscResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        body = {}
        if not DaraCore.is_null(request.vsc_id):
            body['VscId'] = request.vsc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteVsc',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteVscResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_vsc(
        self,
        request: main_models.DeleteVscRequest,
    ) -> main_models.DeleteVscResponse:
        runtime = RuntimeOptions()
        return self.delete_vsc_with_options(request, runtime)

    async def delete_vsc_async(
        self,
        request: main_models.DeleteVscRequest,
    ) -> main_models.DeleteVscResponse:
        runtime = RuntimeOptions()
        return await self.delete_vsc_with_options_async(request, runtime)

    def describe_cluster_with_options(
        self,
        request: main_models.DescribeClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCluster',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_with_options_async(
        self,
        request: main_models.DescribeClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeClusterResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCluster',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster(
        self,
        request: main_models.DescribeClusterRequest,
    ) -> main_models.DescribeClusterResponse:
        runtime = RuntimeOptions()
        return self.describe_cluster_with_options(request, runtime)

    async def describe_cluster_async(
        self,
        request: main_models.DescribeClusterRequest,
    ) -> main_models.DescribeClusterResponse:
        runtime = RuntimeOptions()
        return await self.describe_cluster_with_options_async(request, runtime)

    def describe_diagnostic_result_with_options(
        self,
        request: main_models.DescribeDiagnosticResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosticResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.diagnostic_id):
            body['DiagnosticId'] = request.diagnostic_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosticResult',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosticResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_diagnostic_result_with_options_async(
        self,
        request: main_models.DescribeDiagnosticResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDiagnosticResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.diagnostic_id):
            body['DiagnosticId'] = request.diagnostic_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDiagnosticResult',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDiagnosticResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_diagnostic_result(
        self,
        request: main_models.DescribeDiagnosticResultRequest,
    ) -> main_models.DescribeDiagnosticResultResponse:
        runtime = RuntimeOptions()
        return self.describe_diagnostic_result_with_options(request, runtime)

    async def describe_diagnostic_result_async(
        self,
        request: main_models.DescribeDiagnosticResultRequest,
    ) -> main_models.DescribeDiagnosticResultResponse:
        runtime = RuntimeOptions()
        return await self.describe_diagnostic_result_with_options_async(request, runtime)

    def describe_hyper_node_with_options(
        self,
        request: main_models.DescribeHyperNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHyperNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hyper_node_id):
            body['HyperNodeId'] = request.hyper_node_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHyperNode',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHyperNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hyper_node_with_options_async(
        self,
        request: main_models.DescribeHyperNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHyperNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hyper_node_id):
            body['HyperNodeId'] = request.hyper_node_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHyperNode',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHyperNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hyper_node(
        self,
        request: main_models.DescribeHyperNodeRequest,
    ) -> main_models.DescribeHyperNodeResponse:
        runtime = RuntimeOptions()
        return self.describe_hyper_node_with_options(request, runtime)

    async def describe_hyper_node_async(
        self,
        request: main_models.DescribeHyperNodeRequest,
    ) -> main_models.DescribeHyperNodeResponse:
        runtime = RuntimeOptions()
        return await self.describe_hyper_node_with_options_async(request, runtime)

    def describe_invocations_with_options(
        self,
        request: main_models.DescribeInvocationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvocationsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content_encoding):
            body['ContentEncoding'] = request.content_encoding
        if not DaraCore.is_null(request.include_output):
            body['IncludeOutput'] = request.include_output
        if not DaraCore.is_null(request.invoke_id):
            body['InvokeId'] = request.invoke_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvocations',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_invocations_with_options_async(
        self,
        request: main_models.DescribeInvocationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeInvocationsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.content_encoding):
            body['ContentEncoding'] = request.content_encoding
        if not DaraCore.is_null(request.include_output):
            body['IncludeOutput'] = request.include_output
        if not DaraCore.is_null(request.invoke_id):
            body['InvokeId'] = request.invoke_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeInvocations',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeInvocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_invocations(
        self,
        request: main_models.DescribeInvocationsRequest,
    ) -> main_models.DescribeInvocationsResponse:
        runtime = RuntimeOptions()
        return self.describe_invocations_with_options(request, runtime)

    async def describe_invocations_async(
        self,
        request: main_models.DescribeInvocationsRequest,
    ) -> main_models.DescribeInvocationsResponse:
        runtime = RuntimeOptions()
        return await self.describe_invocations_with_options_async(request, runtime)

    def describe_net_test_result_with_options(
        self,
        request: main_models.DescribeNetTestResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetTestResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.test_id):
            body['TestId'] = request.test_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetTestResult',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetTestResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_net_test_result_with_options_async(
        self,
        request: main_models.DescribeNetTestResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNetTestResultResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.test_id):
            body['TestId'] = request.test_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNetTestResult',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNetTestResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_net_test_result(
        self,
        request: main_models.DescribeNetTestResultRequest,
    ) -> main_models.DescribeNetTestResultResponse:
        runtime = RuntimeOptions()
        return self.describe_net_test_result_with_options(request, runtime)

    async def describe_net_test_result_async(
        self,
        request: main_models.DescribeNetTestResultRequest,
    ) -> main_models.DescribeNetTestResultResponse:
        runtime = RuntimeOptions()
        return await self.describe_net_test_result_with_options_async(request, runtime)

    def describe_node_with_options(
        self,
        request: main_models.DescribeNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNode',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_node_with_options_async(
        self,
        request: main_models.DescribeNodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNodeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNode',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_node(
        self,
        request: main_models.DescribeNodeRequest,
    ) -> main_models.DescribeNodeResponse:
        runtime = RuntimeOptions()
        return self.describe_node_with_options(request, runtime)

    async def describe_node_async(
        self,
        request: main_models.DescribeNodeRequest,
    ) -> main_models.DescribeNodeResponse:
        runtime = RuntimeOptions()
        return await self.describe_node_with_options_async(request, runtime)

    def describe_node_group_with_options(
        self,
        request: main_models.DescribeNodeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNodeGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNodeGroup',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_node_group_with_options_async(
        self,
        request: main_models.DescribeNodeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNodeGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNodeGroup',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_node_group(
        self,
        request: main_models.DescribeNodeGroupRequest,
    ) -> main_models.DescribeNodeGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_node_group_with_options(request, runtime)

    async def describe_node_group_async(
        self,
        request: main_models.DescribeNodeGroupRequest,
    ) -> main_models.DescribeNodeGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_node_group_with_options_async(request, runtime)

    def describe_node_type_with_options(
        self,
        request: main_models.DescribeNodeTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNodeTypeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.node_type):
            body['NodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNodeType',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNodeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_node_type_with_options_async(
        self,
        request: main_models.DescribeNodeTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNodeTypeResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.node_type):
            body['NodeType'] = request.node_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNodeType',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNodeTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_node_type(
        self,
        request: main_models.DescribeNodeTypeRequest,
    ) -> main_models.DescribeNodeTypeResponse:
        runtime = RuntimeOptions()
        return self.describe_node_type_with_options(request, runtime)

    async def describe_node_type_async(
        self,
        request: main_models.DescribeNodeTypeRequest,
    ) -> main_models.DescribeNodeTypeResponse:
        runtime = RuntimeOptions()
        return await self.describe_node_type_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2022-12-15',
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
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2022-12-15',
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

    def describe_send_file_results_with_options(
        self,
        request: main_models.DescribeSendFileResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSendFileResultsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.invoke_id):
            body['InvokeId'] = request.invoke_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSendFileResults',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSendFileResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_send_file_results_with_options_async(
        self,
        request: main_models.DescribeSendFileResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSendFileResultsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.invoke_id):
            body['InvokeId'] = request.invoke_id
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSendFileResults',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSendFileResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_send_file_results(
        self,
        request: main_models.DescribeSendFileResultsRequest,
    ) -> main_models.DescribeSendFileResultsResponse:
        runtime = RuntimeOptions()
        return self.describe_send_file_results_with_options(request, runtime)

    async def describe_send_file_results_async(
        self,
        request: main_models.DescribeSendFileResultsRequest,
    ) -> main_models.DescribeSendFileResultsResponse:
        runtime = RuntimeOptions()
        return await self.describe_send_file_results_with_options_async(request, runtime)

    def describe_task_with_options(
        self,
        request: main_models.DescribeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTask',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_task_with_options_async(
        self,
        request: main_models.DescribeTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTask',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_task(
        self,
        request: main_models.DescribeTaskRequest,
    ) -> main_models.DescribeTaskResponse:
        runtime = RuntimeOptions()
        return self.describe_task_with_options(request, runtime)

    async def describe_task_async(
        self,
        request: main_models.DescribeTaskRequest,
    ) -> main_models.DescribeTaskResponse:
        runtime = RuntimeOptions()
        return await self.describe_task_with_options_async(request, runtime)

    def describe_vsc_with_options(
        self,
        request: main_models.DescribeVscRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVscResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.vsc_id):
            body['VscId'] = request.vsc_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsc',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVscResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_vsc_with_options_async(
        self,
        request: main_models.DescribeVscRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeVscResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.vsc_id):
            body['VscId'] = request.vsc_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeVsc',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeVscResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_vsc(
        self,
        request: main_models.DescribeVscRequest,
    ) -> main_models.DescribeVscResponse:
        runtime = RuntimeOptions()
        return self.describe_vsc_with_options(request, runtime)

    async def describe_vsc_async(
        self,
        request: main_models.DescribeVscRequest,
    ) -> main_models.DescribeVscResponse:
        runtime = RuntimeOptions()
        return await self.describe_vsc_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: main_models.DescribeZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: main_models.DescribeZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.accept_language):
            body['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: main_models.DescribeZonesRequest,
    ) -> main_models.DescribeZonesResponse:
        runtime = RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: main_models.DescribeZonesRequest,
    ) -> main_models.DescribeZonesResponse:
        runtime = RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def extend_cluster_with_options(
        self,
        tmp_req: main_models.ExtendClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExtendClusterResponse:
        tmp_req.validate()
        request = main_models.ExtendClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ip_allocation_policy):
            request.ip_allocation_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.ip_allocation_policy, 'IpAllocationPolicy', 'json')
        if not DaraCore.is_null(tmp_req.node_groups):
            request.node_groups_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_groups, 'NodeGroups', 'json')
        if not DaraCore.is_null(tmp_req.vpd_subnets):
            request.vpd_subnets_shrink = Utils.array_to_string_with_specified_style(tmp_req.vpd_subnets, 'VpdSubnets', 'json')
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not DaraCore.is_null(request.ip_allocation_policy_shrink):
            body['IpAllocationPolicy'] = request.ip_allocation_policy_shrink
        if not DaraCore.is_null(request.node_groups_shrink):
            body['NodeGroups'] = request.node_groups_shrink
        if not DaraCore.is_null(request.v_switch_zone_id):
            body['VSwitchZoneId'] = request.v_switch_zone_id
        if not DaraCore.is_null(request.vpd_subnets_shrink):
            body['VpdSubnets'] = request.vpd_subnets_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExtendCluster',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExtendClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def extend_cluster_with_options_async(
        self,
        tmp_req: main_models.ExtendClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExtendClusterResponse:
        tmp_req.validate()
        request = main_models.ExtendClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ip_allocation_policy):
            request.ip_allocation_policy_shrink = Utils.array_to_string_with_specified_style(tmp_req.ip_allocation_policy, 'IpAllocationPolicy', 'json')
        if not DaraCore.is_null(tmp_req.node_groups):
            request.node_groups_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_groups, 'NodeGroups', 'json')
        if not DaraCore.is_null(tmp_req.vpd_subnets):
            request.vpd_subnets_shrink = Utils.array_to_string_with_specified_style(tmp_req.vpd_subnets, 'VpdSubnets', 'json')
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not DaraCore.is_null(request.ip_allocation_policy_shrink):
            body['IpAllocationPolicy'] = request.ip_allocation_policy_shrink
        if not DaraCore.is_null(request.node_groups_shrink):
            body['NodeGroups'] = request.node_groups_shrink
        if not DaraCore.is_null(request.v_switch_zone_id):
            body['VSwitchZoneId'] = request.v_switch_zone_id
        if not DaraCore.is_null(request.vpd_subnets_shrink):
            body['VpdSubnets'] = request.vpd_subnets_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExtendCluster',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExtendClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def extend_cluster(
        self,
        request: main_models.ExtendClusterRequest,
    ) -> main_models.ExtendClusterResponse:
        runtime = RuntimeOptions()
        return self.extend_cluster_with_options(request, runtime)

    async def extend_cluster_async(
        self,
        request: main_models.ExtendClusterRequest,
    ) -> main_models.ExtendClusterResponse:
        runtime = RuntimeOptions()
        return await self.extend_cluster_with_options_async(request, runtime)

    def list_cluster_hyper_nodes_with_options(
        self,
        request: main_models.ListClusterHyperNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterHyperNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterHyperNodes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterHyperNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_hyper_nodes_with_options_async(
        self,
        request: main_models.ListClusterHyperNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterHyperNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterHyperNodes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterHyperNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_hyper_nodes(
        self,
        request: main_models.ListClusterHyperNodesRequest,
    ) -> main_models.ListClusterHyperNodesResponse:
        runtime = RuntimeOptions()
        return self.list_cluster_hyper_nodes_with_options(request, runtime)

    async def list_cluster_hyper_nodes_async(
        self,
        request: main_models.ListClusterHyperNodesRequest,
    ) -> main_models.ListClusterHyperNodesResponse:
        runtime = RuntimeOptions()
        return await self.list_cluster_hyper_nodes_with_options_async(request, runtime)

    def list_cluster_nodes_with_options(
        self,
        request: main_models.ListClusterNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.operating_states):
            body['OperatingStates'] = request.operating_states
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterNodes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_nodes_with_options_async(
        self,
        request: main_models.ListClusterNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.operating_states):
            body['OperatingStates'] = request.operating_states
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterNodes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_nodes(
        self,
        request: main_models.ListClusterNodesRequest,
    ) -> main_models.ListClusterNodesResponse:
        runtime = RuntimeOptions()
        return self.list_cluster_nodes_with_options(request, runtime)

    async def list_cluster_nodes_async(
        self,
        request: main_models.ListClusterNodesRequest,
    ) -> main_models.ListClusterNodesResponse:
        runtime = RuntimeOptions()
        return await self.list_cluster_nodes_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: main_models.ListClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListClusters',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: main_models.ListClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListClusters',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        request: main_models.ListClustersRequest,
    ) -> main_models.ListClustersResponse:
        runtime = RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: main_models.ListClustersRequest,
    ) -> main_models.ListClustersResponse:
        runtime = RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_diagnostic_results_with_options(
        self,
        request: main_models.ListDiagnosticResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDiagnosticResultsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.diag_type):
            body['DiagType'] = request.diag_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDiagnosticResults',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDiagnosticResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_diagnostic_results_with_options_async(
        self,
        request: main_models.ListDiagnosticResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDiagnosticResultsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.diag_type):
            body['DiagType'] = request.diag_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListDiagnosticResults',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDiagnosticResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_diagnostic_results(
        self,
        request: main_models.ListDiagnosticResultsRequest,
    ) -> main_models.ListDiagnosticResultsResponse:
        runtime = RuntimeOptions()
        return self.list_diagnostic_results_with_options(request, runtime)

    async def list_diagnostic_results_async(
        self,
        request: main_models.ListDiagnosticResultsRequest,
    ) -> main_models.ListDiagnosticResultsResponse:
        runtime = RuntimeOptions()
        return await self.list_diagnostic_results_with_options_async(request, runtime)

    def list_free_hyper_nodes_with_options(
        self,
        request: main_models.ListFreeHyperNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFreeHyperNodesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hpn_zone):
            body['HpnZone'] = request.hpn_zone
        if not DaraCore.is_null(request.machine_type):
            body['MachineType'] = request.machine_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFreeHyperNodes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFreeHyperNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_free_hyper_nodes_with_options_async(
        self,
        request: main_models.ListFreeHyperNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFreeHyperNodesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.hpn_zone):
            body['HpnZone'] = request.hpn_zone
        if not DaraCore.is_null(request.machine_type):
            body['MachineType'] = request.machine_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            body['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFreeHyperNodes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFreeHyperNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_free_hyper_nodes(
        self,
        request: main_models.ListFreeHyperNodesRequest,
    ) -> main_models.ListFreeHyperNodesResponse:
        runtime = RuntimeOptions()
        return self.list_free_hyper_nodes_with_options(request, runtime)

    async def list_free_hyper_nodes_async(
        self,
        request: main_models.ListFreeHyperNodesRequest,
    ) -> main_models.ListFreeHyperNodesResponse:
        runtime = RuntimeOptions()
        return await self.list_free_hyper_nodes_with_options_async(request, runtime)

    def list_free_nodes_with_options(
        self,
        request: main_models.ListFreeNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFreeNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not DaraCore.is_null(request.hpn_zone):
            body['HpnZone'] = request.hpn_zone
        if not DaraCore.is_null(request.machine_type):
            body['MachineType'] = request.machine_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.operating_states):
            body['OperatingStates'] = request.operating_states
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFreeNodes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFreeNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_free_nodes_with_options_async(
        self,
        request: main_models.ListFreeNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListFreeNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        body = {}
        if not DaraCore.is_null(request.hpn_zone):
            body['HpnZone'] = request.hpn_zone
        if not DaraCore.is_null(request.machine_type):
            body['MachineType'] = request.machine_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.operating_states):
            body['OperatingStates'] = request.operating_states
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListFreeNodes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFreeNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_free_nodes(
        self,
        request: main_models.ListFreeNodesRequest,
    ) -> main_models.ListFreeNodesResponse:
        runtime = RuntimeOptions()
        return self.list_free_nodes_with_options(request, runtime)

    async def list_free_nodes_async(
        self,
        request: main_models.ListFreeNodesRequest,
    ) -> main_models.ListFreeNodesResponse:
        runtime = RuntimeOptions()
        return await self.list_free_nodes_with_options_async(request, runtime)

    def list_hyper_nodes_with_options(
        self,
        tmp_req: main_models.ListHyperNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHyperNodesResponse:
        tmp_req.validate()
        request = main_models.ListHyperNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operating_states):
            request.operating_states_shrink = Utils.array_to_string_with_specified_style(tmp_req.operating_states, 'OperatingStates', 'json')
        query = {}
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.operating_states_shrink):
            query['OperatingStates'] = request.operating_states_shrink
        body = {}
        if not DaraCore.is_null(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.hpn_zone):
            body['HpnZone'] = request.hpn_zone
        if not DaraCore.is_null(request.hyper_node_id):
            body['HyperNodeId'] = request.hyper_node_id
        if not DaraCore.is_null(request.machine_type):
            body['MachineType'] = request.machine_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_group_name):
            body['NodeGroupName'] = request.node_group_name
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHyperNodes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHyperNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_hyper_nodes_with_options_async(
        self,
        tmp_req: main_models.ListHyperNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListHyperNodesResponse:
        tmp_req.validate()
        request = main_models.ListHyperNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operating_states):
            request.operating_states_shrink = Utils.array_to_string_with_specified_style(tmp_req.operating_states, 'OperatingStates', 'json')
        query = {}
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.operating_states_shrink):
            query['OperatingStates'] = request.operating_states_shrink
        body = {}
        if not DaraCore.is_null(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.hpn_zone):
            body['HpnZone'] = request.hpn_zone
        if not DaraCore.is_null(request.hyper_node_id):
            body['HyperNodeId'] = request.hyper_node_id
        if not DaraCore.is_null(request.machine_type):
            body['MachineType'] = request.machine_type
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_group_name):
            body['NodeGroupName'] = request.node_group_name
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListHyperNodes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListHyperNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_hyper_nodes(
        self,
        request: main_models.ListHyperNodesRequest,
    ) -> main_models.ListHyperNodesResponse:
        runtime = RuntimeOptions()
        return self.list_hyper_nodes_with_options(request, runtime)

    async def list_hyper_nodes_async(
        self,
        request: main_models.ListHyperNodesRequest,
    ) -> main_models.ListHyperNodesResponse:
        runtime = RuntimeOptions()
        return await self.list_hyper_nodes_with_options_async(request, runtime)

    def list_images_with_options(
        self,
        request: main_models.ListImagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListImagesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.architecture):
            body['Architecture'] = request.architecture
        if not DaraCore.is_null(request.image_version):
            body['ImageVersion'] = request.image_version
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListImages',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_images_with_options_async(
        self,
        request: main_models.ListImagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListImagesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.architecture):
            body['Architecture'] = request.architecture
        if not DaraCore.is_null(request.image_version):
            body['ImageVersion'] = request.image_version
        if not DaraCore.is_null(request.platform):
            body['Platform'] = request.platform
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListImages',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListImagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_images(
        self,
        request: main_models.ListImagesRequest,
    ) -> main_models.ListImagesResponse:
        runtime = RuntimeOptions()
        return self.list_images_with_options(request, runtime)

    async def list_images_async(
        self,
        request: main_models.ListImagesRequest,
    ) -> main_models.ListImagesResponse:
        runtime = RuntimeOptions()
        return await self.list_images_with_options_async(request, runtime)

    def list_machine_network_info_with_options(
        self,
        tmp_req: main_models.ListMachineNetworkInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMachineNetworkInfoResponse:
        tmp_req.validate()
        request = main_models.ListMachineNetworkInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.machine_hpn_info):
            request.machine_hpn_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.machine_hpn_info, 'MachineHpnInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.machine_hpn_info_shrink):
            body['MachineHpnInfo'] = request.machine_hpn_info_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMachineNetworkInfo',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMachineNetworkInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_machine_network_info_with_options_async(
        self,
        tmp_req: main_models.ListMachineNetworkInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMachineNetworkInfoResponse:
        tmp_req.validate()
        request = main_models.ListMachineNetworkInfoShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.machine_hpn_info):
            request.machine_hpn_info_shrink = Utils.array_to_string_with_specified_style(tmp_req.machine_hpn_info, 'MachineHpnInfo', 'json')
        body = {}
        if not DaraCore.is_null(request.machine_hpn_info_shrink):
            body['MachineHpnInfo'] = request.machine_hpn_info_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMachineNetworkInfo',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMachineNetworkInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_machine_network_info(
        self,
        request: main_models.ListMachineNetworkInfoRequest,
    ) -> main_models.ListMachineNetworkInfoResponse:
        runtime = RuntimeOptions()
        return self.list_machine_network_info_with_options(request, runtime)

    async def list_machine_network_info_async(
        self,
        request: main_models.ListMachineNetworkInfoRequest,
    ) -> main_models.ListMachineNetworkInfoResponse:
        runtime = RuntimeOptions()
        return await self.list_machine_network_info_with_options_async(request, runtime)

    def list_machine_types_with_options(
        self,
        request: main_models.ListMachineTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMachineTypesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMachineTypes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMachineTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_machine_types_with_options_async(
        self,
        request: main_models.ListMachineTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMachineTypesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListMachineTypes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMachineTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_machine_types(
        self,
        request: main_models.ListMachineTypesRequest,
    ) -> main_models.ListMachineTypesResponse:
        runtime = RuntimeOptions()
        return self.list_machine_types_with_options(request, runtime)

    async def list_machine_types_async(
        self,
        request: main_models.ListMachineTypesRequest,
    ) -> main_models.ListMachineTypesResponse:
        runtime = RuntimeOptions()
        return await self.list_machine_types_with_options_async(request, runtime)

    def list_net_test_results_with_options(
        self,
        request: main_models.ListNetTestResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetTestResultsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.net_test_type):
            body['NetTestType'] = request.net_test_type
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNetTestResults',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetTestResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_net_test_results_with_options_async(
        self,
        request: main_models.ListNetTestResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNetTestResultsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.net_test_type):
            body['NetTestType'] = request.net_test_type
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNetTestResults',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNetTestResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_net_test_results(
        self,
        request: main_models.ListNetTestResultsRequest,
    ) -> main_models.ListNetTestResultsResponse:
        runtime = RuntimeOptions()
        return self.list_net_test_results_with_options(request, runtime)

    async def list_net_test_results_async(
        self,
        request: main_models.ListNetTestResultsRequest,
    ) -> main_models.ListNetTestResultsResponse:
        runtime = RuntimeOptions()
        return await self.list_net_test_results_with_options_async(request, runtime)

    def list_node_groups_with_options(
        self,
        request: main_models.ListNodeGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodeGroupsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNodeGroups',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodeGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_groups_with_options_async(
        self,
        request: main_models.ListNodeGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodeGroupsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListNodeGroups',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodeGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_groups(
        self,
        request: main_models.ListNodeGroupsRequest,
    ) -> main_models.ListNodeGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_node_groups_with_options(request, runtime)

    async def list_node_groups_async(
        self,
        request: main_models.ListNodeGroupsRequest,
    ) -> main_models.ListNodeGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_node_groups_with_options_async(request, runtime)

    def list_syslogs_with_options(
        self,
        request: main_models.ListSyslogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSyslogsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.from_time):
            body['FromTime'] = request.from_time
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.reverse):
            body['Reverse'] = request.reverse
        if not DaraCore.is_null(request.to_time):
            body['ToTime'] = request.to_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSyslogs',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSyslogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_syslogs_with_options_async(
        self,
        request: main_models.ListSyslogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSyslogsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.from_time):
            body['FromTime'] = request.from_time
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_id):
            body['NodeId'] = request.node_id
        if not DaraCore.is_null(request.query):
            body['Query'] = request.query
        if not DaraCore.is_null(request.reverse):
            body['Reverse'] = request.reverse
        if not DaraCore.is_null(request.to_time):
            body['ToTime'] = request.to_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListSyslogs',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSyslogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_syslogs(
        self,
        request: main_models.ListSyslogsRequest,
    ) -> main_models.ListSyslogsResponse:
        runtime = RuntimeOptions()
        return self.list_syslogs_with_options(request, runtime)

    async def list_syslogs_async(
        self,
        request: main_models.ListSyslogsRequest,
    ) -> main_models.ListSyslogsResponse:
        runtime = RuntimeOptions()
        return await self.list_syslogs_with_options_async(request, runtime)

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
            version = '2022-12-15',
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
            version = '2022-12-15',
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

    def list_user_cluster_types_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserClusterTypesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListUserClusterTypes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserClusterTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_cluster_types_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListUserClusterTypesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListUserClusterTypes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserClusterTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_cluster_types(self) -> main_models.ListUserClusterTypesResponse:
        runtime = RuntimeOptions()
        return self.list_user_cluster_types_with_options(runtime)

    async def list_user_cluster_types_async(self) -> main_models.ListUserClusterTypesResponse:
        runtime = RuntimeOptions()
        return await self.list_user_cluster_types_with_options_async(runtime)

    def list_vscs_with_options(
        self,
        tmp_req: main_models.ListVscsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVscsResponse:
        tmp_req.validate()
        request = main_models.ListVscsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_ids):
            request.node_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_ids, 'NodeIds', 'json')
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_ids_shrink):
            body['NodeIds'] = request.node_ids_shrink
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vsc_name):
            body['VscName'] = request.vsc_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVscs',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVscsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vscs_with_options_async(
        self,
        tmp_req: main_models.ListVscsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListVscsResponse:
        tmp_req.validate()
        request = main_models.ListVscsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_ids):
            request.node_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_ids, 'NodeIds', 'json')
        query = {}
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        body = {}
        if not DaraCore.is_null(request.max_results):
            body['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            body['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_ids_shrink):
            body['NodeIds'] = request.node_ids_shrink
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vsc_name):
            body['VscName'] = request.vsc_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListVscs',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListVscsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_vscs(
        self,
        request: main_models.ListVscsRequest,
    ) -> main_models.ListVscsResponse:
        runtime = RuntimeOptions()
        return self.list_vscs_with_options(request, runtime)

    async def list_vscs_async(
        self,
        request: main_models.ListVscsRequest,
    ) -> main_models.ListVscsResponse:
        runtime = RuntimeOptions()
        return await self.list_vscs_with_options_async(request, runtime)

    def reboot_nodes_with_options(
        self,
        tmp_req: main_models.RebootNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootNodesResponse:
        tmp_req.validate()
        request = main_models.RebootNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.nodes):
            request.nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.nodes, 'Nodes', 'json')
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not DaraCore.is_null(request.nodes_shrink):
            body['Nodes'] = request.nodes_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RebootNodes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def reboot_nodes_with_options_async(
        self,
        tmp_req: main_models.RebootNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RebootNodesResponse:
        tmp_req.validate()
        request = main_models.RebootNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.nodes):
            request.nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.nodes, 'Nodes', 'json')
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not DaraCore.is_null(request.nodes_shrink):
            body['Nodes'] = request.nodes_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RebootNodes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RebootNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reboot_nodes(
        self,
        request: main_models.RebootNodesRequest,
    ) -> main_models.RebootNodesResponse:
        runtime = RuntimeOptions()
        return self.reboot_nodes_with_options(request, runtime)

    async def reboot_nodes_async(
        self,
        request: main_models.RebootNodesRequest,
    ) -> main_models.RebootNodesResponse:
        runtime = RuntimeOptions()
        return await self.reboot_nodes_with_options_async(request, runtime)

    def reimage_nodes_with_options(
        self,
        tmp_req: main_models.ReimageNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReimageNodesResponse:
        tmp_req.validate()
        request = main_models.ReimageNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.nodes):
            request.nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.nodes, 'Nodes', 'json')
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not DaraCore.is_null(request.nodes_shrink):
            body['Nodes'] = request.nodes_shrink
        if not DaraCore.is_null(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReimageNodes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReimageNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def reimage_nodes_with_options_async(
        self,
        tmp_req: main_models.ReimageNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReimageNodesResponse:
        tmp_req.validate()
        request = main_models.ReimageNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.nodes):
            request.nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.nodes, 'Nodes', 'json')
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not DaraCore.is_null(request.nodes_shrink):
            body['Nodes'] = request.nodes_shrink
        if not DaraCore.is_null(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReimageNodes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReimageNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reimage_nodes(
        self,
        request: main_models.ReimageNodesRequest,
    ) -> main_models.ReimageNodesResponse:
        runtime = RuntimeOptions()
        return self.reimage_nodes_with_options(request, runtime)

    async def reimage_nodes_async(
        self,
        request: main_models.ReimageNodesRequest,
    ) -> main_models.ReimageNodesResponse:
        runtime = RuntimeOptions()
        return await self.reimage_nodes_with_options_async(request, runtime)

    def report_nodes_status_with_options(
        self,
        tmp_req: main_models.ReportNodesStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReportNodesStatusResponse:
        tmp_req.validate()
        request = main_models.ReportNodesStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.nodes):
            request.nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.nodes, 'Nodes', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.issue_category):
            body['IssueCategory'] = request.issue_category
        if not DaraCore.is_null(request.nodes_shrink):
            body['Nodes'] = request.nodes_shrink
        if not DaraCore.is_null(request.reason):
            body['Reason'] = request.reason
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReportNodesStatus',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReportNodesStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def report_nodes_status_with_options_async(
        self,
        tmp_req: main_models.ReportNodesStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReportNodesStatusResponse:
        tmp_req.validate()
        request = main_models.ReportNodesStatusShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.nodes):
            request.nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.nodes, 'Nodes', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.issue_category):
            body['IssueCategory'] = request.issue_category
        if not DaraCore.is_null(request.nodes_shrink):
            body['Nodes'] = request.nodes_shrink
        if not DaraCore.is_null(request.reason):
            body['Reason'] = request.reason
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ReportNodesStatus',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReportNodesStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def report_nodes_status(
        self,
        request: main_models.ReportNodesStatusRequest,
    ) -> main_models.ReportNodesStatusResponse:
        runtime = RuntimeOptions()
        return self.report_nodes_status_with_options(request, runtime)

    async def report_nodes_status_async(
        self,
        request: main_models.ReportNodesStatusRequest,
    ) -> main_models.ReportNodesStatusResponse:
        runtime = RuntimeOptions()
        return await self.report_nodes_status_with_options_async(request, runtime)

    def run_command_with_options(
        self,
        tmp_req: main_models.RunCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunCommandResponse:
        tmp_req.validate()
        request = main_models.RunCommandShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_id_list):
            request.node_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_id_list, 'NodeIdList', 'json')
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.command_content):
            body['CommandContent'] = request.command_content
        if not DaraCore.is_null(request.command_id):
            body['CommandId'] = request.command_id
        if not DaraCore.is_null(request.content_encoding):
            body['ContentEncoding'] = request.content_encoding
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enable_parameter):
            body['EnableParameter'] = request.enable_parameter
        if not DaraCore.is_null(request.frequency):
            body['Frequency'] = request.frequency
        if not DaraCore.is_null(request.launcher):
            body['Launcher'] = request.launcher
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.node_id_list_shrink):
            body['NodeIdList'] = request.node_id_list_shrink
        if not DaraCore.is_null(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.repeat_mode):
            body['RepeatMode'] = request.repeat_mode
        if not DaraCore.is_null(request.termination_mode):
            body['TerminationMode'] = request.termination_mode
        if not DaraCore.is_null(request.timeout):
            body['Timeout'] = request.timeout
        if not DaraCore.is_null(request.username):
            body['Username'] = request.username
        if not DaraCore.is_null(request.working_dir):
            body['WorkingDir'] = request.working_dir
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCommand',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCommandResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_command_with_options_async(
        self,
        tmp_req: main_models.RunCommandRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunCommandResponse:
        tmp_req.validate()
        request = main_models.RunCommandShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_id_list):
            request.node_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_id_list, 'NodeIdList', 'json')
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        body = {}
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.command_content):
            body['CommandContent'] = request.command_content
        if not DaraCore.is_null(request.command_id):
            body['CommandId'] = request.command_id
        if not DaraCore.is_null(request.content_encoding):
            body['ContentEncoding'] = request.content_encoding
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.enable_parameter):
            body['EnableParameter'] = request.enable_parameter
        if not DaraCore.is_null(request.frequency):
            body['Frequency'] = request.frequency
        if not DaraCore.is_null(request.launcher):
            body['Launcher'] = request.launcher
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.node_id_list_shrink):
            body['NodeIdList'] = request.node_id_list_shrink
        if not DaraCore.is_null(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.repeat_mode):
            body['RepeatMode'] = request.repeat_mode
        if not DaraCore.is_null(request.termination_mode):
            body['TerminationMode'] = request.termination_mode
        if not DaraCore.is_null(request.timeout):
            body['Timeout'] = request.timeout
        if not DaraCore.is_null(request.username):
            body['Username'] = request.username
        if not DaraCore.is_null(request.working_dir):
            body['WorkingDir'] = request.working_dir
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCommand',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunCommandResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_command(
        self,
        request: main_models.RunCommandRequest,
    ) -> main_models.RunCommandResponse:
        runtime = RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    async def run_command_async(
        self,
        request: main_models.RunCommandRequest,
    ) -> main_models.RunCommandResponse:
        runtime = RuntimeOptions()
        return await self.run_command_with_options_async(request, runtime)

    def send_file_with_options(
        self,
        tmp_req: main_models.SendFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendFileResponse:
        tmp_req.validate()
        request = main_models.SendFileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_id_list):
            request.node_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_id_list, 'NodeIdList', 'json')
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.content_type):
            body['ContentType'] = request.content_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.file_group):
            body['FileGroup'] = request.file_group
        if not DaraCore.is_null(request.file_mode):
            body['FileMode'] = request.file_mode
        if not DaraCore.is_null(request.file_owner):
            body['FileOwner'] = request.file_owner
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.node_id_list_shrink):
            body['NodeIdList'] = request.node_id_list_shrink
        if not DaraCore.is_null(request.overwrite):
            body['Overwrite'] = request.overwrite
        if not DaraCore.is_null(request.target_dir):
            body['TargetDir'] = request.target_dir
        if not DaraCore.is_null(request.timeout):
            body['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendFile',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_file_with_options_async(
        self,
        tmp_req: main_models.SendFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendFileResponse:
        tmp_req.validate()
        request = main_models.SendFileShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_id_list):
            request.node_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_id_list, 'NodeIdList', 'json')
        body = {}
        if not DaraCore.is_null(request.content):
            body['Content'] = request.content
        if not DaraCore.is_null(request.content_type):
            body['ContentType'] = request.content_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.file_group):
            body['FileGroup'] = request.file_group
        if not DaraCore.is_null(request.file_mode):
            body['FileMode'] = request.file_mode
        if not DaraCore.is_null(request.file_owner):
            body['FileOwner'] = request.file_owner
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.node_id_list_shrink):
            body['NodeIdList'] = request.node_id_list_shrink
        if not DaraCore.is_null(request.overwrite):
            body['Overwrite'] = request.overwrite
        if not DaraCore.is_null(request.target_dir):
            body['TargetDir'] = request.target_dir
        if not DaraCore.is_null(request.timeout):
            body['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendFile',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_file(
        self,
        request: main_models.SendFileRequest,
    ) -> main_models.SendFileResponse:
        runtime = RuntimeOptions()
        return self.send_file_with_options(request, runtime)

    async def send_file_async(
        self,
        request: main_models.SendFileRequest,
    ) -> main_models.SendFileResponse:
        runtime = RuntimeOptions()
        return await self.send_file_with_options_async(request, runtime)

    def shrink_cluster_with_options(
        self,
        tmp_req: main_models.ShrinkClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ShrinkClusterResponse:
        tmp_req.validate()
        request = main_models.ShrinkClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_groups):
            request.node_groups_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_groups, 'NodeGroups', 'json')
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not DaraCore.is_null(request.node_groups_shrink):
            body['NodeGroups'] = request.node_groups_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ShrinkCluster',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ShrinkClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def shrink_cluster_with_options_async(
        self,
        tmp_req: main_models.ShrinkClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ShrinkClusterResponse:
        tmp_req.validate()
        request = main_models.ShrinkClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_groups):
            request.node_groups_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_groups, 'NodeGroups', 'json')
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not DaraCore.is_null(request.node_groups_shrink):
            body['NodeGroups'] = request.node_groups_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ShrinkCluster',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ShrinkClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def shrink_cluster(
        self,
        request: main_models.ShrinkClusterRequest,
    ) -> main_models.ShrinkClusterResponse:
        runtime = RuntimeOptions()
        return self.shrink_cluster_with_options(request, runtime)

    async def shrink_cluster_async(
        self,
        request: main_models.ShrinkClusterRequest,
    ) -> main_models.ShrinkClusterResponse:
        runtime = RuntimeOptions()
        return await self.shrink_cluster_with_options_async(request, runtime)

    def stop_invocation_with_options(
        self,
        tmp_req: main_models.StopInvocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopInvocationResponse:
        tmp_req.validate()
        request = main_models.StopInvocationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_id_list):
            request.node_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_id_list, 'NodeIdList', 'json')
        body = {}
        if not DaraCore.is_null(request.invoke_id):
            body['InvokeId'] = request.invoke_id
        if not DaraCore.is_null(request.node_id_list_shrink):
            body['NodeIdList'] = request.node_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopInvocation',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInvocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_invocation_with_options_async(
        self,
        tmp_req: main_models.StopInvocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopInvocationResponse:
        tmp_req.validate()
        request = main_models.StopInvocationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.node_id_list):
            request.node_id_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_id_list, 'NodeIdList', 'json')
        body = {}
        if not DaraCore.is_null(request.invoke_id):
            body['InvokeId'] = request.invoke_id
        if not DaraCore.is_null(request.node_id_list_shrink):
            body['NodeIdList'] = request.node_id_list_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopInvocation',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopInvocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_invocation(
        self,
        request: main_models.StopInvocationRequest,
    ) -> main_models.StopInvocationResponse:
        runtime = RuntimeOptions()
        return self.stop_invocation_with_options(request, runtime)

    async def stop_invocation_async(
        self,
        request: main_models.StopInvocationRequest,
    ) -> main_models.StopInvocationResponse:
        runtime = RuntimeOptions()
        return await self.stop_invocation_with_options_async(request, runtime)

    def stop_nodes_with_options(
        self,
        tmp_req: main_models.StopNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopNodesResponse:
        tmp_req.validate()
        request = main_models.StopNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.nodes):
            request.nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.nodes, 'Nodes', 'json')
        body = {}
        if not DaraCore.is_null(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not DaraCore.is_null(request.nodes_shrink):
            body['Nodes'] = request.nodes_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopNodes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_nodes_with_options_async(
        self,
        tmp_req: main_models.StopNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopNodesResponse:
        tmp_req.validate()
        request = main_models.StopNodesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.nodes):
            request.nodes_shrink = Utils.array_to_string_with_specified_style(tmp_req.nodes, 'Nodes', 'json')
        body = {}
        if not DaraCore.is_null(request.ignore_failed_node_tasks):
            body['IgnoreFailedNodeTasks'] = request.ignore_failed_node_tasks
        if not DaraCore.is_null(request.nodes_shrink):
            body['Nodes'] = request.nodes_shrink
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'StopNodes',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_nodes(
        self,
        request: main_models.StopNodesRequest,
    ) -> main_models.StopNodesResponse:
        runtime = RuntimeOptions()
        return self.stop_nodes_with_options(request, runtime)

    async def stop_nodes_async(
        self,
        request: main_models.StopNodesRequest,
    ) -> main_models.StopNodesResponse:
        runtime = RuntimeOptions()
        return await self.stop_nodes_with_options_async(request, runtime)

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
            version = '2022-12-15',
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
            version = '2022-12-15',
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
            version = '2022-12-15',
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
            version = '2022-12-15',
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

    def update_node_group_with_options(
        self,
        request: main_models.UpdateNodeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNodeGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_system_mount_enabled):
            body['FileSystemMountEnabled'] = request.file_system_mount_enabled
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.key_pair_name):
            body['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.login_password):
            body['LoginPassword'] = request.login_password
        if not DaraCore.is_null(request.new_node_group_name):
            body['NewNodeGroupName'] = request.new_node_group_name
        if not DaraCore.is_null(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNodeGroup',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_node_group_with_options_async(
        self,
        request: main_models.UpdateNodeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNodeGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.file_system_mount_enabled):
            body['FileSystemMountEnabled'] = request.file_system_mount_enabled
        if not DaraCore.is_null(request.image_id):
            body['ImageId'] = request.image_id
        if not DaraCore.is_null(request.key_pair_name):
            body['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.login_password):
            body['LoginPassword'] = request.login_password
        if not DaraCore.is_null(request.new_node_group_name):
            body['NewNodeGroupName'] = request.new_node_group_name
        if not DaraCore.is_null(request.node_group_id):
            body['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.user_data):
            body['UserData'] = request.user_data
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNodeGroup',
            version = '2022-12-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_node_group(
        self,
        request: main_models.UpdateNodeGroupRequest,
    ) -> main_models.UpdateNodeGroupResponse:
        runtime = RuntimeOptions()
        return self.update_node_group_with_options(request, runtime)

    async def update_node_group_async(
        self,
        request: main_models.UpdateNodeGroupRequest,
    ) -> main_models.UpdateNodeGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_node_group_with_options_async(request, runtime)
