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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.AddMockRuleResponse(),
            self.do_rpcrequest('AddMockRule', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_mock_rule_with_options_async(
        self,
        request: mse_20190531_models.AddMockRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.AddMockRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.AddMockRuleResponse(),
            await self.do_rpcrequest_async('AddMockRule', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.AddServiceSourceResponse(),
            self.do_rpcrequest('AddServiceSource', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_service_source_with_options_async(
        self,
        request: mse_20190531_models.AddServiceSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.AddServiceSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.AddServiceSourceResponse(),
            await self.do_rpcrequest_async('AddServiceSource', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CloneNacosConfigResponse(),
            self.do_rpcrequest('CloneNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clone_nacos_config_with_options_async(
        self,
        request: mse_20190531_models.CloneNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CloneNacosConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CloneNacosConfigResponse(),
            await self.do_rpcrequest_async('CloneNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateAlarmRuleResponse(),
            self.do_rpcrequest('CreateAlarmRule', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateAlarmRuleResponse(),
            await self.do_rpcrequest_async('CreateAlarmRule', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateApplicationResponse(),
            self.do_rpcrequest('CreateApplication', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_application_with_options_async(
        self,
        request: mse_20190531_models.CreateApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateApplicationResponse(),
            await self.do_rpcrequest_async('CreateApplication', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateClusterResponse(),
            self.do_rpcrequest('CreateCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: mse_20190531_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateClusterResponse(),
            await self.do_rpcrequest_async('CreateCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateEngineNamespaceResponse(),
            self.do_rpcrequest('CreateEngineNamespace', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_engine_namespace_with_options_async(
        self,
        request: mse_20190531_models.CreateEngineNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateEngineNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateEngineNamespaceResponse(),
            await self.do_rpcrequest_async('CreateEngineNamespace', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateGovernanceKubernetesClusterResponse(),
            self.do_rpcrequest('CreateGovernanceKubernetesCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_governance_kubernetes_cluster_with_options_async(
        self,
        request: mse_20190531_models.CreateGovernanceKubernetesClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateGovernanceKubernetesClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateGovernanceKubernetesClusterResponse(),
            await self.do_rpcrequest_async('CreateGovernanceKubernetesCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateNacosConfigResponse(),
            self.do_rpcrequest('CreateNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_nacos_config_with_options_async(
        self,
        request: mse_20190531_models.CreateNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateNacosConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateNacosConfigResponse(),
            await self.do_rpcrequest_async('CreateNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateZnodeResponse(),
            self.do_rpcrequest('CreateZnode', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_znode_with_options_async(
        self,
        request: mse_20190531_models.CreateZnodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.CreateZnodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateZnodeResponse(),
            await self.do_rpcrequest_async('CreateZnode', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteAlarmRuleResponse(),
            self.do_rpcrequest('DeleteAlarmRule', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_alarm_rule_with_options_async(
        self,
        request: mse_20190531_models.DeleteAlarmRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteAlarmRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteAlarmRuleResponse(),
            await self.do_rpcrequest_async('DeleteAlarmRule', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteClusterResponse(),
            self.do_rpcrequest('DeleteCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_cluster_with_options_async(
        self,
        request: mse_20190531_models.DeleteClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteClusterResponse(),
            await self.do_rpcrequest_async('DeleteCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteEngineNamespaceResponse(),
            self.do_rpcrequest('DeleteEngineNamespace', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_engine_namespace_with_options_async(
        self,
        request: mse_20190531_models.DeleteEngineNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteEngineNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteEngineNamespaceResponse(),
            await self.do_rpcrequest_async('DeleteEngineNamespace', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosConfigResponse(),
            self.do_rpcrequest('DeleteNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_nacos_config_with_options_async(
        self,
        request: mse_20190531_models.DeleteNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteNacosConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosConfigResponse(),
            await self.do_rpcrequest_async('DeleteNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosConfigsResponse(),
            self.do_rpcrequest('DeleteNacosConfigs', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_nacos_configs_with_options_async(
        self,
        request: mse_20190531_models.DeleteNacosConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteNacosConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosConfigsResponse(),
            await self.do_rpcrequest_async('DeleteNacosConfigs', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosServiceResponse(),
            self.do_rpcrequest('DeleteNacosService', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_nacos_service_with_options_async(
        self,
        request: mse_20190531_models.DeleteNacosServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteNacosServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosServiceResponse(),
            await self.do_rpcrequest_async('DeleteNacosService', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteZnodeResponse(),
            self.do_rpcrequest('DeleteZnode', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_znode_with_options_async(
        self,
        request: mse_20190531_models.DeleteZnodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.DeleteZnodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteZnodeResponse(),
            await self.do_rpcrequest_async('DeleteZnode', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ExportNacosConfigResponse(),
            self.do_rpcrequest('ExportNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_nacos_config_with_options_async(
        self,
        request: mse_20190531_models.ExportNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ExportNacosConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ExportNacosConfigResponse(),
            await self.do_rpcrequest_async('ExportNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetEngineNamepaceResponse(),
            self.do_rpcrequest('GetEngineNamepace', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_engine_namepace_with_options_async(
        self,
        request: mse_20190531_models.GetEngineNamepaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetEngineNamepaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetEngineNamepaceResponse(),
            await self.do_rpcrequest_async('GetEngineNamepace', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGatewayResponse(),
            self.do_rpcrequest('GetGateway', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_gateway_with_options_async(
        self,
        request: mse_20190531_models.GetGatewayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetGatewayResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGatewayResponse(),
            await self.do_rpcrequest_async('GetGateway', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGatewayOptionResponse(),
            self.do_rpcrequest('GetGatewayOption', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_gateway_option_with_options_async(
        self,
        request: mse_20190531_models.GetGatewayOptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetGatewayOptionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGatewayOptionResponse(),
            await self.do_rpcrequest_async('GetGatewayOption', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGovernanceKubernetesClusterResponse(),
            self.do_rpcrequest('GetGovernanceKubernetesCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_governance_kubernetes_cluster_with_options_async(
        self,
        request: mse_20190531_models.GetGovernanceKubernetesClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetGovernanceKubernetesClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGovernanceKubernetesClusterResponse(),
            await self.do_rpcrequest_async('GetGovernanceKubernetesCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGovernanceKubernetesClusterListResponse(),
            self.do_rpcrequest('GetGovernanceKubernetesClusterList', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_governance_kubernetes_cluster_list_with_options_async(
        self,
        request: mse_20190531_models.GetGovernanceKubernetesClusterListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetGovernanceKubernetesClusterListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetGovernanceKubernetesClusterListResponse(),
            await self.do_rpcrequest_async('GetGovernanceKubernetesClusterList', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetImageResponse(),
            self.do_rpcrequest('GetImage', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_image_with_options_async(
        self,
        request: mse_20190531_models.GetImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetImageResponse(),
            await self.do_rpcrequest_async('GetImage', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetImportFileUrlResponse(),
            self.do_rpcrequest('GetImportFileUrl', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_import_file_url_with_options_async(
        self,
        request: mse_20190531_models.GetImportFileUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetImportFileUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetImportFileUrlResponse(),
            await self.do_rpcrequest_async('GetImportFileUrl', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return TeaCore.from_map(
            mse_20190531_models.GetMseFeatureSwitchResponse(),
            self.do_rpcrequest('GetMseFeatureSwitch', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_mse_feature_switch_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetMseFeatureSwitchResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mse_20190531_models.GetMseFeatureSwitchResponse(),
            await self.do_rpcrequest_async('GetMseFeatureSwitch', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetNacosConfigResponse(),
            self.do_rpcrequest('GetNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_nacos_config_with_options_async(
        self,
        request: mse_20190531_models.GetNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetNacosConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetNacosConfigResponse(),
            await self.do_rpcrequest_async('GetNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetNacosHistoryConfigResponse(),
            self.do_rpcrequest('GetNacosHistoryConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_nacos_history_config_with_options_async(
        self,
        request: mse_20190531_models.GetNacosHistoryConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetNacosHistoryConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetNacosHistoryConfigResponse(),
            await self.do_rpcrequest_async('GetNacosHistoryConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetOverviewResponse(),
            self.do_rpcrequest('GetOverview', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_overview_with_options_async(
        self,
        request: mse_20190531_models.GetOverviewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.GetOverviewResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetOverviewResponse(),
            await self.do_rpcrequest_async('GetOverview', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ImportNacosConfigResponse(),
            self.do_rpcrequest('ImportNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_nacos_config_with_options_async(
        self,
        request: mse_20190531_models.ImportNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ImportNacosConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ImportNacosConfigResponse(),
            await self.do_rpcrequest_async('ImportNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmContactGroupsResponse(),
            self.do_rpcrequest('ListAlarmContactGroups', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_alarm_contact_groups_with_options_async(
        self,
        request: mse_20190531_models.ListAlarmContactGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAlarmContactGroupsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmContactGroupsResponse(),
            await self.do_rpcrequest_async('ListAlarmContactGroups', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmHistoriesResponse(),
            self.do_rpcrequest('ListAlarmHistories', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_alarm_histories_with_options_async(
        self,
        request: mse_20190531_models.ListAlarmHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAlarmHistoriesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmHistoriesResponse(),
            await self.do_rpcrequest_async('ListAlarmHistories', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmItemsResponse(),
            self.do_rpcrequest('ListAlarmItems', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_alarm_items_with_options_async(
        self,
        request: mse_20190531_models.ListAlarmItemsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAlarmItemsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmItemsResponse(),
            await self.do_rpcrequest_async('ListAlarmItems', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmRulesResponse(),
            self.do_rpcrequest('ListAlarmRules', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_alarm_rules_with_options_async(
        self,
        request: mse_20190531_models.ListAlarmRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAlarmRulesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmRulesResponse(),
            await self.do_rpcrequest_async('ListAlarmRules', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsInstancesResponse(),
            self.do_rpcrequest('ListAnsInstances', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_ans_instances_with_options_async(
        self,
        request: mse_20190531_models.ListAnsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAnsInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsInstancesResponse(),
            await self.do_rpcrequest_async('ListAnsInstances', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsServiceClustersResponse(),
            self.do_rpcrequest('ListAnsServiceClusters', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_ans_service_clusters_with_options_async(
        self,
        request: mse_20190531_models.ListAnsServiceClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAnsServiceClustersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsServiceClustersResponse(),
            await self.do_rpcrequest_async('ListAnsServiceClusters', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsServicesResponse(),
            self.do_rpcrequest('ListAnsServices', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_ans_services_with_options_async(
        self,
        request: mse_20190531_models.ListAnsServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListAnsServicesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsServicesResponse(),
            await self.do_rpcrequest_async('ListAnsServices', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        return TeaCore.from_map(
            mse_20190531_models.ListClusterConnectionTypesResponse(),
            self.do_rpcrequest('ListClusterConnectionTypes', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_connection_types_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListClusterConnectionTypesResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mse_20190531_models.ListClusterConnectionTypesResponse(),
            await self.do_rpcrequest_async('ListClusterConnectionTypes', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClusterTypesResponse(),
            self.do_rpcrequest('ListClusterTypes', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_types_with_options_async(
        self,
        request: mse_20190531_models.ListClusterTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListClusterTypesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClusterTypesResponse(),
            await self.do_rpcrequest_async('ListClusterTypes', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClusterVersionsResponse(),
            self.do_rpcrequest('ListClusterVersions', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_versions_with_options_async(
        self,
        request: mse_20190531_models.ListClusterVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListClusterVersionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClusterVersionsResponse(),
            await self.do_rpcrequest_async('ListClusterVersions', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClustersResponse(),
            self.do_rpcrequest('ListClusters', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: mse_20190531_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListClustersResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClustersResponse(),
            await self.do_rpcrequest_async('ListClusters', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEngineNamespacesResponse(),
            self.do_rpcrequest('ListEngineNamespaces', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_engine_namespaces_with_options_async(
        self,
        request: mse_20190531_models.ListEngineNamespacesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListEngineNamespacesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEngineNamespacesResponse(),
            await self.do_rpcrequest_async('ListEngineNamespaces', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEurekaInstancesResponse(),
            self.do_rpcrequest('ListEurekaInstances', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_eureka_instances_with_options_async(
        self,
        request: mse_20190531_models.ListEurekaInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListEurekaInstancesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEurekaInstancesResponse(),
            await self.do_rpcrequest_async('ListEurekaInstances', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEurekaServicesResponse(),
            self.do_rpcrequest('ListEurekaServices', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_eureka_services_with_options_async(
        self,
        request: mse_20190531_models.ListEurekaServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListEurekaServicesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEurekaServicesResponse(),
            await self.do_rpcrequest_async('ListEurekaServices', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListGatewayResponse(),
            self.do_rpcrequest('ListGateway', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListGatewayResponse(),
            await self.do_rpcrequest_async('ListGateway', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListListenersByConfigResponse(),
            self.do_rpcrequest('ListListenersByConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_listeners_by_config_with_options_async(
        self,
        request: mse_20190531_models.ListListenersByConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListListenersByConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListListenersByConfigResponse(),
            await self.do_rpcrequest_async('ListListenersByConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListListenersByIpResponse(),
            self.do_rpcrequest('ListListenersByIp', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_listeners_by_ip_with_options_async(
        self,
        request: mse_20190531_models.ListListenersByIpRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListListenersByIpResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListListenersByIpResponse(),
            await self.do_rpcrequest_async('ListListenersByIp', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListNacosConfigsResponse(),
            self.do_rpcrequest('ListNacosConfigs', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_nacos_configs_with_options_async(
        self,
        request: mse_20190531_models.ListNacosConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListNacosConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListNacosConfigsResponse(),
            await self.do_rpcrequest_async('ListNacosConfigs', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListNacosHistoryConfigsResponse(),
            self.do_rpcrequest('ListNacosHistoryConfigs', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_nacos_history_configs_with_options_async(
        self,
        request: mse_20190531_models.ListNacosHistoryConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListNacosHistoryConfigsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListNacosHistoryConfigsResponse(),
            await self.do_rpcrequest_async('ListNacosHistoryConfigs', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListZnodeChildrenResponse(),
            self.do_rpcrequest('ListZnodeChildren', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_znode_children_with_options_async(
        self,
        request: mse_20190531_models.ListZnodeChildrenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ListZnodeChildrenResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListZnodeChildrenResponse(),
            await self.do_rpcrequest_async('ListZnodeChildren', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ModifyGovernanceKubernetesClusterResponse(),
            self.do_rpcrequest('ModifyGovernanceKubernetesCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_governance_kubernetes_cluster_with_options_async(
        self,
        request: mse_20190531_models.ModifyGovernanceKubernetesClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ModifyGovernanceKubernetesClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ModifyGovernanceKubernetesClusterResponse(),
            await self.do_rpcrequest_async('ModifyGovernanceKubernetesCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return TeaCore.from_map(
            mse_20190531_models.QueryBusinessLocationsResponse(),
            self.do_rpcrequest('QueryBusinessLocations', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_business_locations_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryBusinessLocationsResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mse_20190531_models.QueryBusinessLocationsResponse(),
            await self.do_rpcrequest_async('QueryBusinessLocations', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterDetailResponse(),
            self.do_rpcrequest('QueryClusterDetail', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_cluster_detail_with_options_async(
        self,
        request: mse_20190531_models.QueryClusterDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryClusterDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterDetailResponse(),
            await self.do_rpcrequest_async('QueryClusterDetail', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterDiskSpecificationResponse(),
            self.do_rpcrequest('QueryClusterDiskSpecification', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_cluster_disk_specification_with_options_async(
        self,
        request: mse_20190531_models.QueryClusterDiskSpecificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryClusterDiskSpecificationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterDiskSpecificationResponse(),
            await self.do_rpcrequest_async('QueryClusterDiskSpecification', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterSpecificationResponse(),
            self.do_rpcrequest('QueryClusterSpecification', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_cluster_specification_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryClusterSpecificationResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterSpecificationResponse(),
            await self.do_rpcrequest_async('QueryClusterSpecification', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryConfigResponse(),
            self.do_rpcrequest('QueryConfig', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_config_with_options_async(
        self,
        request: mse_20190531_models.QueryConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryConfigResponse(),
            await self.do_rpcrequest_async('QueryConfig', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        return TeaCore.from_map(
            mse_20190531_models.QueryGatewayRegionResponse(),
            self.do_rpcrequest('QueryGatewayRegion', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_gateway_region_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryGatewayRegionResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mse_20190531_models.QueryGatewayRegionResponse(),
            await self.do_rpcrequest_async('QueryGatewayRegion', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        return TeaCore.from_map(
            mse_20190531_models.QueryGatewayTypeResponse(),
            self.do_rpcrequest('QueryGatewayType', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_gateway_type_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryGatewayTypeResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mse_20190531_models.QueryGatewayTypeResponse(),
            await self.do_rpcrequest_async('QueryGatewayType', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryMonitorResponse(),
            self.do_rpcrequest('QueryMonitor', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_monitor_with_options_async(
        self,
        request: mse_20190531_models.QueryMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryMonitorResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryMonitorResponse(),
            await self.do_rpcrequest_async('QueryMonitor', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        return TeaCore.from_map(
            mse_20190531_models.QuerySlbSpecResponse(),
            self.do_rpcrequest('QuerySlbSpec', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_slb_spec_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QuerySlbSpecResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mse_20190531_models.QuerySlbSpecResponse(),
            await self.do_rpcrequest_async('QuerySlbSpec', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryZnodeDetailResponse(),
            self.do_rpcrequest('QueryZnodeDetail', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def query_znode_detail_with_options_async(
        self,
        request: mse_20190531_models.QueryZnodeDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.QueryZnodeDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryZnodeDetailResponse(),
            await self.do_rpcrequest_async('QueryZnodeDetail', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.RestartClusterResponse(),
            self.do_rpcrequest('RestartCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restart_cluster_with_options_async(
        self,
        request: mse_20190531_models.RestartClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.RestartClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.RestartClusterResponse(),
            await self.do_rpcrequest_async('RestartCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.RetryClusterResponse(),
            self.do_rpcrequest('RetryCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def retry_cluster_with_options_async(
        self,
        request: mse_20190531_models.RetryClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.RetryClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.RetryClusterResponse(),
            await self.do_rpcrequest_async('RetryCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ScalingClusterResponse(),
            self.do_rpcrequest('ScalingCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def scaling_cluster_with_options_async(
        self,
        request: mse_20190531_models.ScalingClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.ScalingClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ScalingClusterResponse(),
            await self.do_rpcrequest_async('ScalingCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateAclResponse(),
            self.do_rpcrequest('UpdateAcl', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_acl_with_options_async(
        self,
        request: mse_20190531_models.UpdateAclRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateAclResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateAclResponse(),
            await self.do_rpcrequest_async('UpdateAcl', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateClusterResponse(),
            self.do_rpcrequest('UpdateCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_cluster_with_options_async(
        self,
        request: mse_20190531_models.UpdateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateClusterResponse(),
            await self.do_rpcrequest_async('UpdateCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateConfigResponse(),
            self.do_rpcrequest('UpdateConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_config_with_options_async(
        self,
        request: mse_20190531_models.UpdateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateConfigResponse(),
            await self.do_rpcrequest_async('UpdateConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateEngineNamespaceResponse(),
            self.do_rpcrequest('UpdateEngineNamespace', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_engine_namespace_with_options_async(
        self,
        request: mse_20190531_models.UpdateEngineNamespaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateEngineNamespaceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateEngineNamespaceResponse(),
            await self.do_rpcrequest_async('UpdateEngineNamespace', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayNameResponse(),
            self.do_rpcrequest('UpdateGatewayName', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def update_gateway_name_with_options_async(
        self,
        request: mse_20190531_models.UpdateGatewayNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateGatewayNameResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayNameResponse(),
            await self.do_rpcrequest_async('UpdateGatewayName', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayOptionResponse(),
            self.do_rpcrequest('UpdateGatewayOption', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayOptionResponse(),
            await self.do_rpcrequest_async('UpdateGatewayOption', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayRouteHTTPRewriteResponse(),
            self.do_rpcrequest('UpdateGatewayRouteHTTPRewrite', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_gateway_route_httprewrite_with_options_async(
        self,
        request: mse_20190531_models.UpdateGatewayRouteHTTPRewriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateGatewayRouteHTTPRewriteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateGatewayRouteHTTPRewriteResponse(),
            await self.do_rpcrequest_async('UpdateGatewayRouteHTTPRewrite', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateImageResponse(),
            self.do_rpcrequest('UpdateImage', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_image_with_options_async(
        self,
        request: mse_20190531_models.UpdateImageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateImageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateImageResponse(),
            await self.do_rpcrequest_async('UpdateImage', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateNacosConfigResponse(),
            self.do_rpcrequest('UpdateNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_nacos_config_with_options_async(
        self,
        request: mse_20190531_models.UpdateNacosConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateNacosConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateNacosConfigResponse(),
            await self.do_rpcrequest_async('UpdateNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateNacosInstanceResponse(),
            self.do_rpcrequest('UpdateNacosInstance', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_nacos_instance_with_options_async(
        self,
        request: mse_20190531_models.UpdateNacosInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateNacosInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateNacosInstanceResponse(),
            await self.do_rpcrequest_async('UpdateNacosInstance', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateZnodeResponse(),
            self.do_rpcrequest('UpdateZnode', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_znode_with_options_async(
        self,
        request: mse_20190531_models.UpdateZnodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpdateZnodeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateZnodeResponse(),
            await self.do_rpcrequest_async('UpdateZnode', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpgradeClusterResponse(),
            self.do_rpcrequest('UpgradeCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def upgrade_cluster_with_options_async(
        self,
        request: mse_20190531_models.UpgradeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> mse_20190531_models.UpgradeClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpgradeClusterResponse(),
            await self.do_rpcrequest_async('UpgradeCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
