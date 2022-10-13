# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_emr20210320 import models as emr_20210320_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-beijing': 'emr.aliyuncs.com',
            'cn-hangzhou': 'emr.aliyuncs.com',
            'cn-shanghai': 'emr.aliyuncs.com',
            'cn-shenzhen': 'emr.aliyuncs.com',
            'ap-southeast-1': 'emr.aliyuncs.com',
            'us-west-1': 'emr.aliyuncs.com',
            'cn-hangzhou-finance': 'emr.aliyuncs.com',
            'cn-shenzhen-finance-1': 'emr.aliyuncs.com',
            'cn-shanghai-finance-1': 'emr.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('emr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_cluster_with_options(
        self,
        request: emr_20210320_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.CreateClusterResponse:
        """
        调用CreateCluster创建集群。
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_configs):
            query['ApplicationConfigs'] = request.application_configs
        if not UtilClient.is_unset(request.applications):
            query['Applications'] = request.applications
        if not UtilClient.is_unset(request.bootstrap_scripts):
            query['BootstrapScripts'] = request.bootstrap_scripts
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.deploy_mode):
            query['DeployMode'] = request.deploy_mode
        if not UtilClient.is_unset(request.node_attributes):
            query['NodeAttributes'] = request.node_attributes
        if not UtilClient.is_unset(request.node_groups):
            query['NodeGroups'] = request.node_groups
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.release_version):
            query['ReleaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_mode):
            query['SecurityMode'] = request.security_mode
        if not UtilClient.is_unset(request.subscription_config):
            query['SubscriptionConfig'] = request.subscription_config
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: emr_20210320_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.CreateClusterResponse:
        """
        调用CreateCluster创建集群。
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_configs):
            query['ApplicationConfigs'] = request.application_configs
        if not UtilClient.is_unset(request.applications):
            query['Applications'] = request.applications
        if not UtilClient.is_unset(request.bootstrap_scripts):
            query['BootstrapScripts'] = request.bootstrap_scripts
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.deploy_mode):
            query['DeployMode'] = request.deploy_mode
        if not UtilClient.is_unset(request.node_attributes):
            query['NodeAttributes'] = request.node_attributes
        if not UtilClient.is_unset(request.node_groups):
            query['NodeGroups'] = request.node_groups
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.release_version):
            query['ReleaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_mode):
            query['SecurityMode'] = request.security_mode
        if not UtilClient.is_unset(request.subscription_config):
            query['SubscriptionConfig'] = request.subscription_config
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: emr_20210320_models.CreateClusterRequest,
    ) -> emr_20210320_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: emr_20210320_models.CreateClusterRequest,
    ) -> emr_20210320_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def decrease_nodes_with_options(
        self,
        request: emr_20210320_models.DecreaseNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.DecreaseNodesResponse:
        """
        缩容节点。
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.decrease_node_count):
            query['DecreaseNodeCount'] = request.decrease_node_count
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DecreaseNodes',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.DecreaseNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def decrease_nodes_with_options_async(
        self,
        request: emr_20210320_models.DecreaseNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.DecreaseNodesResponse:
        """
        缩容节点。
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.decrease_node_count):
            query['DecreaseNodeCount'] = request.decrease_node_count
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DecreaseNodes',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.DecreaseNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def decrease_nodes(
        self,
        request: emr_20210320_models.DecreaseNodesRequest,
    ) -> emr_20210320_models.DecreaseNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.decrease_nodes_with_options(request, runtime)

    async def decrease_nodes_async(
        self,
        request: emr_20210320_models.DecreaseNodesRequest,
    ) -> emr_20210320_models.DecreaseNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.decrease_nodes_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: emr_20210320_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.DeleteClusterResponse:
        """
        删除集群。
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: emr_20210320_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.DeleteClusterResponse:
        """
        删除集群。
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        request: emr_20210320_models.DeleteClusterRequest,
    ) -> emr_20210320_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: emr_20210320_models.DeleteClusterRequest,
    ) -> emr_20210320_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def get_cluster_with_options(
        self,
        request: emr_20210320_models.GetClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetClusterResponse:
        """
        调用GetCluster获取集群详情。
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_with_options_async(
        self,
        request: emr_20210320_models.GetClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetClusterResponse:
        """
        调用GetCluster获取集群详情。
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster(
        self,
        request: emr_20210320_models.GetClusterRequest,
    ) -> emr_20210320_models.GetClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_with_options(request, runtime)

    async def get_cluster_async(
        self,
        request: emr_20210320_models.GetClusterRequest,
    ) -> emr_20210320_models.GetClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_with_options_async(request, runtime)

    def get_node_group_with_options(
        self,
        request: emr_20210320_models.GetNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetNodeGroupResponse:
        """
        获取节点组详情。
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNodeGroup',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_group_with_options_async(
        self,
        request: emr_20210320_models.GetNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetNodeGroupResponse:
        """
        获取节点组详情。
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNodeGroup',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node_group(
        self,
        request: emr_20210320_models.GetNodeGroupRequest,
    ) -> emr_20210320_models.GetNodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_node_group_with_options(request, runtime)

    async def get_node_group_async(
        self,
        request: emr_20210320_models.GetNodeGroupRequest,
    ) -> emr_20210320_models.GetNodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_node_group_with_options_async(request, runtime)

    def get_operation_with_options(
        self,
        request: emr_20210320_models.GetOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetOperationResponse:
        """
        获取操作详情。
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.operation_id):
            query['OperationId'] = request.operation_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOperation',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_operation_with_options_async(
        self,
        request: emr_20210320_models.GetOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetOperationResponse:
        """
        获取操作详情。
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.operation_id):
            query['OperationId'] = request.operation_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOperation',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_operation(
        self,
        request: emr_20210320_models.GetOperationRequest,
    ) -> emr_20210320_models.GetOperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_operation_with_options(request, runtime)

    async def get_operation_async(
        self,
        request: emr_20210320_models.GetOperationRequest,
    ) -> emr_20210320_models.GetOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_operation_with_options_async(request, runtime)

    def increase_nodes_with_options(
        self,
        request: emr_20210320_models.IncreaseNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.IncreaseNodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_configs):
            query['ApplicationConfigs'] = request.application_configs
        if not UtilClient.is_unset(request.auto_pay_order):
            query['AutoPayOrder'] = request.auto_pay_order
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.increase_node_count):
            query['IncreaseNodeCount'] = request.increase_node_count
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.payment_duration):
            query['PaymentDuration'] = request.payment_duration
        if not UtilClient.is_unset(request.payment_duration_unit):
            query['PaymentDurationUnit'] = request.payment_duration_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IncreaseNodes',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.IncreaseNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def increase_nodes_with_options_async(
        self,
        request: emr_20210320_models.IncreaseNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.IncreaseNodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_configs):
            query['ApplicationConfigs'] = request.application_configs
        if not UtilClient.is_unset(request.auto_pay_order):
            query['AutoPayOrder'] = request.auto_pay_order
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.increase_node_count):
            query['IncreaseNodeCount'] = request.increase_node_count
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.payment_duration):
            query['PaymentDuration'] = request.payment_duration
        if not UtilClient.is_unset(request.payment_duration_unit):
            query['PaymentDurationUnit'] = request.payment_duration_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IncreaseNodes',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.IncreaseNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def increase_nodes(
        self,
        request: emr_20210320_models.IncreaseNodesRequest,
    ) -> emr_20210320_models.IncreaseNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.increase_nodes_with_options(request, runtime)

    async def increase_nodes_async(
        self,
        request: emr_20210320_models.IncreaseNodesRequest,
    ) -> emr_20210320_models.IncreaseNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.increase_nodes_with_options_async(request, runtime)

    def join_resource_group_with_options(
        self,
        request: emr_20210320_models.JoinResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.JoinResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinResourceGroup',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.JoinResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_resource_group_with_options_async(
        self,
        request: emr_20210320_models.JoinResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.JoinResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinResourceGroup',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.JoinResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def join_resource_group(
        self,
        request: emr_20210320_models.JoinResourceGroupRequest,
    ) -> emr_20210320_models.JoinResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_resource_group_with_options(request, runtime)

    async def join_resource_group_async(
        self,
        request: emr_20210320_models.JoinResourceGroupRequest,
    ) -> emr_20210320_models.JoinResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_resource_group_with_options_async(request, runtime)

    def list_node_groups_with_options(
        self,
        request: emr_20210320_models.ListNodeGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListNodeGroupsResponse:
        """
        查询节点组。
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_group_ids):
            query['NodeGroupIds'] = request.node_group_ids
        if not UtilClient.is_unset(request.node_group_names):
            query['NodeGroupNames'] = request.node_group_names
        if not UtilClient.is_unset(request.node_group_states):
            query['NodeGroupStates'] = request.node_group_states
        if not UtilClient.is_unset(request.node_group_types):
            query['NodeGroupTypes'] = request.node_group_types
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeGroups',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListNodeGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_groups_with_options_async(
        self,
        request: emr_20210320_models.ListNodeGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListNodeGroupsResponse:
        """
        查询节点组。
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_group_ids):
            query['NodeGroupIds'] = request.node_group_ids
        if not UtilClient.is_unset(request.node_group_names):
            query['NodeGroupNames'] = request.node_group_names
        if not UtilClient.is_unset(request.node_group_states):
            query['NodeGroupStates'] = request.node_group_states
        if not UtilClient.is_unset(request.node_group_types):
            query['NodeGroupTypes'] = request.node_group_types
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeGroups',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListNodeGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_groups(
        self,
        request: emr_20210320_models.ListNodeGroupsRequest,
    ) -> emr_20210320_models.ListNodeGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_node_groups_with_options(request, runtime)

    async def list_node_groups_async(
        self,
        request: emr_20210320_models.ListNodeGroupsRequest,
    ) -> emr_20210320_models.ListNodeGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_node_groups_with_options_async(request, runtime)

    def list_nodes_with_options(
        self,
        request: emr_20210320_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListNodesResponse:
        """
        查询节点。
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_group_ids):
            query['NodeGroupIds'] = request.node_group_ids
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.node_names):
            query['NodeNames'] = request.node_names
        if not UtilClient.is_unset(request.node_states):
            query['NodeStates'] = request.node_states
        if not UtilClient.is_unset(request.private_ips):
            query['PrivateIps'] = request.private_ips
        if not UtilClient.is_unset(request.public_ips):
            query['PublicIps'] = request.public_ips
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        request: emr_20210320_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListNodesResponse:
        """
        查询节点。
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_group_ids):
            query['NodeGroupIds'] = request.node_group_ids
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.node_names):
            query['NodeNames'] = request.node_names
        if not UtilClient.is_unset(request.node_states):
            query['NodeStates'] = request.node_states
        if not UtilClient.is_unset(request.private_ips):
            query['PrivateIps'] = request.private_ips
        if not UtilClient.is_unset(request.public_ips):
            query['PublicIps'] = request.public_ips
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: emr_20210320_models.ListNodesRequest,
    ) -> emr_20210320_models.ListNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: emr_20210320_models.ListNodesRequest,
    ) -> emr_20210320_models.ListNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)
