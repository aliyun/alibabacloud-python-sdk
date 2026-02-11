# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_arms20210422 import models as main_models
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
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'ap-northeast-2-pop': 'arms.aliyuncs.com',
            'cn-beijing-finance-1': 'arms.aliyuncs.com',
            'cn-beijing-finance-pop': 'arms.aliyuncs.com',
            'cn-beijing-gov-1': 'arms.aliyuncs.com',
            'cn-beijing-nu16-b01': 'arms.aliyuncs.com',
            'cn-edge-1': 'arms.aliyuncs.com',
            'cn-fujian': 'arms.aliyuncs.com',
            'cn-haidian-cm12-c01': 'arms.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'arms.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'arms.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'arms.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'arms.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'arms.aliyuncs.com',
            'cn-hangzhou-test-306': 'arms.aliyuncs.com',
            'cn-hongkong-finance-pop': 'arms.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'arms.aliyuncs.com',
            'cn-qingdao-nebula': 'arms.aliyuncs.com',
            'cn-shanghai-et15-b01': 'arms.aliyuncs.com',
            'cn-shanghai-et2-b01': 'arms.aliyuncs.com',
            'cn-shanghai-inner': 'arms.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'arms.aliyuncs.com',
            'cn-shenzhen-inner': 'arms.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'arms.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'arms.aliyuncs.com',
            'cn-wuhan': 'arms.aliyuncs.com',
            'cn-yushanfang': 'arms.aliyuncs.com',
            'cn-zhangbei': 'arms.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'arms.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'arms.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'arms.aliyuncs.com',
            'eu-west-1-oxs': 'arms.aliyuncs.com',
            'me-east-1': 'arms.aliyuncs.com',
            'rus-west-1-pop': 'arms.aliyuncs.com'
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_grafana_with_options(
        self,
        request: main_models.AddGrafanaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGrafanaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.integration):
            query['Integration'] = request.integration
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGrafana',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGrafanaResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_grafana_with_options_async(
        self,
        request: main_models.AddGrafanaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddGrafanaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.integration):
            query['Integration'] = request.integration
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddGrafana',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddGrafanaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_grafana(
        self,
        request: main_models.AddGrafanaRequest,
    ) -> main_models.AddGrafanaResponse:
        runtime = RuntimeOptions()
        return self.add_grafana_with_options(request, runtime)

    async def add_grafana_async(
        self,
        request: main_models.AddGrafanaRequest,
    ) -> main_models.AddGrafanaResponse:
        runtime = RuntimeOptions()
        return await self.add_grafana_with_options_async(request, runtime)

    def add_integration_with_options(
        self,
        request: main_models.AddIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddIntegrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.integration):
            query['Integration'] = request.integration
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddIntegration',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_integration_with_options_async(
        self,
        request: main_models.AddIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddIntegrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.integration):
            query['Integration'] = request.integration
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddIntegration',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_integration(
        self,
        request: main_models.AddIntegrationRequest,
    ) -> main_models.AddIntegrationResponse:
        runtime = RuntimeOptions()
        return self.add_integration_with_options(request, runtime)

    async def add_integration_async(
        self,
        request: main_models.AddIntegrationRequest,
    ) -> main_models.AddIntegrationResponse:
        runtime = RuntimeOptions()
        return await self.add_integration_with_options_async(request, runtime)

    def apply_scenario_with_options(
        self,
        tmp_req: main_models.ApplyScenarioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyScenarioResponse:
        tmp_req.validate()
        request = main_models.ApplyScenarioShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config):
            request.config_shrink = Utils.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.config_shrink):
            query['Config'] = request.config_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scenario):
            query['Scenario'] = request.scenario
        if not DaraCore.is_null(request.sign):
            query['Sign'] = request.sign
        if not DaraCore.is_null(request.sn_dump):
            query['SnDump'] = request.sn_dump
        if not DaraCore.is_null(request.sn_force):
            query['SnForce'] = request.sn_force
        if not DaraCore.is_null(request.sn_stat):
            query['SnStat'] = request.sn_stat
        if not DaraCore.is_null(request.sn_transfer):
            query['SnTransfer'] = request.sn_transfer
        if not DaraCore.is_null(request.update_option):
            query['UpdateOption'] = request.update_option
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyScenario',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_scenario_with_options_async(
        self,
        tmp_req: main_models.ApplyScenarioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyScenarioResponse:
        tmp_req.validate()
        request = main_models.ApplyScenarioShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.config):
            request.config_shrink = Utils.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.config_shrink):
            query['Config'] = request.config_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scenario):
            query['Scenario'] = request.scenario
        if not DaraCore.is_null(request.sign):
            query['Sign'] = request.sign
        if not DaraCore.is_null(request.sn_dump):
            query['SnDump'] = request.sn_dump
        if not DaraCore.is_null(request.sn_force):
            query['SnForce'] = request.sn_force
        if not DaraCore.is_null(request.sn_stat):
            query['SnStat'] = request.sn_stat
        if not DaraCore.is_null(request.sn_transfer):
            query['SnTransfer'] = request.sn_transfer
        if not DaraCore.is_null(request.update_option):
            query['UpdateOption'] = request.update_option
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyScenario',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyScenarioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_scenario(
        self,
        request: main_models.ApplyScenarioRequest,
    ) -> main_models.ApplyScenarioResponse:
        runtime = RuntimeOptions()
        return self.apply_scenario_with_options(request, runtime)

    async def apply_scenario_async(
        self,
        request: main_models.ApplyScenarioRequest,
    ) -> main_models.ApplyScenarioResponse:
        runtime = RuntimeOptions()
        return await self.apply_scenario_with_options_async(request, runtime)

    def check_data_consistency_with_options(
        self,
        request: main_models.CheckDataConsistencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDataConsistencyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.current_timestamp):
            query['CurrentTimestamp'] = request.current_timestamp
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDataConsistency',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDataConsistencyResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_data_consistency_with_options_async(
        self,
        request: main_models.CheckDataConsistencyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckDataConsistencyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.current_timestamp):
            query['CurrentTimestamp'] = request.current_timestamp
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckDataConsistency',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDataConsistencyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_data_consistency(
        self,
        request: main_models.CheckDataConsistencyRequest,
    ) -> main_models.CheckDataConsistencyResponse:
        runtime = RuntimeOptions()
        return self.check_data_consistency_with_options(request, runtime)

    async def check_data_consistency_async(
        self,
        request: main_models.CheckDataConsistencyRequest,
    ) -> main_models.CheckDataConsistencyResponse:
        runtime = RuntimeOptions()
        return await self.check_data_consistency_with_options_async(request, runtime)

    def check_service_linked_role_for_deleting_with_options(
        self,
        request: main_models.CheckServiceLinkedRoleForDeletingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckServiceLinkedRoleForDeletingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.spiregion_id):
            query['SPIRegionId'] = request.spiregion_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceLinkedRoleForDeleting',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckServiceLinkedRoleForDeletingResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_linked_role_for_deleting_with_options_async(
        self,
        request: main_models.CheckServiceLinkedRoleForDeletingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckServiceLinkedRoleForDeletingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not DaraCore.is_null(request.spiregion_id):
            query['SPIRegionId'] = request.spiregion_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceLinkedRoleForDeleting',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckServiceLinkedRoleForDeletingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_linked_role_for_deleting(
        self,
        request: main_models.CheckServiceLinkedRoleForDeletingRequest,
    ) -> main_models.CheckServiceLinkedRoleForDeletingResponse:
        runtime = RuntimeOptions()
        return self.check_service_linked_role_for_deleting_with_options(request, runtime)

    async def check_service_linked_role_for_deleting_async(
        self,
        request: main_models.CheckServiceLinkedRoleForDeletingRequest,
    ) -> main_models.CheckServiceLinkedRoleForDeletingResponse:
        runtime = RuntimeOptions()
        return await self.check_service_linked_role_for_deleting_with_options_async(request, runtime)

    def check_service_status_with_options(
        self,
        request: main_models.CheckServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckServiceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.svc_code):
            query['SvcCode'] = request.svc_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceStatus',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_status_with_options_async(
        self,
        request: main_models.CheckServiceStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckServiceStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.svc_code):
            query['SvcCode'] = request.svc_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceStatus',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_status(
        self,
        request: main_models.CheckServiceStatusRequest,
    ) -> main_models.CheckServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.check_service_status_with_options(request, runtime)

    async def check_service_status_async(
        self,
        request: main_models.CheckServiceStatusRequest,
    ) -> main_models.CheckServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.check_service_status_with_options_async(request, runtime)

    def config_app_with_options(
        self,
        request: main_models.ConfigAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigApp',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_app_with_options_async(
        self,
        request: main_models.ConfigAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_ids):
            query['AppIds'] = request.app_ids
        if not DaraCore.is_null(request.enable):
            query['Enable'] = request.enable
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigApp',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_app(
        self,
        request: main_models.ConfigAppRequest,
    ) -> main_models.ConfigAppResponse:
        runtime = RuntimeOptions()
        return self.config_app_with_options(request, runtime)

    async def config_app_async(
        self,
        request: main_models.ConfigAppRequest,
    ) -> main_models.ConfigAppResponse:
        runtime = RuntimeOptions()
        return await self.config_app_with_options_async(request, runtime)

    def create_alert_contact_with_options(
        self,
        request: main_models.CreateAlertContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlertContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.ding_robot_webhook_url):
            query['DingRobotWebhookUrl'] = request.ding_robot_webhook_url
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.system_noc):
            query['SystemNoc'] = request.system_noc
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlertContact',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alert_contact_with_options_async(
        self,
        request: main_models.CreateAlertContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlertContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.ding_robot_webhook_url):
            query['DingRobotWebhookUrl'] = request.ding_robot_webhook_url
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.system_noc):
            query['SystemNoc'] = request.system_noc
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlertContact',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alert_contact(
        self,
        request: main_models.CreateAlertContactRequest,
    ) -> main_models.CreateAlertContactResponse:
        runtime = RuntimeOptions()
        return self.create_alert_contact_with_options(request, runtime)

    async def create_alert_contact_async(
        self,
        request: main_models.CreateAlertContactRequest,
    ) -> main_models.CreateAlertContactResponse:
        runtime = RuntimeOptions()
        return await self.create_alert_contact_with_options_async(request, runtime)

    def create_alert_contact_group_with_options(
        self,
        request: main_models.CreateAlertContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlertContactGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not DaraCore.is_null(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlertContactGroup',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alert_contact_group_with_options_async(
        self,
        request: main_models.CreateAlertContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlertContactGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not DaraCore.is_null(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlertContactGroup',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alert_contact_group(
        self,
        request: main_models.CreateAlertContactGroupRequest,
    ) -> main_models.CreateAlertContactGroupResponse:
        runtime = RuntimeOptions()
        return self.create_alert_contact_group_with_options(request, runtime)

    async def create_alert_contact_group_async(
        self,
        request: main_models.CreateAlertContactGroupRequest,
    ) -> main_models.CreateAlertContactGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_alert_contact_group_with_options_async(request, runtime)

    def create_alert_template_with_options(
        self,
        request: main_models.CreateAlertTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlertTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.match_expressions):
            query['MatchExpressions'] = request.match_expressions
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule):
            query['Rule'] = request.rule
        if not DaraCore.is_null(request.template_provider):
            query['TemplateProvider'] = request.template_provider
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlertTemplate',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlertTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alert_template_with_options_async(
        self,
        request: main_models.CreateAlertTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAlertTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.match_expressions):
            query['MatchExpressions'] = request.match_expressions
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parent_id):
            query['ParentId'] = request.parent_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule):
            query['Rule'] = request.rule
        if not DaraCore.is_null(request.template_provider):
            query['TemplateProvider'] = request.template_provider
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlertTemplate',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAlertTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alert_template(
        self,
        request: main_models.CreateAlertTemplateRequest,
    ) -> main_models.CreateAlertTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_alert_template_with_options(request, runtime)

    async def create_alert_template_async(
        self,
        request: main_models.CreateAlertTemplateRequest,
    ) -> main_models.CreateAlertTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_alert_template_with_options_async(request, runtime)

    def create_dispatch_rule_with_options(
        self,
        request: main_models.CreateDispatchRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDispatchRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dispatch_rule):
            query['DispatchRule'] = request.dispatch_rule
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDispatchRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dispatch_rule_with_options_async(
        self,
        request: main_models.CreateDispatchRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDispatchRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dispatch_rule):
            query['DispatchRule'] = request.dispatch_rule
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDispatchRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDispatchRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dispatch_rule(
        self,
        request: main_models.CreateDispatchRuleRequest,
    ) -> main_models.CreateDispatchRuleResponse:
        runtime = RuntimeOptions()
        return self.create_dispatch_rule_with_options(request, runtime)

    async def create_dispatch_rule_async(
        self,
        request: main_models.CreateDispatchRuleRequest,
    ) -> main_models.CreateDispatchRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_dispatch_rule_with_options_async(request, runtime)

    def create_prometheus_alert_rule_with_options(
        self,
        request: main_models.CreatePrometheusAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrometheusAlertRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_name):
            query['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.dispatch_rule_id):
            query['DispatchRuleId'] = request.dispatch_rule_id
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrometheusAlertRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prometheus_alert_rule_with_options_async(
        self,
        request: main_models.CreatePrometheusAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrometheusAlertRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_name):
            query['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.dispatch_rule_id):
            query['DispatchRuleId'] = request.dispatch_rule_id
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrometheusAlertRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrometheusAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prometheus_alert_rule(
        self,
        request: main_models.CreatePrometheusAlertRuleRequest,
    ) -> main_models.CreatePrometheusAlertRuleResponse:
        runtime = RuntimeOptions()
        return self.create_prometheus_alert_rule_with_options(request, runtime)

    async def create_prometheus_alert_rule_async(
        self,
        request: main_models.CreatePrometheusAlertRuleRequest,
    ) -> main_models.CreatePrometheusAlertRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_prometheus_alert_rule_with_options_async(request, runtime)

    def create_retcode_app_with_options(
        self,
        request: main_models.CreateRetcodeAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRetcodeAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        if not DaraCore.is_null(request.retcode_app_type):
            query['RetcodeAppType'] = request.retcode_app_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRetcodeApp',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRetcodeAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_retcode_app_with_options_async(
        self,
        request: main_models.CreateRetcodeAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRetcodeAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        if not DaraCore.is_null(request.retcode_app_type):
            query['RetcodeAppType'] = request.retcode_app_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRetcodeApp',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRetcodeAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_retcode_app(
        self,
        request: main_models.CreateRetcodeAppRequest,
    ) -> main_models.CreateRetcodeAppResponse:
        runtime = RuntimeOptions()
        return self.create_retcode_app_with_options(request, runtime)

    async def create_retcode_app_async(
        self,
        request: main_models.CreateRetcodeAppRequest,
    ) -> main_models.CreateRetcodeAppResponse:
        runtime = RuntimeOptions()
        return await self.create_retcode_app_with_options_async(request, runtime)

    def create_wehook_with_options(
        self,
        request: main_models.CreateWehookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWehookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.body):
            query['Body'] = request.body
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.http_headers):
            query['HttpHeaders'] = request.http_headers
        if not DaraCore.is_null(request.http_params):
            query['HttpParams'] = request.http_params
        if not DaraCore.is_null(request.method):
            query['Method'] = request.method
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWehook',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWehookResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_wehook_with_options_async(
        self,
        request: main_models.CreateWehookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWehookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.body):
            query['Body'] = request.body
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.http_headers):
            query['HttpHeaders'] = request.http_headers
        if not DaraCore.is_null(request.http_params):
            query['HttpParams'] = request.http_params
        if not DaraCore.is_null(request.method):
            query['Method'] = request.method
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWehook',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWehookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_wehook(
        self,
        request: main_models.CreateWehookRequest,
    ) -> main_models.CreateWehookResponse:
        runtime = RuntimeOptions()
        return self.create_wehook_with_options(request, runtime)

    async def create_wehook_async(
        self,
        request: main_models.CreateWehookRequest,
    ) -> main_models.CreateWehookResponse:
        runtime = RuntimeOptions()
        return await self.create_wehook_with_options_async(request, runtime)

    def delete_alert_contact_with_options(
        self,
        request: main_models.DeleteAlertContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertContact',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_contact_with_options_async(
        self,
        request: main_models.DeleteAlertContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertContact',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_contact(
        self,
        request: main_models.DeleteAlertContactRequest,
    ) -> main_models.DeleteAlertContactResponse:
        runtime = RuntimeOptions()
        return self.delete_alert_contact_with_options(request, runtime)

    async def delete_alert_contact_async(
        self,
        request: main_models.DeleteAlertContactRequest,
    ) -> main_models.DeleteAlertContactResponse:
        runtime = RuntimeOptions()
        return await self.delete_alert_contact_with_options_async(request, runtime)

    def delete_alert_contact_group_with_options(
        self,
        request: main_models.DeleteAlertContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertContactGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_id):
            query['ContactGroupId'] = request.contact_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertContactGroup',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_contact_group_with_options_async(
        self,
        request: main_models.DeleteAlertContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertContactGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_id):
            query['ContactGroupId'] = request.contact_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertContactGroup',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_contact_group(
        self,
        request: main_models.DeleteAlertContactGroupRequest,
    ) -> main_models.DeleteAlertContactGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_alert_contact_group_with_options(request, runtime)

    async def delete_alert_contact_group_async(
        self,
        request: main_models.DeleteAlertContactGroupRequest,
    ) -> main_models.DeleteAlertContactGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_alert_contact_group_with_options_async(request, runtime)

    def delete_alert_rules_with_options(
        self,
        request: main_models.DeleteAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertRules',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_rules_with_options_async(
        self,
        request: main_models.DeleteAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertRules',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_rules(
        self,
        request: main_models.DeleteAlertRulesRequest,
    ) -> main_models.DeleteAlertRulesResponse:
        runtime = RuntimeOptions()
        return self.delete_alert_rules_with_options(request, runtime)

    async def delete_alert_rules_async(
        self,
        request: main_models.DeleteAlertRulesRequest,
    ) -> main_models.DeleteAlertRulesResponse:
        runtime = RuntimeOptions()
        return await self.delete_alert_rules_with_options_async(request, runtime)

    def delete_alert_template_with_options(
        self,
        request: main_models.DeleteAlertTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertTemplate',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_template_with_options_async(
        self,
        request: main_models.DeleteAlertTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertTemplate',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_template(
        self,
        request: main_models.DeleteAlertTemplateRequest,
    ) -> main_models.DeleteAlertTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_alert_template_with_options(request, runtime)

    async def delete_alert_template_async(
        self,
        request: main_models.DeleteAlertTemplateRequest,
    ) -> main_models.DeleteAlertTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_alert_template_with_options_async(request, runtime)

    def delete_dispatch_rule_with_options(
        self,
        request: main_models.DeleteDispatchRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDispatchRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDispatchRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dispatch_rule_with_options_async(
        self,
        request: main_models.DeleteDispatchRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDispatchRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDispatchRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDispatchRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dispatch_rule(
        self,
        request: main_models.DeleteDispatchRuleRequest,
    ) -> main_models.DeleteDispatchRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_dispatch_rule_with_options(request, runtime)

    async def delete_dispatch_rule_async(
        self,
        request: main_models.DeleteDispatchRuleRequest,
    ) -> main_models.DeleteDispatchRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_dispatch_rule_with_options_async(request, runtime)

    def delete_grafana_resource_with_options(
        self,
        request: main_models.DeleteGrafanaResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGrafanaResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGrafanaResource',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGrafanaResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_grafana_resource_with_options_async(
        self,
        request: main_models.DeleteGrafanaResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGrafanaResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGrafanaResource',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGrafanaResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_grafana_resource(
        self,
        request: main_models.DeleteGrafanaResourceRequest,
    ) -> main_models.DeleteGrafanaResourceResponse:
        runtime = RuntimeOptions()
        return self.delete_grafana_resource_with_options(request, runtime)

    async def delete_grafana_resource_async(
        self,
        request: main_models.DeleteGrafanaResourceRequest,
    ) -> main_models.DeleteGrafanaResourceResponse:
        runtime = RuntimeOptions()
        return await self.delete_grafana_resource_with_options_async(request, runtime)

    def delete_prometheus_alert_rule_with_options(
        self,
        request: main_models.DeletePrometheusAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrometheusAlertRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrometheusAlertRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_prometheus_alert_rule_with_options_async(
        self,
        request: main_models.DeletePrometheusAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrometheusAlertRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrometheusAlertRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrometheusAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_prometheus_alert_rule(
        self,
        request: main_models.DeletePrometheusAlertRuleRequest,
    ) -> main_models.DeletePrometheusAlertRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_prometheus_alert_rule_with_options(request, runtime)

    async def delete_prometheus_alert_rule_async(
        self,
        request: main_models.DeletePrometheusAlertRuleRequest,
    ) -> main_models.DeletePrometheusAlertRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_prometheus_alert_rule_with_options_async(request, runtime)

    def delete_retcode_app_with_options(
        self,
        request: main_models.DeleteRetcodeAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRetcodeAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRetcodeApp',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRetcodeAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_retcode_app_with_options_async(
        self,
        request: main_models.DeleteRetcodeAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRetcodeAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRetcodeApp',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRetcodeAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_retcode_app(
        self,
        request: main_models.DeleteRetcodeAppRequest,
    ) -> main_models.DeleteRetcodeAppResponse:
        runtime = RuntimeOptions()
        return self.delete_retcode_app_with_options(request, runtime)

    async def delete_retcode_app_async(
        self,
        request: main_models.DeleteRetcodeAppRequest,
    ) -> main_models.DeleteRetcodeAppResponse:
        runtime = RuntimeOptions()
        return await self.delete_retcode_app_with_options_async(request, runtime)

    def delete_scenario_with_options(
        self,
        request: main_models.DeleteScenarioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScenarioResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScenario',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scenario_with_options_async(
        self,
        request: main_models.DeleteScenarioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteScenarioResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteScenario',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteScenarioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scenario(
        self,
        request: main_models.DeleteScenarioRequest,
    ) -> main_models.DeleteScenarioResponse:
        runtime = RuntimeOptions()
        return self.delete_scenario_with_options(request, runtime)

    async def delete_scenario_async(
        self,
        request: main_models.DeleteScenarioRequest,
    ) -> main_models.DeleteScenarioResponse:
        runtime = RuntimeOptions()
        return await self.delete_scenario_with_options_async(request, runtime)

    def delete_trace_app_with_options(
        self,
        request: main_models.DeleteTraceAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTraceAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTraceApp',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTraceAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_trace_app_with_options_async(
        self,
        request: main_models.DeleteTraceAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTraceAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTraceApp',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTraceAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_trace_app(
        self,
        request: main_models.DeleteTraceAppRequest,
    ) -> main_models.DeleteTraceAppResponse:
        runtime = RuntimeOptions()
        return self.delete_trace_app_with_options(request, runtime)

    async def delete_trace_app_async(
        self,
        request: main_models.DeleteTraceAppRequest,
    ) -> main_models.DeleteTraceAppResponse:
        runtime = RuntimeOptions()
        return await self.delete_trace_app_with_options_async(request, runtime)

    def describe_dispatch_rule_with_options(
        self,
        request: main_models.DescribeDispatchRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDispatchRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDispatchRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dispatch_rule_with_options_async(
        self,
        request: main_models.DescribeDispatchRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDispatchRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDispatchRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDispatchRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dispatch_rule(
        self,
        request: main_models.DescribeDispatchRuleRequest,
    ) -> main_models.DescribeDispatchRuleResponse:
        runtime = RuntimeOptions()
        return self.describe_dispatch_rule_with_options(request, runtime)

    async def describe_dispatch_rule_async(
        self,
        request: main_models.DescribeDispatchRuleRequest,
    ) -> main_models.DescribeDispatchRuleResponse:
        runtime = RuntimeOptions()
        return await self.describe_dispatch_rule_with_options_async(request, runtime)

    def describe_prometheus_alert_rule_with_options(
        self,
        request: main_models.DescribePrometheusAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePrometheusAlertRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrometheusAlertRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_prometheus_alert_rule_with_options_async(
        self,
        request: main_models.DescribePrometheusAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePrometheusAlertRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrometheusAlertRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePrometheusAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_prometheus_alert_rule(
        self,
        request: main_models.DescribePrometheusAlertRuleRequest,
    ) -> main_models.DescribePrometheusAlertRuleResponse:
        runtime = RuntimeOptions()
        return self.describe_prometheus_alert_rule_with_options(request, runtime)

    async def describe_prometheus_alert_rule_async(
        self,
        request: main_models.DescribePrometheusAlertRuleRequest,
    ) -> main_models.DescribePrometheusAlertRuleResponse:
        runtime = RuntimeOptions()
        return await self.describe_prometheus_alert_rule_with_options_async(request, runtime)

    def describe_trace_license_key_with_options(
        self,
        request: main_models.DescribeTraceLicenseKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTraceLicenseKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTraceLicenseKey',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTraceLicenseKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_trace_license_key_with_options_async(
        self,
        request: main_models.DescribeTraceLicenseKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTraceLicenseKeyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTraceLicenseKey',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTraceLicenseKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_trace_license_key(
        self,
        request: main_models.DescribeTraceLicenseKeyRequest,
    ) -> main_models.DescribeTraceLicenseKeyResponse:
        runtime = RuntimeOptions()
        return self.describe_trace_license_key_with_options(request, runtime)

    async def describe_trace_license_key_async(
        self,
        request: main_models.DescribeTraceLicenseKeyRequest,
    ) -> main_models.DescribeTraceLicenseKeyResponse:
        runtime = RuntimeOptions()
        return await self.describe_trace_license_key_with_options_async(request, runtime)

    def describe_trace_location_with_options(
        self,
        request: main_models.DescribeTraceLocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTraceLocationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTraceLocation',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTraceLocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_trace_location_with_options_async(
        self,
        request: main_models.DescribeTraceLocationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTraceLocationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTraceLocation',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTraceLocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_trace_location(
        self,
        request: main_models.DescribeTraceLocationRequest,
    ) -> main_models.DescribeTraceLocationResponse:
        runtime = RuntimeOptions()
        return self.describe_trace_location_with_options(request, runtime)

    async def describe_trace_location_async(
        self,
        request: main_models.DescribeTraceLocationRequest,
    ) -> main_models.DescribeTraceLocationResponse:
        runtime = RuntimeOptions()
        return await self.describe_trace_location_with_options_async(request, runtime)

    def disable_alert_template_with_options(
        self,
        request: main_models.DisableAlertTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAlertTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableAlertTemplate',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAlertTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_alert_template_with_options_async(
        self,
        request: main_models.DisableAlertTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableAlertTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableAlertTemplate',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableAlertTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_alert_template(
        self,
        request: main_models.DisableAlertTemplateRequest,
    ) -> main_models.DisableAlertTemplateResponse:
        runtime = RuntimeOptions()
        return self.disable_alert_template_with_options(request, runtime)

    async def disable_alert_template_async(
        self,
        request: main_models.DisableAlertTemplateRequest,
    ) -> main_models.DisableAlertTemplateResponse:
        runtime = RuntimeOptions()
        return await self.disable_alert_template_with_options_async(request, runtime)

    def enable_alert_template_with_options(
        self,
        request: main_models.EnableAlertTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAlertTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableAlertTemplate',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAlertTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_alert_template_with_options_async(
        self,
        request: main_models.EnableAlertTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableAlertTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableAlertTemplate',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableAlertTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_alert_template(
        self,
        request: main_models.EnableAlertTemplateRequest,
    ) -> main_models.EnableAlertTemplateResponse:
        runtime = RuntimeOptions()
        return self.enable_alert_template_with_options(request, runtime)

    async def enable_alert_template_async(
        self,
        request: main_models.EnableAlertTemplateRequest,
    ) -> main_models.EnableAlertTemplateResponse:
        runtime = RuntimeOptions()
        return await self.enable_alert_template_with_options_async(request, runtime)

    def export_prometheus_rules_with_options(
        self,
        request: main_models.ExportPrometheusRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportPrometheusRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.name_space):
            query['NameSpace'] = request.name_space
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportPrometheusRules',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportPrometheusRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_prometheus_rules_with_options_async(
        self,
        request: main_models.ExportPrometheusRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExportPrometheusRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.name_space):
            query['NameSpace'] = request.name_space
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExportPrometheusRules',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExportPrometheusRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_prometheus_rules(
        self,
        request: main_models.ExportPrometheusRulesRequest,
    ) -> main_models.ExportPrometheusRulesResponse:
        runtime = RuntimeOptions()
        return self.export_prometheus_rules_with_options(request, runtime)

    async def export_prometheus_rules_async(
        self,
        request: main_models.ExportPrometheusRulesRequest,
    ) -> main_models.ExportPrometheusRulesResponse:
        runtime = RuntimeOptions()
        return await self.export_prometheus_rules_with_options_async(request, runtime)

    def get_agent_download_url_with_options(
        self,
        request: main_models.GetAgentDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentDownloadUrlResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentDownloadUrl',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_download_url_with_options_async(
        self,
        request: main_models.GetAgentDownloadUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentDownloadUrlResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentDownloadUrl',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_download_url(
        self,
        request: main_models.GetAgentDownloadUrlRequest,
    ) -> main_models.GetAgentDownloadUrlResponse:
        runtime = RuntimeOptions()
        return self.get_agent_download_url_with_options(request, runtime)

    async def get_agent_download_url_async(
        self,
        request: main_models.GetAgentDownloadUrlRequest,
    ) -> main_models.GetAgentDownloadUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_agent_download_url_with_options_async(request, runtime)

    def get_app_api_by_page_with_options(
        self,
        request: main_models.GetAppApiByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppApiByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval_mills):
            query['IntervalMills'] = request.interval_mills
        if not DaraCore.is_null(request.pid):
            query['PId'] = request.pid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppApiByPage',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppApiByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_api_by_page_with_options_async(
        self,
        request: main_models.GetAppApiByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppApiByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.interval_mills):
            query['IntervalMills'] = request.interval_mills
        if not DaraCore.is_null(request.pid):
            query['PId'] = request.pid
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppApiByPage',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppApiByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_api_by_page(
        self,
        request: main_models.GetAppApiByPageRequest,
    ) -> main_models.GetAppApiByPageResponse:
        runtime = RuntimeOptions()
        return self.get_app_api_by_page_with_options(request, runtime)

    async def get_app_api_by_page_async(
        self,
        request: main_models.GetAppApiByPageRequest,
    ) -> main_models.GetAppApiByPageResponse:
        runtime = RuntimeOptions()
        return await self.get_app_api_by_page_with_options_async(request, runtime)

    def get_consistency_snapshot_with_options(
        self,
        request: main_models.GetConsistencySnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConsistencySnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.current_timestamp):
            query['CurrentTimestamp'] = request.current_timestamp
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConsistencySnapshot',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsistencySnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consistency_snapshot_with_options_async(
        self,
        request: main_models.GetConsistencySnapshotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConsistencySnapshotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.current_timestamp):
            query['CurrentTimestamp'] = request.current_timestamp
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConsistencySnapshot',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConsistencySnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consistency_snapshot(
        self,
        request: main_models.GetConsistencySnapshotRequest,
    ) -> main_models.GetConsistencySnapshotResponse:
        runtime = RuntimeOptions()
        return self.get_consistency_snapshot_with_options(request, runtime)

    async def get_consistency_snapshot_async(
        self,
        request: main_models.GetConsistencySnapshotRequest,
    ) -> main_models.GetConsistencySnapshotResponse:
        runtime = RuntimeOptions()
        return await self.get_consistency_snapshot_with_options_async(request, runtime)

    def get_integration_token_with_options(
        self,
        request: main_models.GetIntegrationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIntegrationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIntegrationToken',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIntegrationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_integration_token_with_options_async(
        self,
        request: main_models.GetIntegrationTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIntegrationTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetIntegrationToken',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIntegrationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_integration_token(
        self,
        request: main_models.GetIntegrationTokenRequest,
    ) -> main_models.GetIntegrationTokenResponse:
        runtime = RuntimeOptions()
        return self.get_integration_token_with_options(request, runtime)

    async def get_integration_token_async(
        self,
        request: main_models.GetIntegrationTokenRequest,
    ) -> main_models.GetIntegrationTokenResponse:
        runtime = RuntimeOptions()
        return await self.get_integration_token_with_options_async(request, runtime)

    def get_multiple_trace_with_options(
        self,
        request: main_models.GetMultipleTraceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMultipleTraceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.trace_ids):
            query['TraceIDs'] = request.trace_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMultipleTrace',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultipleTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multiple_trace_with_options_async(
        self,
        request: main_models.GetMultipleTraceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMultipleTraceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.trace_ids):
            query['TraceIDs'] = request.trace_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMultipleTrace',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultipleTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multiple_trace(
        self,
        request: main_models.GetMultipleTraceRequest,
    ) -> main_models.GetMultipleTraceResponse:
        runtime = RuntimeOptions()
        return self.get_multiple_trace_with_options(request, runtime)

    async def get_multiple_trace_async(
        self,
        request: main_models.GetMultipleTraceRequest,
    ) -> main_models.GetMultipleTraceResponse:
        runtime = RuntimeOptions()
        return await self.get_multiple_trace_with_options_async(request, runtime)

    def get_prometheus_api_token_with_options(
        self,
        request: main_models.GetPrometheusApiTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPrometheusApiTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrometheusApiToken',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrometheusApiTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_api_token_with_options_async(
        self,
        request: main_models.GetPrometheusApiTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPrometheusApiTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrometheusApiToken',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrometheusApiTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_api_token(
        self,
        request: main_models.GetPrometheusApiTokenRequest,
    ) -> main_models.GetPrometheusApiTokenResponse:
        runtime = RuntimeOptions()
        return self.get_prometheus_api_token_with_options(request, runtime)

    async def get_prometheus_api_token_async(
        self,
        request: main_models.GetPrometheusApiTokenRequest,
    ) -> main_models.GetPrometheusApiTokenResponse:
        runtime = RuntimeOptions()
        return await self.get_prometheus_api_token_with_options_async(request, runtime)

    def get_retcode_share_url_with_options(
        self,
        request: main_models.GetRetcodeShareUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRetcodeShareUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRetcodeShareUrl',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRetcodeShareUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_retcode_share_url_with_options_async(
        self,
        request: main_models.GetRetcodeShareUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRetcodeShareUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRetcodeShareUrl',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRetcodeShareUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_retcode_share_url(
        self,
        request: main_models.GetRetcodeShareUrlRequest,
    ) -> main_models.GetRetcodeShareUrlResponse:
        runtime = RuntimeOptions()
        return self.get_retcode_share_url_with_options(request, runtime)

    async def get_retcode_share_url_async(
        self,
        request: main_models.GetRetcodeShareUrlRequest,
    ) -> main_models.GetRetcodeShareUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_retcode_share_url_with_options_async(request, runtime)

    def get_stack_with_options(
        self,
        request: main_models.GetStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rpc_id):
            query['RpcID'] = request.rpc_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStack',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_with_options_async(
        self,
        request: main_models.GetStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rpc_id):
            query['RpcID'] = request.rpc_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStack',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack(
        self,
        request: main_models.GetStackRequest,
    ) -> main_models.GetStackResponse:
        runtime = RuntimeOptions()
        return self.get_stack_with_options(request, runtime)

    async def get_stack_async(
        self,
        request: main_models.GetStackRequest,
    ) -> main_models.GetStackResponse:
        runtime = RuntimeOptions()
        return await self.get_stack_with_options_async(request, runtime)

    def get_trace_with_options(
        self,
        request: main_models.GetTraceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTraceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrace',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trace_with_options_async(
        self,
        request: main_models.GetTraceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTraceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrace',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trace(
        self,
        request: main_models.GetTraceRequest,
    ) -> main_models.GetTraceResponse:
        runtime = RuntimeOptions()
        return self.get_trace_with_options(request, runtime)

    async def get_trace_async(
        self,
        request: main_models.GetTraceRequest,
    ) -> main_models.GetTraceResponse:
        runtime = RuntimeOptions()
        return await self.get_trace_with_options_async(request, runtime)

    def get_trace_app_with_options(
        self,
        request: main_models.GetTraceAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTraceAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTraceApp',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTraceAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trace_app_with_options_async(
        self,
        request: main_models.GetTraceAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTraceAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTraceApp',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTraceAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trace_app(
        self,
        request: main_models.GetTraceAppRequest,
    ) -> main_models.GetTraceAppResponse:
        runtime = RuntimeOptions()
        return self.get_trace_app_with_options(request, runtime)

    async def get_trace_app_async(
        self,
        request: main_models.GetTraceAppRequest,
    ) -> main_models.GetTraceAppResponse:
        runtime = RuntimeOptions()
        return await self.get_trace_app_with_options_async(request, runtime)

    def import_app_alert_rules_with_options(
        self,
        request: main_models.ImportAppAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportAppAlertRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not DaraCore.is_null(request.is_auto_start):
            query['IsAutoStart'] = request.is_auto_start
        if not DaraCore.is_null(request.pids):
            query['Pids'] = request.pids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        if not DaraCore.is_null(request.template_alert_id):
            query['TemplateAlertId'] = request.template_alert_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportAppAlertRules',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportAppAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_app_alert_rules_with_options_async(
        self,
        request: main_models.ImportAppAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportAppAlertRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not DaraCore.is_null(request.is_auto_start):
            query['IsAutoStart'] = request.is_auto_start
        if not DaraCore.is_null(request.pids):
            query['Pids'] = request.pids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        if not DaraCore.is_null(request.template_alert_id):
            query['TemplateAlertId'] = request.template_alert_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportAppAlertRules',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportAppAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_app_alert_rules(
        self,
        request: main_models.ImportAppAlertRulesRequest,
    ) -> main_models.ImportAppAlertRulesResponse:
        runtime = RuntimeOptions()
        return self.import_app_alert_rules_with_options(request, runtime)

    async def import_app_alert_rules_async(
        self,
        request: main_models.ImportAppAlertRulesRequest,
    ) -> main_models.ImportAppAlertRulesResponse:
        runtime = RuntimeOptions()
        return await self.import_app_alert_rules_with_options_async(request, runtime)

    def import_custom_alert_rules_with_options(
        self,
        request: main_models.ImportCustomAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportCustomAlertRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not DaraCore.is_null(request.is_auto_start):
            query['IsAutoStart'] = request.is_auto_start
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        if not DaraCore.is_null(request.template_alert_config):
            query['TemplateAlertConfig'] = request.template_alert_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportCustomAlertRules',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportCustomAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_custom_alert_rules_with_options_async(
        self,
        request: main_models.ImportCustomAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportCustomAlertRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not DaraCore.is_null(request.is_auto_start):
            query['IsAutoStart'] = request.is_auto_start
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        if not DaraCore.is_null(request.template_alert_config):
            query['TemplateAlertConfig'] = request.template_alert_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportCustomAlertRules',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportCustomAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_custom_alert_rules(
        self,
        request: main_models.ImportCustomAlertRulesRequest,
    ) -> main_models.ImportCustomAlertRulesResponse:
        runtime = RuntimeOptions()
        return self.import_custom_alert_rules_with_options(request, runtime)

    async def import_custom_alert_rules_async(
        self,
        request: main_models.ImportCustomAlertRulesRequest,
    ) -> main_models.ImportCustomAlertRulesResponse:
        runtime = RuntimeOptions()
        return await self.import_custom_alert_rules_with_options_async(request, runtime)

    def import_prometheus_rules_with_options(
        self,
        request: main_models.ImportPrometheusRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportPrometheusRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.name_space):
            query['NameSpace'] = request.name_space
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportPrometheusRules',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportPrometheusRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_prometheus_rules_with_options_async(
        self,
        request: main_models.ImportPrometheusRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportPrometheusRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.name_space):
            query['NameSpace'] = request.name_space
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportPrometheusRules',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportPrometheusRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_prometheus_rules(
        self,
        request: main_models.ImportPrometheusRulesRequest,
    ) -> main_models.ImportPrometheusRulesResponse:
        runtime = RuntimeOptions()
        return self.import_prometheus_rules_with_options(request, runtime)

    async def import_prometheus_rules_async(
        self,
        request: main_models.ImportPrometheusRulesRequest,
    ) -> main_models.ImportPrometheusRulesResponse:
        runtime = RuntimeOptions()
        return await self.import_prometheus_rules_with_options_async(request, runtime)

    def list_activated_alerts_with_options(
        self,
        request: main_models.ListActivatedAlertsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListActivatedAlertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListActivatedAlerts',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListActivatedAlertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_activated_alerts_with_options_async(
        self,
        request: main_models.ListActivatedAlertsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListActivatedAlertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListActivatedAlerts',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListActivatedAlertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_activated_alerts(
        self,
        request: main_models.ListActivatedAlertsRequest,
    ) -> main_models.ListActivatedAlertsResponse:
        runtime = RuntimeOptions()
        return self.list_activated_alerts_with_options(request, runtime)

    async def list_activated_alerts_async(
        self,
        request: main_models.ListActivatedAlertsRequest,
    ) -> main_models.ListActivatedAlertsResponse:
        runtime = RuntimeOptions()
        return await self.list_activated_alerts_with_options_async(request, runtime)

    def list_alert_templates_with_options(
        self,
        request: main_models.ListAlertTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_provider):
            query['AlertProvider'] = request.alert_provider
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.template_provider):
            query['TemplateProvider'] = request.template_provider
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlertTemplates',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alert_templates_with_options_async(
        self,
        request: main_models.ListAlertTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_provider):
            query['AlertProvider'] = request.alert_provider
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.template_provider):
            query['TemplateProvider'] = request.template_provider
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlertTemplates',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alert_templates(
        self,
        request: main_models.ListAlertTemplatesRequest,
    ) -> main_models.ListAlertTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_alert_templates_with_options(request, runtime)

    async def list_alert_templates_async(
        self,
        request: main_models.ListAlertTemplatesRequest,
    ) -> main_models.ListAlertTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_alert_templates_with_options_async(request, runtime)

    def list_cluster_from_grafana_with_options(
        self,
        request: main_models.ListClusterFromGrafanaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterFromGrafanaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterFromGrafana',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterFromGrafanaResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_from_grafana_with_options_async(
        self,
        request: main_models.ListClusterFromGrafanaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListClusterFromGrafanaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListClusterFromGrafana',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListClusterFromGrafanaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_from_grafana(
        self,
        request: main_models.ListClusterFromGrafanaRequest,
    ) -> main_models.ListClusterFromGrafanaResponse:
        runtime = RuntimeOptions()
        return self.list_cluster_from_grafana_with_options(request, runtime)

    async def list_cluster_from_grafana_async(
        self,
        request: main_models.ListClusterFromGrafanaRequest,
    ) -> main_models.ListClusterFromGrafanaResponse:
        runtime = RuntimeOptions()
        return await self.list_cluster_from_grafana_with_options_async(request, runtime)

    def list_dashboards_with_options(
        self,
        request: main_models.ListDashboardsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDashboardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.recreate_switch):
            query['RecreateSwitch'] = request.recreate_switch
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDashboards',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDashboardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dashboards_with_options_async(
        self,
        request: main_models.ListDashboardsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDashboardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.recreate_switch):
            query['RecreateSwitch'] = request.recreate_switch
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDashboards',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDashboardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dashboards(
        self,
        request: main_models.ListDashboardsRequest,
    ) -> main_models.ListDashboardsResponse:
        runtime = RuntimeOptions()
        return self.list_dashboards_with_options(request, runtime)

    async def list_dashboards_async(
        self,
        request: main_models.ListDashboardsRequest,
    ) -> main_models.ListDashboardsResponse:
        runtime = RuntimeOptions()
        return await self.list_dashboards_with_options_async(request, runtime)

    def list_dispatch_rule_with_options(
        self,
        request: main_models.ListDispatchRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDispatchRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.system):
            query['System'] = request.system
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDispatchRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dispatch_rule_with_options_async(
        self,
        request: main_models.ListDispatchRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDispatchRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.system):
            query['System'] = request.system
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDispatchRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDispatchRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dispatch_rule(
        self,
        request: main_models.ListDispatchRuleRequest,
    ) -> main_models.ListDispatchRuleResponse:
        runtime = RuntimeOptions()
        return self.list_dispatch_rule_with_options(request, runtime)

    async def list_dispatch_rule_async(
        self,
        request: main_models.ListDispatchRuleRequest,
    ) -> main_models.ListDispatchRuleResponse:
        runtime = RuntimeOptions()
        return await self.list_dispatch_rule_with_options_async(request, runtime)

    def list_prom_clusters_with_options(
        self,
        request: main_models.ListPromClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPromClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPromClusters',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPromClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prom_clusters_with_options_async(
        self,
        request: main_models.ListPromClustersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPromClustersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPromClusters',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPromClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prom_clusters(
        self,
        request: main_models.ListPromClustersRequest,
    ) -> main_models.ListPromClustersResponse:
        runtime = RuntimeOptions()
        return self.list_prom_clusters_with_options(request, runtime)

    async def list_prom_clusters_async(
        self,
        request: main_models.ListPromClustersRequest,
    ) -> main_models.ListPromClustersResponse:
        runtime = RuntimeOptions()
        return await self.list_prom_clusters_with_options_async(request, runtime)

    def list_prometheus_alert_rules_with_options(
        self,
        request: main_models.ListPrometheusAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusAlertRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.match_expressions):
            query['MatchExpressions'] = request.match_expressions
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusAlertRules',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_alert_rules_with_options_async(
        self,
        request: main_models.ListPrometheusAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusAlertRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.match_expressions):
            query['MatchExpressions'] = request.match_expressions
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusAlertRules',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_alert_rules(
        self,
        request: main_models.ListPrometheusAlertRulesRequest,
    ) -> main_models.ListPrometheusAlertRulesResponse:
        runtime = RuntimeOptions()
        return self.list_prometheus_alert_rules_with_options(request, runtime)

    async def list_prometheus_alert_rules_async(
        self,
        request: main_models.ListPrometheusAlertRulesRequest,
    ) -> main_models.ListPrometheusAlertRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_prometheus_alert_rules_with_options_async(request, runtime)

    def list_prometheus_alert_templates_with_options(
        self,
        request: main_models.ListPrometheusAlertTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusAlertTemplatesResponse:
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
            action = 'ListPrometheusAlertTemplates',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusAlertTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_alert_templates_with_options_async(
        self,
        request: main_models.ListPrometheusAlertTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusAlertTemplatesResponse:
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
            action = 'ListPrometheusAlertTemplates',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusAlertTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_alert_templates(
        self,
        request: main_models.ListPrometheusAlertTemplatesRequest,
    ) -> main_models.ListPrometheusAlertTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_prometheus_alert_templates_with_options(request, runtime)

    async def list_prometheus_alert_templates_async(
        self,
        request: main_models.ListPrometheusAlertTemplatesRequest,
    ) -> main_models.ListPrometheusAlertTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_prometheus_alert_templates_with_options_async(request, runtime)

    def list_retcode_apps_with_options(
        self,
        request: main_models.ListRetcodeAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRetcodeAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRetcodeApps',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRetcodeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_retcode_apps_with_options_async(
        self,
        request: main_models.ListRetcodeAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRetcodeAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRetcodeApps',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRetcodeAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_retcode_apps(
        self,
        request: main_models.ListRetcodeAppsRequest,
    ) -> main_models.ListRetcodeAppsResponse:
        runtime = RuntimeOptions()
        return self.list_retcode_apps_with_options(request, runtime)

    async def list_retcode_apps_async(
        self,
        request: main_models.ListRetcodeAppsRequest,
    ) -> main_models.ListRetcodeAppsResponse:
        runtime = RuntimeOptions()
        return await self.list_retcode_apps_with_options_async(request, runtime)

    def list_scenario_with_options(
        self,
        request: main_models.ListScenarioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScenarioResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scenario):
            query['Scenario'] = request.scenario
        if not DaraCore.is_null(request.sign):
            query['Sign'] = request.sign
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScenario',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scenario_with_options_async(
        self,
        request: main_models.ListScenarioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListScenarioResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scenario):
            query['Scenario'] = request.scenario
        if not DaraCore.is_null(request.sign):
            query['Sign'] = request.sign
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListScenario',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListScenarioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scenario(
        self,
        request: main_models.ListScenarioRequest,
    ) -> main_models.ListScenarioResponse:
        runtime = RuntimeOptions()
        return self.list_scenario_with_options(request, runtime)

    async def list_scenario_async(
        self,
        request: main_models.ListScenarioRequest,
    ) -> main_models.ListScenarioResponse:
        runtime = RuntimeOptions()
        return await self.list_scenario_with_options_async(request, runtime)

    def list_serverless_top_napps_with_options(
        self,
        request: main_models.ListServerlessTopNAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServerlessTopNAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServerlessTopNApps',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServerlessTopNAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_serverless_top_napps_with_options_async(
        self,
        request: main_models.ListServerlessTopNAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServerlessTopNAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServerlessTopNApps',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServerlessTopNAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_serverless_top_napps(
        self,
        request: main_models.ListServerlessTopNAppsRequest,
    ) -> main_models.ListServerlessTopNAppsResponse:
        runtime = RuntimeOptions()
        return self.list_serverless_top_napps_with_options(request, runtime)

    async def list_serverless_top_napps_async(
        self,
        request: main_models.ListServerlessTopNAppsRequest,
    ) -> main_models.ListServerlessTopNAppsResponse:
        runtime = RuntimeOptions()
        return await self.list_serverless_top_napps_with_options_async(request, runtime)

    def list_trace_apps_with_options(
        self,
        request: main_models.ListTraceAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTraceAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTraceApps',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTraceAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_trace_apps_with_options_async(
        self,
        request: main_models.ListTraceAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTraceAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTraceApps',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTraceAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_trace_apps(
        self,
        request: main_models.ListTraceAppsRequest,
    ) -> main_models.ListTraceAppsResponse:
        runtime = RuntimeOptions()
        return self.list_trace_apps_with_options(request, runtime)

    async def list_trace_apps_async(
        self,
        request: main_models.ListTraceAppsRequest,
    ) -> main_models.ListTraceAppsResponse:
        runtime = RuntimeOptions()
        return await self.list_trace_apps_with_options_async(request, runtime)

    def open_arms_default_slrwith_options(
        self,
        request: main_models.OpenArmsDefaultSLRRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenArmsDefaultSLRResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenArmsDefaultSLR',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenArmsDefaultSLRResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_arms_default_slrwith_options_async(
        self,
        request: main_models.OpenArmsDefaultSLRRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenArmsDefaultSLRResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenArmsDefaultSLR',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenArmsDefaultSLRResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_arms_default_slr(
        self,
        request: main_models.OpenArmsDefaultSLRRequest,
    ) -> main_models.OpenArmsDefaultSLRResponse:
        runtime = RuntimeOptions()
        return self.open_arms_default_slrwith_options(request, runtime)

    async def open_arms_default_slr_async(
        self,
        request: main_models.OpenArmsDefaultSLRRequest,
    ) -> main_models.OpenArmsDefaultSLRResponse:
        runtime = RuntimeOptions()
        return await self.open_arms_default_slrwith_options_async(request, runtime)

    def open_arms_service_with_options(
        self,
        request: main_models.OpenArmsServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenArmsServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenArmsService',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenArmsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_arms_service_with_options_async(
        self,
        request: main_models.OpenArmsServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenArmsServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenArmsService',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenArmsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_arms_service(
        self,
        request: main_models.OpenArmsServiceRequest,
    ) -> main_models.OpenArmsServiceResponse:
        runtime = RuntimeOptions()
        return self.open_arms_service_with_options(request, runtime)

    async def open_arms_service_async(
        self,
        request: main_models.OpenArmsServiceRequest,
    ) -> main_models.OpenArmsServiceResponse:
        runtime = RuntimeOptions()
        return await self.open_arms_service_with_options_async(request, runtime)

    def open_vcluster_with_options(
        self,
        request: main_models.OpenVClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenVClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.recreate_switch):
            query['RecreateSwitch'] = request.recreate_switch
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenVCluster',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenVClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_vcluster_with_options_async(
        self,
        request: main_models.OpenVClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenVClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.recreate_switch):
            query['RecreateSwitch'] = request.recreate_switch
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenVCluster',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenVClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_vcluster(
        self,
        request: main_models.OpenVClusterRequest,
    ) -> main_models.OpenVClusterResponse:
        runtime = RuntimeOptions()
        return self.open_vcluster_with_options(request, runtime)

    async def open_vcluster_async(
        self,
        request: main_models.OpenVClusterRequest,
    ) -> main_models.OpenVClusterResponse:
        runtime = RuntimeOptions()
        return await self.open_vcluster_with_options_async(request, runtime)

    def open_xtrace_default_slrwith_options(
        self,
        request: main_models.OpenXtraceDefaultSLRRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenXtraceDefaultSLRResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenXtraceDefaultSLR',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenXtraceDefaultSLRResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_xtrace_default_slrwith_options_async(
        self,
        request: main_models.OpenXtraceDefaultSLRRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenXtraceDefaultSLRResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenXtraceDefaultSLR',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenXtraceDefaultSLRResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_xtrace_default_slr(
        self,
        request: main_models.OpenXtraceDefaultSLRRequest,
    ) -> main_models.OpenXtraceDefaultSLRResponse:
        runtime = RuntimeOptions()
        return self.open_xtrace_default_slrwith_options(request, runtime)

    async def open_xtrace_default_slr_async(
        self,
        request: main_models.OpenXtraceDefaultSLRRequest,
    ) -> main_models.OpenXtraceDefaultSLRResponse:
        runtime = RuntimeOptions()
        return await self.open_xtrace_default_slrwith_options_async(request, runtime)

    def query_dataset_with_options(
        self,
        request: main_models.QueryDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.date_str):
            query['DateStr'] = request.date_str
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.hungry_mode):
            query['HungryMode'] = request.hungry_mode
        if not DaraCore.is_null(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not DaraCore.is_null(request.is_drill_down):
            query['IsDrillDown'] = request.is_drill_down
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.max_time):
            query['MaxTime'] = request.max_time
        if not DaraCore.is_null(request.measures):
            query['Measures'] = request.measures
        if not DaraCore.is_null(request.min_time):
            query['MinTime'] = request.min_time
        if not DaraCore.is_null(request.optional_dims):
            query['OptionalDims'] = request.optional_dims
        if not DaraCore.is_null(request.order_by_key):
            query['OrderByKey'] = request.order_by_key
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.reduce_tail):
            query['ReduceTail'] = request.reduce_tail
        if not DaraCore.is_null(request.required_dims):
            query['RequiredDims'] = request.required_dims
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDataset',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dataset_with_options_async(
        self,
        request: main_models.QueryDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.date_str):
            query['DateStr'] = request.date_str
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.hungry_mode):
            query['HungryMode'] = request.hungry_mode
        if not DaraCore.is_null(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not DaraCore.is_null(request.is_drill_down):
            query['IsDrillDown'] = request.is_drill_down
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.max_time):
            query['MaxTime'] = request.max_time
        if not DaraCore.is_null(request.measures):
            query['Measures'] = request.measures
        if not DaraCore.is_null(request.min_time):
            query['MinTime'] = request.min_time
        if not DaraCore.is_null(request.optional_dims):
            query['OptionalDims'] = request.optional_dims
        if not DaraCore.is_null(request.order_by_key):
            query['OrderByKey'] = request.order_by_key
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.reduce_tail):
            query['ReduceTail'] = request.reduce_tail
        if not DaraCore.is_null(request.required_dims):
            query['RequiredDims'] = request.required_dims
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryDataset',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dataset(
        self,
        request: main_models.QueryDatasetRequest,
    ) -> main_models.QueryDatasetResponse:
        runtime = RuntimeOptions()
        return self.query_dataset_with_options(request, runtime)

    async def query_dataset_async(
        self,
        request: main_models.QueryDatasetRequest,
    ) -> main_models.QueryDatasetResponse:
        runtime = RuntimeOptions()
        return await self.query_dataset_with_options_async(request, runtime)

    def query_metric_with_options(
        self,
        request: main_models.QueryMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consistency_data_key):
            query['ConsistencyDataKey'] = request.consistency_data_key
        if not DaraCore.is_null(request.consistency_query_strategy):
            query['ConsistencyQueryStrategy'] = request.consistency_query_strategy
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.measures):
            query['Measures'] = request.measures
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMetric',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_metric_with_options_async(
        self,
        request: main_models.QueryMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.consistency_data_key):
            query['ConsistencyDataKey'] = request.consistency_data_key
        if not DaraCore.is_null(request.consistency_query_strategy):
            query['ConsistencyQueryStrategy'] = request.consistency_query_strategy
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not DaraCore.is_null(request.limit):
            query['Limit'] = request.limit
        if not DaraCore.is_null(request.measures):
            query['Measures'] = request.measures
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMetric',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_metric(
        self,
        request: main_models.QueryMetricRequest,
    ) -> main_models.QueryMetricResponse:
        runtime = RuntimeOptions()
        return self.query_metric_with_options(request, runtime)

    async def query_metric_async(
        self,
        request: main_models.QueryMetricRequest,
    ) -> main_models.QueryMetricResponse:
        runtime = RuntimeOptions()
        return await self.query_metric_with_options_async(request, runtime)

    def query_metric_by_page_with_options(
        self,
        request: main_models.QueryMetricByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMetricByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.custom_filters):
            query['CustomFilters'] = request.custom_filters
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not DaraCore.is_null(request.measures):
            query['Measures'] = request.measures
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMetricByPage',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMetricByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_metric_by_page_with_options_async(
        self,
        request: main_models.QueryMetricByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryMetricByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.custom_filters):
            query['CustomFilters'] = request.custom_filters
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not DaraCore.is_null(request.measures):
            query['Measures'] = request.measures
        if not DaraCore.is_null(request.metric):
            query['Metric'] = request.metric
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryMetricByPage',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryMetricByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_metric_by_page(
        self,
        request: main_models.QueryMetricByPageRequest,
    ) -> main_models.QueryMetricByPageResponse:
        runtime = RuntimeOptions()
        return self.query_metric_by_page_with_options(request, runtime)

    async def query_metric_by_page_async(
        self,
        request: main_models.QueryMetricByPageRequest,
    ) -> main_models.QueryMetricByPageResponse:
        runtime = RuntimeOptions()
        return await self.query_metric_by_page_with_options_async(request, runtime)

    def save_trace_app_config_with_options(
        self,
        request: main_models.SaveTraceAppConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTraceAppConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.settings):
            query['Settings'] = request.settings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTraceAppConfig',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTraceAppConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_trace_app_config_with_options_async(
        self,
        request: main_models.SaveTraceAppConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SaveTraceAppConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.settings):
            query['Settings'] = request.settings
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SaveTraceAppConfig',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SaveTraceAppConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_trace_app_config(
        self,
        request: main_models.SaveTraceAppConfigRequest,
    ) -> main_models.SaveTraceAppConfigResponse:
        runtime = RuntimeOptions()
        return self.save_trace_app_config_with_options(request, runtime)

    async def save_trace_app_config_async(
        self,
        request: main_models.SaveTraceAppConfigRequest,
    ) -> main_models.SaveTraceAppConfigResponse:
        runtime = RuntimeOptions()
        return await self.save_trace_app_config_with_options_async(request, runtime)

    def search_alert_contact_with_options(
        self,
        request: main_models.SearchAlertContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchAlertContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchAlertContact',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_alert_contact_with_options_async(
        self,
        request: main_models.SearchAlertContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchAlertContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchAlertContact',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_alert_contact(
        self,
        request: main_models.SearchAlertContactRequest,
    ) -> main_models.SearchAlertContactResponse:
        runtime = RuntimeOptions()
        return self.search_alert_contact_with_options(request, runtime)

    async def search_alert_contact_async(
        self,
        request: main_models.SearchAlertContactRequest,
    ) -> main_models.SearchAlertContactResponse:
        runtime = RuntimeOptions()
        return await self.search_alert_contact_with_options_async(request, runtime)

    def search_alert_contact_group_with_options(
        self,
        request: main_models.SearchAlertContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchAlertContactGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not DaraCore.is_null(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchAlertContactGroup',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_alert_contact_group_with_options_async(
        self,
        request: main_models.SearchAlertContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchAlertContactGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not DaraCore.is_null(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchAlertContactGroup',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_alert_contact_group(
        self,
        request: main_models.SearchAlertContactGroupRequest,
    ) -> main_models.SearchAlertContactGroupResponse:
        runtime = RuntimeOptions()
        return self.search_alert_contact_group_with_options(request, runtime)

    async def search_alert_contact_group_async(
        self,
        request: main_models.SearchAlertContactGroupRequest,
    ) -> main_models.SearchAlertContactGroupResponse:
        runtime = RuntimeOptions()
        return await self.search_alert_contact_group_with_options_async(request, runtime)

    def search_alert_histories_with_options(
        self,
        request: main_models.SearchAlertHistoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchAlertHistoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        if not DaraCore.is_null(request.alert_type):
            query['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchAlertHistories',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchAlertHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_alert_histories_with_options_async(
        self,
        request: main_models.SearchAlertHistoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchAlertHistoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        if not DaraCore.is_null(request.alert_type):
            query['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchAlertHistories',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchAlertHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_alert_histories(
        self,
        request: main_models.SearchAlertHistoriesRequest,
    ) -> main_models.SearchAlertHistoriesResponse:
        runtime = RuntimeOptions()
        return self.search_alert_histories_with_options(request, runtime)

    async def search_alert_histories_async(
        self,
        request: main_models.SearchAlertHistoriesRequest,
    ) -> main_models.SearchAlertHistoriesResponse:
        runtime = RuntimeOptions()
        return await self.search_alert_histories_with_options_async(request, runtime)

    def search_alert_rules_with_options(
        self,
        request: main_models.SearchAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchAlertRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchAlertRules',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_alert_rules_with_options_async(
        self,
        request: main_models.SearchAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchAlertRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchAlertRules',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_alert_rules(
        self,
        request: main_models.SearchAlertRulesRequest,
    ) -> main_models.SearchAlertRulesResponse:
        runtime = RuntimeOptions()
        return self.search_alert_rules_with_options(request, runtime)

    async def search_alert_rules_async(
        self,
        request: main_models.SearchAlertRulesRequest,
    ) -> main_models.SearchAlertRulesResponse:
        runtime = RuntimeOptions()
        return await self.search_alert_rules_with_options_async(request, runtime)

    def search_events_with_options(
        self,
        request: main_models.SearchEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        if not DaraCore.is_null(request.alert_type):
            query['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.is_trigger):
            query['IsTrigger'] = request.is_trigger
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchEvents',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_events_with_options_async(
        self,
        request: main_models.SearchEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        if not DaraCore.is_null(request.alert_type):
            query['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.is_trigger):
            query['IsTrigger'] = request.is_trigger
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchEvents',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_events(
        self,
        request: main_models.SearchEventsRequest,
    ) -> main_models.SearchEventsResponse:
        runtime = RuntimeOptions()
        return self.search_events_with_options(request, runtime)

    async def search_events_async(
        self,
        request: main_models.SearchEventsRequest,
    ) -> main_models.SearchEventsResponse:
        runtime = RuntimeOptions()
        return await self.search_events_with_options_async(request, runtime)

    def search_retcode_app_by_page_with_options(
        self,
        request: main_models.SearchRetcodeAppByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchRetcodeAppByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchRetcodeAppByPage',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchRetcodeAppByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_retcode_app_by_page_with_options_async(
        self,
        request: main_models.SearchRetcodeAppByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchRetcodeAppByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchRetcodeAppByPage',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchRetcodeAppByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_retcode_app_by_page(
        self,
        request: main_models.SearchRetcodeAppByPageRequest,
    ) -> main_models.SearchRetcodeAppByPageResponse:
        runtime = RuntimeOptions()
        return self.search_retcode_app_by_page_with_options(request, runtime)

    async def search_retcode_app_by_page_async(
        self,
        request: main_models.SearchRetcodeAppByPageRequest,
    ) -> main_models.SearchRetcodeAppByPageResponse:
        runtime = RuntimeOptions()
        return await self.search_retcode_app_by_page_with_options_async(request, runtime)

    def search_trace_app_by_name_with_options(
        self,
        request: main_models.SearchTraceAppByNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchTraceAppByNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.trace_app_name):
            query['TraceAppName'] = request.trace_app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTraceAppByName',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchTraceAppByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_trace_app_by_name_with_options_async(
        self,
        request: main_models.SearchTraceAppByNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchTraceAppByNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.trace_app_name):
            query['TraceAppName'] = request.trace_app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTraceAppByName',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchTraceAppByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_trace_app_by_name(
        self,
        request: main_models.SearchTraceAppByNameRequest,
    ) -> main_models.SearchTraceAppByNameResponse:
        runtime = RuntimeOptions()
        return self.search_trace_app_by_name_with_options(request, runtime)

    async def search_trace_app_by_name_async(
        self,
        request: main_models.SearchTraceAppByNameRequest,
    ) -> main_models.SearchTraceAppByNameResponse:
        runtime = RuntimeOptions()
        return await self.search_trace_app_by_name_with_options_async(request, runtime)

    def search_trace_app_by_page_with_options(
        self,
        request: main_models.SearchTraceAppByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchTraceAppByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.trace_app_name):
            query['TraceAppName'] = request.trace_app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTraceAppByPage',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchTraceAppByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_trace_app_by_page_with_options_async(
        self,
        request: main_models.SearchTraceAppByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchTraceAppByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.trace_app_name):
            query['TraceAppName'] = request.trace_app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTraceAppByPage',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchTraceAppByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_trace_app_by_page(
        self,
        request: main_models.SearchTraceAppByPageRequest,
    ) -> main_models.SearchTraceAppByPageResponse:
        runtime = RuntimeOptions()
        return self.search_trace_app_by_page_with_options(request, runtime)

    async def search_trace_app_by_page_async(
        self,
        request: main_models.SearchTraceAppByPageRequest,
    ) -> main_models.SearchTraceAppByPageResponse:
        runtime = RuntimeOptions()
        return await self.search_trace_app_by_page_with_options_async(request, runtime)

    def search_traces_with_options(
        self,
        request: main_models.SearchTracesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchTracesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.exclusion_filters):
            query['ExclusionFilters'] = request.exclusion_filters
        if not DaraCore.is_null(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not DaraCore.is_null(request.operation_name):
            query['OperationName'] = request.operation_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        if not DaraCore.is_null(request.service_ip):
            query['ServiceIp'] = request.service_ip
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTraces',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchTracesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_traces_with_options_async(
        self,
        request: main_models.SearchTracesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchTracesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.exclusion_filters):
            query['ExclusionFilters'] = request.exclusion_filters
        if not DaraCore.is_null(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not DaraCore.is_null(request.operation_name):
            query['OperationName'] = request.operation_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        if not DaraCore.is_null(request.service_ip):
            query['ServiceIp'] = request.service_ip
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTraces',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchTracesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_traces(
        self,
        request: main_models.SearchTracesRequest,
    ) -> main_models.SearchTracesResponse:
        runtime = RuntimeOptions()
        return self.search_traces_with_options(request, runtime)

    async def search_traces_async(
        self,
        request: main_models.SearchTracesRequest,
    ) -> main_models.SearchTracesResponse:
        runtime = RuntimeOptions()
        return await self.search_traces_with_options_async(request, runtime)

    def search_traces_by_page_with_options(
        self,
        request: main_models.SearchTracesByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchTracesByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.exclusion_filters):
            query['ExclusionFilters'] = request.exclusion_filters
        if not DaraCore.is_null(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not DaraCore.is_null(request.operation_name):
            query['OperationName'] = request.operation_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        if not DaraCore.is_null(request.service_ip):
            query['ServiceIp'] = request.service_ip
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTracesByPage',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchTracesByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_traces_by_page_with_options_async(
        self,
        request: main_models.SearchTracesByPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchTracesByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.exclusion_filters):
            query['ExclusionFilters'] = request.exclusion_filters
        if not DaraCore.is_null(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not DaraCore.is_null(request.operation_name):
            query['OperationName'] = request.operation_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.reverse):
            query['Reverse'] = request.reverse
        if not DaraCore.is_null(request.service_ip):
            query['ServiceIp'] = request.service_ip
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTracesByPage',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchTracesByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_traces_by_page(
        self,
        request: main_models.SearchTracesByPageRequest,
    ) -> main_models.SearchTracesByPageResponse:
        runtime = RuntimeOptions()
        return self.search_traces_by_page_with_options(request, runtime)

    async def search_traces_by_page_async(
        self,
        request: main_models.SearchTracesByPageRequest,
    ) -> main_models.SearchTracesByPageResponse:
        runtime = RuntimeOptions()
        return await self.search_traces_by_page_with_options_async(request, runtime)

    def send_custom_incidents_with_options(
        self,
        request: main_models.SendCustomIncidentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendCustomIncidentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.incidents):
            query['Incidents'] = request.incidents
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendCustomIncidents',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendCustomIncidentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_custom_incidents_with_options_async(
        self,
        request: main_models.SendCustomIncidentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendCustomIncidentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.incidents):
            query['Incidents'] = request.incidents
        if not DaraCore.is_null(request.product_type):
            query['ProductType'] = request.product_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendCustomIncidents',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendCustomIncidentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_custom_incidents(
        self,
        request: main_models.SendCustomIncidentsRequest,
    ) -> main_models.SendCustomIncidentsResponse:
        runtime = RuntimeOptions()
        return self.send_custom_incidents_with_options(request, runtime)

    async def send_custom_incidents_async(
        self,
        request: main_models.SendCustomIncidentsRequest,
    ) -> main_models.SendCustomIncidentsResponse:
        runtime = RuntimeOptions()
        return await self.send_custom_incidents_with_options_async(request, runtime)

    def send_mse_incident_with_options(
        self,
        request: main_models.SendMseIncidentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendMseIncidentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.incidents):
            query['Incidents'] = request.incidents
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendMseIncident',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendMseIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_mse_incident_with_options_async(
        self,
        request: main_models.SendMseIncidentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendMseIncidentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.incidents):
            query['Incidents'] = request.incidents
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendMseIncident',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendMseIncidentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_mse_incident(
        self,
        request: main_models.SendMseIncidentRequest,
    ) -> main_models.SendMseIncidentResponse:
        runtime = RuntimeOptions()
        return self.send_mse_incident_with_options(request, runtime)

    async def send_mse_incident_async(
        self,
        request: main_models.SendMseIncidentRequest,
    ) -> main_models.SendMseIncidentResponse:
        runtime = RuntimeOptions()
        return await self.send_mse_incident_with_options_async(request, runtime)

    def set_retcode_share_status_with_options(
        self,
        request: main_models.SetRetcodeShareStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetRetcodeShareStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetRetcodeShareStatus',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetRetcodeShareStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_retcode_share_status_with_options_async(
        self,
        request: main_models.SetRetcodeShareStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetRetcodeShareStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetRetcodeShareStatus',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetRetcodeShareStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_retcode_share_status(
        self,
        request: main_models.SetRetcodeShareStatusRequest,
    ) -> main_models.SetRetcodeShareStatusResponse:
        runtime = RuntimeOptions()
        return self.set_retcode_share_status_with_options(request, runtime)

    async def set_retcode_share_status_async(
        self,
        request: main_models.SetRetcodeShareStatusRequest,
    ) -> main_models.SetRetcodeShareStatusResponse:
        runtime = RuntimeOptions()
        return await self.set_retcode_share_status_with_options_async(request, runtime)

    def start_alert_with_options(
        self,
        request: main_models.StartAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartAlert',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_alert_with_options_async(
        self,
        request: main_models.StartAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartAlert',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_alert(
        self,
        request: main_models.StartAlertRequest,
    ) -> main_models.StartAlertResponse:
        runtime = RuntimeOptions()
        return self.start_alert_with_options(request, runtime)

    async def start_alert_async(
        self,
        request: main_models.StartAlertRequest,
    ) -> main_models.StartAlertResponse:
        runtime = RuntimeOptions()
        return await self.start_alert_with_options_async(request, runtime)

    def stop_alert_with_options(
        self,
        request: main_models.StopAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopAlert',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_alert_with_options_async(
        self,
        request: main_models.StopAlertRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopAlertResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopAlert',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_alert(
        self,
        request: main_models.StopAlertRequest,
    ) -> main_models.StopAlertResponse:
        runtime = RuntimeOptions()
        return self.stop_alert_with_options(request, runtime)

    async def stop_alert_async(
        self,
        request: main_models.StopAlertRequest,
    ) -> main_models.StopAlertResponse:
        runtime = RuntimeOptions()
        return await self.stop_alert_with_options_async(request, runtime)

    def update_alert_contact_with_options(
        self,
        request: main_models.UpdateAlertContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.ding_robot_webhook_url):
            query['DingRobotWebhookUrl'] = request.ding_robot_webhook_url
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.system_noc):
            query['SystemNoc'] = request.system_noc
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlertContact',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alert_contact_with_options_async(
        self,
        request: main_models.UpdateAlertContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.ding_robot_webhook_url):
            query['DingRobotWebhookUrl'] = request.ding_robot_webhook_url
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.system_noc):
            query['SystemNoc'] = request.system_noc
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlertContact',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alert_contact(
        self,
        request: main_models.UpdateAlertContactRequest,
    ) -> main_models.UpdateAlertContactResponse:
        runtime = RuntimeOptions()
        return self.update_alert_contact_with_options(request, runtime)

    async def update_alert_contact_async(
        self,
        request: main_models.UpdateAlertContactRequest,
    ) -> main_models.UpdateAlertContactResponse:
        runtime = RuntimeOptions()
        return await self.update_alert_contact_with_options_async(request, runtime)

    def update_alert_contact_group_with_options(
        self,
        request: main_models.UpdateAlertContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertContactGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_id):
            query['ContactGroupId'] = request.contact_group_id
        if not DaraCore.is_null(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not DaraCore.is_null(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlertContactGroup',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alert_contact_group_with_options_async(
        self,
        request: main_models.UpdateAlertContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertContactGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_id):
            query['ContactGroupId'] = request.contact_group_id
        if not DaraCore.is_null(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not DaraCore.is_null(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlertContactGroup',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alert_contact_group(
        self,
        request: main_models.UpdateAlertContactGroupRequest,
    ) -> main_models.UpdateAlertContactGroupResponse:
        runtime = RuntimeOptions()
        return self.update_alert_contact_group_with_options(request, runtime)

    async def update_alert_contact_group_async(
        self,
        request: main_models.UpdateAlertContactGroupRequest,
    ) -> main_models.UpdateAlertContactGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_alert_contact_group_with_options_async(request, runtime)

    def update_alert_rule_with_options(
        self,
        request: main_models.UpdateAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        if not DaraCore.is_null(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not DaraCore.is_null(request.is_auto_start):
            query['IsAutoStart'] = request.is_auto_start
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlertRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alert_rule_with_options_async(
        self,
        request: main_models.UpdateAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        if not DaraCore.is_null(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not DaraCore.is_null(request.is_auto_start):
            query['IsAutoStart'] = request.is_auto_start
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlertRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alert_rule(
        self,
        request: main_models.UpdateAlertRuleRequest,
    ) -> main_models.UpdateAlertRuleResponse:
        runtime = RuntimeOptions()
        return self.update_alert_rule_with_options(request, runtime)

    async def update_alert_rule_async(
        self,
        request: main_models.UpdateAlertRuleRequest,
    ) -> main_models.UpdateAlertRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_alert_rule_with_options_async(request, runtime)

    def update_alert_template_with_options(
        self,
        request: main_models.UpdateAlertTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.match_expressions):
            query['MatchExpressions'] = request.match_expressions
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule):
            query['Rule'] = request.rule
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlertTemplate',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alert_template_with_options_async(
        self,
        request: main_models.UpdateAlertTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAlertTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.match_expressions):
            query['MatchExpressions'] = request.match_expressions
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule):
            query['Rule'] = request.rule
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAlertTemplate',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAlertTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alert_template(
        self,
        request: main_models.UpdateAlertTemplateRequest,
    ) -> main_models.UpdateAlertTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_alert_template_with_options(request, runtime)

    async def update_alert_template_async(
        self,
        request: main_models.UpdateAlertTemplateRequest,
    ) -> main_models.UpdateAlertTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_alert_template_with_options_async(request, runtime)

    def update_dispatch_rule_with_options(
        self,
        request: main_models.UpdateDispatchRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDispatchRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dispatch_rule):
            query['DispatchRule'] = request.dispatch_rule
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDispatchRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dispatch_rule_with_options_async(
        self,
        request: main_models.UpdateDispatchRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDispatchRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dispatch_rule):
            query['DispatchRule'] = request.dispatch_rule
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDispatchRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDispatchRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dispatch_rule(
        self,
        request: main_models.UpdateDispatchRuleRequest,
    ) -> main_models.UpdateDispatchRuleResponse:
        runtime = RuntimeOptions()
        return self.update_dispatch_rule_with_options(request, runtime)

    async def update_dispatch_rule_async(
        self,
        request: main_models.UpdateDispatchRuleRequest,
    ) -> main_models.UpdateDispatchRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_dispatch_rule_with_options_async(request, runtime)

    def update_prometheus_alert_rule_with_options(
        self,
        request: main_models.UpdatePrometheusAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusAlertRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        if not DaraCore.is_null(request.alert_name):
            query['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.dispatch_rule_id):
            query['DispatchRuleId'] = request.dispatch_rule_id
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusAlertRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_alert_rule_with_options_async(
        self,
        request: main_models.UpdatePrometheusAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusAlertRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        if not DaraCore.is_null(request.alert_name):
            query['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.annotations):
            query['Annotations'] = request.annotations
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.dispatch_rule_id):
            query['DispatchRuleId'] = request.dispatch_rule_id
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.message):
            query['Message'] = request.message
        if not DaraCore.is_null(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusAlertRule',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_alert_rule(
        self,
        request: main_models.UpdatePrometheusAlertRuleRequest,
    ) -> main_models.UpdatePrometheusAlertRuleResponse:
        runtime = RuntimeOptions()
        return self.update_prometheus_alert_rule_with_options(request, runtime)

    async def update_prometheus_alert_rule_async(
        self,
        request: main_models.UpdatePrometheusAlertRuleRequest,
    ) -> main_models.UpdatePrometheusAlertRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_prometheus_alert_rule_with_options_async(request, runtime)

    def update_webhook_with_options(
        self,
        request: main_models.UpdateWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWebhookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.body):
            query['Body'] = request.body
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.http_headers):
            query['HttpHeaders'] = request.http_headers
        if not DaraCore.is_null(request.http_params):
            query['HttpParams'] = request.http_params
        if not DaraCore.is_null(request.method):
            query['Method'] = request.method
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWebhook',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_webhook_with_options_async(
        self,
        request: main_models.UpdateWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateWebhookResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.body):
            query['Body'] = request.body
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.http_headers):
            query['HttpHeaders'] = request.http_headers
        if not DaraCore.is_null(request.http_params):
            query['HttpParams'] = request.http_params
        if not DaraCore.is_null(request.method):
            query['Method'] = request.method
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWebhook',
            version = '2021-04-22',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_webhook(
        self,
        request: main_models.UpdateWebhookRequest,
    ) -> main_models.UpdateWebhookResponse:
        runtime = RuntimeOptions()
        return self.update_webhook_with_options(request, runtime)

    async def update_webhook_async(
        self,
        request: main_models.UpdateWebhookRequest,
    ) -> main_models.UpdateWebhookResponse:
        runtime = RuntimeOptions()
        return await self.update_webhook_with_options_async(request, runtime)
