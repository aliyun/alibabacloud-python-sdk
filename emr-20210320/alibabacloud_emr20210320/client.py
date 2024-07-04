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
            'cn-shanghai-finance-1': 'emr.aliyuncs.com',
            'cn-shenzhen-finance-1': 'emr.aliyuncs.com',
            'cn-north-2-gov-1': 'emr.aliyuncs.com',
            'ap-northeast-2-pop': 'emr.aliyuncs.com',
            'cn-beijing-finance-1': 'emr.aliyuncs.com',
            'cn-beijing-finance-pop': 'emr.aliyuncs.com',
            'cn-beijing-gov-1': 'emr.aliyuncs.com',
            'cn-beijing-nu16-b01': 'emr.aliyuncs.com',
            'cn-edge-1': 'emr.aliyuncs.com',
            'cn-fujian': 'emr.aliyuncs.com',
            'cn-haidian-cm12-c01': 'emr.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'emr.aliyuncs.com',
            'cn-hangzhou-finance': 'emr.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'emr.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'emr.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'emr.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'emr.aliyuncs.com',
            'cn-hangzhou-test-306': 'emr.aliyuncs.com',
            'cn-hongkong-finance-pop': 'emr.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'emr.aliyuncs.com',
            'cn-qingdao-nebula': 'emr.aliyuncs.com',
            'cn-shanghai-et15-b01': 'emr.aliyuncs.com',
            'cn-shanghai-et2-b01': 'emr.aliyuncs.com',
            'cn-shanghai-inner': 'emr.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'emr.aliyuncs.com',
            'cn-shenzhen-inner': 'emr.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'emr.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'emr.aliyuncs.com',
            'cn-wuhan': 'emr.aliyuncs.com',
            'cn-yushanfang': 'emr.aliyuncs.com',
            'cn-zhangbei': 'emr.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'emr.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'emr.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'emr.aliyuncs.com',
            'eu-west-1-oxs': 'emr.aliyuncs.com',
            'rus-west-1-pop': 'emr.aliyuncs.com'
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

    def create_api_template_with_options(
        self,
        request: emr_20210320_models.CreateApiTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.CreateApiTemplateResponse:
        """
        @param request: CreateApiTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApiTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApiTemplate',
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
            emr_20210320_models.CreateApiTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_template_with_options_async(
        self,
        request: emr_20210320_models.CreateApiTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.CreateApiTemplateResponse:
        """
        @param request: CreateApiTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateApiTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateApiTemplate',
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
            emr_20210320_models.CreateApiTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_template(
        self,
        request: emr_20210320_models.CreateApiTemplateRequest,
    ) -> emr_20210320_models.CreateApiTemplateResponse:
        """
        @param request: CreateApiTemplateRequest
        @return: CreateApiTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_api_template_with_options(request, runtime)

    async def create_api_template_async(
        self,
        request: emr_20210320_models.CreateApiTemplateRequest,
    ) -> emr_20210320_models.CreateApiTemplateResponse:
        """
        @param request: CreateApiTemplateRequest
        @return: CreateApiTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_api_template_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        request: emr_20210320_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.CreateClusterResponse:
        """
        @summary Creates a pay-as-you-go or subscription cluster.
        
        @param request: CreateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
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
        @summary Creates a pay-as-you-go or subscription cluster.
        
        @param request: CreateClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateClusterResponse
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
        """
        @summary Creates a pay-as-you-go or subscription cluster.
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: emr_20210320_models.CreateClusterRequest,
    ) -> emr_20210320_models.CreateClusterResponse:
        """
        @summary Creates a pay-as-you-go or subscription cluster.
        
        @param request: CreateClusterRequest
        @return: CreateClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_node_group_with_options(
        self,
        request: emr_20210320_models.CreateNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.CreateNodeGroupResponse:
        """
        @summary Creates a node group.
        
        @description 创建节点组。
        
        @param request: CreateNodeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNodeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_group):
            query['NodeGroup'] = request.node_group
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNodeGroup',
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
            emr_20210320_models.CreateNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_node_group_with_options_async(
        self,
        request: emr_20210320_models.CreateNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.CreateNodeGroupResponse:
        """
        @summary Creates a node group.
        
        @description 创建节点组。
        
        @param request: CreateNodeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateNodeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_group):
            query['NodeGroup'] = request.node_group
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNodeGroup',
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
            emr_20210320_models.CreateNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_node_group(
        self,
        request: emr_20210320_models.CreateNodeGroupRequest,
    ) -> emr_20210320_models.CreateNodeGroupResponse:
        """
        @summary Creates a node group.
        
        @description 创建节点组。
        
        @param request: CreateNodeGroupRequest
        @return: CreateNodeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_node_group_with_options(request, runtime)

    async def create_node_group_async(
        self,
        request: emr_20210320_models.CreateNodeGroupRequest,
    ) -> emr_20210320_models.CreateNodeGroupResponse:
        """
        @summary Creates a node group.
        
        @description 创建节点组。
        
        @param request: CreateNodeGroupRequest
        @return: CreateNodeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_node_group_with_options_async(request, runtime)

    def create_script_with_options(
        self,
        request: emr_20210320_models.CreateScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.CreateScriptResponse:
        """
        @param request: CreateScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.script_type):
            query['ScriptType'] = request.script_type
        if not UtilClient.is_unset(request.scripts):
            query['Scripts'] = request.scripts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScript',
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
            emr_20210320_models.CreateScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_script_with_options_async(
        self,
        request: emr_20210320_models.CreateScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.CreateScriptResponse:
        """
        @param request: CreateScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.script_type):
            query['ScriptType'] = request.script_type
        if not UtilClient.is_unset(request.scripts):
            query['Scripts'] = request.scripts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateScript',
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
            emr_20210320_models.CreateScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_script(
        self,
        request: emr_20210320_models.CreateScriptRequest,
    ) -> emr_20210320_models.CreateScriptResponse:
        """
        @param request: CreateScriptRequest
        @return: CreateScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_script_with_options(request, runtime)

    async def create_script_async(
        self,
        request: emr_20210320_models.CreateScriptRequest,
    ) -> emr_20210320_models.CreateScriptResponse:
        """
        @param request: CreateScriptRequest
        @return: CreateScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_script_with_options_async(request, runtime)

    def decrease_nodes_with_options(
        self,
        request: emr_20210320_models.DecreaseNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.DecreaseNodesResponse:
        """
        @summary Perform a scale-out operation on the target node group.
        
        @param request: DecreaseNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DecreaseNodesResponse
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
        @summary Perform a scale-out operation on the target node group.
        
        @param request: DecreaseNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DecreaseNodesResponse
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
        """
        @summary Perform a scale-out operation on the target node group.
        
        @param request: DecreaseNodesRequest
        @return: DecreaseNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.decrease_nodes_with_options(request, runtime)

    async def decrease_nodes_async(
        self,
        request: emr_20210320_models.DecreaseNodesRequest,
    ) -> emr_20210320_models.DecreaseNodesResponse:
        """
        @summary Perform a scale-out operation on the target node group.
        
        @param request: DecreaseNodesRequest
        @return: DecreaseNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.decrease_nodes_with_options_async(request, runtime)

    def delete_api_template_with_options(
        self,
        request: emr_20210320_models.DeleteApiTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.DeleteApiTemplateResponse:
        """
        @description 创建集群模板
        
        @param request: DeleteApiTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApiTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApiTemplate',
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
            emr_20210320_models.DeleteApiTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_template_with_options_async(
        self,
        request: emr_20210320_models.DeleteApiTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.DeleteApiTemplateResponse:
        """
        @description 创建集群模板
        
        @param request: DeleteApiTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteApiTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteApiTemplate',
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
            emr_20210320_models.DeleteApiTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_template(
        self,
        request: emr_20210320_models.DeleteApiTemplateRequest,
    ) -> emr_20210320_models.DeleteApiTemplateResponse:
        """
        @description 创建集群模板
        
        @param request: DeleteApiTemplateRequest
        @return: DeleteApiTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_api_template_with_options(request, runtime)

    async def delete_api_template_async(
        self,
        request: emr_20210320_models.DeleteApiTemplateRequest,
    ) -> emr_20210320_models.DeleteApiTemplateResponse:
        """
        @description 创建集群模板
        
        @param request: DeleteApiTemplateRequest
        @return: DeleteApiTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_api_template_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: emr_20210320_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.DeleteClusterResponse:
        """
        @param request: DeleteClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
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
        @param request: DeleteClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteClusterResponse
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
        """
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: emr_20210320_models.DeleteClusterRequest,
    ) -> emr_20210320_models.DeleteClusterResponse:
        """
        @param request: DeleteClusterRequest
        @return: DeleteClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def delete_script_with_options(
        self,
        request: emr_20210320_models.DeleteScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.DeleteScriptResponse:
        """
        @param request: DeleteScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.script_type):
            query['ScriptType'] = request.script_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScript',
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
            emr_20210320_models.DeleteScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_script_with_options_async(
        self,
        request: emr_20210320_models.DeleteScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.DeleteScriptResponse:
        """
        @param request: DeleteScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteScriptResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.script_type):
            query['ScriptType'] = request.script_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScript',
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
            emr_20210320_models.DeleteScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_script(
        self,
        request: emr_20210320_models.DeleteScriptRequest,
    ) -> emr_20210320_models.DeleteScriptResponse:
        """
        @param request: DeleteScriptRequest
        @return: DeleteScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_script_with_options(request, runtime)

    async def delete_script_async(
        self,
        request: emr_20210320_models.DeleteScriptRequest,
    ) -> emr_20210320_models.DeleteScriptResponse:
        """
        @param request: DeleteScriptRequest
        @return: DeleteScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_script_with_options_async(request, runtime)

    def get_api_template_with_options(
        self,
        request: emr_20210320_models.GetApiTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetApiTemplateResponse:
        """
        @summary 获取API模板详情
        
        @param request: GetApiTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApiTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApiTemplate',
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
            emr_20210320_models.GetApiTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_api_template_with_options_async(
        self,
        request: emr_20210320_models.GetApiTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetApiTemplateResponse:
        """
        @summary 获取API模板详情
        
        @param request: GetApiTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApiTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApiTemplate',
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
            emr_20210320_models.GetApiTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_api_template(
        self,
        request: emr_20210320_models.GetApiTemplateRequest,
    ) -> emr_20210320_models.GetApiTemplateResponse:
        """
        @summary 获取API模板详情
        
        @param request: GetApiTemplateRequest
        @return: GetApiTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_api_template_with_options(request, runtime)

    async def get_api_template_async(
        self,
        request: emr_20210320_models.GetApiTemplateRequest,
    ) -> emr_20210320_models.GetApiTemplateResponse:
        """
        @summary 获取API模板详情
        
        @param request: GetApiTemplateRequest
        @return: GetApiTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_api_template_with_options_async(request, runtime)

    def get_application_with_options(
        self,
        request: emr_20210320_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetApplicationResponse:
        """
        @description 查询应用详情。
        
        @param request: GetApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
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
            emr_20210320_models.GetApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_with_options_async(
        self,
        request: emr_20210320_models.GetApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetApplicationResponse:
        """
        @description 查询应用详情。
        
        @param request: GetApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetApplication',
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
            emr_20210320_models.GetApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application(
        self,
        request: emr_20210320_models.GetApplicationRequest,
    ) -> emr_20210320_models.GetApplicationResponse:
        """
        @description 查询应用详情。
        
        @param request: GetApplicationRequest
        @return: GetApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_application_with_options(request, runtime)

    async def get_application_async(
        self,
        request: emr_20210320_models.GetApplicationRequest,
    ) -> emr_20210320_models.GetApplicationResponse:
        """
        @description 查询应用详情。
        
        @param request: GetApplicationRequest
        @return: GetApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_application_with_options_async(request, runtime)

    def get_auto_scaling_activity_with_options(
        self,
        request: emr_20210320_models.GetAutoScalingActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetAutoScalingActivityResponse:
        """
        @description 获取弹性伸缩活动详情。
        
        @param request: GetAutoScalingActivityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoScalingActivityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoScalingActivity',
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
            emr_20210320_models.GetAutoScalingActivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_scaling_activity_with_options_async(
        self,
        request: emr_20210320_models.GetAutoScalingActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetAutoScalingActivityResponse:
        """
        @description 获取弹性伸缩活动详情。
        
        @param request: GetAutoScalingActivityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoScalingActivityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoScalingActivity',
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
            emr_20210320_models.GetAutoScalingActivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_scaling_activity(
        self,
        request: emr_20210320_models.GetAutoScalingActivityRequest,
    ) -> emr_20210320_models.GetAutoScalingActivityResponse:
        """
        @description 获取弹性伸缩活动详情。
        
        @param request: GetAutoScalingActivityRequest
        @return: GetAutoScalingActivityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_auto_scaling_activity_with_options(request, runtime)

    async def get_auto_scaling_activity_async(
        self,
        request: emr_20210320_models.GetAutoScalingActivityRequest,
    ) -> emr_20210320_models.GetAutoScalingActivityResponse:
        """
        @description 获取弹性伸缩活动详情。
        
        @param request: GetAutoScalingActivityRequest
        @return: GetAutoScalingActivityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_scaling_activity_with_options_async(request, runtime)

    def get_auto_scaling_policy_with_options(
        self,
        request: emr_20210320_models.GetAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetAutoScalingPolicyResponse:
        """
        @param request: GetAutoScalingPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoScalingPolicyResponse
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
            action='GetAutoScalingPolicy',
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
            emr_20210320_models.GetAutoScalingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_scaling_policy_with_options_async(
        self,
        request: emr_20210320_models.GetAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetAutoScalingPolicyResponse:
        """
        @param request: GetAutoScalingPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetAutoScalingPolicyResponse
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
            action='GetAutoScalingPolicy',
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
            emr_20210320_models.GetAutoScalingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_scaling_policy(
        self,
        request: emr_20210320_models.GetAutoScalingPolicyRequest,
    ) -> emr_20210320_models.GetAutoScalingPolicyResponse:
        """
        @param request: GetAutoScalingPolicyRequest
        @return: GetAutoScalingPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_auto_scaling_policy_with_options(request, runtime)

    async def get_auto_scaling_policy_async(
        self,
        request: emr_20210320_models.GetAutoScalingPolicyRequest,
    ) -> emr_20210320_models.GetAutoScalingPolicyResponse:
        """
        @param request: GetAutoScalingPolicyRequest
        @return: GetAutoScalingPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_scaling_policy_with_options_async(request, runtime)

    def get_cluster_with_options(
        self,
        request: emr_20210320_models.GetClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetClusterResponse:
        """
        @summary Obtains the details of a cluster.
        
        @param request: GetClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterResponse
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
        @summary Obtains the details of a cluster.
        
        @param request: GetClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetClusterResponse
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
        """
        @summary Obtains the details of a cluster.
        
        @param request: GetClusterRequest
        @return: GetClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_with_options(request, runtime)

    async def get_cluster_async(
        self,
        request: emr_20210320_models.GetClusterRequest,
    ) -> emr_20210320_models.GetClusterResponse:
        """
        @summary Obtains the details of a cluster.
        
        @param request: GetClusterRequest
        @return: GetClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_with_options_async(request, runtime)

    def get_doctor_application_with_options(
        self,
        request: emr_20210320_models.GetDoctorApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorApplicationResponse:
        """
        @summary Obtains job analysis information on E-MapReduce (EMR) Doctor.
        
        @description get one doctor analysis app
        
        @param request: GetDoctorApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorApplication',
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
            emr_20210320_models.GetDoctorApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_application_with_options_async(
        self,
        request: emr_20210320_models.GetDoctorApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorApplicationResponse:
        """
        @summary Obtains job analysis information on E-MapReduce (EMR) Doctor.
        
        @description get one doctor analysis app
        
        @param request: GetDoctorApplicationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorApplication',
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
            emr_20210320_models.GetDoctorApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_application(
        self,
        request: emr_20210320_models.GetDoctorApplicationRequest,
    ) -> emr_20210320_models.GetDoctorApplicationResponse:
        """
        @summary Obtains job analysis information on E-MapReduce (EMR) Doctor.
        
        @description get one doctor analysis app
        
        @param request: GetDoctorApplicationRequest
        @return: GetDoctorApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_application_with_options(request, runtime)

    async def get_doctor_application_async(
        self,
        request: emr_20210320_models.GetDoctorApplicationRequest,
    ) -> emr_20210320_models.GetDoctorApplicationResponse:
        """
        @summary Obtains job analysis information on E-MapReduce (EMR) Doctor.
        
        @description get one doctor analysis app
        
        @param request: GetDoctorApplicationRequest
        @return: GetDoctorApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doctor_application_with_options_async(request, runtime)

    def get_doctor_compute_summary_with_options(
        self,
        request: emr_20210320_models.GetDoctorComputeSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorComputeSummaryResponse:
        """
        @summary Obtains the information about resource usage in a cluster on E-MapReduce (EMR) Doctor.
        
        @description get one specific luster engine queue by <type, name>
        
        @param request: GetDoctorComputeSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorComputeSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_info):
            query['ComponentInfo'] = request.component_info
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorComputeSummary',
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
            emr_20210320_models.GetDoctorComputeSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_compute_summary_with_options_async(
        self,
        request: emr_20210320_models.GetDoctorComputeSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorComputeSummaryResponse:
        """
        @summary Obtains the information about resource usage in a cluster on E-MapReduce (EMR) Doctor.
        
        @description get one specific luster engine queue by <type, name>
        
        @param request: GetDoctorComputeSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorComputeSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_info):
            query['ComponentInfo'] = request.component_info
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorComputeSummary',
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
            emr_20210320_models.GetDoctorComputeSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_compute_summary(
        self,
        request: emr_20210320_models.GetDoctorComputeSummaryRequest,
    ) -> emr_20210320_models.GetDoctorComputeSummaryResponse:
        """
        @summary Obtains the information about resource usage in a cluster on E-MapReduce (EMR) Doctor.
        
        @description get one specific luster engine queue by <type, name>
        
        @param request: GetDoctorComputeSummaryRequest
        @return: GetDoctorComputeSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_compute_summary_with_options(request, runtime)

    async def get_doctor_compute_summary_async(
        self,
        request: emr_20210320_models.GetDoctorComputeSummaryRequest,
    ) -> emr_20210320_models.GetDoctorComputeSummaryResponse:
        """
        @summary Obtains the information about resource usage in a cluster on E-MapReduce (EMR) Doctor.
        
        @description get one specific luster engine queue by <type, name>
        
        @param request: GetDoctorComputeSummaryRequest
        @return: GetDoctorComputeSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doctor_compute_summary_with_options_async(request, runtime)

    def get_doctor_hbase_cluster_with_options(
        self,
        request: emr_20210320_models.GetDoctorHBaseClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHBaseClusterResponse:
        """
        @summary Obtains the metrics of an HBase cluster.
        
        @description get Doctor HBaseCluster
        
        @param request: GetDoctorHBaseClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHBaseClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHBaseCluster',
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
            emr_20210320_models.GetDoctorHBaseClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hbase_cluster_with_options_async(
        self,
        request: emr_20210320_models.GetDoctorHBaseClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHBaseClusterResponse:
        """
        @summary Obtains the metrics of an HBase cluster.
        
        @description get Doctor HBaseCluster
        
        @param request: GetDoctorHBaseClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHBaseClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHBaseCluster',
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
            emr_20210320_models.GetDoctorHBaseClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hbase_cluster(
        self,
        request: emr_20210320_models.GetDoctorHBaseClusterRequest,
    ) -> emr_20210320_models.GetDoctorHBaseClusterResponse:
        """
        @summary Obtains the metrics of an HBase cluster.
        
        @description get Doctor HBaseCluster
        
        @param request: GetDoctorHBaseClusterRequest
        @return: GetDoctorHBaseClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hbase_cluster_with_options(request, runtime)

    async def get_doctor_hbase_cluster_async(
        self,
        request: emr_20210320_models.GetDoctorHBaseClusterRequest,
    ) -> emr_20210320_models.GetDoctorHBaseClusterResponse:
        """
        @summary Obtains the metrics of an HBase cluster.
        
        @description get Doctor HBaseCluster
        
        @param request: GetDoctorHBaseClusterRequest
        @return: GetDoctorHBaseClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doctor_hbase_cluster_with_options_async(request, runtime)

    def get_doctor_hbase_region_with_options(
        self,
        request: emr_20210320_models.GetDoctorHBaseRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHBaseRegionResponse:
        """
        @description list Doctor HBaseRegions
        
        @param request: GetDoctorHBaseRegionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHBaseRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.hbase_region_id):
            query['HbaseRegionId'] = request.hbase_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHBaseRegion',
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
            emr_20210320_models.GetDoctorHBaseRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hbase_region_with_options_async(
        self,
        request: emr_20210320_models.GetDoctorHBaseRegionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHBaseRegionResponse:
        """
        @description list Doctor HBaseRegions
        
        @param request: GetDoctorHBaseRegionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHBaseRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.hbase_region_id):
            query['HbaseRegionId'] = request.hbase_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHBaseRegion',
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
            emr_20210320_models.GetDoctorHBaseRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hbase_region(
        self,
        request: emr_20210320_models.GetDoctorHBaseRegionRequest,
    ) -> emr_20210320_models.GetDoctorHBaseRegionResponse:
        """
        @description list Doctor HBaseRegions
        
        @param request: GetDoctorHBaseRegionRequest
        @return: GetDoctorHBaseRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hbase_region_with_options(request, runtime)

    async def get_doctor_hbase_region_async(
        self,
        request: emr_20210320_models.GetDoctorHBaseRegionRequest,
    ) -> emr_20210320_models.GetDoctorHBaseRegionResponse:
        """
        @description list Doctor HBaseRegions
        
        @param request: GetDoctorHBaseRegionRequest
        @return: GetDoctorHBaseRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doctor_hbase_region_with_options_async(request, runtime)

    def get_doctor_hbase_region_server_with_options(
        self,
        request: emr_20210320_models.GetDoctorHBaseRegionServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHBaseRegionServerResponse:
        """
        @summary Obtains the information about an HBase region server.
        
        @description get Doctor HBaseRegionServer
        
        @param request: GetDoctorHBaseRegionServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHBaseRegionServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_server_host):
            query['RegionServerHost'] = request.region_server_host
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHBaseRegionServer',
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
            emr_20210320_models.GetDoctorHBaseRegionServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hbase_region_server_with_options_async(
        self,
        request: emr_20210320_models.GetDoctorHBaseRegionServerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHBaseRegionServerResponse:
        """
        @summary Obtains the information about an HBase region server.
        
        @description get Doctor HBaseRegionServer
        
        @param request: GetDoctorHBaseRegionServerRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHBaseRegionServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_server_host):
            query['RegionServerHost'] = request.region_server_host
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHBaseRegionServer',
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
            emr_20210320_models.GetDoctorHBaseRegionServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hbase_region_server(
        self,
        request: emr_20210320_models.GetDoctorHBaseRegionServerRequest,
    ) -> emr_20210320_models.GetDoctorHBaseRegionServerResponse:
        """
        @summary Obtains the information about an HBase region server.
        
        @description get Doctor HBaseRegionServer
        
        @param request: GetDoctorHBaseRegionServerRequest
        @return: GetDoctorHBaseRegionServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hbase_region_server_with_options(request, runtime)

    async def get_doctor_hbase_region_server_async(
        self,
        request: emr_20210320_models.GetDoctorHBaseRegionServerRequest,
    ) -> emr_20210320_models.GetDoctorHBaseRegionServerResponse:
        """
        @summary Obtains the information about an HBase region server.
        
        @description get Doctor HBaseRegionServer
        
        @param request: GetDoctorHBaseRegionServerRequest
        @return: GetDoctorHBaseRegionServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doctor_hbase_region_server_with_options_async(request, runtime)

    def get_doctor_hbase_table_with_options(
        self,
        request: emr_20210320_models.GetDoctorHBaseTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHBaseTableResponse:
        """
        @description get Doctor HBaseTable
        
        @param request: GetDoctorHBaseTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHBaseTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHBaseTable',
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
            emr_20210320_models.GetDoctorHBaseTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hbase_table_with_options_async(
        self,
        request: emr_20210320_models.GetDoctorHBaseTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHBaseTableResponse:
        """
        @description get Doctor HBaseTable
        
        @param request: GetDoctorHBaseTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHBaseTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHBaseTable',
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
            emr_20210320_models.GetDoctorHBaseTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hbase_table(
        self,
        request: emr_20210320_models.GetDoctorHBaseTableRequest,
    ) -> emr_20210320_models.GetDoctorHBaseTableResponse:
        """
        @description get Doctor HBaseTable
        
        @param request: GetDoctorHBaseTableRequest
        @return: GetDoctorHBaseTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hbase_table_with_options(request, runtime)

    async def get_doctor_hbase_table_async(
        self,
        request: emr_20210320_models.GetDoctorHBaseTableRequest,
    ) -> emr_20210320_models.GetDoctorHBaseTableResponse:
        """
        @description get Doctor HBaseTable
        
        @param request: GetDoctorHBaseTableRequest
        @return: GetDoctorHBaseTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doctor_hbase_table_with_options_async(request, runtime)

    def get_doctor_hdfscluster_with_options(
        self,
        request: emr_20210320_models.GetDoctorHDFSClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHDFSClusterResponse:
        """
        @summary Obtains the analysis results of the Hadoop Distributed File System (HDFS) storage resources of a cluster on E-MapReduce (EMR) Doctor.
        
        @description list Doctor HBaseTableRegions
        
        @param request: GetDoctorHDFSClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHDFSClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHDFSCluster',
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
            emr_20210320_models.GetDoctorHDFSClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hdfscluster_with_options_async(
        self,
        request: emr_20210320_models.GetDoctorHDFSClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHDFSClusterResponse:
        """
        @summary Obtains the analysis results of the Hadoop Distributed File System (HDFS) storage resources of a cluster on E-MapReduce (EMR) Doctor.
        
        @description list Doctor HBaseTableRegions
        
        @param request: GetDoctorHDFSClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHDFSClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHDFSCluster',
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
            emr_20210320_models.GetDoctorHDFSClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hdfscluster(
        self,
        request: emr_20210320_models.GetDoctorHDFSClusterRequest,
    ) -> emr_20210320_models.GetDoctorHDFSClusterResponse:
        """
        @summary Obtains the analysis results of the Hadoop Distributed File System (HDFS) storage resources of a cluster on E-MapReduce (EMR) Doctor.
        
        @description list Doctor HBaseTableRegions
        
        @param request: GetDoctorHDFSClusterRequest
        @return: GetDoctorHDFSClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hdfscluster_with_options(request, runtime)

    async def get_doctor_hdfscluster_async(
        self,
        request: emr_20210320_models.GetDoctorHDFSClusterRequest,
    ) -> emr_20210320_models.GetDoctorHDFSClusterResponse:
        """
        @summary Obtains the analysis results of the Hadoop Distributed File System (HDFS) storage resources of a cluster on E-MapReduce (EMR) Doctor.
        
        @description list Doctor HBaseTableRegions
        
        @param request: GetDoctorHDFSClusterRequest
        @return: GetDoctorHDFSClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doctor_hdfscluster_with_options_async(request, runtime)

    def get_doctor_hdfsdirectory_with_options(
        self,
        request: emr_20210320_models.GetDoctorHDFSDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHDFSDirectoryResponse:
        """
        @summary Obtains the analysis results of a specific Hadoop Distributed File System (HDFS) directory of a cluster. The depth of the directory is not greater than five.
        
        @description get Doctor HDFSNode
        
        @param request: GetDoctorHDFSDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHDFSDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.dir_path):
            query['DirPath'] = request.dir_path
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHDFSDirectory',
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
            emr_20210320_models.GetDoctorHDFSDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hdfsdirectory_with_options_async(
        self,
        request: emr_20210320_models.GetDoctorHDFSDirectoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHDFSDirectoryResponse:
        """
        @summary Obtains the analysis results of a specific Hadoop Distributed File System (HDFS) directory of a cluster. The depth of the directory is not greater than five.
        
        @description get Doctor HDFSNode
        
        @param request: GetDoctorHDFSDirectoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHDFSDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.dir_path):
            query['DirPath'] = request.dir_path
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHDFSDirectory',
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
            emr_20210320_models.GetDoctorHDFSDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hdfsdirectory(
        self,
        request: emr_20210320_models.GetDoctorHDFSDirectoryRequest,
    ) -> emr_20210320_models.GetDoctorHDFSDirectoryResponse:
        """
        @summary Obtains the analysis results of a specific Hadoop Distributed File System (HDFS) directory of a cluster. The depth of the directory is not greater than five.
        
        @description get Doctor HDFSNode
        
        @param request: GetDoctorHDFSDirectoryRequest
        @return: GetDoctorHDFSDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hdfsdirectory_with_options(request, runtime)

    async def get_doctor_hdfsdirectory_async(
        self,
        request: emr_20210320_models.GetDoctorHDFSDirectoryRequest,
    ) -> emr_20210320_models.GetDoctorHDFSDirectoryResponse:
        """
        @summary Obtains the analysis results of a specific Hadoop Distributed File System (HDFS) directory of a cluster. The depth of the directory is not greater than five.
        
        @description get Doctor HDFSNode
        
        @param request: GetDoctorHDFSDirectoryRequest
        @return: GetDoctorHDFSDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doctor_hdfsdirectory_with_options_async(request, runtime)

    def get_doctor_hdfsugiwith_options(
        self,
        request: emr_20210320_models.GetDoctorHDFSUGIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHDFSUGIResponse:
        """
        @summary Obtains the analysis results of Hadoop Distributed File System (HDFS) storage resources for a specific owner or group on E-MapReduce (EMR) Doctor.
        
        @description get Doctor HDFS UGI
        
        @param request: GetDoctorHDFSUGIRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHDFSUGIResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHDFSUGI',
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
            emr_20210320_models.GetDoctorHDFSUGIResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hdfsugiwith_options_async(
        self,
        request: emr_20210320_models.GetDoctorHDFSUGIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHDFSUGIResponse:
        """
        @summary Obtains the analysis results of Hadoop Distributed File System (HDFS) storage resources for a specific owner or group on E-MapReduce (EMR) Doctor.
        
        @description get Doctor HDFS UGI
        
        @param request: GetDoctorHDFSUGIRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHDFSUGIResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHDFSUGI',
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
            emr_20210320_models.GetDoctorHDFSUGIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hdfsugi(
        self,
        request: emr_20210320_models.GetDoctorHDFSUGIRequest,
    ) -> emr_20210320_models.GetDoctorHDFSUGIResponse:
        """
        @summary Obtains the analysis results of Hadoop Distributed File System (HDFS) storage resources for a specific owner or group on E-MapReduce (EMR) Doctor.
        
        @description get Doctor HDFS UGI
        
        @param request: GetDoctorHDFSUGIRequest
        @return: GetDoctorHDFSUGIResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hdfsugiwith_options(request, runtime)

    async def get_doctor_hdfsugi_async(
        self,
        request: emr_20210320_models.GetDoctorHDFSUGIRequest,
    ) -> emr_20210320_models.GetDoctorHDFSUGIResponse:
        """
        @summary Obtains the analysis results of Hadoop Distributed File System (HDFS) storage resources for a specific owner or group on E-MapReduce (EMR) Doctor.
        
        @description get Doctor HDFS UGI
        
        @param request: GetDoctorHDFSUGIRequest
        @return: GetDoctorHDFSUGIResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doctor_hdfsugiwith_options_async(request, runtime)

    def get_doctor_hive_cluster_with_options(
        self,
        request: emr_20210320_models.GetDoctorHiveClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHiveClusterResponse:
        """
        @summary Obtains the analysis results of a Hive cluster.
        
        @description list Doctor Hive Cluster
        
        @param request: GetDoctorHiveClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHiveClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHiveCluster',
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
            emr_20210320_models.GetDoctorHiveClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hive_cluster_with_options_async(
        self,
        request: emr_20210320_models.GetDoctorHiveClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHiveClusterResponse:
        """
        @summary Obtains the analysis results of a Hive cluster.
        
        @description list Doctor Hive Cluster
        
        @param request: GetDoctorHiveClusterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHiveClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHiveCluster',
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
            emr_20210320_models.GetDoctorHiveClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hive_cluster(
        self,
        request: emr_20210320_models.GetDoctorHiveClusterRequest,
    ) -> emr_20210320_models.GetDoctorHiveClusterResponse:
        """
        @summary Obtains the analysis results of a Hive cluster.
        
        @description list Doctor Hive Cluster
        
        @param request: GetDoctorHiveClusterRequest
        @return: GetDoctorHiveClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hive_cluster_with_options(request, runtime)

    async def get_doctor_hive_cluster_async(
        self,
        request: emr_20210320_models.GetDoctorHiveClusterRequest,
    ) -> emr_20210320_models.GetDoctorHiveClusterResponse:
        """
        @summary Obtains the analysis results of a Hive cluster.
        
        @description list Doctor Hive Cluster
        
        @param request: GetDoctorHiveClusterRequest
        @return: GetDoctorHiveClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doctor_hive_cluster_with_options_async(request, runtime)

    def get_doctor_hive_database_with_options(
        self,
        request: emr_20210320_models.GetDoctorHiveDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHiveDatabaseResponse:
        """
        @summary Obtains the analysis results of a Hive database.
        
        @description get Doctor Hive Database
        
        @param request: GetDoctorHiveDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHiveDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHiveDatabase',
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
            emr_20210320_models.GetDoctorHiveDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hive_database_with_options_async(
        self,
        request: emr_20210320_models.GetDoctorHiveDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHiveDatabaseResponse:
        """
        @summary Obtains the analysis results of a Hive database.
        
        @description get Doctor Hive Database
        
        @param request: GetDoctorHiveDatabaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHiveDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHiveDatabase',
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
            emr_20210320_models.GetDoctorHiveDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hive_database(
        self,
        request: emr_20210320_models.GetDoctorHiveDatabaseRequest,
    ) -> emr_20210320_models.GetDoctorHiveDatabaseResponse:
        """
        @summary Obtains the analysis results of a Hive database.
        
        @description get Doctor Hive Database
        
        @param request: GetDoctorHiveDatabaseRequest
        @return: GetDoctorHiveDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hive_database_with_options(request, runtime)

    async def get_doctor_hive_database_async(
        self,
        request: emr_20210320_models.GetDoctorHiveDatabaseRequest,
    ) -> emr_20210320_models.GetDoctorHiveDatabaseResponse:
        """
        @summary Obtains the analysis results of a Hive database.
        
        @description get Doctor Hive Database
        
        @param request: GetDoctorHiveDatabaseRequest
        @return: GetDoctorHiveDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doctor_hive_database_with_options_async(request, runtime)

    def get_doctor_hive_table_with_options(
        self,
        request: emr_20210320_models.GetDoctorHiveTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHiveTableResponse:
        """
        @summary Obtains the analysis results of a specific Hive table in a cluster on E-MapReduce (EMR) Doctor.
        
        @description get Doctor Hive Table
        
        @param request: GetDoctorHiveTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHiveTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHiveTable',
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
            emr_20210320_models.GetDoctorHiveTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hive_table_with_options_async(
        self,
        request: emr_20210320_models.GetDoctorHiveTableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorHiveTableResponse:
        """
        @summary Obtains the analysis results of a specific Hive table in a cluster on E-MapReduce (EMR) Doctor.
        
        @description get Doctor Hive Table
        
        @param request: GetDoctorHiveTableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorHiveTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHiveTable',
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
            emr_20210320_models.GetDoctorHiveTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hive_table(
        self,
        request: emr_20210320_models.GetDoctorHiveTableRequest,
    ) -> emr_20210320_models.GetDoctorHiveTableResponse:
        """
        @summary Obtains the analysis results of a specific Hive table in a cluster on E-MapReduce (EMR) Doctor.
        
        @description get Doctor Hive Table
        
        @param request: GetDoctorHiveTableRequest
        @return: GetDoctorHiveTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hive_table_with_options(request, runtime)

    async def get_doctor_hive_table_async(
        self,
        request: emr_20210320_models.GetDoctorHiveTableRequest,
    ) -> emr_20210320_models.GetDoctorHiveTableResponse:
        """
        @summary Obtains the analysis results of a specific Hive table in a cluster on E-MapReduce (EMR) Doctor.
        
        @description get Doctor Hive Table
        
        @param request: GetDoctorHiveTableRequest
        @return: GetDoctorHiveTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doctor_hive_table_with_options_async(request, runtime)

    def get_doctor_job_with_options(
        self,
        request: emr_20210320_models.GetDoctorJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorJobResponse:
        """
        @summary Obtains the basic running information about a job on E-MapReduce (EMR) Doctor.
        
        @description Get realtime job by yarn
        
        @param request: GetDoctorJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorJob',
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
            emr_20210320_models.GetDoctorJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_job_with_options_async(
        self,
        request: emr_20210320_models.GetDoctorJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorJobResponse:
        """
        @summary Obtains the basic running information about a job on E-MapReduce (EMR) Doctor.
        
        @description Get realtime job by yarn
        
        @param request: GetDoctorJobRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorJob',
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
            emr_20210320_models.GetDoctorJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_job(
        self,
        request: emr_20210320_models.GetDoctorJobRequest,
    ) -> emr_20210320_models.GetDoctorJobResponse:
        """
        @summary Obtains the basic running information about a job on E-MapReduce (EMR) Doctor.
        
        @description Get realtime job by yarn
        
        @param request: GetDoctorJobRequest
        @return: GetDoctorJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_job_with_options(request, runtime)

    async def get_doctor_job_async(
        self,
        request: emr_20210320_models.GetDoctorJobRequest,
    ) -> emr_20210320_models.GetDoctorJobResponse:
        """
        @summary Obtains the basic running information about a job on E-MapReduce (EMR) Doctor.
        
        @description Get realtime job by yarn
        
        @param request: GetDoctorJobRequest
        @return: GetDoctorJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doctor_job_with_options_async(request, runtime)

    def get_doctor_report_component_summary_with_options(
        self,
        request: emr_20210320_models.GetDoctorReportComponentSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorReportComponentSummaryResponse:
        """
        @description get specify component's report analysis by emr doctor
        
        @param request: GetDoctorReportComponentSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorReportComponentSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_type):
            query['ComponentType'] = request.component_type
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorReportComponentSummary',
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
            emr_20210320_models.GetDoctorReportComponentSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_report_component_summary_with_options_async(
        self,
        request: emr_20210320_models.GetDoctorReportComponentSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetDoctorReportComponentSummaryResponse:
        """
        @description get specify component's report analysis by emr doctor
        
        @param request: GetDoctorReportComponentSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDoctorReportComponentSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_type):
            query['ComponentType'] = request.component_type
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorReportComponentSummary',
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
            emr_20210320_models.GetDoctorReportComponentSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_report_component_summary(
        self,
        request: emr_20210320_models.GetDoctorReportComponentSummaryRequest,
    ) -> emr_20210320_models.GetDoctorReportComponentSummaryResponse:
        """
        @description get specify component's report analysis by emr doctor
        
        @param request: GetDoctorReportComponentSummaryRequest
        @return: GetDoctorReportComponentSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_report_component_summary_with_options(request, runtime)

    async def get_doctor_report_component_summary_async(
        self,
        request: emr_20210320_models.GetDoctorReportComponentSummaryRequest,
    ) -> emr_20210320_models.GetDoctorReportComponentSummaryResponse:
        """
        @description get specify component's report analysis by emr doctor
        
        @param request: GetDoctorReportComponentSummaryRequest
        @return: GetDoctorReportComponentSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_doctor_report_component_summary_with_options_async(request, runtime)

    def get_node_group_with_options(
        self,
        request: emr_20210320_models.GetNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetNodeGroupResponse:
        """
        @summary You can call this operation to obtain the details of a node group.
        
        @description 获取节点组详情。
        
        @param request: GetNodeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNodeGroupResponse
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
        @summary You can call this operation to obtain the details of a node group.
        
        @description 获取节点组详情。
        
        @param request: GetNodeGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetNodeGroupResponse
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
        """
        @summary You can call this operation to obtain the details of a node group.
        
        @description 获取节点组详情。
        
        @param request: GetNodeGroupRequest
        @return: GetNodeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_node_group_with_options(request, runtime)

    async def get_node_group_async(
        self,
        request: emr_20210320_models.GetNodeGroupRequest,
    ) -> emr_20210320_models.GetNodeGroupResponse:
        """
        @summary You can call this operation to obtain the details of a node group.
        
        @description 获取节点组详情。
        
        @param request: GetNodeGroupRequest
        @return: GetNodeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_node_group_with_options_async(request, runtime)

    def get_operation_with_options(
        self,
        request: emr_20210320_models.GetOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.GetOperationResponse:
        """
        @summary Gets the details of an asynchronous operation.
        
        @param request: GetOperationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOperationResponse
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
        @summary Gets the details of an asynchronous operation.
        
        @param request: GetOperationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetOperationResponse
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
        """
        @summary Gets the details of an asynchronous operation.
        
        @param request: GetOperationRequest
        @return: GetOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_operation_with_options(request, runtime)

    async def get_operation_async(
        self,
        request: emr_20210320_models.GetOperationRequest,
    ) -> emr_20210320_models.GetOperationResponse:
        """
        @summary Gets the details of an asynchronous operation.
        
        @param request: GetOperationRequest
        @return: GetOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_operation_with_options_async(request, runtime)

    def increase_nodes_with_options(
        self,
        request: emr_20210320_models.IncreaseNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.IncreaseNodesResponse:
        """
        @summary Scale out the node group.
        
        @param request: IncreaseNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IncreaseNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_configs):
            query['ApplicationConfigs'] = request.application_configs
        if not UtilClient.is_unset(request.auto_pay_order):
            query['AutoPayOrder'] = request.auto_pay_order
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.increase_node_count):
            query['IncreaseNodeCount'] = request.increase_node_count
        if not UtilClient.is_unset(request.min_increase_node_count):
            query['MinIncreaseNodeCount'] = request.min_increase_node_count
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
        """
        @summary Scale out the node group.
        
        @param request: IncreaseNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: IncreaseNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_configs):
            query['ApplicationConfigs'] = request.application_configs
        if not UtilClient.is_unset(request.auto_pay_order):
            query['AutoPayOrder'] = request.auto_pay_order
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.increase_node_count):
            query['IncreaseNodeCount'] = request.increase_node_count
        if not UtilClient.is_unset(request.min_increase_node_count):
            query['MinIncreaseNodeCount'] = request.min_increase_node_count
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
        """
        @summary Scale out the node group.
        
        @param request: IncreaseNodesRequest
        @return: IncreaseNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.increase_nodes_with_options(request, runtime)

    async def increase_nodes_async(
        self,
        request: emr_20210320_models.IncreaseNodesRequest,
    ) -> emr_20210320_models.IncreaseNodesResponse:
        """
        @summary Scale out the node group.
        
        @param request: IncreaseNodesRequest
        @return: IncreaseNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.increase_nodes_with_options_async(request, runtime)

    def join_resource_group_with_options(
        self,
        request: emr_20210320_models.JoinResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.JoinResourceGroupResponse:
        """
        @summary Add an EMR resource to the target resource group. A resource can belong to only one resource group.
        
        @param request: JoinResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: JoinResourceGroupResponse
        """
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
        """
        @summary Add an EMR resource to the target resource group. A resource can belong to only one resource group.
        
        @param request: JoinResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: JoinResourceGroupResponse
        """
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
        """
        @summary Add an EMR resource to the target resource group. A resource can belong to only one resource group.
        
        @param request: JoinResourceGroupRequest
        @return: JoinResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.join_resource_group_with_options(request, runtime)

    async def join_resource_group_async(
        self,
        request: emr_20210320_models.JoinResourceGroupRequest,
    ) -> emr_20210320_models.JoinResourceGroupResponse:
        """
        @summary Add an EMR resource to the target resource group. A resource can belong to only one resource group.
        
        @param request: JoinResourceGroupRequest
        @return: JoinResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.join_resource_group_with_options_async(request, runtime)

    def list_api_templates_with_options(
        self,
        request: emr_20210320_models.ListApiTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListApiTemplatesResponse:
        """
        @summary 查询API模板
        
        @param request: ListApiTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApiTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_ids):
            query['TemplateIds'] = request.template_ids
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApiTemplates',
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
            emr_20210320_models.ListApiTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_templates_with_options_async(
        self,
        request: emr_20210320_models.ListApiTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListApiTemplatesResponse:
        """
        @summary 查询API模板
        
        @param request: ListApiTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApiTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_ids):
            query['TemplateIds'] = request.template_ids
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApiTemplates',
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
            emr_20210320_models.ListApiTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_templates(
        self,
        request: emr_20210320_models.ListApiTemplatesRequest,
    ) -> emr_20210320_models.ListApiTemplatesResponse:
        """
        @summary 查询API模板
        
        @param request: ListApiTemplatesRequest
        @return: ListApiTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_api_templates_with_options(request, runtime)

    async def list_api_templates_async(
        self,
        request: emr_20210320_models.ListApiTemplatesRequest,
    ) -> emr_20210320_models.ListApiTemplatesResponse:
        """
        @summary 查询API模板
        
        @param request: ListApiTemplatesRequest
        @return: ListApiTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_api_templates_with_options_async(request, runtime)

    def list_application_configs_with_options(
        self,
        request: emr_20210320_models.ListApplicationConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListApplicationConfigsResponse:
        """
        @description 查询应用配置。
        
        @param request: ListApplicationConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.config_file_name):
            query['ConfigFileName'] = request.config_file_name
        if not UtilClient.is_unset(request.config_item_key):
            query['ConfigItemKey'] = request.config_item_key
        if not UtilClient.is_unset(request.config_item_value):
            query['ConfigItemValue'] = request.config_item_value
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationConfigs',
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
            emr_20210320_models.ListApplicationConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_configs_with_options_async(
        self,
        request: emr_20210320_models.ListApplicationConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListApplicationConfigsResponse:
        """
        @description 查询应用配置。
        
        @param request: ListApplicationConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.config_file_name):
            query['ConfigFileName'] = request.config_file_name
        if not UtilClient.is_unset(request.config_item_key):
            query['ConfigItemKey'] = request.config_item_key
        if not UtilClient.is_unset(request.config_item_value):
            query['ConfigItemValue'] = request.config_item_value
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationConfigs',
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
            emr_20210320_models.ListApplicationConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_configs(
        self,
        request: emr_20210320_models.ListApplicationConfigsRequest,
    ) -> emr_20210320_models.ListApplicationConfigsResponse:
        """
        @description 查询应用配置。
        
        @param request: ListApplicationConfigsRequest
        @return: ListApplicationConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_application_configs_with_options(request, runtime)

    async def list_application_configs_async(
        self,
        request: emr_20210320_models.ListApplicationConfigsRequest,
    ) -> emr_20210320_models.ListApplicationConfigsResponse:
        """
        @description 查询应用配置。
        
        @param request: ListApplicationConfigsRequest
        @return: ListApplicationConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_application_configs_with_options_async(request, runtime)

    def list_applications_with_options(
        self,
        request: emr_20210320_models.ListApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListApplicationsResponse:
        """
        @description 查询应用列表。
        
        @param request: ListApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_names):
            query['ApplicationNames'] = request.application_names
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplications',
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
            emr_20210320_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_with_options_async(
        self,
        request: emr_20210320_models.ListApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListApplicationsResponse:
        """
        @description 查询应用列表。
        
        @param request: ListApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_names):
            query['ApplicationNames'] = request.application_names
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplications',
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
            emr_20210320_models.ListApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications(
        self,
        request: emr_20210320_models.ListApplicationsRequest,
    ) -> emr_20210320_models.ListApplicationsResponse:
        """
        @description 查询应用列表。
        
        @param request: ListApplicationsRequest
        @return: ListApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_applications_with_options(request, runtime)

    async def list_applications_async(
        self,
        request: emr_20210320_models.ListApplicationsRequest,
    ) -> emr_20210320_models.ListApplicationsResponse:
        """
        @description 查询应用列表。
        
        @param request: ListApplicationsRequest
        @return: ListApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_applications_with_options_async(request, runtime)

    def list_auto_scaling_activities_with_options(
        self,
        request: emr_20210320_models.ListAutoScalingActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListAutoScalingActivitiesResponse:
        """
        @description 查询弹性伸缩活动列表。
        
        @param request: ListAutoScalingActivitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAutoScalingActivitiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_activity_states):
            query['ScalingActivityStates'] = request.scaling_activity_states
        if not UtilClient.is_unset(request.scaling_activity_type):
            query['ScalingActivityType'] = request.scaling_activity_type
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAutoScalingActivities',
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
            emr_20210320_models.ListAutoScalingActivitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_auto_scaling_activities_with_options_async(
        self,
        request: emr_20210320_models.ListAutoScalingActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListAutoScalingActivitiesResponse:
        """
        @description 查询弹性伸缩活动列表。
        
        @param request: ListAutoScalingActivitiesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAutoScalingActivitiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_activity_states):
            query['ScalingActivityStates'] = request.scaling_activity_states
        if not UtilClient.is_unset(request.scaling_activity_type):
            query['ScalingActivityType'] = request.scaling_activity_type
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAutoScalingActivities',
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
            emr_20210320_models.ListAutoScalingActivitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_auto_scaling_activities(
        self,
        request: emr_20210320_models.ListAutoScalingActivitiesRequest,
    ) -> emr_20210320_models.ListAutoScalingActivitiesResponse:
        """
        @description 查询弹性伸缩活动列表。
        
        @param request: ListAutoScalingActivitiesRequest
        @return: ListAutoScalingActivitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_auto_scaling_activities_with_options(request, runtime)

    async def list_auto_scaling_activities_async(
        self,
        request: emr_20210320_models.ListAutoScalingActivitiesRequest,
    ) -> emr_20210320_models.ListAutoScalingActivitiesResponse:
        """
        @description 查询弹性伸缩活动列表。
        
        @param request: ListAutoScalingActivitiesRequest
        @return: ListAutoScalingActivitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_auto_scaling_activities_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: emr_20210320_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListClustersResponse:
        """
        @summary Queries E-MapReduce (EMR) clusters.
        
        @param request: ListClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_states):
            query['ClusterStates'] = request.cluster_states
        if not UtilClient.is_unset(request.cluster_types):
            query['ClusterTypes'] = request.cluster_types
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.payment_types):
            query['PaymentTypes'] = request.payment_types
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
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
            emr_20210320_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: emr_20210320_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListClustersResponse:
        """
        @summary Queries E-MapReduce (EMR) clusters.
        
        @param request: ListClustersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListClustersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_states):
            query['ClusterStates'] = request.cluster_states
        if not UtilClient.is_unset(request.cluster_types):
            query['ClusterTypes'] = request.cluster_types
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.payment_types):
            query['PaymentTypes'] = request.payment_types
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
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
            emr_20210320_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        request: emr_20210320_models.ListClustersRequest,
    ) -> emr_20210320_models.ListClustersResponse:
        """
        @summary Queries E-MapReduce (EMR) clusters.
        
        @param request: ListClustersRequest
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: emr_20210320_models.ListClustersRequest,
    ) -> emr_20210320_models.ListClustersResponse:
        """
        @summary Queries E-MapReduce (EMR) clusters.
        
        @param request: ListClustersRequest
        @return: ListClustersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_component_instances_with_options(
        self,
        request: emr_20210320_models.ListComponentInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListComponentInstancesResponse:
        """
        @description 查询组件实例列表。
        
        @param request: ListComponentInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComponentInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_names):
            query['ApplicationNames'] = request.application_names
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_names):
            query['ComponentNames'] = request.component_names
        if not UtilClient.is_unset(request.component_states):
            query['ComponentStates'] = request.component_states
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.node_names):
            query['NodeNames'] = request.node_names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListComponentInstances',
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
            emr_20210320_models.ListComponentInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_component_instances_with_options_async(
        self,
        request: emr_20210320_models.ListComponentInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListComponentInstancesResponse:
        """
        @description 查询组件实例列表。
        
        @param request: ListComponentInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComponentInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_names):
            query['ApplicationNames'] = request.application_names
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_names):
            query['ComponentNames'] = request.component_names
        if not UtilClient.is_unset(request.component_states):
            query['ComponentStates'] = request.component_states
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.node_names):
            query['NodeNames'] = request.node_names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListComponentInstances',
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
            emr_20210320_models.ListComponentInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_component_instances(
        self,
        request: emr_20210320_models.ListComponentInstancesRequest,
    ) -> emr_20210320_models.ListComponentInstancesResponse:
        """
        @description 查询组件实例列表。
        
        @param request: ListComponentInstancesRequest
        @return: ListComponentInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_component_instances_with_options(request, runtime)

    async def list_component_instances_async(
        self,
        request: emr_20210320_models.ListComponentInstancesRequest,
    ) -> emr_20210320_models.ListComponentInstancesResponse:
        """
        @description 查询组件实例列表。
        
        @param request: ListComponentInstancesRequest
        @return: ListComponentInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_component_instances_with_options_async(request, runtime)

    def list_components_with_options(
        self,
        request: emr_20210320_models.ListComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListComponentsResponse:
        """
        @description 查询组件列表。
        
        @param request: ListComponentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComponentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_names):
            query['ApplicationNames'] = request.application_names
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_names):
            query['ComponentNames'] = request.component_names
        if not UtilClient.is_unset(request.component_states):
            query['ComponentStates'] = request.component_states
        if not UtilClient.is_unset(request.include_expired_config):
            query['IncludeExpiredConfig'] = request.include_expired_config
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListComponents',
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
            emr_20210320_models.ListComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_components_with_options_async(
        self,
        request: emr_20210320_models.ListComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListComponentsResponse:
        """
        @description 查询组件列表。
        
        @param request: ListComponentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListComponentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_names):
            query['ApplicationNames'] = request.application_names
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_names):
            query['ComponentNames'] = request.component_names
        if not UtilClient.is_unset(request.component_states):
            query['ComponentStates'] = request.component_states
        if not UtilClient.is_unset(request.include_expired_config):
            query['IncludeExpiredConfig'] = request.include_expired_config
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListComponents',
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
            emr_20210320_models.ListComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_components(
        self,
        request: emr_20210320_models.ListComponentsRequest,
    ) -> emr_20210320_models.ListComponentsResponse:
        """
        @description 查询组件列表。
        
        @param request: ListComponentsRequest
        @return: ListComponentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_components_with_options(request, runtime)

    async def list_components_async(
        self,
        request: emr_20210320_models.ListComponentsRequest,
    ) -> emr_20210320_models.ListComponentsResponse:
        """
        @description 查询组件列表。
        
        @param request: ListComponentsRequest
        @return: ListComponentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_components_with_options_async(request, runtime)

    def list_doctor_applications_with_options(
        self,
        request: emr_20210320_models.ListDoctorApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorApplicationsResponse:
        """
        @summary Obtains the analysis results of multiple jobs on E-MapReduce (EMR) Doctor.
        
        @description list all doctor analysis apps
        
        @param request: ListDoctorApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.queues):
            query['Queues'] = request.queues
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.users):
            query['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorApplications',
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
            emr_20210320_models.ListDoctorApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_applications_with_options_async(
        self,
        request: emr_20210320_models.ListDoctorApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorApplicationsResponse:
        """
        @summary Obtains the analysis results of multiple jobs on E-MapReduce (EMR) Doctor.
        
        @description list all doctor analysis apps
        
        @param request: ListDoctorApplicationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.queues):
            query['Queues'] = request.queues
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.users):
            query['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorApplications',
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
            emr_20210320_models.ListDoctorApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_applications(
        self,
        request: emr_20210320_models.ListDoctorApplicationsRequest,
    ) -> emr_20210320_models.ListDoctorApplicationsResponse:
        """
        @summary Obtains the analysis results of multiple jobs on E-MapReduce (EMR) Doctor.
        
        @description list all doctor analysis apps
        
        @param request: ListDoctorApplicationsRequest
        @return: ListDoctorApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_applications_with_options(request, runtime)

    async def list_doctor_applications_async(
        self,
        request: emr_20210320_models.ListDoctorApplicationsRequest,
    ) -> emr_20210320_models.ListDoctorApplicationsResponse:
        """
        @summary Obtains the analysis results of multiple jobs on E-MapReduce (EMR) Doctor.
        
        @description list all doctor analysis apps
        
        @param request: ListDoctorApplicationsRequest
        @return: ListDoctorApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_doctor_applications_with_options_async(request, runtime)

    def list_doctor_compute_summary_with_options(
        self,
        request: emr_20210320_models.ListDoctorComputeSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorComputeSummaryResponse:
        """
        @summary Obtains the information about resource usage by resource type in a cluster on E-MapReduce (EMR) Doctor.
        
        @description list Doctor analysis result of cluster engine queue view
        
        @param request: ListDoctorComputeSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorComputeSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_types):
            query['ComponentTypes'] = request.component_types
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorComputeSummary',
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
            emr_20210320_models.ListDoctorComputeSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_compute_summary_with_options_async(
        self,
        request: emr_20210320_models.ListDoctorComputeSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorComputeSummaryResponse:
        """
        @summary Obtains the information about resource usage by resource type in a cluster on E-MapReduce (EMR) Doctor.
        
        @description list Doctor analysis result of cluster engine queue view
        
        @param request: ListDoctorComputeSummaryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorComputeSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_types):
            query['ComponentTypes'] = request.component_types
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorComputeSummary',
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
            emr_20210320_models.ListDoctorComputeSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_compute_summary(
        self,
        request: emr_20210320_models.ListDoctorComputeSummaryRequest,
    ) -> emr_20210320_models.ListDoctorComputeSummaryResponse:
        """
        @summary Obtains the information about resource usage by resource type in a cluster on E-MapReduce (EMR) Doctor.
        
        @description list Doctor analysis result of cluster engine queue view
        
        @param request: ListDoctorComputeSummaryRequest
        @return: ListDoctorComputeSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_compute_summary_with_options(request, runtime)

    async def list_doctor_compute_summary_async(
        self,
        request: emr_20210320_models.ListDoctorComputeSummaryRequest,
    ) -> emr_20210320_models.ListDoctorComputeSummaryResponse:
        """
        @summary Obtains the information about resource usage by resource type in a cluster on E-MapReduce (EMR) Doctor.
        
        @description list Doctor analysis result of cluster engine queue view
        
        @param request: ListDoctorComputeSummaryRequest
        @return: ListDoctorComputeSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_doctor_compute_summary_with_options_async(request, runtime)

    def list_doctor_hbase_region_servers_with_options(
        self,
        request: emr_20210320_models.ListDoctorHBaseRegionServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorHBaseRegionServersResponse:
        """
        @summary Obtains the information about multiple HBase RegionServers at a time.
        
        @description list Doctor HBaseRegionServers
        
        @param request: ListDoctorHBaseRegionServersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorHBaseRegionServersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_server_hosts):
            query['RegionServerHosts'] = request.region_server_hosts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHBaseRegionServers',
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
            emr_20210320_models.ListDoctorHBaseRegionServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_hbase_region_servers_with_options_async(
        self,
        request: emr_20210320_models.ListDoctorHBaseRegionServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorHBaseRegionServersResponse:
        """
        @summary Obtains the information about multiple HBase RegionServers at a time.
        
        @description list Doctor HBaseRegionServers
        
        @param request: ListDoctorHBaseRegionServersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorHBaseRegionServersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_server_hosts):
            query['RegionServerHosts'] = request.region_server_hosts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHBaseRegionServers',
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
            emr_20210320_models.ListDoctorHBaseRegionServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_hbase_region_servers(
        self,
        request: emr_20210320_models.ListDoctorHBaseRegionServersRequest,
    ) -> emr_20210320_models.ListDoctorHBaseRegionServersResponse:
        """
        @summary Obtains the information about multiple HBase RegionServers at a time.
        
        @description list Doctor HBaseRegionServers
        
        @param request: ListDoctorHBaseRegionServersRequest
        @return: ListDoctorHBaseRegionServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_hbase_region_servers_with_options(request, runtime)

    async def list_doctor_hbase_region_servers_async(
        self,
        request: emr_20210320_models.ListDoctorHBaseRegionServersRequest,
    ) -> emr_20210320_models.ListDoctorHBaseRegionServersResponse:
        """
        @summary Obtains the information about multiple HBase RegionServers at a time.
        
        @description list Doctor HBaseRegionServers
        
        @param request: ListDoctorHBaseRegionServersRequest
        @return: ListDoctorHBaseRegionServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_doctor_hbase_region_servers_with_options_async(request, runtime)

    def list_doctor_hbase_tables_with_options(
        self,
        request: emr_20210320_models.ListDoctorHBaseTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorHBaseTablesResponse:
        """
        @summary Obtains the information about multiple HBase tables at a time.
        
        @description list Doctor HBaseTables
        
        @param request: ListDoctorHBaseTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorHBaseTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_names):
            query['TableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHBaseTables',
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
            emr_20210320_models.ListDoctorHBaseTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_hbase_tables_with_options_async(
        self,
        request: emr_20210320_models.ListDoctorHBaseTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorHBaseTablesResponse:
        """
        @summary Obtains the information about multiple HBase tables at a time.
        
        @description list Doctor HBaseTables
        
        @param request: ListDoctorHBaseTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorHBaseTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_names):
            query['TableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHBaseTables',
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
            emr_20210320_models.ListDoctorHBaseTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_hbase_tables(
        self,
        request: emr_20210320_models.ListDoctorHBaseTablesRequest,
    ) -> emr_20210320_models.ListDoctorHBaseTablesResponse:
        """
        @summary Obtains the information about multiple HBase tables at a time.
        
        @description list Doctor HBaseTables
        
        @param request: ListDoctorHBaseTablesRequest
        @return: ListDoctorHBaseTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_hbase_tables_with_options(request, runtime)

    async def list_doctor_hbase_tables_async(
        self,
        request: emr_20210320_models.ListDoctorHBaseTablesRequest,
    ) -> emr_20210320_models.ListDoctorHBaseTablesResponse:
        """
        @summary Obtains the information about multiple HBase tables at a time.
        
        @description list Doctor HBaseTables
        
        @param request: ListDoctorHBaseTablesRequest
        @return: ListDoctorHBaseTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_doctor_hbase_tables_with_options_async(request, runtime)

    def list_doctor_hdfsdirectories_with_options(
        self,
        request: emr_20210320_models.ListDoctorHDFSDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorHDFSDirectoriesResponse:
        """
        @description list Doctor HDFSNodes
        
        @param request: ListDoctorHDFSDirectoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorHDFSDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.dir_path):
            query['DirPath'] = request.dir_path
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHDFSDirectories',
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
            emr_20210320_models.ListDoctorHDFSDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_hdfsdirectories_with_options_async(
        self,
        request: emr_20210320_models.ListDoctorHDFSDirectoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorHDFSDirectoriesResponse:
        """
        @description list Doctor HDFSNodes
        
        @param request: ListDoctorHDFSDirectoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorHDFSDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.dir_path):
            query['DirPath'] = request.dir_path
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHDFSDirectories',
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
            emr_20210320_models.ListDoctorHDFSDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_hdfsdirectories(
        self,
        request: emr_20210320_models.ListDoctorHDFSDirectoriesRequest,
    ) -> emr_20210320_models.ListDoctorHDFSDirectoriesResponse:
        """
        @description list Doctor HDFSNodes
        
        @param request: ListDoctorHDFSDirectoriesRequest
        @return: ListDoctorHDFSDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_hdfsdirectories_with_options(request, runtime)

    async def list_doctor_hdfsdirectories_async(
        self,
        request: emr_20210320_models.ListDoctorHDFSDirectoriesRequest,
    ) -> emr_20210320_models.ListDoctorHDFSDirectoriesResponse:
        """
        @description list Doctor HDFSNodes
        
        @param request: ListDoctorHDFSDirectoriesRequest
        @return: ListDoctorHDFSDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_doctor_hdfsdirectories_with_options_async(request, runtime)

    def list_doctor_hdfsugiwith_options(
        self,
        request: emr_20210320_models.ListDoctorHDFSUGIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorHDFSUGIResponse:
        """
        @summary Obtains the analysis results of Hadoop Distributed File System (HDFS) storage resources for multiple owners or groups at a time on E-MapReduce (EMR) Doctor.
        
        @description list Doctor HDFS UGIs
        
        @param request: ListDoctorHDFSUGIRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorHDFSUGIResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHDFSUGI',
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
            emr_20210320_models.ListDoctorHDFSUGIResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_hdfsugiwith_options_async(
        self,
        request: emr_20210320_models.ListDoctorHDFSUGIRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorHDFSUGIResponse:
        """
        @summary Obtains the analysis results of Hadoop Distributed File System (HDFS) storage resources for multiple owners or groups at a time on E-MapReduce (EMR) Doctor.
        
        @description list Doctor HDFS UGIs
        
        @param request: ListDoctorHDFSUGIRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorHDFSUGIResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHDFSUGI',
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
            emr_20210320_models.ListDoctorHDFSUGIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_hdfsugi(
        self,
        request: emr_20210320_models.ListDoctorHDFSUGIRequest,
    ) -> emr_20210320_models.ListDoctorHDFSUGIResponse:
        """
        @summary Obtains the analysis results of Hadoop Distributed File System (HDFS) storage resources for multiple owners or groups at a time on E-MapReduce (EMR) Doctor.
        
        @description list Doctor HDFS UGIs
        
        @param request: ListDoctorHDFSUGIRequest
        @return: ListDoctorHDFSUGIResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_hdfsugiwith_options(request, runtime)

    async def list_doctor_hdfsugi_async(
        self,
        request: emr_20210320_models.ListDoctorHDFSUGIRequest,
    ) -> emr_20210320_models.ListDoctorHDFSUGIResponse:
        """
        @summary Obtains the analysis results of Hadoop Distributed File System (HDFS) storage resources for multiple owners or groups at a time on E-MapReduce (EMR) Doctor.
        
        @description list Doctor HDFS UGIs
        
        @param request: ListDoctorHDFSUGIRequest
        @return: ListDoctorHDFSUGIResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_doctor_hdfsugiwith_options_async(request, runtime)

    def list_doctor_hive_databases_with_options(
        self,
        request: emr_20210320_models.ListDoctorHiveDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorHiveDatabasesResponse:
        """
        @summary Obtains the analysis results of multiple Hive databases at a time.
        
        @description list Doctor Hive Databases
        
        @param request: ListDoctorHiveDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorHiveDatabasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_names):
            query['DatabaseNames'] = request.database_names
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHiveDatabases',
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
            emr_20210320_models.ListDoctorHiveDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_hive_databases_with_options_async(
        self,
        request: emr_20210320_models.ListDoctorHiveDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorHiveDatabasesResponse:
        """
        @summary Obtains the analysis results of multiple Hive databases at a time.
        
        @description list Doctor Hive Databases
        
        @param request: ListDoctorHiveDatabasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorHiveDatabasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_names):
            query['DatabaseNames'] = request.database_names
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHiveDatabases',
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
            emr_20210320_models.ListDoctorHiveDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_hive_databases(
        self,
        request: emr_20210320_models.ListDoctorHiveDatabasesRequest,
    ) -> emr_20210320_models.ListDoctorHiveDatabasesResponse:
        """
        @summary Obtains the analysis results of multiple Hive databases at a time.
        
        @description list Doctor Hive Databases
        
        @param request: ListDoctorHiveDatabasesRequest
        @return: ListDoctorHiveDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_hive_databases_with_options(request, runtime)

    async def list_doctor_hive_databases_async(
        self,
        request: emr_20210320_models.ListDoctorHiveDatabasesRequest,
    ) -> emr_20210320_models.ListDoctorHiveDatabasesResponse:
        """
        @summary Obtains the analysis results of multiple Hive databases at a time.
        
        @description list Doctor Hive Databases
        
        @param request: ListDoctorHiveDatabasesRequest
        @return: ListDoctorHiveDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_doctor_hive_databases_with_options_async(request, runtime)

    def list_doctor_hive_tables_with_options(
        self,
        request: emr_20210320_models.ListDoctorHiveTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorHiveTablesResponse:
        """
        @summary Obtains the analysis results of multiple Hive tables at a time on E-MapReduce (EMR) Doctor.
        
        @description list Doctor Hive Tables
        
        @param request: ListDoctorHiveTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorHiveTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_names):
            query['TableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHiveTables',
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
            emr_20210320_models.ListDoctorHiveTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_hive_tables_with_options_async(
        self,
        request: emr_20210320_models.ListDoctorHiveTablesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorHiveTablesResponse:
        """
        @summary Obtains the analysis results of multiple Hive tables at a time on E-MapReduce (EMR) Doctor.
        
        @description list Doctor Hive Tables
        
        @param request: ListDoctorHiveTablesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorHiveTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_names):
            query['TableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHiveTables',
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
            emr_20210320_models.ListDoctorHiveTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_hive_tables(
        self,
        request: emr_20210320_models.ListDoctorHiveTablesRequest,
    ) -> emr_20210320_models.ListDoctorHiveTablesResponse:
        """
        @summary Obtains the analysis results of multiple Hive tables at a time on E-MapReduce (EMR) Doctor.
        
        @description list Doctor Hive Tables
        
        @param request: ListDoctorHiveTablesRequest
        @return: ListDoctorHiveTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_hive_tables_with_options(request, runtime)

    async def list_doctor_hive_tables_async(
        self,
        request: emr_20210320_models.ListDoctorHiveTablesRequest,
    ) -> emr_20210320_models.ListDoctorHiveTablesResponse:
        """
        @summary Obtains the analysis results of multiple Hive tables at a time on E-MapReduce (EMR) Doctor.
        
        @description list Doctor Hive Tables
        
        @param request: ListDoctorHiveTablesRequest
        @return: ListDoctorHiveTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_doctor_hive_tables_with_options_async(request, runtime)

    def list_doctor_jobs_with_options(
        self,
        request: emr_20210320_models.ListDoctorJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorJobsResponse:
        """
        @summary Obtains the basic running information about multiple jobs at a time on E-MapReduce (EMR) Doctor.
        
        @description list realtime jobs by yarn
        
        @param request: ListDoctorJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_range):
            query['EndRange'] = request.end_range
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.queues):
            query['Queues'] = request.queues
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_range):
            query['StartRange'] = request.start_range
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.users):
            query['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorJobs',
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
            emr_20210320_models.ListDoctorJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_jobs_with_options_async(
        self,
        request: emr_20210320_models.ListDoctorJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorJobsResponse:
        """
        @summary Obtains the basic running information about multiple jobs at a time on E-MapReduce (EMR) Doctor.
        
        @description list realtime jobs by yarn
        
        @param request: ListDoctorJobsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_range):
            query['EndRange'] = request.end_range
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.queues):
            query['Queues'] = request.queues
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_range):
            query['StartRange'] = request.start_range
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.users):
            query['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorJobs',
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
            emr_20210320_models.ListDoctorJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_jobs(
        self,
        request: emr_20210320_models.ListDoctorJobsRequest,
    ) -> emr_20210320_models.ListDoctorJobsResponse:
        """
        @summary Obtains the basic running information about multiple jobs at a time on E-MapReduce (EMR) Doctor.
        
        @description list realtime jobs by yarn
        
        @param request: ListDoctorJobsRequest
        @return: ListDoctorJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_jobs_with_options(request, runtime)

    async def list_doctor_jobs_async(
        self,
        request: emr_20210320_models.ListDoctorJobsRequest,
    ) -> emr_20210320_models.ListDoctorJobsResponse:
        """
        @summary Obtains the basic running information about multiple jobs at a time on E-MapReduce (EMR) Doctor.
        
        @description list realtime jobs by yarn
        
        @param request: ListDoctorJobsRequest
        @return: ListDoctorJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_doctor_jobs_with_options_async(request, runtime)

    def list_doctor_jobs_stats_with_options(
        self,
        request: emr_20210320_models.ListDoctorJobsStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorJobsStatsResponse:
        """
        @summary Obtains the summary of basic running information about multiple jobs at a time on E-MapReduce (EMR) Doctor.
        
        @description list stats groupBy jobs by yarn
        
        @param request: ListDoctorJobsStatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorJobsStatsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_range):
            query['EndRange'] = request.end_range
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_range):
            query['StartRange'] = request.start_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorJobsStats',
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
            emr_20210320_models.ListDoctorJobsStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_jobs_stats_with_options_async(
        self,
        request: emr_20210320_models.ListDoctorJobsStatsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorJobsStatsResponse:
        """
        @summary Obtains the summary of basic running information about multiple jobs at a time on E-MapReduce (EMR) Doctor.
        
        @description list stats groupBy jobs by yarn
        
        @param request: ListDoctorJobsStatsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorJobsStatsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_range):
            query['EndRange'] = request.end_range
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_range):
            query['StartRange'] = request.start_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorJobsStats',
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
            emr_20210320_models.ListDoctorJobsStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_jobs_stats(
        self,
        request: emr_20210320_models.ListDoctorJobsStatsRequest,
    ) -> emr_20210320_models.ListDoctorJobsStatsResponse:
        """
        @summary Obtains the summary of basic running information about multiple jobs at a time on E-MapReduce (EMR) Doctor.
        
        @description list stats groupBy jobs by yarn
        
        @param request: ListDoctorJobsStatsRequest
        @return: ListDoctorJobsStatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_jobs_stats_with_options(request, runtime)

    async def list_doctor_jobs_stats_async(
        self,
        request: emr_20210320_models.ListDoctorJobsStatsRequest,
    ) -> emr_20210320_models.ListDoctorJobsStatsResponse:
        """
        @summary Obtains the summary of basic running information about multiple jobs at a time on E-MapReduce (EMR) Doctor.
        
        @description list stats groupBy jobs by yarn
        
        @param request: ListDoctorJobsStatsRequest
        @return: ListDoctorJobsStatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_doctor_jobs_stats_with_options_async(request, runtime)

    def list_doctor_reports_with_options(
        self,
        request: emr_20210320_models.ListDoctorReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorReportsResponse:
        """
        @summary Obtains the overall analysis result reports of E-MapReduce (EMR) Doctor at a time.
        
        @description list all reports analysis by emr doctor
        
        @param request: ListDoctorReportsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorReportsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorReports',
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
            emr_20210320_models.ListDoctorReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_reports_with_options_async(
        self,
        request: emr_20210320_models.ListDoctorReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListDoctorReportsResponse:
        """
        @summary Obtains the overall analysis result reports of E-MapReduce (EMR) Doctor at a time.
        
        @description list all reports analysis by emr doctor
        
        @param request: ListDoctorReportsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDoctorReportsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorReports',
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
            emr_20210320_models.ListDoctorReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_reports(
        self,
        request: emr_20210320_models.ListDoctorReportsRequest,
    ) -> emr_20210320_models.ListDoctorReportsResponse:
        """
        @summary Obtains the overall analysis result reports of E-MapReduce (EMR) Doctor at a time.
        
        @description list all reports analysis by emr doctor
        
        @param request: ListDoctorReportsRequest
        @return: ListDoctorReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_reports_with_options(request, runtime)

    async def list_doctor_reports_async(
        self,
        request: emr_20210320_models.ListDoctorReportsRequest,
    ) -> emr_20210320_models.ListDoctorReportsResponse:
        """
        @summary Obtains the overall analysis result reports of E-MapReduce (EMR) Doctor at a time.
        
        @description list all reports analysis by emr doctor
        
        @param request: ListDoctorReportsRequest
        @return: ListDoctorReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_doctor_reports_with_options_async(request, runtime)

    def list_inspection_history_with_options(
        self,
        request: emr_20210320_models.ListInspectionHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListInspectionHistoryResponse:
        """
        @param request: ListInspectionHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInspectionHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component):
            query['Component'] = request.component
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInspectionHistory',
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
            emr_20210320_models.ListInspectionHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_inspection_history_with_options_async(
        self,
        request: emr_20210320_models.ListInspectionHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListInspectionHistoryResponse:
        """
        @param request: ListInspectionHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInspectionHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component):
            query['Component'] = request.component
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInspectionHistory',
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
            emr_20210320_models.ListInspectionHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_inspection_history(
        self,
        request: emr_20210320_models.ListInspectionHistoryRequest,
    ) -> emr_20210320_models.ListInspectionHistoryResponse:
        """
        @param request: ListInspectionHistoryRequest
        @return: ListInspectionHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_inspection_history_with_options(request, runtime)

    async def list_inspection_history_async(
        self,
        request: emr_20210320_models.ListInspectionHistoryRequest,
    ) -> emr_20210320_models.ListInspectionHistoryResponse:
        """
        @param request: ListInspectionHistoryRequest
        @return: ListInspectionHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_inspection_history_with_options_async(request, runtime)

    def list_instance_types_with_options(
        self,
        request: emr_20210320_models.ListInstanceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListInstanceTypesResponse:
        """
        @param request: ListInstanceTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceTypesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.deploy_mode):
            query['DeployMode'] = request.deploy_mode
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.is_modification):
            query['IsModification'] = request.is_modification
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.node_group_type):
            query['NodeGroupType'] = request.node_group_type
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.release_version):
            query['ReleaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceTypes',
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
            emr_20210320_models.ListInstanceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_types_with_options_async(
        self,
        request: emr_20210320_models.ListInstanceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListInstanceTypesResponse:
        """
        @param request: ListInstanceTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListInstanceTypesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.deploy_mode):
            query['DeployMode'] = request.deploy_mode
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.is_modification):
            query['IsModification'] = request.is_modification
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.node_group_type):
            query['NodeGroupType'] = request.node_group_type
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.release_version):
            query['ReleaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceTypes',
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
            emr_20210320_models.ListInstanceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_types(
        self,
        request: emr_20210320_models.ListInstanceTypesRequest,
    ) -> emr_20210320_models.ListInstanceTypesResponse:
        """
        @param request: ListInstanceTypesRequest
        @return: ListInstanceTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_instance_types_with_options(request, runtime)

    async def list_instance_types_async(
        self,
        request: emr_20210320_models.ListInstanceTypesRequest,
    ) -> emr_20210320_models.ListInstanceTypesResponse:
        """
        @param request: ListInstanceTypesRequest
        @return: ListInstanceTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_instance_types_with_options_async(request, runtime)

    def list_node_groups_with_options(
        self,
        request: emr_20210320_models.ListNodeGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListNodeGroupsResponse:
        """
        @summary Queries the list of node groups in an EMR cluster.
        
        @param request: ListNodeGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodeGroupsResponse
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
        @summary Queries the list of node groups in an EMR cluster.
        
        @param request: ListNodeGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodeGroupsResponse
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
        """
        @summary Queries the list of node groups in an EMR cluster.
        
        @param request: ListNodeGroupsRequest
        @return: ListNodeGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_node_groups_with_options(request, runtime)

    async def list_node_groups_async(
        self,
        request: emr_20210320_models.ListNodeGroupsRequest,
    ) -> emr_20210320_models.ListNodeGroupsResponse:
        """
        @summary Queries the list of node groups in an EMR cluster.
        
        @param request: ListNodeGroupsRequest
        @return: ListNodeGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_node_groups_with_options_async(request, runtime)

    def list_nodes_with_options(
        self,
        request: emr_20210320_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListNodesResponse:
        """
        @summary Queries the node list of an EMR cluster.
        
        @param request: ListNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesResponse
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
        @summary Queries the node list of an EMR cluster.
        
        @param request: ListNodesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListNodesResponse
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
        """
        @summary Queries the node list of an EMR cluster.
        
        @param request: ListNodesRequest
        @return: ListNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: emr_20210320_models.ListNodesRequest,
    ) -> emr_20210320_models.ListNodesResponse:
        """
        @summary Queries the node list of an EMR cluster.
        
        @param request: ListNodesRequest
        @return: ListNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)

    def list_release_versions_with_options(
        self,
        request: emr_20210320_models.ListReleaseVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListReleaseVersionsResponse:
        """
        @summary Queries the major E-MapReduce (EMR) versions.
        
        @description 查询主版本。
        
        @param request: ListReleaseVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListReleaseVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.iaas_type):
            query['IaasType'] = request.iaas_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReleaseVersions',
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
            emr_20210320_models.ListReleaseVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_release_versions_with_options_async(
        self,
        request: emr_20210320_models.ListReleaseVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListReleaseVersionsResponse:
        """
        @summary Queries the major E-MapReduce (EMR) versions.
        
        @description 查询主版本。
        
        @param request: ListReleaseVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListReleaseVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.iaas_type):
            query['IaasType'] = request.iaas_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReleaseVersions',
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
            emr_20210320_models.ListReleaseVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_release_versions(
        self,
        request: emr_20210320_models.ListReleaseVersionsRequest,
    ) -> emr_20210320_models.ListReleaseVersionsResponse:
        """
        @summary Queries the major E-MapReduce (EMR) versions.
        
        @description 查询主版本。
        
        @param request: ListReleaseVersionsRequest
        @return: ListReleaseVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_release_versions_with_options(request, runtime)

    async def list_release_versions_async(
        self,
        request: emr_20210320_models.ListReleaseVersionsRequest,
    ) -> emr_20210320_models.ListReleaseVersionsResponse:
        """
        @summary Queries the major E-MapReduce (EMR) versions.
        
        @description 查询主版本。
        
        @param request: ListReleaseVersionsRequest
        @return: ListReleaseVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_release_versions_with_options_async(request, runtime)

    def list_resource_health_inspections_with_options(
        self,
        request: emr_20210320_models.ListResourceHealthInspectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListResourceHealthInspectionsResponse:
        """
        @description 查询资源巡检项。
        
        @param request: ListResourceHealthInspectionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceHealthInspectionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.health_statuses):
            query['HealthStatuses'] = request.health_statuses
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.node_names):
            query['NodeNames'] = request.node_names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceHealthInspections',
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
            emr_20210320_models.ListResourceHealthInspectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_health_inspections_with_options_async(
        self,
        request: emr_20210320_models.ListResourceHealthInspectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListResourceHealthInspectionsResponse:
        """
        @description 查询资源巡检项。
        
        @param request: ListResourceHealthInspectionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceHealthInspectionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.health_statuses):
            query['HealthStatuses'] = request.health_statuses
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.node_names):
            query['NodeNames'] = request.node_names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceHealthInspections',
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
            emr_20210320_models.ListResourceHealthInspectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_health_inspections(
        self,
        request: emr_20210320_models.ListResourceHealthInspectionsRequest,
    ) -> emr_20210320_models.ListResourceHealthInspectionsResponse:
        """
        @description 查询资源巡检项。
        
        @param request: ListResourceHealthInspectionsRequest
        @return: ListResourceHealthInspectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_health_inspections_with_options(request, runtime)

    async def list_resource_health_inspections_async(
        self,
        request: emr_20210320_models.ListResourceHealthInspectionsRequest,
    ) -> emr_20210320_models.ListResourceHealthInspectionsResponse:
        """
        @description 查询资源巡检项。
        
        @param request: ListResourceHealthInspectionsRequest
        @return: ListResourceHealthInspectionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_health_inspections_with_options_async(request, runtime)

    def list_scripts_with_options(
        self,
        request: emr_20210320_models.ListScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListScriptsResponse:
        """
        @param request: ListScriptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScriptsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.script_type):
            query['ScriptType'] = request.script_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScripts',
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
            emr_20210320_models.ListScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scripts_with_options_async(
        self,
        request: emr_20210320_models.ListScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListScriptsResponse:
        """
        @param request: ListScriptsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListScriptsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.script_type):
            query['ScriptType'] = request.script_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScripts',
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
            emr_20210320_models.ListScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scripts(
        self,
        request: emr_20210320_models.ListScriptsRequest,
    ) -> emr_20210320_models.ListScriptsResponse:
        """
        @param request: ListScriptsRequest
        @return: ListScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_scripts_with_options(request, runtime)

    async def list_scripts_async(
        self,
        request: emr_20210320_models.ListScriptsRequest,
    ) -> emr_20210320_models.ListScriptsResponse:
        """
        @param request: ListScriptsRequest
        @return: ListScriptsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_scripts_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: emr_20210320_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are bound to an EMR cluster.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
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
            emr_20210320_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: emr_20210320_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are bound to an EMR cluster.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
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
            emr_20210320_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: emr_20210320_models.ListTagResourcesRequest,
    ) -> emr_20210320_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are bound to an EMR cluster.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: emr_20210320_models.ListTagResourcesRequest,
    ) -> emr_20210320_models.ListTagResourcesResponse:
        """
        @summary Queries the tags that are bound to an EMR cluster.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def put_auto_scaling_policy_with_options(
        self,
        request: emr_20210320_models.PutAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.PutAutoScalingPolicyResponse:
        """
        @summary Configures auto scaling rules.
        
        @description You can call this operation to configure auto scaling policies.
        
        @param request: PutAutoScalingPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutAutoScalingPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.constraints):
            query['Constraints'] = request.constraints
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_rules):
            query['ScalingRules'] = request.scaling_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutAutoScalingPolicy',
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
            emr_20210320_models.PutAutoScalingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_auto_scaling_policy_with_options_async(
        self,
        request: emr_20210320_models.PutAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.PutAutoScalingPolicyResponse:
        """
        @summary Configures auto scaling rules.
        
        @description You can call this operation to configure auto scaling policies.
        
        @param request: PutAutoScalingPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PutAutoScalingPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.constraints):
            query['Constraints'] = request.constraints
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_rules):
            query['ScalingRules'] = request.scaling_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutAutoScalingPolicy',
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
            emr_20210320_models.PutAutoScalingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_auto_scaling_policy(
        self,
        request: emr_20210320_models.PutAutoScalingPolicyRequest,
    ) -> emr_20210320_models.PutAutoScalingPolicyResponse:
        """
        @summary Configures auto scaling rules.
        
        @description You can call this operation to configure auto scaling policies.
        
        @param request: PutAutoScalingPolicyRequest
        @return: PutAutoScalingPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_auto_scaling_policy_with_options(request, runtime)

    async def put_auto_scaling_policy_async(
        self,
        request: emr_20210320_models.PutAutoScalingPolicyRequest,
    ) -> emr_20210320_models.PutAutoScalingPolicyResponse:
        """
        @summary Configures auto scaling rules.
        
        @description You can call this operation to configure auto scaling policies.
        
        @param request: PutAutoScalingPolicyRequest
        @return: PutAutoScalingPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.put_auto_scaling_policy_with_options_async(request, runtime)

    def remove_auto_scaling_policy_with_options(
        self,
        request: emr_20210320_models.RemoveAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.RemoveAutoScalingPolicyResponse:
        """
        @param request: RemoveAutoScalingPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveAutoScalingPolicyResponse
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
            action='RemoveAutoScalingPolicy',
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
            emr_20210320_models.RemoveAutoScalingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_auto_scaling_policy_with_options_async(
        self,
        request: emr_20210320_models.RemoveAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.RemoveAutoScalingPolicyResponse:
        """
        @param request: RemoveAutoScalingPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveAutoScalingPolicyResponse
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
            action='RemoveAutoScalingPolicy',
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
            emr_20210320_models.RemoveAutoScalingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_auto_scaling_policy(
        self,
        request: emr_20210320_models.RemoveAutoScalingPolicyRequest,
    ) -> emr_20210320_models.RemoveAutoScalingPolicyResponse:
        """
        @param request: RemoveAutoScalingPolicyRequest
        @return: RemoveAutoScalingPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_auto_scaling_policy_with_options(request, runtime)

    async def remove_auto_scaling_policy_async(
        self,
        request: emr_20210320_models.RemoveAutoScalingPolicyRequest,
    ) -> emr_20210320_models.RemoveAutoScalingPolicyResponse:
        """
        @param request: RemoveAutoScalingPolicyRequest
        @return: RemoveAutoScalingPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_auto_scaling_policy_with_options_async(request, runtime)

    def run_api_template_with_options(
        self,
        request: emr_20210320_models.RunApiTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.RunApiTemplateResponse:
        """
        @param request: RunApiTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunApiTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunApiTemplate',
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
            emr_20210320_models.RunApiTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_api_template_with_options_async(
        self,
        request: emr_20210320_models.RunApiTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.RunApiTemplateResponse:
        """
        @param request: RunApiTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunApiTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunApiTemplate',
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
            emr_20210320_models.RunApiTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_api_template(
        self,
        request: emr_20210320_models.RunApiTemplateRequest,
    ) -> emr_20210320_models.RunApiTemplateResponse:
        """
        @param request: RunApiTemplateRequest
        @return: RunApiTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_api_template_with_options(request, runtime)

    async def run_api_template_async(
        self,
        request: emr_20210320_models.RunApiTemplateRequest,
    ) -> emr_20210320_models.RunApiTemplateResponse:
        """
        @param request: RunApiTemplateRequest
        @return: RunApiTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_api_template_with_options_async(request, runtime)

    def run_application_action_with_options(
        self,
        request: emr_20210320_models.RunApplicationActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.RunApplicationActionResponse:
        """
        @param request: RunApplicationActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunApplicationActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.batch_size):
            query['BatchSize'] = request.batch_size
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_instance_selector):
            query['ComponentInstanceSelector'] = request.component_instance_selector
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execute_strategy):
            query['ExecuteStrategy'] = request.execute_strategy
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rolling_execute):
            query['RollingExecute'] = request.rolling_execute
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunApplicationAction',
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
            emr_20210320_models.RunApplicationActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_application_action_with_options_async(
        self,
        request: emr_20210320_models.RunApplicationActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.RunApplicationActionResponse:
        """
        @param request: RunApplicationActionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RunApplicationActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.batch_size):
            query['BatchSize'] = request.batch_size
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_instance_selector):
            query['ComponentInstanceSelector'] = request.component_instance_selector
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execute_strategy):
            query['ExecuteStrategy'] = request.execute_strategy
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rolling_execute):
            query['RollingExecute'] = request.rolling_execute
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunApplicationAction',
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
            emr_20210320_models.RunApplicationActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_application_action(
        self,
        request: emr_20210320_models.RunApplicationActionRequest,
    ) -> emr_20210320_models.RunApplicationActionResponse:
        """
        @param request: RunApplicationActionRequest
        @return: RunApplicationActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_application_action_with_options(request, runtime)

    async def run_application_action_async(
        self,
        request: emr_20210320_models.RunApplicationActionRequest,
    ) -> emr_20210320_models.RunApplicationActionResponse:
        """
        @param request: RunApplicationActionRequest
        @return: RunApplicationActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.run_application_action_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: emr_20210320_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.TagResourcesResponse:
        """
        @summary Bind tags to a specified EMR cluster.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
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
            emr_20210320_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: emr_20210320_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.TagResourcesResponse:
        """
        @summary Bind tags to a specified EMR cluster.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
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
            emr_20210320_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: emr_20210320_models.TagResourcesRequest,
    ) -> emr_20210320_models.TagResourcesResponse:
        """
        @summary Bind tags to a specified EMR cluster.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: emr_20210320_models.TagResourcesRequest,
    ) -> emr_20210320_models.TagResourcesResponse:
        """
        @summary Bind tags to a specified EMR cluster.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: emr_20210320_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.UntagResourcesResponse:
        """
        @summary Unbinds tags from a specified column in an EMR cluster. If the tag is not bound to other resources, the tag is automatically deleted.
        
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
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
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
            emr_20210320_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: emr_20210320_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.UntagResourcesResponse:
        """
        @summary Unbinds tags from a specified column in an EMR cluster. If the tag is not bound to other resources, the tag is automatically deleted.
        
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
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
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
            emr_20210320_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: emr_20210320_models.UntagResourcesRequest,
    ) -> emr_20210320_models.UntagResourcesResponse:
        """
        @summary Unbinds tags from a specified column in an EMR cluster. If the tag is not bound to other resources, the tag is automatically deleted.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: emr_20210320_models.UntagResourcesRequest,
    ) -> emr_20210320_models.UntagResourcesResponse:
        """
        @summary Unbinds tags from a specified column in an EMR cluster. If the tag is not bound to other resources, the tag is automatically deleted.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_api_template_with_options(
        self,
        request: emr_20210320_models.UpdateApiTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.UpdateApiTemplateResponse:
        """
        @summary Updates an API operation template.
        
        @description 修改集群模板
        
        @param request: UpdateApiTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApiTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApiTemplate',
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
            emr_20210320_models.UpdateApiTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_api_template_with_options_async(
        self,
        request: emr_20210320_models.UpdateApiTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.UpdateApiTemplateResponse:
        """
        @summary Updates an API operation template.
        
        @description 修改集群模板
        
        @param request: UpdateApiTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApiTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['ApiName'] = request.api_name
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApiTemplate',
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
            emr_20210320_models.UpdateApiTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_api_template(
        self,
        request: emr_20210320_models.UpdateApiTemplateRequest,
    ) -> emr_20210320_models.UpdateApiTemplateResponse:
        """
        @summary Updates an API operation template.
        
        @description 修改集群模板
        
        @param request: UpdateApiTemplateRequest
        @return: UpdateApiTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_api_template_with_options(request, runtime)

    async def update_api_template_async(
        self,
        request: emr_20210320_models.UpdateApiTemplateRequest,
    ) -> emr_20210320_models.UpdateApiTemplateResponse:
        """
        @summary Updates an API operation template.
        
        @description 修改集群模板
        
        @param request: UpdateApiTemplateRequest
        @return: UpdateApiTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_api_template_with_options_async(request, runtime)

    def update_application_configs_with_options(
        self,
        request: emr_20210320_models.UpdateApplicationConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.UpdateApplicationConfigsResponse:
        """
        @param request: UpdateApplicationConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_configs):
            query['ApplicationConfigs'] = request.application_configs
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.config_action):
            query['ConfigAction'] = request.config_action
        if not UtilClient.is_unset(request.config_scope):
            query['ConfigScope'] = request.config_scope
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.refresh_config):
            query['RefreshConfig'] = request.refresh_config
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationConfigs',
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
            emr_20210320_models.UpdateApplicationConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_configs_with_options_async(
        self,
        request: emr_20210320_models.UpdateApplicationConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.UpdateApplicationConfigsResponse:
        """
        @param request: UpdateApplicationConfigsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateApplicationConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_configs):
            query['ApplicationConfigs'] = request.application_configs
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.config_action):
            query['ConfigAction'] = request.config_action
        if not UtilClient.is_unset(request.config_scope):
            query['ConfigScope'] = request.config_scope
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.refresh_config):
            query['RefreshConfig'] = request.refresh_config
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationConfigs',
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
            emr_20210320_models.UpdateApplicationConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_configs(
        self,
        request: emr_20210320_models.UpdateApplicationConfigsRequest,
    ) -> emr_20210320_models.UpdateApplicationConfigsResponse:
        """
        @param request: UpdateApplicationConfigsRequest
        @return: UpdateApplicationConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_application_configs_with_options(request, runtime)

    async def update_application_configs_async(
        self,
        request: emr_20210320_models.UpdateApplicationConfigsRequest,
    ) -> emr_20210320_models.UpdateApplicationConfigsResponse:
        """
        @param request: UpdateApplicationConfigsRequest
        @return: UpdateApplicationConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_application_configs_with_options_async(request, runtime)

    def update_script_with_options(
        self,
        tmp_req: emr_20210320_models.UpdateScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.UpdateScriptResponse:
        """
        @param tmp_req: UpdateScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateScriptResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_20210320_models.UpdateScriptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.script):
            request.script_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.script, 'Script', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.script_shrink):
            query['Script'] = request.script_shrink
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.script_type):
            query['ScriptType'] = request.script_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScript',
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
            emr_20210320_models.UpdateScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_script_with_options_async(
        self,
        tmp_req: emr_20210320_models.UpdateScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20210320_models.UpdateScriptResponse:
        """
        @param tmp_req: UpdateScriptRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateScriptResponse
        """
        UtilClient.validate_model(tmp_req)
        request = emr_20210320_models.UpdateScriptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.script):
            request.script_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.script, 'Script', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.script_shrink):
            query['Script'] = request.script_shrink
        if not UtilClient.is_unset(request.script_id):
            query['ScriptId'] = request.script_id
        if not UtilClient.is_unset(request.script_type):
            query['ScriptType'] = request.script_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateScript',
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
            emr_20210320_models.UpdateScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_script(
        self,
        request: emr_20210320_models.UpdateScriptRequest,
    ) -> emr_20210320_models.UpdateScriptResponse:
        """
        @param request: UpdateScriptRequest
        @return: UpdateScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_script_with_options(request, runtime)

    async def update_script_async(
        self,
        request: emr_20210320_models.UpdateScriptRequest,
    ) -> emr_20210320_models.UpdateScriptResponse:
        """
        @param request: UpdateScriptRequest
        @return: UpdateScriptResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_script_with_options_async(request, runtime)
