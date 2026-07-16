# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_emr20210320 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
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
            'rus-west-1-pop': 'emr.aliyuncs.com',
            'us-east-1': 'emr.us-east-1.aliyuncs.com',
            'me-east-1': 'emr.me-east-1.aliyuncs.com',
            'me-central-1': 'emr.me-central-1.aliyuncs.com',
            'eu-west-1': 'emr.eu-west-1.aliyuncs.com',
            'eu-central-1': 'emr.eu-central-1.aliyuncs.com',
            'cn-zhangjiakou': 'emr.cn-zhangjiakou.aliyuncs.com',
            'cn-wulanchabu': 'emr.cn-wulanchabu.aliyuncs.com',
            'cn-qingdao': 'emr.cn-qingdao.aliyuncs.com',
            'cn-huhehaote': 'emr.cn-huhehaote.aliyuncs.com',
            'cn-hongkong': 'emr.cn-hongkong.aliyuncs.com',
            'cn-heyuan-acdr-1': 'emr.cn-heyuan-acdr-1.aliyuncs.com',
            'cn-chengdu': 'emr.cn-chengdu.aliyuncs.com',
            'ap-southeast-5': 'emr.ap-southeast-5.aliyuncs.com',
            'ap-southeast-3': 'emr.ap-southeast-3.aliyuncs.com',
            'ap-northeast-1': 'emr.ap-northeast-1.aliyuncs.com'
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_api_template_with_options(
        self,
        request: main_models.CreateApiTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiTemplate',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_api_template_with_options_async(
        self,
        request: main_models.CreateApiTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateApiTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateApiTemplate',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateApiTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_api_template(
        self,
        request: main_models.CreateApiTemplateRequest,
    ) -> main_models.CreateApiTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_api_template_with_options(request, runtime)

    async def create_api_template_async(
        self,
        request: main_models.CreateApiTemplateRequest,
    ) -> main_models.CreateApiTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_api_template_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        request: main_models.CreateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_configs):
            query['ApplicationConfigs'] = request.application_configs
        if not DaraCore.is_null(request.applications):
            query['Applications'] = request.applications
        if not DaraCore.is_null(request.bootstrap_scripts):
            query['BootstrapScripts'] = request.bootstrap_scripts
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.deploy_mode):
            query['DeployMode'] = request.deploy_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.node_attributes):
            query['NodeAttributes'] = request.node_attributes
        if not DaraCore.is_null(request.node_groups):
            query['NodeGroups'] = request.node_groups
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.release_version):
            query['ReleaseVersion'] = request.release_version
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_mode):
            query['SecurityMode'] = request.security_mode
        if not DaraCore.is_null(request.subscription_config):
            query['SubscriptionConfig'] = request.subscription_config
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCluster',
            version = '2021-03-20',
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
        request: main_models.CreateClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_configs):
            query['ApplicationConfigs'] = request.application_configs
        if not DaraCore.is_null(request.applications):
            query['Applications'] = request.applications
        if not DaraCore.is_null(request.bootstrap_scripts):
            query['BootstrapScripts'] = request.bootstrap_scripts
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.deploy_mode):
            query['DeployMode'] = request.deploy_mode
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.node_attributes):
            query['NodeAttributes'] = request.node_attributes
        if not DaraCore.is_null(request.node_groups):
            query['NodeGroups'] = request.node_groups
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.release_version):
            query['ReleaseVersion'] = request.release_version
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_mode):
            query['SecurityMode'] = request.security_mode
        if not DaraCore.is_null(request.subscription_config):
            query['SubscriptionConfig'] = request.subscription_config
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateCluster',
            version = '2021-03-20',
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

    def create_node_group_with_options(
        self,
        request: main_models.CreateNodeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNodeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_group):
            query['NodeGroup'] = request.node_group
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNodeGroup',
            version = '2021-03-20',
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
        request: main_models.CreateNodeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateNodeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_group):
            query['NodeGroup'] = request.node_group
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateNodeGroup',
            version = '2021-03-20',
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

    def create_script_with_options(
        self,
        request: main_models.CreateScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.script_type):
            query['ScriptType'] = request.script_type
        if not DaraCore.is_null(request.scripts):
            query['Scripts'] = request.scripts
        if not DaraCore.is_null(request.timeout_secs):
            query['TimeoutSecs'] = request.timeout_secs
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScript',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_script_with_options_async(
        self,
        request: main_models.CreateScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.script_type):
            query['ScriptType'] = request.script_type
        if not DaraCore.is_null(request.scripts):
            query['Scripts'] = request.scripts
        if not DaraCore.is_null(request.timeout_secs):
            query['TimeoutSecs'] = request.timeout_secs
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateScript',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_script(
        self,
        request: main_models.CreateScriptRequest,
    ) -> main_models.CreateScriptResponse:
        runtime = RuntimeOptions()
        return self.create_script_with_options(request, runtime)

    async def create_script_async(
        self,
        request: main_models.CreateScriptRequest,
    ) -> main_models.CreateScriptResponse:
        runtime = RuntimeOptions()
        return await self.create_script_with_options_async(request, runtime)

    def create_users_with_options(
        self,
        request: main_models.CreateUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.users):
            query['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUsers',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_users_with_options_async(
        self,
        request: main_models.CreateUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.users):
            query['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateUsers',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_users(
        self,
        request: main_models.CreateUsersRequest,
    ) -> main_models.CreateUsersResponse:
        runtime = RuntimeOptions()
        return self.create_users_with_options(request, runtime)

    async def create_users_async(
        self,
        request: main_models.CreateUsersRequest,
    ) -> main_models.CreateUsersResponse:
        runtime = RuntimeOptions()
        return await self.create_users_with_options_async(request, runtime)

    def decrease_nodes_with_options(
        self,
        request: main_models.DecreaseNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DecreaseNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_interval):
            query['BatchInterval'] = request.batch_interval
        if not DaraCore.is_null(request.batch_size):
            query['BatchSize'] = request.batch_size
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.decrease_node_count):
            query['DecreaseNodeCount'] = request.decrease_node_count
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DecreaseNodes',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DecreaseNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def decrease_nodes_with_options_async(
        self,
        request: main_models.DecreaseNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DecreaseNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_interval):
            query['BatchInterval'] = request.batch_interval
        if not DaraCore.is_null(request.batch_size):
            query['BatchSize'] = request.batch_size
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.decrease_node_count):
            query['DecreaseNodeCount'] = request.decrease_node_count
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DecreaseNodes',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DecreaseNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def decrease_nodes(
        self,
        request: main_models.DecreaseNodesRequest,
    ) -> main_models.DecreaseNodesResponse:
        runtime = RuntimeOptions()
        return self.decrease_nodes_with_options(request, runtime)

    async def decrease_nodes_async(
        self,
        request: main_models.DecreaseNodesRequest,
    ) -> main_models.DecreaseNodesResponse:
        runtime = RuntimeOptions()
        return await self.decrease_nodes_with_options_async(request, runtime)

    def delete_api_template_with_options(
        self,
        request: main_models.DeleteApiTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiTemplate',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_api_template_with_options_async(
        self,
        request: main_models.DeleteApiTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteApiTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteApiTemplate',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteApiTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_api_template(
        self,
        request: main_models.DeleteApiTemplateRequest,
    ) -> main_models.DeleteApiTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_api_template_with_options(request, runtime)

    async def delete_api_template_async(
        self,
        request: main_models.DeleteApiTemplateRequest,
    ) -> main_models.DeleteApiTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_api_template_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: main_models.DeleteClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCluster',
            version = '2021-03-20',
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
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCluster',
            version = '2021-03-20',
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

    def delete_node_group_with_options(
        self,
        request: main_models.DeleteNodeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNodeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNodeGroup',
            version = '2021-03-20',
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
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNodeGroup',
            version = '2021-03-20',
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

    def delete_script_with_options(
        self,
        request: main_models.DeleteScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.script_type):
            query['ScriptType'] = request.script_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScript',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_script_with_options_async(
        self,
        request: main_models.DeleteScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScriptResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.script_type):
            query['ScriptType'] = request.script_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScript',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_script(
        self,
        request: main_models.DeleteScriptRequest,
    ) -> main_models.DeleteScriptResponse:
        runtime = RuntimeOptions()
        return self.delete_script_with_options(request, runtime)

    async def delete_script_async(
        self,
        request: main_models.DeleteScriptRequest,
    ) -> main_models.DeleteScriptResponse:
        runtime = RuntimeOptions()
        return await self.delete_script_with_options_async(request, runtime)

    def delete_users_with_options(
        self,
        tmp_req: main_models.DeleteUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUsersResponse:
        tmp_req.validate()
        request = main_models.DeleteUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_names):
            request.user_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_names, 'UserNames', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.user_names_shrink):
            body['UserNames'] = request.user_names_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUsers',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_users_with_options_async(
        self,
        tmp_req: main_models.DeleteUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteUsersResponse:
        tmp_req.validate()
        request = main_models.DeleteUsersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_names):
            request.user_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_names, 'UserNames', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.user_names_shrink):
            body['UserNames'] = request.user_names_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteUsers',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_users(
        self,
        request: main_models.DeleteUsersRequest,
    ) -> main_models.DeleteUsersResponse:
        runtime = RuntimeOptions()
        return self.delete_users_with_options(request, runtime)

    async def delete_users_async(
        self,
        request: main_models.DeleteUsersRequest,
    ) -> main_models.DeleteUsersResponse:
        runtime = RuntimeOptions()
        return await self.delete_users_with_options_async(request, runtime)

    def export_application_configs_with_options(
        self,
        request: main_models.ExportApplicationConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportApplicationConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_config_files):
            query['ApplicationConfigFiles'] = request.application_config_files
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.config_scope):
            query['ConfigScope'] = request.config_scope
        if not DaraCore.is_null(request.export_mode):
            query['ExportMode'] = request.export_mode
        if not DaraCore.is_null(request.file_format):
            query['FileFormat'] = request.file_format
        if not DaraCore.is_null(request.node_group_ids):
            query['NodeGroupIds'] = request.node_group_ids
        if not DaraCore.is_null(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportApplicationConfigs',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportApplicationConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_application_configs_with_options_async(
        self,
        request: main_models.ExportApplicationConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportApplicationConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_config_files):
            query['ApplicationConfigFiles'] = request.application_config_files
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.config_scope):
            query['ConfigScope'] = request.config_scope
        if not DaraCore.is_null(request.export_mode):
            query['ExportMode'] = request.export_mode
        if not DaraCore.is_null(request.file_format):
            query['FileFormat'] = request.file_format
        if not DaraCore.is_null(request.node_group_ids):
            query['NodeGroupIds'] = request.node_group_ids
        if not DaraCore.is_null(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportApplicationConfigs',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportApplicationConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_application_configs(
        self,
        request: main_models.ExportApplicationConfigsRequest,
    ) -> main_models.ExportApplicationConfigsResponse:
        runtime = RuntimeOptions()
        return self.export_application_configs_with_options(request, runtime)

    async def export_application_configs_async(
        self,
        request: main_models.ExportApplicationConfigsRequest,
    ) -> main_models.ExportApplicationConfigsResponse:
        runtime = RuntimeOptions()
        return await self.export_application_configs_with_options_async(request, runtime)

    def get_api_template_with_options(
        self,
        request: main_models.GetApiTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApiTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApiTemplate',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApiTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_api_template_with_options_async(
        self,
        request: main_models.GetApiTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApiTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApiTemplate',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetApiTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_api_template(
        self,
        request: main_models.GetApiTemplateRequest,
    ) -> main_models.GetApiTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_api_template_with_options(request, runtime)

    async def get_api_template_async(
        self,
        request: main_models.GetApiTemplateRequest,
    ) -> main_models.GetApiTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_api_template_with_options_async(request, runtime)

    def get_application_with_options(
        self,
        request: main_models.GetApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplication',
            version = '2021-03-20',
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
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetApplication',
            version = '2021-03-20',
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

    def get_auto_scaling_activity_with_options(
        self,
        request: main_models.GetAutoScalingActivityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoScalingActivityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoScalingActivity',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoScalingActivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_scaling_activity_with_options_async(
        self,
        request: main_models.GetAutoScalingActivityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoScalingActivityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoScalingActivity',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoScalingActivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_scaling_activity(
        self,
        request: main_models.GetAutoScalingActivityRequest,
    ) -> main_models.GetAutoScalingActivityResponse:
        runtime = RuntimeOptions()
        return self.get_auto_scaling_activity_with_options(request, runtime)

    async def get_auto_scaling_activity_async(
        self,
        request: main_models.GetAutoScalingActivityRequest,
    ) -> main_models.GetAutoScalingActivityResponse:
        runtime = RuntimeOptions()
        return await self.get_auto_scaling_activity_with_options_async(request, runtime)

    def get_auto_scaling_policy_with_options(
        self,
        request: main_models.GetAutoScalingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoScalingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoScalingPolicy',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoScalingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_scaling_policy_with_options_async(
        self,
        request: main_models.GetAutoScalingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAutoScalingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAutoScalingPolicy',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAutoScalingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_scaling_policy(
        self,
        request: main_models.GetAutoScalingPolicyRequest,
    ) -> main_models.GetAutoScalingPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_auto_scaling_policy_with_options(request, runtime)

    async def get_auto_scaling_policy_async(
        self,
        request: main_models.GetAutoScalingPolicyRequest,
    ) -> main_models.GetAutoScalingPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_auto_scaling_policy_with_options_async(request, runtime)

    def get_cluster_with_options(
        self,
        request: main_models.GetClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCluster',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_with_options_async(
        self,
        request: main_models.GetClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCluster',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster(
        self,
        request: main_models.GetClusterRequest,
    ) -> main_models.GetClusterResponse:
        runtime = RuntimeOptions()
        return self.get_cluster_with_options(request, runtime)

    async def get_cluster_async(
        self,
        request: main_models.GetClusterRequest,
    ) -> main_models.GetClusterResponse:
        runtime = RuntimeOptions()
        return await self.get_cluster_with_options_async(request, runtime)

    def get_cluster_clone_meta_with_options(
        self,
        request: main_models.GetClusterCloneMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterCloneMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClusterCloneMeta',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterCloneMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_clone_meta_with_options_async(
        self,
        request: main_models.GetClusterCloneMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterCloneMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetClusterCloneMeta',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterCloneMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_clone_meta(
        self,
        request: main_models.GetClusterCloneMetaRequest,
    ) -> main_models.GetClusterCloneMetaResponse:
        runtime = RuntimeOptions()
        return self.get_cluster_clone_meta_with_options(request, runtime)

    async def get_cluster_clone_meta_async(
        self,
        request: main_models.GetClusterCloneMetaRequest,
    ) -> main_models.GetClusterCloneMetaResponse:
        runtime = RuntimeOptions()
        return await self.get_cluster_clone_meta_with_options_async(request, runtime)

    def get_doctor_application_with_options(
        self,
        request: main_models.GetDoctorApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorApplication',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_application_with_options_async(
        self,
        request: main_models.GetDoctorApplicationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorApplicationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorApplication',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_application(
        self,
        request: main_models.GetDoctorApplicationRequest,
    ) -> main_models.GetDoctorApplicationResponse:
        runtime = RuntimeOptions()
        return self.get_doctor_application_with_options(request, runtime)

    async def get_doctor_application_async(
        self,
        request: main_models.GetDoctorApplicationRequest,
    ) -> main_models.GetDoctorApplicationResponse:
        runtime = RuntimeOptions()
        return await self.get_doctor_application_with_options_async(request, runtime)

    def get_doctor_compute_summary_with_options(
        self,
        request: main_models.GetDoctorComputeSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorComputeSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.component_info):
            query['ComponentInfo'] = request.component_info
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorComputeSummary',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorComputeSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_compute_summary_with_options_async(
        self,
        request: main_models.GetDoctorComputeSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorComputeSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.component_info):
            query['ComponentInfo'] = request.component_info
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorComputeSummary',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorComputeSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_compute_summary(
        self,
        request: main_models.GetDoctorComputeSummaryRequest,
    ) -> main_models.GetDoctorComputeSummaryResponse:
        runtime = RuntimeOptions()
        return self.get_doctor_compute_summary_with_options(request, runtime)

    async def get_doctor_compute_summary_async(
        self,
        request: main_models.GetDoctorComputeSummaryRequest,
    ) -> main_models.GetDoctorComputeSummaryResponse:
        runtime = RuntimeOptions()
        return await self.get_doctor_compute_summary_with_options_async(request, runtime)

    def get_doctor_hbase_cluster_with_options(
        self,
        request: main_models.GetDoctorHBaseClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHBaseClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHBaseCluster',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHBaseClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hbase_cluster_with_options_async(
        self,
        request: main_models.GetDoctorHBaseClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHBaseClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHBaseCluster',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHBaseClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hbase_cluster(
        self,
        request: main_models.GetDoctorHBaseClusterRequest,
    ) -> main_models.GetDoctorHBaseClusterResponse:
        runtime = RuntimeOptions()
        return self.get_doctor_hbase_cluster_with_options(request, runtime)

    async def get_doctor_hbase_cluster_async(
        self,
        request: main_models.GetDoctorHBaseClusterRequest,
    ) -> main_models.GetDoctorHBaseClusterResponse:
        runtime = RuntimeOptions()
        return await self.get_doctor_hbase_cluster_with_options_async(request, runtime)

    def get_doctor_hbase_region_with_options(
        self,
        request: main_models.GetDoctorHBaseRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHBaseRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.hbase_region_id):
            query['HbaseRegionId'] = request.hbase_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHBaseRegion',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHBaseRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hbase_region_with_options_async(
        self,
        request: main_models.GetDoctorHBaseRegionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHBaseRegionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.hbase_region_id):
            query['HbaseRegionId'] = request.hbase_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHBaseRegion',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHBaseRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hbase_region(
        self,
        request: main_models.GetDoctorHBaseRegionRequest,
    ) -> main_models.GetDoctorHBaseRegionResponse:
        runtime = RuntimeOptions()
        return self.get_doctor_hbase_region_with_options(request, runtime)

    async def get_doctor_hbase_region_async(
        self,
        request: main_models.GetDoctorHBaseRegionRequest,
    ) -> main_models.GetDoctorHBaseRegionResponse:
        runtime = RuntimeOptions()
        return await self.get_doctor_hbase_region_with_options_async(request, runtime)

    def get_doctor_hbase_region_server_with_options(
        self,
        request: main_models.GetDoctorHBaseRegionServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHBaseRegionServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_server_host):
            query['RegionServerHost'] = request.region_server_host
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHBaseRegionServer',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHBaseRegionServerResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hbase_region_server_with_options_async(
        self,
        request: main_models.GetDoctorHBaseRegionServerRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHBaseRegionServerResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_server_host):
            query['RegionServerHost'] = request.region_server_host
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHBaseRegionServer',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHBaseRegionServerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hbase_region_server(
        self,
        request: main_models.GetDoctorHBaseRegionServerRequest,
    ) -> main_models.GetDoctorHBaseRegionServerResponse:
        runtime = RuntimeOptions()
        return self.get_doctor_hbase_region_server_with_options(request, runtime)

    async def get_doctor_hbase_region_server_async(
        self,
        request: main_models.GetDoctorHBaseRegionServerRequest,
    ) -> main_models.GetDoctorHBaseRegionServerResponse:
        runtime = RuntimeOptions()
        return await self.get_doctor_hbase_region_server_with_options_async(request, runtime)

    def get_doctor_hbase_table_with_options(
        self,
        request: main_models.GetDoctorHBaseTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHBaseTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHBaseTable',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHBaseTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hbase_table_with_options_async(
        self,
        request: main_models.GetDoctorHBaseTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHBaseTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHBaseTable',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHBaseTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hbase_table(
        self,
        request: main_models.GetDoctorHBaseTableRequest,
    ) -> main_models.GetDoctorHBaseTableResponse:
        runtime = RuntimeOptions()
        return self.get_doctor_hbase_table_with_options(request, runtime)

    async def get_doctor_hbase_table_async(
        self,
        request: main_models.GetDoctorHBaseTableRequest,
    ) -> main_models.GetDoctorHBaseTableResponse:
        runtime = RuntimeOptions()
        return await self.get_doctor_hbase_table_with_options_async(request, runtime)

    def get_doctor_hdfscluster_with_options(
        self,
        request: main_models.GetDoctorHDFSClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHDFSClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHDFSCluster',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHDFSClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hdfscluster_with_options_async(
        self,
        request: main_models.GetDoctorHDFSClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHDFSClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHDFSCluster',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHDFSClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hdfscluster(
        self,
        request: main_models.GetDoctorHDFSClusterRequest,
    ) -> main_models.GetDoctorHDFSClusterResponse:
        runtime = RuntimeOptions()
        return self.get_doctor_hdfscluster_with_options(request, runtime)

    async def get_doctor_hdfscluster_async(
        self,
        request: main_models.GetDoctorHDFSClusterRequest,
    ) -> main_models.GetDoctorHDFSClusterResponse:
        runtime = RuntimeOptions()
        return await self.get_doctor_hdfscluster_with_options_async(request, runtime)

    def get_doctor_hdfsdirectory_with_options(
        self,
        request: main_models.GetDoctorHDFSDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHDFSDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.dir_path):
            query['DirPath'] = request.dir_path
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHDFSDirectory',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHDFSDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hdfsdirectory_with_options_async(
        self,
        request: main_models.GetDoctorHDFSDirectoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHDFSDirectoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.dir_path):
            query['DirPath'] = request.dir_path
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHDFSDirectory',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHDFSDirectoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hdfsdirectory(
        self,
        request: main_models.GetDoctorHDFSDirectoryRequest,
    ) -> main_models.GetDoctorHDFSDirectoryResponse:
        runtime = RuntimeOptions()
        return self.get_doctor_hdfsdirectory_with_options(request, runtime)

    async def get_doctor_hdfsdirectory_async(
        self,
        request: main_models.GetDoctorHDFSDirectoryRequest,
    ) -> main_models.GetDoctorHDFSDirectoryResponse:
        runtime = RuntimeOptions()
        return await self.get_doctor_hdfsdirectory_with_options_async(request, runtime)

    def get_doctor_hive_cluster_with_options(
        self,
        request: main_models.GetDoctorHiveClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHiveClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHiveCluster',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHiveClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hive_cluster_with_options_async(
        self,
        request: main_models.GetDoctorHiveClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHiveClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHiveCluster',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHiveClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hive_cluster(
        self,
        request: main_models.GetDoctorHiveClusterRequest,
    ) -> main_models.GetDoctorHiveClusterResponse:
        runtime = RuntimeOptions()
        return self.get_doctor_hive_cluster_with_options(request, runtime)

    async def get_doctor_hive_cluster_async(
        self,
        request: main_models.GetDoctorHiveClusterRequest,
    ) -> main_models.GetDoctorHiveClusterResponse:
        runtime = RuntimeOptions()
        return await self.get_doctor_hive_cluster_with_options_async(request, runtime)

    def get_doctor_hive_database_with_options(
        self,
        request: main_models.GetDoctorHiveDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHiveDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHiveDatabase',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHiveDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hive_database_with_options_async(
        self,
        request: main_models.GetDoctorHiveDatabaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHiveDatabaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_name):
            query['DatabaseName'] = request.database_name
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHiveDatabase',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHiveDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hive_database(
        self,
        request: main_models.GetDoctorHiveDatabaseRequest,
    ) -> main_models.GetDoctorHiveDatabaseResponse:
        runtime = RuntimeOptions()
        return self.get_doctor_hive_database_with_options(request, runtime)

    async def get_doctor_hive_database_async(
        self,
        request: main_models.GetDoctorHiveDatabaseRequest,
    ) -> main_models.GetDoctorHiveDatabaseResponse:
        runtime = RuntimeOptions()
        return await self.get_doctor_hive_database_with_options_async(request, runtime)

    def get_doctor_hive_table_with_options(
        self,
        request: main_models.GetDoctorHiveTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHiveTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHiveTable',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHiveTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_hive_table_with_options_async(
        self,
        request: main_models.GetDoctorHiveTableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorHiveTableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorHiveTable',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorHiveTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_hive_table(
        self,
        request: main_models.GetDoctorHiveTableRequest,
    ) -> main_models.GetDoctorHiveTableResponse:
        runtime = RuntimeOptions()
        return self.get_doctor_hive_table_with_options(request, runtime)

    async def get_doctor_hive_table_async(
        self,
        request: main_models.GetDoctorHiveTableRequest,
    ) -> main_models.GetDoctorHiveTableResponse:
        runtime = RuntimeOptions()
        return await self.get_doctor_hive_table_with_options_async(request, runtime)

    def get_doctor_job_with_options(
        self,
        request: main_models.GetDoctorJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorJob',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_job_with_options_async(
        self,
        request: main_models.GetDoctorJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorJob',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_job(
        self,
        request: main_models.GetDoctorJobRequest,
    ) -> main_models.GetDoctorJobResponse:
        runtime = RuntimeOptions()
        return self.get_doctor_job_with_options(request, runtime)

    async def get_doctor_job_async(
        self,
        request: main_models.GetDoctorJobRequest,
    ) -> main_models.GetDoctorJobResponse:
        runtime = RuntimeOptions()
        return await self.get_doctor_job_with_options_async(request, runtime)

    def get_doctor_report_component_summary_with_options(
        self,
        request: main_models.GetDoctorReportComponentSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorReportComponentSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.component_type):
            query['ComponentType'] = request.component_type
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorReportComponentSummary',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorReportComponentSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_doctor_report_component_summary_with_options_async(
        self,
        request: main_models.GetDoctorReportComponentSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDoctorReportComponentSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.component_type):
            query['ComponentType'] = request.component_type
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDoctorReportComponentSummary',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDoctorReportComponentSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_doctor_report_component_summary(
        self,
        request: main_models.GetDoctorReportComponentSummaryRequest,
    ) -> main_models.GetDoctorReportComponentSummaryResponse:
        runtime = RuntimeOptions()
        return self.get_doctor_report_component_summary_with_options(request, runtime)

    async def get_doctor_report_component_summary_async(
        self,
        request: main_models.GetDoctorReportComponentSummaryRequest,
    ) -> main_models.GetDoctorReportComponentSummaryResponse:
        runtime = RuntimeOptions()
        return await self.get_doctor_report_component_summary_with_options_async(request, runtime)

    def get_managed_scaling_policy_with_options(
        self,
        request: main_models.GetManagedScalingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetManagedScalingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetManagedScalingPolicy',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetManagedScalingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_managed_scaling_policy_with_options_async(
        self,
        request: main_models.GetManagedScalingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetManagedScalingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetManagedScalingPolicy',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetManagedScalingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_managed_scaling_policy(
        self,
        request: main_models.GetManagedScalingPolicyRequest,
    ) -> main_models.GetManagedScalingPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_managed_scaling_policy_with_options(request, runtime)

    async def get_managed_scaling_policy_async(
        self,
        request: main_models.GetManagedScalingPolicyRequest,
    ) -> main_models.GetManagedScalingPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_managed_scaling_policy_with_options_async(request, runtime)

    def get_node_group_with_options(
        self,
        request: main_models.GetNodeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNodeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNodeGroup',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_node_group_with_options_async(
        self,
        request: main_models.GetNodeGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNodeGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetNodeGroup',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_node_group(
        self,
        request: main_models.GetNodeGroupRequest,
    ) -> main_models.GetNodeGroupResponse:
        runtime = RuntimeOptions()
        return self.get_node_group_with_options(request, runtime)

    async def get_node_group_async(
        self,
        request: main_models.GetNodeGroupRequest,
    ) -> main_models.GetNodeGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_node_group_with_options_async(request, runtime)

    def get_operation_with_options(
        self,
        request: main_models.GetOperationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOperationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.operation_id):
            query['OperationId'] = request.operation_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOperation',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_operation_with_options_async(
        self,
        request: main_models.GetOperationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOperationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.operation_id):
            query['OperationId'] = request.operation_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOperation',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_operation(
        self,
        request: main_models.GetOperationRequest,
    ) -> main_models.GetOperationResponse:
        runtime = RuntimeOptions()
        return self.get_operation_with_options(request, runtime)

    async def get_operation_async(
        self,
        request: main_models.GetOperationRequest,
    ) -> main_models.GetOperationResponse:
        runtime = RuntimeOptions()
        return await self.get_operation_with_options_async(request, runtime)

    def increase_nodes_with_options(
        self,
        request: main_models.IncreaseNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IncreaseNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_configs):
            query['ApplicationConfigs'] = request.application_configs
        if not DaraCore.is_null(request.auto_pay_order):
            query['AutoPayOrder'] = request.auto_pay_order
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.increase_node_count):
            query['IncreaseNodeCount'] = request.increase_node_count
        if not DaraCore.is_null(request.min_increase_node_count):
            query['MinIncreaseNodeCount'] = request.min_increase_node_count
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.payment_duration):
            query['PaymentDuration'] = request.payment_duration
        if not DaraCore.is_null(request.payment_duration_unit):
            query['PaymentDurationUnit'] = request.payment_duration_unit
        if not DaraCore.is_null(request.promotions):
            query['Promotions'] = request.promotions
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IncreaseNodes',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IncreaseNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def increase_nodes_with_options_async(
        self,
        request: main_models.IncreaseNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.IncreaseNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_configs):
            query['ApplicationConfigs'] = request.application_configs
        if not DaraCore.is_null(request.auto_pay_order):
            query['AutoPayOrder'] = request.auto_pay_order
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.increase_node_count):
            query['IncreaseNodeCount'] = request.increase_node_count
        if not DaraCore.is_null(request.min_increase_node_count):
            query['MinIncreaseNodeCount'] = request.min_increase_node_count
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.payment_duration):
            query['PaymentDuration'] = request.payment_duration
        if not DaraCore.is_null(request.payment_duration_unit):
            query['PaymentDurationUnit'] = request.payment_duration_unit
        if not DaraCore.is_null(request.promotions):
            query['Promotions'] = request.promotions
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'IncreaseNodes',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.IncreaseNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def increase_nodes(
        self,
        request: main_models.IncreaseNodesRequest,
    ) -> main_models.IncreaseNodesResponse:
        runtime = RuntimeOptions()
        return self.increase_nodes_with_options(request, runtime)

    async def increase_nodes_async(
        self,
        request: main_models.IncreaseNodesRequest,
    ) -> main_models.IncreaseNodesResponse:
        runtime = RuntimeOptions()
        return await self.increase_nodes_with_options_async(request, runtime)

    def join_resource_group_with_options(
        self,
        request: main_models.JoinResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.JoinResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'JoinResourceGroup',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.JoinResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_resource_group_with_options_async(
        self,
        request: main_models.JoinResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.JoinResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'JoinResourceGroup',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.JoinResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def join_resource_group(
        self,
        request: main_models.JoinResourceGroupRequest,
    ) -> main_models.JoinResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.join_resource_group_with_options(request, runtime)

    async def join_resource_group_async(
        self,
        request: main_models.JoinResourceGroupRequest,
    ) -> main_models.JoinResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.join_resource_group_with_options_async(request, runtime)

    def list_api_templates_with_options(
        self,
        request: main_models.ListApiTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApiTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiTemplates',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_api_templates_with_options_async(
        self,
        request: main_models.ListApiTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApiTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApiTemplates',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApiTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_api_templates(
        self,
        request: main_models.ListApiTemplatesRequest,
    ) -> main_models.ListApiTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_api_templates_with_options(request, runtime)

    async def list_api_templates_async(
        self,
        request: main_models.ListApiTemplatesRequest,
    ) -> main_models.ListApiTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_api_templates_with_options_async(request, runtime)

    def list_application_configs_with_options(
        self,
        request: main_models.ListApplicationConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.config_file_name):
            query['ConfigFileName'] = request.config_file_name
        if not DaraCore.is_null(request.config_item_key):
            query['ConfigItemKey'] = request.config_item_key
        if not DaraCore.is_null(request.config_item_value):
            query['ConfigItemValue'] = request.config_item_value
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationConfigs',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_configs_with_options_async(
        self,
        request: main_models.ListApplicationConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.config_file_name):
            query['ConfigFileName'] = request.config_file_name
        if not DaraCore.is_null(request.config_item_key):
            query['ConfigItemKey'] = request.config_item_key
        if not DaraCore.is_null(request.config_item_value):
            query['ConfigItemValue'] = request.config_item_value
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListApplicationConfigs',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListApplicationConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_configs(
        self,
        request: main_models.ListApplicationConfigsRequest,
    ) -> main_models.ListApplicationConfigsResponse:
        runtime = RuntimeOptions()
        return self.list_application_configs_with_options(request, runtime)

    async def list_application_configs_async(
        self,
        request: main_models.ListApplicationConfigsRequest,
    ) -> main_models.ListApplicationConfigsResponse:
        runtime = RuntimeOptions()
        return await self.list_application_configs_with_options_async(request, runtime)

    def list_applications_with_options(
        self,
        request: main_models.ListApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_names):
            query['ApplicationNames'] = request.application_names
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
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
            action = 'ListApplications',
            version = '2021-03-20',
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
        request: main_models.ListApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_names):
            query['ApplicationNames'] = request.application_names
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
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
            action = 'ListApplications',
            version = '2021-03-20',
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

    def list_auto_scaling_activities_with_options(
        self,
        request: main_models.ListAutoScalingActivitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAutoScalingActivitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_charge_types):
            query['InstanceChargeTypes'] = request.instance_charge_types
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scaling_activity_states):
            query['ScalingActivityStates'] = request.scaling_activity_states
        if not DaraCore.is_null(request.scaling_activity_type):
            query['ScalingActivityType'] = request.scaling_activity_type
        if not DaraCore.is_null(request.scaling_policy_type):
            query['ScalingPolicyType'] = request.scaling_policy_type
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAutoScalingActivities',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAutoScalingActivitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_auto_scaling_activities_with_options_async(
        self,
        request: main_models.ListAutoScalingActivitiesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAutoScalingActivitiesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.instance_charge_types):
            query['InstanceChargeTypes'] = request.instance_charge_types
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scaling_activity_states):
            query['ScalingActivityStates'] = request.scaling_activity_states
        if not DaraCore.is_null(request.scaling_activity_type):
            query['ScalingActivityType'] = request.scaling_activity_type
        if not DaraCore.is_null(request.scaling_policy_type):
            query['ScalingPolicyType'] = request.scaling_policy_type
        if not DaraCore.is_null(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAutoScalingActivities',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAutoScalingActivitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_auto_scaling_activities(
        self,
        request: main_models.ListAutoScalingActivitiesRequest,
    ) -> main_models.ListAutoScalingActivitiesResponse:
        runtime = RuntimeOptions()
        return self.list_auto_scaling_activities_with_options(request, runtime)

    async def list_auto_scaling_activities_async(
        self,
        request: main_models.ListAutoScalingActivitiesRequest,
    ) -> main_models.ListAutoScalingActivitiesResponse:
        runtime = RuntimeOptions()
        return await self.list_auto_scaling_activities_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: main_models.ListClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_states):
            query['ClusterStates'] = request.cluster_states
        if not DaraCore.is_null(request.cluster_types):
            query['ClusterTypes'] = request.cluster_types
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.payment_types):
            query['PaymentTypes'] = request.payment_types
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
            action = 'ListClusters',
            version = '2021-03-20',
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
        if not DaraCore.is_null(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_states):
            query['ClusterStates'] = request.cluster_states
        if not DaraCore.is_null(request.cluster_types):
            query['ClusterTypes'] = request.cluster_types
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.payment_types):
            query['PaymentTypes'] = request.payment_types
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
            action = 'ListClusters',
            version = '2021-03-20',
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

    def list_component_instances_with_options(
        self,
        request: main_models.ListComponentInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_names):
            query['ApplicationNames'] = request.application_names
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.component_names):
            query['ComponentNames'] = request.component_names
        if not DaraCore.is_null(request.component_states):
            query['ComponentStates'] = request.component_states
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.node_names):
            query['NodeNames'] = request.node_names
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComponentInstances',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_component_instances_with_options_async(
        self,
        request: main_models.ListComponentInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_names):
            query['ApplicationNames'] = request.application_names
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.component_names):
            query['ComponentNames'] = request.component_names
        if not DaraCore.is_null(request.component_states):
            query['ComponentStates'] = request.component_states
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.node_names):
            query['NodeNames'] = request.node_names
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComponentInstances',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_component_instances(
        self,
        request: main_models.ListComponentInstancesRequest,
    ) -> main_models.ListComponentInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_component_instances_with_options(request, runtime)

    async def list_component_instances_async(
        self,
        request: main_models.ListComponentInstancesRequest,
    ) -> main_models.ListComponentInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_component_instances_with_options_async(request, runtime)

    def list_components_with_options(
        self,
        request: main_models.ListComponentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_names):
            query['ApplicationNames'] = request.application_names
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.component_names):
            query['ComponentNames'] = request.component_names
        if not DaraCore.is_null(request.component_states):
            query['ComponentStates'] = request.component_states
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
            action = 'ListComponents',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_components_with_options_async(
        self,
        request: main_models.ListComponentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_names):
            query['ApplicationNames'] = request.application_names
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.component_names):
            query['ComponentNames'] = request.component_names
        if not DaraCore.is_null(request.component_states):
            query['ComponentStates'] = request.component_states
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
            action = 'ListComponents',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_components(
        self,
        request: main_models.ListComponentsRequest,
    ) -> main_models.ListComponentsResponse:
        runtime = RuntimeOptions()
        return self.list_components_with_options(request, runtime)

    async def list_components_async(
        self,
        request: main_models.ListComponentsRequest,
    ) -> main_models.ListComponentsResponse:
        runtime = RuntimeOptions()
        return await self.list_components_with_options_async(request, runtime)

    def list_doctor_applications_with_options(
        self,
        request: main_models.ListDoctorApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.queues):
            query['Queues'] = request.queues
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.types):
            query['Types'] = request.types
        if not DaraCore.is_null(request.users):
            query['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorApplications',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_applications_with_options_async(
        self,
        request: main_models.ListDoctorApplicationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorApplicationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.queues):
            query['Queues'] = request.queues
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.types):
            query['Types'] = request.types
        if not DaraCore.is_null(request.users):
            query['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorApplications',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_applications(
        self,
        request: main_models.ListDoctorApplicationsRequest,
    ) -> main_models.ListDoctorApplicationsResponse:
        runtime = RuntimeOptions()
        return self.list_doctor_applications_with_options(request, runtime)

    async def list_doctor_applications_async(
        self,
        request: main_models.ListDoctorApplicationsRequest,
    ) -> main_models.ListDoctorApplicationsResponse:
        runtime = RuntimeOptions()
        return await self.list_doctor_applications_with_options_async(request, runtime)

    def list_doctor_compute_summary_with_options(
        self,
        request: main_models.ListDoctorComputeSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorComputeSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.component_types):
            query['ComponentTypes'] = request.component_types
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorComputeSummary',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorComputeSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_compute_summary_with_options_async(
        self,
        request: main_models.ListDoctorComputeSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorComputeSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.component_types):
            query['ComponentTypes'] = request.component_types
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorComputeSummary',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorComputeSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_compute_summary(
        self,
        request: main_models.ListDoctorComputeSummaryRequest,
    ) -> main_models.ListDoctorComputeSummaryResponse:
        runtime = RuntimeOptions()
        return self.list_doctor_compute_summary_with_options(request, runtime)

    async def list_doctor_compute_summary_async(
        self,
        request: main_models.ListDoctorComputeSummaryRequest,
    ) -> main_models.ListDoctorComputeSummaryResponse:
        runtime = RuntimeOptions()
        return await self.list_doctor_compute_summary_with_options_async(request, runtime)

    def list_doctor_hbase_region_servers_with_options(
        self,
        request: main_models.ListDoctorHBaseRegionServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorHBaseRegionServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_server_hosts):
            query['RegionServerHosts'] = request.region_server_hosts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorHBaseRegionServers',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorHBaseRegionServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_hbase_region_servers_with_options_async(
        self,
        request: main_models.ListDoctorHBaseRegionServersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorHBaseRegionServersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_server_hosts):
            query['RegionServerHosts'] = request.region_server_hosts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorHBaseRegionServers',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorHBaseRegionServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_hbase_region_servers(
        self,
        request: main_models.ListDoctorHBaseRegionServersRequest,
    ) -> main_models.ListDoctorHBaseRegionServersResponse:
        runtime = RuntimeOptions()
        return self.list_doctor_hbase_region_servers_with_options(request, runtime)

    async def list_doctor_hbase_region_servers_async(
        self,
        request: main_models.ListDoctorHBaseRegionServersRequest,
    ) -> main_models.ListDoctorHBaseRegionServersResponse:
        runtime = RuntimeOptions()
        return await self.list_doctor_hbase_region_servers_with_options_async(request, runtime)

    def list_doctor_hbase_tables_with_options(
        self,
        request: main_models.ListDoctorHBaseTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorHBaseTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_names):
            query['TableNames'] = request.table_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorHBaseTables',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorHBaseTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_hbase_tables_with_options_async(
        self,
        request: main_models.ListDoctorHBaseTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorHBaseTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_names):
            query['TableNames'] = request.table_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorHBaseTables',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorHBaseTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_hbase_tables(
        self,
        request: main_models.ListDoctorHBaseTablesRequest,
    ) -> main_models.ListDoctorHBaseTablesResponse:
        runtime = RuntimeOptions()
        return self.list_doctor_hbase_tables_with_options(request, runtime)

    async def list_doctor_hbase_tables_async(
        self,
        request: main_models.ListDoctorHBaseTablesRequest,
    ) -> main_models.ListDoctorHBaseTablesResponse:
        runtime = RuntimeOptions()
        return await self.list_doctor_hbase_tables_with_options_async(request, runtime)

    def list_doctor_hdfsdirectories_with_options(
        self,
        request: main_models.ListDoctorHDFSDirectoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorHDFSDirectoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.dir_path):
            query['DirPath'] = request.dir_path
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorHDFSDirectories',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorHDFSDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_hdfsdirectories_with_options_async(
        self,
        request: main_models.ListDoctorHDFSDirectoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorHDFSDirectoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.dir_path):
            query['DirPath'] = request.dir_path
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorHDFSDirectories',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorHDFSDirectoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_hdfsdirectories(
        self,
        request: main_models.ListDoctorHDFSDirectoriesRequest,
    ) -> main_models.ListDoctorHDFSDirectoriesResponse:
        runtime = RuntimeOptions()
        return self.list_doctor_hdfsdirectories_with_options(request, runtime)

    async def list_doctor_hdfsdirectories_async(
        self,
        request: main_models.ListDoctorHDFSDirectoriesRequest,
    ) -> main_models.ListDoctorHDFSDirectoriesResponse:
        runtime = RuntimeOptions()
        return await self.list_doctor_hdfsdirectories_with_options_async(request, runtime)

    def list_doctor_hdfsugiwith_options(
        self,
        request: main_models.ListDoctorHDFSUGIRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorHDFSUGIResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorHDFSUGI',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorHDFSUGIResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_hdfsugiwith_options_async(
        self,
        request: main_models.ListDoctorHDFSUGIRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorHDFSUGIResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorHDFSUGI',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorHDFSUGIResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_hdfsugi(
        self,
        request: main_models.ListDoctorHDFSUGIRequest,
    ) -> main_models.ListDoctorHDFSUGIResponse:
        runtime = RuntimeOptions()
        return self.list_doctor_hdfsugiwith_options(request, runtime)

    async def list_doctor_hdfsugi_async(
        self,
        request: main_models.ListDoctorHDFSUGIRequest,
    ) -> main_models.ListDoctorHDFSUGIResponse:
        runtime = RuntimeOptions()
        return await self.list_doctor_hdfsugiwith_options_async(request, runtime)

    def list_doctor_hive_databases_with_options(
        self,
        request: main_models.ListDoctorHiveDatabasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorHiveDatabasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_names):
            query['DatabaseNames'] = request.database_names
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorHiveDatabases',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorHiveDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_hive_databases_with_options_async(
        self,
        request: main_models.ListDoctorHiveDatabasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorHiveDatabasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.database_names):
            query['DatabaseNames'] = request.database_names
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorHiveDatabases',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorHiveDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_hive_databases(
        self,
        request: main_models.ListDoctorHiveDatabasesRequest,
    ) -> main_models.ListDoctorHiveDatabasesResponse:
        runtime = RuntimeOptions()
        return self.list_doctor_hive_databases_with_options(request, runtime)

    async def list_doctor_hive_databases_async(
        self,
        request: main_models.ListDoctorHiveDatabasesRequest,
    ) -> main_models.ListDoctorHiveDatabasesResponse:
        runtime = RuntimeOptions()
        return await self.list_doctor_hive_databases_with_options_async(request, runtime)

    def list_doctor_hive_tables_with_options(
        self,
        request: main_models.ListDoctorHiveTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorHiveTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_names):
            query['TableNames'] = request.table_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorHiveTables',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorHiveTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_hive_tables_with_options_async(
        self,
        request: main_models.ListDoctorHiveTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorHiveTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.date_time):
            query['DateTime'] = request.date_time
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.table_names):
            query['TableNames'] = request.table_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorHiveTables',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorHiveTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_hive_tables(
        self,
        request: main_models.ListDoctorHiveTablesRequest,
    ) -> main_models.ListDoctorHiveTablesResponse:
        runtime = RuntimeOptions()
        return self.list_doctor_hive_tables_with_options(request, runtime)

    async def list_doctor_hive_tables_async(
        self,
        request: main_models.ListDoctorHiveTablesRequest,
    ) -> main_models.ListDoctorHiveTablesResponse:
        runtime = RuntimeOptions()
        return await self.list_doctor_hive_tables_with_options_async(request, runtime)

    def list_doctor_jobs_with_options(
        self,
        request: main_models.ListDoctorJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_range):
            query['EndRange'] = request.end_range
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.queues):
            query['Queues'] = request.queues
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_range):
            query['StartRange'] = request.start_range
        if not DaraCore.is_null(request.types):
            query['Types'] = request.types
        if not DaraCore.is_null(request.users):
            query['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorJobs',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_jobs_with_options_async(
        self,
        request: main_models.ListDoctorJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_range):
            query['EndRange'] = request.end_range
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.queues):
            query['Queues'] = request.queues
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_range):
            query['StartRange'] = request.start_range
        if not DaraCore.is_null(request.types):
            query['Types'] = request.types
        if not DaraCore.is_null(request.users):
            query['Users'] = request.users
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorJobs',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_jobs(
        self,
        request: main_models.ListDoctorJobsRequest,
    ) -> main_models.ListDoctorJobsResponse:
        runtime = RuntimeOptions()
        return self.list_doctor_jobs_with_options(request, runtime)

    async def list_doctor_jobs_async(
        self,
        request: main_models.ListDoctorJobsRequest,
    ) -> main_models.ListDoctorJobsResponse:
        runtime = RuntimeOptions()
        return await self.list_doctor_jobs_with_options_async(request, runtime)

    def list_doctor_jobs_stats_with_options(
        self,
        request: main_models.ListDoctorJobsStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorJobsStatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_range):
            query['EndRange'] = request.end_range
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_range):
            query['StartRange'] = request.start_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorJobsStats',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorJobsStatsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_jobs_stats_with_options_async(
        self,
        request: main_models.ListDoctorJobsStatsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorJobsStatsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.end_range):
            query['EndRange'] = request.end_range
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_range):
            query['StartRange'] = request.start_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDoctorJobsStats',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorJobsStatsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_jobs_stats(
        self,
        request: main_models.ListDoctorJobsStatsRequest,
    ) -> main_models.ListDoctorJobsStatsResponse:
        runtime = RuntimeOptions()
        return self.list_doctor_jobs_stats_with_options(request, runtime)

    async def list_doctor_jobs_stats_async(
        self,
        request: main_models.ListDoctorJobsStatsRequest,
    ) -> main_models.ListDoctorJobsStatsResponse:
        runtime = RuntimeOptions()
        return await self.list_doctor_jobs_stats_with_options_async(request, runtime)

    def list_doctor_reports_with_options(
        self,
        request: main_models.ListDoctorReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
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
            action = 'ListDoctorReports',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_doctor_reports_with_options_async(
        self,
        request: main_models.ListDoctorReportsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDoctorReportsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
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
            action = 'ListDoctorReports',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDoctorReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_doctor_reports(
        self,
        request: main_models.ListDoctorReportsRequest,
    ) -> main_models.ListDoctorReportsResponse:
        runtime = RuntimeOptions()
        return self.list_doctor_reports_with_options(request, runtime)

    async def list_doctor_reports_async(
        self,
        request: main_models.ListDoctorReportsRequest,
    ) -> main_models.ListDoctorReportsResponse:
        runtime = RuntimeOptions()
        return await self.list_doctor_reports_with_options_async(request, runtime)

    def list_instance_types_with_options(
        self,
        request: main_models.ListInstanceTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.deploy_mode):
            query['DeployMode'] = request.deploy_mode
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.is_modification):
            query['IsModification'] = request.is_modification
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.node_group_type):
            query['NodeGroupType'] = request.node_group_type
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.release_version):
            query['ReleaseVersion'] = request.release_version
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceTypes',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_instance_types_with_options_async(
        self,
        request: main_models.ListInstanceTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInstanceTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.deploy_mode):
            query['DeployMode'] = request.deploy_mode
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.is_modification):
            query['IsModification'] = request.is_modification
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.node_group_type):
            query['NodeGroupType'] = request.node_group_type
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.release_version):
            query['ReleaseVersion'] = request.release_version
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListInstanceTypes',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInstanceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_instance_types(
        self,
        request: main_models.ListInstanceTypesRequest,
    ) -> main_models.ListInstanceTypesResponse:
        runtime = RuntimeOptions()
        return self.list_instance_types_with_options(request, runtime)

    async def list_instance_types_async(
        self,
        request: main_models.ListInstanceTypesRequest,
    ) -> main_models.ListInstanceTypesResponse:
        runtime = RuntimeOptions()
        return await self.list_instance_types_with_options_async(request, runtime)

    def list_node_groups_with_options(
        self,
        request: main_models.ListNodeGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodeGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_group_ids):
            query['NodeGroupIds'] = request.node_group_ids
        if not DaraCore.is_null(request.node_group_names):
            query['NodeGroupNames'] = request.node_group_names
        if not DaraCore.is_null(request.node_group_states):
            query['NodeGroupStates'] = request.node_group_states
        if not DaraCore.is_null(request.node_group_types):
            query['NodeGroupTypes'] = request.node_group_types
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodeGroups',
            version = '2021-03-20',
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
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_group_ids):
            query['NodeGroupIds'] = request.node_group_ids
        if not DaraCore.is_null(request.node_group_names):
            query['NodeGroupNames'] = request.node_group_names
        if not DaraCore.is_null(request.node_group_states):
            query['NodeGroupStates'] = request.node_group_states
        if not DaraCore.is_null(request.node_group_types):
            query['NodeGroupTypes'] = request.node_group_types
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodeGroups',
            version = '2021-03-20',
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

    def list_nodes_with_options(
        self,
        request: main_models.ListNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_group_ids):
            query['NodeGroupIds'] = request.node_group_ids
        if not DaraCore.is_null(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.node_names):
            query['NodeNames'] = request.node_names
        if not DaraCore.is_null(request.node_states):
            query['NodeStates'] = request.node_states
        if not DaraCore.is_null(request.private_ips):
            query['PrivateIps'] = request.private_ips
        if not DaraCore.is_null(request.public_ips):
            query['PublicIps'] = request.public_ips
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodes',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        request: main_models.ListNodesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNodesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.node_group_ids):
            query['NodeGroupIds'] = request.node_group_ids
        if not DaraCore.is_null(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not DaraCore.is_null(request.node_names):
            query['NodeNames'] = request.node_names
        if not DaraCore.is_null(request.node_states):
            query['NodeStates'] = request.node_states
        if not DaraCore.is_null(request.private_ips):
            query['PrivateIps'] = request.private_ips
        if not DaraCore.is_null(request.public_ips):
            query['PublicIps'] = request.public_ips
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNodes',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: main_models.ListNodesRequest,
    ) -> main_models.ListNodesResponse:
        runtime = RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: main_models.ListNodesRequest,
    ) -> main_models.ListNodesResponse:
        runtime = RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)

    def list_release_versions_with_options(
        self,
        request: main_models.ListReleaseVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListReleaseVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.iaas_type):
            query['IaasType'] = request.iaas_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListReleaseVersions',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReleaseVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_release_versions_with_options_async(
        self,
        request: main_models.ListReleaseVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListReleaseVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.iaas_type):
            query['IaasType'] = request.iaas_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListReleaseVersions',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReleaseVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_release_versions(
        self,
        request: main_models.ListReleaseVersionsRequest,
    ) -> main_models.ListReleaseVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_release_versions_with_options(request, runtime)

    async def list_release_versions_async(
        self,
        request: main_models.ListReleaseVersionsRequest,
    ) -> main_models.ListReleaseVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_release_versions_with_options_async(request, runtime)

    def list_scripts_with_options(
        self,
        request: main_models.ListScriptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScriptsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.script_name):
            query['ScriptName'] = request.script_name
        if not DaraCore.is_null(request.script_type):
            query['ScriptType'] = request.script_type
        if not DaraCore.is_null(request.statuses):
            query['Statuses'] = request.statuses
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScripts',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scripts_with_options_async(
        self,
        request: main_models.ListScriptsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScriptsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.script_name):
            query['ScriptName'] = request.script_name
        if not DaraCore.is_null(request.script_type):
            query['ScriptType'] = request.script_type
        if not DaraCore.is_null(request.statuses):
            query['Statuses'] = request.statuses
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScripts',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scripts(
        self,
        request: main_models.ListScriptsRequest,
    ) -> main_models.ListScriptsResponse:
        runtime = RuntimeOptions()
        return self.list_scripts_with_options(request, runtime)

    async def list_scripts_async(
        self,
        request: main_models.ListScriptsRequest,
    ) -> main_models.ListScriptsResponse:
        runtime = RuntimeOptions()
        return await self.list_scripts_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2021-03-20',
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
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2021-03-20',
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

    def list_users_with_options(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_names):
            query['UserNames'] = request.user_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: main_models.ListUsersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        if not DaraCore.is_null(request.user_names):
            query['UserNames'] = request.user_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def put_auto_scaling_policy_with_options(
        self,
        request: main_models.PutAutoScalingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutAutoScalingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.constraints):
            query['Constraints'] = request.constraints
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scaling_rules):
            query['ScalingRules'] = request.scaling_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutAutoScalingPolicy',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutAutoScalingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_auto_scaling_policy_with_options_async(
        self,
        request: main_models.PutAutoScalingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutAutoScalingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.constraints):
            query['Constraints'] = request.constraints
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scaling_rules):
            query['ScalingRules'] = request.scaling_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutAutoScalingPolicy',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutAutoScalingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_auto_scaling_policy(
        self,
        request: main_models.PutAutoScalingPolicyRequest,
    ) -> main_models.PutAutoScalingPolicyResponse:
        runtime = RuntimeOptions()
        return self.put_auto_scaling_policy_with_options(request, runtime)

    async def put_auto_scaling_policy_async(
        self,
        request: main_models.PutAutoScalingPolicyRequest,
    ) -> main_models.PutAutoScalingPolicyResponse:
        runtime = RuntimeOptions()
        return await self.put_auto_scaling_policy_with_options_async(request, runtime)

    def put_managed_scaling_policy_with_options(
        self,
        request: main_models.PutManagedScalingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutManagedScalingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.constraints):
            query['Constraints'] = request.constraints
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutManagedScalingPolicy',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutManagedScalingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_managed_scaling_policy_with_options_async(
        self,
        request: main_models.PutManagedScalingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutManagedScalingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.constraints):
            query['Constraints'] = request.constraints
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutManagedScalingPolicy',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutManagedScalingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_managed_scaling_policy(
        self,
        request: main_models.PutManagedScalingPolicyRequest,
    ) -> main_models.PutManagedScalingPolicyResponse:
        runtime = RuntimeOptions()
        return self.put_managed_scaling_policy_with_options(request, runtime)

    async def put_managed_scaling_policy_async(
        self,
        request: main_models.PutManagedScalingPolicyRequest,
    ) -> main_models.PutManagedScalingPolicyResponse:
        runtime = RuntimeOptions()
        return await self.put_managed_scaling_policy_with_options_async(request, runtime)

    def remove_auto_scaling_policy_with_options(
        self,
        request: main_models.RemoveAutoScalingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAutoScalingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveAutoScalingPolicy',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAutoScalingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_auto_scaling_policy_with_options_async(
        self,
        request: main_models.RemoveAutoScalingPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAutoScalingPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveAutoScalingPolicy',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAutoScalingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_auto_scaling_policy(
        self,
        request: main_models.RemoveAutoScalingPolicyRequest,
    ) -> main_models.RemoveAutoScalingPolicyResponse:
        runtime = RuntimeOptions()
        return self.remove_auto_scaling_policy_with_options(request, runtime)

    async def remove_auto_scaling_policy_async(
        self,
        request: main_models.RemoveAutoScalingPolicyRequest,
    ) -> main_models.RemoveAutoScalingPolicyResponse:
        runtime = RuntimeOptions()
        return await self.remove_auto_scaling_policy_with_options_async(request, runtime)

    def run_api_template_with_options(
        self,
        request: main_models.RunApiTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunApiTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunApiTemplate',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunApiTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_api_template_with_options_async(
        self,
        request: main_models.RunApiTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunApiTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunApiTemplate',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunApiTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_api_template(
        self,
        request: main_models.RunApiTemplateRequest,
    ) -> main_models.RunApiTemplateResponse:
        runtime = RuntimeOptions()
        return self.run_api_template_with_options(request, runtime)

    async def run_api_template_async(
        self,
        request: main_models.RunApiTemplateRequest,
    ) -> main_models.RunApiTemplateResponse:
        runtime = RuntimeOptions()
        return await self.run_api_template_with_options_async(request, runtime)

    def run_application_action_with_options(
        self,
        request: main_models.RunApplicationActionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunApplicationActionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_name):
            query['ActionName'] = request.action_name
        if not DaraCore.is_null(request.batch_size):
            query['BatchSize'] = request.batch_size
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.component_instance_selector):
            query['ComponentInstanceSelector'] = request.component_instance_selector
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execute_strategy):
            query['ExecuteStrategy'] = request.execute_strategy
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rolling_execute):
            query['RollingExecute'] = request.rolling_execute
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunApplicationAction',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunApplicationActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_application_action_with_options_async(
        self,
        request: main_models.RunApplicationActionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunApplicationActionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action_name):
            query['ActionName'] = request.action_name
        if not DaraCore.is_null(request.batch_size):
            query['BatchSize'] = request.batch_size
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.component_instance_selector):
            query['ComponentInstanceSelector'] = request.component_instance_selector
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execute_strategy):
            query['ExecuteStrategy'] = request.execute_strategy
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rolling_execute):
            query['RollingExecute'] = request.rolling_execute
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunApplicationAction',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunApplicationActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_application_action(
        self,
        request: main_models.RunApplicationActionRequest,
    ) -> main_models.RunApplicationActionResponse:
        runtime = RuntimeOptions()
        return self.run_application_action_with_options(request, runtime)

    async def run_application_action_async(
        self,
        request: main_models.RunApplicationActionRequest,
    ) -> main_models.RunApplicationActionResponse:
        runtime = RuntimeOptions()
        return await self.run_application_action_with_options_async(request, runtime)

    def run_cluster_with_options(
        self,
        tmp_req: main_models.RunClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunClusterResponse:
        tmp_req.validate()
        request = main_models.RunClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.application_configs):
            request.application_configs_shrink = Utils.array_to_string_with_specified_style(tmp_req.application_configs, 'ApplicationConfigs', 'json')
        if not DaraCore.is_null(tmp_req.applications):
            request.applications_shrink = Utils.array_to_string_with_specified_style(tmp_req.applications, 'Applications', 'json')
        if not DaraCore.is_null(tmp_req.bootstrap_scripts):
            request.bootstrap_scripts_shrink = Utils.array_to_string_with_specified_style(tmp_req.bootstrap_scripts, 'BootstrapScripts', 'json')
        if not DaraCore.is_null(tmp_req.node_attributes):
            request.node_attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_attributes, 'NodeAttributes', 'json')
        if not DaraCore.is_null(tmp_req.node_groups):
            request.node_groups_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_groups, 'NodeGroups', 'json')
        if not DaraCore.is_null(tmp_req.promotions):
            request.promotions_shrink = Utils.array_to_string_with_specified_style(tmp_req.promotions, 'Promotions', 'json')
        if not DaraCore.is_null(tmp_req.subscription_config):
            request.subscription_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.subscription_config, 'SubscriptionConfig', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.promotions_shrink):
            query['Promotions'] = request.promotions_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.application_configs_shrink):
            body['ApplicationConfigs'] = request.application_configs_shrink
        if not DaraCore.is_null(request.applications_shrink):
            body['Applications'] = request.applications_shrink
        if not DaraCore.is_null(request.bootstrap_scripts_shrink):
            body['BootstrapScripts'] = request.bootstrap_scripts_shrink
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_type):
            body['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.deletion_protection):
            body['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.deploy_mode):
            body['DeployMode'] = request.deploy_mode
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.node_attributes_shrink):
            body['NodeAttributes'] = request.node_attributes_shrink
        if not DaraCore.is_null(request.node_groups_shrink):
            body['NodeGroups'] = request.node_groups_shrink
        if not DaraCore.is_null(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.release_version):
            body['ReleaseVersion'] = request.release_version
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_mode):
            body['SecurityMode'] = request.security_mode
        if not DaraCore.is_null(request.subscription_config_shrink):
            body['SubscriptionConfig'] = request.subscription_config_shrink
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCluster',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_cluster_with_options_async(
        self,
        tmp_req: main_models.RunClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunClusterResponse:
        tmp_req.validate()
        request = main_models.RunClusterShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.application_configs):
            request.application_configs_shrink = Utils.array_to_string_with_specified_style(tmp_req.application_configs, 'ApplicationConfigs', 'json')
        if not DaraCore.is_null(tmp_req.applications):
            request.applications_shrink = Utils.array_to_string_with_specified_style(tmp_req.applications, 'Applications', 'json')
        if not DaraCore.is_null(tmp_req.bootstrap_scripts):
            request.bootstrap_scripts_shrink = Utils.array_to_string_with_specified_style(tmp_req.bootstrap_scripts, 'BootstrapScripts', 'json')
        if not DaraCore.is_null(tmp_req.node_attributes):
            request.node_attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_attributes, 'NodeAttributes', 'json')
        if not DaraCore.is_null(tmp_req.node_groups):
            request.node_groups_shrink = Utils.array_to_string_with_specified_style(tmp_req.node_groups, 'NodeGroups', 'json')
        if not DaraCore.is_null(tmp_req.promotions):
            request.promotions_shrink = Utils.array_to_string_with_specified_style(tmp_req.promotions, 'Promotions', 'json')
        if not DaraCore.is_null(tmp_req.subscription_config):
            request.subscription_config_shrink = Utils.array_to_string_with_specified_style(tmp_req.subscription_config, 'SubscriptionConfig', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.promotions_shrink):
            query['Promotions'] = request.promotions_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.application_configs_shrink):
            body['ApplicationConfigs'] = request.application_configs_shrink
        if not DaraCore.is_null(request.applications_shrink):
            body['Applications'] = request.applications_shrink
        if not DaraCore.is_null(request.bootstrap_scripts_shrink):
            body['BootstrapScripts'] = request.bootstrap_scripts_shrink
        if not DaraCore.is_null(request.client_token):
            body['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_type):
            body['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.deletion_protection):
            body['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.deploy_mode):
            body['DeployMode'] = request.deploy_mode
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.node_attributes_shrink):
            body['NodeAttributes'] = request.node_attributes_shrink
        if not DaraCore.is_null(request.node_groups_shrink):
            body['NodeGroups'] = request.node_groups_shrink
        if not DaraCore.is_null(request.payment_type):
            body['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.release_version):
            body['ReleaseVersion'] = request.release_version
        if not DaraCore.is_null(request.resource_group_id):
            body['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_mode):
            body['SecurityMode'] = request.security_mode
        if not DaraCore.is_null(request.subscription_config_shrink):
            body['SubscriptionConfig'] = request.subscription_config_shrink
        if not DaraCore.is_null(request.tags_shrink):
            body['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RunCluster',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_cluster(
        self,
        request: main_models.RunClusterRequest,
    ) -> main_models.RunClusterResponse:
        runtime = RuntimeOptions()
        return self.run_cluster_with_options(request, runtime)

    async def run_cluster_async(
        self,
        request: main_models.RunClusterRequest,
    ) -> main_models.RunClusterResponse:
        runtime = RuntimeOptions()
        return await self.run_cluster_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2021-03-20',
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
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2021-03-20',
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
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2021-03-20',
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
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2021-03-20',
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

    def update_api_template_with_options(
        self,
        request: main_models.UpdateApiTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApiTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApiTemplate',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApiTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_api_template_with_options_async(
        self,
        request: main_models.UpdateApiTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApiTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.api_name):
            query['ApiName'] = request.api_name
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApiTemplate',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApiTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_api_template(
        self,
        request: main_models.UpdateApiTemplateRequest,
    ) -> main_models.UpdateApiTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_api_template_with_options(request, runtime)

    async def update_api_template_async(
        self,
        request: main_models.UpdateApiTemplateRequest,
    ) -> main_models.UpdateApiTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_api_template_with_options_async(request, runtime)

    def update_application_configs_with_options(
        self,
        request: main_models.UpdateApplicationConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.config_action):
            query['ConfigAction'] = request.config_action
        if not DaraCore.is_null(request.config_scope):
            query['ConfigScope'] = request.config_scope
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.refresh_config):
            query['RefreshConfig'] = request.refresh_config
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.application_configs):
            body_flat['ApplicationConfigs'] = request.application_configs
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationConfigs',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_application_configs_with_options_async(
        self,
        request: main_models.UpdateApplicationConfigsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateApplicationConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.application_name):
            query['ApplicationName'] = request.application_name
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.config_action):
            query['ConfigAction'] = request.config_action
        if not DaraCore.is_null(request.config_scope):
            query['ConfigScope'] = request.config_scope
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.node_id):
            query['NodeId'] = request.node_id
        if not DaraCore.is_null(request.refresh_config):
            query['RefreshConfig'] = request.refresh_config
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        body_flat = {}
        if not DaraCore.is_null(request.application_configs):
            body_flat['ApplicationConfigs'] = request.application_configs
        body = DaraCore.merge({}, body, Utils.query(body_flat))
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateApplicationConfigs',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateApplicationConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_application_configs(
        self,
        request: main_models.UpdateApplicationConfigsRequest,
    ) -> main_models.UpdateApplicationConfigsResponse:
        runtime = RuntimeOptions()
        return self.update_application_configs_with_options(request, runtime)

    async def update_application_configs_async(
        self,
        request: main_models.UpdateApplicationConfigsRequest,
    ) -> main_models.UpdateApplicationConfigsResponse:
        runtime = RuntimeOptions()
        return await self.update_application_configs_with_options_async(request, runtime)

    def update_cluster_attribute_with_options(
        self,
        request: main_models.UpdateClusterAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClusterAttribute',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_attribute_with_options_async(
        self,
        request: main_models.UpdateClusterAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClusterAttribute',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster_attribute(
        self,
        request: main_models.UpdateClusterAttributeRequest,
    ) -> main_models.UpdateClusterAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_cluster_attribute_with_options(request, runtime)

    async def update_cluster_attribute_async(
        self,
        request: main_models.UpdateClusterAttributeRequest,
    ) -> main_models.UpdateClusterAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_cluster_attribute_with_options_async(request, runtime)

    def update_cluster_auto_renew_with_options(
        self,
        request: main_models.UpdateClusterAutoRenewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterAutoRenewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew_instances):
            query['AutoRenewInstances'] = request.auto_renew_instances
        if not DaraCore.is_null(request.cluster_auto_renew):
            query['ClusterAutoRenew'] = request.cluster_auto_renew
        if not DaraCore.is_null(request.cluster_auto_renew_duration):
            query['ClusterAutoRenewDuration'] = request.cluster_auto_renew_duration
        if not DaraCore.is_null(request.cluster_auto_renew_duration_unit):
            query['ClusterAutoRenewDurationUnit'] = request.cluster_auto_renew_duration_unit
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.renew_all_instances):
            query['RenewAllInstances'] = request.renew_all_instances
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClusterAutoRenew',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterAutoRenewResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_auto_renew_with_options_async(
        self,
        request: main_models.UpdateClusterAutoRenewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateClusterAutoRenewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_renew_instances):
            query['AutoRenewInstances'] = request.auto_renew_instances
        if not DaraCore.is_null(request.cluster_auto_renew):
            query['ClusterAutoRenew'] = request.cluster_auto_renew
        if not DaraCore.is_null(request.cluster_auto_renew_duration):
            query['ClusterAutoRenewDuration'] = request.cluster_auto_renew_duration
        if not DaraCore.is_null(request.cluster_auto_renew_duration_unit):
            query['ClusterAutoRenewDurationUnit'] = request.cluster_auto_renew_duration_unit
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.renew_all_instances):
            query['RenewAllInstances'] = request.renew_all_instances
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateClusterAutoRenew',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateClusterAutoRenewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster_auto_renew(
        self,
        request: main_models.UpdateClusterAutoRenewRequest,
    ) -> main_models.UpdateClusterAutoRenewResponse:
        runtime = RuntimeOptions()
        return self.update_cluster_auto_renew_with_options(request, runtime)

    async def update_cluster_auto_renew_async(
        self,
        request: main_models.UpdateClusterAutoRenewRequest,
    ) -> main_models.UpdateClusterAutoRenewResponse:
        runtime = RuntimeOptions()
        return await self.update_cluster_auto_renew_with_options_async(request, runtime)

    def update_node_group_attributes_with_options(
        self,
        request: main_models.UpdateNodeGroupAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNodeGroupAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ack_config):
            query['AckConfig'] = request.ack_config
        if not DaraCore.is_null(request.additional_security_group_ids):
            query['AdditionalSecurityGroupIds'] = request.additional_security_group_ids
        if not DaraCore.is_null(request.auto_compensate_state):
            query['AutoCompensateState'] = request.auto_compensate_state
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cost_optimized_config):
            query['CostOptimizedConfig'] = request.cost_optimized_config
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ecs_spot_strategy):
            query['EcsSpotStrategy'] = request.ecs_spot_strategy
        if not DaraCore.is_null(request.enable_graceful_decommission):
            query['EnableGracefulDecommission'] = request.enable_graceful_decommission
        if not DaraCore.is_null(request.instance_type_list):
            query['InstanceTypeList'] = request.instance_type_list
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.max_size):
            query['MaxSize'] = request.max_size
        if not DaraCore.is_null(request.min_size):
            query['MinSize'] = request.min_size
        if not DaraCore.is_null(request.node_count):
            query['NodeCount'] = request.node_count
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.node_group_name):
            query['NodeGroupName'] = request.node_group_name
        if not DaraCore.is_null(request.node_resize_strategy):
            query['NodeResizeStrategy'] = request.node_resize_strategy
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.spot_bid_prices):
            query['SpotBidPrices'] = request.spot_bid_prices
        if not DaraCore.is_null(request.spot_instance_remedy):
            query['SpotInstanceRemedy'] = request.spot_instance_remedy
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNodeGroupAttributes',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNodeGroupAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_node_group_attributes_with_options_async(
        self,
        request: main_models.UpdateNodeGroupAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateNodeGroupAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ack_config):
            query['AckConfig'] = request.ack_config
        if not DaraCore.is_null(request.additional_security_group_ids):
            query['AdditionalSecurityGroupIds'] = request.additional_security_group_ids
        if not DaraCore.is_null(request.auto_compensate_state):
            query['AutoCompensateState'] = request.auto_compensate_state
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cost_optimized_config):
            query['CostOptimizedConfig'] = request.cost_optimized_config
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.ecs_spot_strategy):
            query['EcsSpotStrategy'] = request.ecs_spot_strategy
        if not DaraCore.is_null(request.enable_graceful_decommission):
            query['EnableGracefulDecommission'] = request.enable_graceful_decommission
        if not DaraCore.is_null(request.instance_type_list):
            query['InstanceTypeList'] = request.instance_type_list
        if not DaraCore.is_null(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not DaraCore.is_null(request.max_size):
            query['MaxSize'] = request.max_size
        if not DaraCore.is_null(request.min_size):
            query['MinSize'] = request.min_size
        if not DaraCore.is_null(request.node_count):
            query['NodeCount'] = request.node_count
        if not DaraCore.is_null(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not DaraCore.is_null(request.node_group_name):
            query['NodeGroupName'] = request.node_group_name
        if not DaraCore.is_null(request.node_resize_strategy):
            query['NodeResizeStrategy'] = request.node_resize_strategy
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.spot_bid_prices):
            query['SpotBidPrices'] = request.spot_bid_prices
        if not DaraCore.is_null(request.spot_instance_remedy):
            query['SpotInstanceRemedy'] = request.spot_instance_remedy
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateNodeGroupAttributes',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateNodeGroupAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_node_group_attributes(
        self,
        request: main_models.UpdateNodeGroupAttributesRequest,
    ) -> main_models.UpdateNodeGroupAttributesResponse:
        runtime = RuntimeOptions()
        return self.update_node_group_attributes_with_options(request, runtime)

    async def update_node_group_attributes_async(
        self,
        request: main_models.UpdateNodeGroupAttributesRequest,
    ) -> main_models.UpdateNodeGroupAttributesResponse:
        runtime = RuntimeOptions()
        return await self.update_node_group_attributes_with_options_async(request, runtime)

    def update_script_with_options(
        self,
        tmp_req: main_models.UpdateScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateScriptResponse:
        tmp_req.validate()
        request = main_models.UpdateScriptShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.script):
            request.script_shrink = Utils.array_to_string_with_specified_style(tmp_req.script, 'Script', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.script_shrink):
            query['Script'] = request.script_shrink
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.script_type):
            query['ScriptType'] = request.script_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScript',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_script_with_options_async(
        self,
        tmp_req: main_models.UpdateScriptRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateScriptResponse:
        tmp_req.validate()
        request = main_models.UpdateScriptShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.script):
            request.script_shrink = Utils.array_to_string_with_specified_style(tmp_req.script, 'Script', 'json')
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.script_shrink):
            query['Script'] = request.script_shrink
        if not DaraCore.is_null(request.script_id):
            query['ScriptId'] = request.script_id
        if not DaraCore.is_null(request.script_type):
            query['ScriptType'] = request.script_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateScript',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_script(
        self,
        request: main_models.UpdateScriptRequest,
    ) -> main_models.UpdateScriptResponse:
        runtime = RuntimeOptions()
        return self.update_script_with_options(request, runtime)

    async def update_script_async(
        self,
        request: main_models.UpdateScriptRequest,
    ) -> main_models.UpdateScriptResponse:
        runtime = RuntimeOptions()
        return await self.update_script_with_options_async(request, runtime)

    def update_user_attribute_with_options(
        self,
        request: main_models.UpdateUserAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserAttribute',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_attribute_with_options_async(
        self,
        request: main_models.UpdateUserAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserAttribute',
            version = '2021-03-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_attribute(
        self,
        request: main_models.UpdateUserAttributeRequest,
    ) -> main_models.UpdateUserAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_user_attribute_with_options(request, runtime)

    async def update_user_attribute_async(
        self,
        request: main_models.UpdateUserAttributeRequest,
    ) -> main_models.UpdateUserAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_user_attribute_with_options_async(request, runtime)
