# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mse20190531 import models as mse_20190531_models
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
        self.check_config(config)
        self._endpoint = self.get_endpoint('mse', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_mock_rule_with_options(
        self,
        request: mse_20190531_models.AddMockRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.AddMockRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConsumerAppIds'] = request.consumer_app_ids
        query['DubboMockItems'] = request.dubbo_mock_items
        query['Enable'] = request.enable
        query['ExtraJson'] = request.extra_json
        query['MockType'] = request.mock_type
        query['Name'] = request.name
        query['ProviderAppId'] = request.provider_app_id
        query['ProviderAppName'] = request.provider_app_name
        query['Region'] = request.region
        query['ScMockItems'] = request.sc_mock_items
        query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddMockRule',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.AddMockRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_mock_rule_with_options_async(
        self,
        request: mse_20190531_models.AddMockRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.AddMockRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConsumerAppIds'] = request.consumer_app_ids
        query['DubboMockItems'] = request.dubbo_mock_items
        query['Enable'] = request.enable
        query['ExtraJson'] = request.extra_json
        query['MockType'] = request.mock_type
        query['Name'] = request.name
        query['ProviderAppId'] = request.provider_app_id
        query['ProviderAppName'] = request.provider_app_name
        query['Region'] = request.region
        query['ScMockItems'] = request.sc_mock_items
        query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddMockRule',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.AddMockRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_mock_rule(
        self,
        request: mse_20190531_models.AddMockRuleRequest,
    ) -> mse_20190531_models.AddMockRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_mock_rule_with_options(request, runtime)

    async def add_mock_rule_async(
        self,
        request: mse_20190531_models.AddMockRuleRequest,
    ) -> mse_20190531_models.AddMockRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_mock_rule_with_options_async(request, runtime)

    def add_service_source_with_options(
        self,
        request: mse_20190531_models.AddServiceSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.AddServiceSourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Address'] = request.address
        query['GatewayId'] = request.gateway_id
        query['GatewayUniqueId'] = request.gateway_unique_id
        query['Info1'] = request.info_1
        query['Info2'] = request.info_2
        query['Name'] = request.name
        query['Source'] = request.source
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddServiceSource',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.AddServiceSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_service_source_with_options_async(
        self,
        request: mse_20190531_models.AddServiceSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.AddServiceSourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Address'] = request.address
        query['GatewayId'] = request.gateway_id
        query['GatewayUniqueId'] = request.gateway_unique_id
        query['Info1'] = request.info_1
        query['Info2'] = request.info_2
        query['Name'] = request.name
        query['Source'] = request.source
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddServiceSource',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.AddServiceSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_service_source(
        self,
        request: mse_20190531_models.AddServiceSourceRequest,
    ) -> mse_20190531_models.AddServiceSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_service_source_with_options(request, runtime)

    async def add_service_source_async(
        self,
        request: mse_20190531_models.AddServiceSourceRequest,
    ) -> mse_20190531_models.AddServiceSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_service_source_with_options_async(request, runtime)

    def clone_nacos_config_with_options(
        self,
        request: mse_20190531_models.CloneNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CloneNacosConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Ids'] = request.ids
        query['InstanceId'] = request.instance_id
        query['OriginNamespaceId'] = request.origin_namespace_id
        query['Policy'] = request.policy
        query['TargetNamespaceId'] = request.target_namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CloneNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CloneNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_nacos_config_with_options_async(
        self,
        request: mse_20190531_models.CloneNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CloneNacosConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Ids'] = request.ids
        query['InstanceId'] = request.instance_id
        query['OriginNamespaceId'] = request.origin_namespace_id
        query['Policy'] = request.policy
        query['TargetNamespaceId'] = request.target_namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CloneNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CloneNacosConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def clone_nacos_config(
        self,
        request: mse_20190531_models.CloneNacosConfigRequest,
    ) -> mse_20190531_models.CloneNacosConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.clone_nacos_config_with_options(request, runtime)

    async def clone_nacos_config_async(
        self,
        request: mse_20190531_models.CloneNacosConfigRequest,
    ) -> mse_20190531_models.CloneNacosConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clone_nacos_config_with_options_async(request, runtime)

    def create_alarm_rule_with_options(
        self,
        tmp_req: mse_20190531_models.CreateAlarmRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateAlarmRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.CreateAlarmRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alert_way):
            request.alert_way_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_way, 'AlertWay', 'json')
        if not UtilClient.is_unset(tmp_req.contact_group_ids):
            request.contact_group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact_group_ids, 'ContactGroupIds', 'json')
        query = {}
        query['Aggregates'] = request.aggregates
        query['AlarmAliasName'] = request.alarm_alias_name
        query['AlarmItem'] = request.alarm_item
        query['AlertWay'] = request.alert_way_shrink
        query['ContactGroupIds'] = request.contact_group_ids_shrink
        query['InstanceId'] = request.instance_id
        query['NValue'] = request.nvalue
        query['Operator'] = request.operator
        query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAlarmRule',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateAlarmRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alarm_rule_with_options_async(
        self,
        tmp_req: mse_20190531_models.CreateAlarmRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateAlarmRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.CreateAlarmRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alert_way):
            request.alert_way_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_way, 'AlertWay', 'json')
        if not UtilClient.is_unset(tmp_req.contact_group_ids):
            request.contact_group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact_group_ids, 'ContactGroupIds', 'json')
        query = {}
        query['Aggregates'] = request.aggregates
        query['AlarmAliasName'] = request.alarm_alias_name
        query['AlarmItem'] = request.alarm_item
        query['AlertWay'] = request.alert_way_shrink
        query['ContactGroupIds'] = request.contact_group_ids_shrink
        query['InstanceId'] = request.instance_id
        query['NValue'] = request.nvalue
        query['Operator'] = request.operator
        query['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAlarmRule',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateAlarmRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alarm_rule(
        self,
        request: mse_20190531_models.CreateAlarmRuleRequest,
    ) -> mse_20190531_models.CreateAlarmRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_alarm_rule_with_options(request, runtime)

    async def create_alarm_rule_async(
        self,
        request: mse_20190531_models.CreateAlarmRuleRequest,
    ) -> mse_20190531_models.CreateAlarmRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_alarm_rule_with_options_async(request, runtime)

    def create_application_with_options(
        self,
        request: mse_20190531_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppName'] = request.app_name
        query['ExtraInfo'] = request.extra_info
        query['Language'] = request.language
        query['Region'] = request.region
        query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_application_with_options_async(
        self,
        request: mse_20190531_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppName'] = request.app_name
        query['ExtraInfo'] = request.extra_info
        query['Language'] = request.language
        query['Region'] = request.region
        query['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateApplication',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_application(
        self,
        request: mse_20190531_models.CreateApplicationRequest,
    ) -> mse_20190531_models.CreateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    async def create_application_async(
        self,
        request: mse_20190531_models.CreateApplicationRequest,
    ) -> mse_20190531_models.CreateApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_application_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        request: mse_20190531_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterSpecification'] = request.cluster_specification
        query['ClusterType'] = request.cluster_type
        query['ClusterVersion'] = request.cluster_version
        query['ConnectionType'] = request.connection_type
        query['DiskCapacity'] = request.disk_capacity
        query['DiskType'] = request.disk_type
        query['InstanceCount'] = request.instance_count
        query['MseVersion'] = request.mse_version
        query['NetType'] = request.net_type
        query['PrivateSlbSpecification'] = request.private_slb_specification
        query['PubNetworkFlow'] = request.pub_network_flow
        query['PubSlbSpecification'] = request.pub_slb_specification
        query['Region'] = request.region
        query['RequestPars'] = request.request_pars
        query['VSwitchId'] = request.v_switch_id
        query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: mse_20190531_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterSpecification'] = request.cluster_specification
        query['ClusterType'] = request.cluster_type
        query['ClusterVersion'] = request.cluster_version
        query['ConnectionType'] = request.connection_type
        query['DiskCapacity'] = request.disk_capacity
        query['DiskType'] = request.disk_type
        query['InstanceCount'] = request.instance_count
        query['MseVersion'] = request.mse_version
        query['NetType'] = request.net_type
        query['PrivateSlbSpecification'] = request.private_slb_specification
        query['PubNetworkFlow'] = request.pub_network_flow
        query['PubSlbSpecification'] = request.pub_slb_specification
        query['Region'] = request.region
        query['RequestPars'] = request.request_pars
        query['VSwitchId'] = request.v_switch_id
        query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: mse_20190531_models.CreateClusterRequest,
    ) -> mse_20190531_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: mse_20190531_models.CreateClusterRequest,
    ) -> mse_20190531_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_engine_namespace_with_options(
        self,
        request: mse_20190531_models.CreateEngineNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateEngineNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Desc'] = request.desc
        query['InstanceId'] = request.instance_id
        query['Name'] = request.name
        query['ServiceCount'] = request.service_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateEngineNamespace',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateEngineNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_engine_namespace_with_options_async(
        self,
        request: mse_20190531_models.CreateEngineNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateEngineNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Desc'] = request.desc
        query['InstanceId'] = request.instance_id
        query['Name'] = request.name
        query['ServiceCount'] = request.service_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateEngineNamespace',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateEngineNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_engine_namespace(
        self,
        request: mse_20190531_models.CreateEngineNamespaceRequest,
    ) -> mse_20190531_models.CreateEngineNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_engine_namespace_with_options(request, runtime)

    async def create_engine_namespace_async(
        self,
        request: mse_20190531_models.CreateEngineNamespaceRequest,
    ) -> mse_20190531_models.CreateEngineNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_engine_namespace_with_options_async(request, runtime)

    def create_governance_kubernetes_cluster_with_options(
        self,
        request: mse_20190531_models.CreateGovernanceKubernetesClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateGovernanceKubernetesClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['ClusterName'] = request.cluster_name
        query['K8sVersion'] = request.k_8s_version
        query['NameSpaceInfos'] = request.name_space_infos
        query['PilotStartTime'] = request.pilot_start_time
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateGovernanceKubernetesCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateGovernanceKubernetesClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_governance_kubernetes_cluster_with_options_async(
        self,
        request: mse_20190531_models.CreateGovernanceKubernetesClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateGovernanceKubernetesClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['ClusterName'] = request.cluster_name
        query['K8sVersion'] = request.k_8s_version
        query['NameSpaceInfos'] = request.name_space_infos
        query['PilotStartTime'] = request.pilot_start_time
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateGovernanceKubernetesCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateGovernanceKubernetesClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_governance_kubernetes_cluster(
        self,
        request: mse_20190531_models.CreateGovernanceKubernetesClusterRequest,
    ) -> mse_20190531_models.CreateGovernanceKubernetesClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_governance_kubernetes_cluster_with_options(request, runtime)

    async def create_governance_kubernetes_cluster_async(
        self,
        request: mse_20190531_models.CreateGovernanceKubernetesClusterRequest,
    ) -> mse_20190531_models.CreateGovernanceKubernetesClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_governance_kubernetes_cluster_with_options_async(request, runtime)

    def create_nacos_config_with_options(
        self,
        request: mse_20190531_models.CreateNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateNacosConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppName'] = request.app_name
        query['BetaIps'] = request.beta_ips
        query['Content'] = request.content
        query['DataId'] = request.data_id
        query['Desc'] = request.desc
        query['Group'] = request.group
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        query['Tags'] = request.tags
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_nacos_config_with_options_async(
        self,
        request: mse_20190531_models.CreateNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateNacosConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppName'] = request.app_name
        query['BetaIps'] = request.beta_ips
        query['Content'] = request.content
        query['DataId'] = request.data_id
        query['Desc'] = request.desc
        query['Group'] = request.group
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        query['Tags'] = request.tags
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateNacosConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_nacos_config(
        self,
        request: mse_20190531_models.CreateNacosConfigRequest,
    ) -> mse_20190531_models.CreateNacosConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_nacos_config_with_options(request, runtime)

    async def create_nacos_config_async(
        self,
        request: mse_20190531_models.CreateNacosConfigRequest,
    ) -> mse_20190531_models.CreateNacosConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_nacos_config_with_options_async(request, runtime)

    def create_znode_with_options(
        self,
        request: mse_20190531_models.CreateZnodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateZnodeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Data'] = request.data
        query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateZnode',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateZnodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_znode_with_options_async(
        self,
        request: mse_20190531_models.CreateZnodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateZnodeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Data'] = request.data
        query['Path'] = request.path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateZnode',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateZnodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_znode(
        self,
        request: mse_20190531_models.CreateZnodeRequest,
    ) -> mse_20190531_models.CreateZnodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_znode_with_options(request, runtime)

    async def create_znode_async(
        self,
        request: mse_20190531_models.CreateZnodeRequest,
    ) -> mse_20190531_models.CreateZnodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_znode_with_options_async(request, runtime)

    def delete_alarm_rule_with_options(
        self,
        request: mse_20190531_models.DeleteAlarmRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteAlarmRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlarmRuleId'] = request.alarm_rule_id
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAlarmRule',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteAlarmRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alarm_rule_with_options_async(
        self,
        request: mse_20190531_models.DeleteAlarmRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteAlarmRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlarmRuleId'] = request.alarm_rule_id
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAlarmRule',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteAlarmRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alarm_rule(
        self,
        request: mse_20190531_models.DeleteAlarmRuleRequest,
    ) -> mse_20190531_models.DeleteAlarmRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alarm_rule_with_options(request, runtime)

    async def delete_alarm_rule_async(
        self,
        request: mse_20190531_models.DeleteAlarmRuleRequest,
    ) -> mse_20190531_models.DeleteAlarmRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alarm_rule_with_options_async(request, runtime)

    def delete_cluster_with_options(
        self,
        request: mse_20190531_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: mse_20190531_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster(
        self,
        request: mse_20190531_models.DeleteClusterRequest,
    ) -> mse_20190531_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    async def delete_cluster_async(
        self,
        request: mse_20190531_models.DeleteClusterRequest,
    ) -> mse_20190531_models.DeleteClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_with_options_async(request, runtime)

    def delete_engine_namespace_with_options(
        self,
        request: mse_20190531_models.DeleteEngineNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteEngineNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Id'] = request.id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteEngineNamespace',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteEngineNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_engine_namespace_with_options_async(
        self,
        request: mse_20190531_models.DeleteEngineNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteEngineNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Id'] = request.id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteEngineNamespace',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteEngineNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_engine_namespace(
        self,
        request: mse_20190531_models.DeleteEngineNamespaceRequest,
    ) -> mse_20190531_models.DeleteEngineNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_engine_namespace_with_options(request, runtime)

    async def delete_engine_namespace_async(
        self,
        request: mse_20190531_models.DeleteEngineNamespaceRequest,
    ) -> mse_20190531_models.DeleteEngineNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_engine_namespace_with_options_async(request, runtime)

    def delete_nacos_config_with_options(
        self,
        request: mse_20190531_models.DeleteNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteNacosConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Beta'] = request.beta
        query['DataId'] = request.data_id
        query['Group'] = request.group
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nacos_config_with_options_async(
        self,
        request: mse_20190531_models.DeleteNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteNacosConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Beta'] = request.beta
        query['DataId'] = request.data_id
        query['Group'] = request.group
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nacos_config(
        self,
        request: mse_20190531_models.DeleteNacosConfigRequest,
    ) -> mse_20190531_models.DeleteNacosConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_nacos_config_with_options(request, runtime)

    async def delete_nacos_config_async(
        self,
        request: mse_20190531_models.DeleteNacosConfigRequest,
    ) -> mse_20190531_models.DeleteNacosConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_nacos_config_with_options_async(request, runtime)

    def delete_nacos_configs_with_options(
        self,
        request: mse_20190531_models.DeleteNacosConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteNacosConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Ids'] = request.ids
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteNacosConfigs',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nacos_configs_with_options_async(
        self,
        request: mse_20190531_models.DeleteNacosConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteNacosConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Ids'] = request.ids
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteNacosConfigs',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nacos_configs(
        self,
        request: mse_20190531_models.DeleteNacosConfigsRequest,
    ) -> mse_20190531_models.DeleteNacosConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_nacos_configs_with_options(request, runtime)

    async def delete_nacos_configs_async(
        self,
        request: mse_20190531_models.DeleteNacosConfigsRequest,
    ) -> mse_20190531_models.DeleteNacosConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_nacos_configs_with_options_async(request, runtime)

    def delete_nacos_service_with_options(
        self,
        request: mse_20190531_models.DeleteNacosServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteNacosServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupName'] = request.group_name
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteNacosService',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_nacos_service_with_options_async(
        self,
        request: mse_20190531_models.DeleteNacosServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteNacosServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GroupName'] = request.group_name
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteNacosService',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_nacos_service(
        self,
        request: mse_20190531_models.DeleteNacosServiceRequest,
    ) -> mse_20190531_models.DeleteNacosServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_nacos_service_with_options(request, runtime)

    async def delete_nacos_service_async(
        self,
        request: mse_20190531_models.DeleteNacosServiceRequest,
    ) -> mse_20190531_models.DeleteNacosServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_nacos_service_with_options_async(request, runtime)

    def delete_znode_with_options(
        self,
        request: mse_20190531_models.DeleteZnodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteZnodeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Path'] = request.path
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteZnode',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteZnodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_znode_with_options_async(
        self,
        request: mse_20190531_models.DeleteZnodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteZnodeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Path'] = request.path
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteZnode',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteZnodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_znode(
        self,
        request: mse_20190531_models.DeleteZnodeRequest,
    ) -> mse_20190531_models.DeleteZnodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_znode_with_options(request, runtime)

    async def delete_znode_async(
        self,
        request: mse_20190531_models.DeleteZnodeRequest,
    ) -> mse_20190531_models.DeleteZnodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_znode_with_options_async(request, runtime)

    def export_nacos_config_with_options(
        self,
        request: mse_20190531_models.ExportNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ExportNacosConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppName'] = request.app_name
        query['DataId'] = request.data_id
        query['Group'] = request.group
        query['Ids'] = request.ids
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ExportNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ExportNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_nacos_config_with_options_async(
        self,
        request: mse_20190531_models.ExportNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ExportNacosConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppName'] = request.app_name
        query['DataId'] = request.data_id
        query['Group'] = request.group
        query['Ids'] = request.ids
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ExportNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ExportNacosConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_nacos_config(
        self,
        request: mse_20190531_models.ExportNacosConfigRequest,
    ) -> mse_20190531_models.ExportNacosConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_nacos_config_with_options(request, runtime)

    async def export_nacos_config_async(
        self,
        request: mse_20190531_models.ExportNacosConfigRequest,
    ) -> mse_20190531_models.ExportNacosConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_nacos_config_with_options_async(request, runtime)

    def get_engine_namepace_with_options(
        self,
        request: mse_20190531_models.GetEngineNamepaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetEngineNamepaceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Id'] = request.id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetEngineNamepace',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetEngineNamepaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_engine_namepace_with_options_async(
        self,
        request: mse_20190531_models.GetEngineNamepaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetEngineNamepaceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Id'] = request.id
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetEngineNamepace',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetEngineNamepaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_engine_namepace(
        self,
        request: mse_20190531_models.GetEngineNamepaceRequest,
    ) -> mse_20190531_models.GetEngineNamepaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_engine_namepace_with_options(request, runtime)

    async def get_engine_namepace_async(
        self,
        request: mse_20190531_models.GetEngineNamepaceRequest,
    ) -> mse_20190531_models.GetEngineNamepaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_engine_namepace_with_options_async(request, runtime)

    def get_gateway_with_options(
        self,
        request: mse_20190531_models.GetGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetGatewayResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGateway',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_with_options_async(
        self,
        request: mse_20190531_models.GetGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetGatewayResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGateway',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway(
        self,
        request: mse_20190531_models.GetGatewayRequest,
    ) -> mse_20190531_models.GetGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_gateway_with_options(request, runtime)

    async def get_gateway_async(
        self,
        request: mse_20190531_models.GetGatewayRequest,
    ) -> mse_20190531_models.GetGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_gateway_with_options_async(request, runtime)

    def get_gateway_option_with_options(
        self,
        request: mse_20190531_models.GetGatewayOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetGatewayOptionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetGatewayOption',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGatewayOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_gateway_option_with_options_async(
        self,
        request: mse_20190531_models.GetGatewayOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetGatewayOptionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GatewayId'] = request.gateway_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetGatewayOption',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGatewayOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_gateway_option(
        self,
        request: mse_20190531_models.GetGatewayOptionRequest,
    ) -> mse_20190531_models.GetGatewayOptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_gateway_option_with_options(request, runtime)

    async def get_gateway_option_async(
        self,
        request: mse_20190531_models.GetGatewayOptionRequest,
    ) -> mse_20190531_models.GetGatewayOptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_gateway_option_with_options_async(request, runtime)

    def get_governance_kubernetes_cluster_with_options(
        self,
        request: mse_20190531_models.GetGovernanceKubernetesClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetGovernanceKubernetesClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetGovernanceKubernetesCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGovernanceKubernetesClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_governance_kubernetes_cluster_with_options_async(
        self,
        request: mse_20190531_models.GetGovernanceKubernetesClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetGovernanceKubernetesClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetGovernanceKubernetesCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGovernanceKubernetesClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_governance_kubernetes_cluster(
        self,
        request: mse_20190531_models.GetGovernanceKubernetesClusterRequest,
    ) -> mse_20190531_models.GetGovernanceKubernetesClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_governance_kubernetes_cluster_with_options(request, runtime)

    async def get_governance_kubernetes_cluster_async(
        self,
        request: mse_20190531_models.GetGovernanceKubernetesClusterRequest,
    ) -> mse_20190531_models.GetGovernanceKubernetesClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_governance_kubernetes_cluster_with_options_async(request, runtime)

    def get_governance_kubernetes_cluster_list_with_options(
        self,
        request: mse_20190531_models.GetGovernanceKubernetesClusterListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetGovernanceKubernetesClusterListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['ClusterName'] = request.cluster_name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetGovernanceKubernetesClusterList',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGovernanceKubernetesClusterListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_governance_kubernetes_cluster_list_with_options_async(
        self,
        request: mse_20190531_models.GetGovernanceKubernetesClusterListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetGovernanceKubernetesClusterListResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['ClusterName'] = request.cluster_name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetGovernanceKubernetesClusterList',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGovernanceKubernetesClusterListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_governance_kubernetes_cluster_list(
        self,
        request: mse_20190531_models.GetGovernanceKubernetesClusterListRequest,
    ) -> mse_20190531_models.GetGovernanceKubernetesClusterListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_governance_kubernetes_cluster_list_with_options(request, runtime)

    async def get_governance_kubernetes_cluster_list_async(
        self,
        request: mse_20190531_models.GetGovernanceKubernetesClusterListRequest,
    ) -> mse_20190531_models.GetGovernanceKubernetesClusterListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_governance_kubernetes_cluster_list_with_options_async(request, runtime)

    def get_image_with_options(
        self,
        request: mse_20190531_models.GetImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetImageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['VersionCode'] = request.version_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_image_with_options_async(
        self,
        request: mse_20190531_models.GetImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetImageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['VersionCode'] = request.version_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetImage',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_image(
        self,
        request: mse_20190531_models.GetImageRequest,
    ) -> mse_20190531_models.GetImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_image_with_options(request, runtime)

    async def get_image_async(
        self,
        request: mse_20190531_models.GetImageRequest,
    ) -> mse_20190531_models.GetImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_image_with_options_async(request, runtime)

    def get_import_file_url_with_options(
        self,
        request: mse_20190531_models.GetImportFileUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetImportFileUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContentType'] = request.content_type
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetImportFileUrl',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetImportFileUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_import_file_url_with_options_async(
        self,
        request: mse_20190531_models.GetImportFileUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetImportFileUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ContentType'] = request.content_type
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetImportFileUrl',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetImportFileUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_import_file_url(
        self,
        request: mse_20190531_models.GetImportFileUrlRequest,
    ) -> mse_20190531_models.GetImportFileUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_import_file_url_with_options(request, runtime)

    async def get_import_file_url_async(
        self,
        request: mse_20190531_models.GetImportFileUrlRequest,
    ) -> mse_20190531_models.GetImportFileUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_import_file_url_with_options_async(request, runtime)

    def get_mse_feature_switch_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetMseFeatureSwitchResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetMseFeatureSwitch',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetMseFeatureSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_mse_feature_switch_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetMseFeatureSwitchResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetMseFeatureSwitch',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetMseFeatureSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_mse_feature_switch(self) -> mse_20190531_models.GetMseFeatureSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_mse_feature_switch_with_options(runtime)

    async def get_mse_feature_switch_async(self) -> mse_20190531_models.GetMseFeatureSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_mse_feature_switch_with_options_async(runtime)

    def get_nacos_config_with_options(
        self,
        request: mse_20190531_models.GetNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetNacosConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Beta'] = request.beta
        query['DataId'] = request.data_id
        query['Group'] = request.group
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_nacos_config_with_options_async(
        self,
        request: mse_20190531_models.GetNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetNacosConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Beta'] = request.beta
        query['DataId'] = request.data_id
        query['Group'] = request.group
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetNacosConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_nacos_config(
        self,
        request: mse_20190531_models.GetNacosConfigRequest,
    ) -> mse_20190531_models.GetNacosConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_nacos_config_with_options(request, runtime)

    async def get_nacos_config_async(
        self,
        request: mse_20190531_models.GetNacosConfigRequest,
    ) -> mse_20190531_models.GetNacosConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_nacos_config_with_options_async(request, runtime)

    def get_nacos_history_config_with_options(
        self,
        request: mse_20190531_models.GetNacosHistoryConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetNacosHistoryConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DataId'] = request.data_id
        query['Group'] = request.group
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        query['Nid'] = request.nid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetNacosHistoryConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetNacosHistoryConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_nacos_history_config_with_options_async(
        self,
        request: mse_20190531_models.GetNacosHistoryConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetNacosHistoryConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DataId'] = request.data_id
        query['Group'] = request.group
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        query['Nid'] = request.nid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetNacosHistoryConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetNacosHistoryConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_nacos_history_config(
        self,
        request: mse_20190531_models.GetNacosHistoryConfigRequest,
    ) -> mse_20190531_models.GetNacosHistoryConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_nacos_history_config_with_options(request, runtime)

    async def get_nacos_history_config_async(
        self,
        request: mse_20190531_models.GetNacosHistoryConfigRequest,
    ) -> mse_20190531_models.GetNacosHistoryConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_nacos_history_config_with_options_async(request, runtime)

    def get_overview_with_options(
        self,
        request: mse_20190531_models.GetOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Period'] = request.period
        query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetOverview',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetOverviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_overview_with_options_async(
        self,
        request: mse_20190531_models.GetOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetOverviewResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Period'] = request.period
        query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetOverview',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.GetOverviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_overview(
        self,
        request: mse_20190531_models.GetOverviewRequest,
    ) -> mse_20190531_models.GetOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_overview_with_options(request, runtime)

    async def get_overview_async(
        self,
        request: mse_20190531_models.GetOverviewRequest,
    ) -> mse_20190531_models.GetOverviewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_overview_with_options_async(request, runtime)

    def import_nacos_config_with_options(
        self,
        request: mse_20190531_models.ImportNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ImportNacosConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileUrl'] = request.file_url
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        query['Policy'] = request.policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ImportNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ImportNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_nacos_config_with_options_async(
        self,
        request: mse_20190531_models.ImportNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ImportNacosConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FileUrl'] = request.file_url
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        query['Policy'] = request.policy
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ImportNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ImportNacosConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_nacos_config(
        self,
        request: mse_20190531_models.ImportNacosConfigRequest,
    ) -> mse_20190531_models.ImportNacosConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_nacos_config_with_options(request, runtime)

    async def import_nacos_config_async(
        self,
        request: mse_20190531_models.ImportNacosConfigRequest,
    ) -> mse_20190531_models.ImportNacosConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_nacos_config_with_options_async(request, runtime)

    def list_alarm_contact_groups_with_options(
        self,
        request: mse_20190531_models.ListAlarmContactGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAlarmContactGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmContactGroups',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmContactGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alarm_contact_groups_with_options_async(
        self,
        request: mse_20190531_models.ListAlarmContactGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAlarmContactGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmContactGroups',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmContactGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alarm_contact_groups(
        self,
        request: mse_20190531_models.ListAlarmContactGroupsRequest,
    ) -> mse_20190531_models.ListAlarmContactGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_contact_groups_with_options(request, runtime)

    async def list_alarm_contact_groups_async(
        self,
        request: mse_20190531_models.ListAlarmContactGroupsRequest,
    ) -> mse_20190531_models.ListAlarmContactGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_alarm_contact_groups_with_options_async(request, runtime)

    def list_alarm_histories_with_options(
        self,
        request: mse_20190531_models.ListAlarmHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAlarmHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmHistories',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alarm_histories_with_options_async(
        self,
        request: mse_20190531_models.ListAlarmHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAlarmHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmHistories',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alarm_histories(
        self,
        request: mse_20190531_models.ListAlarmHistoriesRequest,
    ) -> mse_20190531_models.ListAlarmHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_histories_with_options(request, runtime)

    async def list_alarm_histories_async(
        self,
        request: mse_20190531_models.ListAlarmHistoriesRequest,
    ) -> mse_20190531_models.ListAlarmHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_alarm_histories_with_options_async(request, runtime)

    def list_alarm_items_with_options(
        self,
        request: mse_20190531_models.ListAlarmItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAlarmItemsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmItems',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alarm_items_with_options_async(
        self,
        request: mse_20190531_models.ListAlarmItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAlarmItemsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmItems',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alarm_items(
        self,
        request: mse_20190531_models.ListAlarmItemsRequest,
    ) -> mse_20190531_models.ListAlarmItemsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_items_with_options(request, runtime)

    async def list_alarm_items_async(
        self,
        request: mse_20190531_models.ListAlarmItemsRequest,
    ) -> mse_20190531_models.ListAlarmItemsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_alarm_items_with_options_async(request, runtime)

    def list_alarm_rules_with_options(
        self,
        request: mse_20190531_models.ListAlarmRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAlarmRulesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmRules',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alarm_rules_with_options_async(
        self,
        request: mse_20190531_models.ListAlarmRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAlarmRulesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlarmRules',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alarm_rules(
        self,
        request: mse_20190531_models.ListAlarmRulesRequest,
    ) -> mse_20190531_models.ListAlarmRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_rules_with_options(request, runtime)

    async def list_alarm_rules_async(
        self,
        request: mse_20190531_models.ListAlarmRulesRequest,
    ) -> mse_20190531_models.ListAlarmRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_alarm_rules_with_options_async(request, runtime)

    def list_ans_instances_with_options(
        self,
        request: mse_20190531_models.ListAnsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAnsInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnsInstances',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ans_instances_with_options_async(
        self,
        request: mse_20190531_models.ListAnsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAnsInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnsInstances',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ans_instances(
        self,
        request: mse_20190531_models.ListAnsInstancesRequest,
    ) -> mse_20190531_models.ListAnsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ans_instances_with_options(request, runtime)

    async def list_ans_instances_async(
        self,
        request: mse_20190531_models.ListAnsInstancesRequest,
    ) -> mse_20190531_models.ListAnsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ans_instances_with_options_async(request, runtime)

    def list_ans_service_clusters_with_options(
        self,
        request: mse_20190531_models.ListAnsServiceClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAnsServiceClustersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnsServiceClusters',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsServiceClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ans_service_clusters_with_options_async(
        self,
        request: mse_20190531_models.ListAnsServiceClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAnsServiceClustersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnsServiceClusters',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsServiceClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ans_service_clusters(
        self,
        request: mse_20190531_models.ListAnsServiceClustersRequest,
    ) -> mse_20190531_models.ListAnsServiceClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ans_service_clusters_with_options(request, runtime)

    async def list_ans_service_clusters_async(
        self,
        request: mse_20190531_models.ListAnsServiceClustersRequest,
    ) -> mse_20190531_models.ListAnsServiceClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ans_service_clusters_with_options_async(request, runtime)

    def list_ans_services_with_options(
        self,
        request: mse_20190531_models.ListAnsServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAnsServicesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnsServices',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ans_services_with_options_async(
        self,
        request: mse_20190531_models.ListAnsServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAnsServicesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnsServices',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ans_services(
        self,
        request: mse_20190531_models.ListAnsServicesRequest,
    ) -> mse_20190531_models.ListAnsServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ans_services_with_options(request, runtime)

    async def list_ans_services_async(
        self,
        request: mse_20190531_models.ListAnsServicesRequest,
    ) -> mse_20190531_models.ListAnsServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ans_services_with_options_async(request, runtime)

    def list_cluster_connection_types_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListClusterConnectionTypesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListClusterConnectionTypes',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClusterConnectionTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_connection_types_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListClusterConnectionTypesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListClusterConnectionTypes',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClusterConnectionTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_connection_types(self) -> mse_20190531_models.ListClusterConnectionTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_connection_types_with_options(runtime)

    async def list_cluster_connection_types_async(self) -> mse_20190531_models.ListClusterConnectionTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_connection_types_with_options_async(runtime)

    def list_cluster_types_with_options(
        self,
        request: mse_20190531_models.ListClusterTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListClusterTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterTypes',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClusterTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_types_with_options_async(
        self,
        request: mse_20190531_models.ListClusterTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListClusterTypesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterTypes',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClusterTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_types(
        self,
        request: mse_20190531_models.ListClusterTypesRequest,
    ) -> mse_20190531_models.ListClusterTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_types_with_options(request, runtime)

    async def list_cluster_types_async(
        self,
        request: mse_20190531_models.ListClusterTypesRequest,
    ) -> mse_20190531_models.ListClusterTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_types_with_options_async(request, runtime)

    def list_cluster_versions_with_options(
        self,
        request: mse_20190531_models.ListClusterVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListClusterVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterType'] = request.cluster_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterVersions',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClusterVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_versions_with_options_async(
        self,
        request: mse_20190531_models.ListClusterVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListClusterVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterType'] = request.cluster_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterVersions',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClusterVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_versions(
        self,
        request: mse_20190531_models.ListClusterVersionsRequest,
    ) -> mse_20190531_models.ListClusterVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_versions_with_options(request, runtime)

    async def list_cluster_versions_async(
        self,
        request: mse_20190531_models.ListClusterVersionsRequest,
    ) -> mse_20190531_models.ListClusterVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_versions_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: mse_20190531_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListClustersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: mse_20190531_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListClustersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        request: mse_20190531_models.ListClustersRequest,
    ) -> mse_20190531_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: mse_20190531_models.ListClustersRequest,
    ) -> mse_20190531_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_engine_namespaces_with_options(
        self,
        request: mse_20190531_models.ListEngineNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListEngineNamespacesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEngineNamespaces',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEngineNamespacesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_engine_namespaces_with_options_async(
        self,
        request: mse_20190531_models.ListEngineNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListEngineNamespacesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEngineNamespaces',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEngineNamespacesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_engine_namespaces(
        self,
        request: mse_20190531_models.ListEngineNamespacesRequest,
    ) -> mse_20190531_models.ListEngineNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_engine_namespaces_with_options(request, runtime)

    async def list_engine_namespaces_async(
        self,
        request: mse_20190531_models.ListEngineNamespacesRequest,
    ) -> mse_20190531_models.ListEngineNamespacesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_engine_namespaces_with_options_async(request, runtime)

    def list_eureka_instances_with_options(
        self,
        request: mse_20190531_models.ListEurekaInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListEurekaInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEurekaInstances',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEurekaInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_eureka_instances_with_options_async(
        self,
        request: mse_20190531_models.ListEurekaInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListEurekaInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEurekaInstances',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEurekaInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_eureka_instances(
        self,
        request: mse_20190531_models.ListEurekaInstancesRequest,
    ) -> mse_20190531_models.ListEurekaInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_eureka_instances_with_options(request, runtime)

    async def list_eureka_instances_async(
        self,
        request: mse_20190531_models.ListEurekaInstancesRequest,
    ) -> mse_20190531_models.ListEurekaInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_eureka_instances_with_options_async(request, runtime)

    def list_eureka_services_with_options(
        self,
        request: mse_20190531_models.ListEurekaServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListEurekaServicesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEurekaServices',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEurekaServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_eureka_services_with_options_async(
        self,
        request: mse_20190531_models.ListEurekaServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListEurekaServicesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEurekaServices',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEurekaServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_eureka_services(
        self,
        request: mse_20190531_models.ListEurekaServicesRequest,
    ) -> mse_20190531_models.ListEurekaServicesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_eureka_services_with_options(request, runtime)

    async def list_eureka_services_async(
        self,
        request: mse_20190531_models.ListEurekaServicesRequest,
    ) -> mse_20190531_models.ListEurekaServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_eureka_services_with_options_async(request, runtime)

    def list_gateway_with_options(
        self,
        tmp_req: mse_20190531_models.ListGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListGatewayResponse:
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.ListGatewayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_params):
            request.filter_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.filter_params), 'FilterParams', 'json')
        query = {}
        query['DescSort'] = request.desc_sort
        query['FilterParams'] = request.filter_params_shrink
        query['OrderItem'] = request.order_item
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListGateway',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_gateway_with_options_async(
        self,
        tmp_req: mse_20190531_models.ListGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListGatewayResponse:
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.ListGatewayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter_params):
            request.filter_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.filter_params), 'FilterParams', 'json')
        query = {}
        query['DescSort'] = request.desc_sort
        query['FilterParams'] = request.filter_params_shrink
        query['OrderItem'] = request.order_item
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListGateway',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListGatewayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_gateway(
        self,
        request: mse_20190531_models.ListGatewayRequest,
    ) -> mse_20190531_models.ListGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_gateway_with_options(request, runtime)

    async def list_gateway_async(
        self,
        request: mse_20190531_models.ListGatewayRequest,
    ) -> mse_20190531_models.ListGatewayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_gateway_with_options_async(request, runtime)

    def list_listeners_by_config_with_options(
        self,
        request: mse_20190531_models.ListListenersByConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListListenersByConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DataId'] = request.data_id
        query['Group'] = request.group
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListListenersByConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListListenersByConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_listeners_by_config_with_options_async(
        self,
        request: mse_20190531_models.ListListenersByConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListListenersByConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DataId'] = request.data_id
        query['Group'] = request.group
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListListenersByConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListListenersByConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_listeners_by_config(
        self,
        request: mse_20190531_models.ListListenersByConfigRequest,
    ) -> mse_20190531_models.ListListenersByConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_listeners_by_config_with_options(request, runtime)

    async def list_listeners_by_config_async(
        self,
        request: mse_20190531_models.ListListenersByConfigRequest,
    ) -> mse_20190531_models.ListListenersByConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_listeners_by_config_with_options_async(request, runtime)

    def list_listeners_by_ip_with_options(
        self,
        request: mse_20190531_models.ListListenersByIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListListenersByIpResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Ip'] = request.ip
        query['NamespaceId'] = request.namespace_id
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListListenersByIp',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListListenersByIpResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_listeners_by_ip_with_options_async(
        self,
        request: mse_20190531_models.ListListenersByIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListListenersByIpResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['Ip'] = request.ip
        query['NamespaceId'] = request.namespace_id
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListListenersByIp',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListListenersByIpResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_listeners_by_ip(
        self,
        request: mse_20190531_models.ListListenersByIpRequest,
    ) -> mse_20190531_models.ListListenersByIpResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_listeners_by_ip_with_options(request, runtime)

    async def list_listeners_by_ip_async(
        self,
        request: mse_20190531_models.ListListenersByIpRequest,
    ) -> mse_20190531_models.ListListenersByIpResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_listeners_by_ip_with_options_async(request, runtime)

    def list_nacos_configs_with_options(
        self,
        request: mse_20190531_models.ListNacosConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListNacosConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppName'] = request.app_name
        query['DataId'] = request.data_id
        query['Group'] = request.group
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['RequestPars'] = request.request_pars
        query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListNacosConfigs',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListNacosConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nacos_configs_with_options_async(
        self,
        request: mse_20190531_models.ListNacosConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListNacosConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppName'] = request.app_name
        query['DataId'] = request.data_id
        query['Group'] = request.group
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['RequestPars'] = request.request_pars
        query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListNacosConfigs',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListNacosConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nacos_configs(
        self,
        request: mse_20190531_models.ListNacosConfigsRequest,
    ) -> mse_20190531_models.ListNacosConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_nacos_configs_with_options(request, runtime)

    async def list_nacos_configs_async(
        self,
        request: mse_20190531_models.ListNacosConfigsRequest,
    ) -> mse_20190531_models.ListNacosConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nacos_configs_with_options_async(request, runtime)

    def list_nacos_history_configs_with_options(
        self,
        request: mse_20190531_models.ListNacosHistoryConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListNacosHistoryConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DataId'] = request.data_id
        query['Group'] = request.group
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListNacosHistoryConfigs',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListNacosHistoryConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nacos_history_configs_with_options_async(
        self,
        request: mse_20190531_models.ListNacosHistoryConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListNacosHistoryConfigsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['DataId'] = request.data_id
        query['Group'] = request.group
        query['InstanceId'] = request.instance_id
        query['NamespaceId'] = request.namespace_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListNacosHistoryConfigs',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListNacosHistoryConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nacos_history_configs(
        self,
        request: mse_20190531_models.ListNacosHistoryConfigsRequest,
    ) -> mse_20190531_models.ListNacosHistoryConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_nacos_history_configs_with_options(request, runtime)

    async def list_nacos_history_configs_async(
        self,
        request: mse_20190531_models.ListNacosHistoryConfigsRequest,
    ) -> mse_20190531_models.ListNacosHistoryConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nacos_history_configs_with_options_async(request, runtime)

    def list_znode_children_with_options(
        self,
        request: mse_20190531_models.ListZnodeChildrenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListZnodeChildrenResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListZnodeChildren',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListZnodeChildrenResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_znode_children_with_options_async(
        self,
        request: mse_20190531_models.ListZnodeChildrenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListZnodeChildrenResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListZnodeChildren',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ListZnodeChildrenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_znode_children(
        self,
        request: mse_20190531_models.ListZnodeChildrenRequest,
    ) -> mse_20190531_models.ListZnodeChildrenResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_znode_children_with_options(request, runtime)

    async def list_znode_children_async(
        self,
        request: mse_20190531_models.ListZnodeChildrenRequest,
    ) -> mse_20190531_models.ListZnodeChildrenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_znode_children_with_options_async(request, runtime)

    def modify_governance_kubernetes_cluster_with_options(
        self,
        request: mse_20190531_models.ModifyGovernanceKubernetesClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ModifyGovernanceKubernetesClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['NamespaceInfos'] = request.namespace_infos
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyGovernanceKubernetesCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ModifyGovernanceKubernetesClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_governance_kubernetes_cluster_with_options_async(
        self,
        request: mse_20190531_models.ModifyGovernanceKubernetesClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ModifyGovernanceKubernetesClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['NamespaceInfos'] = request.namespace_infos
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyGovernanceKubernetesCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ModifyGovernanceKubernetesClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_governance_kubernetes_cluster(
        self,
        request: mse_20190531_models.ModifyGovernanceKubernetesClusterRequest,
    ) -> mse_20190531_models.ModifyGovernanceKubernetesClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_governance_kubernetes_cluster_with_options(request, runtime)

    async def modify_governance_kubernetes_cluster_async(
        self,
        request: mse_20190531_models.ModifyGovernanceKubernetesClusterRequest,
    ) -> mse_20190531_models.ModifyGovernanceKubernetesClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_governance_kubernetes_cluster_with_options_async(request, runtime)

    def query_business_locations_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryBusinessLocationsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryBusinessLocations',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryBusinessLocationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_business_locations_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryBusinessLocationsResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryBusinessLocations',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryBusinessLocationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_business_locations(self) -> mse_20190531_models.QueryBusinessLocationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_business_locations_with_options(runtime)

    async def query_business_locations_async(self) -> mse_20190531_models.QueryBusinessLocationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_business_locations_with_options_async(runtime)

    def query_cluster_detail_with_options(
        self,
        request: mse_20190531_models.QueryClusterDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryClusterDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryClusterDetail',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cluster_detail_with_options_async(
        self,
        request: mse_20190531_models.QueryClusterDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryClusterDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryClusterDetail',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cluster_detail(
        self,
        request: mse_20190531_models.QueryClusterDetailRequest,
    ) -> mse_20190531_models.QueryClusterDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_cluster_detail_with_options(request, runtime)

    async def query_cluster_detail_async(
        self,
        request: mse_20190531_models.QueryClusterDetailRequest,
    ) -> mse_20190531_models.QueryClusterDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_cluster_detail_with_options_async(request, runtime)

    def query_cluster_disk_specification_with_options(
        self,
        request: mse_20190531_models.QueryClusterDiskSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryClusterDiskSpecificationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterType'] = request.cluster_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryClusterDiskSpecification',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterDiskSpecificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cluster_disk_specification_with_options_async(
        self,
        request: mse_20190531_models.QueryClusterDiskSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryClusterDiskSpecificationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterType'] = request.cluster_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryClusterDiskSpecification',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterDiskSpecificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cluster_disk_specification(
        self,
        request: mse_20190531_models.QueryClusterDiskSpecificationRequest,
    ) -> mse_20190531_models.QueryClusterDiskSpecificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_cluster_disk_specification_with_options(request, runtime)

    async def query_cluster_disk_specification_async(
        self,
        request: mse_20190531_models.QueryClusterDiskSpecificationRequest,
    ) -> mse_20190531_models.QueryClusterDiskSpecificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_cluster_disk_specification_with_options_async(request, runtime)

    def query_cluster_specification_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryClusterSpecificationResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryClusterSpecification',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterSpecificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_cluster_specification_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryClusterSpecificationResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryClusterSpecification',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterSpecificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_cluster_specification(self) -> mse_20190531_models.QueryClusterSpecificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_cluster_specification_with_options(runtime)

    async def query_cluster_specification_async(self) -> mse_20190531_models.QueryClusterSpecificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_cluster_specification_with_options_async(runtime)

    def query_config_with_options(
        self,
        request: mse_20190531_models.QueryConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_config_with_options_async(
        self,
        request: mse_20190531_models.QueryConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_config(
        self,
        request: mse_20190531_models.QueryConfigRequest,
    ) -> mse_20190531_models.QueryConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_config_with_options(request, runtime)

    async def query_config_async(
        self,
        request: mse_20190531_models.QueryConfigRequest,
    ) -> mse_20190531_models.QueryConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_config_with_options_async(request, runtime)

    def query_gateway_region_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryGatewayRegionResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryGatewayRegion',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryGatewayRegionResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_gateway_region_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryGatewayRegionResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryGatewayRegion',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryGatewayRegionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_gateway_region(self) -> mse_20190531_models.QueryGatewayRegionResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_gateway_region_with_options(runtime)

    async def query_gateway_region_async(self) -> mse_20190531_models.QueryGatewayRegionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_gateway_region_with_options_async(runtime)

    def query_gateway_type_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryGatewayTypeResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryGatewayType',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryGatewayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_gateway_type_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryGatewayTypeResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryGatewayType',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryGatewayTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_gateway_type(self) -> mse_20190531_models.QueryGatewayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_gateway_type_with_options(runtime)

    async def query_gateway_type_async(self) -> mse_20190531_models.QueryGatewayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_gateway_type_with_options_async(runtime)

    def query_monitor_with_options(
        self,
        request: mse_20190531_models.QueryMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryMonitorResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMonitor',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_monitor_with_options_async(
        self,
        request: mse_20190531_models.QueryMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryMonitorResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMonitor',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_monitor(
        self,
        request: mse_20190531_models.QueryMonitorRequest,
    ) -> mse_20190531_models.QueryMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_monitor_with_options(request, runtime)

    async def query_monitor_async(
        self,
        request: mse_20190531_models.QueryMonitorRequest,
    ) -> mse_20190531_models.QueryMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_monitor_with_options_async(request, runtime)

    def query_slb_spec_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QuerySlbSpecResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QuerySlbSpec',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QuerySlbSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_slb_spec_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QuerySlbSpecResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QuerySlbSpec',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QuerySlbSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_slb_spec(self) -> mse_20190531_models.QuerySlbSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_slb_spec_with_options(runtime)

    async def query_slb_spec_async(self) -> mse_20190531_models.QuerySlbSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_slb_spec_with_options_async(runtime)

    def query_znode_detail_with_options(
        self,
        request: mse_20190531_models.QueryZnodeDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryZnodeDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryZnodeDetail',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryZnodeDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_znode_detail_with_options_async(
        self,
        request: mse_20190531_models.QueryZnodeDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryZnodeDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryZnodeDetail',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryZnodeDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_znode_detail(
        self,
        request: mse_20190531_models.QueryZnodeDetailRequest,
    ) -> mse_20190531_models.QueryZnodeDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_znode_detail_with_options(request, runtime)

    async def query_znode_detail_async(
        self,
        request: mse_20190531_models.QueryZnodeDetailRequest,
    ) -> mse_20190531_models.QueryZnodeDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_znode_detail_with_options_async(request, runtime)

    def restart_cluster_with_options(
        self,
        request: mse_20190531_models.RestartClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.RestartClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['InstanceId'] = request.instance_id
        query['PodNameList'] = request.pod_name_list
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestartCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.RestartClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_cluster_with_options_async(
        self,
        request: mse_20190531_models.RestartClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.RestartClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['InstanceId'] = request.instance_id
        query['PodNameList'] = request.pod_name_list
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RestartCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.RestartClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_cluster(
        self,
        request: mse_20190531_models.RestartClusterRequest,
    ) -> mse_20190531_models.RestartClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_cluster_with_options(request, runtime)

    async def restart_cluster_async(
        self,
        request: mse_20190531_models.RestartClusterRequest,
    ) -> mse_20190531_models.RestartClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_cluster_with_options_async(request, runtime)

    def retry_cluster_with_options(
        self,
        request: mse_20190531_models.RetryClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.RetryClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RetryCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.RetryClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_cluster_with_options_async(
        self,
        request: mse_20190531_models.RetryClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.RetryClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RetryCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.RetryClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_cluster(
        self,
        request: mse_20190531_models.RetryClusterRequest,
    ) -> mse_20190531_models.RetryClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_cluster_with_options(request, runtime)

    async def retry_cluster_async(
        self,
        request: mse_20190531_models.RetryClusterRequest,
    ) -> mse_20190531_models.RetryClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_cluster_with_options_async(request, runtime)

    def scaling_cluster_with_options(
        self,
        request: mse_20190531_models.ScalingClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ScalingClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterSpecification'] = request.cluster_specification
        query['Cpu'] = request.cpu
        query['InstanceCount'] = request.instance_count
        query['InstanceId'] = request.instance_id
        query['MemoryCapacity'] = request.memory_capacity
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ScalingCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ScalingClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def scaling_cluster_with_options_async(
        self,
        request: mse_20190531_models.ScalingClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ScalingClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterSpecification'] = request.cluster_specification
        query['Cpu'] = request.cpu
        query['InstanceCount'] = request.instance_count
        query['InstanceId'] = request.instance_id
        query['MemoryCapacity'] = request.memory_capacity
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ScalingCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.ScalingClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scaling_cluster(
        self,
        request: mse_20190531_models.ScalingClusterRequest,
    ) -> mse_20190531_models.ScalingClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.scaling_cluster_with_options(request, runtime)

    async def scaling_cluster_async(
        self,
        request: mse_20190531_models.ScalingClusterRequest,
    ) -> mse_20190531_models.ScalingClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.scaling_cluster_with_options_async(request, runtime)

    def update_acl_with_options(
        self,
        request: mse_20190531_models.UpdateAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateAclResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AclEntryList'] = request.acl_entry_list
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAcl',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateAclResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_acl_with_options_async(
        self,
        request: mse_20190531_models.UpdateAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateAclResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AclEntryList'] = request.acl_entry_list
        query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAcl',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateAclResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_acl(
        self,
        request: mse_20190531_models.UpdateAclRequest,
    ) -> mse_20190531_models.UpdateAclResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_acl_with_options(request, runtime)

    async def update_acl_async(
        self,
        request: mse_20190531_models.UpdateAclRequest,
    ) -> mse_20190531_models.UpdateAclResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_acl_with_options_async(request, runtime)

    def update_cluster_with_options(
        self,
        request: mse_20190531_models.UpdateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterAliasName'] = request.cluster_alias_name
        query['InstanceId'] = request.instance_id
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_with_options_async(
        self,
        request: mse_20190531_models.UpdateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterAliasName'] = request.cluster_alias_name
        query['InstanceId'] = request.instance_id
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster(
        self,
        request: mse_20190531_models.UpdateClusterRequest,
    ) -> mse_20190531_models.UpdateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_with_options(request, runtime)

    async def update_cluster_async(
        self,
        request: mse_20190531_models.UpdateClusterRequest,
    ) -> mse_20190531_models.UpdateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cluster_with_options_async(request, runtime)

    def update_config_with_options(
        self,
        request: mse_20190531_models.UpdateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AutopurgePurgeInterval'] = request.autopurge_purge_interval
        query['AutopurgeSnapRetainCount'] = request.autopurge_snap_retain_count
        query['ClusterId'] = request.cluster_id
        query['ConfigAuthEnabled'] = request.config_auth_enabled
        query['ConfigSecretEnabled'] = request.config_secret_enabled
        query['ConfigType'] = request.config_type
        query['InitLimit'] = request.init_limit
        query['InstanceId'] = request.instance_id
        query['JuteMaxbuffer'] = request.jute_maxbuffer
        query['MCPEnabled'] = request.mcpenabled
        query['MaxClientCnxns'] = request.max_client_cnxns
        query['PassWord'] = request.pass_word
        query['RequestPars'] = request.request_pars
        query['SyncLimit'] = request.sync_limit
        query['TickTime'] = request.tick_time
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_with_options_async(
        self,
        request: mse_20190531_models.UpdateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AutopurgePurgeInterval'] = request.autopurge_purge_interval
        query['AutopurgeSnapRetainCount'] = request.autopurge_snap_retain_count
        query['ClusterId'] = request.cluster_id
        query['ConfigAuthEnabled'] = request.config_auth_enabled
        query['ConfigSecretEnabled'] = request.config_secret_enabled
        query['ConfigType'] = request.config_type
        query['InitLimit'] = request.init_limit
        query['InstanceId'] = request.instance_id
        query['JuteMaxbuffer'] = request.jute_maxbuffer
        query['MCPEnabled'] = request.mcpenabled
        query['MaxClientCnxns'] = request.max_client_cnxns
        query['PassWord'] = request.pass_word
        query['RequestPars'] = request.request_pars
        query['SyncLimit'] = request.sync_limit
        query['TickTime'] = request.tick_time
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config(
        self,
        request: mse_20190531_models.UpdateConfigRequest,
    ) -> mse_20190531_models.UpdateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_config_with_options(request, runtime)

    async def update_config_async(
        self,
        request: mse_20190531_models.UpdateConfigRequest,
    ) -> mse_20190531_models.UpdateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_config_with_options_async(request, runtime)

    def update_engine_namespace_with_options(
        self,
        request: mse_20190531_models.UpdateEngineNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateEngineNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Desc'] = request.desc
        query['Id'] = request.id
        query['InstanceId'] = request.instance_id
        query['Name'] = request.name
        query['ServiceCount'] = request.service_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateEngineNamespace',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateEngineNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_engine_namespace_with_options_async(
        self,
        request: mse_20190531_models.UpdateEngineNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateEngineNamespaceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Desc'] = request.desc
        query['Id'] = request.id
        query['InstanceId'] = request.instance_id
        query['Name'] = request.name
        query['ServiceCount'] = request.service_count
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateEngineNamespace',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateEngineNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_engine_namespace(
        self,
        request: mse_20190531_models.UpdateEngineNamespaceRequest,
    ) -> mse_20190531_models.UpdateEngineNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_engine_namespace_with_options(request, runtime)

    async def update_engine_namespace_async(
        self,
        request: mse_20190531_models.UpdateEngineNamespaceRequest,
    ) -> mse_20190531_models.UpdateEngineNamespaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_engine_namespace_with_options_async(request, runtime)

    def update_gateway_name_with_options(
        self,
        request: mse_20190531_models.UpdateGatewayNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateGatewayNameResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayName',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_name_with_options_async(
        self,
        request: mse_20190531_models.UpdateGatewayNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateGatewayNameResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGatewayName',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_name(
        self,
        request: mse_20190531_models.UpdateGatewayNameRequest,
    ) -> mse_20190531_models.UpdateGatewayNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_name_with_options(request, runtime)

    async def update_gateway_name_async(
        self,
        request: mse_20190531_models.UpdateGatewayNameRequest,
    ) -> mse_20190531_models.UpdateGatewayNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_gateway_name_with_options_async(request, runtime)

    def update_gateway_option_with_options(
        self,
        tmp_req: mse_20190531_models.UpdateGatewayOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateGatewayOptionResponse:
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.UpdateGatewayOptionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.gateway_option):
            request.gateway_option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.gateway_option), 'GatewayOption', 'json')
        query = {}
        query['GatewayId'] = request.gateway_id
        query['GatewayOption'] = request.gateway_option_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGatewayOption',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_option_with_options_async(
        self,
        tmp_req: mse_20190531_models.UpdateGatewayOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateGatewayOptionResponse:
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.UpdateGatewayOptionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.gateway_option):
            request.gateway_option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.gateway_option), 'GatewayOption', 'json')
        query = {}
        query['GatewayId'] = request.gateway_id
        query['GatewayOption'] = request.gateway_option_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGatewayOption',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_option(
        self,
        request: mse_20190531_models.UpdateGatewayOptionRequest,
    ) -> mse_20190531_models.UpdateGatewayOptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_option_with_options(request, runtime)

    async def update_gateway_option_async(
        self,
        request: mse_20190531_models.UpdateGatewayOptionRequest,
    ) -> mse_20190531_models.UpdateGatewayOptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_gateway_option_with_options_async(request, runtime)

    def update_gateway_route_httprewrite_with_options(
        self,
        request: mse_20190531_models.UpdateGatewayRouteHTTPRewriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateGatewayRouteHTTPRewriteResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GatewayId'] = request.gateway_id
        query['HttpRewriteJSON'] = request.http_rewrite_json
        query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGatewayRouteHTTPRewrite',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayRouteHTTPRewriteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_gateway_route_httprewrite_with_options_async(
        self,
        request: mse_20190531_models.UpdateGatewayRouteHTTPRewriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateGatewayRouteHTTPRewriteResponse:
        UtilClient.validate_model(request)
        query = {}
        query['GatewayId'] = request.gateway_id
        query['HttpRewriteJSON'] = request.http_rewrite_json
        query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateGatewayRouteHTTPRewrite',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayRouteHTTPRewriteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_gateway_route_httprewrite(
        self,
        request: mse_20190531_models.UpdateGatewayRouteHTTPRewriteRequest,
    ) -> mse_20190531_models.UpdateGatewayRouteHTTPRewriteResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_gateway_route_httprewrite_with_options(request, runtime)

    async def update_gateway_route_httprewrite_async(
        self,
        request: mse_20190531_models.UpdateGatewayRouteHTTPRewriteRequest,
    ) -> mse_20190531_models.UpdateGatewayRouteHTTPRewriteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_gateway_route_httprewrite_with_options_async(request, runtime)

    def update_image_with_options(
        self,
        request: mse_20190531_models.UpdateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateImageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['VersionCode'] = request.version_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateImage',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_image_with_options_async(
        self,
        request: mse_20190531_models.UpdateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateImageResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['VersionCode'] = request.version_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateImage',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_image(
        self,
        request: mse_20190531_models.UpdateImageRequest,
    ) -> mse_20190531_models.UpdateImageResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_image_with_options(request, runtime)

    async def update_image_async(
        self,
        request: mse_20190531_models.UpdateImageRequest,
    ) -> mse_20190531_models.UpdateImageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_image_with_options_async(request, runtime)

    def update_nacos_config_with_options(
        self,
        request: mse_20190531_models.UpdateNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateNacosConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppName'] = request.app_name
        query['BetaIps'] = request.beta_ips
        query['Content'] = request.content
        query['DataId'] = request.data_id
        query['Desc'] = request.desc
        query['EncryptedDataKey'] = request.encrypted_data_key
        query['Group'] = request.group
        query['InstanceId'] = request.instance_id
        query['Md5'] = request.md_5
        query['NamespaceId'] = request.namespace_id
        query['Tags'] = request.tags
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateNacosConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_nacos_config_with_options_async(
        self,
        request: mse_20190531_models.UpdateNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateNacosConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppName'] = request.app_name
        query['BetaIps'] = request.beta_ips
        query['Content'] = request.content
        query['DataId'] = request.data_id
        query['Desc'] = request.desc
        query['EncryptedDataKey'] = request.encrypted_data_key
        query['Group'] = request.group
        query['InstanceId'] = request.instance_id
        query['Md5'] = request.md_5
        query['NamespaceId'] = request.namespace_id
        query['Tags'] = request.tags
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateNacosConfig',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateNacosConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_nacos_config(
        self,
        request: mse_20190531_models.UpdateNacosConfigRequest,
    ) -> mse_20190531_models.UpdateNacosConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_nacos_config_with_options(request, runtime)

    async def update_nacos_config_async(
        self,
        request: mse_20190531_models.UpdateNacosConfigRequest,
    ) -> mse_20190531_models.UpdateNacosConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_nacos_config_with_options_async(request, runtime)

    def update_nacos_instance_with_options(
        self,
        request: mse_20190531_models.UpdateNacosInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateNacosInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterName'] = request.cluster_name
        query['Enabled'] = request.enabled
        query['Ephemeral'] = request.ephemeral
        query['GroupName'] = request.group_name
        query['InstanceId'] = request.instance_id
        query['Ip'] = request.ip
        query['NamespaceId'] = request.namespace_id
        query['Port'] = request.port
        query['ServiceName'] = request.service_name
        query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateNacosInstance',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateNacosInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_nacos_instance_with_options_async(
        self,
        request: mse_20190531_models.UpdateNacosInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateNacosInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterName'] = request.cluster_name
        query['Enabled'] = request.enabled
        query['Ephemeral'] = request.ephemeral
        query['GroupName'] = request.group_name
        query['InstanceId'] = request.instance_id
        query['Ip'] = request.ip
        query['NamespaceId'] = request.namespace_id
        query['Port'] = request.port
        query['ServiceName'] = request.service_name
        query['Weight'] = request.weight
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateNacosInstance',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateNacosInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_nacos_instance(
        self,
        request: mse_20190531_models.UpdateNacosInstanceRequest,
    ) -> mse_20190531_models.UpdateNacosInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_nacos_instance_with_options(request, runtime)

    async def update_nacos_instance_async(
        self,
        request: mse_20190531_models.UpdateNacosInstanceRequest,
    ) -> mse_20190531_models.UpdateNacosInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_nacos_instance_with_options_async(request, runtime)

    def update_znode_with_options(
        self,
        request: mse_20190531_models.UpdateZnodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateZnodeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Data'] = request.data
        query['Path'] = request.path
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateZnode',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateZnodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_znode_with_options_async(
        self,
        request: mse_20190531_models.UpdateZnodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateZnodeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Data'] = request.data
        query['Path'] = request.path
        query['RequestPars'] = request.request_pars
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateZnode',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateZnodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_znode(
        self,
        request: mse_20190531_models.UpdateZnodeRequest,
    ) -> mse_20190531_models.UpdateZnodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_znode_with_options(request, runtime)

    async def update_znode_async(
        self,
        request: mse_20190531_models.UpdateZnodeRequest,
    ) -> mse_20190531_models.UpdateZnodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_znode_with_options_async(request, runtime)

    def upgrade_cluster_with_options(
        self,
        request: mse_20190531_models.UpgradeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpgradeClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['RequestPars'] = request.request_pars
        query['UpgradeVersion'] = request.upgrade_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpgradeCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpgradeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_cluster_with_options_async(
        self,
        request: mse_20190531_models.UpgradeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpgradeClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['InstanceId'] = request.instance_id
        query['RequestPars'] = request.request_pars
        query['UpgradeVersion'] = request.upgrade_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpgradeCluster',
            version='2019-05-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            mse_20190531_models.UpgradeClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_cluster(
        self,
        request: mse_20190531_models.UpgradeClusterRequest,
    ) -> mse_20190531_models.UpgradeClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_cluster_with_options(request, runtime)

    async def upgrade_cluster_async(
        self,
        request: mse_20190531_models.UpgradeClusterRequest,
    ) -> mse_20190531_models.UpgradeClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_cluster_with_options_async(request, runtime)
