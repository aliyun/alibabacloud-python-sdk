# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_retailcloud20180313 import models as retailcloud_20180313_models
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
            'ap-northeast-1': 'retailcloud.aliyuncs.com',
            'ap-northeast-2-pop': 'retailcloud.aliyuncs.com',
            'ap-south-1': 'retailcloud.aliyuncs.com',
            'ap-southeast-1': 'retailcloud.aliyuncs.com',
            'ap-southeast-2': 'retailcloud.aliyuncs.com',
            'ap-southeast-3': 'retailcloud.aliyuncs.com',
            'ap-southeast-5': 'retailcloud.aliyuncs.com',
            'cn-beijing': 'retailcloud.aliyuncs.com',
            'cn-beijing-finance-1': 'retailcloud.aliyuncs.com',
            'cn-beijing-finance-pop': 'retailcloud.aliyuncs.com',
            'cn-beijing-gov-1': 'retailcloud.aliyuncs.com',
            'cn-beijing-nu16-b01': 'retailcloud.aliyuncs.com',
            'cn-chengdu': 'retailcloud.aliyuncs.com',
            'cn-edge-1': 'retailcloud.aliyuncs.com',
            'cn-fujian': 'retailcloud.aliyuncs.com',
            'cn-haidian-cm12-c01': 'retailcloud.aliyuncs.com',
            'cn-hangzhou': 'retailcloud.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'retailcloud.aliyuncs.com',
            'cn-hangzhou-finance': 'retailcloud.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'retailcloud.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'retailcloud.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'retailcloud.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'retailcloud.aliyuncs.com',
            'cn-hangzhou-test-306': 'retailcloud.aliyuncs.com',
            'cn-hongkong': 'retailcloud.aliyuncs.com',
            'cn-hongkong-finance-pop': 'retailcloud.aliyuncs.com',
            'cn-huhehaote': 'retailcloud.aliyuncs.com',
            'cn-north-2-gov-1': 'retailcloud.aliyuncs.com',
            'cn-qingdao': 'retailcloud.aliyuncs.com',
            'cn-qingdao-nebula': 'retailcloud.aliyuncs.com',
            'cn-shanghai': 'retailcloud.aliyuncs.com',
            'cn-shanghai-et15-b01': 'retailcloud.aliyuncs.com',
            'cn-shanghai-et2-b01': 'retailcloud.aliyuncs.com',
            'cn-shanghai-finance-1': 'retailcloud.aliyuncs.com',
            'cn-shanghai-inner': 'retailcloud.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'retailcloud.aliyuncs.com',
            'cn-shenzhen': 'retailcloud.aliyuncs.com',
            'cn-shenzhen-finance-1': 'retailcloud.aliyuncs.com',
            'cn-shenzhen-inner': 'retailcloud.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'retailcloud.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'retailcloud.aliyuncs.com',
            'cn-wuhan': 'retailcloud.aliyuncs.com',
            'cn-yushanfang': 'retailcloud.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'retailcloud.aliyuncs.com',
            'cn-zhangjiakou': 'retailcloud.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'retailcloud.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'retailcloud.aliyuncs.com',
            'eu-central-1': 'retailcloud.aliyuncs.com',
            'eu-west-1': 'retailcloud.aliyuncs.com',
            'eu-west-1-oxs': 'retailcloud.aliyuncs.com',
            'me-east-1': 'retailcloud.aliyuncs.com',
            'rus-west-1-pop': 'retailcloud.aliyuncs.com',
            'us-east-1': 'retailcloud.aliyuncs.com',
            'us-west-1': 'retailcloud.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('retailcloud', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_cluster_node_with_options(
        self,
        request: retailcloud_20180313_models.AddClusterNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.AddClusterNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterInstanceId'] = request.cluster_instance_id
        query['EcsInstanceIdList'] = request.ecs_instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddClusterNode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.AddClusterNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_cluster_node_with_options_async(
        self,
        request: retailcloud_20180313_models.AddClusterNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.AddClusterNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterInstanceId'] = request.cluster_instance_id
        query['EcsInstanceIdList'] = request.ecs_instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddClusterNode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.AddClusterNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_cluster_node(
        self,
        request: retailcloud_20180313_models.AddClusterNodeRequest,
    ) -> retailcloud_20180313_models.AddClusterNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_cluster_node_with_options(request, runtime)

    async def add_cluster_node_async(
        self,
        request: retailcloud_20180313_models.AddClusterNodeRequest,
    ) -> retailcloud_20180313_models.AddClusterNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_cluster_node_with_options_async(request, runtime)

    def allocate_pod_config_with_options(
        self,
        request: retailcloud_20180313_models.AllocatePodConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.AllocatePodConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EnvId'] = request.env_id
        query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AllocatePodConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.AllocatePodConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def allocate_pod_config_with_options_async(
        self,
        request: retailcloud_20180313_models.AllocatePodConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.AllocatePodConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EnvId'] = request.env_id
        query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AllocatePodConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.AllocatePodConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def allocate_pod_config(
        self,
        request: retailcloud_20180313_models.AllocatePodConfigRequest,
    ) -> retailcloud_20180313_models.AllocatePodConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.allocate_pod_config_with_options(request, runtime)

    async def allocate_pod_config_async(
        self,
        request: retailcloud_20180313_models.AllocatePodConfigRequest,
    ) -> retailcloud_20180313_models.AllocatePodConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.allocate_pod_config_with_options_async(request, runtime)

    def batch_add_servers_with_options(
        self,
        request: retailcloud_20180313_models.BatchAddServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.BatchAddServersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['RegionId'] = request.region_id
        query['Sign'] = request.sign
        query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchAddServers',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.BatchAddServersResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_add_servers_with_options_async(
        self,
        request: retailcloud_20180313_models.BatchAddServersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.BatchAddServersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['RegionId'] = request.region_id
        query['Sign'] = request.sign
        query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BatchAddServers',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.BatchAddServersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_add_servers(
        self,
        request: retailcloud_20180313_models.BatchAddServersRequest,
    ) -> retailcloud_20180313_models.BatchAddServersResponse:
        runtime = util_models.RuntimeOptions()
        return self.batch_add_servers_with_options(request, runtime)

    async def batch_add_servers_async(
        self,
        request: retailcloud_20180313_models.BatchAddServersRequest,
    ) -> retailcloud_20180313_models.BatchAddServersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.batch_add_servers_with_options_async(request, runtime)

    def bind_group_with_options(
        self,
        request: retailcloud_20180313_models.BindGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.BindGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['BizCode'] = request.biz_code
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindGroup',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.BindGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_group_with_options_async(
        self,
        request: retailcloud_20180313_models.BindGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.BindGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['BizCode'] = request.biz_code
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindGroup',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.BindGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_group(
        self,
        request: retailcloud_20180313_models.BindGroupRequest,
    ) -> retailcloud_20180313_models.BindGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_group_with_options(request, runtime)

    async def bind_group_async(
        self,
        request: retailcloud_20180313_models.BindGroupRequest,
    ) -> retailcloud_20180313_models.BindGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_group_with_options_async(request, runtime)

    def bind_node_label_with_options(
        self,
        request: retailcloud_20180313_models.BindNodeLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.BindNodeLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['InstanceId'] = request.instance_id
        query['LabelKey'] = request.label_key
        query['LabelValue'] = request.label_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindNodeLabel',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.BindNodeLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_node_label_with_options_async(
        self,
        request: retailcloud_20180313_models.BindNodeLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.BindNodeLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['InstanceId'] = request.instance_id
        query['LabelKey'] = request.label_key
        query['LabelValue'] = request.label_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='BindNodeLabel',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.BindNodeLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_node_label(
        self,
        request: retailcloud_20180313_models.BindNodeLabelRequest,
    ) -> retailcloud_20180313_models.BindNodeLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_node_label_with_options(request, runtime)

    async def bind_node_label_async(
        self,
        request: retailcloud_20180313_models.BindNodeLabelRequest,
    ) -> retailcloud_20180313_models.BindNodeLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_node_label_with_options_async(request, runtime)

    def close_deploy_order_with_options(
        self,
        request: retailcloud_20180313_models.CloseDeployOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CloseDeployOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeployOrderId'] = request.deploy_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CloseDeployOrder',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CloseDeployOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_deploy_order_with_options_async(
        self,
        request: retailcloud_20180313_models.CloseDeployOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CloseDeployOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeployOrderId'] = request.deploy_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CloseDeployOrder',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CloseDeployOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_deploy_order(
        self,
        request: retailcloud_20180313_models.CloseDeployOrderRequest,
    ) -> retailcloud_20180313_models.CloseDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_deploy_order_with_options(request, runtime)

    async def close_deploy_order_async(
        self,
        request: retailcloud_20180313_models.CloseDeployOrderRequest,
    ) -> retailcloud_20180313_models.CloseDeployOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_deploy_order_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        request: retailcloud_20180313_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        request: retailcloud_20180313_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: retailcloud_20180313_models.CreateAccountRequest,
    ) -> retailcloud_20180313_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: retailcloud_20180313_models.CreateAccountRequest,
    ) -> retailcloud_20180313_models.CreateAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_app_with_options(
        self,
        request: retailcloud_20180313_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_with_options_async(
        self,
        request: retailcloud_20180313_models.CreateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app(
        self,
        request: retailcloud_20180313_models.CreateAppRequest,
    ) -> retailcloud_20180313_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    async def create_app_async(
        self,
        request: retailcloud_20180313_models.CreateAppRequest,
    ) -> retailcloud_20180313_models.CreateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_with_options_async(request, runtime)

    def create_app_group_with_options(
        self,
        request: retailcloud_20180313_models.CreateAppGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateAppGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAppGroup',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_group_with_options_async(
        self,
        request: retailcloud_20180313_models.CreateAppGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateAppGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAppGroup',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_group(
        self,
        request: retailcloud_20180313_models.CreateAppGroupRequest,
    ) -> retailcloud_20180313_models.CreateAppGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_group_with_options(request, runtime)

    async def create_app_group_async(
        self,
        request: retailcloud_20180313_models.CreateAppGroupRequest,
    ) -> retailcloud_20180313_models.CreateAppGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_group_with_options_async(request, runtime)

    def create_app_monitors_with_options(
        self,
        request: retailcloud_20180313_models.CreateAppMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateAppMonitorsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlarmTemplateId'] = request.alarm_template_id
        query['EnvType'] = request.env_type
        query['MainUserId'] = request.main_user_id
        query['SilenceTime'] = request.silence_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAppMonitors',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateAppMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_monitors_with_options_async(
        self,
        request: retailcloud_20180313_models.CreateAppMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateAppMonitorsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlarmTemplateId'] = request.alarm_template_id
        query['EnvType'] = request.env_type
        query['MainUserId'] = request.main_user_id
        query['SilenceTime'] = request.silence_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAppMonitors',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateAppMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_monitors(
        self,
        request: retailcloud_20180313_models.CreateAppMonitorsRequest,
    ) -> retailcloud_20180313_models.CreateAppMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_monitors_with_options(request, runtime)

    async def create_app_monitors_async(
        self,
        request: retailcloud_20180313_models.CreateAppMonitorsRequest,
    ) -> retailcloud_20180313_models.CreateAppMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_monitors_with_options_async(request, runtime)

    def create_app_resource_alloc_with_options(
        self,
        request: retailcloud_20180313_models.CreateAppResourceAllocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateAppResourceAllocResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppEnvId'] = request.app_env_id
        query['AppId'] = request.app_id
        query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAppResourceAlloc',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateAppResourceAllocResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_app_resource_alloc_with_options_async(
        self,
        request: retailcloud_20180313_models.CreateAppResourceAllocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateAppResourceAllocResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppEnvId'] = request.app_env_id
        query['AppId'] = request.app_id
        query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAppResourceAlloc',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateAppResourceAllocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_app_resource_alloc(
        self,
        request: retailcloud_20180313_models.CreateAppResourceAllocRequest,
    ) -> retailcloud_20180313_models.CreateAppResourceAllocResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_app_resource_alloc_with_options(request, runtime)

    async def create_app_resource_alloc_async(
        self,
        request: retailcloud_20180313_models.CreateAppResourceAllocRequest,
    ) -> retailcloud_20180313_models.CreateAppResourceAllocResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_app_resource_alloc_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        request: retailcloud_20180313_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BusinessCode'] = request.business_code
        query['CloudMonitorFlags'] = request.cloud_monitor_flags
        query['ClusterEnvType'] = request.cluster_env_type
        query['ClusterId'] = request.cluster_id
        query['ClusterTitle'] = request.cluster_title
        query['ClusterType'] = request.cluster_type
        query['CreateWithArmsIntegration'] = request.create_with_arms_integration
        query['CreateWithLogIntegration'] = request.create_with_log_integration
        query['KeyPair'] = request.key_pair
        query['NetPlug'] = request.net_plug
        query['Password'] = request.password
        query['PodCIDR'] = request.pod_cidr
        query['PrivateZone'] = request.private_zone
        query['PublicSlb'] = request.public_slb
        query['RegionId'] = request.region_id
        query['RegionName'] = request.region_name
        query['ServiceCIDR'] = request.service_cidr
        query['SnatEntry'] = request.snat_entry
        query['VpcId'] = request.vpc_id
        query['Vswitchids'] = request.vswitchids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: retailcloud_20180313_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BusinessCode'] = request.business_code
        query['CloudMonitorFlags'] = request.cloud_monitor_flags
        query['ClusterEnvType'] = request.cluster_env_type
        query['ClusterId'] = request.cluster_id
        query['ClusterTitle'] = request.cluster_title
        query['ClusterType'] = request.cluster_type
        query['CreateWithArmsIntegration'] = request.create_with_arms_integration
        query['CreateWithLogIntegration'] = request.create_with_log_integration
        query['KeyPair'] = request.key_pair
        query['NetPlug'] = request.net_plug
        query['Password'] = request.password
        query['PodCIDR'] = request.pod_cidr
        query['PrivateZone'] = request.private_zone
        query['PublicSlb'] = request.public_slb
        query['RegionId'] = request.region_id
        query['RegionName'] = request.region_name
        query['ServiceCIDR'] = request.service_cidr
        query['SnatEntry'] = request.snat_entry
        query['VpcId'] = request.vpc_id
        query['Vswitchids'] = request.vswitchids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: retailcloud_20180313_models.CreateClusterRequest,
    ) -> retailcloud_20180313_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: retailcloud_20180313_models.CreateClusterRequest,
    ) -> retailcloud_20180313_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_db_with_options(
        self,
        request: retailcloud_20180313_models.CreateDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateDbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDb',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateDbResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_db_with_options_async(
        self,
        request: retailcloud_20180313_models.CreateDbRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateDbResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDb',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateDbResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_db(
        self,
        request: retailcloud_20180313_models.CreateDbRequest,
    ) -> retailcloud_20180313_models.CreateDbResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_db_with_options(request, runtime)

    async def create_db_async(
        self,
        request: retailcloud_20180313_models.CreateDbRequest,
    ) -> retailcloud_20180313_models.CreateDbResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_db_with_options_async(request, runtime)

    def create_deploy_config_with_options(
        self,
        request: retailcloud_20180313_models.CreateDeployConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateDeployConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CodePath'] = request.code_path
        query['ConfigMap'] = request.config_map
        query['ConfigMapList'] = request.config_map_list
        query['CronJob'] = request.cron_job
        query['Deployment'] = request.deployment
        query['EnvType'] = request.env_type
        query['Name'] = request.name
        query['SecretList'] = request.secret_list
        query['StatefulSet'] = request.stateful_set
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDeployConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateDeployConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_deploy_config_with_options_async(
        self,
        request: retailcloud_20180313_models.CreateDeployConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateDeployConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CodePath'] = request.code_path
        query['ConfigMap'] = request.config_map
        query['ConfigMapList'] = request.config_map_list
        query['CronJob'] = request.cron_job
        query['Deployment'] = request.deployment
        query['EnvType'] = request.env_type
        query['Name'] = request.name
        query['SecretList'] = request.secret_list
        query['StatefulSet'] = request.stateful_set
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDeployConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateDeployConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_deploy_config(
        self,
        request: retailcloud_20180313_models.CreateDeployConfigRequest,
    ) -> retailcloud_20180313_models.CreateDeployConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_deploy_config_with_options(request, runtime)

    async def create_deploy_config_async(
        self,
        request: retailcloud_20180313_models.CreateDeployConfigRequest,
    ) -> retailcloud_20180313_models.CreateDeployConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_deploy_config_with_options_async(request, runtime)

    def create_eci_config_with_options(
        self,
        request: retailcloud_20180313_models.CreateEciConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateEciConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppEnvId'] = request.app_env_id
        query['EipBandwidth'] = request.eip_bandwidth
        query['EnableEciSchedulePolicy'] = request.enable_eci_schedule_policy
        query['MirrorCache'] = request.mirror_cache
        query['NormalInstanceLimit'] = request.normal_instance_limit
        query['ScheduleVirtualNode'] = request.schedule_virtual_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateEciConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateEciConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_eci_config_with_options_async(
        self,
        request: retailcloud_20180313_models.CreateEciConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateEciConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppEnvId'] = request.app_env_id
        query['EipBandwidth'] = request.eip_bandwidth
        query['EnableEciSchedulePolicy'] = request.enable_eci_schedule_policy
        query['MirrorCache'] = request.mirror_cache
        query['NormalInstanceLimit'] = request.normal_instance_limit
        query['ScheduleVirtualNode'] = request.schedule_virtual_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateEciConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateEciConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_eci_config(
        self,
        request: retailcloud_20180313_models.CreateEciConfigRequest,
    ) -> retailcloud_20180313_models.CreateEciConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_eci_config_with_options(request, runtime)

    async def create_eci_config_async(
        self,
        request: retailcloud_20180313_models.CreateEciConfigRequest,
    ) -> retailcloud_20180313_models.CreateEciConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_eci_config_with_options_async(request, runtime)

    def create_environment_with_options(
        self,
        request: retailcloud_20180313_models.CreateEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['AppSchemaId'] = request.app_schema_id
        query['ClusterId'] = request.cluster_id
        query['EnvName'] = request.env_name
        query['EnvType'] = request.env_type
        query['Region'] = request.region
        query['Replicas'] = request.replicas
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateEnvironment',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_environment_with_options_async(
        self,
        request: retailcloud_20180313_models.CreateEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['AppSchemaId'] = request.app_schema_id
        query['ClusterId'] = request.cluster_id
        query['EnvName'] = request.env_name
        query['EnvType'] = request.env_type
        query['Region'] = request.region
        query['Replicas'] = request.replicas
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateEnvironment',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_environment(
        self,
        request: retailcloud_20180313_models.CreateEnvironmentRequest,
    ) -> retailcloud_20180313_models.CreateEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_environment_with_options(request, runtime)

    async def create_environment_async(
        self,
        request: retailcloud_20180313_models.CreateEnvironmentRequest,
    ) -> retailcloud_20180313_models.CreateEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_environment_with_options_async(request, runtime)

    def create_node_label_with_options(
        self,
        request: retailcloud_20180313_models.CreateNodeLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateNodeLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['LabelKey'] = request.label_key
        query['LabelValue'] = request.label_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateNodeLabel',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateNodeLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_node_label_with_options_async(
        self,
        request: retailcloud_20180313_models.CreateNodeLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateNodeLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['LabelKey'] = request.label_key
        query['LabelValue'] = request.label_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateNodeLabel',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateNodeLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_node_label(
        self,
        request: retailcloud_20180313_models.CreateNodeLabelRequest,
    ) -> retailcloud_20180313_models.CreateNodeLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_node_label_with_options(request, runtime)

    async def create_node_label_async(
        self,
        request: retailcloud_20180313_models.CreateNodeLabelRequest,
    ) -> retailcloud_20180313_models.CreateNodeLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_node_label_with_options_async(request, runtime)

    def create_persistent_volume_with_options(
        self,
        request: retailcloud_20180313_models.CreatePersistentVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreatePersistentVolumeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePersistentVolume',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreatePersistentVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_persistent_volume_with_options_async(
        self,
        request: retailcloud_20180313_models.CreatePersistentVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreatePersistentVolumeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePersistentVolume',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreatePersistentVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_persistent_volume(
        self,
        request: retailcloud_20180313_models.CreatePersistentVolumeRequest,
    ) -> retailcloud_20180313_models.CreatePersistentVolumeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_persistent_volume_with_options(request, runtime)

    async def create_persistent_volume_async(
        self,
        request: retailcloud_20180313_models.CreatePersistentVolumeRequest,
    ) -> retailcloud_20180313_models.CreatePersistentVolumeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_persistent_volume_with_options_async(request, runtime)

    def create_persistent_volume_claim_with_options(
        self,
        request: retailcloud_20180313_models.CreatePersistentVolumeClaimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreatePersistentVolumeClaimResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessModes'] = request.access_modes
        query['AppId'] = request.app_id
        query['Capacity'] = request.capacity
        query['EnvId'] = request.env_id
        query['Name'] = request.name
        query['StorageClass'] = request.storage_class
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePersistentVolumeClaim',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreatePersistentVolumeClaimResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_persistent_volume_claim_with_options_async(
        self,
        request: retailcloud_20180313_models.CreatePersistentVolumeClaimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreatePersistentVolumeClaimResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AccessModes'] = request.access_modes
        query['AppId'] = request.app_id
        query['Capacity'] = request.capacity
        query['EnvId'] = request.env_id
        query['Name'] = request.name
        query['StorageClass'] = request.storage_class
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreatePersistentVolumeClaim',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreatePersistentVolumeClaimResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_persistent_volume_claim(
        self,
        request: retailcloud_20180313_models.CreatePersistentVolumeClaimRequest,
    ) -> retailcloud_20180313_models.CreatePersistentVolumeClaimResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_persistent_volume_claim_with_options(request, runtime)

    async def create_persistent_volume_claim_async(
        self,
        request: retailcloud_20180313_models.CreatePersistentVolumeClaimRequest,
    ) -> retailcloud_20180313_models.CreatePersistentVolumeClaimResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_persistent_volume_claim_with_options_async(request, runtime)

    def create_service_with_options(
        self,
        request: retailcloud_20180313_models.CreateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EnvId'] = request.env_id
        query['Headless'] = request.headless
        query['K8sServiceId'] = request.k_8s_service_id
        query['Name'] = request.name
        query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_with_options_async(
        self,
        request: retailcloud_20180313_models.CreateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EnvId'] = request.env_id
        query['Headless'] = request.headless
        query['K8sServiceId'] = request.k_8s_service_id
        query['Name'] = request.name
        query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service(
        self,
        request: retailcloud_20180313_models.CreateServiceRequest,
    ) -> retailcloud_20180313_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_service_with_options(request, runtime)

    async def create_service_async(
        self,
        request: retailcloud_20180313_models.CreateServiceRequest,
    ) -> retailcloud_20180313_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_with_options_async(request, runtime)

    def create_slb_apwith_options(
        self,
        request: retailcloud_20180313_models.CreateSlbAPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateSlbAPResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CookieTimeout'] = request.cookie_timeout
        query['EnvId'] = request.env_id
        query['EstablishedTimeout'] = request.established_timeout
        query['ListenerPort'] = request.listener_port
        query['Name'] = request.name
        query['Protocol'] = request.protocol
        query['RealServerPort'] = request.real_server_port
        query['SlbId'] = request.slb_id
        query['SslCertId'] = request.ssl_cert_id
        query['StickySession'] = request.sticky_session
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSlbAP',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateSlbAPResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_slb_apwith_options_async(
        self,
        request: retailcloud_20180313_models.CreateSlbAPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.CreateSlbAPResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CookieTimeout'] = request.cookie_timeout
        query['EnvId'] = request.env_id
        query['EstablishedTimeout'] = request.established_timeout
        query['ListenerPort'] = request.listener_port
        query['Name'] = request.name
        query['Protocol'] = request.protocol
        query['RealServerPort'] = request.real_server_port
        query['SlbId'] = request.slb_id
        query['SslCertId'] = request.ssl_cert_id
        query['StickySession'] = request.sticky_session
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateSlbAP',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateSlbAPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_slb_ap(
        self,
        request: retailcloud_20180313_models.CreateSlbAPRequest,
    ) -> retailcloud_20180313_models.CreateSlbAPResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_slb_apwith_options(request, runtime)

    async def create_slb_ap_async(
        self,
        request: retailcloud_20180313_models.CreateSlbAPRequest,
    ) -> retailcloud_20180313_models.CreateSlbAPResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_slb_apwith_options_async(request, runtime)

    def delete_app_detail_with_options(
        self,
        request: retailcloud_20180313_models.DeleteAppDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteAppDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteAppDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_detail_with_options_async(
        self,
        request: retailcloud_20180313_models.DeleteAppDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteAppDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteAppDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_detail(
        self,
        request: retailcloud_20180313_models.DeleteAppDetailRequest,
    ) -> retailcloud_20180313_models.DeleteAppDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_detail_with_options(request, runtime)

    async def delete_app_detail_async(
        self,
        request: retailcloud_20180313_models.DeleteAppDetailRequest,
    ) -> retailcloud_20180313_models.DeleteAppDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_detail_with_options_async(request, runtime)

    def delete_app_environment_with_options(
        self,
        request: retailcloud_20180313_models.DeleteAppEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteAppEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EnvId'] = request.env_id
        query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAppEnvironment',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteAppEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_environment_with_options_async(
        self,
        request: retailcloud_20180313_models.DeleteAppEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteAppEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EnvId'] = request.env_id
        query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAppEnvironment',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteAppEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_environment(
        self,
        request: retailcloud_20180313_models.DeleteAppEnvironmentRequest,
    ) -> retailcloud_20180313_models.DeleteAppEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_environment_with_options(request, runtime)

    async def delete_app_environment_async(
        self,
        request: retailcloud_20180313_models.DeleteAppEnvironmentRequest,
    ) -> retailcloud_20180313_models.DeleteAppEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_environment_with_options_async(request, runtime)

    def delete_app_group_with_options(
        self,
        request: retailcloud_20180313_models.DeleteAppGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteAppGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Force'] = request.force
        query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAppGroup',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_group_with_options_async(
        self,
        request: retailcloud_20180313_models.DeleteAppGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteAppGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Force'] = request.force
        query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAppGroup',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_group(
        self,
        request: retailcloud_20180313_models.DeleteAppGroupRequest,
    ) -> retailcloud_20180313_models.DeleteAppGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_group_with_options(request, runtime)

    async def delete_app_group_async(
        self,
        request: retailcloud_20180313_models.DeleteAppGroupRequest,
    ) -> retailcloud_20180313_models.DeleteAppGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_group_with_options_async(request, runtime)

    def delete_app_resource_alloc_with_options(
        self,
        request: retailcloud_20180313_models.DeleteAppResourceAllocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteAppResourceAllocResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppEnvId'] = request.app_env_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAppResourceAlloc',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteAppResourceAllocResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_resource_alloc_with_options_async(
        self,
        request: retailcloud_20180313_models.DeleteAppResourceAllocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteAppResourceAllocResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppEnvId'] = request.app_env_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAppResourceAlloc',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteAppResourceAllocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_resource_alloc(
        self,
        request: retailcloud_20180313_models.DeleteAppResourceAllocRequest,
    ) -> retailcloud_20180313_models.DeleteAppResourceAllocResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_resource_alloc_with_options(request, runtime)

    async def delete_app_resource_alloc_async(
        self,
        request: retailcloud_20180313_models.DeleteAppResourceAllocRequest,
    ) -> retailcloud_20180313_models.DeleteAppResourceAllocResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_resource_alloc_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: retailcloud_20180313_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterInstanceId'] = request.cluster_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: retailcloud_20180313_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterInstanceId'] = request.cluster_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        request: retailcloud_20180313_models.DeleteClusterRequest,
    ) -> retailcloud_20180313_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: retailcloud_20180313_models.DeleteClusterRequest,
    ) -> retailcloud_20180313_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def delete_database_with_options(
        self,
        request: retailcloud_20180313_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_database_with_options_async(
        self,
        request: retailcloud_20180313_models.DeleteDatabaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteDatabaseResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_database(
        self,
        request: retailcloud_20180313_models.DeleteDatabaseRequest,
    ) -> retailcloud_20180313_models.DeleteDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_database_with_options(request, runtime)

    async def delete_database_async(
        self,
        request: retailcloud_20180313_models.DeleteDatabaseRequest,
    ) -> retailcloud_20180313_models.DeleteDatabaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_database_with_options_async(request, runtime)

    def delete_deploy_config_with_options(
        self,
        request: retailcloud_20180313_models.DeleteDeployConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteDeployConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDeployConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteDeployConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_deploy_config_with_options_async(
        self,
        request: retailcloud_20180313_models.DeleteDeployConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteDeployConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteDeployConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteDeployConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_deploy_config(
        self,
        request: retailcloud_20180313_models.DeleteDeployConfigRequest,
    ) -> retailcloud_20180313_models.DeleteDeployConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_deploy_config_with_options(request, runtime)

    async def delete_deploy_config_async(
        self,
        request: retailcloud_20180313_models.DeleteDeployConfigRequest,
    ) -> retailcloud_20180313_models.DeleteDeployConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_deploy_config_with_options_async(request, runtime)

    def delete_node_label_with_options(
        self,
        request: retailcloud_20180313_models.DeleteNodeLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteNodeLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Force'] = request.force
        query['LabelKey'] = request.label_key
        query['LabelValue'] = request.label_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteNodeLabel',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteNodeLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_node_label_with_options_async(
        self,
        request: retailcloud_20180313_models.DeleteNodeLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteNodeLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Force'] = request.force
        query['LabelKey'] = request.label_key
        query['LabelValue'] = request.label_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteNodeLabel',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteNodeLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_node_label(
        self,
        request: retailcloud_20180313_models.DeleteNodeLabelRequest,
    ) -> retailcloud_20180313_models.DeleteNodeLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_node_label_with_options(request, runtime)

    async def delete_node_label_async(
        self,
        request: retailcloud_20180313_models.DeleteNodeLabelRequest,
    ) -> retailcloud_20180313_models.DeleteNodeLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_node_label_with_options_async(request, runtime)

    def delete_persistent_volume_with_options(
        self,
        request: retailcloud_20180313_models.DeletePersistentVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeletePersistentVolumeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeletePersistentVolume',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeletePersistentVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_persistent_volume_with_options_async(
        self,
        request: retailcloud_20180313_models.DeletePersistentVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeletePersistentVolumeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeletePersistentVolume',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeletePersistentVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_persistent_volume(
        self,
        request: retailcloud_20180313_models.DeletePersistentVolumeRequest,
    ) -> retailcloud_20180313_models.DeletePersistentVolumeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_persistent_volume_with_options(request, runtime)

    async def delete_persistent_volume_async(
        self,
        request: retailcloud_20180313_models.DeletePersistentVolumeRequest,
    ) -> retailcloud_20180313_models.DeletePersistentVolumeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_persistent_volume_with_options_async(request, runtime)

    def delete_persistent_volume_claim_with_options(
        self,
        request: retailcloud_20180313_models.DeletePersistentVolumeClaimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeletePersistentVolumeClaimResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EnvId'] = request.env_id
        query['PersistentVolumeClaimName'] = request.persistent_volume_claim_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeletePersistentVolumeClaim',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeletePersistentVolumeClaimResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_persistent_volume_claim_with_options_async(
        self,
        request: retailcloud_20180313_models.DeletePersistentVolumeClaimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeletePersistentVolumeClaimResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EnvId'] = request.env_id
        query['PersistentVolumeClaimName'] = request.persistent_volume_claim_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeletePersistentVolumeClaim',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeletePersistentVolumeClaimResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_persistent_volume_claim(
        self,
        request: retailcloud_20180313_models.DeletePersistentVolumeClaimRequest,
    ) -> retailcloud_20180313_models.DeletePersistentVolumeClaimResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_persistent_volume_claim_with_options(request, runtime)

    async def delete_persistent_volume_claim_async(
        self,
        request: retailcloud_20180313_models.DeletePersistentVolumeClaimRequest,
    ) -> retailcloud_20180313_models.DeletePersistentVolumeClaimResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_persistent_volume_claim_with_options_async(request, runtime)

    def delete_rds_account_with_options(
        self,
        request: retailcloud_20180313_models.DeleteRdsAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteRdsAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteRdsAccount',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteRdsAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rds_account_with_options_async(
        self,
        request: retailcloud_20180313_models.DeleteRdsAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteRdsAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteRdsAccount',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteRdsAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rds_account(
        self,
        request: retailcloud_20180313_models.DeleteRdsAccountRequest,
    ) -> retailcloud_20180313_models.DeleteRdsAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_rds_account_with_options(request, runtime)

    async def delete_rds_account_async(
        self,
        request: retailcloud_20180313_models.DeleteRdsAccountRequest,
    ) -> retailcloud_20180313_models.DeleteRdsAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_rds_account_with_options_async(request, runtime)

    def delete_service_with_options(
        self,
        request: retailcloud_20180313_models.DeleteServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        request: retailcloud_20180313_models.DeleteServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service(
        self,
        request: retailcloud_20180313_models.DeleteServiceRequest,
    ) -> retailcloud_20180313_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_service_with_options(request, runtime)

    async def delete_service_async(
        self,
        request: retailcloud_20180313_models.DeleteServiceRequest,
    ) -> retailcloud_20180313_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_with_options_async(request, runtime)

    def delete_slb_apwith_options(
        self,
        request: retailcloud_20180313_models.DeleteSlbAPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteSlbAPResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SlbAPId'] = request.slb_apid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSlbAP',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteSlbAPResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_slb_apwith_options_async(
        self,
        request: retailcloud_20180313_models.DeleteSlbAPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeleteSlbAPResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SlbAPId'] = request.slb_apid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteSlbAP',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteSlbAPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_slb_ap(
        self,
        request: retailcloud_20180313_models.DeleteSlbAPRequest,
    ) -> retailcloud_20180313_models.DeleteSlbAPResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_slb_apwith_options(request, runtime)

    async def delete_slb_ap_async(
        self,
        request: retailcloud_20180313_models.DeleteSlbAPRequest,
    ) -> retailcloud_20180313_models.DeleteSlbAPResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_slb_apwith_options_async(request, runtime)

    def deploy_app_with_options(
        self,
        request: retailcloud_20180313_models.DeployAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeployAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ArmsFlag'] = request.arms_flag
        query['ContainerImageList'] = request.container_image_list
        query['DefaultPacketOfAppGroup'] = request.default_packet_of_app_group
        query['DeployPacketId'] = request.deploy_packet_id
        query['DeployPacketUrl'] = request.deploy_packet_url
        query['Description'] = request.description
        query['EnvId'] = request.env_id
        query['InitContainerImageList'] = request.init_container_image_list
        query['Name'] = request.name
        query['PauseType'] = request.pause_type
        query['TotalPartitions'] = request.total_partitions
        query['UpdateStrategyType'] = request.update_strategy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeployApp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeployAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_app_with_options_async(
        self,
        request: retailcloud_20180313_models.DeployAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DeployAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ArmsFlag'] = request.arms_flag
        query['ContainerImageList'] = request.container_image_list
        query['DefaultPacketOfAppGroup'] = request.default_packet_of_app_group
        query['DeployPacketId'] = request.deploy_packet_id
        query['DeployPacketUrl'] = request.deploy_packet_url
        query['Description'] = request.description
        query['EnvId'] = request.env_id
        query['InitContainerImageList'] = request.init_container_image_list
        query['Name'] = request.name
        query['PauseType'] = request.pause_type
        query['TotalPartitions'] = request.total_partitions
        query['UpdateStrategyType'] = request.update_strategy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeployApp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeployAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_app(
        self,
        request: retailcloud_20180313_models.DeployAppRequest,
    ) -> retailcloud_20180313_models.DeployAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_app_with_options(request, runtime)

    async def deploy_app_async(
        self,
        request: retailcloud_20180313_models.DeployAppRequest,
    ) -> retailcloud_20180313_models.DeployAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_app_with_options_async(request, runtime)

    def describe_app_detail_with_options(
        self,
        request: retailcloud_20180313_models.DescribeAppDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeAppDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAppDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeAppDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_detail_with_options_async(
        self,
        request: retailcloud_20180313_models.DescribeAppDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeAppDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAppDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeAppDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_detail(
        self,
        request: retailcloud_20180313_models.DescribeAppDetailRequest,
    ) -> retailcloud_20180313_models.DescribeAppDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_detail_with_options(request, runtime)

    async def describe_app_detail_async(
        self,
        request: retailcloud_20180313_models.DescribeAppDetailRequest,
    ) -> retailcloud_20180313_models.DescribeAppDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_detail_with_options_async(request, runtime)

    def describe_app_environment_detail_with_options(
        self,
        request: retailcloud_20180313_models.DescribeAppEnvironmentDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeAppEnvironmentDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppEnvironmentDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeAppEnvironmentDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_environment_detail_with_options_async(
        self,
        request: retailcloud_20180313_models.DescribeAppEnvironmentDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeAppEnvironmentDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppEnvironmentDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeAppEnvironmentDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_environment_detail(
        self,
        request: retailcloud_20180313_models.DescribeAppEnvironmentDetailRequest,
    ) -> retailcloud_20180313_models.DescribeAppEnvironmentDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_environment_detail_with_options(request, runtime)

    async def describe_app_environment_detail_async(
        self,
        request: retailcloud_20180313_models.DescribeAppEnvironmentDetailRequest,
    ) -> retailcloud_20180313_models.DescribeAppEnvironmentDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_environment_detail_with_options_async(request, runtime)

    def describe_app_monitor_metric_with_options(
        self,
        request: retailcloud_20180313_models.DescribeAppMonitorMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeAppMonitorMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['DeployOrderId'] = request.deploy_order_id
        query['EndTime'] = request.end_time
        query['EnvId'] = request.env_id
        query['Metric'] = request.metric
        query['PodName'] = request.pod_name
        query['StartTime'] = request.start_time
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAppMonitorMetric',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeAppMonitorMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_monitor_metric_with_options_async(
        self,
        request: retailcloud_20180313_models.DescribeAppMonitorMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeAppMonitorMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['DeployOrderId'] = request.deploy_order_id
        query['EndTime'] = request.end_time
        query['EnvId'] = request.env_id
        query['Metric'] = request.metric
        query['PodName'] = request.pod_name
        query['StartTime'] = request.start_time
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAppMonitorMetric',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeAppMonitorMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_monitor_metric(
        self,
        request: retailcloud_20180313_models.DescribeAppMonitorMetricRequest,
    ) -> retailcloud_20180313_models.DescribeAppMonitorMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_monitor_metric_with_options(request, runtime)

    async def describe_app_monitor_metric_async(
        self,
        request: retailcloud_20180313_models.DescribeAppMonitorMetricRequest,
    ) -> retailcloud_20180313_models.DescribeAppMonitorMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_monitor_metric_with_options_async(request, runtime)

    def describe_app_resource_alloc_with_options(
        self,
        request: retailcloud_20180313_models.DescribeAppResourceAllocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeAppResourceAllocResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppResourceAlloc',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeAppResourceAllocResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_app_resource_alloc_with_options_async(
        self,
        request: retailcloud_20180313_models.DescribeAppResourceAllocRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeAppResourceAllocResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppResourceAlloc',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeAppResourceAllocResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_app_resource_alloc(
        self,
        request: retailcloud_20180313_models.DescribeAppResourceAllocRequest,
    ) -> retailcloud_20180313_models.DescribeAppResourceAllocResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_app_resource_alloc_with_options(request, runtime)

    async def describe_app_resource_alloc_async(
        self,
        request: retailcloud_20180313_models.DescribeAppResourceAllocRequest,
    ) -> retailcloud_20180313_models.DescribeAppResourceAllocResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_app_resource_alloc_with_options_async(request, runtime)

    def describe_cluster_detail_with_options(
        self,
        request: retailcloud_20180313_models.DescribeClusterDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeClusterDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterInstanceId'] = request.cluster_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeClusterDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_detail_with_options_async(
        self,
        request: retailcloud_20180313_models.DescribeClusterDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeClusterDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterInstanceId'] = request.cluster_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeClusterDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_cluster_detail(
        self,
        request: retailcloud_20180313_models.DescribeClusterDetailRequest,
    ) -> retailcloud_20180313_models.DescribeClusterDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_detail_with_options(request, runtime)

    async def describe_cluster_detail_async(
        self,
        request: retailcloud_20180313_models.DescribeClusterDetailRequest,
    ) -> retailcloud_20180313_models.DescribeClusterDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_detail_with_options_async(request, runtime)

    def describe_databases_with_options(
        self,
        request: retailcloud_20180313_models.DescribeDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeDatabasesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabases',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_databases_with_options_async(
        self,
        request: retailcloud_20180313_models.DescribeDatabasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeDatabasesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabases',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_databases(
        self,
        request: retailcloud_20180313_models.DescribeDatabasesRequest,
    ) -> retailcloud_20180313_models.DescribeDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_databases_with_options(request, runtime)

    async def describe_databases_async(
        self,
        request: retailcloud_20180313_models.DescribeDatabasesRequest,
    ) -> retailcloud_20180313_models.DescribeDatabasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_databases_with_options_async(request, runtime)

    def describe_deploy_order_detail_with_options(
        self,
        request: retailcloud_20180313_models.DescribeDeployOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeDeployOrderDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeployOrderId'] = request.deploy_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDeployOrderDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeDeployOrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_deploy_order_detail_with_options_async(
        self,
        request: retailcloud_20180313_models.DescribeDeployOrderDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeDeployOrderDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeployOrderId'] = request.deploy_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDeployOrderDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeDeployOrderDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_deploy_order_detail(
        self,
        request: retailcloud_20180313_models.DescribeDeployOrderDetailRequest,
    ) -> retailcloud_20180313_models.DescribeDeployOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_deploy_order_detail_with_options(request, runtime)

    async def describe_deploy_order_detail_async(
        self,
        request: retailcloud_20180313_models.DescribeDeployOrderDetailRequest,
    ) -> retailcloud_20180313_models.DescribeDeployOrderDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_deploy_order_detail_with_options_async(request, runtime)

    def describe_eci_config_with_options(
        self,
        request: retailcloud_20180313_models.DescribeEciConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeEciConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEciConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeEciConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_eci_config_with_options_async(
        self,
        request: retailcloud_20180313_models.DescribeEciConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeEciConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEciConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeEciConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_eci_config(
        self,
        request: retailcloud_20180313_models.DescribeEciConfigRequest,
    ) -> retailcloud_20180313_models.DescribeEciConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_eci_config_with_options(request, runtime)

    async def describe_eci_config_async(
        self,
        request: retailcloud_20180313_models.DescribeEciConfigRequest,
    ) -> retailcloud_20180313_models.DescribeEciConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_eci_config_with_options_async(request, runtime)

    def describe_event_monitor_list_with_options(
        self,
        request: retailcloud_20180313_models.DescribeEventMonitorListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeEventMonitorListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EndTime'] = request.end_time
        query['EnvId'] = request.env_id
        query['EventLevel'] = request.event_level
        query['EventType'] = request.event_type
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        query['PodName'] = request.pod_name
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeEventMonitorList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeEventMonitorListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_monitor_list_with_options_async(
        self,
        request: retailcloud_20180313_models.DescribeEventMonitorListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeEventMonitorListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EndTime'] = request.end_time
        query['EnvId'] = request.env_id
        query['EventLevel'] = request.event_level
        query['EventType'] = request.event_type
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        query['PodName'] = request.pod_name
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeEventMonitorList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeEventMonitorListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_monitor_list(
        self,
        request: retailcloud_20180313_models.DescribeEventMonitorListRequest,
    ) -> retailcloud_20180313_models.DescribeEventMonitorListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_event_monitor_list_with_options(request, runtime)

    async def describe_event_monitor_list_async(
        self,
        request: retailcloud_20180313_models.DescribeEventMonitorListRequest,
    ) -> retailcloud_20180313_models.DescribeEventMonitorListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_event_monitor_list_with_options_async(request, runtime)

    def describe_job_log_with_options(
        self,
        request: retailcloud_20180313_models.DescribeJobLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeJobLogResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeJobLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_log_with_options_async(
        self,
        request: retailcloud_20180313_models.DescribeJobLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeJobLogResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeJobLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_log(
        self,
        request: retailcloud_20180313_models.DescribeJobLogRequest,
    ) -> retailcloud_20180313_models.DescribeJobLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_job_log_with_options(request, runtime)

    async def describe_job_log_async(
        self,
        request: retailcloud_20180313_models.DescribeJobLogRequest,
    ) -> retailcloud_20180313_models.DescribeJobLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_log_with_options_async(request, runtime)

    def describe_pod_container_log_list_with_options(
        self,
        request: retailcloud_20180313_models.DescribePodContainerLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribePodContainerLogListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EnvId'] = request.env_id
        query['Line'] = request.line
        query['PodName'] = request.pod_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePodContainerLogList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribePodContainerLogListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pod_container_log_list_with_options_async(
        self,
        request: retailcloud_20180313_models.DescribePodContainerLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribePodContainerLogListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EnvId'] = request.env_id
        query['Line'] = request.line
        query['PodName'] = request.pod_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePodContainerLogList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribePodContainerLogListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pod_container_log_list(
        self,
        request: retailcloud_20180313_models.DescribePodContainerLogListRequest,
    ) -> retailcloud_20180313_models.DescribePodContainerLogListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pod_container_log_list_with_options(request, runtime)

    async def describe_pod_container_log_list_async(
        self,
        request: retailcloud_20180313_models.DescribePodContainerLogListRequest,
    ) -> retailcloud_20180313_models.DescribePodContainerLogListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pod_container_log_list_with_options_async(request, runtime)

    def describe_pod_events_with_options(
        self,
        request: retailcloud_20180313_models.DescribePodEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribePodEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppInstId'] = request.app_inst_id
        query['DeployOrderId'] = request.deploy_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePodEvents',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribePodEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pod_events_with_options_async(
        self,
        request: retailcloud_20180313_models.DescribePodEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribePodEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppInstId'] = request.app_inst_id
        query['DeployOrderId'] = request.deploy_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePodEvents',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribePodEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pod_events(
        self,
        request: retailcloud_20180313_models.DescribePodEventsRequest,
    ) -> retailcloud_20180313_models.DescribePodEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pod_events_with_options(request, runtime)

    async def describe_pod_events_async(
        self,
        request: retailcloud_20180313_models.DescribePodEventsRequest,
    ) -> retailcloud_20180313_models.DescribePodEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pod_events_with_options_async(request, runtime)

    def describe_pod_log_with_options(
        self,
        request: retailcloud_20180313_models.DescribePodLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribePodLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePodLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribePodLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pod_log_with_options_async(
        self,
        request: retailcloud_20180313_models.DescribePodLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribePodLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribePodLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribePodLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pod_log(
        self,
        request: retailcloud_20180313_models.DescribePodLogRequest,
    ) -> retailcloud_20180313_models.DescribePodLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pod_log_with_options(request, runtime)

    async def describe_pod_log_async(
        self,
        request: retailcloud_20180313_models.DescribePodLogRequest,
    ) -> retailcloud_20180313_models.DescribePodLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pod_log_with_options_async(request, runtime)

    def describe_rds_accounts_with_options(
        self,
        request: retailcloud_20180313_models.DescribeRdsAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeRdsAccountsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsAccounts',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeRdsAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_rds_accounts_with_options_async(
        self,
        request: retailcloud_20180313_models.DescribeRdsAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeRdsAccountsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsAccounts',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeRdsAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_rds_accounts(
        self,
        request: retailcloud_20180313_models.DescribeRdsAccountsRequest,
    ) -> retailcloud_20180313_models.DescribeRdsAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_accounts_with_options(request, runtime)

    async def describe_rds_accounts_async(
        self,
        request: retailcloud_20180313_models.DescribeRdsAccountsRequest,
    ) -> retailcloud_20180313_models.DescribeRdsAccountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_rds_accounts_with_options_async(request, runtime)

    def describe_service_detail_with_options(
        self,
        request: retailcloud_20180313_models.DescribeServiceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeServiceDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeServiceDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeServiceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_service_detail_with_options_async(
        self,
        request: retailcloud_20180313_models.DescribeServiceDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeServiceDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeServiceDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeServiceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_service_detail(
        self,
        request: retailcloud_20180313_models.DescribeServiceDetailRequest,
    ) -> retailcloud_20180313_models.DescribeServiceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_service_detail_with_options(request, runtime)

    async def describe_service_detail_async(
        self,
        request: retailcloud_20180313_models.DescribeServiceDetailRequest,
    ) -> retailcloud_20180313_models.DescribeServiceDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_service_detail_with_options_async(request, runtime)

    def describe_slb_apdetail_with_options(
        self,
        request: retailcloud_20180313_models.DescribeSlbAPDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeSlbAPDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SlbAPId'] = request.slb_apid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlbAPDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeSlbAPDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slb_apdetail_with_options_async(
        self,
        request: retailcloud_20180313_models.DescribeSlbAPDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.DescribeSlbAPDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['SlbAPId'] = request.slb_apid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSlbAPDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeSlbAPDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slb_apdetail(
        self,
        request: retailcloud_20180313_models.DescribeSlbAPDetailRequest,
    ) -> retailcloud_20180313_models.DescribeSlbAPDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_slb_apdetail_with_options(request, runtime)

    async def describe_slb_apdetail_async(
        self,
        request: retailcloud_20180313_models.DescribeSlbAPDetailRequest,
    ) -> retailcloud_20180313_models.DescribeSlbAPDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_slb_apdetail_with_options_async(request, runtime)

    def get_inst_trans_info_with_options(
        self,
        request: retailcloud_20180313_models.GetInstTransInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.GetInstTransInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetInstTransInfo',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.GetInstTransInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_inst_trans_info_with_options_async(
        self,
        request: retailcloud_20180313_models.GetInstTransInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.GetInstTransInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetInstTransInfo',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.GetInstTransInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_inst_trans_info(
        self,
        request: retailcloud_20180313_models.GetInstTransInfoRequest,
    ) -> retailcloud_20180313_models.GetInstTransInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_inst_trans_info_with_options(request, runtime)

    async def get_inst_trans_info_async(
        self,
        request: retailcloud_20180313_models.GetInstTransInfoRequest,
    ) -> retailcloud_20180313_models.GetInstTransInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_inst_trans_info_with_options_async(request, runtime)

    def get_rds_back_up_with_options(
        self,
        request: retailcloud_20180313_models.GetRdsBackUpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.GetRdsBackUpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetRdsBackUp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.GetRdsBackUpResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rds_back_up_with_options_async(
        self,
        request: retailcloud_20180313_models.GetRdsBackUpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.GetRdsBackUpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetRdsBackUp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.GetRdsBackUpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rds_back_up(
        self,
        request: retailcloud_20180313_models.GetRdsBackUpRequest,
    ) -> retailcloud_20180313_models.GetRdsBackUpResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_rds_back_up_with_options(request, runtime)

    async def get_rds_back_up_async(
        self,
        request: retailcloud_20180313_models.GetRdsBackUpRequest,
    ) -> retailcloud_20180313_models.GetRdsBackUpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_rds_back_up_with_options_async(request, runtime)

    def grant_db_to_account_with_options(
        self,
        request: retailcloud_20180313_models.GrantDbToAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.GrantDbToAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GrantDbToAccount',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.GrantDbToAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_db_to_account_with_options_async(
        self,
        request: retailcloud_20180313_models.GrantDbToAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.GrantDbToAccountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GrantDbToAccount',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.GrantDbToAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_db_to_account(
        self,
        request: retailcloud_20180313_models.GrantDbToAccountRequest,
    ) -> retailcloud_20180313_models.GrantDbToAccountResponse:
        runtime = util_models.RuntimeOptions()
        return self.grant_db_to_account_with_options(request, runtime)

    async def grant_db_to_account_async(
        self,
        request: retailcloud_20180313_models.GrantDbToAccountRequest,
    ) -> retailcloud_20180313_models.GrantDbToAccountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.grant_db_to_account_with_options_async(request, runtime)

    def list_app_with_options(
        self,
        request: retailcloud_20180313_models.ListAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListAppResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_with_options_async(
        self,
        request: retailcloud_20180313_models.ListAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListAppResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app(
        self,
        request: retailcloud_20180313_models.ListAppRequest,
    ) -> retailcloud_20180313_models.ListAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_with_options(request, runtime)

    async def list_app_async(
        self,
        request: retailcloud_20180313_models.ListAppRequest,
    ) -> retailcloud_20180313_models.ListAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_with_options_async(request, runtime)

    def list_app_cms_groups_with_options(
        self,
        request: retailcloud_20180313_models.ListAppCmsGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListAppCmsGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppCmsGroups',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppCmsGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_cms_groups_with_options_async(
        self,
        request: retailcloud_20180313_models.ListAppCmsGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListAppCmsGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppCmsGroups',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppCmsGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_cms_groups(
        self,
        request: retailcloud_20180313_models.ListAppCmsGroupsRequest,
    ) -> retailcloud_20180313_models.ListAppCmsGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_cms_groups_with_options(request, runtime)

    async def list_app_cms_groups_async(
        self,
        request: retailcloud_20180313_models.ListAppCmsGroupsRequest,
    ) -> retailcloud_20180313_models.ListAppCmsGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_cms_groups_with_options_async(request, runtime)

    def list_app_environment_with_options(
        self,
        request: retailcloud_20180313_models.ListAppEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListAppEnvironmentResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppEnvironment',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_environment_with_options_async(
        self,
        request: retailcloud_20180313_models.ListAppEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListAppEnvironmentResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppEnvironment',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_environment(
        self,
        request: retailcloud_20180313_models.ListAppEnvironmentRequest,
    ) -> retailcloud_20180313_models.ListAppEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_environment_with_options(request, runtime)

    async def list_app_environment_async(
        self,
        request: retailcloud_20180313_models.ListAppEnvironmentRequest,
    ) -> retailcloud_20180313_models.ListAppEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_environment_with_options_async(request, runtime)

    def list_app_group_with_options(
        self,
        request: retailcloud_20180313_models.ListAppGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListAppGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BizCode'] = request.biz_code
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAppGroup',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_group_with_options_async(
        self,
        request: retailcloud_20180313_models.ListAppGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListAppGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BizCode'] = request.biz_code
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAppGroup',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_group(
        self,
        request: retailcloud_20180313_models.ListAppGroupRequest,
    ) -> retailcloud_20180313_models.ListAppGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_group_with_options(request, runtime)

    async def list_app_group_async(
        self,
        request: retailcloud_20180313_models.ListAppGroupRequest,
    ) -> retailcloud_20180313_models.ListAppGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_group_with_options_async(request, runtime)

    def list_app_group_mapping_with_options(
        self,
        request: retailcloud_20180313_models.ListAppGroupMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListAppGroupMappingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BizCode'] = request.biz_code
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAppGroupMapping',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppGroupMappingResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_group_mapping_with_options_async(
        self,
        request: retailcloud_20180313_models.ListAppGroupMappingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListAppGroupMappingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['BizCode'] = request.biz_code
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAppGroupMapping',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppGroupMappingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_group_mapping(
        self,
        request: retailcloud_20180313_models.ListAppGroupMappingRequest,
    ) -> retailcloud_20180313_models.ListAppGroupMappingResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_group_mapping_with_options(request, runtime)

    async def list_app_group_mapping_async(
        self,
        request: retailcloud_20180313_models.ListAppGroupMappingRequest,
    ) -> retailcloud_20180313_models.ListAppGroupMappingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_group_mapping_with_options_async(request, runtime)

    def list_app_instance_with_options(
        self,
        request: retailcloud_20180313_models.ListAppInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListAppInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAppInstance',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_instance_with_options_async(
        self,
        request: retailcloud_20180313_models.ListAppInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListAppInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAppInstance',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_instance(
        self,
        request: retailcloud_20180313_models.ListAppInstanceRequest,
    ) -> retailcloud_20180313_models.ListAppInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_instance_with_options(request, runtime)

    async def list_app_instance_async(
        self,
        request: retailcloud_20180313_models.ListAppInstanceRequest,
    ) -> retailcloud_20180313_models.ListAppInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_instance_with_options_async(request, runtime)

    def list_app_resource_allocs_with_options(
        self,
        request: retailcloud_20180313_models.ListAppResourceAllocsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListAppResourceAllocsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppResourceAllocs',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppResourceAllocsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_app_resource_allocs_with_options_async(
        self,
        request: retailcloud_20180313_models.ListAppResourceAllocsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListAppResourceAllocsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppResourceAllocs',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppResourceAllocsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_app_resource_allocs(
        self,
        request: retailcloud_20180313_models.ListAppResourceAllocsRequest,
    ) -> retailcloud_20180313_models.ListAppResourceAllocsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_app_resource_allocs_with_options(request, runtime)

    async def list_app_resource_allocs_async(
        self,
        request: retailcloud_20180313_models.ListAppResourceAllocsRequest,
    ) -> retailcloud_20180313_models.ListAppResourceAllocsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_app_resource_allocs_with_options_async(request, runtime)

    def list_available_cluster_node_with_options(
        self,
        request: retailcloud_20180313_models.ListAvailableClusterNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListAvailableClusterNodeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableClusterNode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAvailableClusterNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_available_cluster_node_with_options_async(
        self,
        request: retailcloud_20180313_models.ListAvailableClusterNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListAvailableClusterNodeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableClusterNode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAvailableClusterNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_available_cluster_node(
        self,
        request: retailcloud_20180313_models.ListAvailableClusterNodeRequest,
    ) -> retailcloud_20180313_models.ListAvailableClusterNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_available_cluster_node_with_options(request, runtime)

    async def list_available_cluster_node_async(
        self,
        request: retailcloud_20180313_models.ListAvailableClusterNodeRequest,
    ) -> retailcloud_20180313_models.ListAvailableClusterNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_available_cluster_node_with_options_async(request, runtime)

    def list_cluster_with_options(
        self,
        request: retailcloud_20180313_models.ListClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCluster',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_with_options_async(
        self,
        request: retailcloud_20180313_models.ListClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListClusterResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCluster',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster(
        self,
        request: retailcloud_20180313_models.ListClusterRequest,
    ) -> retailcloud_20180313_models.ListClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_with_options(request, runtime)

    async def list_cluster_async(
        self,
        request: retailcloud_20180313_models.ListClusterRequest,
    ) -> retailcloud_20180313_models.ListClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_with_options_async(request, runtime)

    def list_cluster_node_with_options(
        self,
        request: retailcloud_20180313_models.ListClusterNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListClusterNodeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterNode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListClusterNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_node_with_options_async(
        self,
        request: retailcloud_20180313_models.ListClusterNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListClusterNodeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterNode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListClusterNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_node(
        self,
        request: retailcloud_20180313_models.ListClusterNodeRequest,
    ) -> retailcloud_20180313_models.ListClusterNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_node_with_options(request, runtime)

    async def list_cluster_node_async(
        self,
        request: retailcloud_20180313_models.ListClusterNodeRequest,
    ) -> retailcloud_20180313_models.ListClusterNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_node_with_options_async(request, runtime)

    def list_deploy_config_with_options(
        self,
        request: retailcloud_20180313_models.ListDeployConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListDeployConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EnvType'] = request.env_type
        query['Id'] = request.id
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDeployConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListDeployConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deploy_config_with_options_async(
        self,
        request: retailcloud_20180313_models.ListDeployConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListDeployConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EnvType'] = request.env_type
        query['Id'] = request.id
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDeployConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListDeployConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deploy_config(
        self,
        request: retailcloud_20180313_models.ListDeployConfigRequest,
    ) -> retailcloud_20180313_models.ListDeployConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_deploy_config_with_options(request, runtime)

    async def list_deploy_config_async(
        self,
        request: retailcloud_20180313_models.ListDeployConfigRequest,
    ) -> retailcloud_20180313_models.ListDeployConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_deploy_config_with_options_async(request, runtime)

    def list_deploy_orders_with_options(
        self,
        request: retailcloud_20180313_models.ListDeployOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListDeployOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['DeployCategory'] = request.deploy_category
        query['DeployType'] = request.deploy_type
        query['EndTimeGreaterThan'] = request.end_time_greater_than
        query['EndTimeGreaterThanOrEqualTo'] = request.end_time_greater_than_or_equal_to
        query['EndTimeLessThan'] = request.end_time_less_than
        query['EndTimeLessThanOrEqualTo'] = request.end_time_less_than_or_equal_to
        query['EnvId'] = request.env_id
        query['EnvType'] = request.env_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['PartitionType'] = request.partition_type
        query['PauseType'] = request.pause_type
        query['StartTimeGreaterThan'] = request.start_time_greater_than
        query['StartTimeGreaterThanOrEqualTo'] = request.start_time_greater_than_or_equal_to
        query['StartTimeLessThan'] = request.start_time_less_than
        query['StartTimeLessThanOrEqualTo'] = request.start_time_less_than_or_equal_to
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDeployOrders',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListDeployOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deploy_orders_with_options_async(
        self,
        request: retailcloud_20180313_models.ListDeployOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListDeployOrdersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['DeployCategory'] = request.deploy_category
        query['DeployType'] = request.deploy_type
        query['EndTimeGreaterThan'] = request.end_time_greater_than
        query['EndTimeGreaterThanOrEqualTo'] = request.end_time_greater_than_or_equal_to
        query['EndTimeLessThan'] = request.end_time_less_than
        query['EndTimeLessThanOrEqualTo'] = request.end_time_less_than_or_equal_to
        query['EnvId'] = request.env_id
        query['EnvType'] = request.env_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['PartitionType'] = request.partition_type
        query['PauseType'] = request.pause_type
        query['StartTimeGreaterThan'] = request.start_time_greater_than
        query['StartTimeGreaterThanOrEqualTo'] = request.start_time_greater_than_or_equal_to
        query['StartTimeLessThan'] = request.start_time_less_than
        query['StartTimeLessThanOrEqualTo'] = request.start_time_less_than_or_equal_to
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDeployOrders',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListDeployOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deploy_orders(
        self,
        request: retailcloud_20180313_models.ListDeployOrdersRequest,
    ) -> retailcloud_20180313_models.ListDeployOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_deploy_orders_with_options(request, runtime)

    async def list_deploy_orders_async(
        self,
        request: retailcloud_20180313_models.ListDeployOrdersRequest,
    ) -> retailcloud_20180313_models.ListDeployOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_deploy_orders_with_options_async(request, runtime)

    def list_job_histories_with_options(
        self,
        request: retailcloud_20180313_models.ListJobHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListJobHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobHistories',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListJobHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_histories_with_options_async(
        self,
        request: retailcloud_20180313_models.ListJobHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListJobHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobHistories',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListJobHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_histories(
        self,
        request: retailcloud_20180313_models.ListJobHistoriesRequest,
    ) -> retailcloud_20180313_models.ListJobHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_job_histories_with_options(request, runtime)

    async def list_job_histories_async(
        self,
        request: retailcloud_20180313_models.ListJobHistoriesRequest,
    ) -> retailcloud_20180313_models.ListJobHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_job_histories_with_options_async(request, runtime)

    def list_node_label_bindings_with_options(
        self,
        request: retailcloud_20180313_models.ListNodeLabelBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListNodeLabelBindingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeLabelBindings',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListNodeLabelBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_label_bindings_with_options_async(
        self,
        request: retailcloud_20180313_models.ListNodeLabelBindingsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListNodeLabelBindingsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeLabelBindings',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListNodeLabelBindingsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_label_bindings(
        self,
        request: retailcloud_20180313_models.ListNodeLabelBindingsRequest,
    ) -> retailcloud_20180313_models.ListNodeLabelBindingsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_node_label_bindings_with_options(request, runtime)

    async def list_node_label_bindings_async(
        self,
        request: retailcloud_20180313_models.ListNodeLabelBindingsRequest,
    ) -> retailcloud_20180313_models.ListNodeLabelBindingsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_node_label_bindings_with_options_async(request, runtime)

    def list_node_labels_with_options(
        self,
        request: retailcloud_20180313_models.ListNodeLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListNodeLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['LabelKey'] = request.label_key
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListNodeLabels',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListNodeLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_labels_with_options_async(
        self,
        request: retailcloud_20180313_models.ListNodeLabelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListNodeLabelsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['LabelKey'] = request.label_key
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListNodeLabels',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListNodeLabelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_labels(
        self,
        request: retailcloud_20180313_models.ListNodeLabelsRequest,
    ) -> retailcloud_20180313_models.ListNodeLabelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_node_labels_with_options(request, runtime)

    async def list_node_labels_async(
        self,
        request: retailcloud_20180313_models.ListNodeLabelsRequest,
    ) -> retailcloud_20180313_models.ListNodeLabelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_node_labels_with_options_async(request, runtime)

    def list_persistent_volume_with_options(
        self,
        request: retailcloud_20180313_models.ListPersistentVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListPersistentVolumeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPersistentVolume',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListPersistentVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_persistent_volume_with_options_async(
        self,
        request: retailcloud_20180313_models.ListPersistentVolumeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListPersistentVolumeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPersistentVolume',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListPersistentVolumeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_persistent_volume(
        self,
        request: retailcloud_20180313_models.ListPersistentVolumeRequest,
    ) -> retailcloud_20180313_models.ListPersistentVolumeResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_persistent_volume_with_options(request, runtime)

    async def list_persistent_volume_async(
        self,
        request: retailcloud_20180313_models.ListPersistentVolumeRequest,
    ) -> retailcloud_20180313_models.ListPersistentVolumeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_persistent_volume_with_options_async(request, runtime)

    def list_persistent_volume_claim_with_options(
        self,
        request: retailcloud_20180313_models.ListPersistentVolumeClaimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListPersistentVolumeClaimResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EnvId'] = request.env_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPersistentVolumeClaim',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListPersistentVolumeClaimResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_persistent_volume_claim_with_options_async(
        self,
        request: retailcloud_20180313_models.ListPersistentVolumeClaimRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListPersistentVolumeClaimResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EnvId'] = request.env_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPersistentVolumeClaim',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListPersistentVolumeClaimResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_persistent_volume_claim(
        self,
        request: retailcloud_20180313_models.ListPersistentVolumeClaimRequest,
    ) -> retailcloud_20180313_models.ListPersistentVolumeClaimResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_persistent_volume_claim_with_options(request, runtime)

    async def list_persistent_volume_claim_async(
        self,
        request: retailcloud_20180313_models.ListPersistentVolumeClaimRequest,
    ) -> retailcloud_20180313_models.ListPersistentVolumeClaimResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_persistent_volume_claim_with_options_async(request, runtime)

    def list_pods_with_options(
        self,
        request: retailcloud_20180313_models.ListPodsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListPodsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeployOrderId'] = request.deploy_order_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPods',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListPodsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pods_with_options_async(
        self,
        request: retailcloud_20180313_models.ListPodsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListPodsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeployOrderId'] = request.deploy_order_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListPods',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListPodsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pods(
        self,
        request: retailcloud_20180313_models.ListPodsRequest,
    ) -> retailcloud_20180313_models.ListPodsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_pods_with_options(request, runtime)

    async def list_pods_async(
        self,
        request: retailcloud_20180313_models.ListPodsRequest,
    ) -> retailcloud_20180313_models.ListPodsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_pods_with_options_async(request, runtime)

    def list_services_with_options(
        self,
        request: retailcloud_20180313_models.ListServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EnvId'] = request.env_id
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        request: retailcloud_20180313_models.ListServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListServicesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EnvId'] = request.env_id
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(
        self,
        request: retailcloud_20180313_models.ListServicesRequest,
    ) -> retailcloud_20180313_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_services_with_options(request, runtime)

    async def list_services_async(
        self,
        request: retailcloud_20180313_models.ListServicesRequest,
    ) -> retailcloud_20180313_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_services_with_options_async(request, runtime)

    def list_slb_aps_with_options(
        self,
        request: retailcloud_20180313_models.ListSlbAPsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListSlbAPsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EnvId'] = request.env_id
        query['Name'] = request.name
        query['NetworkMode'] = request.network_mode
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SlbId'] = request.slb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListSlbAPs',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListSlbAPsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_slb_aps_with_options_async(
        self,
        request: retailcloud_20180313_models.ListSlbAPsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListSlbAPsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['EnvId'] = request.env_id
        query['Name'] = request.name
        query['NetworkMode'] = request.network_mode
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['SlbId'] = request.slb_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListSlbAPs',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListSlbAPsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_slb_aps(
        self,
        request: retailcloud_20180313_models.ListSlbAPsRequest,
    ) -> retailcloud_20180313_models.ListSlbAPsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_slb_aps_with_options(request, runtime)

    async def list_slb_aps_async(
        self,
        request: retailcloud_20180313_models.ListSlbAPsRequest,
    ) -> retailcloud_20180313_models.ListSlbAPsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_slb_aps_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: retailcloud_20180313_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: retailcloud_20180313_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: retailcloud_20180313_models.ListUsersRequest,
    ) -> retailcloud_20180313_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: retailcloud_20180313_models.ListUsersRequest,
    ) -> retailcloud_20180313_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def modify_service_with_options(
        self,
        request: retailcloud_20180313_models.ModifyServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ModifyServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyService',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ModifyServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_service_with_options_async(
        self,
        request: retailcloud_20180313_models.ModifyServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ModifyServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyService',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ModifyServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_service(
        self,
        request: retailcloud_20180313_models.ModifyServiceRequest,
    ) -> retailcloud_20180313_models.ModifyServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_service_with_options(request, runtime)

    async def modify_service_async(
        self,
        request: retailcloud_20180313_models.ModifyServiceRequest,
    ) -> retailcloud_20180313_models.ModifyServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_service_with_options_async(request, runtime)

    def modify_slb_apwith_options(
        self,
        request: retailcloud_20180313_models.ModifySlbAPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ModifySlbAPResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CookieTimeout'] = request.cookie_timeout
        query['EstablishedTimeout'] = request.established_timeout
        query['Name'] = request.name
        query['RealServerPort'] = request.real_server_port
        query['SlbAPId'] = request.slb_apid
        query['SslCertId'] = request.ssl_cert_id
        query['StickySession'] = request.sticky_session
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySlbAP',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ModifySlbAPResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_slb_apwith_options_async(
        self,
        request: retailcloud_20180313_models.ModifySlbAPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ModifySlbAPResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CookieTimeout'] = request.cookie_timeout
        query['EstablishedTimeout'] = request.established_timeout
        query['Name'] = request.name
        query['RealServerPort'] = request.real_server_port
        query['SlbAPId'] = request.slb_apid
        query['SslCertId'] = request.ssl_cert_id
        query['StickySession'] = request.sticky_session
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifySlbAP',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ModifySlbAPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_slb_ap(
        self,
        request: retailcloud_20180313_models.ModifySlbAPRequest,
    ) -> retailcloud_20180313_models.ModifySlbAPResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_slb_apwith_options(request, runtime)

    async def modify_slb_ap_async(
        self,
        request: retailcloud_20180313_models.ModifySlbAPRequest,
    ) -> retailcloud_20180313_models.ModifySlbAPResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_slb_apwith_options_async(request, runtime)

    def query_cluster_detail_with_options(
        self,
        request: retailcloud_20180313_models.QueryClusterDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.QueryClusterDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryClusterDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.QueryClusterDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cluster_detail_with_options_async(
        self,
        request: retailcloud_20180313_models.QueryClusterDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.QueryClusterDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryClusterDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.QueryClusterDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cluster_detail(
        self,
        request: retailcloud_20180313_models.QueryClusterDetailRequest,
    ) -> retailcloud_20180313_models.QueryClusterDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_cluster_detail_with_options(request, runtime)

    async def query_cluster_detail_async(
        self,
        request: retailcloud_20180313_models.QueryClusterDetailRequest,
    ) -> retailcloud_20180313_models.QueryClusterDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_cluster_detail_with_options_async(request, runtime)

    def rebuild_app_instance_with_options(
        self,
        request: retailcloud_20180313_models.RebuildAppInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.RebuildAppInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['AppInstanceId'] = request.app_instance_id
        query['EnvId'] = request.env_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RebuildAppInstance',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.RebuildAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebuild_app_instance_with_options_async(
        self,
        request: retailcloud_20180313_models.RebuildAppInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.RebuildAppInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['AppInstanceId'] = request.app_instance_id
        query['EnvId'] = request.env_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RebuildAppInstance',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.RebuildAppInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebuild_app_instance(
        self,
        request: retailcloud_20180313_models.RebuildAppInstanceRequest,
    ) -> retailcloud_20180313_models.RebuildAppInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.rebuild_app_instance_with_options(request, runtime)

    async def rebuild_app_instance_async(
        self,
        request: retailcloud_20180313_models.RebuildAppInstanceRequest,
    ) -> retailcloud_20180313_models.RebuildAppInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rebuild_app_instance_with_options_async(request, runtime)

    def remove_cluster_node_with_options(
        self,
        request: retailcloud_20180313_models.RemoveClusterNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.RemoveClusterNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterInstanceId'] = request.cluster_instance_id
        query['EcsInstanceIdList'] = request.ecs_instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveClusterNode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.RemoveClusterNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_cluster_node_with_options_async(
        self,
        request: retailcloud_20180313_models.RemoveClusterNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.RemoveClusterNodeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterInstanceId'] = request.cluster_instance_id
        query['EcsInstanceIdList'] = request.ecs_instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveClusterNode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.RemoveClusterNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_cluster_node(
        self,
        request: retailcloud_20180313_models.RemoveClusterNodeRequest,
    ) -> retailcloud_20180313_models.RemoveClusterNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_cluster_node_with_options(request, runtime)

    async def remove_cluster_node_async(
        self,
        request: retailcloud_20180313_models.RemoveClusterNodeRequest,
    ) -> retailcloud_20180313_models.RemoveClusterNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_cluster_node_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: retailcloud_20180313_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: retailcloud_20180313_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ResetAccountPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: retailcloud_20180313_models.ResetAccountPasswordRequest,
    ) -> retailcloud_20180313_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: retailcloud_20180313_models.ResetAccountPasswordRequest,
    ) -> retailcloud_20180313_models.ResetAccountPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def resource_status_notify_with_options(
        self,
        request: retailcloud_20180313_models.ResourceStatusNotifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ResourceStatusNotifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResourceStatusNotify',
            version='2018-03-13',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ResourceStatusNotifyResponse(),
            self.call_api(params, req, runtime)
        )

    async def resource_status_notify_with_options_async(
        self,
        request: retailcloud_20180313_models.ResourceStatusNotifyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ResourceStatusNotifyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResourceStatusNotify',
            version='2018-03-13',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ResourceStatusNotifyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resource_status_notify(
        self,
        request: retailcloud_20180313_models.ResourceStatusNotifyRequest,
    ) -> retailcloud_20180313_models.ResourceStatusNotifyResponse:
        runtime = util_models.RuntimeOptions()
        return self.resource_status_notify_with_options(request, runtime)

    async def resource_status_notify_async(
        self,
        request: retailcloud_20180313_models.ResourceStatusNotifyRequest,
    ) -> retailcloud_20180313_models.ResourceStatusNotifyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resource_status_notify_with_options_async(request, runtime)

    def resume_deploy_with_options(
        self,
        request: retailcloud_20180313_models.ResumeDeployRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ResumeDeployResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeployOrderId'] = request.deploy_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResumeDeploy',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ResumeDeployResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_deploy_with_options_async(
        self,
        request: retailcloud_20180313_models.ResumeDeployRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ResumeDeployResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeployOrderId'] = request.deploy_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResumeDeploy',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ResumeDeployResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_deploy(
        self,
        request: retailcloud_20180313_models.ResumeDeployRequest,
    ) -> retailcloud_20180313_models.ResumeDeployResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_deploy_with_options(request, runtime)

    async def resume_deploy_async(
        self,
        request: retailcloud_20180313_models.ResumeDeployRequest,
    ) -> retailcloud_20180313_models.ResumeDeployResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_deploy_with_options_async(request, runtime)

    def scale_app_with_options(
        self,
        request: retailcloud_20180313_models.ScaleAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ScaleAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EnvId'] = request.env_id
        query['Replicas'] = request.replicas
        query['TotalPartitions'] = request.total_partitions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ScaleApp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ScaleAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_app_with_options_async(
        self,
        request: retailcloud_20180313_models.ScaleAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.ScaleAppResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EnvId'] = request.env_id
        query['Replicas'] = request.replicas
        query['TotalPartitions'] = request.total_partitions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ScaleApp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ScaleAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_app(
        self,
        request: retailcloud_20180313_models.ScaleAppRequest,
    ) -> retailcloud_20180313_models.ScaleAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.scale_app_with_options(request, runtime)

    async def scale_app_async(
        self,
        request: retailcloud_20180313_models.ScaleAppRequest,
    ) -> retailcloud_20180313_models.ScaleAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.scale_app_with_options_async(request, runtime)

    def set_deploy_pause_type_with_options(
        self,
        request: retailcloud_20180313_models.SetDeployPauseTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.SetDeployPauseTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeployOrderId'] = request.deploy_order_id
        query['DeployPauseType'] = request.deploy_pause_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDeployPauseType',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.SetDeployPauseTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_deploy_pause_type_with_options_async(
        self,
        request: retailcloud_20180313_models.SetDeployPauseTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.SetDeployPauseTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DeployOrderId'] = request.deploy_order_id
        query['DeployPauseType'] = request.deploy_pause_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SetDeployPauseType',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.SetDeployPauseTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_deploy_pause_type(
        self,
        request: retailcloud_20180313_models.SetDeployPauseTypeRequest,
    ) -> retailcloud_20180313_models.SetDeployPauseTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_deploy_pause_type_with_options(request, runtime)

    async def set_deploy_pause_type_async(
        self,
        request: retailcloud_20180313_models.SetDeployPauseTypeRequest,
    ) -> retailcloud_20180313_models.SetDeployPauseTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_deploy_pause_type_with_options_async(request, runtime)

    def submit_info_with_options(
        self,
        request: retailcloud_20180313_models.SubmitInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.SubmitInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallerUid'] = request.caller_uid
        query['MainUserId'] = request.main_user_id
        query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitInfo',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.SubmitInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_info_with_options_async(
        self,
        request: retailcloud_20180313_models.SubmitInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.SubmitInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CallerUid'] = request.caller_uid
        query['MainUserId'] = request.main_user_id
        query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitInfo',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.SubmitInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def submit_info(
        self,
        request: retailcloud_20180313_models.SubmitInfoRequest,
    ) -> retailcloud_20180313_models.SubmitInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_info_with_options(request, runtime)

    async def submit_info_async(
        self,
        request: retailcloud_20180313_models.SubmitInfoRequest,
    ) -> retailcloud_20180313_models.SubmitInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_info_with_options_async(request, runtime)

    def sync_pod_info_with_options(
        self,
        request: retailcloud_20180313_models.SyncPodInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.SyncPodInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PodName'] = request.pod_name
        query['Reason'] = request.reason
        query['RequestId'] = request.request_id
        query['SideCarType'] = request.side_car_type
        query['Status'] = request.status
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SyncPodInfo',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.SyncPodInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_pod_info_with_options_async(
        self,
        request: retailcloud_20180313_models.SyncPodInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.SyncPodInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PodName'] = request.pod_name
        query['Reason'] = request.reason
        query['RequestId'] = request.request_id
        query['SideCarType'] = request.side_car_type
        query['Status'] = request.status
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SyncPodInfo',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.SyncPodInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_pod_info(
        self,
        request: retailcloud_20180313_models.SyncPodInfoRequest,
    ) -> retailcloud_20180313_models.SyncPodInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.sync_pod_info_with_options(request, runtime)

    async def sync_pod_info_async(
        self,
        request: retailcloud_20180313_models.SyncPodInfoRequest,
    ) -> retailcloud_20180313_models.SyncPodInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sync_pod_info_with_options_async(request, runtime)

    def unbind_group_with_options(
        self,
        request: retailcloud_20180313_models.UnbindGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.UnbindGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['BizCode'] = request.biz_code
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindGroup',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UnbindGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_group_with_options_async(
        self,
        request: retailcloud_20180313_models.UnbindGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.UnbindGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['BizCode'] = request.biz_code
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindGroup',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UnbindGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_group(
        self,
        request: retailcloud_20180313_models.UnbindGroupRequest,
    ) -> retailcloud_20180313_models.UnbindGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_group_with_options(request, runtime)

    async def unbind_group_async(
        self,
        request: retailcloud_20180313_models.UnbindGroupRequest,
    ) -> retailcloud_20180313_models.UnbindGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_group_with_options_async(request, runtime)

    def unbind_node_label_with_options(
        self,
        request: retailcloud_20180313_models.UnbindNodeLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.UnbindNodeLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['InstanceId'] = request.instance_id
        query['LabelKey'] = request.label_key
        query['LabelValue'] = request.label_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindNodeLabel',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UnbindNodeLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_node_label_with_options_async(
        self,
        request: retailcloud_20180313_models.UnbindNodeLabelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.UnbindNodeLabelResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['InstanceId'] = request.instance_id
        query['LabelKey'] = request.label_key
        query['LabelValue'] = request.label_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UnbindNodeLabel',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UnbindNodeLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_node_label(
        self,
        request: retailcloud_20180313_models.UnbindNodeLabelRequest,
    ) -> retailcloud_20180313_models.UnbindNodeLabelResponse:
        runtime = util_models.RuntimeOptions()
        return self.unbind_node_label_with_options(request, runtime)

    async def unbind_node_label_async(
        self,
        request: retailcloud_20180313_models.UnbindNodeLabelRequest,
    ) -> retailcloud_20180313_models.UnbindNodeLabelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.unbind_node_label_with_options_async(request, runtime)

    def update_app_with_options(
        self,
        request: retailcloud_20180313_models.UpdateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.UpdateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateApp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UpdateAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_with_options_async(
        self,
        request: retailcloud_20180313_models.UpdateAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.UpdateAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateApp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UpdateAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app(
        self,
        request: retailcloud_20180313_models.UpdateAppRequest,
    ) -> retailcloud_20180313_models.UpdateAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_with_options(request, runtime)

    async def update_app_async(
        self,
        request: retailcloud_20180313_models.UpdateAppRequest,
    ) -> retailcloud_20180313_models.UpdateAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_with_options_async(request, runtime)

    def update_app_monitors_with_options(
        self,
        request: retailcloud_20180313_models.UpdateAppMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.UpdateAppMonitorsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAppMonitors',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UpdateAppMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_app_monitors_with_options_async(
        self,
        request: retailcloud_20180313_models.UpdateAppMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.UpdateAppMonitorsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAppMonitors',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UpdateAppMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_app_monitors(
        self,
        request: retailcloud_20180313_models.UpdateAppMonitorsRequest,
    ) -> retailcloud_20180313_models.UpdateAppMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_app_monitors_with_options(request, runtime)

    async def update_app_monitors_async(
        self,
        request: retailcloud_20180313_models.UpdateAppMonitorsRequest,
    ) -> retailcloud_20180313_models.UpdateAppMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_app_monitors_with_options_async(request, runtime)

    def update_deploy_config_with_options(
        self,
        request: retailcloud_20180313_models.UpdateDeployConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.UpdateDeployConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CodePath'] = request.code_path
        query['ConfigMap'] = request.config_map
        query['ConfigMapList'] = request.config_map_list
        query['CronJob'] = request.cron_job
        query['Deployment'] = request.deployment
        query['Id'] = request.id
        query['SecretList'] = request.secret_list
        query['StatefulSet'] = request.stateful_set
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDeployConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UpdateDeployConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_deploy_config_with_options_async(
        self,
        request: retailcloud_20180313_models.UpdateDeployConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.UpdateDeployConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CodePath'] = request.code_path
        query['ConfigMap'] = request.config_map
        query['ConfigMapList'] = request.config_map_list
        query['CronJob'] = request.cron_job
        query['Deployment'] = request.deployment
        query['Id'] = request.id
        query['SecretList'] = request.secret_list
        query['StatefulSet'] = request.stateful_set
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDeployConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UpdateDeployConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_deploy_config(
        self,
        request: retailcloud_20180313_models.UpdateDeployConfigRequest,
    ) -> retailcloud_20180313_models.UpdateDeployConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_deploy_config_with_options(request, runtime)

    async def update_deploy_config_async(
        self,
        request: retailcloud_20180313_models.UpdateDeployConfigRequest,
    ) -> retailcloud_20180313_models.UpdateDeployConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_deploy_config_with_options_async(request, runtime)

    def update_eci_config_with_options(
        self,
        request: retailcloud_20180313_models.UpdateEciConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.UpdateEciConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppEnvId'] = request.app_env_id
        query['EipBandwidth'] = request.eip_bandwidth
        query['EnableEciSchedulePolicy'] = request.enable_eci_schedule_policy
        query['MirrorCache'] = request.mirror_cache
        query['NormalInstanceLimit'] = request.normal_instance_limit
        query['ScheduleVirtualNode'] = request.schedule_virtual_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateEciConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UpdateEciConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_eci_config_with_options_async(
        self,
        request: retailcloud_20180313_models.UpdateEciConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.UpdateEciConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppEnvId'] = request.app_env_id
        query['EipBandwidth'] = request.eip_bandwidth
        query['EnableEciSchedulePolicy'] = request.enable_eci_schedule_policy
        query['MirrorCache'] = request.mirror_cache
        query['NormalInstanceLimit'] = request.normal_instance_limit
        query['ScheduleVirtualNode'] = request.schedule_virtual_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateEciConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UpdateEciConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_eci_config(
        self,
        request: retailcloud_20180313_models.UpdateEciConfigRequest,
    ) -> retailcloud_20180313_models.UpdateEciConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_eci_config_with_options(request, runtime)

    async def update_eci_config_async(
        self,
        request: retailcloud_20180313_models.UpdateEciConfigRequest,
    ) -> retailcloud_20180313_models.UpdateEciConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_eci_config_with_options_async(request, runtime)

    def update_environment_with_options(
        self,
        request: retailcloud_20180313_models.UpdateEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.UpdateEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppEnvId'] = request.app_env_id
        query['AppId'] = request.app_id
        query['AppSchemaId'] = request.app_schema_id
        query['Replicas'] = request.replicas
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateEnvironment',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UpdateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_environment_with_options_async(
        self,
        request: retailcloud_20180313_models.UpdateEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> retailcloud_20180313_models.UpdateEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppEnvId'] = request.app_env_id
        query['AppId'] = request.app_id
        query['AppSchemaId'] = request.app_schema_id
        query['Replicas'] = request.replicas
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateEnvironment',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UpdateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_environment(
        self,
        request: retailcloud_20180313_models.UpdateEnvironmentRequest,
    ) -> retailcloud_20180313_models.UpdateEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_environment_with_options(request, runtime)

    async def update_environment_async(
        self,
        request: retailcloud_20180313_models.UpdateEnvironmentRequest,
    ) -> retailcloud_20180313_models.UpdateEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_environment_with_options_async(request, runtime)
