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
        runtime = util_models.RuntimeOptions()
        return self.approve_operation_with_options(request, runtime)

    async def approve_operation_async(
        self,
        request: eflo_controller_20221215_models.ApproveOperationRequest,
    ) -> eflo_controller_20221215_models.ApproveOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.approve_operation_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: eflo_controller_20221215_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ChangeResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
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
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: eflo_controller_20221215_models.ChangeResourceGroupRequest,
    ) -> eflo_controller_20221215_models.ChangeResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.CreateClusterResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: eflo_controller_20221215_models.CreateClusterRequest,
    ) -> eflo_controller_20221215_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: eflo_controller_20221215_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DeleteClusterResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: eflo_controller_20221215_models.DeleteClusterRequest,
    ) -> eflo_controller_20221215_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def describe_cluster_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeClusterResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_with_options(request, runtime)

    async def describe_cluster_async(
        self,
        request: eflo_controller_20221215_models.DescribeClusterRequest,
    ) -> eflo_controller_20221215_models.DescribeClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_with_options_async(request, runtime)

    def describe_invocations_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeInvocationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeInvocationsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_invocations_with_options(request, runtime)

    async def describe_invocations_async(
        self,
        request: eflo_controller_20221215_models.DescribeInvocationsRequest,
    ) -> eflo_controller_20221215_models.DescribeInvocationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_invocations_with_options_async(request, runtime)

    def describe_node_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeNodeResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_node_with_options(request, runtime)

    async def describe_node_async(
        self,
        request: eflo_controller_20221215_models.DescribeNodeRequest,
    ) -> eflo_controller_20221215_models.DescribeNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_node_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeRegionsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: eflo_controller_20221215_models.DescribeRegionsRequest,
    ) -> eflo_controller_20221215_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_send_file_results_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeSendFileResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeSendFileResultsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_send_file_results_with_options(request, runtime)

    async def describe_send_file_results_async(
        self,
        request: eflo_controller_20221215_models.DescribeSendFileResultsRequest,
    ) -> eflo_controller_20221215_models.DescribeSendFileResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_send_file_results_with_options_async(request, runtime)

    def describe_task_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeTaskResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_task_with_options(request, runtime)

    async def describe_task_async(
        self,
        request: eflo_controller_20221215_models.DescribeTaskRequest,
    ) -> eflo_controller_20221215_models.DescribeTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_task_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: eflo_controller_20221215_models.DescribeZonesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.DescribeZonesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: eflo_controller_20221215_models.DescribeZonesRequest,
    ) -> eflo_controller_20221215_models.DescribeZonesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def extend_cluster_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.ExtendClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ExtendClusterResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.extend_cluster_with_options(request, runtime)

    async def extend_cluster_async(
        self,
        request: eflo_controller_20221215_models.ExtendClusterRequest,
    ) -> eflo_controller_20221215_models.ExtendClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.extend_cluster_with_options_async(request, runtime)

    def list_cluster_nodes_with_options(
        self,
        request: eflo_controller_20221215_models.ListClusterNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListClusterNodesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_nodes_with_options(request, runtime)

    async def list_cluster_nodes_async(
        self,
        request: eflo_controller_20221215_models.ListClusterNodesRequest,
    ) -> eflo_controller_20221215_models.ListClusterNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_nodes_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: eflo_controller_20221215_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListClustersResponse:
        UtilClient.validate_model(request)
        body = {}
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
        UtilClient.validate_model(request)
        body = {}
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
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: eflo_controller_20221215_models.ListClustersRequest,
    ) -> eflo_controller_20221215_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_free_nodes_with_options(
        self,
        request: eflo_controller_20221215_models.ListFreeNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListFreeNodesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hpn_zone):
            body['HpnZone'] = request.hpn_zone
        if not UtilClient.is_unset(request.machine_type):
            body['MachineType'] = request.machine_type
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
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.hpn_zone):
            body['HpnZone'] = request.hpn_zone
        if not UtilClient.is_unset(request.machine_type):
            body['MachineType'] = request.machine_type
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
        runtime = util_models.RuntimeOptions()
        return self.list_free_nodes_with_options(request, runtime)

    async def list_free_nodes_async(
        self,
        request: eflo_controller_20221215_models.ListFreeNodesRequest,
    ) -> eflo_controller_20221215_models.ListFreeNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_free_nodes_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: eflo_controller_20221215_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ListTagResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: eflo_controller_20221215_models.ListTagResourcesRequest,
    ) -> eflo_controller_20221215_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def reboot_nodes_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.RebootNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.RebootNodesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.reboot_nodes_with_options(request, runtime)

    async def reboot_nodes_async(
        self,
        request: eflo_controller_20221215_models.RebootNodesRequest,
    ) -> eflo_controller_20221215_models.RebootNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reboot_nodes_with_options_async(request, runtime)

    def reimage_nodes_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.ReimageNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ReimageNodesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.reimage_nodes_with_options(request, runtime)

    async def reimage_nodes_async(
        self,
        request: eflo_controller_20221215_models.ReimageNodesRequest,
    ) -> eflo_controller_20221215_models.ReimageNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reimage_nodes_with_options_async(request, runtime)

    def run_command_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.RunCommandRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.RunCommandResponse:
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
        if not UtilClient.is_unset(request.content_encoding):
            body['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable_parameter):
            body['EnableParameter'] = request.enable_parameter
        if not UtilClient.is_unset(request.frequency):
            body['Frequency'] = request.frequency
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.node_id_list_shrink):
            body['NodeIdList'] = request.node_id_list_shrink
        if not UtilClient.is_unset(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.repeat_mode):
            body['RepeatMode'] = request.repeat_mode
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
        if not UtilClient.is_unset(request.content_encoding):
            body['ContentEncoding'] = request.content_encoding
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.enable_parameter):
            body['EnableParameter'] = request.enable_parameter
        if not UtilClient.is_unset(request.frequency):
            body['Frequency'] = request.frequency
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.node_id_list_shrink):
            body['NodeIdList'] = request.node_id_list_shrink
        if not UtilClient.is_unset(request.parameters_shrink):
            body['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.repeat_mode):
            body['RepeatMode'] = request.repeat_mode
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
        runtime = util_models.RuntimeOptions()
        return self.run_command_with_options(request, runtime)

    async def run_command_async(
        self,
        request: eflo_controller_20221215_models.RunCommandRequest,
    ) -> eflo_controller_20221215_models.RunCommandResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_command_with_options_async(request, runtime)

    def send_file_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.SendFileRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.SendFileResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.send_file_with_options(request, runtime)

    async def send_file_async(
        self,
        request: eflo_controller_20221215_models.SendFileRequest,
    ) -> eflo_controller_20221215_models.SendFileResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_file_with_options_async(request, runtime)

    def shrink_cluster_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.ShrinkClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.ShrinkClusterResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.shrink_cluster_with_options(request, runtime)

    async def shrink_cluster_async(
        self,
        request: eflo_controller_20221215_models.ShrinkClusterRequest,
    ) -> eflo_controller_20221215_models.ShrinkClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.shrink_cluster_with_options_async(request, runtime)

    def stop_invocation_with_options(
        self,
        tmp_req: eflo_controller_20221215_models.StopInvocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.StopInvocationResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.stop_invocation_with_options(request, runtime)

    async def stop_invocation_async(
        self,
        request: eflo_controller_20221215_models.StopInvocationRequest,
    ) -> eflo_controller_20221215_models.StopInvocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_invocation_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: eflo_controller_20221215_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.TagResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: eflo_controller_20221215_models.TagResourcesRequest,
    ) -> eflo_controller_20221215_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: eflo_controller_20221215_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_controller_20221215_models.UntagResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: eflo_controller_20221215_models.UntagResourcesRequest,
    ) -> eflo_controller_20221215_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)
