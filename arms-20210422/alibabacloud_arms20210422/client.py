# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_arms20210422 import models as arms20210422_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_grafana_with_options(
        self,
        request: arms20210422_models.AddGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.AddGrafanaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.integration):
            query['Integration'] = request.integration
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGrafana',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.AddGrafanaResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_grafana_with_options_async(
        self,
        request: arms20210422_models.AddGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.AddGrafanaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.integration):
            query['Integration'] = request.integration
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGrafana',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.AddGrafanaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_grafana(
        self,
        request: arms20210422_models.AddGrafanaRequest,
    ) -> arms20210422_models.AddGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_grafana_with_options(request, runtime)

    async def add_grafana_async(
        self,
        request: arms20210422_models.AddGrafanaRequest,
    ) -> arms20210422_models.AddGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_grafana_with_options_async(request, runtime)

    def add_integration_with_options(
        self,
        request: arms20210422_models.AddIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.AddIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.integration):
            query['Integration'] = request.integration
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddIntegration',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.AddIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_integration_with_options_async(
        self,
        request: arms20210422_models.AddIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.AddIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.integration):
            query['Integration'] = request.integration
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddIntegration',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.AddIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_integration(
        self,
        request: arms20210422_models.AddIntegrationRequest,
    ) -> arms20210422_models.AddIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_integration_with_options(request, runtime)

    async def add_integration_async(
        self,
        request: arms20210422_models.AddIntegrationRequest,
    ) -> arms20210422_models.AddIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_integration_with_options_async(request, runtime)

    def apply_scenario_with_options(
        self,
        tmp_req: arms20210422_models.ApplyScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ApplyScenarioResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20210422_models.ApplyScenarioShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.config_shrink):
            query['Config'] = request.config_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scenario):
            query['Scenario'] = request.scenario
        if not UtilClient.is_unset(request.sign):
            query['Sign'] = request.sign
        if not UtilClient.is_unset(request.sn_dump):
            query['SnDump'] = request.sn_dump
        if not UtilClient.is_unset(request.sn_force):
            query['SnForce'] = request.sn_force
        if not UtilClient.is_unset(request.sn_stat):
            query['SnStat'] = request.sn_stat
        if not UtilClient.is_unset(request.sn_transfer):
            query['SnTransfer'] = request.sn_transfer
        if not UtilClient.is_unset(request.update_option):
            query['UpdateOption'] = request.update_option
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyScenario',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ApplyScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_scenario_with_options_async(
        self,
        tmp_req: arms20210422_models.ApplyScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ApplyScenarioResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20210422_models.ApplyScenarioShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.config_shrink):
            query['Config'] = request.config_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scenario):
            query['Scenario'] = request.scenario
        if not UtilClient.is_unset(request.sign):
            query['Sign'] = request.sign
        if not UtilClient.is_unset(request.sn_dump):
            query['SnDump'] = request.sn_dump
        if not UtilClient.is_unset(request.sn_force):
            query['SnForce'] = request.sn_force
        if not UtilClient.is_unset(request.sn_stat):
            query['SnStat'] = request.sn_stat
        if not UtilClient.is_unset(request.sn_transfer):
            query['SnTransfer'] = request.sn_transfer
        if not UtilClient.is_unset(request.update_option):
            query['UpdateOption'] = request.update_option
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyScenario',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ApplyScenarioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_scenario(
        self,
        request: arms20210422_models.ApplyScenarioRequest,
    ) -> arms20210422_models.ApplyScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_scenario_with_options(request, runtime)

    async def apply_scenario_async(
        self,
        request: arms20210422_models.ApplyScenarioRequest,
    ) -> arms20210422_models.ApplyScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_scenario_with_options_async(request, runtime)

    def check_data_consistency_with_options(
        self,
        request: arms20210422_models.CheckDataConsistencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CheckDataConsistencyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.current_timestamp):
            query['CurrentTimestamp'] = request.current_timestamp
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDataConsistency',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CheckDataConsistencyResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_data_consistency_with_options_async(
        self,
        request: arms20210422_models.CheckDataConsistencyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CheckDataConsistencyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.current_timestamp):
            query['CurrentTimestamp'] = request.current_timestamp
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDataConsistency',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CheckDataConsistencyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_data_consistency(
        self,
        request: arms20210422_models.CheckDataConsistencyRequest,
    ) -> arms20210422_models.CheckDataConsistencyResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_data_consistency_with_options(request, runtime)

    async def check_data_consistency_async(
        self,
        request: arms20210422_models.CheckDataConsistencyRequest,
    ) -> arms20210422_models.CheckDataConsistencyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_data_consistency_with_options_async(request, runtime)

    def check_service_linked_role_for_deleting_with_options(
        self,
        request: arms20210422_models.CheckServiceLinkedRoleForDeletingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CheckServiceLinkedRoleForDeletingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.spiregion_id):
            query['SPIRegionId'] = request.spiregion_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRoleForDeleting',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CheckServiceLinkedRoleForDeletingResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_linked_role_for_deleting_with_options_async(
        self,
        request: arms20210422_models.CheckServiceLinkedRoleForDeletingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CheckServiceLinkedRoleForDeletingResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.spiregion_id):
            query['SPIRegionId'] = request.spiregion_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRoleForDeleting',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CheckServiceLinkedRoleForDeletingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_linked_role_for_deleting(
        self,
        request: arms20210422_models.CheckServiceLinkedRoleForDeletingRequest,
    ) -> arms20210422_models.CheckServiceLinkedRoleForDeletingResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_for_deleting_with_options(request, runtime)

    async def check_service_linked_role_for_deleting_async(
        self,
        request: arms20210422_models.CheckServiceLinkedRoleForDeletingRequest,
    ) -> arms20210422_models.CheckServiceLinkedRoleForDeletingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_service_linked_role_for_deleting_with_options_async(request, runtime)

    def check_service_status_with_options(
        self,
        request: arms20210422_models.CheckServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CheckServiceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.svc_code):
            query['SvcCode'] = request.svc_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceStatus',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CheckServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_status_with_options_async(
        self,
        request: arms20210422_models.CheckServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CheckServiceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.svc_code):
            query['SvcCode'] = request.svc_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceStatus',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CheckServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_status(
        self,
        request: arms20210422_models.CheckServiceStatusRequest,
    ) -> arms20210422_models.CheckServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_service_status_with_options(request, runtime)

    async def check_service_status_async(
        self,
        request: arms20210422_models.CheckServiceStatusRequest,
    ) -> arms20210422_models.CheckServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_service_status_with_options_async(request, runtime)

    def config_app_with_options(
        self,
        request: arms20210422_models.ConfigAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ConfigAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigApp',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ConfigAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_app_with_options_async(
        self,
        request: arms20210422_models.ConfigAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ConfigAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigApp',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ConfigAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_app(
        self,
        request: arms20210422_models.ConfigAppRequest,
    ) -> arms20210422_models.ConfigAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_app_with_options(request, runtime)

    async def config_app_async(
        self,
        request: arms20210422_models.ConfigAppRequest,
    ) -> arms20210422_models.ConfigAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_app_with_options_async(request, runtime)

    def create_alert_contact_with_options(
        self,
        request: arms20210422_models.CreateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CreateAlertContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.ding_robot_webhook_url):
            query['DingRobotWebhookUrl'] = request.ding_robot_webhook_url
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.system_noc):
            query['SystemNoc'] = request.system_noc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlertContact',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alert_contact_with_options_async(
        self,
        request: arms20210422_models.CreateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CreateAlertContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.ding_robot_webhook_url):
            query['DingRobotWebhookUrl'] = request.ding_robot_webhook_url
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.system_noc):
            query['SystemNoc'] = request.system_noc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlertContact',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alert_contact(
        self,
        request: arms20210422_models.CreateAlertContactRequest,
    ) -> arms20210422_models.CreateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_alert_contact_with_options(request, runtime)

    async def create_alert_contact_async(
        self,
        request: arms20210422_models.CreateAlertContactRequest,
    ) -> arms20210422_models.CreateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_alert_contact_with_options_async(request, runtime)

    def create_alert_contact_group_with_options(
        self,
        request: arms20210422_models.CreateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CreateAlertContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlertContactGroup',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alert_contact_group_with_options_async(
        self,
        request: arms20210422_models.CreateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CreateAlertContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlertContactGroup',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alert_contact_group(
        self,
        request: arms20210422_models.CreateAlertContactGroupRequest,
    ) -> arms20210422_models.CreateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_alert_contact_group_with_options(request, runtime)

    async def create_alert_contact_group_async(
        self,
        request: arms20210422_models.CreateAlertContactGroupRequest,
    ) -> arms20210422_models.CreateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_alert_contact_group_with_options_async(request, runtime)

    def create_alert_template_with_options(
        self,
        request: arms20210422_models.CreateAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CreateAlertTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.match_expressions):
            query['MatchExpressions'] = request.match_expressions
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.template_provider):
            query['TemplateProvider'] = request.template_provider
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlertTemplate',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateAlertTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alert_template_with_options_async(
        self,
        request: arms20210422_models.CreateAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CreateAlertTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.match_expressions):
            query['MatchExpressions'] = request.match_expressions
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.template_provider):
            query['TemplateProvider'] = request.template_provider
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlertTemplate',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateAlertTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alert_template(
        self,
        request: arms20210422_models.CreateAlertTemplateRequest,
    ) -> arms20210422_models.CreateAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_alert_template_with_options(request, runtime)

    async def create_alert_template_async(
        self,
        request: arms20210422_models.CreateAlertTemplateRequest,
    ) -> arms20210422_models.CreateAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_alert_template_with_options_async(request, runtime)

    def create_dispatch_rule_with_options(
        self,
        request: arms20210422_models.CreateDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CreateDispatchRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dispatch_rule):
            query['DispatchRule'] = request.dispatch_rule
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDispatchRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dispatch_rule_with_options_async(
        self,
        request: arms20210422_models.CreateDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CreateDispatchRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dispatch_rule):
            query['DispatchRule'] = request.dispatch_rule
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDispatchRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateDispatchRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dispatch_rule(
        self,
        request: arms20210422_models.CreateDispatchRuleRequest,
    ) -> arms20210422_models.CreateDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dispatch_rule_with_options(request, runtime)

    async def create_dispatch_rule_async(
        self,
        request: arms20210422_models.CreateDispatchRuleRequest,
    ) -> arms20210422_models.CreateDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dispatch_rule_with_options_async(request, runtime)

    def create_prometheus_alert_rule_with_options(
        self,
        request: arms20210422_models.CreatePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CreatePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_name):
            query['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.dispatch_rule_id):
            query['DispatchRuleId'] = request.dispatch_rule_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePrometheusAlertRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreatePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prometheus_alert_rule_with_options_async(
        self,
        request: arms20210422_models.CreatePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CreatePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_name):
            query['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.dispatch_rule_id):
            query['DispatchRuleId'] = request.dispatch_rule_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePrometheusAlertRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreatePrometheusAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prometheus_alert_rule(
        self,
        request: arms20210422_models.CreatePrometheusAlertRuleRequest,
    ) -> arms20210422_models.CreatePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_prometheus_alert_rule_with_options(request, runtime)

    async def create_prometheus_alert_rule_async(
        self,
        request: arms20210422_models.CreatePrometheusAlertRuleRequest,
    ) -> arms20210422_models.CreatePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_prometheus_alert_rule_with_options_async(request, runtime)

    def create_retcode_app_with_options(
        self,
        request: arms20210422_models.CreateRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CreateRetcodeAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        if not UtilClient.is_unset(request.retcode_app_type):
            query['RetcodeAppType'] = request.retcode_app_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRetcodeApp',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateRetcodeAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_retcode_app_with_options_async(
        self,
        request: arms20210422_models.CreateRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CreateRetcodeAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        if not UtilClient.is_unset(request.retcode_app_type):
            query['RetcodeAppType'] = request.retcode_app_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRetcodeApp',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateRetcodeAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_retcode_app(
        self,
        request: arms20210422_models.CreateRetcodeAppRequest,
    ) -> arms20210422_models.CreateRetcodeAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_retcode_app_with_options(request, runtime)

    async def create_retcode_app_async(
        self,
        request: arms20210422_models.CreateRetcodeAppRequest,
    ) -> arms20210422_models.CreateRetcodeAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_retcode_app_with_options_async(request, runtime)

    def create_wehook_with_options(
        self,
        request: arms20210422_models.CreateWehookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CreateWehookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.http_headers):
            query['HttpHeaders'] = request.http_headers
        if not UtilClient.is_unset(request.http_params):
            query['HttpParams'] = request.http_params
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWehook',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateWehookResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_wehook_with_options_async(
        self,
        request: arms20210422_models.CreateWehookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.CreateWehookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.http_headers):
            query['HttpHeaders'] = request.http_headers
        if not UtilClient.is_unset(request.http_params):
            query['HttpParams'] = request.http_params
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWehook',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateWehookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_wehook(
        self,
        request: arms20210422_models.CreateWehookRequest,
    ) -> arms20210422_models.CreateWehookResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_wehook_with_options(request, runtime)

    async def create_wehook_async(
        self,
        request: arms20210422_models.CreateWehookRequest,
    ) -> arms20210422_models.CreateWehookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_wehook_with_options_async(request, runtime)

    def delete_alert_contact_with_options(
        self,
        request: arms20210422_models.DeleteAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteAlertContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlertContact',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_contact_with_options_async(
        self,
        request: arms20210422_models.DeleteAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteAlertContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlertContact',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_contact(
        self,
        request: arms20210422_models.DeleteAlertContactRequest,
    ) -> arms20210422_models.DeleteAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_with_options(request, runtime)

    async def delete_alert_contact_async(
        self,
        request: arms20210422_models.DeleteAlertContactRequest,
    ) -> arms20210422_models.DeleteAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_contact_with_options_async(request, runtime)

    def delete_alert_contact_group_with_options(
        self,
        request: arms20210422_models.DeleteAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteAlertContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_id):
            query['ContactGroupId'] = request.contact_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlertContactGroup',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_contact_group_with_options_async(
        self,
        request: arms20210422_models.DeleteAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteAlertContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_id):
            query['ContactGroupId'] = request.contact_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlertContactGroup',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_contact_group(
        self,
        request: arms20210422_models.DeleteAlertContactGroupRequest,
    ) -> arms20210422_models.DeleteAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_group_with_options(request, runtime)

    async def delete_alert_contact_group_async(
        self,
        request: arms20210422_models.DeleteAlertContactGroupRequest,
    ) -> arms20210422_models.DeleteAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_contact_group_with_options_async(request, runtime)

    def delete_alert_rules_with_options(
        self,
        request: arms20210422_models.DeleteAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteAlertRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlertRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_rules_with_options_async(
        self,
        request: arms20210422_models.DeleteAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteAlertRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlertRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_rules(
        self,
        request: arms20210422_models.DeleteAlertRulesRequest,
    ) -> arms20210422_models.DeleteAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_rules_with_options(request, runtime)

    async def delete_alert_rules_async(
        self,
        request: arms20210422_models.DeleteAlertRulesRequest,
    ) -> arms20210422_models.DeleteAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_rules_with_options_async(request, runtime)

    def delete_alert_template_with_options(
        self,
        request: arms20210422_models.DeleteAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteAlertTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlertTemplate',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteAlertTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_template_with_options_async(
        self,
        request: arms20210422_models.DeleteAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteAlertTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlertTemplate',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteAlertTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_template(
        self,
        request: arms20210422_models.DeleteAlertTemplateRequest,
    ) -> arms20210422_models.DeleteAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_template_with_options(request, runtime)

    async def delete_alert_template_async(
        self,
        request: arms20210422_models.DeleteAlertTemplateRequest,
    ) -> arms20210422_models.DeleteAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_template_with_options_async(request, runtime)

    def delete_dispatch_rule_with_options(
        self,
        request: arms20210422_models.DeleteDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteDispatchRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDispatchRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dispatch_rule_with_options_async(
        self,
        request: arms20210422_models.DeleteDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteDispatchRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDispatchRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteDispatchRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dispatch_rule(
        self,
        request: arms20210422_models.DeleteDispatchRuleRequest,
    ) -> arms20210422_models.DeleteDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dispatch_rule_with_options(request, runtime)

    async def delete_dispatch_rule_async(
        self,
        request: arms20210422_models.DeleteDispatchRuleRequest,
    ) -> arms20210422_models.DeleteDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dispatch_rule_with_options_async(request, runtime)

    def delete_grafana_resource_with_options(
        self,
        request: arms20210422_models.DeleteGrafanaResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteGrafanaResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGrafanaResource',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteGrafanaResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_grafana_resource_with_options_async(
        self,
        request: arms20210422_models.DeleteGrafanaResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteGrafanaResourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGrafanaResource',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteGrafanaResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_grafana_resource(
        self,
        request: arms20210422_models.DeleteGrafanaResourceRequest,
    ) -> arms20210422_models.DeleteGrafanaResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_grafana_resource_with_options(request, runtime)

    async def delete_grafana_resource_async(
        self,
        request: arms20210422_models.DeleteGrafanaResourceRequest,
    ) -> arms20210422_models.DeleteGrafanaResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_grafana_resource_with_options_async(request, runtime)

    def delete_prometheus_alert_rule_with_options(
        self,
        request: arms20210422_models.DeletePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeletePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusAlertRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeletePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_prometheus_alert_rule_with_options_async(
        self,
        request: arms20210422_models.DeletePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeletePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusAlertRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeletePrometheusAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_prometheus_alert_rule(
        self,
        request: arms20210422_models.DeletePrometheusAlertRuleRequest,
    ) -> arms20210422_models.DeletePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_prometheus_alert_rule_with_options(request, runtime)

    async def delete_prometheus_alert_rule_async(
        self,
        request: arms20210422_models.DeletePrometheusAlertRuleRequest,
    ) -> arms20210422_models.DeletePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_prometheus_alert_rule_with_options_async(request, runtime)

    def delete_retcode_app_with_options(
        self,
        request: arms20210422_models.DeleteRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteRetcodeAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRetcodeApp',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteRetcodeAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_retcode_app_with_options_async(
        self,
        request: arms20210422_models.DeleteRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteRetcodeAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRetcodeApp',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteRetcodeAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_retcode_app(
        self,
        request: arms20210422_models.DeleteRetcodeAppRequest,
    ) -> arms20210422_models.DeleteRetcodeAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_retcode_app_with_options(request, runtime)

    async def delete_retcode_app_async(
        self,
        request: arms20210422_models.DeleteRetcodeAppRequest,
    ) -> arms20210422_models.DeleteRetcodeAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_retcode_app_with_options_async(request, runtime)

    def delete_scenario_with_options(
        self,
        request: arms20210422_models.DeleteScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteScenarioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScenario',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scenario_with_options_async(
        self,
        request: arms20210422_models.DeleteScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteScenarioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScenario',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteScenarioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scenario(
        self,
        request: arms20210422_models.DeleteScenarioRequest,
    ) -> arms20210422_models.DeleteScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scenario_with_options(request, runtime)

    async def delete_scenario_async(
        self,
        request: arms20210422_models.DeleteScenarioRequest,
    ) -> arms20210422_models.DeleteScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scenario_with_options_async(request, runtime)

    def delete_trace_app_with_options(
        self,
        request: arms20210422_models.DeleteTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteTraceAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTraceApp',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteTraceAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_trace_app_with_options_async(
        self,
        request: arms20210422_models.DeleteTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DeleteTraceAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTraceApp',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteTraceAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_trace_app(
        self,
        request: arms20210422_models.DeleteTraceAppRequest,
    ) -> arms20210422_models.DeleteTraceAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_trace_app_with_options(request, runtime)

    async def delete_trace_app_async(
        self,
        request: arms20210422_models.DeleteTraceAppRequest,
    ) -> arms20210422_models.DeleteTraceAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_trace_app_with_options_async(request, runtime)

    def describe_dispatch_rule_with_options(
        self,
        request: arms20210422_models.DescribeDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DescribeDispatchRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDispatchRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DescribeDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dispatch_rule_with_options_async(
        self,
        request: arms20210422_models.DescribeDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DescribeDispatchRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDispatchRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DescribeDispatchRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dispatch_rule(
        self,
        request: arms20210422_models.DescribeDispatchRuleRequest,
    ) -> arms20210422_models.DescribeDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dispatch_rule_with_options(request, runtime)

    async def describe_dispatch_rule_async(
        self,
        request: arms20210422_models.DescribeDispatchRuleRequest,
    ) -> arms20210422_models.DescribeDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dispatch_rule_with_options_async(request, runtime)

    def describe_prometheus_alert_rule_with_options(
        self,
        request: arms20210422_models.DescribePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DescribePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrometheusAlertRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DescribePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_prometheus_alert_rule_with_options_async(
        self,
        request: arms20210422_models.DescribePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DescribePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrometheusAlertRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DescribePrometheusAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_prometheus_alert_rule(
        self,
        request: arms20210422_models.DescribePrometheusAlertRuleRequest,
    ) -> arms20210422_models.DescribePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_prometheus_alert_rule_with_options(request, runtime)

    async def describe_prometheus_alert_rule_async(
        self,
        request: arms20210422_models.DescribePrometheusAlertRuleRequest,
    ) -> arms20210422_models.DescribePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_prometheus_alert_rule_with_options_async(request, runtime)

    def describe_trace_license_key_with_options(
        self,
        request: arms20210422_models.DescribeTraceLicenseKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DescribeTraceLicenseKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTraceLicenseKey',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DescribeTraceLicenseKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_trace_license_key_with_options_async(
        self,
        request: arms20210422_models.DescribeTraceLicenseKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DescribeTraceLicenseKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTraceLicenseKey',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DescribeTraceLicenseKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_trace_license_key(
        self,
        request: arms20210422_models.DescribeTraceLicenseKeyRequest,
    ) -> arms20210422_models.DescribeTraceLicenseKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_trace_license_key_with_options(request, runtime)

    async def describe_trace_license_key_async(
        self,
        request: arms20210422_models.DescribeTraceLicenseKeyRequest,
    ) -> arms20210422_models.DescribeTraceLicenseKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_trace_license_key_with_options_async(request, runtime)

    def describe_trace_location_with_options(
        self,
        request: arms20210422_models.DescribeTraceLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DescribeTraceLocationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTraceLocation',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DescribeTraceLocationResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_trace_location_with_options_async(
        self,
        request: arms20210422_models.DescribeTraceLocationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DescribeTraceLocationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTraceLocation',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DescribeTraceLocationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_trace_location(
        self,
        request: arms20210422_models.DescribeTraceLocationRequest,
    ) -> arms20210422_models.DescribeTraceLocationResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_trace_location_with_options(request, runtime)

    async def describe_trace_location_async(
        self,
        request: arms20210422_models.DescribeTraceLocationRequest,
    ) -> arms20210422_models.DescribeTraceLocationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_trace_location_with_options_async(request, runtime)

    def disable_alert_template_with_options(
        self,
        request: arms20210422_models.DisableAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DisableAlertTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAlertTemplate',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DisableAlertTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_alert_template_with_options_async(
        self,
        request: arms20210422_models.DisableAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.DisableAlertTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAlertTemplate',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DisableAlertTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_alert_template(
        self,
        request: arms20210422_models.DisableAlertTemplateRequest,
    ) -> arms20210422_models.DisableAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_alert_template_with_options(request, runtime)

    async def disable_alert_template_async(
        self,
        request: arms20210422_models.DisableAlertTemplateRequest,
    ) -> arms20210422_models.DisableAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_alert_template_with_options_async(request, runtime)

    def enable_alert_template_with_options(
        self,
        request: arms20210422_models.EnableAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.EnableAlertTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAlertTemplate',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.EnableAlertTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_alert_template_with_options_async(
        self,
        request: arms20210422_models.EnableAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.EnableAlertTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAlertTemplate',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.EnableAlertTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_alert_template(
        self,
        request: arms20210422_models.EnableAlertTemplateRequest,
    ) -> arms20210422_models.EnableAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_alert_template_with_options(request, runtime)

    async def enable_alert_template_async(
        self,
        request: arms20210422_models.EnableAlertTemplateRequest,
    ) -> arms20210422_models.EnableAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_alert_template_with_options_async(request, runtime)

    def export_prometheus_rules_with_options(
        self,
        request: arms20210422_models.ExportPrometheusRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ExportPrometheusRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.name_space):
            query['NameSpace'] = request.name_space
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportPrometheusRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ExportPrometheusRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def export_prometheus_rules_with_options_async(
        self,
        request: arms20210422_models.ExportPrometheusRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ExportPrometheusRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.name_space):
            query['NameSpace'] = request.name_space
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportPrometheusRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ExportPrometheusRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def export_prometheus_rules(
        self,
        request: arms20210422_models.ExportPrometheusRulesRequest,
    ) -> arms20210422_models.ExportPrometheusRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.export_prometheus_rules_with_options(request, runtime)

    async def export_prometheus_rules_async(
        self,
        request: arms20210422_models.ExportPrometheusRulesRequest,
    ) -> arms20210422_models.ExportPrometheusRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.export_prometheus_rules_with_options_async(request, runtime)

    def get_agent_download_url_with_options(
        self,
        request: arms20210422_models.GetAgentDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetAgentDownloadUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentDownloadUrl',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetAgentDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_download_url_with_options_async(
        self,
        request: arms20210422_models.GetAgentDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetAgentDownloadUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentDownloadUrl',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetAgentDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_download_url(
        self,
        request: arms20210422_models.GetAgentDownloadUrlRequest,
    ) -> arms20210422_models.GetAgentDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_agent_download_url_with_options(request, runtime)

    async def get_agent_download_url_async(
        self,
        request: arms20210422_models.GetAgentDownloadUrlRequest,
    ) -> arms20210422_models.GetAgentDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_download_url_with_options_async(request, runtime)

    def get_app_api_by_page_with_options(
        self,
        request: arms20210422_models.GetAppApiByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetAppApiByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval_mills):
            query['IntervalMills'] = request.interval_mills
        if not UtilClient.is_unset(request.pid):
            query['PId'] = request.pid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppApiByPage',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetAppApiByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_api_by_page_with_options_async(
        self,
        request: arms20210422_models.GetAppApiByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetAppApiByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval_mills):
            query['IntervalMills'] = request.interval_mills
        if not UtilClient.is_unset(request.pid):
            query['PId'] = request.pid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppApiByPage',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetAppApiByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_api_by_page(
        self,
        request: arms20210422_models.GetAppApiByPageRequest,
    ) -> arms20210422_models.GetAppApiByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_api_by_page_with_options(request, runtime)

    async def get_app_api_by_page_async(
        self,
        request: arms20210422_models.GetAppApiByPageRequest,
    ) -> arms20210422_models.GetAppApiByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_api_by_page_with_options_async(request, runtime)

    def get_consistency_snapshot_with_options(
        self,
        request: arms20210422_models.GetConsistencySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetConsistencySnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.current_timestamp):
            query['CurrentTimestamp'] = request.current_timestamp
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConsistencySnapshot',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetConsistencySnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_consistency_snapshot_with_options_async(
        self,
        request: arms20210422_models.GetConsistencySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetConsistencySnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.current_timestamp):
            query['CurrentTimestamp'] = request.current_timestamp
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConsistencySnapshot',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetConsistencySnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_consistency_snapshot(
        self,
        request: arms20210422_models.GetConsistencySnapshotRequest,
    ) -> arms20210422_models.GetConsistencySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_consistency_snapshot_with_options(request, runtime)

    async def get_consistency_snapshot_async(
        self,
        request: arms20210422_models.GetConsistencySnapshotRequest,
    ) -> arms20210422_models.GetConsistencySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_consistency_snapshot_with_options_async(request, runtime)

    def get_integration_token_with_options(
        self,
        request: arms20210422_models.GetIntegrationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetIntegrationTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIntegrationToken',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetIntegrationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_integration_token_with_options_async(
        self,
        request: arms20210422_models.GetIntegrationTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetIntegrationTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIntegrationToken',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetIntegrationTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_integration_token(
        self,
        request: arms20210422_models.GetIntegrationTokenRequest,
    ) -> arms20210422_models.GetIntegrationTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_integration_token_with_options(request, runtime)

    async def get_integration_token_async(
        self,
        request: arms20210422_models.GetIntegrationTokenRequest,
    ) -> arms20210422_models.GetIntegrationTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_integration_token_with_options_async(request, runtime)

    def get_multiple_trace_with_options(
        self,
        request: arms20210422_models.GetMultipleTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetMultipleTraceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.trace_ids):
            query['TraceIDs'] = request.trace_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultipleTrace',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetMultipleTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multiple_trace_with_options_async(
        self,
        request: arms20210422_models.GetMultipleTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetMultipleTraceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.trace_ids):
            query['TraceIDs'] = request.trace_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultipleTrace',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetMultipleTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multiple_trace(
        self,
        request: arms20210422_models.GetMultipleTraceRequest,
    ) -> arms20210422_models.GetMultipleTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_multiple_trace_with_options(request, runtime)

    async def get_multiple_trace_async(
        self,
        request: arms20210422_models.GetMultipleTraceRequest,
    ) -> arms20210422_models.GetMultipleTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_multiple_trace_with_options_async(request, runtime)

    def get_prometheus_api_token_with_options(
        self,
        request: arms20210422_models.GetPrometheusApiTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetPrometheusApiTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusApiToken',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetPrometheusApiTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_api_token_with_options_async(
        self,
        request: arms20210422_models.GetPrometheusApiTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetPrometheusApiTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusApiToken',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetPrometheusApiTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_api_token(
        self,
        request: arms20210422_models.GetPrometheusApiTokenRequest,
    ) -> arms20210422_models.GetPrometheusApiTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_prometheus_api_token_with_options(request, runtime)

    async def get_prometheus_api_token_async(
        self,
        request: arms20210422_models.GetPrometheusApiTokenRequest,
    ) -> arms20210422_models.GetPrometheusApiTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_prometheus_api_token_with_options_async(request, runtime)

    def get_retcode_share_url_with_options(
        self,
        request: arms20210422_models.GetRetcodeShareUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetRetcodeShareUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRetcodeShareUrl',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetRetcodeShareUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_retcode_share_url_with_options_async(
        self,
        request: arms20210422_models.GetRetcodeShareUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetRetcodeShareUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRetcodeShareUrl',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetRetcodeShareUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_retcode_share_url(
        self,
        request: arms20210422_models.GetRetcodeShareUrlRequest,
    ) -> arms20210422_models.GetRetcodeShareUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_retcode_share_url_with_options(request, runtime)

    async def get_retcode_share_url_async(
        self,
        request: arms20210422_models.GetRetcodeShareUrlRequest,
    ) -> arms20210422_models.GetRetcodeShareUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_retcode_share_url_with_options_async(request, runtime)

    def get_stack_with_options(
        self,
        request: arms20210422_models.GetStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetStackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rpc_id):
            query['RpcID'] = request.rpc_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStack',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_with_options_async(
        self,
        request: arms20210422_models.GetStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetStackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rpc_id):
            query['RpcID'] = request.rpc_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStack',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack(
        self,
        request: arms20210422_models.GetStackRequest,
    ) -> arms20210422_models.GetStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_with_options(request, runtime)

    async def get_stack_async(
        self,
        request: arms20210422_models.GetStackRequest,
    ) -> arms20210422_models.GetStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_with_options_async(request, runtime)

    def get_trace_with_options(
        self,
        request: arms20210422_models.GetTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetTraceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrace',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trace_with_options_async(
        self,
        request: arms20210422_models.GetTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetTraceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrace',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trace(
        self,
        request: arms20210422_models.GetTraceRequest,
    ) -> arms20210422_models.GetTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_trace_with_options(request, runtime)

    async def get_trace_async(
        self,
        request: arms20210422_models.GetTraceRequest,
    ) -> arms20210422_models.GetTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_trace_with_options_async(request, runtime)

    def get_trace_app_with_options(
        self,
        request: arms20210422_models.GetTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetTraceAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTraceApp',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetTraceAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trace_app_with_options_async(
        self,
        request: arms20210422_models.GetTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.GetTraceAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTraceApp',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetTraceAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trace_app(
        self,
        request: arms20210422_models.GetTraceAppRequest,
    ) -> arms20210422_models.GetTraceAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_trace_app_with_options(request, runtime)

    async def get_trace_app_async(
        self,
        request: arms20210422_models.GetTraceAppRequest,
    ) -> arms20210422_models.GetTraceAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_trace_app_with_options_async(request, runtime)

    def import_app_alert_rules_with_options(
        self,
        request: arms20210422_models.ImportAppAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ImportAppAlertRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not UtilClient.is_unset(request.is_auto_start):
            query['IsAutoStart'] = request.is_auto_start
        if not UtilClient.is_unset(request.pids):
            query['Pids'] = request.pids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        if not UtilClient.is_unset(request.template_alert_id):
            query['TemplateAlertId'] = request.template_alert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportAppAlertRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ImportAppAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_app_alert_rules_with_options_async(
        self,
        request: arms20210422_models.ImportAppAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ImportAppAlertRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not UtilClient.is_unset(request.is_auto_start):
            query['IsAutoStart'] = request.is_auto_start
        if not UtilClient.is_unset(request.pids):
            query['Pids'] = request.pids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        if not UtilClient.is_unset(request.template_alert_id):
            query['TemplateAlertId'] = request.template_alert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportAppAlertRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ImportAppAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_app_alert_rules(
        self,
        request: arms20210422_models.ImportAppAlertRulesRequest,
    ) -> arms20210422_models.ImportAppAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_app_alert_rules_with_options(request, runtime)

    async def import_app_alert_rules_async(
        self,
        request: arms20210422_models.ImportAppAlertRulesRequest,
    ) -> arms20210422_models.ImportAppAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_app_alert_rules_with_options_async(request, runtime)

    def import_custom_alert_rules_with_options(
        self,
        request: arms20210422_models.ImportCustomAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ImportCustomAlertRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not UtilClient.is_unset(request.is_auto_start):
            query['IsAutoStart'] = request.is_auto_start
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        if not UtilClient.is_unset(request.template_alert_config):
            query['TemplateAlertConfig'] = request.template_alert_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportCustomAlertRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ImportCustomAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_custom_alert_rules_with_options_async(
        self,
        request: arms20210422_models.ImportCustomAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ImportCustomAlertRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not UtilClient.is_unset(request.is_auto_start):
            query['IsAutoStart'] = request.is_auto_start
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        if not UtilClient.is_unset(request.template_alert_config):
            query['TemplateAlertConfig'] = request.template_alert_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportCustomAlertRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ImportCustomAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_custom_alert_rules(
        self,
        request: arms20210422_models.ImportCustomAlertRulesRequest,
    ) -> arms20210422_models.ImportCustomAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_custom_alert_rules_with_options(request, runtime)

    async def import_custom_alert_rules_async(
        self,
        request: arms20210422_models.ImportCustomAlertRulesRequest,
    ) -> arms20210422_models.ImportCustomAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_custom_alert_rules_with_options_async(request, runtime)

    def import_prometheus_rules_with_options(
        self,
        request: arms20210422_models.ImportPrometheusRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ImportPrometheusRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.name_space):
            query['NameSpace'] = request.name_space
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportPrometheusRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ImportPrometheusRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_prometheus_rules_with_options_async(
        self,
        request: arms20210422_models.ImportPrometheusRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ImportPrometheusRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.name_space):
            query['NameSpace'] = request.name_space
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportPrometheusRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ImportPrometheusRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_prometheus_rules(
        self,
        request: arms20210422_models.ImportPrometheusRulesRequest,
    ) -> arms20210422_models.ImportPrometheusRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_prometheus_rules_with_options(request, runtime)

    async def import_prometheus_rules_async(
        self,
        request: arms20210422_models.ImportPrometheusRulesRequest,
    ) -> arms20210422_models.ImportPrometheusRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_prometheus_rules_with_options_async(request, runtime)

    def list_activated_alerts_with_options(
        self,
        request: arms20210422_models.ListActivatedAlertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListActivatedAlertsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListActivatedAlerts',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListActivatedAlertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_activated_alerts_with_options_async(
        self,
        request: arms20210422_models.ListActivatedAlertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListActivatedAlertsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListActivatedAlerts',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListActivatedAlertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_activated_alerts(
        self,
        request: arms20210422_models.ListActivatedAlertsRequest,
    ) -> arms20210422_models.ListActivatedAlertsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_activated_alerts_with_options(request, runtime)

    async def list_activated_alerts_async(
        self,
        request: arms20210422_models.ListActivatedAlertsRequest,
    ) -> arms20210422_models.ListActivatedAlertsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_activated_alerts_with_options_async(request, runtime)

    def list_alert_templates_with_options(
        self,
        request: arms20210422_models.ListAlertTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListAlertTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_provider):
            query['AlertProvider'] = request.alert_provider
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_provider):
            query['TemplateProvider'] = request.template_provider
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlertTemplates',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListAlertTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alert_templates_with_options_async(
        self,
        request: arms20210422_models.ListAlertTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListAlertTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_provider):
            query['AlertProvider'] = request.alert_provider
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_provider):
            query['TemplateProvider'] = request.template_provider
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlertTemplates',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListAlertTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alert_templates(
        self,
        request: arms20210422_models.ListAlertTemplatesRequest,
    ) -> arms20210422_models.ListAlertTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_alert_templates_with_options(request, runtime)

    async def list_alert_templates_async(
        self,
        request: arms20210422_models.ListAlertTemplatesRequest,
    ) -> arms20210422_models.ListAlertTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_alert_templates_with_options_async(request, runtime)

    def list_cluster_from_grafana_with_options(
        self,
        request: arms20210422_models.ListClusterFromGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListClusterFromGrafanaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterFromGrafana',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListClusterFromGrafanaResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_from_grafana_with_options_async(
        self,
        request: arms20210422_models.ListClusterFromGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListClusterFromGrafanaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterFromGrafana',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListClusterFromGrafanaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_from_grafana(
        self,
        request: arms20210422_models.ListClusterFromGrafanaRequest,
    ) -> arms20210422_models.ListClusterFromGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_from_grafana_with_options(request, runtime)

    async def list_cluster_from_grafana_async(
        self,
        request: arms20210422_models.ListClusterFromGrafanaRequest,
    ) -> arms20210422_models.ListClusterFromGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_from_grafana_with_options_async(request, runtime)

    def list_dashboards_with_options(
        self,
        request: arms20210422_models.ListDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListDashboardsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.recreate_switch):
            query['RecreateSwitch'] = request.recreate_switch
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboards',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListDashboardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dashboards_with_options_async(
        self,
        request: arms20210422_models.ListDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListDashboardsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.recreate_switch):
            query['RecreateSwitch'] = request.recreate_switch
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboards',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListDashboardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dashboards(
        self,
        request: arms20210422_models.ListDashboardsRequest,
    ) -> arms20210422_models.ListDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dashboards_with_options(request, runtime)

    async def list_dashboards_async(
        self,
        request: arms20210422_models.ListDashboardsRequest,
    ) -> arms20210422_models.ListDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dashboards_with_options_async(request, runtime)

    def list_dispatch_rule_with_options(
        self,
        request: arms20210422_models.ListDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListDispatchRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.system):
            query['System'] = request.system
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDispatchRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dispatch_rule_with_options_async(
        self,
        request: arms20210422_models.ListDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListDispatchRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.system):
            query['System'] = request.system
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDispatchRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListDispatchRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dispatch_rule(
        self,
        request: arms20210422_models.ListDispatchRuleRequest,
    ) -> arms20210422_models.ListDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dispatch_rule_with_options(request, runtime)

    async def list_dispatch_rule_async(
        self,
        request: arms20210422_models.ListDispatchRuleRequest,
    ) -> arms20210422_models.ListDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dispatch_rule_with_options_async(request, runtime)

    def list_prom_clusters_with_options(
        self,
        request: arms20210422_models.ListPromClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListPromClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPromClusters',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListPromClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prom_clusters_with_options_async(
        self,
        request: arms20210422_models.ListPromClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListPromClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPromClusters',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListPromClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prom_clusters(
        self,
        request: arms20210422_models.ListPromClustersRequest,
    ) -> arms20210422_models.ListPromClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_prom_clusters_with_options(request, runtime)

    async def list_prom_clusters_async(
        self,
        request: arms20210422_models.ListPromClustersRequest,
    ) -> arms20210422_models.ListPromClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_prom_clusters_with_options_async(request, runtime)

    def list_prometheus_alert_rules_with_options(
        self,
        request: arms20210422_models.ListPrometheusAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListPrometheusAlertRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.match_expressions):
            query['MatchExpressions'] = request.match_expressions
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusAlertRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListPrometheusAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_alert_rules_with_options_async(
        self,
        request: arms20210422_models.ListPrometheusAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListPrometheusAlertRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.match_expressions):
            query['MatchExpressions'] = request.match_expressions
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusAlertRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListPrometheusAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_alert_rules(
        self,
        request: arms20210422_models.ListPrometheusAlertRulesRequest,
    ) -> arms20210422_models.ListPrometheusAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_alert_rules_with_options(request, runtime)

    async def list_prometheus_alert_rules_async(
        self,
        request: arms20210422_models.ListPrometheusAlertRulesRequest,
    ) -> arms20210422_models.ListPrometheusAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_prometheus_alert_rules_with_options_async(request, runtime)

    def list_prometheus_alert_templates_with_options(
        self,
        request: arms20210422_models.ListPrometheusAlertTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListPrometheusAlertTemplatesResponse:
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
            action='ListPrometheusAlertTemplates',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListPrometheusAlertTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_alert_templates_with_options_async(
        self,
        request: arms20210422_models.ListPrometheusAlertTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListPrometheusAlertTemplatesResponse:
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
            action='ListPrometheusAlertTemplates',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListPrometheusAlertTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_alert_templates(
        self,
        request: arms20210422_models.ListPrometheusAlertTemplatesRequest,
    ) -> arms20210422_models.ListPrometheusAlertTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_alert_templates_with_options(request, runtime)

    async def list_prometheus_alert_templates_async(
        self,
        request: arms20210422_models.ListPrometheusAlertTemplatesRequest,
    ) -> arms20210422_models.ListPrometheusAlertTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_prometheus_alert_templates_with_options_async(request, runtime)

    def list_retcode_apps_with_options(
        self,
        request: arms20210422_models.ListRetcodeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListRetcodeAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRetcodeApps',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListRetcodeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_retcode_apps_with_options_async(
        self,
        request: arms20210422_models.ListRetcodeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListRetcodeAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRetcodeApps',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListRetcodeAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_retcode_apps(
        self,
        request: arms20210422_models.ListRetcodeAppsRequest,
    ) -> arms20210422_models.ListRetcodeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_retcode_apps_with_options(request, runtime)

    async def list_retcode_apps_async(
        self,
        request: arms20210422_models.ListRetcodeAppsRequest,
    ) -> arms20210422_models.ListRetcodeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_retcode_apps_with_options_async(request, runtime)

    def list_scenario_with_options(
        self,
        request: arms20210422_models.ListScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListScenarioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scenario):
            query['Scenario'] = request.scenario
        if not UtilClient.is_unset(request.sign):
            query['Sign'] = request.sign
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScenario',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scenario_with_options_async(
        self,
        request: arms20210422_models.ListScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListScenarioResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scenario):
            query['Scenario'] = request.scenario
        if not UtilClient.is_unset(request.sign):
            query['Sign'] = request.sign
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScenario',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListScenarioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scenario(
        self,
        request: arms20210422_models.ListScenarioRequest,
    ) -> arms20210422_models.ListScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_scenario_with_options(request, runtime)

    async def list_scenario_async(
        self,
        request: arms20210422_models.ListScenarioRequest,
    ) -> arms20210422_models.ListScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_scenario_with_options_async(request, runtime)

    def list_serverless_top_napps_with_options(
        self,
        request: arms20210422_models.ListServerlessTopNAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListServerlessTopNAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServerlessTopNApps',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListServerlessTopNAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_serverless_top_napps_with_options_async(
        self,
        request: arms20210422_models.ListServerlessTopNAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListServerlessTopNAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServerlessTopNApps',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListServerlessTopNAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_serverless_top_napps(
        self,
        request: arms20210422_models.ListServerlessTopNAppsRequest,
    ) -> arms20210422_models.ListServerlessTopNAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_serverless_top_napps_with_options(request, runtime)

    async def list_serverless_top_napps_async(
        self,
        request: arms20210422_models.ListServerlessTopNAppsRequest,
    ) -> arms20210422_models.ListServerlessTopNAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_serverless_top_napps_with_options_async(request, runtime)

    def list_trace_apps_with_options(
        self,
        request: arms20210422_models.ListTraceAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListTraceAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTraceApps',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListTraceAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_trace_apps_with_options_async(
        self,
        request: arms20210422_models.ListTraceAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.ListTraceAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTraceApps',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListTraceAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_trace_apps(
        self,
        request: arms20210422_models.ListTraceAppsRequest,
    ) -> arms20210422_models.ListTraceAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_trace_apps_with_options(request, runtime)

    async def list_trace_apps_async(
        self,
        request: arms20210422_models.ListTraceAppsRequest,
    ) -> arms20210422_models.ListTraceAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_trace_apps_with_options_async(request, runtime)

    def open_arms_default_slrwith_options(
        self,
        request: arms20210422_models.OpenArmsDefaultSLRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.OpenArmsDefaultSLRResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenArmsDefaultSLR',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.OpenArmsDefaultSLRResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_arms_default_slrwith_options_async(
        self,
        request: arms20210422_models.OpenArmsDefaultSLRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.OpenArmsDefaultSLRResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenArmsDefaultSLR',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.OpenArmsDefaultSLRResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_arms_default_slr(
        self,
        request: arms20210422_models.OpenArmsDefaultSLRRequest,
    ) -> arms20210422_models.OpenArmsDefaultSLRResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_arms_default_slrwith_options(request, runtime)

    async def open_arms_default_slr_async(
        self,
        request: arms20210422_models.OpenArmsDefaultSLRRequest,
    ) -> arms20210422_models.OpenArmsDefaultSLRResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_arms_default_slrwith_options_async(request, runtime)

    def open_arms_service_with_options(
        self,
        request: arms20210422_models.OpenArmsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.OpenArmsServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenArmsService',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.OpenArmsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_arms_service_with_options_async(
        self,
        request: arms20210422_models.OpenArmsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.OpenArmsServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenArmsService',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.OpenArmsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_arms_service(
        self,
        request: arms20210422_models.OpenArmsServiceRequest,
    ) -> arms20210422_models.OpenArmsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_arms_service_with_options(request, runtime)

    async def open_arms_service_async(
        self,
        request: arms20210422_models.OpenArmsServiceRequest,
    ) -> arms20210422_models.OpenArmsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_arms_service_with_options_async(request, runtime)

    def open_vcluster_with_options(
        self,
        request: arms20210422_models.OpenVClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.OpenVClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.recreate_switch):
            query['RecreateSwitch'] = request.recreate_switch
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenVCluster',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.OpenVClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_vcluster_with_options_async(
        self,
        request: arms20210422_models.OpenVClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.OpenVClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.recreate_switch):
            query['RecreateSwitch'] = request.recreate_switch
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenVCluster',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.OpenVClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_vcluster(
        self,
        request: arms20210422_models.OpenVClusterRequest,
    ) -> arms20210422_models.OpenVClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_vcluster_with_options(request, runtime)

    async def open_vcluster_async(
        self,
        request: arms20210422_models.OpenVClusterRequest,
    ) -> arms20210422_models.OpenVClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_vcluster_with_options_async(request, runtime)

    def open_xtrace_default_slrwith_options(
        self,
        request: arms20210422_models.OpenXtraceDefaultSLRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.OpenXtraceDefaultSLRResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenXtraceDefaultSLR',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.OpenXtraceDefaultSLRResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_xtrace_default_slrwith_options_async(
        self,
        request: arms20210422_models.OpenXtraceDefaultSLRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.OpenXtraceDefaultSLRResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenXtraceDefaultSLR',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.OpenXtraceDefaultSLRResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_xtrace_default_slr(
        self,
        request: arms20210422_models.OpenXtraceDefaultSLRRequest,
    ) -> arms20210422_models.OpenXtraceDefaultSLRResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_xtrace_default_slrwith_options(request, runtime)

    async def open_xtrace_default_slr_async(
        self,
        request: arms20210422_models.OpenXtraceDefaultSLRRequest,
    ) -> arms20210422_models.OpenXtraceDefaultSLRResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_xtrace_default_slrwith_options_async(request, runtime)

    def query_dataset_with_options(
        self,
        request: arms20210422_models.QueryDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.QueryDatasetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.date_str):
            query['DateStr'] = request.date_str
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.hungry_mode):
            query['HungryMode'] = request.hungry_mode
        if not UtilClient.is_unset(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not UtilClient.is_unset(request.is_drill_down):
            query['IsDrillDown'] = request.is_drill_down
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.max_time):
            query['MaxTime'] = request.max_time
        if not UtilClient.is_unset(request.measures):
            query['Measures'] = request.measures
        if not UtilClient.is_unset(request.min_time):
            query['MinTime'] = request.min_time
        if not UtilClient.is_unset(request.optional_dims):
            query['OptionalDims'] = request.optional_dims
        if not UtilClient.is_unset(request.order_by_key):
            query['OrderByKey'] = request.order_by_key
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.reduce_tail):
            query['ReduceTail'] = request.reduce_tail
        if not UtilClient.is_unset(request.required_dims):
            query['RequiredDims'] = request.required_dims
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataset',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.QueryDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dataset_with_options_async(
        self,
        request: arms20210422_models.QueryDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.QueryDatasetResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.date_str):
            query['DateStr'] = request.date_str
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.hungry_mode):
            query['HungryMode'] = request.hungry_mode
        if not UtilClient.is_unset(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not UtilClient.is_unset(request.is_drill_down):
            query['IsDrillDown'] = request.is_drill_down
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.max_time):
            query['MaxTime'] = request.max_time
        if not UtilClient.is_unset(request.measures):
            query['Measures'] = request.measures
        if not UtilClient.is_unset(request.min_time):
            query['MinTime'] = request.min_time
        if not UtilClient.is_unset(request.optional_dims):
            query['OptionalDims'] = request.optional_dims
        if not UtilClient.is_unset(request.order_by_key):
            query['OrderByKey'] = request.order_by_key
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.reduce_tail):
            query['ReduceTail'] = request.reduce_tail
        if not UtilClient.is_unset(request.required_dims):
            query['RequiredDims'] = request.required_dims
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataset',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.QueryDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dataset(
        self,
        request: arms20210422_models.QueryDatasetRequest,
    ) -> arms20210422_models.QueryDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_with_options(request, runtime)

    async def query_dataset_async(
        self,
        request: arms20210422_models.QueryDatasetRequest,
    ) -> arms20210422_models.QueryDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dataset_with_options_async(request, runtime)

    def query_metric_with_options(
        self,
        request: arms20210422_models.QueryMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.QueryMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consistency_data_key):
            query['ConsistencyDataKey'] = request.consistency_data_key
        if not UtilClient.is_unset(request.consistency_query_strategy):
            query['ConsistencyQueryStrategy'] = request.consistency_query_strategy
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.measures):
            query['Measures'] = request.measures
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetric',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.QueryMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_metric_with_options_async(
        self,
        request: arms20210422_models.QueryMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.QueryMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consistency_data_key):
            query['ConsistencyDataKey'] = request.consistency_data_key
        if not UtilClient.is_unset(request.consistency_query_strategy):
            query['ConsistencyQueryStrategy'] = request.consistency_query_strategy
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.measures):
            query['Measures'] = request.measures
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetric',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.QueryMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_metric(
        self,
        request: arms20210422_models.QueryMetricRequest,
    ) -> arms20210422_models.QueryMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_metric_with_options(request, runtime)

    async def query_metric_async(
        self,
        request: arms20210422_models.QueryMetricRequest,
    ) -> arms20210422_models.QueryMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_metric_with_options_async(request, runtime)

    def query_metric_by_page_with_options(
        self,
        request: arms20210422_models.QueryMetricByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.QueryMetricByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.custom_filters):
            query['CustomFilters'] = request.custom_filters
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not UtilClient.is_unset(request.measures):
            query['Measures'] = request.measures
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetricByPage',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.QueryMetricByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_metric_by_page_with_options_async(
        self,
        request: arms20210422_models.QueryMetricByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.QueryMetricByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.custom_filters):
            query['CustomFilters'] = request.custom_filters
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not UtilClient.is_unset(request.measures):
            query['Measures'] = request.measures
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetricByPage',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.QueryMetricByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_metric_by_page(
        self,
        request: arms20210422_models.QueryMetricByPageRequest,
    ) -> arms20210422_models.QueryMetricByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_metric_by_page_with_options(request, runtime)

    async def query_metric_by_page_async(
        self,
        request: arms20210422_models.QueryMetricByPageRequest,
    ) -> arms20210422_models.QueryMetricByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_metric_by_page_with_options_async(request, runtime)

    def save_trace_app_config_with_options(
        self,
        request: arms20210422_models.SaveTraceAppConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SaveTraceAppConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.settings):
            query['Settings'] = request.settings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTraceAppConfig',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SaveTraceAppConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_trace_app_config_with_options_async(
        self,
        request: arms20210422_models.SaveTraceAppConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SaveTraceAppConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.settings):
            query['Settings'] = request.settings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTraceAppConfig',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SaveTraceAppConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_trace_app_config(
        self,
        request: arms20210422_models.SaveTraceAppConfigRequest,
    ) -> arms20210422_models.SaveTraceAppConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_trace_app_config_with_options(request, runtime)

    async def save_trace_app_config_async(
        self,
        request: arms20210422_models.SaveTraceAppConfigRequest,
    ) -> arms20210422_models.SaveTraceAppConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_trace_app_config_with_options_async(request, runtime)

    def search_alert_contact_with_options(
        self,
        request: arms20210422_models.SearchAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchAlertContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchAlertContact',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_alert_contact_with_options_async(
        self,
        request: arms20210422_models.SearchAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchAlertContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchAlertContact',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_alert_contact(
        self,
        request: arms20210422_models.SearchAlertContactRequest,
    ) -> arms20210422_models.SearchAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_alert_contact_with_options(request, runtime)

    async def search_alert_contact_async(
        self,
        request: arms20210422_models.SearchAlertContactRequest,
    ) -> arms20210422_models.SearchAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_contact_with_options_async(request, runtime)

    def search_alert_contact_group_with_options(
        self,
        request: arms20210422_models.SearchAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchAlertContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchAlertContactGroup',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_alert_contact_group_with_options_async(
        self,
        request: arms20210422_models.SearchAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchAlertContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchAlertContactGroup',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_alert_contact_group(
        self,
        request: arms20210422_models.SearchAlertContactGroupRequest,
    ) -> arms20210422_models.SearchAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_alert_contact_group_with_options(request, runtime)

    async def search_alert_contact_group_async(
        self,
        request: arms20210422_models.SearchAlertContactGroupRequest,
    ) -> arms20210422_models.SearchAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_contact_group_with_options_async(request, runtime)

    def search_alert_histories_with_options(
        self,
        request: arms20210422_models.SearchAlertHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchAlertHistoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.alert_type):
            query['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchAlertHistories',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchAlertHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_alert_histories_with_options_async(
        self,
        request: arms20210422_models.SearchAlertHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchAlertHistoriesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.alert_type):
            query['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchAlertHistories',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchAlertHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_alert_histories(
        self,
        request: arms20210422_models.SearchAlertHistoriesRequest,
    ) -> arms20210422_models.SearchAlertHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_alert_histories_with_options(request, runtime)

    async def search_alert_histories_async(
        self,
        request: arms20210422_models.SearchAlertHistoriesRequest,
    ) -> arms20210422_models.SearchAlertHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_histories_with_options_async(request, runtime)

    def search_alert_rules_with_options(
        self,
        request: arms20210422_models.SearchAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchAlertRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchAlertRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_alert_rules_with_options_async(
        self,
        request: arms20210422_models.SearchAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchAlertRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchAlertRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_alert_rules(
        self,
        request: arms20210422_models.SearchAlertRulesRequest,
    ) -> arms20210422_models.SearchAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_alert_rules_with_options(request, runtime)

    async def search_alert_rules_async(
        self,
        request: arms20210422_models.SearchAlertRulesRequest,
    ) -> arms20210422_models.SearchAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_rules_with_options_async(request, runtime)

    def search_events_with_options(
        self,
        request: arms20210422_models.SearchEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.alert_type):
            query['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.is_trigger):
            query['IsTrigger'] = request.is_trigger
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchEvents',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_events_with_options_async(
        self,
        request: arms20210422_models.SearchEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.alert_type):
            query['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.is_trigger):
            query['IsTrigger'] = request.is_trigger
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchEvents',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_events(
        self,
        request: arms20210422_models.SearchEventsRequest,
    ) -> arms20210422_models.SearchEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_events_with_options(request, runtime)

    async def search_events_async(
        self,
        request: arms20210422_models.SearchEventsRequest,
    ) -> arms20210422_models.SearchEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_events_with_options_async(request, runtime)

    def search_retcode_app_by_page_with_options(
        self,
        request: arms20210422_models.SearchRetcodeAppByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchRetcodeAppByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchRetcodeAppByPage',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchRetcodeAppByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_retcode_app_by_page_with_options_async(
        self,
        request: arms20210422_models.SearchRetcodeAppByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchRetcodeAppByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchRetcodeAppByPage',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchRetcodeAppByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_retcode_app_by_page(
        self,
        request: arms20210422_models.SearchRetcodeAppByPageRequest,
    ) -> arms20210422_models.SearchRetcodeAppByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_retcode_app_by_page_with_options(request, runtime)

    async def search_retcode_app_by_page_async(
        self,
        request: arms20210422_models.SearchRetcodeAppByPageRequest,
    ) -> arms20210422_models.SearchRetcodeAppByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_retcode_app_by_page_with_options_async(request, runtime)

    def search_trace_app_by_name_with_options(
        self,
        request: arms20210422_models.SearchTraceAppByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchTraceAppByNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.trace_app_name):
            query['TraceAppName'] = request.trace_app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTraceAppByName',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchTraceAppByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_trace_app_by_name_with_options_async(
        self,
        request: arms20210422_models.SearchTraceAppByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchTraceAppByNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.trace_app_name):
            query['TraceAppName'] = request.trace_app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTraceAppByName',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchTraceAppByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_trace_app_by_name(
        self,
        request: arms20210422_models.SearchTraceAppByNameRequest,
    ) -> arms20210422_models.SearchTraceAppByNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_trace_app_by_name_with_options(request, runtime)

    async def search_trace_app_by_name_async(
        self,
        request: arms20210422_models.SearchTraceAppByNameRequest,
    ) -> arms20210422_models.SearchTraceAppByNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_trace_app_by_name_with_options_async(request, runtime)

    def search_trace_app_by_page_with_options(
        self,
        request: arms20210422_models.SearchTraceAppByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchTraceAppByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.trace_app_name):
            query['TraceAppName'] = request.trace_app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTraceAppByPage',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchTraceAppByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_trace_app_by_page_with_options_async(
        self,
        request: arms20210422_models.SearchTraceAppByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchTraceAppByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.trace_app_name):
            query['TraceAppName'] = request.trace_app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTraceAppByPage',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchTraceAppByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_trace_app_by_page(
        self,
        request: arms20210422_models.SearchTraceAppByPageRequest,
    ) -> arms20210422_models.SearchTraceAppByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_trace_app_by_page_with_options(request, runtime)

    async def search_trace_app_by_page_async(
        self,
        request: arms20210422_models.SearchTraceAppByPageRequest,
    ) -> arms20210422_models.SearchTraceAppByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_trace_app_by_page_with_options_async(request, runtime)

    def search_traces_with_options(
        self,
        request: arms20210422_models.SearchTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchTracesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.exclusion_filters):
            query['ExclusionFilters'] = request.exclusion_filters
        if not UtilClient.is_unset(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not UtilClient.is_unset(request.operation_name):
            query['OperationName'] = request.operation_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.service_ip):
            query['ServiceIp'] = request.service_ip
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTraces',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchTracesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_traces_with_options_async(
        self,
        request: arms20210422_models.SearchTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchTracesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.exclusion_filters):
            query['ExclusionFilters'] = request.exclusion_filters
        if not UtilClient.is_unset(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not UtilClient.is_unset(request.operation_name):
            query['OperationName'] = request.operation_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.service_ip):
            query['ServiceIp'] = request.service_ip
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTraces',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchTracesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_traces(
        self,
        request: arms20210422_models.SearchTracesRequest,
    ) -> arms20210422_models.SearchTracesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_traces_with_options(request, runtime)

    async def search_traces_async(
        self,
        request: arms20210422_models.SearchTracesRequest,
    ) -> arms20210422_models.SearchTracesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_traces_with_options_async(request, runtime)

    def search_traces_by_page_with_options(
        self,
        request: arms20210422_models.SearchTracesByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchTracesByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.exclusion_filters):
            query['ExclusionFilters'] = request.exclusion_filters
        if not UtilClient.is_unset(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not UtilClient.is_unset(request.operation_name):
            query['OperationName'] = request.operation_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.service_ip):
            query['ServiceIp'] = request.service_ip
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTracesByPage',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchTracesByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_traces_by_page_with_options_async(
        self,
        request: arms20210422_models.SearchTracesByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SearchTracesByPageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.exclusion_filters):
            query['ExclusionFilters'] = request.exclusion_filters
        if not UtilClient.is_unset(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not UtilClient.is_unset(request.operation_name):
            query['OperationName'] = request.operation_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.service_ip):
            query['ServiceIp'] = request.service_ip
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTracesByPage',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchTracesByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_traces_by_page(
        self,
        request: arms20210422_models.SearchTracesByPageRequest,
    ) -> arms20210422_models.SearchTracesByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_traces_by_page_with_options(request, runtime)

    async def search_traces_by_page_async(
        self,
        request: arms20210422_models.SearchTracesByPageRequest,
    ) -> arms20210422_models.SearchTracesByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_traces_by_page_with_options_async(request, runtime)

    def send_custom_incidents_with_options(
        self,
        request: arms20210422_models.SendCustomIncidentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SendCustomIncidentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.incidents):
            query['Incidents'] = request.incidents
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendCustomIncidents',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SendCustomIncidentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_custom_incidents_with_options_async(
        self,
        request: arms20210422_models.SendCustomIncidentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SendCustomIncidentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.incidents):
            query['Incidents'] = request.incidents
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendCustomIncidents',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SendCustomIncidentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_custom_incidents(
        self,
        request: arms20210422_models.SendCustomIncidentsRequest,
    ) -> arms20210422_models.SendCustomIncidentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_custom_incidents_with_options(request, runtime)

    async def send_custom_incidents_async(
        self,
        request: arms20210422_models.SendCustomIncidentsRequest,
    ) -> arms20210422_models.SendCustomIncidentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_custom_incidents_with_options_async(request, runtime)

    def send_mse_incident_with_options(
        self,
        request: arms20210422_models.SendMseIncidentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SendMseIncidentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.incidents):
            query['Incidents'] = request.incidents
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendMseIncident',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SendMseIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_mse_incident_with_options_async(
        self,
        request: arms20210422_models.SendMseIncidentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SendMseIncidentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.incidents):
            query['Incidents'] = request.incidents
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendMseIncident',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SendMseIncidentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_mse_incident(
        self,
        request: arms20210422_models.SendMseIncidentRequest,
    ) -> arms20210422_models.SendMseIncidentResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_mse_incident_with_options(request, runtime)

    async def send_mse_incident_async(
        self,
        request: arms20210422_models.SendMseIncidentRequest,
    ) -> arms20210422_models.SendMseIncidentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_mse_incident_with_options_async(request, runtime)

    def set_retcode_share_status_with_options(
        self,
        request: arms20210422_models.SetRetcodeShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SetRetcodeShareStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRetcodeShareStatus',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SetRetcodeShareStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_retcode_share_status_with_options_async(
        self,
        request: arms20210422_models.SetRetcodeShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.SetRetcodeShareStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRetcodeShareStatus',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SetRetcodeShareStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_retcode_share_status(
        self,
        request: arms20210422_models.SetRetcodeShareStatusRequest,
    ) -> arms20210422_models.SetRetcodeShareStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_retcode_share_status_with_options(request, runtime)

    async def set_retcode_share_status_async(
        self,
        request: arms20210422_models.SetRetcodeShareStatusRequest,
    ) -> arms20210422_models.SetRetcodeShareStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_retcode_share_status_with_options_async(request, runtime)

    def start_alert_with_options(
        self,
        request: arms20210422_models.StartAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.StartAlertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartAlert',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.StartAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_alert_with_options_async(
        self,
        request: arms20210422_models.StartAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.StartAlertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartAlert',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.StartAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_alert(
        self,
        request: arms20210422_models.StartAlertRequest,
    ) -> arms20210422_models.StartAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_alert_with_options(request, runtime)

    async def start_alert_async(
        self,
        request: arms20210422_models.StartAlertRequest,
    ) -> arms20210422_models.StartAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_alert_with_options_async(request, runtime)

    def stop_alert_with_options(
        self,
        request: arms20210422_models.StopAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.StopAlertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAlert',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.StopAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_alert_with_options_async(
        self,
        request: arms20210422_models.StopAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.StopAlertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAlert',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.StopAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_alert(
        self,
        request: arms20210422_models.StopAlertRequest,
    ) -> arms20210422_models.StopAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_alert_with_options(request, runtime)

    async def stop_alert_async(
        self,
        request: arms20210422_models.StopAlertRequest,
    ) -> arms20210422_models.StopAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_alert_with_options_async(request, runtime)

    def update_alert_contact_with_options(
        self,
        request: arms20210422_models.UpdateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.UpdateAlertContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.ding_robot_webhook_url):
            query['DingRobotWebhookUrl'] = request.ding_robot_webhook_url
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.system_noc):
            query['SystemNoc'] = request.system_noc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlertContact',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alert_contact_with_options_async(
        self,
        request: arms20210422_models.UpdateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.UpdateAlertContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.ding_robot_webhook_url):
            query['DingRobotWebhookUrl'] = request.ding_robot_webhook_url
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.system_noc):
            query['SystemNoc'] = request.system_noc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlertContact',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alert_contact(
        self,
        request: arms20210422_models.UpdateAlertContactRequest,
    ) -> arms20210422_models.UpdateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_alert_contact_with_options(request, runtime)

    async def update_alert_contact_async(
        self,
        request: arms20210422_models.UpdateAlertContactRequest,
    ) -> arms20210422_models.UpdateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_alert_contact_with_options_async(request, runtime)

    def update_alert_contact_group_with_options(
        self,
        request: arms20210422_models.UpdateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.UpdateAlertContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_id):
            query['ContactGroupId'] = request.contact_group_id
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlertContactGroup',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alert_contact_group_with_options_async(
        self,
        request: arms20210422_models.UpdateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.UpdateAlertContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_id):
            query['ContactGroupId'] = request.contact_group_id
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlertContactGroup',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alert_contact_group(
        self,
        request: arms20210422_models.UpdateAlertContactGroupRequest,
    ) -> arms20210422_models.UpdateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_alert_contact_group_with_options(request, runtime)

    async def update_alert_contact_group_async(
        self,
        request: arms20210422_models.UpdateAlertContactGroupRequest,
    ) -> arms20210422_models.UpdateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_alert_contact_group_with_options_async(request, runtime)

    def update_alert_rule_with_options(
        self,
        request: arms20210422_models.UpdateAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.UpdateAlertRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not UtilClient.is_unset(request.is_auto_start):
            query['IsAutoStart'] = request.is_auto_start
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlertRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alert_rule_with_options_async(
        self,
        request: arms20210422_models.UpdateAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.UpdateAlertRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not UtilClient.is_unset(request.is_auto_start):
            query['IsAutoStart'] = request.is_auto_start
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlertRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alert_rule(
        self,
        request: arms20210422_models.UpdateAlertRuleRequest,
    ) -> arms20210422_models.UpdateAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_alert_rule_with_options(request, runtime)

    async def update_alert_rule_async(
        self,
        request: arms20210422_models.UpdateAlertRuleRequest,
    ) -> arms20210422_models.UpdateAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_alert_rule_with_options_async(request, runtime)

    def update_alert_template_with_options(
        self,
        request: arms20210422_models.UpdateAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.UpdateAlertTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.match_expressions):
            query['MatchExpressions'] = request.match_expressions
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlertTemplate',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateAlertTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alert_template_with_options_async(
        self,
        request: arms20210422_models.UpdateAlertTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.UpdateAlertTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.match_expressions):
            query['MatchExpressions'] = request.match_expressions
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlertTemplate',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateAlertTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alert_template(
        self,
        request: arms20210422_models.UpdateAlertTemplateRequest,
    ) -> arms20210422_models.UpdateAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_alert_template_with_options(request, runtime)

    async def update_alert_template_async(
        self,
        request: arms20210422_models.UpdateAlertTemplateRequest,
    ) -> arms20210422_models.UpdateAlertTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_alert_template_with_options_async(request, runtime)

    def update_dispatch_rule_with_options(
        self,
        request: arms20210422_models.UpdateDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.UpdateDispatchRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dispatch_rule):
            query['DispatchRule'] = request.dispatch_rule
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDispatchRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dispatch_rule_with_options_async(
        self,
        request: arms20210422_models.UpdateDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.UpdateDispatchRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dispatch_rule):
            query['DispatchRule'] = request.dispatch_rule
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDispatchRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateDispatchRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dispatch_rule(
        self,
        request: arms20210422_models.UpdateDispatchRuleRequest,
    ) -> arms20210422_models.UpdateDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dispatch_rule_with_options(request, runtime)

    async def update_dispatch_rule_async(
        self,
        request: arms20210422_models.UpdateDispatchRuleRequest,
    ) -> arms20210422_models.UpdateDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dispatch_rule_with_options_async(request, runtime)

    def update_prometheus_alert_rule_with_options(
        self,
        request: arms20210422_models.UpdatePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.UpdatePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.alert_name):
            query['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.dispatch_rule_id):
            query['DispatchRuleId'] = request.dispatch_rule_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusAlertRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdatePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_alert_rule_with_options_async(
        self,
        request: arms20210422_models.UpdatePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.UpdatePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.alert_name):
            query['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.dispatch_rule_id):
            query['DispatchRuleId'] = request.dispatch_rule_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusAlertRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdatePrometheusAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_alert_rule(
        self,
        request: arms20210422_models.UpdatePrometheusAlertRuleRequest,
    ) -> arms20210422_models.UpdatePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_prometheus_alert_rule_with_options(request, runtime)

    async def update_prometheus_alert_rule_async(
        self,
        request: arms20210422_models.UpdatePrometheusAlertRuleRequest,
    ) -> arms20210422_models.UpdatePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_prometheus_alert_rule_with_options_async(request, runtime)

    def update_webhook_with_options(
        self,
        request: arms20210422_models.UpdateWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.UpdateWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.http_headers):
            query['HttpHeaders'] = request.http_headers
        if not UtilClient.is_unset(request.http_params):
            query['HttpParams'] = request.http_params
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWebhook',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_webhook_with_options_async(
        self,
        request: arms20210422_models.UpdateWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20210422_models.UpdateWebhookResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.http_headers):
            query['HttpHeaders'] = request.http_headers
        if not UtilClient.is_unset(request.http_params):
            query['HttpParams'] = request.http_params
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWebhook',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_webhook(
        self,
        request: arms20210422_models.UpdateWebhookRequest,
    ) -> arms20210422_models.UpdateWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_webhook_with_options(request, runtime)

    async def update_webhook_async(
        self,
        request: arms20210422_models.UpdateWebhookRequest,
    ) -> arms20210422_models.UpdateWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_webhook_with_options_async(request, runtime)
