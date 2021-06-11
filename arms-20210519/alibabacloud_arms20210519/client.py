# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_arms20210519 import models as arms20210519_models
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
            'ap-northeast-1': 'arms.ap-southeast-1.aliyuncs.com',
            'ap-south-1': 'arms.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'arms.ap-southeast-1.aliyuncs.com',
            'ap-southeast-3': 'arms.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'arms.ap-southeast-1.aliyuncs.com',
            'cn-chengdu': 'arms.aliyuncs.com',
            'cn-huhehaote': 'arms.aliyuncs.com',
            'eu-central-1': 'arms.ap-southeast-1.aliyuncs.com',
            'eu-west-1': 'arms.ap-southeast-1.aliyuncs.com',
            'me-east-1': 'arms.ap-southeast-1.aliyuncs.com',
            'us-east-1': 'arms.ap-southeast-1.aliyuncs.com',
            'cn-hangzhou-finance': 'arms.aliyuncs.com',
            'cn-shenzhen-finance-1': 'arms.aliyuncs.com',
            'cn-shanghai-finance-1': 'arms.aliyuncs.com',
            'cn-north-2-gov-1': 'arms.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('arms', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def apply_scenario_with_options(
        self,
        tmp_req: arms20210519_models.ApplyScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ApplyScenarioResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20210519_models.ApplyScenarioShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ApplyScenarioResponse(),
            self.do_rpcrequest('ApplyScenario', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def apply_scenario_with_options_async(
        self,
        tmp_req: arms20210519_models.ApplyScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ApplyScenarioResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20210519_models.ApplyScenarioShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ApplyScenarioResponse(),
            await self.do_rpcrequest_async('ApplyScenario', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_scenario(
        self,
        request: arms20210519_models.ApplyScenarioRequest,
    ) -> arms20210519_models.ApplyScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_scenario_with_options(request, runtime)

    async def apply_scenario_async(
        self,
        request: arms20210519_models.ApplyScenarioRequest,
    ) -> arms20210519_models.ApplyScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_scenario_with_options_async(request, runtime)

    def update_alert_contact_group_with_options(
        self,
        request: arms20210519_models.UpdateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.UpdateAlertContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.UpdateAlertContactGroupResponse(),
            self.do_rpcrequest('UpdateAlertContactGroup', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_alert_contact_group_with_options_async(
        self,
        request: arms20210519_models.UpdateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.UpdateAlertContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.UpdateAlertContactGroupResponse(),
            await self.do_rpcrequest_async('UpdateAlertContactGroup', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_alert_contact_group(
        self,
        request: arms20210519_models.UpdateAlertContactGroupRequest,
    ) -> arms20210519_models.UpdateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_alert_contact_group_with_options(request, runtime)

    async def update_alert_contact_group_async(
        self,
        request: arms20210519_models.UpdateAlertContactGroupRequest,
    ) -> arms20210519_models.UpdateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_alert_contact_group_with_options_async(request, runtime)

    def get_prometheus_api_token_with_options(
        self,
        request: arms20210519_models.GetPrometheusApiTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetPrometheusApiTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetPrometheusApiTokenResponse(),
            self.do_rpcrequest('GetPrometheusApiToken', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_prometheus_api_token_with_options_async(
        self,
        request: arms20210519_models.GetPrometheusApiTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetPrometheusApiTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetPrometheusApiTokenResponse(),
            await self.do_rpcrequest_async('GetPrometheusApiToken', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_prometheus_api_token(
        self,
        request: arms20210519_models.GetPrometheusApiTokenRequest,
    ) -> arms20210519_models.GetPrometheusApiTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_prometheus_api_token_with_options(request, runtime)

    async def get_prometheus_api_token_async(
        self,
        request: arms20210519_models.GetPrometheusApiTokenRequest,
    ) -> arms20210519_models.GetPrometheusApiTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_prometheus_api_token_with_options_async(request, runtime)

    def open_arms_service_with_options(
        self,
        request: arms20210519_models.OpenArmsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.OpenArmsServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.OpenArmsServiceResponse(),
            self.do_rpcrequest('OpenArmsService', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_arms_service_with_options_async(
        self,
        request: arms20210519_models.OpenArmsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.OpenArmsServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.OpenArmsServiceResponse(),
            await self.do_rpcrequest_async('OpenArmsService', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_arms_service(
        self,
        request: arms20210519_models.OpenArmsServiceRequest,
    ) -> arms20210519_models.OpenArmsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_arms_service_with_options(request, runtime)

    async def open_arms_service_async(
        self,
        request: arms20210519_models.OpenArmsServiceRequest,
    ) -> arms20210519_models.OpenArmsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_arms_service_with_options_async(request, runtime)

    def create_alert_contact_group_with_options(
        self,
        request: arms20210519_models.CreateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CreateAlertContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CreateAlertContactGroupResponse(),
            self.do_rpcrequest('CreateAlertContactGroup', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_alert_contact_group_with_options_async(
        self,
        request: arms20210519_models.CreateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CreateAlertContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CreateAlertContactGroupResponse(),
            await self.do_rpcrequest_async('CreateAlertContactGroup', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_alert_contact_group(
        self,
        request: arms20210519_models.CreateAlertContactGroupRequest,
    ) -> arms20210519_models.CreateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_alert_contact_group_with_options(request, runtime)

    async def create_alert_contact_group_async(
        self,
        request: arms20210519_models.CreateAlertContactGroupRequest,
    ) -> arms20210519_models.CreateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_alert_contact_group_with_options_async(request, runtime)

    def export_prometheus_rules_with_options(
        self,
        request: arms20210519_models.ExportPrometheusRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ExportPrometheusRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ExportPrometheusRulesResponse(),
            self.do_rpcrequest('ExportPrometheusRules', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def export_prometheus_rules_with_options_async(
        self,
        request: arms20210519_models.ExportPrometheusRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ExportPrometheusRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ExportPrometheusRulesResponse(),
            await self.do_rpcrequest_async('ExportPrometheusRules', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_prometheus_rules(
        self,
        request: arms20210519_models.ExportPrometheusRulesRequest,
    ) -> arms20210519_models.ExportPrometheusRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_prometheus_rules_with_options(request, runtime)

    async def export_prometheus_rules_async(
        self,
        request: arms20210519_models.ExportPrometheusRulesRequest,
    ) -> arms20210519_models.ExportPrometheusRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_prometheus_rules_with_options_async(request, runtime)

    def get_trace_app_with_options(
        self,
        request: arms20210519_models.GetTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetTraceAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetTraceAppResponse(),
            self.do_rpcrequest('GetTraceApp', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_trace_app_with_options_async(
        self,
        request: arms20210519_models.GetTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetTraceAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetTraceAppResponse(),
            await self.do_rpcrequest_async('GetTraceApp', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_trace_app(
        self,
        request: arms20210519_models.GetTraceAppRequest,
    ) -> arms20210519_models.GetTraceAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_trace_app_with_options(request, runtime)

    async def get_trace_app_async(
        self,
        request: arms20210519_models.GetTraceAppRequest,
    ) -> arms20210519_models.GetTraceAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_trace_app_with_options_async(request, runtime)

    def update_prometheus_alert_rule_with_options(
        self,
        request: arms20210519_models.UpdatePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.UpdatePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.UpdatePrometheusAlertRuleResponse(),
            self.do_rpcrequest('UpdatePrometheusAlertRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_prometheus_alert_rule_with_options_async(
        self,
        request: arms20210519_models.UpdatePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.UpdatePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.UpdatePrometheusAlertRuleResponse(),
            await self.do_rpcrequest_async('UpdatePrometheusAlertRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_prometheus_alert_rule(
        self,
        request: arms20210519_models.UpdatePrometheusAlertRuleRequest,
    ) -> arms20210519_models.UpdatePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_prometheus_alert_rule_with_options(request, runtime)

    async def update_prometheus_alert_rule_async(
        self,
        request: arms20210519_models.UpdatePrometheusAlertRuleRequest,
    ) -> arms20210519_models.UpdatePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_prometheus_alert_rule_with_options_async(request, runtime)

    def enable_alert_template_with_options(
        self,
        request: arms20210519_models.EnableAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.EnableAlertTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.EnableAlertTemplateResponse(),
            self.do_rpcrequest('EnableAlertTemplate', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_alert_template_with_options_async(
        self,
        request: arms20210519_models.EnableAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.EnableAlertTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.EnableAlertTemplateResponse(),
            await self.do_rpcrequest_async('EnableAlertTemplate', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_alert_template(
        self,
        request: arms20210519_models.EnableAlertTemplateRequest,
    ) -> arms20210519_models.EnableAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_alert_template_with_options(request, runtime)

    async def enable_alert_template_async(
        self,
        request: arms20210519_models.EnableAlertTemplateRequest,
    ) -> arms20210519_models.EnableAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_alert_template_with_options_async(request, runtime)

    def list_cluster_from_grafana_with_options(
        self,
        request: arms20210519_models.ListClusterFromGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListClusterFromGrafanaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListClusterFromGrafanaResponse(),
            self.do_rpcrequest('ListClusterFromGrafana', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_from_grafana_with_options_async(
        self,
        request: arms20210519_models.ListClusterFromGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListClusterFromGrafanaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListClusterFromGrafanaResponse(),
            await self.do_rpcrequest_async('ListClusterFromGrafana', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_from_grafana(
        self,
        request: arms20210519_models.ListClusterFromGrafanaRequest,
    ) -> arms20210519_models.ListClusterFromGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_from_grafana_with_options(request, runtime)

    async def list_cluster_from_grafana_async(
        self,
        request: arms20210519_models.ListClusterFromGrafanaRequest,
    ) -> arms20210519_models.ListClusterFromGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_from_grafana_with_options_async(request, runtime)

    def install_eventer_with_options(
        self,
        request: arms20210519_models.InstallEventerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.InstallEventerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.InstallEventerResponse(),
            self.do_rpcrequest('InstallEventer', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def install_eventer_with_options_async(
        self,
        request: arms20210519_models.InstallEventerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.InstallEventerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.InstallEventerResponse(),
            await self.do_rpcrequest_async('InstallEventer', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def install_eventer(
        self,
        request: arms20210519_models.InstallEventerRequest,
    ) -> arms20210519_models.InstallEventerResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_eventer_with_options(request, runtime)

    async def install_eventer_async(
        self,
        request: arms20210519_models.InstallEventerRequest,
    ) -> arms20210519_models.InstallEventerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_eventer_with_options_async(request, runtime)

    def list_dashboards_with_options(
        self,
        request: arms20210519_models.ListDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListDashboardsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListDashboardsResponse(),
            self.do_rpcrequest('ListDashboards', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_dashboards_with_options_async(
        self,
        request: arms20210519_models.ListDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListDashboardsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListDashboardsResponse(),
            await self.do_rpcrequest_async('ListDashboards', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_dashboards(
        self,
        request: arms20210519_models.ListDashboardsRequest,
    ) -> arms20210519_models.ListDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dashboards_with_options(request, runtime)

    async def list_dashboards_async(
        self,
        request: arms20210519_models.ListDashboardsRequest,
    ) -> arms20210519_models.ListDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dashboards_with_options_async(request, runtime)

    def list_prometheus_alert_rules_with_options(
        self,
        request: arms20210519_models.ListPrometheusAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListPrometheusAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListPrometheusAlertRulesResponse(),
            self.do_rpcrequest('ListPrometheusAlertRules', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_prometheus_alert_rules_with_options_async(
        self,
        request: arms20210519_models.ListPrometheusAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListPrometheusAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListPrometheusAlertRulesResponse(),
            await self.do_rpcrequest_async('ListPrometheusAlertRules', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_prometheus_alert_rules(
        self,
        request: arms20210519_models.ListPrometheusAlertRulesRequest,
    ) -> arms20210519_models.ListPrometheusAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_alert_rules_with_options(request, runtime)

    async def list_prometheus_alert_rules_async(
        self,
        request: arms20210519_models.ListPrometheusAlertRulesRequest,
    ) -> arms20210519_models.ListPrometheusAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_prometheus_alert_rules_with_options_async(request, runtime)

    def delete_trace_app_with_options(
        self,
        request: arms20210519_models.DeleteTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteTraceAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteTraceAppResponse(),
            self.do_rpcrequest('DeleteTraceApp', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_trace_app_with_options_async(
        self,
        request: arms20210519_models.DeleteTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteTraceAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteTraceAppResponse(),
            await self.do_rpcrequest_async('DeleteTraceApp', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_trace_app(
        self,
        request: arms20210519_models.DeleteTraceAppRequest,
    ) -> arms20210519_models.DeleteTraceAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_trace_app_with_options(request, runtime)

    async def delete_trace_app_async(
        self,
        request: arms20210519_models.DeleteTraceAppRequest,
    ) -> arms20210519_models.DeleteTraceAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_trace_app_with_options_async(request, runtime)

    def create_retcode_app_with_options(
        self,
        request: arms20210519_models.CreateRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CreateRetcodeAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CreateRetcodeAppResponse(),
            self.do_rpcrequest('CreateRetcodeApp', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_retcode_app_with_options_async(
        self,
        request: arms20210519_models.CreateRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CreateRetcodeAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CreateRetcodeAppResponse(),
            await self.do_rpcrequest_async('CreateRetcodeApp', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_retcode_app(
        self,
        request: arms20210519_models.CreateRetcodeAppRequest,
    ) -> arms20210519_models.CreateRetcodeAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_retcode_app_with_options(request, runtime)

    async def create_retcode_app_async(
        self,
        request: arms20210519_models.CreateRetcodeAppRequest,
    ) -> arms20210519_models.CreateRetcodeAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_retcode_app_with_options_async(request, runtime)

    def config_app_with_options(
        self,
        request: arms20210519_models.ConfigAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ConfigAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ConfigAppResponse(),
            self.do_rpcrequest('ConfigApp', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def config_app_with_options_async(
        self,
        request: arms20210519_models.ConfigAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ConfigAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ConfigAppResponse(),
            await self.do_rpcrequest_async('ConfigApp', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def config_app(
        self,
        request: arms20210519_models.ConfigAppRequest,
    ) -> arms20210519_models.ConfigAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_app_with_options(request, runtime)

    async def config_app_async(
        self,
        request: arms20210519_models.ConfigAppRequest,
    ) -> arms20210519_models.ConfigAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_app_with_options_async(request, runtime)

    def search_alert_histories_with_options(
        self,
        request: arms20210519_models.SearchAlertHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchAlertHistoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchAlertHistoriesResponse(),
            self.do_rpcrequest('SearchAlertHistories', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_alert_histories_with_options_async(
        self,
        request: arms20210519_models.SearchAlertHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchAlertHistoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchAlertHistoriesResponse(),
            await self.do_rpcrequest_async('SearchAlertHistories', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_alert_histories(
        self,
        request: arms20210519_models.SearchAlertHistoriesRequest,
    ) -> arms20210519_models.SearchAlertHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_alert_histories_with_options(request, runtime)

    async def search_alert_histories_async(
        self,
        request: arms20210519_models.SearchAlertHistoriesRequest,
    ) -> arms20210519_models.SearchAlertHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_histories_with_options_async(request, runtime)

    def search_trace_app_by_page_with_options(
        self,
        request: arms20210519_models.SearchTraceAppByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchTraceAppByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchTraceAppByPageResponse(),
            self.do_rpcrequest('SearchTraceAppByPage', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_trace_app_by_page_with_options_async(
        self,
        request: arms20210519_models.SearchTraceAppByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchTraceAppByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchTraceAppByPageResponse(),
            await self.do_rpcrequest_async('SearchTraceAppByPage', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_trace_app_by_page(
        self,
        request: arms20210519_models.SearchTraceAppByPageRequest,
    ) -> arms20210519_models.SearchTraceAppByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_trace_app_by_page_with_options(request, runtime)

    async def search_trace_app_by_page_async(
        self,
        request: arms20210519_models.SearchTraceAppByPageRequest,
    ) -> arms20210519_models.SearchTraceAppByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_trace_app_by_page_with_options_async(request, runtime)

    def delete_alert_contact_group_with_options(
        self,
        request: arms20210519_models.DeleteAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteAlertContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteAlertContactGroupResponse(),
            self.do_rpcrequest('DeleteAlertContactGroup', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_alert_contact_group_with_options_async(
        self,
        request: arms20210519_models.DeleteAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteAlertContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteAlertContactGroupResponse(),
            await self.do_rpcrequest_async('DeleteAlertContactGroup', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_alert_contact_group(
        self,
        request: arms20210519_models.DeleteAlertContactGroupRequest,
    ) -> arms20210519_models.DeleteAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_group_with_options(request, runtime)

    async def delete_alert_contact_group_async(
        self,
        request: arms20210519_models.DeleteAlertContactGroupRequest,
    ) -> arms20210519_models.DeleteAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_contact_group_with_options_async(request, runtime)

    def import_app_alert_rules_with_options(
        self,
        request: arms20210519_models.ImportAppAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ImportAppAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ImportAppAlertRulesResponse(),
            self.do_rpcrequest('ImportAppAlertRules', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_app_alert_rules_with_options_async(
        self,
        request: arms20210519_models.ImportAppAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ImportAppAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ImportAppAlertRulesResponse(),
            await self.do_rpcrequest_async('ImportAppAlertRules', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_app_alert_rules(
        self,
        request: arms20210519_models.ImportAppAlertRulesRequest,
    ) -> arms20210519_models.ImportAppAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_app_alert_rules_with_options(request, runtime)

    async def import_app_alert_rules_async(
        self,
        request: arms20210519_models.ImportAppAlertRulesRequest,
    ) -> arms20210519_models.ImportAppAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_app_alert_rules_with_options_async(request, runtime)

    def update_webhook_with_options(
        self,
        request: arms20210519_models.UpdateWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.UpdateWebhookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.UpdateWebhookResponse(),
            self.do_rpcrequest('UpdateWebhook', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_webhook_with_options_async(
        self,
        request: arms20210519_models.UpdateWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.UpdateWebhookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.UpdateWebhookResponse(),
            await self.do_rpcrequest_async('UpdateWebhook', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_webhook(
        self,
        request: arms20210519_models.UpdateWebhookRequest,
    ) -> arms20210519_models.UpdateWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_webhook_with_options(request, runtime)

    async def update_webhook_async(
        self,
        request: arms20210519_models.UpdateWebhookRequest,
    ) -> arms20210519_models.UpdateWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_webhook_with_options_async(request, runtime)

    def search_events_with_options(
        self,
        request: arms20210519_models.SearchEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchEventsResponse(),
            self.do_rpcrequest('SearchEvents', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_events_with_options_async(
        self,
        request: arms20210519_models.SearchEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchEventsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchEventsResponse(),
            await self.do_rpcrequest_async('SearchEvents', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_events(
        self,
        request: arms20210519_models.SearchEventsRequest,
    ) -> arms20210519_models.SearchEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_events_with_options(request, runtime)

    async def search_events_async(
        self,
        request: arms20210519_models.SearchEventsRequest,
    ) -> arms20210519_models.SearchEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_events_with_options_async(request, runtime)

    def send_custom_incidents_with_options(
        self,
        request: arms20210519_models.SendCustomIncidentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SendCustomIncidentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SendCustomIncidentsResponse(),
            self.do_rpcrequest('SendCustomIncidents', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_custom_incidents_with_options_async(
        self,
        request: arms20210519_models.SendCustomIncidentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SendCustomIncidentsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SendCustomIncidentsResponse(),
            await self.do_rpcrequest_async('SendCustomIncidents', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_custom_incidents(
        self,
        request: arms20210519_models.SendCustomIncidentsRequest,
    ) -> arms20210519_models.SendCustomIncidentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_custom_incidents_with_options(request, runtime)

    async def send_custom_incidents_async(
        self,
        request: arms20210519_models.SendCustomIncidentsRequest,
    ) -> arms20210519_models.SendCustomIncidentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_custom_incidents_with_options_async(request, runtime)

    def search_trace_app_by_name_with_options(
        self,
        request: arms20210519_models.SearchTraceAppByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchTraceAppByNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchTraceAppByNameResponse(),
            self.do_rpcrequest('SearchTraceAppByName', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_trace_app_by_name_with_options_async(
        self,
        request: arms20210519_models.SearchTraceAppByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchTraceAppByNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchTraceAppByNameResponse(),
            await self.do_rpcrequest_async('SearchTraceAppByName', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_trace_app_by_name(
        self,
        request: arms20210519_models.SearchTraceAppByNameRequest,
    ) -> arms20210519_models.SearchTraceAppByNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_trace_app_by_name_with_options(request, runtime)

    async def search_trace_app_by_name_async(
        self,
        request: arms20210519_models.SearchTraceAppByNameRequest,
    ) -> arms20210519_models.SearchTraceAppByNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_trace_app_by_name_with_options_async(request, runtime)

    def create_prometheus_alert_rule_with_options(
        self,
        request: arms20210519_models.CreatePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CreatePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CreatePrometheusAlertRuleResponse(),
            self.do_rpcrequest('CreatePrometheusAlertRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_prometheus_alert_rule_with_options_async(
        self,
        request: arms20210519_models.CreatePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CreatePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CreatePrometheusAlertRuleResponse(),
            await self.do_rpcrequest_async('CreatePrometheusAlertRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_prometheus_alert_rule(
        self,
        request: arms20210519_models.CreatePrometheusAlertRuleRequest,
    ) -> arms20210519_models.CreatePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_prometheus_alert_rule_with_options(request, runtime)

    async def create_prometheus_alert_rule_async(
        self,
        request: arms20210519_models.CreatePrometheusAlertRuleRequest,
    ) -> arms20210519_models.CreatePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_prometheus_alert_rule_with_options_async(request, runtime)

    def search_traces_with_options(
        self,
        request: arms20210519_models.SearchTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchTracesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchTracesResponse(),
            self.do_rpcrequest('SearchTraces', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_traces_with_options_async(
        self,
        request: arms20210519_models.SearchTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchTracesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchTracesResponse(),
            await self.do_rpcrequest_async('SearchTraces', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_traces(
        self,
        request: arms20210519_models.SearchTracesRequest,
    ) -> arms20210519_models.SearchTracesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_traces_with_options(request, runtime)

    async def search_traces_async(
        self,
        request: arms20210519_models.SearchTracesRequest,
    ) -> arms20210519_models.SearchTracesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_traces_with_options_async(request, runtime)

    def open_vcluster_with_options(
        self,
        request: arms20210519_models.OpenVClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.OpenVClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.OpenVClusterResponse(),
            self.do_rpcrequest('OpenVCluster', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_vcluster_with_options_async(
        self,
        request: arms20210519_models.OpenVClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.OpenVClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.OpenVClusterResponse(),
            await self.do_rpcrequest_async('OpenVCluster', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_vcluster(
        self,
        request: arms20210519_models.OpenVClusterRequest,
    ) -> arms20210519_models.OpenVClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_vcluster_with_options(request, runtime)

    async def open_vcluster_async(
        self,
        request: arms20210519_models.OpenVClusterRequest,
    ) -> arms20210519_models.OpenVClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_vcluster_with_options_async(request, runtime)

    def create_alert_template_with_options(
        self,
        request: arms20210519_models.CreateAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CreateAlertTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CreateAlertTemplateResponse(),
            self.do_rpcrequest('CreateAlertTemplate', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_alert_template_with_options_async(
        self,
        request: arms20210519_models.CreateAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CreateAlertTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CreateAlertTemplateResponse(),
            await self.do_rpcrequest_async('CreateAlertTemplate', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_alert_template(
        self,
        request: arms20210519_models.CreateAlertTemplateRequest,
    ) -> arms20210519_models.CreateAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_alert_template_with_options(request, runtime)

    async def create_alert_template_async(
        self,
        request: arms20210519_models.CreateAlertTemplateRequest,
    ) -> arms20210519_models.CreateAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_alert_template_with_options_async(request, runtime)

    def search_alert_contact_with_options(
        self,
        request: arms20210519_models.SearchAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchAlertContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchAlertContactResponse(),
            self.do_rpcrequest('SearchAlertContact', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_alert_contact_with_options_async(
        self,
        request: arms20210519_models.SearchAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchAlertContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchAlertContactResponse(),
            await self.do_rpcrequest_async('SearchAlertContact', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_alert_contact(
        self,
        request: arms20210519_models.SearchAlertContactRequest,
    ) -> arms20210519_models.SearchAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_alert_contact_with_options(request, runtime)

    async def search_alert_contact_async(
        self,
        request: arms20210519_models.SearchAlertContactRequest,
    ) -> arms20210519_models.SearchAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_contact_with_options_async(request, runtime)

    def delete_grafana_resource_with_options(
        self,
        request: arms20210519_models.DeleteGrafanaResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteGrafanaResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteGrafanaResourceResponse(),
            self.do_rpcrequest('DeleteGrafanaResource', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_grafana_resource_with_options_async(
        self,
        request: arms20210519_models.DeleteGrafanaResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteGrafanaResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteGrafanaResourceResponse(),
            await self.do_rpcrequest_async('DeleteGrafanaResource', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_grafana_resource(
        self,
        request: arms20210519_models.DeleteGrafanaResourceRequest,
    ) -> arms20210519_models.DeleteGrafanaResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_grafana_resource_with_options(request, runtime)

    async def delete_grafana_resource_async(
        self,
        request: arms20210519_models.DeleteGrafanaResourceRequest,
    ) -> arms20210519_models.DeleteGrafanaResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_grafana_resource_with_options_async(request, runtime)

    def check_service_status_with_options(
        self,
        request: arms20210519_models.CheckServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CheckServiceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CheckServiceStatusResponse(),
            self.do_rpcrequest('CheckServiceStatus', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_service_status_with_options_async(
        self,
        request: arms20210519_models.CheckServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CheckServiceStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CheckServiceStatusResponse(),
            await self.do_rpcrequest_async('CheckServiceStatus', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_service_status(
        self,
        request: arms20210519_models.CheckServiceStatusRequest,
    ) -> arms20210519_models.CheckServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_service_status_with_options(request, runtime)

    async def check_service_status_async(
        self,
        request: arms20210519_models.CheckServiceStatusRequest,
    ) -> arms20210519_models.CheckServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_service_status_with_options_async(request, runtime)

    def list_scenario_with_options(
        self,
        request: arms20210519_models.ListScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListScenarioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListScenarioResponse(),
            self.do_rpcrequest('ListScenario', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_scenario_with_options_async(
        self,
        request: arms20210519_models.ListScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListScenarioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListScenarioResponse(),
            await self.do_rpcrequest_async('ListScenario', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scenario(
        self,
        request: arms20210519_models.ListScenarioRequest,
    ) -> arms20210519_models.ListScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_scenario_with_options(request, runtime)

    async def list_scenario_async(
        self,
        request: arms20210519_models.ListScenarioRequest,
    ) -> arms20210519_models.ListScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_scenario_with_options_async(request, runtime)

    def list_serverless_top_napps_with_options(
        self,
        request: arms20210519_models.ListServerlessTopNAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListServerlessTopNAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListServerlessTopNAppsResponse(),
            self.do_rpcrequest('ListServerlessTopNApps', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_serverless_top_napps_with_options_async(
        self,
        request: arms20210519_models.ListServerlessTopNAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListServerlessTopNAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListServerlessTopNAppsResponse(),
            await self.do_rpcrequest_async('ListServerlessTopNApps', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_serverless_top_napps(
        self,
        request: arms20210519_models.ListServerlessTopNAppsRequest,
    ) -> arms20210519_models.ListServerlessTopNAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_serverless_top_napps_with_options(request, runtime)

    async def list_serverless_top_napps_async(
        self,
        request: arms20210519_models.ListServerlessTopNAppsRequest,
    ) -> arms20210519_models.ListServerlessTopNAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_serverless_top_napps_with_options_async(request, runtime)

    def get_agent_download_url_with_options(
        self,
        request: arms20210519_models.GetAgentDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetAgentDownloadUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            arms20210519_models.GetAgentDownloadUrlResponse(),
            self.do_rpcrequest('GetAgentDownloadUrl', '2021-05-19', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_agent_download_url_with_options_async(
        self,
        request: arms20210519_models.GetAgentDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetAgentDownloadUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            arms20210519_models.GetAgentDownloadUrlResponse(),
            await self.do_rpcrequest_async('GetAgentDownloadUrl', '2021-05-19', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_agent_download_url(
        self,
        request: arms20210519_models.GetAgentDownloadUrlRequest,
    ) -> arms20210519_models.GetAgentDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_agent_download_url_with_options(request, runtime)

    async def get_agent_download_url_async(
        self,
        request: arms20210519_models.GetAgentDownloadUrlRequest,
    ) -> arms20210519_models.GetAgentDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_download_url_with_options_async(request, runtime)

    def open_arms_default_slrwith_options(
        self,
        request: arms20210519_models.OpenArmsDefaultSLRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.OpenArmsDefaultSLRResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.OpenArmsDefaultSLRResponse(),
            self.do_rpcrequest('OpenArmsDefaultSLR', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_arms_default_slrwith_options_async(
        self,
        request: arms20210519_models.OpenArmsDefaultSLRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.OpenArmsDefaultSLRResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.OpenArmsDefaultSLRResponse(),
            await self.do_rpcrequest_async('OpenArmsDefaultSLR', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_arms_default_slr(
        self,
        request: arms20210519_models.OpenArmsDefaultSLRRequest,
    ) -> arms20210519_models.OpenArmsDefaultSLRResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_arms_default_slrwith_options(request, runtime)

    async def open_arms_default_slr_async(
        self,
        request: arms20210519_models.OpenArmsDefaultSLRRequest,
    ) -> arms20210519_models.OpenArmsDefaultSLRResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_arms_default_slrwith_options_async(request, runtime)

    def check_data_consistency_with_options(
        self,
        request: arms20210519_models.CheckDataConsistencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CheckDataConsistencyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CheckDataConsistencyResponse(),
            self.do_rpcrequest('CheckDataConsistency', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_data_consistency_with_options_async(
        self,
        request: arms20210519_models.CheckDataConsistencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CheckDataConsistencyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CheckDataConsistencyResponse(),
            await self.do_rpcrequest_async('CheckDataConsistency', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_data_consistency(
        self,
        request: arms20210519_models.CheckDataConsistencyRequest,
    ) -> arms20210519_models.CheckDataConsistencyResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_data_consistency_with_options(request, runtime)

    async def check_data_consistency_async(
        self,
        request: arms20210519_models.CheckDataConsistencyRequest,
    ) -> arms20210519_models.CheckDataConsistencyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_data_consistency_with_options_async(request, runtime)

    def describe_trace_location_with_options(
        self,
        request: arms20210519_models.DescribeTraceLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DescribeTraceLocationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DescribeTraceLocationResponse(),
            self.do_rpcrequest('DescribeTraceLocation', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_trace_location_with_options_async(
        self,
        request: arms20210519_models.DescribeTraceLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DescribeTraceLocationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DescribeTraceLocationResponse(),
            await self.do_rpcrequest_async('DescribeTraceLocation', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_trace_location(
        self,
        request: arms20210519_models.DescribeTraceLocationRequest,
    ) -> arms20210519_models.DescribeTraceLocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_trace_location_with_options(request, runtime)

    async def describe_trace_location_async(
        self,
        request: arms20210519_models.DescribeTraceLocationRequest,
    ) -> arms20210519_models.DescribeTraceLocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_trace_location_with_options_async(request, runtime)

    def query_metric_with_options(
        self,
        request: arms20210519_models.QueryMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.QueryMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.QueryMetricResponse(),
            self.do_rpcrequest('QueryMetric', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_metric_with_options_async(
        self,
        request: arms20210519_models.QueryMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.QueryMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.QueryMetricResponse(),
            await self.do_rpcrequest_async('QueryMetric', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_metric(
        self,
        request: arms20210519_models.QueryMetricRequest,
    ) -> arms20210519_models.QueryMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_metric_with_options(request, runtime)

    async def query_metric_async(
        self,
        request: arms20210519_models.QueryMetricRequest,
    ) -> arms20210519_models.QueryMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_metric_with_options_async(request, runtime)

    def start_alert_with_options(
        self,
        request: arms20210519_models.StartAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.StartAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.StartAlertResponse(),
            self.do_rpcrequest('StartAlert', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_alert_with_options_async(
        self,
        request: arms20210519_models.StartAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.StartAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.StartAlertResponse(),
            await self.do_rpcrequest_async('StartAlert', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_alert(
        self,
        request: arms20210519_models.StartAlertRequest,
    ) -> arms20210519_models.StartAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_alert_with_options(request, runtime)

    async def start_alert_async(
        self,
        request: arms20210519_models.StartAlertRequest,
    ) -> arms20210519_models.StartAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_alert_with_options_async(request, runtime)

    def set_retcode_share_status_with_options(
        self,
        request: arms20210519_models.SetRetcodeShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SetRetcodeShareStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SetRetcodeShareStatusResponse(),
            self.do_rpcrequest('SetRetcodeShareStatus', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def set_retcode_share_status_with_options_async(
        self,
        request: arms20210519_models.SetRetcodeShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SetRetcodeShareStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SetRetcodeShareStatusResponse(),
            await self.do_rpcrequest_async('SetRetcodeShareStatus', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_retcode_share_status(
        self,
        request: arms20210519_models.SetRetcodeShareStatusRequest,
    ) -> arms20210519_models.SetRetcodeShareStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_retcode_share_status_with_options(request, runtime)

    async def set_retcode_share_status_async(
        self,
        request: arms20210519_models.SetRetcodeShareStatusRequest,
    ) -> arms20210519_models.SetRetcodeShareStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_retcode_share_status_with_options_async(request, runtime)

    def open_xtrace_default_slrwith_options(
        self,
        request: arms20210519_models.OpenXtraceDefaultSLRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.OpenXtraceDefaultSLRResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.OpenXtraceDefaultSLRResponse(),
            self.do_rpcrequest('OpenXtraceDefaultSLR', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_xtrace_default_slrwith_options_async(
        self,
        request: arms20210519_models.OpenXtraceDefaultSLRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.OpenXtraceDefaultSLRResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.OpenXtraceDefaultSLRResponse(),
            await self.do_rpcrequest_async('OpenXtraceDefaultSLR', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_xtrace_default_slr(
        self,
        request: arms20210519_models.OpenXtraceDefaultSLRRequest,
    ) -> arms20210519_models.OpenXtraceDefaultSLRResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_xtrace_default_slrwith_options(request, runtime)

    async def open_xtrace_default_slr_async(
        self,
        request: arms20210519_models.OpenXtraceDefaultSLRRequest,
    ) -> arms20210519_models.OpenXtraceDefaultSLRResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_xtrace_default_slrwith_options_async(request, runtime)

    def list_trace_apps_with_options(
        self,
        request: arms20210519_models.ListTraceAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListTraceAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListTraceAppsResponse(),
            self.do_rpcrequest('ListTraceApps', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_trace_apps_with_options_async(
        self,
        request: arms20210519_models.ListTraceAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListTraceAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListTraceAppsResponse(),
            await self.do_rpcrequest_async('ListTraceApps', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_trace_apps(
        self,
        request: arms20210519_models.ListTraceAppsRequest,
    ) -> arms20210519_models.ListTraceAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_trace_apps_with_options(request, runtime)

    async def list_trace_apps_async(
        self,
        request: arms20210519_models.ListTraceAppsRequest,
    ) -> arms20210519_models.ListTraceAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_trace_apps_with_options_async(request, runtime)

    def get_integration_token_with_options(
        self,
        request: arms20210519_models.GetIntegrationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetIntegrationTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetIntegrationTokenResponse(),
            self.do_rpcrequest('GetIntegrationToken', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_integration_token_with_options_async(
        self,
        request: arms20210519_models.GetIntegrationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetIntegrationTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetIntegrationTokenResponse(),
            await self.do_rpcrequest_async('GetIntegrationToken', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_integration_token(
        self,
        request: arms20210519_models.GetIntegrationTokenRequest,
    ) -> arms20210519_models.GetIntegrationTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_integration_token_with_options(request, runtime)

    async def get_integration_token_async(
        self,
        request: arms20210519_models.GetIntegrationTokenRequest,
    ) -> arms20210519_models.GetIntegrationTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_integration_token_with_options_async(request, runtime)

    def save_trace_app_config_with_options(
        self,
        request: arms20210519_models.SaveTraceAppConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SaveTraceAppConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SaveTraceAppConfigResponse(),
            self.do_rpcrequest('SaveTraceAppConfig', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def save_trace_app_config_with_options_async(
        self,
        request: arms20210519_models.SaveTraceAppConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SaveTraceAppConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SaveTraceAppConfigResponse(),
            await self.do_rpcrequest_async('SaveTraceAppConfig', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def save_trace_app_config(
        self,
        request: arms20210519_models.SaveTraceAppConfigRequest,
    ) -> arms20210519_models.SaveTraceAppConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_trace_app_config_with_options(request, runtime)

    async def save_trace_app_config_async(
        self,
        request: arms20210519_models.SaveTraceAppConfigRequest,
    ) -> arms20210519_models.SaveTraceAppConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_trace_app_config_with_options_async(request, runtime)

    def query_dataset_with_options(
        self,
        request: arms20210519_models.QueryDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.QueryDatasetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.QueryDatasetResponse(),
            self.do_rpcrequest('QueryDataset', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_dataset_with_options_async(
        self,
        request: arms20210519_models.QueryDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.QueryDatasetResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.QueryDatasetResponse(),
            await self.do_rpcrequest_async('QueryDataset', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_dataset(
        self,
        request: arms20210519_models.QueryDatasetRequest,
    ) -> arms20210519_models.QueryDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_with_options(request, runtime)

    async def query_dataset_async(
        self,
        request: arms20210519_models.QueryDatasetRequest,
    ) -> arms20210519_models.QueryDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dataset_with_options_async(request, runtime)

    def update_dispatch_rule_with_options(
        self,
        request: arms20210519_models.UpdateDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.UpdateDispatchRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.UpdateDispatchRuleResponse(),
            self.do_rpcrequest('UpdateDispatchRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_dispatch_rule_with_options_async(
        self,
        request: arms20210519_models.UpdateDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.UpdateDispatchRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.UpdateDispatchRuleResponse(),
            await self.do_rpcrequest_async('UpdateDispatchRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dispatch_rule(
        self,
        request: arms20210519_models.UpdateDispatchRuleRequest,
    ) -> arms20210519_models.UpdateDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dispatch_rule_with_options(request, runtime)

    async def update_dispatch_rule_async(
        self,
        request: arms20210519_models.UpdateDispatchRuleRequest,
    ) -> arms20210519_models.UpdateDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dispatch_rule_with_options_async(request, runtime)

    def delete_dispatch_rule_with_options(
        self,
        request: arms20210519_models.DeleteDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteDispatchRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteDispatchRuleResponse(),
            self.do_rpcrequest('DeleteDispatchRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dispatch_rule_with_options_async(
        self,
        request: arms20210519_models.DeleteDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteDispatchRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteDispatchRuleResponse(),
            await self.do_rpcrequest_async('DeleteDispatchRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dispatch_rule(
        self,
        request: arms20210519_models.DeleteDispatchRuleRequest,
    ) -> arms20210519_models.DeleteDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dispatch_rule_with_options(request, runtime)

    async def delete_dispatch_rule_async(
        self,
        request: arms20210519_models.DeleteDispatchRuleRequest,
    ) -> arms20210519_models.DeleteDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dispatch_rule_with_options_async(request, runtime)

    def describe_dispatch_rule_with_options(
        self,
        request: arms20210519_models.DescribeDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DescribeDispatchRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DescribeDispatchRuleResponse(),
            self.do_rpcrequest('DescribeDispatchRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dispatch_rule_with_options_async(
        self,
        request: arms20210519_models.DescribeDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DescribeDispatchRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DescribeDispatchRuleResponse(),
            await self.do_rpcrequest_async('DescribeDispatchRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dispatch_rule(
        self,
        request: arms20210519_models.DescribeDispatchRuleRequest,
    ) -> arms20210519_models.DescribeDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dispatch_rule_with_options(request, runtime)

    async def describe_dispatch_rule_async(
        self,
        request: arms20210519_models.DescribeDispatchRuleRequest,
    ) -> arms20210519_models.DescribeDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dispatch_rule_with_options_async(request, runtime)

    def import_custom_alert_rules_with_options(
        self,
        request: arms20210519_models.ImportCustomAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ImportCustomAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ImportCustomAlertRulesResponse(),
            self.do_rpcrequest('ImportCustomAlertRules', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_custom_alert_rules_with_options_async(
        self,
        request: arms20210519_models.ImportCustomAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ImportCustomAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ImportCustomAlertRulesResponse(),
            await self.do_rpcrequest_async('ImportCustomAlertRules', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_custom_alert_rules(
        self,
        request: arms20210519_models.ImportCustomAlertRulesRequest,
    ) -> arms20210519_models.ImportCustomAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_custom_alert_rules_with_options(request, runtime)

    async def import_custom_alert_rules_async(
        self,
        request: arms20210519_models.ImportCustomAlertRulesRequest,
    ) -> arms20210519_models.ImportCustomAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_custom_alert_rules_with_options_async(request, runtime)

    def create_wehook_with_options(
        self,
        request: arms20210519_models.CreateWehookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CreateWehookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CreateWehookResponse(),
            self.do_rpcrequest('CreateWehook', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_wehook_with_options_async(
        self,
        request: arms20210519_models.CreateWehookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CreateWehookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CreateWehookResponse(),
            await self.do_rpcrequest_async('CreateWehook', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_wehook(
        self,
        request: arms20210519_models.CreateWehookRequest,
    ) -> arms20210519_models.CreateWehookResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_wehook_with_options(request, runtime)

    async def create_wehook_async(
        self,
        request: arms20210519_models.CreateWehookRequest,
    ) -> arms20210519_models.CreateWehookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_wehook_with_options_async(request, runtime)

    def add_grafana_with_options(
        self,
        request: arms20210519_models.AddGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.AddGrafanaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.AddGrafanaResponse(),
            self.do_rpcrequest('AddGrafana', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_grafana_with_options_async(
        self,
        request: arms20210519_models.AddGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.AddGrafanaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.AddGrafanaResponse(),
            await self.do_rpcrequest_async('AddGrafana', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_grafana(
        self,
        request: arms20210519_models.AddGrafanaRequest,
    ) -> arms20210519_models.AddGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_grafana_with_options(request, runtime)

    async def add_grafana_async(
        self,
        request: arms20210519_models.AddGrafanaRequest,
    ) -> arms20210519_models.AddGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_grafana_with_options_async(request, runtime)

    def search_alert_rules_with_options(
        self,
        request: arms20210519_models.SearchAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchAlertRulesResponse(),
            self.do_rpcrequest('SearchAlertRules', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_alert_rules_with_options_async(
        self,
        request: arms20210519_models.SearchAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchAlertRulesResponse(),
            await self.do_rpcrequest_async('SearchAlertRules', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_alert_rules(
        self,
        request: arms20210519_models.SearchAlertRulesRequest,
    ) -> arms20210519_models.SearchAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_alert_rules_with_options(request, runtime)

    async def search_alert_rules_async(
        self,
        request: arms20210519_models.SearchAlertRulesRequest,
    ) -> arms20210519_models.SearchAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_rules_with_options_async(request, runtime)

    def import_prometheus_rules_with_options(
        self,
        request: arms20210519_models.ImportPrometheusRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ImportPrometheusRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ImportPrometheusRulesResponse(),
            self.do_rpcrequest('ImportPrometheusRules', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def import_prometheus_rules_with_options_async(
        self,
        request: arms20210519_models.ImportPrometheusRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ImportPrometheusRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ImportPrometheusRulesResponse(),
            await self.do_rpcrequest_async('ImportPrometheusRules', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_prometheus_rules(
        self,
        request: arms20210519_models.ImportPrometheusRulesRequest,
    ) -> arms20210519_models.ImportPrometheusRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_prometheus_rules_with_options(request, runtime)

    async def import_prometheus_rules_async(
        self,
        request: arms20210519_models.ImportPrometheusRulesRequest,
    ) -> arms20210519_models.ImportPrometheusRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_prometheus_rules_with_options_async(request, runtime)

    def delete_prometheus_alert_rule_with_options(
        self,
        request: arms20210519_models.DeletePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeletePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeletePrometheusAlertRuleResponse(),
            self.do_rpcrequest('DeletePrometheusAlertRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_prometheus_alert_rule_with_options_async(
        self,
        request: arms20210519_models.DeletePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeletePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeletePrometheusAlertRuleResponse(),
            await self.do_rpcrequest_async('DeletePrometheusAlertRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_prometheus_alert_rule(
        self,
        request: arms20210519_models.DeletePrometheusAlertRuleRequest,
    ) -> arms20210519_models.DeletePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_prometheus_alert_rule_with_options(request, runtime)

    async def delete_prometheus_alert_rule_async(
        self,
        request: arms20210519_models.DeletePrometheusAlertRuleRequest,
    ) -> arms20210519_models.DeletePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_prometheus_alert_rule_with_options_async(request, runtime)

    def send_mse_incident_with_options(
        self,
        request: arms20210519_models.SendMseIncidentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SendMseIncidentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SendMseIncidentResponse(),
            self.do_rpcrequest('SendMseIncident', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_mse_incident_with_options_async(
        self,
        request: arms20210519_models.SendMseIncidentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SendMseIncidentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SendMseIncidentResponse(),
            await self.do_rpcrequest_async('SendMseIncident', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_mse_incident(
        self,
        request: arms20210519_models.SendMseIncidentRequest,
    ) -> arms20210519_models.SendMseIncidentResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_mse_incident_with_options(request, runtime)

    async def send_mse_incident_async(
        self,
        request: arms20210519_models.SendMseIncidentRequest,
    ) -> arms20210519_models.SendMseIncidentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_mse_incident_with_options_async(request, runtime)

    def delete_alert_contact_with_options(
        self,
        request: arms20210519_models.DeleteAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteAlertContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteAlertContactResponse(),
            self.do_rpcrequest('DeleteAlertContact', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_alert_contact_with_options_async(
        self,
        request: arms20210519_models.DeleteAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteAlertContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteAlertContactResponse(),
            await self.do_rpcrequest_async('DeleteAlertContact', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_alert_contact(
        self,
        request: arms20210519_models.DeleteAlertContactRequest,
    ) -> arms20210519_models.DeleteAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_with_options(request, runtime)

    async def delete_alert_contact_async(
        self,
        request: arms20210519_models.DeleteAlertContactRequest,
    ) -> arms20210519_models.DeleteAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_contact_with_options_async(request, runtime)

    def get_trace_with_options(
        self,
        request: arms20210519_models.GetTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetTraceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetTraceResponse(),
            self.do_rpcrequest('GetTrace', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_trace_with_options_async(
        self,
        request: arms20210519_models.GetTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetTraceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetTraceResponse(),
            await self.do_rpcrequest_async('GetTrace', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_trace(
        self,
        request: arms20210519_models.GetTraceRequest,
    ) -> arms20210519_models.GetTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_trace_with_options(request, runtime)

    async def get_trace_async(
        self,
        request: arms20210519_models.GetTraceRequest,
    ) -> arms20210519_models.GetTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_trace_with_options_async(request, runtime)

    def delete_retcode_app_with_options(
        self,
        request: arms20210519_models.DeleteRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteRetcodeAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteRetcodeAppResponse(),
            self.do_rpcrequest('DeleteRetcodeApp', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_retcode_app_with_options_async(
        self,
        request: arms20210519_models.DeleteRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteRetcodeAppResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteRetcodeAppResponse(),
            await self.do_rpcrequest_async('DeleteRetcodeApp', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_retcode_app(
        self,
        request: arms20210519_models.DeleteRetcodeAppRequest,
    ) -> arms20210519_models.DeleteRetcodeAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_retcode_app_with_options(request, runtime)

    async def delete_retcode_app_async(
        self,
        request: arms20210519_models.DeleteRetcodeAppRequest,
    ) -> arms20210519_models.DeleteRetcodeAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_retcode_app_with_options_async(request, runtime)

    def update_alert_template_with_options(
        self,
        request: arms20210519_models.UpdateAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.UpdateAlertTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.UpdateAlertTemplateResponse(),
            self.do_rpcrequest('UpdateAlertTemplate', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_alert_template_with_options_async(
        self,
        request: arms20210519_models.UpdateAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.UpdateAlertTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.UpdateAlertTemplateResponse(),
            await self.do_rpcrequest_async('UpdateAlertTemplate', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_alert_template(
        self,
        request: arms20210519_models.UpdateAlertTemplateRequest,
    ) -> arms20210519_models.UpdateAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_alert_template_with_options(request, runtime)

    async def update_alert_template_async(
        self,
        request: arms20210519_models.UpdateAlertTemplateRequest,
    ) -> arms20210519_models.UpdateAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_alert_template_with_options_async(request, runtime)

    def add_integration_with_options(
        self,
        request: arms20210519_models.AddIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.AddIntegrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.AddIntegrationResponse(),
            self.do_rpcrequest('AddIntegration', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_integration_with_options_async(
        self,
        request: arms20210519_models.AddIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.AddIntegrationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.AddIntegrationResponse(),
            await self.do_rpcrequest_async('AddIntegration', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_integration(
        self,
        request: arms20210519_models.AddIntegrationRequest,
    ) -> arms20210519_models.AddIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_integration_with_options(request, runtime)

    async def add_integration_async(
        self,
        request: arms20210519_models.AddIntegrationRequest,
    ) -> arms20210519_models.AddIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_integration_with_options_async(request, runtime)

    def search_retcode_app_by_page_with_options(
        self,
        request: arms20210519_models.SearchRetcodeAppByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchRetcodeAppByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchRetcodeAppByPageResponse(),
            self.do_rpcrequest('SearchRetcodeAppByPage', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_retcode_app_by_page_with_options_async(
        self,
        request: arms20210519_models.SearchRetcodeAppByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchRetcodeAppByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchRetcodeAppByPageResponse(),
            await self.do_rpcrequest_async('SearchRetcodeAppByPage', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_retcode_app_by_page(
        self,
        request: arms20210519_models.SearchRetcodeAppByPageRequest,
    ) -> arms20210519_models.SearchRetcodeAppByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_retcode_app_by_page_with_options(request, runtime)

    async def search_retcode_app_by_page_async(
        self,
        request: arms20210519_models.SearchRetcodeAppByPageRequest,
    ) -> arms20210519_models.SearchRetcodeAppByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_retcode_app_by_page_with_options_async(request, runtime)

    def stop_alert_with_options(
        self,
        request: arms20210519_models.StopAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.StopAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.StopAlertResponse(),
            self.do_rpcrequest('StopAlert', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def stop_alert_with_options_async(
        self,
        request: arms20210519_models.StopAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.StopAlertResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.StopAlertResponse(),
            await self.do_rpcrequest_async('StopAlert', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_alert(
        self,
        request: arms20210519_models.StopAlertRequest,
    ) -> arms20210519_models.StopAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_alert_with_options(request, runtime)

    async def stop_alert_async(
        self,
        request: arms20210519_models.StopAlertRequest,
    ) -> arms20210519_models.StopAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_alert_with_options_async(request, runtime)

    def get_app_api_by_page_with_options(
        self,
        request: arms20210519_models.GetAppApiByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetAppApiByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetAppApiByPageResponse(),
            self.do_rpcrequest('GetAppApiByPage', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_app_api_by_page_with_options_async(
        self,
        request: arms20210519_models.GetAppApiByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetAppApiByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetAppApiByPageResponse(),
            await self.do_rpcrequest_async('GetAppApiByPage', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_app_api_by_page(
        self,
        request: arms20210519_models.GetAppApiByPageRequest,
    ) -> arms20210519_models.GetAppApiByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_api_by_page_with_options(request, runtime)

    async def get_app_api_by_page_async(
        self,
        request: arms20210519_models.GetAppApiByPageRequest,
    ) -> arms20210519_models.GetAppApiByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_api_by_page_with_options_async(request, runtime)

    def list_activated_alerts_with_options(
        self,
        request: arms20210519_models.ListActivatedAlertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListActivatedAlertsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListActivatedAlertsResponse(),
            self.do_rpcrequest('ListActivatedAlerts', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_activated_alerts_with_options_async(
        self,
        request: arms20210519_models.ListActivatedAlertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListActivatedAlertsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListActivatedAlertsResponse(),
            await self.do_rpcrequest_async('ListActivatedAlerts', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_activated_alerts(
        self,
        request: arms20210519_models.ListActivatedAlertsRequest,
    ) -> arms20210519_models.ListActivatedAlertsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_activated_alerts_with_options(request, runtime)

    async def list_activated_alerts_async(
        self,
        request: arms20210519_models.ListActivatedAlertsRequest,
    ) -> arms20210519_models.ListActivatedAlertsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_activated_alerts_with_options_async(request, runtime)

    def search_traces_by_page_with_options(
        self,
        request: arms20210519_models.SearchTracesByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchTracesByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchTracesByPageResponse(),
            self.do_rpcrequest('SearchTracesByPage', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_traces_by_page_with_options_async(
        self,
        request: arms20210519_models.SearchTracesByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchTracesByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchTracesByPageResponse(),
            await self.do_rpcrequest_async('SearchTracesByPage', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_traces_by_page(
        self,
        request: arms20210519_models.SearchTracesByPageRequest,
    ) -> arms20210519_models.SearchTracesByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_traces_by_page_with_options(request, runtime)

    async def search_traces_by_page_async(
        self,
        request: arms20210519_models.SearchTracesByPageRequest,
    ) -> arms20210519_models.SearchTracesByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_traces_by_page_with_options_async(request, runtime)

    def get_multiple_trace_with_options(
        self,
        request: arms20210519_models.GetMultipleTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetMultipleTraceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetMultipleTraceResponse(),
            self.do_rpcrequest('GetMultipleTrace', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_multiple_trace_with_options_async(
        self,
        request: arms20210519_models.GetMultipleTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetMultipleTraceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetMultipleTraceResponse(),
            await self.do_rpcrequest_async('GetMultipleTrace', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_multiple_trace(
        self,
        request: arms20210519_models.GetMultipleTraceRequest,
    ) -> arms20210519_models.GetMultipleTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_multiple_trace_with_options(request, runtime)

    async def get_multiple_trace_async(
        self,
        request: arms20210519_models.GetMultipleTraceRequest,
    ) -> arms20210519_models.GetMultipleTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_multiple_trace_with_options_async(request, runtime)

    def update_alert_contact_with_options(
        self,
        request: arms20210519_models.UpdateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.UpdateAlertContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.UpdateAlertContactResponse(),
            self.do_rpcrequest('UpdateAlertContact', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_alert_contact_with_options_async(
        self,
        request: arms20210519_models.UpdateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.UpdateAlertContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.UpdateAlertContactResponse(),
            await self.do_rpcrequest_async('UpdateAlertContact', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_alert_contact(
        self,
        request: arms20210519_models.UpdateAlertContactRequest,
    ) -> arms20210519_models.UpdateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_alert_contact_with_options(request, runtime)

    async def update_alert_contact_async(
        self,
        request: arms20210519_models.UpdateAlertContactRequest,
    ) -> arms20210519_models.UpdateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_alert_contact_with_options_async(request, runtime)

    def create_webhook_with_options(
        self,
        request: arms20210519_models.CreateWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CreateWebhookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CreateWebhookResponse(),
            self.do_rpcrequest('CreateWebhook', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_webhook_with_options_async(
        self,
        request: arms20210519_models.CreateWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CreateWebhookResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CreateWebhookResponse(),
            await self.do_rpcrequest_async('CreateWebhook', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_webhook(
        self,
        request: arms20210519_models.CreateWebhookRequest,
    ) -> arms20210519_models.CreateWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_webhook_with_options(request, runtime)

    async def create_webhook_async(
        self,
        request: arms20210519_models.CreateWebhookRequest,
    ) -> arms20210519_models.CreateWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_webhook_with_options_async(request, runtime)

    def describe_trace_license_key_with_options(
        self,
        request: arms20210519_models.DescribeTraceLicenseKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DescribeTraceLicenseKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DescribeTraceLicenseKeyResponse(),
            self.do_rpcrequest('DescribeTraceLicenseKey', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_trace_license_key_with_options_async(
        self,
        request: arms20210519_models.DescribeTraceLicenseKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DescribeTraceLicenseKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DescribeTraceLicenseKeyResponse(),
            await self.do_rpcrequest_async('DescribeTraceLicenseKey', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_trace_license_key(
        self,
        request: arms20210519_models.DescribeTraceLicenseKeyRequest,
    ) -> arms20210519_models.DescribeTraceLicenseKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_trace_license_key_with_options(request, runtime)

    async def describe_trace_license_key_async(
        self,
        request: arms20210519_models.DescribeTraceLicenseKeyRequest,
    ) -> arms20210519_models.DescribeTraceLicenseKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_trace_license_key_with_options_async(request, runtime)

    def delete_alert_template_with_options(
        self,
        request: arms20210519_models.DeleteAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteAlertTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteAlertTemplateResponse(),
            self.do_rpcrequest('DeleteAlertTemplate', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_alert_template_with_options_async(
        self,
        request: arms20210519_models.DeleteAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteAlertTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteAlertTemplateResponse(),
            await self.do_rpcrequest_async('DeleteAlertTemplate', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_alert_template(
        self,
        request: arms20210519_models.DeleteAlertTemplateRequest,
    ) -> arms20210519_models.DeleteAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_template_with_options(request, runtime)

    async def delete_alert_template_async(
        self,
        request: arms20210519_models.DeleteAlertTemplateRequest,
    ) -> arms20210519_models.DeleteAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_template_with_options_async(request, runtime)

    def create_dispatch_rule_with_options(
        self,
        request: arms20210519_models.CreateDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CreateDispatchRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CreateDispatchRuleResponse(),
            self.do_rpcrequest('CreateDispatchRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dispatch_rule_with_options_async(
        self,
        request: arms20210519_models.CreateDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CreateDispatchRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CreateDispatchRuleResponse(),
            await self.do_rpcrequest_async('CreateDispatchRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dispatch_rule(
        self,
        request: arms20210519_models.CreateDispatchRuleRequest,
    ) -> arms20210519_models.CreateDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dispatch_rule_with_options(request, runtime)

    async def create_dispatch_rule_async(
        self,
        request: arms20210519_models.CreateDispatchRuleRequest,
    ) -> arms20210519_models.CreateDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dispatch_rule_with_options_async(request, runtime)

    def list_prometheus_alert_templates_with_options(
        self,
        request: arms20210519_models.ListPrometheusAlertTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListPrometheusAlertTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListPrometheusAlertTemplatesResponse(),
            self.do_rpcrequest('ListPrometheusAlertTemplates', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_prometheus_alert_templates_with_options_async(
        self,
        request: arms20210519_models.ListPrometheusAlertTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListPrometheusAlertTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListPrometheusAlertTemplatesResponse(),
            await self.do_rpcrequest_async('ListPrometheusAlertTemplates', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_prometheus_alert_templates(
        self,
        request: arms20210519_models.ListPrometheusAlertTemplatesRequest,
    ) -> arms20210519_models.ListPrometheusAlertTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_alert_templates_with_options(request, runtime)

    async def list_prometheus_alert_templates_async(
        self,
        request: arms20210519_models.ListPrometheusAlertTemplatesRequest,
    ) -> arms20210519_models.ListPrometheusAlertTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_prometheus_alert_templates_with_options_async(request, runtime)

    def describe_prometheus_alert_rule_with_options(
        self,
        request: arms20210519_models.DescribePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DescribePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DescribePrometheusAlertRuleResponse(),
            self.do_rpcrequest('DescribePrometheusAlertRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_prometheus_alert_rule_with_options_async(
        self,
        request: arms20210519_models.DescribePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DescribePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DescribePrometheusAlertRuleResponse(),
            await self.do_rpcrequest_async('DescribePrometheusAlertRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_prometheus_alert_rule(
        self,
        request: arms20210519_models.DescribePrometheusAlertRuleRequest,
    ) -> arms20210519_models.DescribePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_prometheus_alert_rule_with_options(request, runtime)

    async def describe_prometheus_alert_rule_async(
        self,
        request: arms20210519_models.DescribePrometheusAlertRuleRequest,
    ) -> arms20210519_models.DescribePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_prometheus_alert_rule_with_options_async(request, runtime)

    def update_alert_rule_with_options(
        self,
        request: arms20210519_models.UpdateAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.UpdateAlertRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.UpdateAlertRuleResponse(),
            self.do_rpcrequest('UpdateAlertRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_alert_rule_with_options_async(
        self,
        request: arms20210519_models.UpdateAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.UpdateAlertRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.UpdateAlertRuleResponse(),
            await self.do_rpcrequest_async('UpdateAlertRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_alert_rule(
        self,
        request: arms20210519_models.UpdateAlertRuleRequest,
    ) -> arms20210519_models.UpdateAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_alert_rule_with_options(request, runtime)

    async def update_alert_rule_async(
        self,
        request: arms20210519_models.UpdateAlertRuleRequest,
    ) -> arms20210519_models.UpdateAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_alert_rule_with_options_async(request, runtime)

    def list_alert_templates_with_options(
        self,
        request: arms20210519_models.ListAlertTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListAlertTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListAlertTemplatesResponse(),
            self.do_rpcrequest('ListAlertTemplates', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_alert_templates_with_options_async(
        self,
        request: arms20210519_models.ListAlertTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListAlertTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListAlertTemplatesResponse(),
            await self.do_rpcrequest_async('ListAlertTemplates', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_alert_templates(
        self,
        request: arms20210519_models.ListAlertTemplatesRequest,
    ) -> arms20210519_models.ListAlertTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_alert_templates_with_options(request, runtime)

    async def list_alert_templates_async(
        self,
        request: arms20210519_models.ListAlertTemplatesRequest,
    ) -> arms20210519_models.ListAlertTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_alert_templates_with_options_async(request, runtime)

    def search_alert_contact_group_with_options(
        self,
        request: arms20210519_models.SearchAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchAlertContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchAlertContactGroupResponse(),
            self.do_rpcrequest('SearchAlertContactGroup', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_alert_contact_group_with_options_async(
        self,
        request: arms20210519_models.SearchAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.SearchAlertContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.SearchAlertContactGroupResponse(),
            await self.do_rpcrequest_async('SearchAlertContactGroup', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_alert_contact_group(
        self,
        request: arms20210519_models.SearchAlertContactGroupRequest,
    ) -> arms20210519_models.SearchAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_alert_contact_group_with_options(request, runtime)

    async def search_alert_contact_group_async(
        self,
        request: arms20210519_models.SearchAlertContactGroupRequest,
    ) -> arms20210519_models.SearchAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_contact_group_with_options_async(request, runtime)

    def create_alert_contact_with_options(
        self,
        request: arms20210519_models.CreateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CreateAlertContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CreateAlertContactResponse(),
            self.do_rpcrequest('CreateAlertContact', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_alert_contact_with_options_async(
        self,
        request: arms20210519_models.CreateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CreateAlertContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CreateAlertContactResponse(),
            await self.do_rpcrequest_async('CreateAlertContact', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_alert_contact(
        self,
        request: arms20210519_models.CreateAlertContactRequest,
    ) -> arms20210519_models.CreateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_alert_contact_with_options(request, runtime)

    async def create_alert_contact_async(
        self,
        request: arms20210519_models.CreateAlertContactRequest,
    ) -> arms20210519_models.CreateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_alert_contact_with_options_async(request, runtime)

    def delete_scenario_with_options(
        self,
        request: arms20210519_models.DeleteScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteScenarioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteScenarioResponse(),
            self.do_rpcrequest('DeleteScenario', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_scenario_with_options_async(
        self,
        request: arms20210519_models.DeleteScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteScenarioResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteScenarioResponse(),
            await self.do_rpcrequest_async('DeleteScenario', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scenario(
        self,
        request: arms20210519_models.DeleteScenarioRequest,
    ) -> arms20210519_models.DeleteScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scenario_with_options(request, runtime)

    async def delete_scenario_async(
        self,
        request: arms20210519_models.DeleteScenarioRequest,
    ) -> arms20210519_models.DeleteScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scenario_with_options_async(request, runtime)

    def list_dispatch_rule_with_options(
        self,
        request: arms20210519_models.ListDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListDispatchRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListDispatchRuleResponse(),
            self.do_rpcrequest('ListDispatchRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_dispatch_rule_with_options_async(
        self,
        request: arms20210519_models.ListDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListDispatchRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListDispatchRuleResponse(),
            await self.do_rpcrequest_async('ListDispatchRule', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_dispatch_rule(
        self,
        request: arms20210519_models.ListDispatchRuleRequest,
    ) -> arms20210519_models.ListDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dispatch_rule_with_options(request, runtime)

    async def list_dispatch_rule_async(
        self,
        request: arms20210519_models.ListDispatchRuleRequest,
    ) -> arms20210519_models.ListDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dispatch_rule_with_options_async(request, runtime)

    def get_arms_console_url_with_options(
        self,
        request: arms20210519_models.GetArmsConsoleUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetArmsConsoleUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            arms20210519_models.GetArmsConsoleUrlResponse(),
            self.do_rpcrequest('GetArmsConsoleUrl', '2021-05-19', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def get_arms_console_url_with_options_async(
        self,
        request: arms20210519_models.GetArmsConsoleUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetArmsConsoleUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            arms20210519_models.GetArmsConsoleUrlResponse(),
            await self.do_rpcrequest_async('GetArmsConsoleUrl', '2021-05-19', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_arms_console_url(
        self,
        request: arms20210519_models.GetArmsConsoleUrlRequest,
    ) -> arms20210519_models.GetArmsConsoleUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_arms_console_url_with_options(request, runtime)

    async def get_arms_console_url_async(
        self,
        request: arms20210519_models.GetArmsConsoleUrlRequest,
    ) -> arms20210519_models.GetArmsConsoleUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_arms_console_url_with_options_async(request, runtime)

    def get_retcode_share_url_with_options(
        self,
        request: arms20210519_models.GetRetcodeShareUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetRetcodeShareUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetRetcodeShareUrlResponse(),
            self.do_rpcrequest('GetRetcodeShareUrl', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_retcode_share_url_with_options_async(
        self,
        request: arms20210519_models.GetRetcodeShareUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetRetcodeShareUrlResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetRetcodeShareUrlResponse(),
            await self.do_rpcrequest_async('GetRetcodeShareUrl', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_retcode_share_url(
        self,
        request: arms20210519_models.GetRetcodeShareUrlRequest,
    ) -> arms20210519_models.GetRetcodeShareUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_retcode_share_url_with_options(request, runtime)

    async def get_retcode_share_url_async(
        self,
        request: arms20210519_models.GetRetcodeShareUrlRequest,
    ) -> arms20210519_models.GetRetcodeShareUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_retcode_share_url_with_options_async(request, runtime)

    def disable_alert_template_with_options(
        self,
        request: arms20210519_models.DisableAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DisableAlertTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DisableAlertTemplateResponse(),
            self.do_rpcrequest('DisableAlertTemplate', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_alert_template_with_options_async(
        self,
        request: arms20210519_models.DisableAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DisableAlertTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DisableAlertTemplateResponse(),
            await self.do_rpcrequest_async('DisableAlertTemplate', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_alert_template(
        self,
        request: arms20210519_models.DisableAlertTemplateRequest,
    ) -> arms20210519_models.DisableAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_alert_template_with_options(request, runtime)

    async def disable_alert_template_async(
        self,
        request: arms20210519_models.DisableAlertTemplateRequest,
    ) -> arms20210519_models.DisableAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_alert_template_with_options_async(request, runtime)

    def list_retcode_apps_with_options(
        self,
        request: arms20210519_models.ListRetcodeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListRetcodeAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListRetcodeAppsResponse(),
            self.do_rpcrequest('ListRetcodeApps', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_retcode_apps_with_options_async(
        self,
        request: arms20210519_models.ListRetcodeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListRetcodeAppsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListRetcodeAppsResponse(),
            await self.do_rpcrequest_async('ListRetcodeApps', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_retcode_apps(
        self,
        request: arms20210519_models.ListRetcodeAppsRequest,
    ) -> arms20210519_models.ListRetcodeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_retcode_apps_with_options(request, runtime)

    async def list_retcode_apps_async(
        self,
        request: arms20210519_models.ListRetcodeAppsRequest,
    ) -> arms20210519_models.ListRetcodeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_retcode_apps_with_options_async(request, runtime)

    def get_stack_with_options(
        self,
        request: arms20210519_models.GetStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetStackResponse(),
            self.do_rpcrequest('GetStack', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_stack_with_options_async(
        self,
        request: arms20210519_models.GetStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetStackResponse(),
            await self.do_rpcrequest_async('GetStack', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_stack(
        self,
        request: arms20210519_models.GetStackRequest,
    ) -> arms20210519_models.GetStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_with_options(request, runtime)

    async def get_stack_async(
        self,
        request: arms20210519_models.GetStackRequest,
    ) -> arms20210519_models.GetStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_with_options_async(request, runtime)

    def open_arms_service_second_version_with_options(
        self,
        request: arms20210519_models.OpenArmsServiceSecondVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.OpenArmsServiceSecondVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.OpenArmsServiceSecondVersionResponse(),
            self.do_rpcrequest('OpenArmsServiceSecondVersion', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_arms_service_second_version_with_options_async(
        self,
        request: arms20210519_models.OpenArmsServiceSecondVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.OpenArmsServiceSecondVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.OpenArmsServiceSecondVersionResponse(),
            await self.do_rpcrequest_async('OpenArmsServiceSecondVersion', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_arms_service_second_version(
        self,
        request: arms20210519_models.OpenArmsServiceSecondVersionRequest,
    ) -> arms20210519_models.OpenArmsServiceSecondVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_arms_service_second_version_with_options(request, runtime)

    async def open_arms_service_second_version_async(
        self,
        request: arms20210519_models.OpenArmsServiceSecondVersionRequest,
    ) -> arms20210519_models.OpenArmsServiceSecondVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_arms_service_second_version_with_options_async(request, runtime)

    def list_prom_clusters_with_options(
        self,
        request: arms20210519_models.ListPromClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListPromClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListPromClustersResponse(),
            self.do_rpcrequest('ListPromClusters', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_prom_clusters_with_options_async(
        self,
        request: arms20210519_models.ListPromClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.ListPromClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.ListPromClustersResponse(),
            await self.do_rpcrequest_async('ListPromClusters', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_prom_clusters(
        self,
        request: arms20210519_models.ListPromClustersRequest,
    ) -> arms20210519_models.ListPromClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_prom_clusters_with_options(request, runtime)

    async def list_prom_clusters_async(
        self,
        request: arms20210519_models.ListPromClustersRequest,
    ) -> arms20210519_models.ListPromClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_prom_clusters_with_options_async(request, runtime)

    def get_consistency_snapshot_with_options(
        self,
        request: arms20210519_models.GetConsistencySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetConsistencySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetConsistencySnapshotResponse(),
            self.do_rpcrequest('GetConsistencySnapshot', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_consistency_snapshot_with_options_async(
        self,
        request: arms20210519_models.GetConsistencySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.GetConsistencySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.GetConsistencySnapshotResponse(),
            await self.do_rpcrequest_async('GetConsistencySnapshot', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_consistency_snapshot(
        self,
        request: arms20210519_models.GetConsistencySnapshotRequest,
    ) -> arms20210519_models.GetConsistencySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_consistency_snapshot_with_options(request, runtime)

    async def get_consistency_snapshot_async(
        self,
        request: arms20210519_models.GetConsistencySnapshotRequest,
    ) -> arms20210519_models.GetConsistencySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_consistency_snapshot_with_options_async(request, runtime)

    def query_metric_by_page_with_options(
        self,
        request: arms20210519_models.QueryMetricByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.QueryMetricByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.QueryMetricByPageResponse(),
            self.do_rpcrequest('QueryMetricByPage', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_metric_by_page_with_options_async(
        self,
        request: arms20210519_models.QueryMetricByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.QueryMetricByPageResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.QueryMetricByPageResponse(),
            await self.do_rpcrequest_async('QueryMetricByPage', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_metric_by_page(
        self,
        request: arms20210519_models.QueryMetricByPageRequest,
    ) -> arms20210519_models.QueryMetricByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_metric_by_page_with_options(request, runtime)

    async def query_metric_by_page_async(
        self,
        request: arms20210519_models.QueryMetricByPageRequest,
    ) -> arms20210519_models.QueryMetricByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_metric_by_page_with_options_async(request, runtime)

    def install_cms_exporter_with_options(
        self,
        request: arms20210519_models.InstallCmsExporterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.InstallCmsExporterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.InstallCmsExporterResponse(),
            self.do_rpcrequest('InstallCmsExporter', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def install_cms_exporter_with_options_async(
        self,
        request: arms20210519_models.InstallCmsExporterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.InstallCmsExporterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.InstallCmsExporterResponse(),
            await self.do_rpcrequest_async('InstallCmsExporter', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def install_cms_exporter(
        self,
        request: arms20210519_models.InstallCmsExporterRequest,
    ) -> arms20210519_models.InstallCmsExporterResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_cms_exporter_with_options(request, runtime)

    async def install_cms_exporter_async(
        self,
        request: arms20210519_models.InstallCmsExporterRequest,
    ) -> arms20210519_models.InstallCmsExporterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_cms_exporter_with_options_async(request, runtime)

    def delete_alert_rules_with_options(
        self,
        request: arms20210519_models.DeleteAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteAlertRulesResponse(),
            self.do_rpcrequest('DeleteAlertRules', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_alert_rules_with_options_async(
        self,
        request: arms20210519_models.DeleteAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.DeleteAlertRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.DeleteAlertRulesResponse(),
            await self.do_rpcrequest_async('DeleteAlertRules', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_alert_rules(
        self,
        request: arms20210519_models.DeleteAlertRulesRequest,
    ) -> arms20210519_models.DeleteAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_rules_with_options(request, runtime)

    async def delete_alert_rules_async(
        self,
        request: arms20210519_models.DeleteAlertRulesRequest,
    ) -> arms20210519_models.DeleteAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_rules_with_options_async(request, runtime)

    def check_service_linked_role_for_deleting_with_options(
        self,
        request: arms20210519_models.CheckServiceLinkedRoleForDeletingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CheckServiceLinkedRoleForDeletingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CheckServiceLinkedRoleForDeletingResponse(),
            self.do_rpcrequest('CheckServiceLinkedRoleForDeleting', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def check_service_linked_role_for_deleting_with_options_async(
        self,
        request: arms20210519_models.CheckServiceLinkedRoleForDeletingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210519_models.CheckServiceLinkedRoleForDeletingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            arms20210519_models.CheckServiceLinkedRoleForDeletingResponse(),
            await self.do_rpcrequest_async('CheckServiceLinkedRoleForDeleting', '2021-05-19', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_service_linked_role_for_deleting(
        self,
        request: arms20210519_models.CheckServiceLinkedRoleForDeletingRequest,
    ) -> arms20210519_models.CheckServiceLinkedRoleForDeletingResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_for_deleting_with_options(request, runtime)

    async def check_service_linked_role_for_deleting_async(
        self,
        request: arms20210519_models.CheckServiceLinkedRoleForDeletingRequest,
    ) -> arms20210519_models.CheckServiceLinkedRoleForDeletingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_service_linked_role_for_deleting_with_options_async(request, runtime)
