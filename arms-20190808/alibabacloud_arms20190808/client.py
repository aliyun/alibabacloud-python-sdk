# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_arms20190808 import models as main_models
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

    def add_ali_cluster_ids_to_prometheus_global_view_with_options(
        self,
        request: main_models.AddAliClusterIdsToPrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAliClusterIdsToPrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not DaraCore.is_null(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAliClusterIdsToPrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAliClusterIdsToPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ali_cluster_ids_to_prometheus_global_view_with_options_async(
        self,
        request: main_models.AddAliClusterIdsToPrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddAliClusterIdsToPrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not DaraCore.is_null(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddAliClusterIdsToPrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddAliClusterIdsToPrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ali_cluster_ids_to_prometheus_global_view(
        self,
        request: main_models.AddAliClusterIdsToPrometheusGlobalViewRequest,
    ) -> main_models.AddAliClusterIdsToPrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return self.add_ali_cluster_ids_to_prometheus_global_view_with_options(request, runtime)

    async def add_ali_cluster_ids_to_prometheus_global_view_async(
        self,
        request: main_models.AddAliClusterIdsToPrometheusGlobalViewRequest,
    ) -> main_models.AddAliClusterIdsToPrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return await self.add_ali_cluster_ids_to_prometheus_global_view_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def add_prometheus_global_view_with_options(
        self,
        request: main_models.AddPrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.clusters):
            query['Clusters'] = request.clusters
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_prometheus_global_view_with_options_async(
        self,
        request: main_models.AddPrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.clusters):
            query['Clusters'] = request.clusters
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_prometheus_global_view(
        self,
        request: main_models.AddPrometheusGlobalViewRequest,
    ) -> main_models.AddPrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return self.add_prometheus_global_view_with_options(request, runtime)

    async def add_prometheus_global_view_async(
        self,
        request: main_models.AddPrometheusGlobalViewRequest,
    ) -> main_models.AddPrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return await self.add_prometheus_global_view_with_options_async(request, runtime)

    def add_prometheus_global_view_by_ali_cluster_ids_with_options(
        self,
        request: main_models.AddPrometheusGlobalViewByAliClusterIdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPrometheusGlobalViewByAliClusterIdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPrometheusGlobalViewByAliClusterIds',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPrometheusGlobalViewByAliClusterIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_prometheus_global_view_by_ali_cluster_ids_with_options_async(
        self,
        request: main_models.AddPrometheusGlobalViewByAliClusterIdsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPrometheusGlobalViewByAliClusterIdsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPrometheusGlobalViewByAliClusterIds',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPrometheusGlobalViewByAliClusterIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_prometheus_global_view_by_ali_cluster_ids(
        self,
        request: main_models.AddPrometheusGlobalViewByAliClusterIdsRequest,
    ) -> main_models.AddPrometheusGlobalViewByAliClusterIdsResponse:
        runtime = RuntimeOptions()
        return self.add_prometheus_global_view_by_ali_cluster_ids_with_options(request, runtime)

    async def add_prometheus_global_view_by_ali_cluster_ids_async(
        self,
        request: main_models.AddPrometheusGlobalViewByAliClusterIdsRequest,
    ) -> main_models.AddPrometheusGlobalViewByAliClusterIdsResponse:
        runtime = RuntimeOptions()
        return await self.add_prometheus_global_view_by_ali_cluster_ids_with_options_async(request, runtime)

    def add_prometheus_instance_with_options(
        self,
        request: main_models.AddPrometheusInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPrometheusInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPrometheusInstance',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_prometheus_instance_with_options_async(
        self,
        request: main_models.AddPrometheusInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPrometheusInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPrometheusInstance',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPrometheusInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_prometheus_instance(
        self,
        request: main_models.AddPrometheusInstanceRequest,
    ) -> main_models.AddPrometheusInstanceResponse:
        runtime = RuntimeOptions()
        return self.add_prometheus_instance_with_options(request, runtime)

    async def add_prometheus_instance_async(
        self,
        request: main_models.AddPrometheusInstanceRequest,
    ) -> main_models.AddPrometheusInstanceResponse:
        runtime = RuntimeOptions()
        return await self.add_prometheus_instance_with_options_async(request, runtime)

    def add_prometheus_integration_with_options(
        self,
        request: main_models.AddPrometheusIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPrometheusIntegrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPrometheusIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPrometheusIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_prometheus_integration_with_options_async(
        self,
        request: main_models.AddPrometheusIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddPrometheusIntegrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddPrometheusIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddPrometheusIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_prometheus_integration(
        self,
        request: main_models.AddPrometheusIntegrationRequest,
    ) -> main_models.AddPrometheusIntegrationResponse:
        runtime = RuntimeOptions()
        return self.add_prometheus_integration_with_options(request, runtime)

    async def add_prometheus_integration_async(
        self,
        request: main_models.AddPrometheusIntegrationRequest,
    ) -> main_models.AddPrometheusIntegrationResponse:
        runtime = RuntimeOptions()
        return await self.add_prometheus_integration_with_options_async(request, runtime)

    def add_recording_rule_with_options(
        self,
        request: main_models.AddRecordingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRecordingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_yaml):
            query['RuleYaml'] = request.rule_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRecordingRule',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRecordingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_recording_rule_with_options_async(
        self,
        request: main_models.AddRecordingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddRecordingRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rule_yaml):
            query['RuleYaml'] = request.rule_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddRecordingRule',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddRecordingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_recording_rule(
        self,
        request: main_models.AddRecordingRuleRequest,
    ) -> main_models.AddRecordingRuleResponse:
        runtime = RuntimeOptions()
        return self.add_recording_rule_with_options(request, runtime)

    async def add_recording_rule_async(
        self,
        request: main_models.AddRecordingRuleRequest,
    ) -> main_models.AddRecordingRuleResponse:
        runtime = RuntimeOptions()
        return await self.add_recording_rule_with_options_async(request, runtime)

    def add_tag_to_flink_cluster_with_options(
        self,
        request: main_models.AddTagToFlinkClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTagToFlinkClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.flink_work_space_id):
            query['FlinkWorkSpaceId'] = request.flink_work_space_id
        if not DaraCore.is_null(request.flink_work_space_name):
            query['FlinkWorkSpaceName'] = request.flink_work_space_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTagToFlinkCluster',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTagToFlinkClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_tag_to_flink_cluster_with_options_async(
        self,
        request: main_models.AddTagToFlinkClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTagToFlinkClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.flink_work_space_id):
            query['FlinkWorkSpaceId'] = request.flink_work_space_id
        if not DaraCore.is_null(request.flink_work_space_name):
            query['FlinkWorkSpaceName'] = request.flink_work_space_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTagToFlinkCluster',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTagToFlinkClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_tag_to_flink_cluster(
        self,
        request: main_models.AddTagToFlinkClusterRequest,
    ) -> main_models.AddTagToFlinkClusterResponse:
        runtime = RuntimeOptions()
        return self.add_tag_to_flink_cluster_with_options(request, runtime)

    async def add_tag_to_flink_cluster_async(
        self,
        request: main_models.AddTagToFlinkClusterRequest,
    ) -> main_models.AddTagToFlinkClusterResponse:
        runtime = RuntimeOptions()
        return await self.add_tag_to_flink_cluster_with_options_async(request, runtime)

    def append_instances_to_prometheus_global_view_with_options(
        self,
        request: main_models.AppendInstancesToPrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AppendInstancesToPrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.clusters):
            query['Clusters'] = request.clusters
        if not DaraCore.is_null(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AppendInstancesToPrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AppendInstancesToPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def append_instances_to_prometheus_global_view_with_options_async(
        self,
        request: main_models.AppendInstancesToPrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AppendInstancesToPrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.clusters):
            query['Clusters'] = request.clusters
        if not DaraCore.is_null(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AppendInstancesToPrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AppendInstancesToPrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def append_instances_to_prometheus_global_view(
        self,
        request: main_models.AppendInstancesToPrometheusGlobalViewRequest,
    ) -> main_models.AppendInstancesToPrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return self.append_instances_to_prometheus_global_view_with_options(request, runtime)

    async def append_instances_to_prometheus_global_view_async(
        self,
        request: main_models.AppendInstancesToPrometheusGlobalViewRequest,
    ) -> main_models.AppendInstancesToPrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return await self.append_instances_to_prometheus_global_view_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def bind_prometheus_grafana_instance_with_options(
        self,
        request: main_models.BindPrometheusGrafanaInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindPrometheusGrafanaInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.grafana_instance_id):
            query['GrafanaInstanceId'] = request.grafana_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindPrometheusGrafanaInstance',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindPrometheusGrafanaInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_prometheus_grafana_instance_with_options_async(
        self,
        request: main_models.BindPrometheusGrafanaInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BindPrometheusGrafanaInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.grafana_instance_id):
            query['GrafanaInstanceId'] = request.grafana_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BindPrometheusGrafanaInstance',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BindPrometheusGrafanaInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_prometheus_grafana_instance(
        self,
        request: main_models.BindPrometheusGrafanaInstanceRequest,
    ) -> main_models.BindPrometheusGrafanaInstanceResponse:
        runtime = RuntimeOptions()
        return self.bind_prometheus_grafana_instance_with_options(request, runtime)

    async def bind_prometheus_grafana_instance_async(
        self,
        request: main_models.BindPrometheusGrafanaInstanceRequest,
    ) -> main_models.BindPrometheusGrafanaInstanceResponse:
        runtime = RuntimeOptions()
        return await self.bind_prometheus_grafana_instance_with_options_async(request, runtime)

    def block_alarm_notification_with_options(
        self,
        request: main_models.BlockAlarmNotificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BlockAlarmNotificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not DaraCore.is_null(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BlockAlarmNotification',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BlockAlarmNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def block_alarm_notification_with_options_async(
        self,
        request: main_models.BlockAlarmNotificationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BlockAlarmNotificationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not DaraCore.is_null(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BlockAlarmNotification',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BlockAlarmNotificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def block_alarm_notification(
        self,
        request: main_models.BlockAlarmNotificationRequest,
    ) -> main_models.BlockAlarmNotificationResponse:
        runtime = RuntimeOptions()
        return self.block_alarm_notification_with_options(request, runtime)

    async def block_alarm_notification_async(
        self,
        request: main_models.BlockAlarmNotificationRequest,
    ) -> main_models.BlockAlarmNotificationResponse:
        runtime = RuntimeOptions()
        return await self.block_alarm_notification_with_options_async(request, runtime)

    def change_alarm_severity_with_options(
        self,
        request: main_models.ChangeAlarmSeverityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeAlarmSeverityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not DaraCore.is_null(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeAlarmSeverity',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeAlarmSeverityResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_alarm_severity_with_options_async(
        self,
        request: main_models.ChangeAlarmSeverityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeAlarmSeverityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not DaraCore.is_null(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeAlarmSeverity',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeAlarmSeverityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_alarm_severity(
        self,
        request: main_models.ChangeAlarmSeverityRequest,
    ) -> main_models.ChangeAlarmSeverityResponse:
        runtime = RuntimeOptions()
        return self.change_alarm_severity_with_options(request, runtime)

    async def change_alarm_severity_async(
        self,
        request: main_models.ChangeAlarmSeverityRequest,
    ) -> main_models.ChangeAlarmSeverityResponse:
        runtime = RuntimeOptions()
        return await self.change_alarm_severity_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChangeResourceGroup',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def check_commercial_status_with_options(
        self,
        request: main_models.CheckCommercialStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCommercialStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckCommercialStatus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCommercialStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_commercial_status_with_options_async(
        self,
        request: main_models.CheckCommercialStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckCommercialStatusResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckCommercialStatus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckCommercialStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_commercial_status(
        self,
        request: main_models.CheckCommercialStatusRequest,
    ) -> main_models.CheckCommercialStatusResponse:
        runtime = RuntimeOptions()
        return self.check_commercial_status_with_options(request, runtime)

    async def check_commercial_status_async(
        self,
        request: main_models.CheckCommercialStatusRequest,
    ) -> main_models.CheckCommercialStatusResponse:
        runtime = RuntimeOptions()
        return await self.check_commercial_status_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def claim_alarm_with_options(
        self,
        request: main_models.ClaimAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClaimAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not DaraCore.is_null(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClaimAlarm',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClaimAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def claim_alarm_with_options_async(
        self,
        request: main_models.ClaimAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ClaimAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not DaraCore.is_null(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ClaimAlarm',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ClaimAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def claim_alarm(
        self,
        request: main_models.ClaimAlarmRequest,
    ) -> main_models.ClaimAlarmResponse:
        runtime = RuntimeOptions()
        return self.claim_alarm_with_options(request, runtime)

    async def claim_alarm_async(
        self,
        request: main_models.ClaimAlarmRequest,
    ) -> main_models.ClaimAlarmResponse:
        runtime = RuntimeOptions()
        return await self.claim_alarm_with_options_async(request, runtime)

    def close_alarm_with_options(
        self,
        request: main_models.CloseAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not DaraCore.is_null(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.solution):
            query['Solution'] = request.solution
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseAlarm',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_alarm_with_options_async(
        self,
        request: main_models.CloseAlarmRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CloseAlarmResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not DaraCore.is_null(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.solution):
            query['Solution'] = request.solution
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CloseAlarm',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CloseAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_alarm(
        self,
        request: main_models.CloseAlarmRequest,
    ) -> main_models.CloseAlarmResponse:
        runtime = RuntimeOptions()
        return self.close_alarm_with_options(request, runtime)

    async def close_alarm_async(
        self,
        request: main_models.CloseAlarmRequest,
    ) -> main_models.CloseAlarmResponse:
        runtime = RuntimeOptions()
        return await self.close_alarm_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigApp',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigApp',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.system_noc):
            query['SystemNoc'] = request.system_noc
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlertContact',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.system_noc):
            query['SystemNoc'] = request.system_noc
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAlertContact',
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def create_env_custom_job_with_options(
        self,
        request: main_models.CreateEnvCustomJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnvCustomJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.custom_job_name):
            query['CustomJobName'] = request.custom_job_name
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnvCustomJob',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnvCustomJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_env_custom_job_with_options_async(
        self,
        request: main_models.CreateEnvCustomJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnvCustomJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.custom_job_name):
            query['CustomJobName'] = request.custom_job_name
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnvCustomJob',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnvCustomJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_env_custom_job(
        self,
        request: main_models.CreateEnvCustomJobRequest,
    ) -> main_models.CreateEnvCustomJobResponse:
        runtime = RuntimeOptions()
        return self.create_env_custom_job_with_options(request, runtime)

    async def create_env_custom_job_async(
        self,
        request: main_models.CreateEnvCustomJobRequest,
    ) -> main_models.CreateEnvCustomJobResponse:
        runtime = RuntimeOptions()
        return await self.create_env_custom_job_with_options_async(request, runtime)

    def create_env_pod_monitor_with_options(
        self,
        request: main_models.CreateEnvPodMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnvPodMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnvPodMonitor',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnvPodMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_env_pod_monitor_with_options_async(
        self,
        request: main_models.CreateEnvPodMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnvPodMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnvPodMonitor',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnvPodMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_env_pod_monitor(
        self,
        request: main_models.CreateEnvPodMonitorRequest,
    ) -> main_models.CreateEnvPodMonitorResponse:
        runtime = RuntimeOptions()
        return self.create_env_pod_monitor_with_options(request, runtime)

    async def create_env_pod_monitor_async(
        self,
        request: main_models.CreateEnvPodMonitorRequest,
    ) -> main_models.CreateEnvPodMonitorResponse:
        runtime = RuntimeOptions()
        return await self.create_env_pod_monitor_with_options_async(request, runtime)

    def create_env_service_monitor_with_options(
        self,
        request: main_models.CreateEnvServiceMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnvServiceMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnvServiceMonitor',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnvServiceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_env_service_monitor_with_options_async(
        self,
        request: main_models.CreateEnvServiceMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnvServiceMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnvServiceMonitor',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnvServiceMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_env_service_monitor(
        self,
        request: main_models.CreateEnvServiceMonitorRequest,
    ) -> main_models.CreateEnvServiceMonitorResponse:
        runtime = RuntimeOptions()
        return self.create_env_service_monitor_with_options(request, runtime)

    async def create_env_service_monitor_async(
        self,
        request: main_models.CreateEnvServiceMonitorRequest,
    ) -> main_models.CreateEnvServiceMonitorResponse:
        runtime = RuntimeOptions()
        return await self.create_env_service_monitor_with_options_async(request, runtime)

    def create_environment_with_options(
        self,
        request: main_models.CreateEnvironmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnvironmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.bind_resource_id):
            query['BindResourceId'] = request.bind_resource_id
        if not DaraCore.is_null(request.environment_name):
            query['EnvironmentName'] = request.environment_name
        if not DaraCore.is_null(request.environment_sub_type):
            query['EnvironmentSubType'] = request.environment_sub_type
        if not DaraCore.is_null(request.environment_type):
            query['EnvironmentType'] = request.environment_type
        if not DaraCore.is_null(request.fee_package):
            query['FeePackage'] = request.fee_package
        if not DaraCore.is_null(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not DaraCore.is_null(request.init_environment):
            query['InitEnvironment'] = request.init_environment
        if not DaraCore.is_null(request.managed_type):
            query['ManagedType'] = request.managed_type
        if not DaraCore.is_null(request.prometheus_instance_id):
            query['PrometheusInstanceId'] = request.prometheus_instance_id
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
            action = 'CreateEnvironment',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_environment_with_options_async(
        self,
        request: main_models.CreateEnvironmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnvironmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.bind_resource_id):
            query['BindResourceId'] = request.bind_resource_id
        if not DaraCore.is_null(request.environment_name):
            query['EnvironmentName'] = request.environment_name
        if not DaraCore.is_null(request.environment_sub_type):
            query['EnvironmentSubType'] = request.environment_sub_type
        if not DaraCore.is_null(request.environment_type):
            query['EnvironmentType'] = request.environment_type
        if not DaraCore.is_null(request.fee_package):
            query['FeePackage'] = request.fee_package
        if not DaraCore.is_null(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not DaraCore.is_null(request.init_environment):
            query['InitEnvironment'] = request.init_environment
        if not DaraCore.is_null(request.managed_type):
            query['ManagedType'] = request.managed_type
        if not DaraCore.is_null(request.prometheus_instance_id):
            query['PrometheusInstanceId'] = request.prometheus_instance_id
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
            action = 'CreateEnvironment',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_environment(
        self,
        request: main_models.CreateEnvironmentRequest,
    ) -> main_models.CreateEnvironmentResponse:
        runtime = RuntimeOptions()
        return self.create_environment_with_options(request, runtime)

    async def create_environment_async(
        self,
        request: main_models.CreateEnvironmentRequest,
    ) -> main_models.CreateEnvironmentResponse:
        runtime = RuntimeOptions()
        return await self.create_environment_with_options_async(request, runtime)

    def create_grafana_workspace_with_options(
        self,
        tmp_req: main_models.CreateGrafanaWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGrafanaWorkspaceResponse:
        tmp_req.validate()
        request = main_models.CreateGrafanaWorkspaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.account_number):
            query['AccountNumber'] = request.account_number
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.custom_account_number):
            query['CustomAccountNumber'] = request.custom_account_number
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.grafana_version):
            query['GrafanaVersion'] = request.grafana_version
        if not DaraCore.is_null(request.grafana_workspace_edition):
            query['GrafanaWorkspaceEdition'] = request.grafana_workspace_edition
        if not DaraCore.is_null(request.grafana_workspace_name):
            query['GrafanaWorkspaceName'] = request.grafana_workspace_name
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGrafanaWorkspace',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGrafanaWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_grafana_workspace_with_options_async(
        self,
        tmp_req: main_models.CreateGrafanaWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGrafanaWorkspaceResponse:
        tmp_req.validate()
        request = main_models.CreateGrafanaWorkspaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.account_number):
            query['AccountNumber'] = request.account_number
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not DaraCore.is_null(request.custom_account_number):
            query['CustomAccountNumber'] = request.custom_account_number
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.grafana_version):
            query['GrafanaVersion'] = request.grafana_version
        if not DaraCore.is_null(request.grafana_workspace_edition):
            query['GrafanaWorkspaceEdition'] = request.grafana_workspace_edition
        if not DaraCore.is_null(request.grafana_workspace_name):
            query['GrafanaWorkspaceName'] = request.grafana_workspace_name
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGrafanaWorkspace',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGrafanaWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_grafana_workspace(
        self,
        request: main_models.CreateGrafanaWorkspaceRequest,
    ) -> main_models.CreateGrafanaWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.create_grafana_workspace_with_options(request, runtime)

    async def create_grafana_workspace_async(
        self,
        request: main_models.CreateGrafanaWorkspaceRequest,
    ) -> main_models.CreateGrafanaWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.create_grafana_workspace_with_options_async(request, runtime)

    def create_integration_with_options(
        self,
        request: main_models.CreateIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIntegrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.auto_recover):
            body['AutoRecover'] = request.auto_recover
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.integration_name):
            body['IntegrationName'] = request.integration_name
        if not DaraCore.is_null(request.integration_product_type):
            body['IntegrationProductType'] = request.integration_product_type
        if not DaraCore.is_null(request.recover_time):
            body['RecoverTime'] = request.recover_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_integration_with_options_async(
        self,
        request: main_models.CreateIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIntegrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.auto_recover):
            body['AutoRecover'] = request.auto_recover
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.integration_name):
            body['IntegrationName'] = request.integration_name
        if not DaraCore.is_null(request.integration_product_type):
            body['IntegrationProductType'] = request.integration_product_type
        if not DaraCore.is_null(request.recover_time):
            body['RecoverTime'] = request.recover_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_integration(
        self,
        request: main_models.CreateIntegrationRequest,
    ) -> main_models.CreateIntegrationResponse:
        runtime = RuntimeOptions()
        return self.create_integration_with_options(request, runtime)

    async def create_integration_async(
        self,
        request: main_models.CreateIntegrationRequest,
    ) -> main_models.CreateIntegrationResponse:
        runtime = RuntimeOptions()
        return await self.create_integration_with_options_async(request, runtime)

    def create_or_update_alert_rule_with_options(
        self,
        request: main_models.CreateOrUpdateAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateAlertRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_check_type):
            body['AlertCheckType'] = request.alert_check_type
        if not DaraCore.is_null(request.alert_group):
            body['AlertGroup'] = request.alert_group
        if not DaraCore.is_null(request.alert_id):
            body['AlertId'] = request.alert_id
        if not DaraCore.is_null(request.alert_name):
            body['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.alert_piplines):
            body['AlertPiplines'] = request.alert_piplines
        if not DaraCore.is_null(request.alert_rule_content):
            body['AlertRuleContent'] = request.alert_rule_content
        if not DaraCore.is_null(request.alert_status):
            body['AlertStatus'] = request.alert_status
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.annotations):
            body['Annotations'] = request.annotations
        if not DaraCore.is_null(request.auto_add_new_application):
            body['AutoAddNewApplication'] = request.auto_add_new_application
        if not DaraCore.is_null(request.auto_add_target_config):
            body['AutoAddTargetConfig'] = request.auto_add_target_config
        if not DaraCore.is_null(request.check_cycle):
            body['CheckCycle'] = request.check_cycle
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data_config):
            body['DataConfig'] = request.data_config
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.filters):
            body['Filters'] = request.filters
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.level):
            body['Level'] = request.level
        if not DaraCore.is_null(request.mark_tags):
            body['MarkTags'] = request.mark_tags
        if not DaraCore.is_null(request.message):
            body['Message'] = request.message
        if not DaraCore.is_null(request.metrics_key):
            body['MetricsKey'] = request.metrics_key
        if not DaraCore.is_null(request.metrics_type):
            body['MetricsType'] = request.metrics_type
        if not DaraCore.is_null(request.notice):
            body['Notice'] = request.notice
        if not DaraCore.is_null(request.notify_mode):
            body['NotifyMode'] = request.notify_mode
        if not DaraCore.is_null(request.notify_strategy):
            body['NotifyStrategy'] = request.notify_strategy
        if not DaraCore.is_null(request.pids):
            body['Pids'] = request.pids
        if not DaraCore.is_null(request.product):
            body['Product'] = request.product
        if not DaraCore.is_null(request.prom_ql):
            body['PromQL'] = request.prom_ql
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        if not DaraCore.is_null(request.aliyun_lang):
            body['aliyunLang'] = request.aliyun_lang
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateAlertRule',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_alert_rule_with_options_async(
        self,
        request: main_models.CreateOrUpdateAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateAlertRuleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.alert_check_type):
            body['AlertCheckType'] = request.alert_check_type
        if not DaraCore.is_null(request.alert_group):
            body['AlertGroup'] = request.alert_group
        if not DaraCore.is_null(request.alert_id):
            body['AlertId'] = request.alert_id
        if not DaraCore.is_null(request.alert_name):
            body['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.alert_piplines):
            body['AlertPiplines'] = request.alert_piplines
        if not DaraCore.is_null(request.alert_rule_content):
            body['AlertRuleContent'] = request.alert_rule_content
        if not DaraCore.is_null(request.alert_status):
            body['AlertStatus'] = request.alert_status
        if not DaraCore.is_null(request.alert_type):
            body['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.annotations):
            body['Annotations'] = request.annotations
        if not DaraCore.is_null(request.auto_add_new_application):
            body['AutoAddNewApplication'] = request.auto_add_new_application
        if not DaraCore.is_null(request.auto_add_target_config):
            body['AutoAddTargetConfig'] = request.auto_add_target_config
        if not DaraCore.is_null(request.check_cycle):
            body['CheckCycle'] = request.check_cycle
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.data_config):
            body['DataConfig'] = request.data_config
        if not DaraCore.is_null(request.duration):
            body['Duration'] = request.duration
        if not DaraCore.is_null(request.filters):
            body['Filters'] = request.filters
        if not DaraCore.is_null(request.labels):
            body['Labels'] = request.labels
        if not DaraCore.is_null(request.level):
            body['Level'] = request.level
        if not DaraCore.is_null(request.mark_tags):
            body['MarkTags'] = request.mark_tags
        if not DaraCore.is_null(request.message):
            body['Message'] = request.message
        if not DaraCore.is_null(request.metrics_key):
            body['MetricsKey'] = request.metrics_key
        if not DaraCore.is_null(request.metrics_type):
            body['MetricsType'] = request.metrics_type
        if not DaraCore.is_null(request.notice):
            body['Notice'] = request.notice
        if not DaraCore.is_null(request.notify_mode):
            body['NotifyMode'] = request.notify_mode
        if not DaraCore.is_null(request.notify_strategy):
            body['NotifyStrategy'] = request.notify_strategy
        if not DaraCore.is_null(request.pids):
            body['Pids'] = request.pids
        if not DaraCore.is_null(request.product):
            body['Product'] = request.product
        if not DaraCore.is_null(request.prom_ql):
            body['PromQL'] = request.prom_ql
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        if not DaraCore.is_null(request.aliyun_lang):
            body['aliyunLang'] = request.aliyun_lang
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateAlertRule',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_alert_rule(
        self,
        request: main_models.CreateOrUpdateAlertRuleRequest,
    ) -> main_models.CreateOrUpdateAlertRuleResponse:
        runtime = RuntimeOptions()
        return self.create_or_update_alert_rule_with_options(request, runtime)

    async def create_or_update_alert_rule_async(
        self,
        request: main_models.CreateOrUpdateAlertRuleRequest,
    ) -> main_models.CreateOrUpdateAlertRuleResponse:
        runtime = RuntimeOptions()
        return await self.create_or_update_alert_rule_with_options_async(request, runtime)

    def create_or_update_contact_with_options(
        self,
        request: main_models.CreateOrUpdateContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ding_robot_url):
            query['DingRobotUrl'] = request.ding_robot_url
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_name):
            body['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.corp_user_id):
            body['CorpUserId'] = request.corp_user_id
        if not DaraCore.is_null(request.email):
            body['Email'] = request.email
        if not DaraCore.is_null(request.is_email_verify):
            body['IsEmailVerify'] = request.is_email_verify
        if not DaraCore.is_null(request.phone):
            body['Phone'] = request.phone
        if not DaraCore.is_null(request.reissue_send_notice):
            body['ReissueSendNotice'] = request.reissue_send_notice
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateContact',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_contact_with_options_async(
        self,
        request: main_models.CreateOrUpdateContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ding_robot_url):
            query['DingRobotUrl'] = request.ding_robot_url
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.contact_name):
            body['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.corp_user_id):
            body['CorpUserId'] = request.corp_user_id
        if not DaraCore.is_null(request.email):
            body['Email'] = request.email
        if not DaraCore.is_null(request.is_email_verify):
            body['IsEmailVerify'] = request.is_email_verify
        if not DaraCore.is_null(request.phone):
            body['Phone'] = request.phone
        if not DaraCore.is_null(request.reissue_send_notice):
            body['ReissueSendNotice'] = request.reissue_send_notice
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateContact',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_contact(
        self,
        request: main_models.CreateOrUpdateContactRequest,
    ) -> main_models.CreateOrUpdateContactResponse:
        runtime = RuntimeOptions()
        return self.create_or_update_contact_with_options(request, runtime)

    async def create_or_update_contact_async(
        self,
        request: main_models.CreateOrUpdateContactRequest,
    ) -> main_models.CreateOrUpdateContactResponse:
        runtime = RuntimeOptions()
        return await self.create_or_update_contact_with_options_async(request, runtime)

    def create_or_update_contact_group_with_options(
        self,
        request: main_models.CreateOrUpdateContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateContactGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.contact_group_id):
            body['ContactGroupId'] = request.contact_group_id
        if not DaraCore.is_null(request.contact_group_name):
            body['ContactGroupName'] = request.contact_group_name
        if not DaraCore.is_null(request.contact_ids):
            body['ContactIds'] = request.contact_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateContactGroup',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_contact_group_with_options_async(
        self,
        request: main_models.CreateOrUpdateContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateContactGroupResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.contact_group_id):
            body['ContactGroupId'] = request.contact_group_id
        if not DaraCore.is_null(request.contact_group_name):
            body['ContactGroupName'] = request.contact_group_name
        if not DaraCore.is_null(request.contact_ids):
            body['ContactIds'] = request.contact_ids
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateContactGroup',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_contact_group(
        self,
        request: main_models.CreateOrUpdateContactGroupRequest,
    ) -> main_models.CreateOrUpdateContactGroupResponse:
        runtime = RuntimeOptions()
        return self.create_or_update_contact_group_with_options(request, runtime)

    async def create_or_update_contact_group_async(
        self,
        request: main_models.CreateOrUpdateContactGroupRequest,
    ) -> main_models.CreateOrUpdateContactGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_or_update_contact_group_with_options_async(request, runtime)

    def create_or_update_event_bridge_integration_with_options(
        self,
        request: main_models.CreateOrUpdateEventBridgeIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateEventBridgeIntegrationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_key):
            body['AccessKey'] = request.access_key
        if not DaraCore.is_null(request.access_secret):
            body['AccessSecret'] = request.access_secret
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.endpoint):
            body['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_bus_region_id):
            body['EventBusRegionId'] = request.event_bus_region_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.source):
            body['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateEventBridgeIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateEventBridgeIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_event_bridge_integration_with_options_async(
        self,
        request: main_models.CreateOrUpdateEventBridgeIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateEventBridgeIntegrationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.access_key):
            body['AccessKey'] = request.access_key
        if not DaraCore.is_null(request.access_secret):
            body['AccessSecret'] = request.access_secret
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.endpoint):
            body['Endpoint'] = request.endpoint
        if not DaraCore.is_null(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not DaraCore.is_null(request.event_bus_region_id):
            body['EventBusRegionId'] = request.event_bus_region_id
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.source):
            body['Source'] = request.source
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateEventBridgeIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateEventBridgeIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_event_bridge_integration(
        self,
        request: main_models.CreateOrUpdateEventBridgeIntegrationRequest,
    ) -> main_models.CreateOrUpdateEventBridgeIntegrationResponse:
        runtime = RuntimeOptions()
        return self.create_or_update_event_bridge_integration_with_options(request, runtime)

    async def create_or_update_event_bridge_integration_async(
        self,
        request: main_models.CreateOrUpdateEventBridgeIntegrationRequest,
    ) -> main_models.CreateOrUpdateEventBridgeIntegrationResponse:
        runtime = RuntimeOptions()
        return await self.create_or_update_event_bridge_integration_with_options_async(request, runtime)

    def create_or_update_imrobot_with_options(
        self,
        request: main_models.CreateOrUpdateIMRobotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateIMRobotResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.card_template):
            body['CardTemplate'] = request.card_template
        if not DaraCore.is_null(request.daily_noc):
            body['DailyNoc'] = request.daily_noc
        if not DaraCore.is_null(request.daily_noc_time):
            body['DailyNocTime'] = request.daily_noc_time
        if not DaraCore.is_null(request.ding_sign_key):
            body['DingSignKey'] = request.ding_sign_key
        if not DaraCore.is_null(request.enable_outgoing):
            body['EnableOutgoing'] = request.enable_outgoing
        if not DaraCore.is_null(request.robot_address):
            body['RobotAddress'] = request.robot_address
        if not DaraCore.is_null(request.robot_id):
            body['RobotId'] = request.robot_id
        if not DaraCore.is_null(request.robot_name):
            body['RobotName'] = request.robot_name
        if not DaraCore.is_null(request.token):
            body['Token'] = request.token
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateIMRobot',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateIMRobotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_imrobot_with_options_async(
        self,
        request: main_models.CreateOrUpdateIMRobotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateIMRobotResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.card_template):
            body['CardTemplate'] = request.card_template
        if not DaraCore.is_null(request.daily_noc):
            body['DailyNoc'] = request.daily_noc
        if not DaraCore.is_null(request.daily_noc_time):
            body['DailyNocTime'] = request.daily_noc_time
        if not DaraCore.is_null(request.ding_sign_key):
            body['DingSignKey'] = request.ding_sign_key
        if not DaraCore.is_null(request.enable_outgoing):
            body['EnableOutgoing'] = request.enable_outgoing
        if not DaraCore.is_null(request.robot_address):
            body['RobotAddress'] = request.robot_address
        if not DaraCore.is_null(request.robot_id):
            body['RobotId'] = request.robot_id
        if not DaraCore.is_null(request.robot_name):
            body['RobotName'] = request.robot_name
        if not DaraCore.is_null(request.token):
            body['Token'] = request.token
        if not DaraCore.is_null(request.type):
            body['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateIMRobot',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateIMRobotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_imrobot(
        self,
        request: main_models.CreateOrUpdateIMRobotRequest,
    ) -> main_models.CreateOrUpdateIMRobotResponse:
        runtime = RuntimeOptions()
        return self.create_or_update_imrobot_with_options(request, runtime)

    async def create_or_update_imrobot_async(
        self,
        request: main_models.CreateOrUpdateIMRobotRequest,
    ) -> main_models.CreateOrUpdateIMRobotResponse:
        runtime = RuntimeOptions()
        return await self.create_or_update_imrobot_with_options_async(request, runtime)

    def create_or_update_notification_policy_with_options(
        self,
        request: main_models.CreateOrUpdateNotificationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateNotificationPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.directed_mode):
            body['DirectedMode'] = request.directed_mode
        if not DaraCore.is_null(request.escalation_policy_id):
            body['EscalationPolicyId'] = request.escalation_policy_id
        if not DaraCore.is_null(request.group_rule):
            body['GroupRule'] = request.group_rule
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.integration_id):
            body['IntegrationId'] = request.integration_id
        if not DaraCore.is_null(request.matching_rules):
            body['MatchingRules'] = request.matching_rules
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.notify_rule):
            body['NotifyRule'] = request.notify_rule
        if not DaraCore.is_null(request.notify_template):
            body['NotifyTemplate'] = request.notify_template
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repeat):
            body['Repeat'] = request.repeat
        if not DaraCore.is_null(request.repeat_interval):
            body['RepeatInterval'] = request.repeat_interval
        if not DaraCore.is_null(request.send_recover_message):
            body['SendRecoverMessage'] = request.send_recover_message
        if not DaraCore.is_null(request.state):
            body['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateNotificationPolicy',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateNotificationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_notification_policy_with_options_async(
        self,
        request: main_models.CreateOrUpdateNotificationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateNotificationPolicyResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.directed_mode):
            body['DirectedMode'] = request.directed_mode
        if not DaraCore.is_null(request.escalation_policy_id):
            body['EscalationPolicyId'] = request.escalation_policy_id
        if not DaraCore.is_null(request.group_rule):
            body['GroupRule'] = request.group_rule
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.integration_id):
            body['IntegrationId'] = request.integration_id
        if not DaraCore.is_null(request.matching_rules):
            body['MatchingRules'] = request.matching_rules
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.notify_rule):
            body['NotifyRule'] = request.notify_rule
        if not DaraCore.is_null(request.notify_template):
            body['NotifyTemplate'] = request.notify_template
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repeat):
            body['Repeat'] = request.repeat
        if not DaraCore.is_null(request.repeat_interval):
            body['RepeatInterval'] = request.repeat_interval
        if not DaraCore.is_null(request.send_recover_message):
            body['SendRecoverMessage'] = request.send_recover_message
        if not DaraCore.is_null(request.state):
            body['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateNotificationPolicy',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateNotificationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_notification_policy(
        self,
        request: main_models.CreateOrUpdateNotificationPolicyRequest,
    ) -> main_models.CreateOrUpdateNotificationPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_or_update_notification_policy_with_options(request, runtime)

    async def create_or_update_notification_policy_async(
        self,
        request: main_models.CreateOrUpdateNotificationPolicyRequest,
    ) -> main_models.CreateOrUpdateNotificationPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_or_update_notification_policy_with_options_async(request, runtime)

    def create_or_update_silence_policy_with_options(
        self,
        request: main_models.CreateOrUpdateSilencePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateSilencePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effective_time_type):
            query['EffectiveTimeType'] = request.effective_time_type
        if not DaraCore.is_null(request.time_period):
            query['TimePeriod'] = request.time_period
        if not DaraCore.is_null(request.time_slots):
            query['TimeSlots'] = request.time_slots
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.matching_rules):
            body['MatchingRules'] = request.matching_rules
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.state):
            body['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateSilencePolicy',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateSilencePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_silence_policy_with_options_async(
        self,
        request: main_models.CreateOrUpdateSilencePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateSilencePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.effective_time_type):
            query['EffectiveTimeType'] = request.effective_time_type
        if not DaraCore.is_null(request.time_period):
            query['TimePeriod'] = request.time_period
        if not DaraCore.is_null(request.time_slots):
            query['TimeSlots'] = request.time_slots
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        if not DaraCore.is_null(request.matching_rules):
            body['MatchingRules'] = request.matching_rules
        if not DaraCore.is_null(request.name):
            body['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            body['RegionId'] = request.region_id
        if not DaraCore.is_null(request.state):
            body['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateSilencePolicy',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateSilencePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_silence_policy(
        self,
        request: main_models.CreateOrUpdateSilencePolicyRequest,
    ) -> main_models.CreateOrUpdateSilencePolicyResponse:
        runtime = RuntimeOptions()
        return self.create_or_update_silence_policy_with_options(request, runtime)

    async def create_or_update_silence_policy_async(
        self,
        request: main_models.CreateOrUpdateSilencePolicyRequest,
    ) -> main_models.CreateOrUpdateSilencePolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_or_update_silence_policy_with_options_async(request, runtime)

    def create_or_update_webhook_contact_with_options(
        self,
        request: main_models.CreateOrUpdateWebhookContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateWebhookContactResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.biz_headers):
            body['BizHeaders'] = request.biz_headers
        if not DaraCore.is_null(request.biz_params):
            body['BizParams'] = request.biz_params
        if not DaraCore.is_null(request.body):
            body['Body'] = request.body
        if not DaraCore.is_null(request.method):
            body['Method'] = request.method
        if not DaraCore.is_null(request.recover_body):
            body['RecoverBody'] = request.recover_body
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        if not DaraCore.is_null(request.webhook_id):
            body['WebhookId'] = request.webhook_id
        if not DaraCore.is_null(request.webhook_name):
            body['WebhookName'] = request.webhook_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateWebhookContact',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateWebhookContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_webhook_contact_with_options_async(
        self,
        request: main_models.CreateOrUpdateWebhookContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOrUpdateWebhookContactResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.biz_headers):
            body['BizHeaders'] = request.biz_headers
        if not DaraCore.is_null(request.biz_params):
            body['BizParams'] = request.biz_params
        if not DaraCore.is_null(request.body):
            body['Body'] = request.body
        if not DaraCore.is_null(request.method):
            body['Method'] = request.method
        if not DaraCore.is_null(request.recover_body):
            body['RecoverBody'] = request.recover_body
        if not DaraCore.is_null(request.url):
            body['Url'] = request.url
        if not DaraCore.is_null(request.webhook_id):
            body['WebhookId'] = request.webhook_id
        if not DaraCore.is_null(request.webhook_name):
            body['WebhookName'] = request.webhook_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateOrUpdateWebhookContact',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOrUpdateWebhookContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_webhook_contact(
        self,
        request: main_models.CreateOrUpdateWebhookContactRequest,
    ) -> main_models.CreateOrUpdateWebhookContactResponse:
        runtime = RuntimeOptions()
        return self.create_or_update_webhook_contact_with_options(request, runtime)

    async def create_or_update_webhook_contact_async(
        self,
        request: main_models.CreateOrUpdateWebhookContactRequest,
    ) -> main_models.CreateOrUpdateWebhookContactResponse:
        runtime = RuntimeOptions()
        return await self.create_or_update_webhook_contact_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrometheusAlertRule',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrometheusAlertRule',
            version = '2019-08-08',
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

    def create_prometheus_instance_with_options(
        self,
        request: main_models.CreatePrometheusInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrometheusInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all_sub_clusters_success):
            query['AllSubClustersSuccess'] = request.all_sub_clusters_success
        if not DaraCore.is_null(request.archive_duration):
            query['ArchiveDuration'] = request.archive_duration
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.grafana_instance_id):
            query['GrafanaInstanceId'] = request.grafana_instance_id
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.sub_clusters_json):
            query['SubClustersJson'] = request.sub_clusters_json
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrometheusInstance',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prometheus_instance_with_options_async(
        self,
        request: main_models.CreatePrometheusInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrometheusInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all_sub_clusters_success):
            query['AllSubClustersSuccess'] = request.all_sub_clusters_success
        if not DaraCore.is_null(request.archive_duration):
            query['ArchiveDuration'] = request.archive_duration
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.grafana_instance_id):
            query['GrafanaInstanceId'] = request.grafana_instance_id
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.sub_clusters_json):
            query['SubClustersJson'] = request.sub_clusters_json
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrometheusInstance',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrometheusInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prometheus_instance(
        self,
        request: main_models.CreatePrometheusInstanceRequest,
    ) -> main_models.CreatePrometheusInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_prometheus_instance_with_options(request, runtime)

    async def create_prometheus_instance_async(
        self,
        request: main_models.CreatePrometheusInstanceRequest,
    ) -> main_models.CreatePrometheusInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_prometheus_instance_with_options_async(request, runtime)

    def create_prometheus_monitoring_with_options(
        self,
        request: main_models.CreatePrometheusMonitoringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrometheusMonitoringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        body = {}
        if not DaraCore.is_null(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrometheusMonitoring',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrometheusMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prometheus_monitoring_with_options_async(
        self,
        request: main_models.CreatePrometheusMonitoringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrometheusMonitoringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        body = {}
        if not DaraCore.is_null(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrometheusMonitoring',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrometheusMonitoringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prometheus_monitoring(
        self,
        request: main_models.CreatePrometheusMonitoringRequest,
    ) -> main_models.CreatePrometheusMonitoringResponse:
        runtime = RuntimeOptions()
        return self.create_prometheus_monitoring_with_options(request, runtime)

    async def create_prometheus_monitoring_async(
        self,
        request: main_models.CreatePrometheusMonitoringRequest,
    ) -> main_models.CreatePrometheusMonitoringResponse:
        runtime = RuntimeOptions()
        return await self.create_prometheus_monitoring_with_options_async(request, runtime)

    def create_retcode_app_with_options(
        self,
        request: main_models.CreateRetcodeAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRetcodeAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        if not DaraCore.is_null(request.retcode_app_type):
            query['RetcodeAppType'] = request.retcode_app_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRetcodeApp',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        if not DaraCore.is_null(request.retcode_app_type):
            query['RetcodeAppType'] = request.retcode_app_type
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRetcodeApp',
            version = '2019-08-08',
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

    def create_rum_app_with_options(
        self,
        tmp_req: main_models.CreateRumAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRumAppResponse:
        tmp_req.validate()
        request = main_models.CreateRumAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.app_group):
            query['AppGroup'] = request.app_group
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.nick_name):
            query['NickName'] = request.nick_name
        if not DaraCore.is_null(request.package_name):
            query['PackageName'] = request.package_name
        if not DaraCore.is_null(request.real_region_id):
            query['RealRegionId'] = request.real_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.site_type):
            query['SiteType'] = request.site_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRumApp',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRumAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rum_app_with_options_async(
        self,
        tmp_req: main_models.CreateRumAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRumAppResponse:
        tmp_req.validate()
        request = main_models.CreateRumAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.app_group):
            query['AppGroup'] = request.app_group
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.nick_name):
            query['NickName'] = request.nick_name
        if not DaraCore.is_null(request.package_name):
            query['PackageName'] = request.package_name
        if not DaraCore.is_null(request.real_region_id):
            query['RealRegionId'] = request.real_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.site_type):
            query['SiteType'] = request.site_type
        if not DaraCore.is_null(request.source):
            query['Source'] = request.source
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRumApp',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRumAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rum_app(
        self,
        request: main_models.CreateRumAppRequest,
    ) -> main_models.CreateRumAppResponse:
        runtime = RuntimeOptions()
        return self.create_rum_app_with_options(request, runtime)

    async def create_rum_app_async(
        self,
        request: main_models.CreateRumAppRequest,
    ) -> main_models.CreateRumAppResponse:
        runtime = RuntimeOptions()
        return await self.create_rum_app_with_options_async(request, runtime)

    def create_rum_upload_file_url_with_options(
        self,
        request: main_models.CreateRumUploadFileUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRumUploadFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.content_type):
            query['ContentType'] = request.content_type
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.sourcemap_type):
            query['SourcemapType'] = request.sourcemap_type
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        if not DaraCore.is_null(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRumUploadFileUrl',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRumUploadFileUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rum_upload_file_url_with_options_async(
        self,
        request: main_models.CreateRumUploadFileUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRumUploadFileUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.content_type):
            query['ContentType'] = request.content_type
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.sourcemap_type):
            query['SourcemapType'] = request.sourcemap_type
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        if not DaraCore.is_null(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRumUploadFileUrl',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRumUploadFileUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rum_upload_file_url(
        self,
        request: main_models.CreateRumUploadFileUrlRequest,
    ) -> main_models.CreateRumUploadFileUrlResponse:
        runtime = RuntimeOptions()
        return self.create_rum_upload_file_url_with_options(request, runtime)

    async def create_rum_upload_file_url_async(
        self,
        request: main_models.CreateRumUploadFileUrlRequest,
    ) -> main_models.CreateRumUploadFileUrlResponse:
        runtime = RuntimeOptions()
        return await self.create_rum_upload_file_url_with_options_async(request, runtime)

    def create_synthetic_task_with_options(
        self,
        tmp_req: main_models.CreateSyntheticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSyntheticTaskResponse:
        tmp_req.validate()
        request = main_models.CreateSyntheticTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.common_param):
            request.common_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.common_param, 'CommonParam', 'json')
        if not DaraCore.is_null(tmp_req.download):
            request.download_shrink = Utils.array_to_string_with_specified_style(tmp_req.download, 'Download', 'json')
        if not DaraCore.is_null(tmp_req.extend_interval):
            request.extend_interval_shrink = Utils.array_to_string_with_specified_style(tmp_req.extend_interval, 'ExtendInterval', 'json')
        if not DaraCore.is_null(tmp_req.monitor_list):
            request.monitor_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.monitor_list, 'MonitorList', 'json')
        if not DaraCore.is_null(tmp_req.navigation):
            request.navigation_shrink = Utils.array_to_string_with_specified_style(tmp_req.navigation, 'Navigation', 'json')
        if not DaraCore.is_null(tmp_req.net):
            request.net_shrink = Utils.array_to_string_with_specified_style(tmp_req.net, 'Net', 'json')
        if not DaraCore.is_null(tmp_req.protocol):
            request.protocol_shrink = Utils.array_to_string_with_specified_style(tmp_req.protocol, 'Protocol', 'json')
        query = {}
        if not DaraCore.is_null(request.common_param_shrink):
            query['CommonParam'] = request.common_param_shrink
        if not DaraCore.is_null(request.download_shrink):
            query['Download'] = request.download_shrink
        if not DaraCore.is_null(request.extend_interval_shrink):
            query['ExtendInterval'] = request.extend_interval_shrink
        if not DaraCore.is_null(request.interval_time):
            query['IntervalTime'] = request.interval_time
        if not DaraCore.is_null(request.interval_type):
            query['IntervalType'] = request.interval_type
        if not DaraCore.is_null(request.ip_type):
            query['IpType'] = request.ip_type
        if not DaraCore.is_null(request.monitor_list_shrink):
            query['MonitorList'] = request.monitor_list_shrink
        if not DaraCore.is_null(request.navigation_shrink):
            query['Navigation'] = request.navigation_shrink
        if not DaraCore.is_null(request.net_shrink):
            query['Net'] = request.net_shrink
        if not DaraCore.is_null(request.protocol_shrink):
            query['Protocol'] = request.protocol_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.update_task):
            query['UpdateTask'] = request.update_task
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSyntheticTask',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_synthetic_task_with_options_async(
        self,
        tmp_req: main_models.CreateSyntheticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSyntheticTaskResponse:
        tmp_req.validate()
        request = main_models.CreateSyntheticTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.common_param):
            request.common_param_shrink = Utils.array_to_string_with_specified_style(tmp_req.common_param, 'CommonParam', 'json')
        if not DaraCore.is_null(tmp_req.download):
            request.download_shrink = Utils.array_to_string_with_specified_style(tmp_req.download, 'Download', 'json')
        if not DaraCore.is_null(tmp_req.extend_interval):
            request.extend_interval_shrink = Utils.array_to_string_with_specified_style(tmp_req.extend_interval, 'ExtendInterval', 'json')
        if not DaraCore.is_null(tmp_req.monitor_list):
            request.monitor_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.monitor_list, 'MonitorList', 'json')
        if not DaraCore.is_null(tmp_req.navigation):
            request.navigation_shrink = Utils.array_to_string_with_specified_style(tmp_req.navigation, 'Navigation', 'json')
        if not DaraCore.is_null(tmp_req.net):
            request.net_shrink = Utils.array_to_string_with_specified_style(tmp_req.net, 'Net', 'json')
        if not DaraCore.is_null(tmp_req.protocol):
            request.protocol_shrink = Utils.array_to_string_with_specified_style(tmp_req.protocol, 'Protocol', 'json')
        query = {}
        if not DaraCore.is_null(request.common_param_shrink):
            query['CommonParam'] = request.common_param_shrink
        if not DaraCore.is_null(request.download_shrink):
            query['Download'] = request.download_shrink
        if not DaraCore.is_null(request.extend_interval_shrink):
            query['ExtendInterval'] = request.extend_interval_shrink
        if not DaraCore.is_null(request.interval_time):
            query['IntervalTime'] = request.interval_time
        if not DaraCore.is_null(request.interval_type):
            query['IntervalType'] = request.interval_type
        if not DaraCore.is_null(request.ip_type):
            query['IpType'] = request.ip_type
        if not DaraCore.is_null(request.monitor_list_shrink):
            query['MonitorList'] = request.monitor_list_shrink
        if not DaraCore.is_null(request.navigation_shrink):
            query['Navigation'] = request.navigation_shrink
        if not DaraCore.is_null(request.net_shrink):
            query['Net'] = request.net_shrink
        if not DaraCore.is_null(request.protocol_shrink):
            query['Protocol'] = request.protocol_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.update_task):
            query['UpdateTask'] = request.update_task
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSyntheticTask',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSyntheticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_synthetic_task(
        self,
        request: main_models.CreateSyntheticTaskRequest,
    ) -> main_models.CreateSyntheticTaskResponse:
        runtime = RuntimeOptions()
        return self.create_synthetic_task_with_options(request, runtime)

    async def create_synthetic_task_async(
        self,
        request: main_models.CreateSyntheticTaskRequest,
    ) -> main_models.CreateSyntheticTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_synthetic_task_with_options_async(request, runtime)

    def create_timing_synthetic_task_with_options(
        self,
        tmp_req: main_models.CreateTimingSyntheticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTimingSyntheticTaskResponse:
        tmp_req.validate()
        request = main_models.CreateTimingSyntheticTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.available_assertions):
            request.available_assertions_shrink = Utils.array_to_string_with_specified_style(tmp_req.available_assertions, 'AvailableAssertions', 'json')
        if not DaraCore.is_null(tmp_req.common_setting):
            request.common_setting_shrink = Utils.array_to_string_with_specified_style(tmp_req.common_setting, 'CommonSetting', 'json')
        if not DaraCore.is_null(tmp_req.custom_period):
            request.custom_period_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_period, 'CustomPeriod', 'json')
        if not DaraCore.is_null(tmp_req.monitor_conf):
            request.monitor_conf_shrink = Utils.array_to_string_with_specified_style(tmp_req.monitor_conf, 'MonitorConf', 'json')
        if not DaraCore.is_null(tmp_req.monitors):
            request.monitors_shrink = Utils.array_to_string_with_specified_style(tmp_req.monitors, 'Monitors', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.available_assertions_shrink):
            query['AvailableAssertions'] = request.available_assertions_shrink
        if not DaraCore.is_null(request.common_setting_shrink):
            query['CommonSetting'] = request.common_setting_shrink
        if not DaraCore.is_null(request.custom_period_shrink):
            query['CustomPeriod'] = request.custom_period_shrink
        if not DaraCore.is_null(request.frequency):
            query['Frequency'] = request.frequency
        if not DaraCore.is_null(request.monitor_category):
            query['MonitorCategory'] = request.monitor_category
        if not DaraCore.is_null(request.monitor_conf_shrink):
            query['MonitorConf'] = request.monitor_conf_shrink
        if not DaraCore.is_null(request.monitors_shrink):
            query['Monitors'] = request.monitors_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTimingSyntheticTask',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTimingSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_timing_synthetic_task_with_options_async(
        self,
        tmp_req: main_models.CreateTimingSyntheticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTimingSyntheticTaskResponse:
        tmp_req.validate()
        request = main_models.CreateTimingSyntheticTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.available_assertions):
            request.available_assertions_shrink = Utils.array_to_string_with_specified_style(tmp_req.available_assertions, 'AvailableAssertions', 'json')
        if not DaraCore.is_null(tmp_req.common_setting):
            request.common_setting_shrink = Utils.array_to_string_with_specified_style(tmp_req.common_setting, 'CommonSetting', 'json')
        if not DaraCore.is_null(tmp_req.custom_period):
            request.custom_period_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_period, 'CustomPeriod', 'json')
        if not DaraCore.is_null(tmp_req.monitor_conf):
            request.monitor_conf_shrink = Utils.array_to_string_with_specified_style(tmp_req.monitor_conf, 'MonitorConf', 'json')
        if not DaraCore.is_null(tmp_req.monitors):
            request.monitors_shrink = Utils.array_to_string_with_specified_style(tmp_req.monitors, 'Monitors', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.available_assertions_shrink):
            query['AvailableAssertions'] = request.available_assertions_shrink
        if not DaraCore.is_null(request.common_setting_shrink):
            query['CommonSetting'] = request.common_setting_shrink
        if not DaraCore.is_null(request.custom_period_shrink):
            query['CustomPeriod'] = request.custom_period_shrink
        if not DaraCore.is_null(request.frequency):
            query['Frequency'] = request.frequency
        if not DaraCore.is_null(request.monitor_category):
            query['MonitorCategory'] = request.monitor_category
        if not DaraCore.is_null(request.monitor_conf_shrink):
            query['MonitorConf'] = request.monitor_conf_shrink
        if not DaraCore.is_null(request.monitors_shrink):
            query['Monitors'] = request.monitors_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTimingSyntheticTask',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTimingSyntheticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_timing_synthetic_task(
        self,
        request: main_models.CreateTimingSyntheticTaskRequest,
    ) -> main_models.CreateTimingSyntheticTaskResponse:
        runtime = RuntimeOptions()
        return self.create_timing_synthetic_task_with_options(request, runtime)

    async def create_timing_synthetic_task_async(
        self,
        request: main_models.CreateTimingSyntheticTaskRequest,
    ) -> main_models.CreateTimingSyntheticTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_timing_synthetic_task_with_options_async(request, runtime)

    def create_webhook_with_options(
        self,
        request: main_models.CreateWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWebhookResponse:
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
        if not DaraCore.is_null(request.recover_body):
            query['RecoverBody'] = request.recover_body
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWebhook',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_webhook_with_options_async(
        self,
        request: main_models.CreateWebhookRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateWebhookResponse:
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
        if not DaraCore.is_null(request.recover_body):
            query['RecoverBody'] = request.recover_body
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateWebhook',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_webhook(
        self,
        request: main_models.CreateWebhookRequest,
    ) -> main_models.CreateWebhookResponse:
        runtime = RuntimeOptions()
        return self.create_webhook_with_options(request, runtime)

    async def create_webhook_async(
        self,
        request: main_models.CreateWebhookRequest,
    ) -> main_models.CreateWebhookResponse:
        runtime = RuntimeOptions()
        return await self.create_webhook_with_options_async(request, runtime)

    def del_auth_token_with_options(
        self,
        request: main_models.DelAuthTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DelAuthTokenResponse:
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
            action = 'DelAuthToken',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DelAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def del_auth_token_with_options_async(
        self,
        request: main_models.DelAuthTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DelAuthTokenResponse:
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
            action = 'DelAuthToken',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DelAuthTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def del_auth_token(
        self,
        request: main_models.DelAuthTokenRequest,
    ) -> main_models.DelAuthTokenResponse:
        runtime = RuntimeOptions()
        return self.del_auth_token_with_options(request, runtime)

    async def del_auth_token_async(
        self,
        request: main_models.DelAuthTokenRequest,
    ) -> main_models.DelAuthTokenResponse:
        runtime = RuntimeOptions()
        return await self.del_auth_token_with_options_async(request, runtime)

    def delete_addon_release_with_options(
        self,
        request: main_models.DeleteAddonReleaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAddonReleaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['AddonName'] = request.addon_name
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.release_name):
            query['ReleaseName'] = request.release_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAddonRelease',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAddonReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_addon_release_with_options_async(
        self,
        request: main_models.DeleteAddonReleaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAddonReleaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['AddonName'] = request.addon_name
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.release_name):
            query['ReleaseName'] = request.release_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAddonRelease',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAddonReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_addon_release(
        self,
        request: main_models.DeleteAddonReleaseRequest,
    ) -> main_models.DeleteAddonReleaseResponse:
        runtime = RuntimeOptions()
        return self.delete_addon_release_with_options(request, runtime)

    async def delete_addon_release_async(
        self,
        request: main_models.DeleteAddonReleaseRequest,
    ) -> main_models.DeleteAddonReleaseResponse:
        runtime = RuntimeOptions()
        return await self.delete_addon_release_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def delete_alert_rule_with_options(
        self,
        request: main_models.DeleteAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertRule',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_rule_with_options_async(
        self,
        request: main_models.DeleteAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAlertRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAlertRule',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_rule(
        self,
        request: main_models.DeleteAlertRuleRequest,
    ) -> main_models.DeleteAlertRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_alert_rule_with_options(request, runtime)

    async def delete_alert_rule_async(
        self,
        request: main_models.DeleteAlertRuleRequest,
    ) -> main_models.DeleteAlertRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_alert_rule_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def delete_app_list_with_options(
        self,
        request: main_models.DeleteAppListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pids):
            query['Pids'] = request.pids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppList',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_list_with_options_async(
        self,
        request: main_models.DeleteAppListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAppListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pids):
            query['Pids'] = request.pids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAppList',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAppListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_list(
        self,
        request: main_models.DeleteAppListRequest,
    ) -> main_models.DeleteAppListResponse:
        runtime = RuntimeOptions()
        return self.delete_app_list_with_options(request, runtime)

    async def delete_app_list_async(
        self,
        request: main_models.DeleteAppListRequest,
    ) -> main_models.DeleteAppListResponse:
        runtime = RuntimeOptions()
        return await self.delete_app_list_with_options_async(request, runtime)

    def delete_cms_exporter_with_options(
        self,
        request: main_models.DeleteCmsExporterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCmsExporterResponse:
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
            action = 'DeleteCmsExporter',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCmsExporterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cms_exporter_with_options_async(
        self,
        request: main_models.DeleteCmsExporterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCmsExporterResponse:
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
            action = 'DeleteCmsExporter',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCmsExporterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cms_exporter(
        self,
        request: main_models.DeleteCmsExporterRequest,
    ) -> main_models.DeleteCmsExporterResponse:
        runtime = RuntimeOptions()
        return self.delete_cms_exporter_with_options(request, runtime)

    async def delete_cms_exporter_async(
        self,
        request: main_models.DeleteCmsExporterRequest,
    ) -> main_models.DeleteCmsExporterResponse:
        runtime = RuntimeOptions()
        return await self.delete_cms_exporter_with_options_async(request, runtime)

    def delete_contact_with_options(
        self,
        request: main_models.DeleteContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContact',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_with_options_async(
        self,
        request: main_models.DeleteContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_id):
            query['ContactId'] = request.contact_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContact',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact(
        self,
        request: main_models.DeleteContactRequest,
    ) -> main_models.DeleteContactResponse:
        runtime = RuntimeOptions()
        return self.delete_contact_with_options(request, runtime)

    async def delete_contact_async(
        self,
        request: main_models.DeleteContactRequest,
    ) -> main_models.DeleteContactResponse:
        runtime = RuntimeOptions()
        return await self.delete_contact_with_options_async(request, runtime)

    def delete_contact_group_with_options(
        self,
        request: main_models.DeleteContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_id):
            query['ContactGroupId'] = request.contact_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContactGroup',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_group_with_options_async(
        self,
        request: main_models.DeleteContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_id):
            query['ContactGroupId'] = request.contact_group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContactGroup',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact_group(
        self,
        request: main_models.DeleteContactGroupRequest,
    ) -> main_models.DeleteContactGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_contact_group_with_options(request, runtime)

    async def delete_contact_group_async(
        self,
        request: main_models.DeleteContactGroupRequest,
    ) -> main_models.DeleteContactGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_contact_group_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def delete_env_custom_job_with_options(
        self,
        request: main_models.DeleteEnvCustomJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnvCustomJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_job_name):
            query['CustomJobName'] = request.custom_job_name
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnvCustomJob',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnvCustomJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_env_custom_job_with_options_async(
        self,
        request: main_models.DeleteEnvCustomJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnvCustomJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_job_name):
            query['CustomJobName'] = request.custom_job_name
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnvCustomJob',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnvCustomJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_env_custom_job(
        self,
        request: main_models.DeleteEnvCustomJobRequest,
    ) -> main_models.DeleteEnvCustomJobResponse:
        runtime = RuntimeOptions()
        return self.delete_env_custom_job_with_options(request, runtime)

    async def delete_env_custom_job_async(
        self,
        request: main_models.DeleteEnvCustomJobRequest,
    ) -> main_models.DeleteEnvCustomJobResponse:
        runtime = RuntimeOptions()
        return await self.delete_env_custom_job_with_options_async(request, runtime)

    def delete_env_pod_monitor_with_options(
        self,
        request: main_models.DeleteEnvPodMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnvPodMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.pod_monitor_name):
            query['PodMonitorName'] = request.pod_monitor_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnvPodMonitor',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnvPodMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_env_pod_monitor_with_options_async(
        self,
        request: main_models.DeleteEnvPodMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnvPodMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.pod_monitor_name):
            query['PodMonitorName'] = request.pod_monitor_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnvPodMonitor',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnvPodMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_env_pod_monitor(
        self,
        request: main_models.DeleteEnvPodMonitorRequest,
    ) -> main_models.DeleteEnvPodMonitorResponse:
        runtime = RuntimeOptions()
        return self.delete_env_pod_monitor_with_options(request, runtime)

    async def delete_env_pod_monitor_async(
        self,
        request: main_models.DeleteEnvPodMonitorRequest,
    ) -> main_models.DeleteEnvPodMonitorResponse:
        runtime = RuntimeOptions()
        return await self.delete_env_pod_monitor_with_options_async(request, runtime)

    def delete_env_service_monitor_with_options(
        self,
        request: main_models.DeleteEnvServiceMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnvServiceMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_monitor_name):
            query['ServiceMonitorName'] = request.service_monitor_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnvServiceMonitor',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnvServiceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_env_service_monitor_with_options_async(
        self,
        request: main_models.DeleteEnvServiceMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnvServiceMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_monitor_name):
            query['ServiceMonitorName'] = request.service_monitor_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnvServiceMonitor',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnvServiceMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_env_service_monitor(
        self,
        request: main_models.DeleteEnvServiceMonitorRequest,
    ) -> main_models.DeleteEnvServiceMonitorResponse:
        runtime = RuntimeOptions()
        return self.delete_env_service_monitor_with_options(request, runtime)

    async def delete_env_service_monitor_async(
        self,
        request: main_models.DeleteEnvServiceMonitorRequest,
    ) -> main_models.DeleteEnvServiceMonitorResponse:
        runtime = RuntimeOptions()
        return await self.delete_env_service_monitor_with_options_async(request, runtime)

    def delete_environment_with_options(
        self,
        request: main_models.DeleteEnvironmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnvironmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_prom_instance):
            query['DeletePromInstance'] = request.delete_prom_instance
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnvironment',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_environment_with_options_async(
        self,
        request: main_models.DeleteEnvironmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnvironmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_prom_instance):
            query['DeletePromInstance'] = request.delete_prom_instance
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnvironment',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_environment(
        self,
        request: main_models.DeleteEnvironmentRequest,
    ) -> main_models.DeleteEnvironmentResponse:
        runtime = RuntimeOptions()
        return self.delete_environment_with_options(request, runtime)

    async def delete_environment_async(
        self,
        request: main_models.DeleteEnvironmentRequest,
    ) -> main_models.DeleteEnvironmentResponse:
        runtime = RuntimeOptions()
        return await self.delete_environment_with_options_async(request, runtime)

    def delete_environment_feature_with_options(
        self,
        request: main_models.DeleteEnvironmentFeatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnvironmentFeatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnvironmentFeature',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnvironmentFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_environment_feature_with_options_async(
        self,
        request: main_models.DeleteEnvironmentFeatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnvironmentFeatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnvironmentFeature',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEnvironmentFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_environment_feature(
        self,
        request: main_models.DeleteEnvironmentFeatureRequest,
    ) -> main_models.DeleteEnvironmentFeatureResponse:
        runtime = RuntimeOptions()
        return self.delete_environment_feature_with_options(request, runtime)

    async def delete_environment_feature_async(
        self,
        request: main_models.DeleteEnvironmentFeatureRequest,
    ) -> main_models.DeleteEnvironmentFeatureResponse:
        runtime = RuntimeOptions()
        return await self.delete_environment_feature_with_options_async(request, runtime)

    def delete_event_bridge_integration_with_options(
        self,
        request: main_models.DeleteEventBridgeIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventBridgeIntegrationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventBridgeIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventBridgeIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_bridge_integration_with_options_async(
        self,
        request: main_models.DeleteEventBridgeIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventBridgeIntegrationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventBridgeIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventBridgeIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_bridge_integration(
        self,
        request: main_models.DeleteEventBridgeIntegrationRequest,
    ) -> main_models.DeleteEventBridgeIntegrationResponse:
        runtime = RuntimeOptions()
        return self.delete_event_bridge_integration_with_options(request, runtime)

    async def delete_event_bridge_integration_async(
        self,
        request: main_models.DeleteEventBridgeIntegrationRequest,
    ) -> main_models.DeleteEventBridgeIntegrationResponse:
        runtime = RuntimeOptions()
        return await self.delete_event_bridge_integration_with_options_async(request, runtime)

    def delete_grafana_resource_with_options(
        self,
        request: main_models.DeleteGrafanaResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGrafanaResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGrafanaResource',
            version = '2019-08-08',
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
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGrafanaResource',
            version = '2019-08-08',
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

    def delete_grafana_workspace_with_options(
        self,
        request: main_models.DeleteGrafanaWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGrafanaWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGrafanaWorkspace',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGrafanaWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_grafana_workspace_with_options_async(
        self,
        request: main_models.DeleteGrafanaWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGrafanaWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGrafanaWorkspace',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGrafanaWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_grafana_workspace(
        self,
        request: main_models.DeleteGrafanaWorkspaceRequest,
    ) -> main_models.DeleteGrafanaWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.delete_grafana_workspace_with_options(request, runtime)

    async def delete_grafana_workspace_async(
        self,
        request: main_models.DeleteGrafanaWorkspaceRequest,
    ) -> main_models.DeleteGrafanaWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.delete_grafana_workspace_with_options_async(request, runtime)

    def delete_imrobot_with_options(
        self,
        request: main_models.DeleteIMRobotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIMRobotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.robot_id):
            query['RobotId'] = request.robot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIMRobot',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIMRobotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_imrobot_with_options_async(
        self,
        request: main_models.DeleteIMRobotRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIMRobotResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.robot_id):
            query['RobotId'] = request.robot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIMRobot',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIMRobotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_imrobot(
        self,
        request: main_models.DeleteIMRobotRequest,
    ) -> main_models.DeleteIMRobotResponse:
        runtime = RuntimeOptions()
        return self.delete_imrobot_with_options(request, runtime)

    async def delete_imrobot_async(
        self,
        request: main_models.DeleteIMRobotRequest,
    ) -> main_models.DeleteIMRobotResponse:
        runtime = RuntimeOptions()
        return await self.delete_imrobot_with_options_async(request, runtime)

    def delete_integration_with_options(
        self,
        request: main_models.DeleteIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIntegrationResponse:
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
            action = 'DeleteIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_integration_with_options_async(
        self,
        request: main_models.DeleteIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIntegrationResponse:
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
            action = 'DeleteIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_integration(
        self,
        request: main_models.DeleteIntegrationRequest,
    ) -> main_models.DeleteIntegrationResponse:
        runtime = RuntimeOptions()
        return self.delete_integration_with_options(request, runtime)

    async def delete_integration_async(
        self,
        request: main_models.DeleteIntegrationRequest,
    ) -> main_models.DeleteIntegrationResponse:
        runtime = RuntimeOptions()
        return await self.delete_integration_with_options_async(request, runtime)

    def delete_integrations_with_options(
        self,
        request: main_models.DeleteIntegrationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIntegrationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIntegrations',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIntegrationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_integrations_with_options_async(
        self,
        request: main_models.DeleteIntegrationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteIntegrationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteIntegrations',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteIntegrationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_integrations(
        self,
        request: main_models.DeleteIntegrationsRequest,
    ) -> main_models.DeleteIntegrationsResponse:
        runtime = RuntimeOptions()
        return self.delete_integrations_with_options(request, runtime)

    async def delete_integrations_async(
        self,
        request: main_models.DeleteIntegrationsRequest,
    ) -> main_models.DeleteIntegrationsResponse:
        runtime = RuntimeOptions()
        return await self.delete_integrations_with_options_async(request, runtime)

    def delete_notification_policy_with_options(
        self,
        request: main_models.DeleteNotificationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNotificationPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNotificationPolicy',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNotificationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_notification_policy_with_options_async(
        self,
        request: main_models.DeleteNotificationPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteNotificationPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteNotificationPolicy',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteNotificationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_notification_policy(
        self,
        request: main_models.DeleteNotificationPolicyRequest,
    ) -> main_models.DeleteNotificationPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_notification_policy_with_options(request, runtime)

    async def delete_notification_policy_async(
        self,
        request: main_models.DeleteNotificationPolicyRequest,
    ) -> main_models.DeleteNotificationPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_notification_policy_with_options_async(request, runtime)

    def delete_prometheus_alert_rule_with_options(
        self,
        request: main_models.DeletePrometheusAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrometheusAlertRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrometheusAlertRule',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrometheusAlertRule',
            version = '2019-08-08',
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

    def delete_prometheus_global_view_with_options(
        self,
        request: main_models.DeletePrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_prometheus_global_view_with_options_async(
        self,
        request: main_models.DeletePrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_prometheus_global_view(
        self,
        request: main_models.DeletePrometheusGlobalViewRequest,
    ) -> main_models.DeletePrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return self.delete_prometheus_global_view_with_options(request, runtime)

    async def delete_prometheus_global_view_async(
        self,
        request: main_models.DeletePrometheusGlobalViewRequest,
    ) -> main_models.DeletePrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return await self.delete_prometheus_global_view_with_options_async(request, runtime)

    def delete_prometheus_integration_with_options(
        self,
        request: main_models.DeletePrometheusIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrometheusIntegrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrometheusIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrometheusIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_prometheus_integration_with_options_async(
        self,
        request: main_models.DeletePrometheusIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrometheusIntegrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrometheusIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrometheusIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_prometheus_integration(
        self,
        request: main_models.DeletePrometheusIntegrationRequest,
    ) -> main_models.DeletePrometheusIntegrationResponse:
        runtime = RuntimeOptions()
        return self.delete_prometheus_integration_with_options(request, runtime)

    async def delete_prometheus_integration_async(
        self,
        request: main_models.DeletePrometheusIntegrationRequest,
    ) -> main_models.DeletePrometheusIntegrationResponse:
        runtime = RuntimeOptions()
        return await self.delete_prometheus_integration_with_options_async(request, runtime)

    def delete_prometheus_monitoring_with_options(
        self,
        request: main_models.DeletePrometheusMonitoringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrometheusMonitoringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrometheusMonitoring',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrometheusMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_prometheus_monitoring_with_options_async(
        self,
        request: main_models.DeletePrometheusMonitoringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrometheusMonitoringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePrometheusMonitoring',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePrometheusMonitoringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_prometheus_monitoring(
        self,
        request: main_models.DeletePrometheusMonitoringRequest,
    ) -> main_models.DeletePrometheusMonitoringResponse:
        runtime = RuntimeOptions()
        return self.delete_prometheus_monitoring_with_options(request, runtime)

    async def delete_prometheus_monitoring_async(
        self,
        request: main_models.DeletePrometheusMonitoringRequest,
    ) -> main_models.DeletePrometheusMonitoringResponse:
        runtime = RuntimeOptions()
        return await self.delete_prometheus_monitoring_with_options_async(request, runtime)

    def delete_retcode_app_with_options(
        self,
        request: main_models.DeleteRetcodeAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRetcodeAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRetcodeApp',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRetcodeApp',
            version = '2019-08-08',
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

    def delete_rum_app_with_options(
        self,
        request: main_models.DeleteRumAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRumAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_group):
            query['AppGroup'] = request.app_group
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.real_region_id):
            query['RealRegionId'] = request.real_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRumApp',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRumAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rum_app_with_options_async(
        self,
        request: main_models.DeleteRumAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRumAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_group):
            query['AppGroup'] = request.app_group
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.real_region_id):
            query['RealRegionId'] = request.real_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRumApp',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRumAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rum_app(
        self,
        request: main_models.DeleteRumAppRequest,
    ) -> main_models.DeleteRumAppResponse:
        runtime = RuntimeOptions()
        return self.delete_rum_app_with_options(request, runtime)

    async def delete_rum_app_async(
        self,
        request: main_models.DeleteRumAppRequest,
    ) -> main_models.DeleteRumAppResponse:
        runtime = RuntimeOptions()
        return await self.delete_rum_app_with_options_async(request, runtime)

    def delete_rum_upload_file_with_options(
        self,
        request: main_models.DeleteRumUploadFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRumUploadFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_items):
            query['BatchItems'] = request.batch_items
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        if not DaraCore.is_null(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRumUploadFile',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRumUploadFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_rum_upload_file_with_options_async(
        self,
        request: main_models.DeleteRumUploadFileRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRumUploadFileResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.batch_items):
            query['BatchItems'] = request.batch_items
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        if not DaraCore.is_null(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRumUploadFile',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRumUploadFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_rum_upload_file(
        self,
        request: main_models.DeleteRumUploadFileRequest,
    ) -> main_models.DeleteRumUploadFileResponse:
        runtime = RuntimeOptions()
        return self.delete_rum_upload_file_with_options(request, runtime)

    async def delete_rum_upload_file_async(
        self,
        request: main_models.DeleteRumUploadFileRequest,
    ) -> main_models.DeleteRumUploadFileResponse:
        runtime = RuntimeOptions()
        return await self.delete_rum_upload_file_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def delete_silence_policy_with_options(
        self,
        request: main_models.DeleteSilencePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSilencePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSilencePolicy',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSilencePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_silence_policy_with_options_async(
        self,
        request: main_models.DeleteSilencePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSilencePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSilencePolicy',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSilencePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_silence_policy(
        self,
        request: main_models.DeleteSilencePolicyRequest,
    ) -> main_models.DeleteSilencePolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_silence_policy_with_options(request, runtime)

    async def delete_silence_policy_async(
        self,
        request: main_models.DeleteSilencePolicyRequest,
    ) -> main_models.DeleteSilencePolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_silence_policy_with_options_async(request, runtime)

    def delete_source_map_with_options(
        self,
        tmp_req: main_models.DeleteSourceMapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSourceMapResponse:
        tmp_req.validate()
        request = main_models.DeleteSourceMapShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.fid_list):
            request.fid_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.fid_list, 'FidList', 'json')
        query = {}
        if not DaraCore.is_null(request.fid_list_shrink):
            query['FidList'] = request.fid_list_shrink
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSourceMap',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSourceMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_source_map_with_options_async(
        self,
        tmp_req: main_models.DeleteSourceMapRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSourceMapResponse:
        tmp_req.validate()
        request = main_models.DeleteSourceMapShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.fid_list):
            request.fid_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.fid_list, 'FidList', 'json')
        query = {}
        if not DaraCore.is_null(request.fid_list_shrink):
            query['FidList'] = request.fid_list_shrink
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSourceMap',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSourceMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_source_map(
        self,
        request: main_models.DeleteSourceMapRequest,
    ) -> main_models.DeleteSourceMapResponse:
        runtime = RuntimeOptions()
        return self.delete_source_map_with_options(request, runtime)

    async def delete_source_map_async(
        self,
        request: main_models.DeleteSourceMapRequest,
    ) -> main_models.DeleteSourceMapResponse:
        runtime = RuntimeOptions()
        return await self.delete_source_map_with_options_async(request, runtime)

    def delete_synthetic_task_with_options(
        self,
        request: main_models.DeleteSyntheticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSyntheticTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSyntheticTask',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_synthetic_task_with_options_async(
        self,
        request: main_models.DeleteSyntheticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSyntheticTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSyntheticTask',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSyntheticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_synthetic_task(
        self,
        request: main_models.DeleteSyntheticTaskRequest,
    ) -> main_models.DeleteSyntheticTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_synthetic_task_with_options(request, runtime)

    async def delete_synthetic_task_async(
        self,
        request: main_models.DeleteSyntheticTaskRequest,
    ) -> main_models.DeleteSyntheticTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_synthetic_task_with_options_async(request, runtime)

    def delete_timing_synthetic_task_with_options(
        self,
        request: main_models.DeleteTimingSyntheticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTimingSyntheticTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTimingSyntheticTask',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTimingSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_timing_synthetic_task_with_options_async(
        self,
        request: main_models.DeleteTimingSyntheticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTimingSyntheticTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTimingSyntheticTask',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTimingSyntheticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_timing_synthetic_task(
        self,
        request: main_models.DeleteTimingSyntheticTaskRequest,
    ) -> main_models.DeleteTimingSyntheticTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_timing_synthetic_task_with_options(request, runtime)

    async def delete_timing_synthetic_task_async(
        self,
        request: main_models.DeleteTimingSyntheticTaskRequest,
    ) -> main_models.DeleteTimingSyntheticTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_timing_synthetic_task_with_options_async(request, runtime)

    def delete_trace_app_with_options(
        self,
        tmp_req: main_models.DeleteTraceAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTraceAppResponse:
        tmp_req.validate()
        request = main_models.DeleteTraceAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_reason):
            request.delete_reason_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_reason, 'DeleteReason', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.delete_reason_shrink):
            query['DeleteReason'] = request.delete_reason_shrink
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
            version = '2019-08-08',
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
        tmp_req: main_models.DeleteTraceAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTraceAppResponse:
        tmp_req.validate()
        request = main_models.DeleteTraceAppShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.delete_reason):
            request.delete_reason_shrink = Utils.array_to_string_with_specified_style(tmp_req.delete_reason, 'DeleteReason', 'json')
        query = {}
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.delete_reason_shrink):
            query['DeleteReason'] = request.delete_reason_shrink
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
            version = '2019-08-08',
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

    def delete_webhook_contact_with_options(
        self,
        request: main_models.DeleteWebhookContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebhookContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.webhook_id):
            query['WebhookId'] = request.webhook_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebhookContact',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebhookContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_webhook_contact_with_options_async(
        self,
        request: main_models.DeleteWebhookContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteWebhookContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.webhook_id):
            query['WebhookId'] = request.webhook_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteWebhookContact',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteWebhookContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_webhook_contact(
        self,
        request: main_models.DeleteWebhookContactRequest,
    ) -> main_models.DeleteWebhookContactResponse:
        runtime = RuntimeOptions()
        return self.delete_webhook_contact_with_options(request, runtime)

    async def delete_webhook_contact_async(
        self,
        request: main_models.DeleteWebhookContactRequest,
    ) -> main_models.DeleteWebhookContactResponse:
        runtime = RuntimeOptions()
        return await self.delete_webhook_contact_with_options_async(request, runtime)

    def describe_addon_metrics_with_options(
        self,
        request: main_models.DescribeAddonMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAddonMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.environment_type):
            query['EnvironmentType'] = request.environment_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAddonMetrics',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAddonMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_addon_metrics_with_options_async(
        self,
        request: main_models.DescribeAddonMetricsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAddonMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.environment_type):
            query['EnvironmentType'] = request.environment_type
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAddonMetrics',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAddonMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_addon_metrics(
        self,
        request: main_models.DescribeAddonMetricsRequest,
    ) -> main_models.DescribeAddonMetricsResponse:
        runtime = RuntimeOptions()
        return self.describe_addon_metrics_with_options(request, runtime)

    async def describe_addon_metrics_async(
        self,
        request: main_models.DescribeAddonMetricsRequest,
    ) -> main_models.DescribeAddonMetricsResponse:
        runtime = RuntimeOptions()
        return await self.describe_addon_metrics_with_options_async(request, runtime)

    def describe_addon_release_with_options(
        self,
        request: main_models.DescribeAddonReleaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAddonReleaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.release_name):
            query['ReleaseName'] = request.release_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAddonRelease',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAddonReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_addon_release_with_options_async(
        self,
        request: main_models.DescribeAddonReleaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAddonReleaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.release_name):
            query['ReleaseName'] = request.release_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAddonRelease',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAddonReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_addon_release(
        self,
        request: main_models.DescribeAddonReleaseRequest,
    ) -> main_models.DescribeAddonReleaseResponse:
        runtime = RuntimeOptions()
        return self.describe_addon_release_with_options(request, runtime)

    async def describe_addon_release_async(
        self,
        request: main_models.DescribeAddonReleaseRequest,
    ) -> main_models.DescribeAddonReleaseResponse:
        runtime = RuntimeOptions()
        return await self.describe_addon_release_with_options_async(request, runtime)

    def describe_contact_groups_with_options(
        self,
        request: main_models.DescribeContactGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeContactGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeContactGroups',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeContactGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_contact_groups_with_options_async(
        self,
        request: main_models.DescribeContactGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeContactGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeContactGroups',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeContactGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_contact_groups(
        self,
        request: main_models.DescribeContactGroupsRequest,
    ) -> main_models.DescribeContactGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_contact_groups_with_options(request, runtime)

    async def describe_contact_groups_async(
        self,
        request: main_models.DescribeContactGroupsRequest,
    ) -> main_models.DescribeContactGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_contact_groups_with_options_async(request, runtime)

    def describe_contacts_with_options(
        self,
        request: main_models.DescribeContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeContactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeContacts',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_contacts_with_options_async(
        self,
        request: main_models.DescribeContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeContactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.email):
            query['Email'] = request.email
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.phone):
            query['Phone'] = request.phone
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeContacts',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_contacts(
        self,
        request: main_models.DescribeContactsRequest,
    ) -> main_models.DescribeContactsResponse:
        runtime = RuntimeOptions()
        return self.describe_contacts_with_options(request, runtime)

    async def describe_contacts_async(
        self,
        request: main_models.DescribeContactsRequest,
    ) -> main_models.DescribeContactsResponse:
        runtime = RuntimeOptions()
        return await self.describe_contacts_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def describe_env_custom_job_with_options(
        self,
        request: main_models.DescribeEnvCustomJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnvCustomJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_job_name):
            query['CustomJobName'] = request.custom_job_name
        if not DaraCore.is_null(request.encrypt_yaml):
            query['EncryptYaml'] = request.encrypt_yaml
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnvCustomJob',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnvCustomJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_env_custom_job_with_options_async(
        self,
        request: main_models.DescribeEnvCustomJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnvCustomJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.custom_job_name):
            query['CustomJobName'] = request.custom_job_name
        if not DaraCore.is_null(request.encrypt_yaml):
            query['EncryptYaml'] = request.encrypt_yaml
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnvCustomJob',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnvCustomJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_env_custom_job(
        self,
        request: main_models.DescribeEnvCustomJobRequest,
    ) -> main_models.DescribeEnvCustomJobResponse:
        runtime = RuntimeOptions()
        return self.describe_env_custom_job_with_options(request, runtime)

    async def describe_env_custom_job_async(
        self,
        request: main_models.DescribeEnvCustomJobRequest,
    ) -> main_models.DescribeEnvCustomJobResponse:
        runtime = RuntimeOptions()
        return await self.describe_env_custom_job_with_options_async(request, runtime)

    def describe_env_drop_metrics_rule_with_options(
        self,
        request: main_models.DescribeEnvDropMetricsRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnvDropMetricsRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnvDropMetricsRule',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnvDropMetricsRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_env_drop_metrics_rule_with_options_async(
        self,
        request: main_models.DescribeEnvDropMetricsRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnvDropMetricsRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnvDropMetricsRule',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnvDropMetricsRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_env_drop_metrics_rule(
        self,
        request: main_models.DescribeEnvDropMetricsRuleRequest,
    ) -> main_models.DescribeEnvDropMetricsRuleResponse:
        runtime = RuntimeOptions()
        return self.describe_env_drop_metrics_rule_with_options(request, runtime)

    async def describe_env_drop_metrics_rule_async(
        self,
        request: main_models.DescribeEnvDropMetricsRuleRequest,
    ) -> main_models.DescribeEnvDropMetricsRuleResponse:
        runtime = RuntimeOptions()
        return await self.describe_env_drop_metrics_rule_with_options_async(request, runtime)

    def describe_env_pod_monitor_with_options(
        self,
        request: main_models.DescribeEnvPodMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnvPodMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.pod_monitor_name):
            query['PodMonitorName'] = request.pod_monitor_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnvPodMonitor',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnvPodMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_env_pod_monitor_with_options_async(
        self,
        request: main_models.DescribeEnvPodMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnvPodMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.pod_monitor_name):
            query['PodMonitorName'] = request.pod_monitor_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnvPodMonitor',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnvPodMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_env_pod_monitor(
        self,
        request: main_models.DescribeEnvPodMonitorRequest,
    ) -> main_models.DescribeEnvPodMonitorResponse:
        runtime = RuntimeOptions()
        return self.describe_env_pod_monitor_with_options(request, runtime)

    async def describe_env_pod_monitor_async(
        self,
        request: main_models.DescribeEnvPodMonitorRequest,
    ) -> main_models.DescribeEnvPodMonitorResponse:
        runtime = RuntimeOptions()
        return await self.describe_env_pod_monitor_with_options_async(request, runtime)

    def describe_env_service_monitor_with_options(
        self,
        request: main_models.DescribeEnvServiceMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnvServiceMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_monitor_name):
            query['ServiceMonitorName'] = request.service_monitor_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnvServiceMonitor',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnvServiceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_env_service_monitor_with_options_async(
        self,
        request: main_models.DescribeEnvServiceMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnvServiceMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_monitor_name):
            query['ServiceMonitorName'] = request.service_monitor_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnvServiceMonitor',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnvServiceMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_env_service_monitor(
        self,
        request: main_models.DescribeEnvServiceMonitorRequest,
    ) -> main_models.DescribeEnvServiceMonitorResponse:
        runtime = RuntimeOptions()
        return self.describe_env_service_monitor_with_options(request, runtime)

    async def describe_env_service_monitor_async(
        self,
        request: main_models.DescribeEnvServiceMonitorRequest,
    ) -> main_models.DescribeEnvServiceMonitorResponse:
        runtime = RuntimeOptions()
        return await self.describe_env_service_monitor_with_options_async(request, runtime)

    def describe_environment_with_options(
        self,
        request: main_models.DescribeEnvironmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnvironmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnvironment',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_environment_with_options_async(
        self,
        request: main_models.DescribeEnvironmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnvironmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnvironment',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_environment(
        self,
        request: main_models.DescribeEnvironmentRequest,
    ) -> main_models.DescribeEnvironmentResponse:
        runtime = RuntimeOptions()
        return self.describe_environment_with_options(request, runtime)

    async def describe_environment_async(
        self,
        request: main_models.DescribeEnvironmentRequest,
    ) -> main_models.DescribeEnvironmentResponse:
        runtime = RuntimeOptions()
        return await self.describe_environment_with_options_async(request, runtime)

    def describe_environment_feature_with_options(
        self,
        request: main_models.DescribeEnvironmentFeatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnvironmentFeatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnvironmentFeature',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnvironmentFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_environment_feature_with_options_async(
        self,
        request: main_models.DescribeEnvironmentFeatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEnvironmentFeatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEnvironmentFeature',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEnvironmentFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_environment_feature(
        self,
        request: main_models.DescribeEnvironmentFeatureRequest,
    ) -> main_models.DescribeEnvironmentFeatureResponse:
        runtime = RuntimeOptions()
        return self.describe_environment_feature_with_options(request, runtime)

    async def describe_environment_feature_async(
        self,
        request: main_models.DescribeEnvironmentFeatureRequest,
    ) -> main_models.DescribeEnvironmentFeatureResponse:
        runtime = RuntimeOptions()
        return await self.describe_environment_feature_with_options_async(request, runtime)

    def describe_imrobots_with_options(
        self,
        request: main_models.DescribeIMRobotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIMRobotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.robot_ids):
            query['RobotIds'] = request.robot_ids
        if not DaraCore.is_null(request.robot_name):
            query['RobotName'] = request.robot_name
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIMRobots',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIMRobotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_imrobots_with_options_async(
        self,
        request: main_models.DescribeIMRobotsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIMRobotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.robot_ids):
            query['RobotIds'] = request.robot_ids
        if not DaraCore.is_null(request.robot_name):
            query['RobotName'] = request.robot_name
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIMRobots',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIMRobotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_imrobots(
        self,
        request: main_models.DescribeIMRobotsRequest,
    ) -> main_models.DescribeIMRobotsResponse:
        runtime = RuntimeOptions()
        return self.describe_imrobots_with_options(request, runtime)

    async def describe_imrobots_async(
        self,
        request: main_models.DescribeIMRobotsRequest,
    ) -> main_models.DescribeIMRobotsResponse:
        runtime = RuntimeOptions()
        return await self.describe_imrobots_with_options_async(request, runtime)

    def describe_prometheus_alert_rule_with_options(
        self,
        request: main_models.DescribePrometheusAlertRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePrometheusAlertRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_id):
            query['AlertId'] = request.alert_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrometheusAlertRule',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePrometheusAlertRule',
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def describe_webhook_contacts_with_options(
        self,
        request: main_models.DescribeWebhookContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebhookContactsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebhookContacts',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebhookContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_webhook_contacts_with_options_async(
        self,
        request: main_models.DescribeWebhookContactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeWebhookContactsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeWebhookContacts',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeWebhookContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_webhook_contacts(
        self,
        request: main_models.DescribeWebhookContactsRequest,
    ) -> main_models.DescribeWebhookContactsResponse:
        runtime = RuntimeOptions()
        return self.describe_webhook_contacts_with_options(request, runtime)

    async def describe_webhook_contacts_async(
        self,
        request: main_models.DescribeWebhookContactsRequest,
    ) -> main_models.DescribeWebhookContactsResponse:
        runtime = RuntimeOptions()
        return await self.describe_webhook_contacts_with_options_async(request, runtime)

    def do_insights_action_with_options(
        self,
        request: main_models.DoInsightsActionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DoInsightsActionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.module):
            body['Module'] = request.module
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DoInsightsAction',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DoInsightsActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def do_insights_action_with_options_async(
        self,
        request: main_models.DoInsightsActionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DoInsightsActionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.data):
            body['Data'] = request.data
        if not DaraCore.is_null(request.module):
            body['Module'] = request.module
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DoInsightsAction',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DoInsightsActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def do_insights_action(
        self,
        request: main_models.DoInsightsActionRequest,
    ) -> main_models.DoInsightsActionResponse:
        runtime = RuntimeOptions()
        return self.do_insights_action_with_options(request, runtime)

    async def do_insights_action_async(
        self,
        request: main_models.DoInsightsActionRequest,
    ) -> main_models.DoInsightsActionResponse:
        runtime = RuntimeOptions()
        return await self.do_insights_action_with_options_async(request, runtime)

    def enable_metric_with_options(
        self,
        request: main_models.EnableMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.drop_metric):
            query['DropMetric'] = request.drop_metric
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableMetric',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_metric_with_options_async(
        self,
        request: main_models.EnableMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.drop_metric):
            query['DropMetric'] = request.drop_metric
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableMetric',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_metric(
        self,
        request: main_models.EnableMetricRequest,
    ) -> main_models.EnableMetricResponse:
        runtime = RuntimeOptions()
        return self.enable_metric_with_options(request, runtime)

    async def enable_metric_async(
        self,
        request: main_models.EnableMetricRequest,
    ) -> main_models.EnableMetricResponse:
        runtime = RuntimeOptions()
        return await self.enable_metric_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def get_agent_download_url_v2with_options(
        self,
        request: main_models.GetAgentDownloadUrlV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentDownloadUrlV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_type):
            query['AgentType'] = request.agent_type
        if not DaraCore.is_null(request.arch_type):
            query['ArchType'] = request.arch_type
        if not DaraCore.is_null(request.os_type):
            query['OsType'] = request.os_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentDownloadUrlV2',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentDownloadUrlV2Response(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_download_url_v2with_options_async(
        self,
        request: main_models.GetAgentDownloadUrlV2Request,
        runtime: RuntimeOptions,
    ) -> main_models.GetAgentDownloadUrlV2Response:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_type):
            query['AgentType'] = request.agent_type
        if not DaraCore.is_null(request.arch_type):
            query['ArchType'] = request.arch_type
        if not DaraCore.is_null(request.os_type):
            query['OsType'] = request.os_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAgentDownloadUrlV2',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAgentDownloadUrlV2Response(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_download_url_v2(
        self,
        request: main_models.GetAgentDownloadUrlV2Request,
    ) -> main_models.GetAgentDownloadUrlV2Response:
        runtime = RuntimeOptions()
        return self.get_agent_download_url_v2with_options(request, runtime)

    async def get_agent_download_url_v2_async(
        self,
        request: main_models.GetAgentDownloadUrlV2Request,
    ) -> main_models.GetAgentDownloadUrlV2Response:
        runtime = RuntimeOptions()
        return await self.get_agent_download_url_v2with_options_async(request, runtime)

    def get_alert_rules_with_options(
        self,
        request: main_models.GetAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAlertRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not DaraCore.is_null(request.alert_names):
            query['AlertNames'] = request.alert_names
        if not DaraCore.is_null(request.alert_status):
            query['AlertStatus'] = request.alert_status
        if not DaraCore.is_null(request.alert_type):
            query['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlertRules',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alert_rules_with_options_async(
        self,
        request: main_models.GetAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAlertRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not DaraCore.is_null(request.alert_names):
            query['AlertNames'] = request.alert_names
        if not DaraCore.is_null(request.alert_status):
            query['AlertStatus'] = request.alert_status
        if not DaraCore.is_null(request.alert_type):
            query['AlertType'] = request.alert_type
        if not DaraCore.is_null(request.biz_region_id):
            query['BizRegionId'] = request.biz_region_id
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAlertRules',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alert_rules(
        self,
        request: main_models.GetAlertRulesRequest,
    ) -> main_models.GetAlertRulesResponse:
        runtime = RuntimeOptions()
        return self.get_alert_rules_with_options(request, runtime)

    async def get_alert_rules_async(
        self,
        request: main_models.GetAlertRulesRequest,
    ) -> main_models.GetAlertRulesResponse:
        runtime = RuntimeOptions()
        return await self.get_alert_rules_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def get_app_jvmconfig_with_options(
        self,
        request: main_models.GetAppJVMConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppJVMConfigResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppJVMConfig',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppJVMConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_jvmconfig_with_options_async(
        self,
        request: main_models.GetAppJVMConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAppJVMConfigResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAppJVMConfig',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAppJVMConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_jvmconfig(
        self,
        request: main_models.GetAppJVMConfigRequest,
    ) -> main_models.GetAppJVMConfigResponse:
        runtime = RuntimeOptions()
        return self.get_app_jvmconfig_with_options(request, runtime)

    async def get_app_jvmconfig_async(
        self,
        request: main_models.GetAppJVMConfigRequest,
    ) -> main_models.GetAppJVMConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_app_jvmconfig_with_options_async(request, runtime)

    def get_auth_token_with_options(
        self,
        request: main_models.GetAuthTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuthTokenResponse:
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
            action = 'GetAuthToken',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auth_token_with_options_async(
        self,
        request: main_models.GetAuthTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAuthTokenResponse:
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
            action = 'GetAuthToken',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAuthTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auth_token(
        self,
        request: main_models.GetAuthTokenRequest,
    ) -> main_models.GetAuthTokenResponse:
        runtime = RuntimeOptions()
        return self.get_auth_token_with_options(request, runtime)

    async def get_auth_token_async(
        self,
        request: main_models.GetAuthTokenRequest,
    ) -> main_models.GetAuthTokenResponse:
        runtime = RuntimeOptions()
        return await self.get_auth_token_with_options_async(request, runtime)

    def get_cloud_cluster_all_url_with_options(
        self,
        request: main_models.GetCloudClusterAllUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCloudClusterAllUrlResponse:
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
            action = 'GetCloudClusterAllUrl',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCloudClusterAllUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cloud_cluster_all_url_with_options_async(
        self,
        request: main_models.GetCloudClusterAllUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCloudClusterAllUrlResponse:
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
            action = 'GetCloudClusterAllUrl',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCloudClusterAllUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cloud_cluster_all_url(
        self,
        request: main_models.GetCloudClusterAllUrlRequest,
    ) -> main_models.GetCloudClusterAllUrlResponse:
        runtime = RuntimeOptions()
        return self.get_cloud_cluster_all_url_with_options(request, runtime)

    async def get_cloud_cluster_all_url_async(
        self,
        request: main_models.GetCloudClusterAllUrlRequest,
    ) -> main_models.GetCloudClusterAllUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_cloud_cluster_all_url_with_options_async(request, runtime)

    def get_cluster_all_url_with_options(
        self,
        request: main_models.GetClusterAllUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterAllUrlResponse:
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
            action = 'GetClusterAllUrl',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterAllUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_all_url_with_options_async(
        self,
        request: main_models.GetClusterAllUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetClusterAllUrlResponse:
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
            action = 'GetClusterAllUrl',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetClusterAllUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_all_url(
        self,
        request: main_models.GetClusterAllUrlRequest,
    ) -> main_models.GetClusterAllUrlResponse:
        runtime = RuntimeOptions()
        return self.get_cluster_all_url_with_options(request, runtime)

    async def get_cluster_all_url_async(
        self,
        request: main_models.GetClusterAllUrlRequest,
    ) -> main_models.GetClusterAllUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_cluster_all_url_with_options_async(request, runtime)

    def get_commercial_status_with_options(
        self,
        request: main_models.GetCommercialStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCommercialStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCommercialStatus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCommercialStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_commercial_status_with_options_async(
        self,
        request: main_models.GetCommercialStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetCommercialStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCommercialStatus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCommercialStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_commercial_status(
        self,
        request: main_models.GetCommercialStatusRequest,
    ) -> main_models.GetCommercialStatusResponse:
        runtime = RuntimeOptions()
        return self.get_commercial_status_with_options(request, runtime)

    async def get_commercial_status_async(
        self,
        request: main_models.GetCommercialStatusRequest,
    ) -> main_models.GetCommercialStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_commercial_status_with_options_async(request, runtime)

    def get_explore_url_with_options(
        self,
        request: main_models.GetExploreUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExploreUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExploreUrl',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExploreUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_explore_url_with_options_async(
        self,
        request: main_models.GetExploreUrlRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExploreUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExploreUrl',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExploreUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_explore_url(
        self,
        request: main_models.GetExploreUrlRequest,
    ) -> main_models.GetExploreUrlResponse:
        runtime = RuntimeOptions()
        return self.get_explore_url_with_options(request, runtime)

    async def get_explore_url_async(
        self,
        request: main_models.GetExploreUrlRequest,
    ) -> main_models.GetExploreUrlResponse:
        runtime = RuntimeOptions()
        return await self.get_explore_url_with_options_async(request, runtime)

    def get_grafana_workspace_with_options(
        self,
        request: main_models.GetGrafanaWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGrafanaWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGrafanaWorkspace',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGrafanaWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_grafana_workspace_with_options_async(
        self,
        request: main_models.GetGrafanaWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetGrafanaWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetGrafanaWorkspace',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetGrafanaWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_grafana_workspace(
        self,
        request: main_models.GetGrafanaWorkspaceRequest,
    ) -> main_models.GetGrafanaWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.get_grafana_workspace_with_options(request, runtime)

    async def get_grafana_workspace_async(
        self,
        request: main_models.GetGrafanaWorkspaceRequest,
    ) -> main_models.GetGrafanaWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.get_grafana_workspace_with_options_async(request, runtime)

    def get_integration_state_with_options(
        self,
        request: main_models.GetIntegrationStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIntegrationStateResponse:
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
            action = 'GetIntegrationState',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIntegrationStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_integration_state_with_options_async(
        self,
        request: main_models.GetIntegrationStateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetIntegrationStateResponse:
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
            action = 'GetIntegrationState',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIntegrationStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_integration_state(
        self,
        request: main_models.GetIntegrationStateRequest,
    ) -> main_models.GetIntegrationStateResponse:
        runtime = RuntimeOptions()
        return self.get_integration_state_with_options(request, runtime)

    async def get_integration_state_async(
        self,
        request: main_models.GetIntegrationStateRequest,
    ) -> main_models.GetIntegrationStateResponse:
        runtime = RuntimeOptions()
        return await self.get_integration_state_with_options_async(request, runtime)

    def get_managed_prometheus_status_with_options(
        self,
        request: main_models.GetManagedPrometheusStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetManagedPrometheusStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetManagedPrometheusStatus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetManagedPrometheusStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_managed_prometheus_status_with_options_async(
        self,
        request: main_models.GetManagedPrometheusStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetManagedPrometheusStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetManagedPrometheusStatus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetManagedPrometheusStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_managed_prometheus_status(
        self,
        request: main_models.GetManagedPrometheusStatusRequest,
    ) -> main_models.GetManagedPrometheusStatusResponse:
        runtime = RuntimeOptions()
        return self.get_managed_prometheus_status_with_options(request, runtime)

    async def get_managed_prometheus_status_async(
        self,
        request: main_models.GetManagedPrometheusStatusRequest,
    ) -> main_models.GetManagedPrometheusStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_managed_prometheus_status_with_options_async(request, runtime)

    def get_multiple_trace_with_options(
        self,
        request: main_models.GetMultipleTraceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMultipleTraceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.trace_ids):
            query['TraceIDs'] = request.trace_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMultipleTrace',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.trace_ids):
            query['TraceIDs'] = request.trace_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMultipleTrace',
            version = '2019-08-08',
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

    def get_on_call_schedules_detail_with_options(
        self,
        request: main_models.GetOnCallSchedulesDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOnCallSchedulesDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOnCallSchedulesDetail',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOnCallSchedulesDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_on_call_schedules_detail_with_options_async(
        self,
        request: main_models.GetOnCallSchedulesDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOnCallSchedulesDetailResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOnCallSchedulesDetail',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOnCallSchedulesDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_on_call_schedules_detail(
        self,
        request: main_models.GetOnCallSchedulesDetailRequest,
    ) -> main_models.GetOnCallSchedulesDetailResponse:
        runtime = RuntimeOptions()
        return self.get_on_call_schedules_detail_with_options(request, runtime)

    async def get_on_call_schedules_detail_async(
        self,
        request: main_models.GetOnCallSchedulesDetailRequest,
    ) -> main_models.GetOnCallSchedulesDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_on_call_schedules_detail_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def get_prometheus_global_view_with_options(
        self,
        request: main_models.GetPrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_global_view_with_options_async(
        self,
        request: main_models.GetPrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_global_view(
        self,
        request: main_models.GetPrometheusGlobalViewRequest,
    ) -> main_models.GetPrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return self.get_prometheus_global_view_with_options(request, runtime)

    async def get_prometheus_global_view_async(
        self,
        request: main_models.GetPrometheusGlobalViewRequest,
    ) -> main_models.GetPrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return await self.get_prometheus_global_view_with_options_async(request, runtime)

    def get_prometheus_instance_with_options(
        self,
        request: main_models.GetPrometheusInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPrometheusInstanceResponse:
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
            action = 'GetPrometheusInstance',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_instance_with_options_async(
        self,
        request: main_models.GetPrometheusInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPrometheusInstanceResponse:
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
            action = 'GetPrometheusInstance',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrometheusInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_instance(
        self,
        request: main_models.GetPrometheusInstanceRequest,
    ) -> main_models.GetPrometheusInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_prometheus_instance_with_options(request, runtime)

    async def get_prometheus_instance_async(
        self,
        request: main_models.GetPrometheusInstanceRequest,
    ) -> main_models.GetPrometheusInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_prometheus_instance_with_options_async(request, runtime)

    def get_prometheus_integration_with_options(
        self,
        request: main_models.GetPrometheusIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPrometheusIntegrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrometheusIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrometheusIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_integration_with_options_async(
        self,
        request: main_models.GetPrometheusIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPrometheusIntegrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrometheusIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrometheusIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_integration(
        self,
        request: main_models.GetPrometheusIntegrationRequest,
    ) -> main_models.GetPrometheusIntegrationResponse:
        runtime = RuntimeOptions()
        return self.get_prometheus_integration_with_options(request, runtime)

    async def get_prometheus_integration_async(
        self,
        request: main_models.GetPrometheusIntegrationRequest,
    ) -> main_models.GetPrometheusIntegrationResponse:
        runtime = RuntimeOptions()
        return await self.get_prometheus_integration_with_options_async(request, runtime)

    def get_prometheus_monitoring_with_options(
        self,
        request: main_models.GetPrometheusMonitoringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPrometheusMonitoringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrometheusMonitoring',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrometheusMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_monitoring_with_options_async(
        self,
        request: main_models.GetPrometheusMonitoringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPrometheusMonitoringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPrometheusMonitoring',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPrometheusMonitoringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_monitoring(
        self,
        request: main_models.GetPrometheusMonitoringRequest,
    ) -> main_models.GetPrometheusMonitoringResponse:
        runtime = RuntimeOptions()
        return self.get_prometheus_monitoring_with_options(request, runtime)

    async def get_prometheus_monitoring_async(
        self,
        request: main_models.GetPrometheusMonitoringRequest,
    ) -> main_models.GetPrometheusMonitoringResponse:
        runtime = RuntimeOptions()
        return await self.get_prometheus_monitoring_with_options_async(request, runtime)

    def get_recording_rule_with_options(
        self,
        request: main_models.GetRecordingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRecordingRuleResponse:
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
            action = 'GetRecordingRule',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecordingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_recording_rule_with_options_async(
        self,
        request: main_models.GetRecordingRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRecordingRuleResponse:
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
            action = 'GetRecordingRule',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRecordingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_recording_rule(
        self,
        request: main_models.GetRecordingRuleRequest,
    ) -> main_models.GetRecordingRuleResponse:
        runtime = RuntimeOptions()
        return self.get_recording_rule_with_options(request, runtime)

    async def get_recording_rule_async(
        self,
        request: main_models.GetRecordingRuleRequest,
    ) -> main_models.GetRecordingRuleResponse:
        runtime = RuntimeOptions()
        return await self.get_recording_rule_with_options_async(request, runtime)

    def get_retcode_app_by_pid_with_options(
        self,
        request: main_models.GetRetcodeAppByPidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRetcodeAppByPidResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRetcodeAppByPid',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRetcodeAppByPidResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_retcode_app_by_pid_with_options_async(
        self,
        request: main_models.GetRetcodeAppByPidRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRetcodeAppByPidResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRetcodeAppByPid',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRetcodeAppByPidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_retcode_app_by_pid(
        self,
        request: main_models.GetRetcodeAppByPidRequest,
    ) -> main_models.GetRetcodeAppByPidResponse:
        runtime = RuntimeOptions()
        return self.get_retcode_app_by_pid_with_options(request, runtime)

    async def get_retcode_app_by_pid_async(
        self,
        request: main_models.GetRetcodeAppByPidRequest,
    ) -> main_models.GetRetcodeAppByPidResponse:
        runtime = RuntimeOptions()
        return await self.get_retcode_app_by_pid_with_options_async(request, runtime)

    def get_retcode_data_by_query_with_options(
        self,
        request: main_models.GetRetcodeDataByQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRetcodeDataByQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.to):
            query['To'] = request.to
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRetcodeDataByQuery',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRetcodeDataByQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_retcode_data_by_query_with_options_async(
        self,
        request: main_models.GetRetcodeDataByQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRetcodeDataByQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_):
            query['From'] = request.from_
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.to):
            query['To'] = request.to
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRetcodeDataByQuery',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRetcodeDataByQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_retcode_data_by_query(
        self,
        request: main_models.GetRetcodeDataByQueryRequest,
    ) -> main_models.GetRetcodeDataByQueryResponse:
        runtime = RuntimeOptions()
        return self.get_retcode_data_by_query_with_options(request, runtime)

    async def get_retcode_data_by_query_async(
        self,
        request: main_models.GetRetcodeDataByQueryRequest,
    ) -> main_models.GetRetcodeDataByQueryResponse:
        runtime = RuntimeOptions()
        return await self.get_retcode_data_by_query_with_options_async(request, runtime)

    def get_retcode_logstore_with_options(
        self,
        request: main_models.GetRetcodeLogstoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRetcodeLogstoreResponse:
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
            action = 'GetRetcodeLogstore',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRetcodeLogstoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_retcode_logstore_with_options_async(
        self,
        request: main_models.GetRetcodeLogstoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRetcodeLogstoreResponse:
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
            action = 'GetRetcodeLogstore',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRetcodeLogstoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_retcode_logstore(
        self,
        request: main_models.GetRetcodeLogstoreRequest,
    ) -> main_models.GetRetcodeLogstoreResponse:
        runtime = RuntimeOptions()
        return self.get_retcode_logstore_with_options(request, runtime)

    async def get_retcode_logstore_async(
        self,
        request: main_models.GetRetcodeLogstoreRequest,
    ) -> main_models.GetRetcodeLogstoreResponse:
        runtime = RuntimeOptions()
        return await self.get_retcode_logstore_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def get_rum_app_info_with_options(
        self,
        request: main_models.GetRumAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRumAppInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_group):
            query['AppGroup'] = request.app_group
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRumAppInfo',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRumAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rum_app_info_with_options_async(
        self,
        request: main_models.GetRumAppInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRumAppInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_group):
            query['AppGroup'] = request.app_group
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRumAppInfo',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRumAppInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rum_app_info(
        self,
        request: main_models.GetRumAppInfoRequest,
    ) -> main_models.GetRumAppInfoResponse:
        runtime = RuntimeOptions()
        return self.get_rum_app_info_with_options(request, runtime)

    async def get_rum_app_info_async(
        self,
        request: main_models.GetRumAppInfoRequest,
    ) -> main_models.GetRumAppInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_rum_app_info_with_options_async(request, runtime)

    def get_rum_apps_with_options(
        self,
        tmp_req: main_models.GetRumAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRumAppsResponse:
        tmp_req.validate()
        request = main_models.GetRumAppsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.app_group):
            query['AppGroup'] = request.app_group
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRumApps',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRumAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rum_apps_with_options_async(
        self,
        tmp_req: main_models.GetRumAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRumAppsResponse:
        tmp_req.validate()
        request = main_models.GetRumAppsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.app_group):
            query['AppGroup'] = request.app_group
        if not DaraCore.is_null(request.app_id):
            query['AppId'] = request.app_id
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRumApps',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRumAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rum_apps(
        self,
        request: main_models.GetRumAppsRequest,
    ) -> main_models.GetRumAppsResponse:
        runtime = RuntimeOptions()
        return self.get_rum_apps_with_options(request, runtime)

    async def get_rum_apps_async(
        self,
        request: main_models.GetRumAppsRequest,
    ) -> main_models.GetRumAppsResponse:
        runtime = RuntimeOptions()
        return await self.get_rum_apps_with_options_async(request, runtime)

    def get_rum_data_for_page_with_options(
        self,
        request: main_models.GetRumDataForPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRumDataForPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_group):
            query['AppGroup'] = request.app_group
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRumDataForPage',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRumDataForPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rum_data_for_page_with_options_async(
        self,
        request: main_models.GetRumDataForPageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRumDataForPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_group):
            query['AppGroup'] = request.app_group
        if not DaraCore.is_null(request.current_page):
            query['CurrentPage'] = request.current_page
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRumDataForPage',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRumDataForPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rum_data_for_page(
        self,
        request: main_models.GetRumDataForPageRequest,
    ) -> main_models.GetRumDataForPageResponse:
        runtime = RuntimeOptions()
        return self.get_rum_data_for_page_with_options(request, runtime)

    async def get_rum_data_for_page_async(
        self,
        request: main_models.GetRumDataForPageRequest,
    ) -> main_models.GetRumDataForPageResponse:
        runtime = RuntimeOptions()
        return await self.get_rum_data_for_page_with_options_async(request, runtime)

    def get_rum_exception_stack_with_options(
        self,
        request: main_models.GetRumExceptionStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRumExceptionStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.exception_binary_images):
            query['ExceptionBinaryImages'] = request.exception_binary_images
        if not DaraCore.is_null(request.exception_stack):
            query['ExceptionStack'] = request.exception_stack
        if not DaraCore.is_null(request.exception_thread_id):
            query['ExceptionThreadId'] = request.exception_thread_id
        if not DaraCore.is_null(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.sourcemap_type):
            query['SourcemapType'] = request.sourcemap_type
        if not DaraCore.is_null(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRumExceptionStack',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRumExceptionStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rum_exception_stack_with_options_async(
        self,
        request: main_models.GetRumExceptionStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRumExceptionStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.exception_binary_images):
            query['ExceptionBinaryImages'] = request.exception_binary_images
        if not DaraCore.is_null(request.exception_stack):
            query['ExceptionStack'] = request.exception_stack
        if not DaraCore.is_null(request.exception_thread_id):
            query['ExceptionThreadId'] = request.exception_thread_id
        if not DaraCore.is_null(request.extra_info):
            query['ExtraInfo'] = request.extra_info
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.sourcemap_type):
            query['SourcemapType'] = request.sourcemap_type
        if not DaraCore.is_null(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRumExceptionStack',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRumExceptionStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rum_exception_stack(
        self,
        request: main_models.GetRumExceptionStackRequest,
    ) -> main_models.GetRumExceptionStackResponse:
        runtime = RuntimeOptions()
        return self.get_rum_exception_stack_with_options(request, runtime)

    async def get_rum_exception_stack_async(
        self,
        request: main_models.GetRumExceptionStackRequest,
    ) -> main_models.GetRumExceptionStackResponse:
        runtime = RuntimeOptions()
        return await self.get_rum_exception_stack_with_options_async(request, runtime)

    def get_rum_ocu_statistic_data_with_options(
        self,
        tmp_req: main_models.GetRumOcuStatisticDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRumOcuStatisticDataResponse:
        tmp_req.validate()
        request = main_models.GetRumOcuStatisticDataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        if not DaraCore.is_null(tmp_req.group):
            request.group_shrink = Utils.array_to_string_with_specified_style(tmp_req.group, 'Group', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRumOcuStatisticData',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRumOcuStatisticDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rum_ocu_statistic_data_with_options_async(
        self,
        tmp_req: main_models.GetRumOcuStatisticDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRumOcuStatisticDataResponse:
        tmp_req.validate()
        request = main_models.GetRumOcuStatisticDataShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        if not DaraCore.is_null(tmp_req.group):
            request.group_shrink = Utils.array_to_string_with_specified_style(tmp_req.group, 'Group', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRumOcuStatisticData',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRumOcuStatisticDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rum_ocu_statistic_data(
        self,
        request: main_models.GetRumOcuStatisticDataRequest,
    ) -> main_models.GetRumOcuStatisticDataResponse:
        runtime = RuntimeOptions()
        return self.get_rum_ocu_statistic_data_with_options(request, runtime)

    async def get_rum_ocu_statistic_data_async(
        self,
        request: main_models.GetRumOcuStatisticDataRequest,
    ) -> main_models.GetRumOcuStatisticDataResponse:
        runtime = RuntimeOptions()
        return await self.get_rum_ocu_statistic_data_with_options_async(request, runtime)

    def get_rum_upload_files_with_options(
        self,
        request: main_models.GetRumUploadFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRumUploadFilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        if not DaraCore.is_null(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRumUploadFiles',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRumUploadFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rum_upload_files_with_options_async(
        self,
        request: main_models.GetRumUploadFilesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetRumUploadFilesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        if not DaraCore.is_null(request.workspace):
            query['Workspace'] = request.workspace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRumUploadFiles',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRumUploadFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rum_upload_files(
        self,
        request: main_models.GetRumUploadFilesRequest,
    ) -> main_models.GetRumUploadFilesResponse:
        runtime = RuntimeOptions()
        return self.get_rum_upload_files_with_options(request, runtime)

    async def get_rum_upload_files_async(
        self,
        request: main_models.GetRumUploadFilesRequest,
    ) -> main_models.GetRumUploadFilesResponse:
        runtime = RuntimeOptions()
        return await self.get_rum_upload_files_with_options_async(request, runtime)

    def get_source_map_info_with_options(
        self,
        request: main_models.GetSourceMapInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSourceMapInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ascending_sequence):
            query['AscendingSequence'] = request.ascending_sequence
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.id):
            query['ID'] = request.id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.order_field):
            query['OrderField'] = request.order_field
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSourceMapInfo',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSourceMapInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_source_map_info_with_options_async(
        self,
        request: main_models.GetSourceMapInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSourceMapInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ascending_sequence):
            query['AscendingSequence'] = request.ascending_sequence
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.id):
            query['ID'] = request.id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.order_field):
            query['OrderField'] = request.order_field
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSourceMapInfo',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSourceMapInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_source_map_info(
        self,
        request: main_models.GetSourceMapInfoRequest,
    ) -> main_models.GetSourceMapInfoResponse:
        runtime = RuntimeOptions()
        return self.get_source_map_info_with_options(request, runtime)

    async def get_source_map_info_async(
        self,
        request: main_models.GetSourceMapInfoRequest,
    ) -> main_models.GetSourceMapInfoResponse:
        runtime = RuntimeOptions()
        return await self.get_source_map_info_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.span_id):
            query['SpanID'] = request.span_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStack',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.span_id):
            query['SpanID'] = request.span_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStack',
            version = '2019-08-08',
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

    def get_synthetic_monitors_with_options(
        self,
        tmp_req: main_models.GetSyntheticMonitorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSyntheticMonitorsResponse:
        tmp_req.validate()
        request = main_models.GetSyntheticMonitorsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSyntheticMonitors',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSyntheticMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_synthetic_monitors_with_options_async(
        self,
        tmp_req: main_models.GetSyntheticMonitorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSyntheticMonitorsResponse:
        tmp_req.validate()
        request = main_models.GetSyntheticMonitorsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filter):
            request.filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSyntheticMonitors',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSyntheticMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_synthetic_monitors(
        self,
        request: main_models.GetSyntheticMonitorsRequest,
    ) -> main_models.GetSyntheticMonitorsResponse:
        runtime = RuntimeOptions()
        return self.get_synthetic_monitors_with_options(request, runtime)

    async def get_synthetic_monitors_async(
        self,
        request: main_models.GetSyntheticMonitorsRequest,
    ) -> main_models.GetSyntheticMonitorsResponse:
        runtime = RuntimeOptions()
        return await self.get_synthetic_monitors_with_options_async(request, runtime)

    def get_synthetic_task_detail_with_options(
        self,
        request: main_models.GetSyntheticTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSyntheticTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSyntheticTaskDetail',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSyntheticTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_synthetic_task_detail_with_options_async(
        self,
        request: main_models.GetSyntheticTaskDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSyntheticTaskDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSyntheticTaskDetail',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSyntheticTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_synthetic_task_detail(
        self,
        request: main_models.GetSyntheticTaskDetailRequest,
    ) -> main_models.GetSyntheticTaskDetailResponse:
        runtime = RuntimeOptions()
        return self.get_synthetic_task_detail_with_options(request, runtime)

    async def get_synthetic_task_detail_async(
        self,
        request: main_models.GetSyntheticTaskDetailRequest,
    ) -> main_models.GetSyntheticTaskDetailResponse:
        runtime = RuntimeOptions()
        return await self.get_synthetic_task_detail_with_options_async(request, runtime)

    def get_synthetic_task_list_with_options(
        self,
        request: main_models.GetSyntheticTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSyntheticTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_status):
            query['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSyntheticTaskList',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSyntheticTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_synthetic_task_list_with_options_async(
        self,
        request: main_models.GetSyntheticTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSyntheticTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.direction):
            query['Direction'] = request.direction
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_status):
            query['TaskStatus'] = request.task_status
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSyntheticTaskList',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSyntheticTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_synthetic_task_list(
        self,
        request: main_models.GetSyntheticTaskListRequest,
    ) -> main_models.GetSyntheticTaskListResponse:
        runtime = RuntimeOptions()
        return self.get_synthetic_task_list_with_options(request, runtime)

    async def get_synthetic_task_list_async(
        self,
        request: main_models.GetSyntheticTaskListRequest,
    ) -> main_models.GetSyntheticTaskListResponse:
        runtime = RuntimeOptions()
        return await self.get_synthetic_task_list_with_options_async(request, runtime)

    def get_synthetic_task_monitors_with_options(
        self,
        request: main_models.GetSyntheticTaskMonitorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSyntheticTaskMonitorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSyntheticTaskMonitors',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSyntheticTaskMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_synthetic_task_monitors_with_options_async(
        self,
        request: main_models.GetSyntheticTaskMonitorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSyntheticTaskMonitorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSyntheticTaskMonitors',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSyntheticTaskMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_synthetic_task_monitors(
        self,
        request: main_models.GetSyntheticTaskMonitorsRequest,
    ) -> main_models.GetSyntheticTaskMonitorsResponse:
        runtime = RuntimeOptions()
        return self.get_synthetic_task_monitors_with_options(request, runtime)

    async def get_synthetic_task_monitors_async(
        self,
        request: main_models.GetSyntheticTaskMonitorsRequest,
    ) -> main_models.GetSyntheticTaskMonitorsResponse:
        runtime = RuntimeOptions()
        return await self.get_synthetic_task_monitors_with_options_async(request, runtime)

    def get_timing_synthetic_task_with_options(
        self,
        request: main_models.GetTimingSyntheticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTimingSyntheticTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTimingSyntheticTask',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTimingSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_timing_synthetic_task_with_options_async(
        self,
        request: main_models.GetTimingSyntheticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTimingSyntheticTaskResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTimingSyntheticTask',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTimingSyntheticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_timing_synthetic_task(
        self,
        request: main_models.GetTimingSyntheticTaskRequest,
    ) -> main_models.GetTimingSyntheticTaskResponse:
        runtime = RuntimeOptions()
        return self.get_timing_synthetic_task_with_options(request, runtime)

    async def get_timing_synthetic_task_async(
        self,
        request: main_models.GetTimingSyntheticTaskRequest,
    ) -> main_models.GetTimingSyntheticTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_timing_synthetic_task_with_options_async(request, runtime)

    def get_trace_with_options(
        self,
        request: main_models.GetTraceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTraceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrace',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTrace',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTraceApp',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTraceApp',
            version = '2019-08-08',
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

    def get_trace_app_config_with_options(
        self,
        request: main_models.GetTraceAppConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTraceAppConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTraceAppConfig',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTraceAppConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trace_app_config_with_options_async(
        self,
        request: main_models.GetTraceAppConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTraceAppConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTraceAppConfig',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTraceAppConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trace_app_config(
        self,
        request: main_models.GetTraceAppConfigRequest,
    ) -> main_models.GetTraceAppConfigResponse:
        runtime = RuntimeOptions()
        return self.get_trace_app_config_with_options(request, runtime)

    async def get_trace_app_config_async(
        self,
        request: main_models.GetTraceAppConfigRequest,
    ) -> main_models.GetTraceAppConfigResponse:
        runtime = RuntimeOptions()
        return await self.get_trace_app_config_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        if not DaraCore.is_null(request.template_alert_id):
            query['TemplateAlertId'] = request.template_alert_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportAppAlertRules',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        if not DaraCore.is_null(request.template_alert_id):
            query['TemplateAlertId'] = request.template_alert_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportAppAlertRules',
            version = '2019-08-08',
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

    def init_environment_with_options(
        self,
        request: main_models.InitEnvironmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitEnvironmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.create_auth_token):
            query['CreateAuthToken'] = request.create_auth_token
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.managed_type):
            query['ManagedType'] = request.managed_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitEnvironment',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_environment_with_options_async(
        self,
        request: main_models.InitEnvironmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InitEnvironmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.create_auth_token):
            query['CreateAuthToken'] = request.create_auth_token
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.managed_type):
            query['ManagedType'] = request.managed_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InitEnvironment',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_environment(
        self,
        request: main_models.InitEnvironmentRequest,
    ) -> main_models.InitEnvironmentResponse:
        runtime = RuntimeOptions()
        return self.init_environment_with_options(request, runtime)

    async def init_environment_async(
        self,
        request: main_models.InitEnvironmentRequest,
    ) -> main_models.InitEnvironmentResponse:
        runtime = RuntimeOptions()
        return await self.init_environment_with_options_async(request, runtime)

    def install_addon_with_options(
        self,
        request: main_models.InstallAddonRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallAddonResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.release_name):
            query['ReleaseName'] = request.release_name
        if not DaraCore.is_null(request.values):
            query['Values'] = request.values
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallAddon',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallAddonResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_addon_with_options_async(
        self,
        request: main_models.InstallAddonRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallAddonResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.release_name):
            query['ReleaseName'] = request.release_name
        if not DaraCore.is_null(request.values):
            query['Values'] = request.values
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallAddon',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallAddonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_addon(
        self,
        request: main_models.InstallAddonRequest,
    ) -> main_models.InstallAddonResponse:
        runtime = RuntimeOptions()
        return self.install_addon_with_options(request, runtime)

    async def install_addon_async(
        self,
        request: main_models.InstallAddonRequest,
    ) -> main_models.InstallAddonResponse:
        runtime = RuntimeOptions()
        return await self.install_addon_with_options_async(request, runtime)

    def install_cms_exporter_with_options(
        self,
        request: main_models.InstallCmsExporterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallCmsExporterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cms_args):
            query['CmsArgs'] = request.cms_args
        if not DaraCore.is_null(request.direct_args):
            query['DirectArgs'] = request.direct_args
        if not DaraCore.is_null(request.enable_tag):
            query['EnableTag'] = request.enable_tag
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallCmsExporter',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallCmsExporterResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_cms_exporter_with_options_async(
        self,
        request: main_models.InstallCmsExporterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallCmsExporterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cms_args):
            query['CmsArgs'] = request.cms_args
        if not DaraCore.is_null(request.direct_args):
            query['DirectArgs'] = request.direct_args
        if not DaraCore.is_null(request.enable_tag):
            query['EnableTag'] = request.enable_tag
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallCmsExporter',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallCmsExporterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_cms_exporter(
        self,
        request: main_models.InstallCmsExporterRequest,
    ) -> main_models.InstallCmsExporterResponse:
        runtime = RuntimeOptions()
        return self.install_cms_exporter_with_options(request, runtime)

    async def install_cms_exporter_async(
        self,
        request: main_models.InstallCmsExporterRequest,
    ) -> main_models.InstallCmsExporterResponse:
        runtime = RuntimeOptions()
        return await self.install_cms_exporter_with_options_async(request, runtime)

    def install_environment_feature_with_options(
        self,
        request: main_models.InstallEnvironmentFeatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallEnvironmentFeatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not DaraCore.is_null(request.feature_version):
            query['FeatureVersion'] = request.feature_version
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallEnvironmentFeature',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallEnvironmentFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_environment_feature_with_options_async(
        self,
        request: main_models.InstallEnvironmentFeatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallEnvironmentFeatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.config):
            query['Config'] = request.config
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not DaraCore.is_null(request.feature_version):
            query['FeatureVersion'] = request.feature_version
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallEnvironmentFeature',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallEnvironmentFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_environment_feature(
        self,
        request: main_models.InstallEnvironmentFeatureRequest,
    ) -> main_models.InstallEnvironmentFeatureResponse:
        runtime = RuntimeOptions()
        return self.install_environment_feature_with_options(request, runtime)

    async def install_environment_feature_async(
        self,
        request: main_models.InstallEnvironmentFeatureRequest,
    ) -> main_models.InstallEnvironmentFeatureResponse:
        runtime = RuntimeOptions()
        return await self.install_environment_feature_with_options_async(request, runtime)

    def install_managed_prometheus_with_options(
        self,
        request: main_models.InstallManagedPrometheusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallManagedPrometheusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.grafana_instance_id):
            query['GrafanaInstanceId'] = request.grafana_instance_id
        if not DaraCore.is_null(request.kube_config):
            query['KubeConfig'] = request.kube_config
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vc_extra_info):
            query['VcExtraInfo'] = request.vc_extra_info
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallManagedPrometheus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallManagedPrometheusResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_managed_prometheus_with_options_async(
        self,
        request: main_models.InstallManagedPrometheusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallManagedPrometheusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.grafana_instance_id):
            query['GrafanaInstanceId'] = request.grafana_instance_id
        if not DaraCore.is_null(request.kube_config):
            query['KubeConfig'] = request.kube_config
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not DaraCore.is_null(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not DaraCore.is_null(request.vc_extra_info):
            query['VcExtraInfo'] = request.vc_extra_info
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallManagedPrometheus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallManagedPrometheusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_managed_prometheus(
        self,
        request: main_models.InstallManagedPrometheusRequest,
    ) -> main_models.InstallManagedPrometheusResponse:
        runtime = RuntimeOptions()
        return self.install_managed_prometheus_with_options(request, runtime)

    async def install_managed_prometheus_async(
        self,
        request: main_models.InstallManagedPrometheusRequest,
    ) -> main_models.InstallManagedPrometheusResponse:
        runtime = RuntimeOptions()
        return await self.install_managed_prometheus_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def list_addon_releases_with_options(
        self,
        request: main_models.ListAddonReleasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAddonReleasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['AddonName'] = request.addon_name
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddonReleases',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddonReleasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addon_releases_with_options_async(
        self,
        request: main_models.ListAddonReleasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAddonReleasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['AddonName'] = request.addon_name
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddonReleases',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddonReleasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_addon_releases(
        self,
        request: main_models.ListAddonReleasesRequest,
    ) -> main_models.ListAddonReleasesResponse:
        runtime = RuntimeOptions()
        return self.list_addon_releases_with_options(request, runtime)

    async def list_addon_releases_async(
        self,
        request: main_models.ListAddonReleasesRequest,
    ) -> main_models.ListAddonReleasesResponse:
        runtime = RuntimeOptions()
        return await self.list_addon_releases_with_options_async(request, runtime)

    def list_addons_with_options(
        self,
        request: main_models.ListAddonsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAddonsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.regexp):
            query['Regexp'] = request.regexp
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.search):
            query['Search'] = request.search
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddons',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addons_with_options_async(
        self,
        request: main_models.ListAddonsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAddonsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.regexp):
            query['Regexp'] = request.regexp
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.search):
            query['Search'] = request.search
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAddons',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_addons(
        self,
        request: main_models.ListAddonsRequest,
    ) -> main_models.ListAddonsResponse:
        runtime = RuntimeOptions()
        return self.list_addons_with_options(request, runtime)

    async def list_addons_async(
        self,
        request: main_models.ListAddonsRequest,
    ) -> main_models.ListAddonsResponse:
        runtime = RuntimeOptions()
        return await self.list_addons_with_options_async(request, runtime)

    def list_alert_events_with_options(
        self,
        request: main_models.ListAlertEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_name):
            query['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.matching_conditions):
            query['MatchingConditions'] = request.matching_conditions
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.show_notification_policies):
            query['ShowNotificationPolicies'] = request.show_notification_policies
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlertEvents',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alert_events_with_options_async(
        self,
        request: main_models.ListAlertEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_name):
            query['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.matching_conditions):
            query['MatchingConditions'] = request.matching_conditions
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.show_notification_policies):
            query['ShowNotificationPolicies'] = request.show_notification_policies
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlertEvents',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alert_events(
        self,
        request: main_models.ListAlertEventsRequest,
    ) -> main_models.ListAlertEventsResponse:
        runtime = RuntimeOptions()
        return self.list_alert_events_with_options(request, runtime)

    async def list_alert_events_async(
        self,
        request: main_models.ListAlertEventsRequest,
    ) -> main_models.ListAlertEventsResponse:
        runtime = RuntimeOptions()
        return await self.list_alert_events_with_options_async(request, runtime)

    def list_alerts_with_options(
        self,
        request: main_models.ListAlertsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_name):
            query['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.dispatch_rule_id):
            query['DispatchRuleId'] = request.dispatch_rule_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.show_activities):
            query['ShowActivities'] = request.show_activities
        if not DaraCore.is_null(request.show_events):
            query['ShowEvents'] = request.show_events
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlerts',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alerts_with_options_async(
        self,
        request: main_models.ListAlertsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAlertsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_name):
            query['AlertName'] = request.alert_name
        if not DaraCore.is_null(request.dispatch_rule_id):
            query['DispatchRuleId'] = request.dispatch_rule_id
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not DaraCore.is_null(request.owner):
            query['Owner'] = request.owner
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.show_activities):
            query['ShowActivities'] = request.show_activities
        if not DaraCore.is_null(request.show_events):
            query['ShowEvents'] = request.show_events
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAlerts',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAlertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alerts(
        self,
        request: main_models.ListAlertsRequest,
    ) -> main_models.ListAlertsResponse:
        runtime = RuntimeOptions()
        return self.list_alerts_with_options(request, runtime)

    async def list_alerts_async(
        self,
        request: main_models.ListAlertsRequest,
    ) -> main_models.ListAlertsResponse:
        runtime = RuntimeOptions()
        return await self.list_alerts_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def list_cms_instances_with_options(
        self,
        request: main_models.ListCmsInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCmsInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type_filter):
            query['TypeFilter'] = request.type_filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCmsInstances',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCmsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cms_instances_with_options_async(
        self,
        request: main_models.ListCmsInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListCmsInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type_filter):
            query['TypeFilter'] = request.type_filter
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCmsInstances',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCmsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cms_instances(
        self,
        request: main_models.ListCmsInstancesRequest,
    ) -> main_models.ListCmsInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_cms_instances_with_options(request, runtime)

    async def list_cms_instances_async(
        self,
        request: main_models.ListCmsInstancesRequest,
    ) -> main_models.ListCmsInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_cms_instances_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.dashboard_name):
            query['DashboardName'] = request.dashboard_name
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
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
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.dashboard_name):
            query['DashboardName'] = request.dashboard_name
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
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
            version = '2019-08-08',
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

    def list_dashboards_by_name_with_options(
        self,
        request: main_models.ListDashboardsByNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDashboardsByNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.dash_board_name):
            query['DashBoardName'] = request.dash_board_name
        if not DaraCore.is_null(request.dash_board_version):
            query['DashBoardVersion'] = request.dash_board_version
        if not DaraCore.is_null(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.only_query):
            query['OnlyQuery'] = request.only_query
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDashboardsByName',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDashboardsByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dashboards_by_name_with_options_async(
        self,
        request: main_models.ListDashboardsByNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDashboardsByNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.dash_board_name):
            query['DashBoardName'] = request.dash_board_name
        if not DaraCore.is_null(request.dash_board_version):
            query['DashBoardVersion'] = request.dash_board_version
        if not DaraCore.is_null(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.only_query):
            query['OnlyQuery'] = request.only_query
        if not DaraCore.is_null(request.product_code):
            query['ProductCode'] = request.product_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDashboardsByName',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDashboardsByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dashboards_by_name(
        self,
        request: main_models.ListDashboardsByNameRequest,
    ) -> main_models.ListDashboardsByNameResponse:
        runtime = RuntimeOptions()
        return self.list_dashboards_by_name_with_options(request, runtime)

    async def list_dashboards_by_name_async(
        self,
        request: main_models.ListDashboardsByNameRequest,
    ) -> main_models.ListDashboardsByNameResponse:
        runtime = RuntimeOptions()
        return await self.list_dashboards_by_name_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def list_env_custom_jobs_with_options(
        self,
        request: main_models.ListEnvCustomJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvCustomJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_yaml):
            query['EncryptYaml'] = request.encrypt_yaml
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvCustomJobs',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvCustomJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_env_custom_jobs_with_options_async(
        self,
        request: main_models.ListEnvCustomJobsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvCustomJobsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.encrypt_yaml):
            query['EncryptYaml'] = request.encrypt_yaml
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvCustomJobs',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvCustomJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_env_custom_jobs(
        self,
        request: main_models.ListEnvCustomJobsRequest,
    ) -> main_models.ListEnvCustomJobsResponse:
        runtime = RuntimeOptions()
        return self.list_env_custom_jobs_with_options(request, runtime)

    async def list_env_custom_jobs_async(
        self,
        request: main_models.ListEnvCustomJobsRequest,
    ) -> main_models.ListEnvCustomJobsResponse:
        runtime = RuntimeOptions()
        return await self.list_env_custom_jobs_with_options_async(request, runtime)

    def list_env_pod_monitors_with_options(
        self,
        request: main_models.ListEnvPodMonitorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvPodMonitorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvPodMonitors',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvPodMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_env_pod_monitors_with_options_async(
        self,
        request: main_models.ListEnvPodMonitorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvPodMonitorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvPodMonitors',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvPodMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_env_pod_monitors(
        self,
        request: main_models.ListEnvPodMonitorsRequest,
    ) -> main_models.ListEnvPodMonitorsResponse:
        runtime = RuntimeOptions()
        return self.list_env_pod_monitors_with_options(request, runtime)

    async def list_env_pod_monitors_async(
        self,
        request: main_models.ListEnvPodMonitorsRequest,
    ) -> main_models.ListEnvPodMonitorsResponse:
        runtime = RuntimeOptions()
        return await self.list_env_pod_monitors_with_options_async(request, runtime)

    def list_env_service_monitors_with_options(
        self,
        request: main_models.ListEnvServiceMonitorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvServiceMonitorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvServiceMonitors',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvServiceMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_env_service_monitors_with_options_async(
        self,
        request: main_models.ListEnvServiceMonitorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvServiceMonitorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvServiceMonitors',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvServiceMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_env_service_monitors(
        self,
        request: main_models.ListEnvServiceMonitorsRequest,
    ) -> main_models.ListEnvServiceMonitorsResponse:
        runtime = RuntimeOptions()
        return self.list_env_service_monitors_with_options(request, runtime)

    async def list_env_service_monitors_async(
        self,
        request: main_models.ListEnvServiceMonitorsRequest,
    ) -> main_models.ListEnvServiceMonitorsResponse:
        runtime = RuntimeOptions()
        return await self.list_env_service_monitors_with_options_async(request, runtime)

    def list_environment_addons_with_options(
        self,
        request: main_models.ListEnvironmentAddonsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentAddonsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironmentAddons',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environment_addons_with_options_async(
        self,
        request: main_models.ListEnvironmentAddonsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentAddonsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironmentAddons',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environment_addons(
        self,
        request: main_models.ListEnvironmentAddonsRequest,
    ) -> main_models.ListEnvironmentAddonsResponse:
        runtime = RuntimeOptions()
        return self.list_environment_addons_with_options(request, runtime)

    async def list_environment_addons_async(
        self,
        request: main_models.ListEnvironmentAddonsRequest,
    ) -> main_models.ListEnvironmentAddonsResponse:
        runtime = RuntimeOptions()
        return await self.list_environment_addons_with_options_async(request, runtime)

    def list_environment_alert_rules_with_options(
        self,
        request: main_models.ListEnvironmentAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentAlertRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['AddonName'] = request.addon_name
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironmentAlertRules',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environment_alert_rules_with_options_async(
        self,
        request: main_models.ListEnvironmentAlertRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentAlertRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['AddonName'] = request.addon_name
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironmentAlertRules',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environment_alert_rules(
        self,
        request: main_models.ListEnvironmentAlertRulesRequest,
    ) -> main_models.ListEnvironmentAlertRulesResponse:
        runtime = RuntimeOptions()
        return self.list_environment_alert_rules_with_options(request, runtime)

    async def list_environment_alert_rules_async(
        self,
        request: main_models.ListEnvironmentAlertRulesRequest,
    ) -> main_models.ListEnvironmentAlertRulesResponse:
        runtime = RuntimeOptions()
        return await self.list_environment_alert_rules_with_options_async(request, runtime)

    def list_environment_dashboards_with_options(
        self,
        request: main_models.ListEnvironmentDashboardsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentDashboardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['AddonName'] = request.addon_name
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironmentDashboards',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentDashboardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environment_dashboards_with_options_async(
        self,
        request: main_models.ListEnvironmentDashboardsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentDashboardsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['AddonName'] = request.addon_name
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scene):
            query['Scene'] = request.scene
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironmentDashboards',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentDashboardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environment_dashboards(
        self,
        request: main_models.ListEnvironmentDashboardsRequest,
    ) -> main_models.ListEnvironmentDashboardsResponse:
        runtime = RuntimeOptions()
        return self.list_environment_dashboards_with_options(request, runtime)

    async def list_environment_dashboards_async(
        self,
        request: main_models.ListEnvironmentDashboardsRequest,
    ) -> main_models.ListEnvironmentDashboardsResponse:
        runtime = RuntimeOptions()
        return await self.list_environment_dashboards_with_options_async(request, runtime)

    def list_environment_features_with_options(
        self,
        request: main_models.ListEnvironmentFeaturesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentFeaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironmentFeatures',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environment_features_with_options_async(
        self,
        request: main_models.ListEnvironmentFeaturesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentFeaturesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironmentFeatures',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environment_features(
        self,
        request: main_models.ListEnvironmentFeaturesRequest,
    ) -> main_models.ListEnvironmentFeaturesResponse:
        runtime = RuntimeOptions()
        return self.list_environment_features_with_options(request, runtime)

    async def list_environment_features_async(
        self,
        request: main_models.ListEnvironmentFeaturesRequest,
    ) -> main_models.ListEnvironmentFeaturesResponse:
        runtime = RuntimeOptions()
        return await self.list_environment_features_with_options_async(request, runtime)

    def list_environment_kube_resources_with_options(
        self,
        tmp_req: main_models.ListEnvironmentKubeResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentKubeResourcesResponse:
        tmp_req.validate()
        request = main_models.ListEnvironmentKubeResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.label_selectors):
            request.label_selectors_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_selectors, 'LabelSelectors', 'json')
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.kind):
            query['Kind'] = request.kind
        if not DaraCore.is_null(request.label_selectors_shrink):
            query['LabelSelectors'] = request.label_selectors_shrink
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironmentKubeResources',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentKubeResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environment_kube_resources_with_options_async(
        self,
        tmp_req: main_models.ListEnvironmentKubeResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentKubeResourcesResponse:
        tmp_req.validate()
        request = main_models.ListEnvironmentKubeResourcesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.label_selectors):
            request.label_selectors_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_selectors, 'LabelSelectors', 'json')
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.kind):
            query['Kind'] = request.kind
        if not DaraCore.is_null(request.label_selectors_shrink):
            query['LabelSelectors'] = request.label_selectors_shrink
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironmentKubeResources',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentKubeResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environment_kube_resources(
        self,
        request: main_models.ListEnvironmentKubeResourcesRequest,
    ) -> main_models.ListEnvironmentKubeResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_environment_kube_resources_with_options(request, runtime)

    async def list_environment_kube_resources_async(
        self,
        request: main_models.ListEnvironmentKubeResourcesRequest,
    ) -> main_models.ListEnvironmentKubeResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_environment_kube_resources_with_options_async(request, runtime)

    def list_environment_metric_targets_with_options(
        self,
        request: main_models.ListEnvironmentMetricTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentMetricTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironmentMetricTargets',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentMetricTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environment_metric_targets_with_options_async(
        self,
        request: main_models.ListEnvironmentMetricTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentMetricTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.job_name):
            query['JobName'] = request.job_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironmentMetricTargets',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentMetricTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environment_metric_targets(
        self,
        request: main_models.ListEnvironmentMetricTargetsRequest,
    ) -> main_models.ListEnvironmentMetricTargetsResponse:
        runtime = RuntimeOptions()
        return self.list_environment_metric_targets_with_options(request, runtime)

    async def list_environment_metric_targets_async(
        self,
        request: main_models.ListEnvironmentMetricTargetsRequest,
    ) -> main_models.ListEnvironmentMetricTargetsResponse:
        runtime = RuntimeOptions()
        return await self.list_environment_metric_targets_with_options_async(request, runtime)

    def list_environments_with_options(
        self,
        tmp_req: main_models.ListEnvironmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentsResponse:
        tmp_req.validate()
        request = main_models.ListEnvironmentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['AddonName'] = request.addon_name
        if not DaraCore.is_null(request.bind_resource_id):
            query['BindResourceId'] = request.bind_resource_id
        if not DaraCore.is_null(request.environment_type):
            query['EnvironmentType'] = request.environment_type
        if not DaraCore.is_null(request.fee_package):
            query['FeePackage'] = request.fee_package
        if not DaraCore.is_null(request.filter_region_ids):
            query['FilterRegionIds'] = request.filter_region_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironments',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environments_with_options_async(
        self,
        tmp_req: main_models.ListEnvironmentsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvironmentsResponse:
        tmp_req.validate()
        request = main_models.ListEnvironmentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.addon_name):
            query['AddonName'] = request.addon_name
        if not DaraCore.is_null(request.bind_resource_id):
            query['BindResourceId'] = request.bind_resource_id
        if not DaraCore.is_null(request.environment_type):
            query['EnvironmentType'] = request.environment_type
        if not DaraCore.is_null(request.fee_package):
            query['FeePackage'] = request.fee_package
        if not DaraCore.is_null(request.filter_region_ids):
            query['FilterRegionIds'] = request.filter_region_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvironments',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvironmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environments(
        self,
        request: main_models.ListEnvironmentsRequest,
    ) -> main_models.ListEnvironmentsResponse:
        runtime = RuntimeOptions()
        return self.list_environments_with_options(request, runtime)

    async def list_environments_async(
        self,
        request: main_models.ListEnvironmentsRequest,
    ) -> main_models.ListEnvironmentsResponse:
        runtime = RuntimeOptions()
        return await self.list_environments_with_options_async(request, runtime)

    def list_escalation_policies_with_options(
        self,
        request: main_models.ListEscalationPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEscalationPoliciesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEscalationPolicies',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEscalationPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_escalation_policies_with_options_async(
        self,
        request: main_models.ListEscalationPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEscalationPoliciesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEscalationPolicies',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEscalationPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_escalation_policies(
        self,
        request: main_models.ListEscalationPoliciesRequest,
    ) -> main_models.ListEscalationPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_escalation_policies_with_options(request, runtime)

    async def list_escalation_policies_async(
        self,
        request: main_models.ListEscalationPoliciesRequest,
    ) -> main_models.ListEscalationPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_escalation_policies_with_options_async(request, runtime)

    def list_event_bridge_integrations_with_options(
        self,
        request: main_models.ListEventBridgeIntegrationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEventBridgeIntegrationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEventBridgeIntegrations',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEventBridgeIntegrationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_bridge_integrations_with_options_async(
        self,
        request: main_models.ListEventBridgeIntegrationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEventBridgeIntegrationsResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEventBridgeIntegrations',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEventBridgeIntegrationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_bridge_integrations(
        self,
        request: main_models.ListEventBridgeIntegrationsRequest,
    ) -> main_models.ListEventBridgeIntegrationsResponse:
        runtime = RuntimeOptions()
        return self.list_event_bridge_integrations_with_options(request, runtime)

    async def list_event_bridge_integrations_async(
        self,
        request: main_models.ListEventBridgeIntegrationsRequest,
    ) -> main_models.ListEventBridgeIntegrationsResponse:
        runtime = RuntimeOptions()
        return await self.list_event_bridge_integrations_with_options_async(request, runtime)

    def list_grafana_workspace_with_options(
        self,
        tmp_req: main_models.ListGrafanaWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGrafanaWorkspaceResponse:
        tmp_req.validate()
        request = main_models.ListGrafanaWorkspaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGrafanaWorkspace',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGrafanaWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_grafana_workspace_with_options_async(
        self,
        tmp_req: main_models.ListGrafanaWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListGrafanaWorkspaceResponse:
        tmp_req.validate()
        request = main_models.ListGrafanaWorkspaceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGrafanaWorkspace',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGrafanaWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_grafana_workspace(
        self,
        request: main_models.ListGrafanaWorkspaceRequest,
    ) -> main_models.ListGrafanaWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.list_grafana_workspace_with_options(request, runtime)

    async def list_grafana_workspace_async(
        self,
        request: main_models.ListGrafanaWorkspaceRequest,
    ) -> main_models.ListGrafanaWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.list_grafana_workspace_with_options_async(request, runtime)

    def list_insights_events_with_options(
        self,
        request: main_models.ListInsightsEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInsightsEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.insights_types):
            query['InsightsTypes'] = request.insights_types
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
            action = 'ListInsightsEvents',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInsightsEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_insights_events_with_options_async(
        self,
        request: main_models.ListInsightsEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListInsightsEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.insights_types):
            query['InsightsTypes'] = request.insights_types
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
            action = 'ListInsightsEvents',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInsightsEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_insights_events(
        self,
        request: main_models.ListInsightsEventsRequest,
    ) -> main_models.ListInsightsEventsResponse:
        runtime = RuntimeOptions()
        return self.list_insights_events_with_options(request, runtime)

    async def list_insights_events_async(
        self,
        request: main_models.ListInsightsEventsRequest,
    ) -> main_models.ListInsightsEventsResponse:
        runtime = RuntimeOptions()
        return await self.list_insights_events_with_options_async(request, runtime)

    def list_integration_with_options(
        self,
        request: main_models.ListIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_with_options_async(
        self,
        request: main_models.ListIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListIntegrationResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration(
        self,
        request: main_models.ListIntegrationRequest,
    ) -> main_models.ListIntegrationResponse:
        runtime = RuntimeOptions()
        return self.list_integration_with_options(request, runtime)

    async def list_integration_async(
        self,
        request: main_models.ListIntegrationRequest,
    ) -> main_models.ListIntegrationResponse:
        runtime = RuntimeOptions()
        return await self.list_integration_with_options_async(request, runtime)

    def list_notification_policies_with_options(
        self,
        request: main_models.ListNotificationPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNotificationPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directed_mode):
            query['DirectedMode'] = request.directed_mode
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNotificationPolicies',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNotificationPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_notification_policies_with_options_async(
        self,
        request: main_models.ListNotificationPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListNotificationPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.directed_mode):
            query['DirectedMode'] = request.directed_mode
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListNotificationPolicies',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListNotificationPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_notification_policies(
        self,
        request: main_models.ListNotificationPoliciesRequest,
    ) -> main_models.ListNotificationPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_notification_policies_with_options(request, runtime)

    async def list_notification_policies_async(
        self,
        request: main_models.ListNotificationPoliciesRequest,
    ) -> main_models.ListNotificationPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_notification_policies_with_options_async(request, runtime)

    def list_on_call_schedules_with_options(
        self,
        request: main_models.ListOnCallSchedulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOnCallSchedulesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOnCallSchedules',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOnCallSchedulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_on_call_schedules_with_options_async(
        self,
        request: main_models.ListOnCallSchedulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOnCallSchedulesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListOnCallSchedules',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOnCallSchedulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_on_call_schedules(
        self,
        request: main_models.ListOnCallSchedulesRequest,
    ) -> main_models.ListOnCallSchedulesResponse:
        runtime = RuntimeOptions()
        return self.list_on_call_schedules_with_options(request, runtime)

    async def list_on_call_schedules_async(
        self,
        request: main_models.ListOnCallSchedulesRequest,
    ) -> main_models.ListOnCallSchedulesResponse:
        runtime = RuntimeOptions()
        return await self.list_on_call_schedules_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusAlertRules',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusAlertRules',
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def list_prometheus_global_view_with_options(
        self,
        request: main_models.ListPrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_global_view_with_options_async(
        self,
        request: main_models.ListPrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_global_view(
        self,
        request: main_models.ListPrometheusGlobalViewRequest,
    ) -> main_models.ListPrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return self.list_prometheus_global_view_with_options(request, runtime)

    async def list_prometheus_global_view_async(
        self,
        request: main_models.ListPrometheusGlobalViewRequest,
    ) -> main_models.ListPrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return await self.list_prometheus_global_view_with_options_async(request, runtime)

    def list_prometheus_instance_by_tag_and_resource_group_id_with_options(
        self,
        request: main_models.ListPrometheusInstanceByTagAndResourceGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusInstanceByTagAndResourceGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusInstanceByTagAndResourceGroupId',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusInstanceByTagAndResourceGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_instance_by_tag_and_resource_group_id_with_options_async(
        self,
        request: main_models.ListPrometheusInstanceByTagAndResourceGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusInstanceByTagAndResourceGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusInstanceByTagAndResourceGroupId',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusInstanceByTagAndResourceGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_instance_by_tag_and_resource_group_id(
        self,
        request: main_models.ListPrometheusInstanceByTagAndResourceGroupIdRequest,
    ) -> main_models.ListPrometheusInstanceByTagAndResourceGroupIdResponse:
        runtime = RuntimeOptions()
        return self.list_prometheus_instance_by_tag_and_resource_group_id_with_options(request, runtime)

    async def list_prometheus_instance_by_tag_and_resource_group_id_async(
        self,
        request: main_models.ListPrometheusInstanceByTagAndResourceGroupIdRequest,
    ) -> main_models.ListPrometheusInstanceByTagAndResourceGroupIdResponse:
        runtime = RuntimeOptions()
        return await self.list_prometheus_instance_by_tag_and_resource_group_id_with_options_async(request, runtime)

    def list_prometheus_instances_with_options(
        self,
        request: main_models.ListPrometheusInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.show_global_view):
            query['ShowGlobalView'] = request.show_global_view
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusInstances',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_instances_with_options_async(
        self,
        request: main_models.ListPrometheusInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.show_global_view):
            query['ShowGlobalView'] = request.show_global_view
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusInstances',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_instances(
        self,
        request: main_models.ListPrometheusInstancesRequest,
    ) -> main_models.ListPrometheusInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_prometheus_instances_with_options(request, runtime)

    async def list_prometheus_instances_async(
        self,
        request: main_models.ListPrometheusInstancesRequest,
    ) -> main_models.ListPrometheusInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_prometheus_instances_with_options_async(request, runtime)

    def list_prometheus_integration_with_options(
        self,
        request: main_models.ListPrometheusIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusIntegrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_integration_with_options_async(
        self,
        request: main_models.ListPrometheusIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusIntegrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_integration(
        self,
        request: main_models.ListPrometheusIntegrationRequest,
    ) -> main_models.ListPrometheusIntegrationResponse:
        runtime = RuntimeOptions()
        return self.list_prometheus_integration_with_options(request, runtime)

    async def list_prometheus_integration_async(
        self,
        request: main_models.ListPrometheusIntegrationRequest,
    ) -> main_models.ListPrometheusIntegrationResponse:
        runtime = RuntimeOptions()
        return await self.list_prometheus_integration_with_options_async(request, runtime)

    def list_prometheus_monitoring_with_options(
        self,
        request: main_models.ListPrometheusMonitoringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusMonitoringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusMonitoring',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_monitoring_with_options_async(
        self,
        request: main_models.ListPrometheusMonitoringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrometheusMonitoringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrometheusMonitoring',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrometheusMonitoringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_monitoring(
        self,
        request: main_models.ListPrometheusMonitoringRequest,
    ) -> main_models.ListPrometheusMonitoringResponse:
        runtime = RuntimeOptions()
        return self.list_prometheus_monitoring_with_options(request, runtime)

    async def list_prometheus_monitoring_async(
        self,
        request: main_models.ListPrometheusMonitoringRequest,
    ) -> main_models.ListPrometheusMonitoringResponse:
        runtime = RuntimeOptions()
        return await self.list_prometheus_monitoring_with_options_async(request, runtime)

    def list_retcode_apps_with_options(
        self,
        request: main_models.ListRetcodeAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRetcodeAppsResponse:
        request.validate()
        query = {}
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
            action = 'ListRetcodeApps',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRetcodeApps',
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def list_silence_policies_with_options(
        self,
        request: main_models.ListSilencePoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSilencePoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSilencePolicies',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSilencePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_silence_policies_with_options_async(
        self,
        request: main_models.ListSilencePoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSilencePoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSilencePolicies',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSilencePoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_silence_policies(
        self,
        request: main_models.ListSilencePoliciesRequest,
    ) -> main_models.ListSilencePoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_silence_policies_with_options(request, runtime)

    async def list_silence_policies_async(
        self,
        request: main_models.ListSilencePoliciesRequest,
    ) -> main_models.ListSilencePoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_silence_policies_with_options_async(request, runtime)

    def list_synthetic_detail_with_options(
        self,
        tmp_req: main_models.ListSyntheticDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSyntheticDetailResponse:
        tmp_req.validate()
        request = main_models.ListSyntheticDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.advanced_filters):
            request.advanced_filters_shrink = Utils.array_to_string_with_specified_style(tmp_req.advanced_filters, 'AdvancedFilters', 'json')
        if not DaraCore.is_null(tmp_req.exact_filters):
            request.exact_filters_shrink = Utils.array_to_string_with_specified_style(tmp_req.exact_filters, 'ExactFilters', 'json')
        if not DaraCore.is_null(tmp_req.filters):
            request.filters_shrink = Utils.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSyntheticDetail',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSyntheticDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_synthetic_detail_with_options_async(
        self,
        tmp_req: main_models.ListSyntheticDetailRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSyntheticDetailResponse:
        tmp_req.validate()
        request = main_models.ListSyntheticDetailShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.advanced_filters):
            request.advanced_filters_shrink = Utils.array_to_string_with_specified_style(tmp_req.advanced_filters, 'AdvancedFilters', 'json')
        if not DaraCore.is_null(tmp_req.exact_filters):
            request.exact_filters_shrink = Utils.array_to_string_with_specified_style(tmp_req.exact_filters, 'ExactFilters', 'json')
        if not DaraCore.is_null(tmp_req.filters):
            request.filters_shrink = Utils.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSyntheticDetail',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSyntheticDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_synthetic_detail(
        self,
        request: main_models.ListSyntheticDetailRequest,
    ) -> main_models.ListSyntheticDetailResponse:
        runtime = RuntimeOptions()
        return self.list_synthetic_detail_with_options(request, runtime)

    async def list_synthetic_detail_async(
        self,
        request: main_models.ListSyntheticDetailRequest,
    ) -> main_models.ListSyntheticDetailResponse:
        runtime = RuntimeOptions()
        return await self.list_synthetic_detail_with_options_async(request, runtime)

    def list_timing_synthetic_tasks_with_options(
        self,
        tmp_req: main_models.ListTimingSyntheticTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTimingSyntheticTasksResponse:
        tmp_req.validate()
        request = main_models.ListTimingSyntheticTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.search):
            request.search_shrink = Utils.array_to_string_with_specified_style(tmp_req.search, 'Search', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTimingSyntheticTasks',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTimingSyntheticTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_timing_synthetic_tasks_with_options_async(
        self,
        tmp_req: main_models.ListTimingSyntheticTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTimingSyntheticTasksResponse:
        tmp_req.validate()
        request = main_models.ListTimingSyntheticTasksShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.search):
            request.search_shrink = Utils.array_to_string_with_specified_style(tmp_req.search, 'Search', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTimingSyntheticTasks',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTimingSyntheticTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_timing_synthetic_tasks(
        self,
        request: main_models.ListTimingSyntheticTasksRequest,
    ) -> main_models.ListTimingSyntheticTasksResponse:
        runtime = RuntimeOptions()
        return self.list_timing_synthetic_tasks_with_options(request, runtime)

    async def list_timing_synthetic_tasks_async(
        self,
        request: main_models.ListTimingSyntheticTasksRequest,
    ) -> main_models.ListTimingSyntheticTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_timing_synthetic_tasks_with_options_async(request, runtime)

    def list_trace_apps_with_options(
        self,
        request: main_models.ListTraceAppsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTraceAppsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
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
            action = 'ListTraceApps',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
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
            action = 'ListTraceApps',
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def open_arms_service_second_version_with_options(
        self,
        request: main_models.OpenArmsServiceSecondVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenArmsServiceSecondVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenArmsServiceSecondVersion',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenArmsServiceSecondVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_arms_service_second_version_with_options_async(
        self,
        request: main_models.OpenArmsServiceSecondVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.OpenArmsServiceSecondVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'OpenArmsServiceSecondVersion',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenArmsServiceSecondVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_arms_service_second_version(
        self,
        request: main_models.OpenArmsServiceSecondVersionRequest,
    ) -> main_models.OpenArmsServiceSecondVersionResponse:
        runtime = RuntimeOptions()
        return self.open_arms_service_second_version_with_options(request, runtime)

    async def open_arms_service_second_version_async(
        self,
        request: main_models.OpenArmsServiceSecondVersionRequest,
    ) -> main_models.OpenArmsServiceSecondVersionResponse:
        runtime = RuntimeOptions()
        return await self.open_arms_service_second_version_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def query_app_metadata_with_options(
        self,
        request: main_models.QueryAppMetadataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAppMetadataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAppMetadata',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAppMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_app_metadata_with_options_async(
        self,
        request: main_models.QueryAppMetadataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAppMetadataResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAppMetadata',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAppMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_app_metadata(
        self,
        request: main_models.QueryAppMetadataRequest,
    ) -> main_models.QueryAppMetadataResponse:
        runtime = RuntimeOptions()
        return self.query_app_metadata_with_options(request, runtime)

    async def query_app_metadata_async(
        self,
        request: main_models.QueryAppMetadataRequest,
    ) -> main_models.QueryAppMetadataResponse:
        runtime = RuntimeOptions()
        return await self.query_app_metadata_with_options_async(request, runtime)

    def query_app_topology_with_options(
        self,
        tmp_req: main_models.QueryAppTopologyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAppTopologyResponse:
        tmp_req.validate()
        request = main_models.QueryAppTopologyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filters):
            request.filters_shrink = Utils.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        query = {}
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.db):
            query['Db'] = request.db
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters_shrink):
            query['Filters'] = request.filters_shrink
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rpc):
            query['Rpc'] = request.rpc
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAppTopology',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAppTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_app_topology_with_options_async(
        self,
        tmp_req: main_models.QueryAppTopologyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryAppTopologyResponse:
        tmp_req.validate()
        request = main_models.QueryAppTopologyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filters):
            request.filters_shrink = Utils.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        query = {}
        if not DaraCore.is_null(request.app_type):
            query['AppType'] = request.app_type
        if not DaraCore.is_null(request.db):
            query['Db'] = request.db
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filters_shrink):
            query['Filters'] = request.filters_shrink
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.rpc):
            query['Rpc'] = request.rpc
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryAppTopology',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryAppTopologyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_app_topology(
        self,
        request: main_models.QueryAppTopologyRequest,
    ) -> main_models.QueryAppTopologyResponse:
        runtime = RuntimeOptions()
        return self.query_app_topology_with_options(request, runtime)

    async def query_app_topology_async(
        self,
        request: main_models.QueryAppTopologyRequest,
    ) -> main_models.QueryAppTopologyResponse:
        runtime = RuntimeOptions()
        return await self.query_app_topology_with_options_async(request, runtime)

    def query_commercial_usage_with_options(
        self,
        request: main_models.QueryCommercialUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCommercialUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.advanced_filters):
            query['AdvancedFilters'] = request.advanced_filters
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
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
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCommercialUsage',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCommercialUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_commercial_usage_with_options_async(
        self,
        request: main_models.QueryCommercialUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCommercialUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.advanced_filters):
            query['AdvancedFilters'] = request.advanced_filters
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
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
        if not DaraCore.is_null(request.query_type):
            query['QueryType'] = request.query_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCommercialUsage',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCommercialUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_commercial_usage(
        self,
        request: main_models.QueryCommercialUsageRequest,
    ) -> main_models.QueryCommercialUsageResponse:
        runtime = RuntimeOptions()
        return self.query_commercial_usage_with_options(request, runtime)

    async def query_commercial_usage_async(
        self,
        request: main_models.QueryCommercialUsageRequest,
    ) -> main_models.QueryCommercialUsageResponse:
        runtime = RuntimeOptions()
        return await self.query_commercial_usage_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def query_prom_install_status_with_options(
        self,
        request: main_models.QueryPromInstallStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPromInstallStatusResponse:
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
            action = 'QueryPromInstallStatus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPromInstallStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_prom_install_status_with_options_async(
        self,
        request: main_models.QueryPromInstallStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryPromInstallStatusResponse:
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
            action = 'QueryPromInstallStatus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryPromInstallStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_prom_install_status(
        self,
        request: main_models.QueryPromInstallStatusRequest,
    ) -> main_models.QueryPromInstallStatusResponse:
        runtime = RuntimeOptions()
        return self.query_prom_install_status_with_options(request, runtime)

    async def query_prom_install_status_async(
        self,
        request: main_models.QueryPromInstallStatusRequest,
    ) -> main_models.QueryPromInstallStatusResponse:
        runtime = RuntimeOptions()
        return await self.query_prom_install_status_with_options_async(request, runtime)

    def query_release_metric_with_options(
        self,
        request: main_models.QueryReleaseMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryReleaseMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        if not DaraCore.is_null(request.create_time):
            query['CreateTime'] = request.create_time
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.release_end_time):
            query['ReleaseEndTime'] = request.release_end_time
        if not DaraCore.is_null(request.release_start_time):
            query['ReleaseStartTime'] = request.release_start_time
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryReleaseMetric',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryReleaseMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_release_metric_with_options_async(
        self,
        request: main_models.QueryReleaseMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryReleaseMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        if not DaraCore.is_null(request.create_time):
            query['CreateTime'] = request.create_time
        if not DaraCore.is_null(request.metric_type):
            query['MetricType'] = request.metric_type
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not DaraCore.is_null(request.release_end_time):
            query['ReleaseEndTime'] = request.release_end_time
        if not DaraCore.is_null(request.release_start_time):
            query['ReleaseStartTime'] = request.release_start_time
        if not DaraCore.is_null(request.service):
            query['Service'] = request.service
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryReleaseMetric',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryReleaseMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_release_metric(
        self,
        request: main_models.QueryReleaseMetricRequest,
    ) -> main_models.QueryReleaseMetricResponse:
        runtime = RuntimeOptions()
        return self.query_release_metric_with_options(request, runtime)

    async def query_release_metric_async(
        self,
        request: main_models.QueryReleaseMetricRequest,
    ) -> main_models.QueryReleaseMetricResponse:
        runtime = RuntimeOptions()
        return await self.query_release_metric_with_options_async(request, runtime)

    def remove_ali_cluster_ids_from_prometheus_global_view_with_options(
        self,
        request: main_models.RemoveAliClusterIdsFromPrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAliClusterIdsFromPrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not DaraCore.is_null(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveAliClusterIdsFromPrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAliClusterIdsFromPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_ali_cluster_ids_from_prometheus_global_view_with_options_async(
        self,
        request: main_models.RemoveAliClusterIdsFromPrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAliClusterIdsFromPrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not DaraCore.is_null(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveAliClusterIdsFromPrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAliClusterIdsFromPrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_ali_cluster_ids_from_prometheus_global_view(
        self,
        request: main_models.RemoveAliClusterIdsFromPrometheusGlobalViewRequest,
    ) -> main_models.RemoveAliClusterIdsFromPrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return self.remove_ali_cluster_ids_from_prometheus_global_view_with_options(request, runtime)

    async def remove_ali_cluster_ids_from_prometheus_global_view_async(
        self,
        request: main_models.RemoveAliClusterIdsFromPrometheusGlobalViewRequest,
    ) -> main_models.RemoveAliClusterIdsFromPrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return await self.remove_ali_cluster_ids_from_prometheus_global_view_with_options_async(request, runtime)

    def remove_sources_from_prometheus_global_view_with_options(
        self,
        request: main_models.RemoveSourcesFromPrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveSourcesFromPrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source_names):
            query['SourceNames'] = request.source_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveSourcesFromPrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveSourcesFromPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_sources_from_prometheus_global_view_with_options_async(
        self,
        request: main_models.RemoveSourcesFromPrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveSourcesFromPrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.source_names):
            query['SourceNames'] = request.source_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveSourcesFromPrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveSourcesFromPrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_sources_from_prometheus_global_view(
        self,
        request: main_models.RemoveSourcesFromPrometheusGlobalViewRequest,
    ) -> main_models.RemoveSourcesFromPrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return self.remove_sources_from_prometheus_global_view_with_options(request, runtime)

    async def remove_sources_from_prometheus_global_view_async(
        self,
        request: main_models.RemoveSourcesFromPrometheusGlobalViewRequest,
    ) -> main_models.RemoveSourcesFromPrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return await self.remove_sources_from_prometheus_global_view_with_options_async(request, runtime)

    def restart_environment_feature_with_options(
        self,
        request: main_models.RestartEnvironmentFeatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartEnvironmentFeatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartEnvironmentFeature',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartEnvironmentFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_environment_feature_with_options_async(
        self,
        request: main_models.RestartEnvironmentFeatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartEnvironmentFeatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartEnvironmentFeature',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartEnvironmentFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_environment_feature(
        self,
        request: main_models.RestartEnvironmentFeatureRequest,
    ) -> main_models.RestartEnvironmentFeatureResponse:
        runtime = RuntimeOptions()
        return self.restart_environment_feature_with_options(request, runtime)

    async def restart_environment_feature_async(
        self,
        request: main_models.RestartEnvironmentFeatureRequest,
    ) -> main_models.RestartEnvironmentFeatureResponse:
        runtime = RuntimeOptions()
        return await self.restart_environment_feature_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.alert_rule_id):
            query['AlertRuleId'] = request.alert_rule_id
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.system_region_id):
            query['SystemRegionId'] = request.system_region_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchAlertRules',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.alert_rule_id):
            query['AlertRuleId'] = request.alert_rule_id
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.system_region_id):
            query['SystemRegionId'] = request.system_region_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.title):
            query['Title'] = request.title
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchAlertRules',
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.retcode_app_id):
            query['RetcodeAppId'] = request.retcode_app_id
        if not DaraCore.is_null(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchRetcodeAppByPage',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.retcode_app_id):
            query['RetcodeAppId'] = request.retcode_app_id
        if not DaraCore.is_null(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchRetcodeAppByPage',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.trace_app_name):
            query['TraceAppName'] = request.trace_app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTraceAppByName',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.trace_app_name):
            query['TraceAppName'] = request.trace_app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTraceAppByName',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.trace_app_name):
            query['TraceAppName'] = request.trace_app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTraceAppByPage',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.trace_app_name):
            query['TraceAppName'] = request.trace_app_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTraceAppByPage',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
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
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
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
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.is_error):
            query['IsError'] = request.is_error
        if not DaraCore.is_null(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not DaraCore.is_null(request.operation_name):
            query['OperationName'] = request.operation_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
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
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTracesByPage',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.is_error):
            query['IsError'] = request.is_error
        if not DaraCore.is_null(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not DaraCore.is_null(request.operation_name):
            query['OperationName'] = request.operation_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
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
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTracesByPage',
            version = '2019-08-08',
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

    def send_ttsverify_link_with_options(
        self,
        request: main_models.SendTTSVerifyLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendTTSVerifyLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.phone):
            body['Phone'] = request.phone
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendTTSVerifyLink',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendTTSVerifyLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_ttsverify_link_with_options_async(
        self,
        request: main_models.SendTTSVerifyLinkRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendTTSVerifyLinkResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.contact_id):
            body['ContactId'] = request.contact_id
        if not DaraCore.is_null(request.phone):
            body['Phone'] = request.phone
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SendTTSVerifyLink',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendTTSVerifyLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_ttsverify_link(
        self,
        request: main_models.SendTTSVerifyLinkRequest,
    ) -> main_models.SendTTSVerifyLinkResponse:
        runtime = RuntimeOptions()
        return self.send_ttsverify_link_with_options(request, runtime)

    async def send_ttsverify_link_async(
        self,
        request: main_models.SendTTSVerifyLinkRequest,
    ) -> main_models.SendTTSVerifyLinkResponse:
        runtime = RuntimeOptions()
        return await self.send_ttsverify_link_with_options_async(request, runtime)

    def set_retcode_share_status_with_options(
        self,
        request: main_models.SetRetcodeShareStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetRetcodeShareStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetRetcodeShareStatus',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.app_name):
            query['AppName'] = request.app_name
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetRetcodeShareStatus',
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def start_timing_synthetic_task_with_options(
        self,
        tmp_req: main_models.StartTimingSyntheticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartTimingSyntheticTaskResponse:
        tmp_req.validate()
        request = main_models.StartTimingSyntheticTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartTimingSyntheticTask',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartTimingSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_timing_synthetic_task_with_options_async(
        self,
        tmp_req: main_models.StartTimingSyntheticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartTimingSyntheticTaskResponse:
        tmp_req.validate()
        request = main_models.StartTimingSyntheticTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartTimingSyntheticTask',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartTimingSyntheticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_timing_synthetic_task(
        self,
        request: main_models.StartTimingSyntheticTaskRequest,
    ) -> main_models.StartTimingSyntheticTaskResponse:
        runtime = RuntimeOptions()
        return self.start_timing_synthetic_task_with_options(request, runtime)

    async def start_timing_synthetic_task_async(
        self,
        request: main_models.StartTimingSyntheticTaskRequest,
    ) -> main_models.StartTimingSyntheticTaskResponse:
        runtime = RuntimeOptions()
        return await self.start_timing_synthetic_task_with_options_async(request, runtime)

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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def stop_timing_synthetic_task_with_options(
        self,
        tmp_req: main_models.StopTimingSyntheticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopTimingSyntheticTaskResponse:
        tmp_req.validate()
        request = main_models.StopTimingSyntheticTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopTimingSyntheticTask',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTimingSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_timing_synthetic_task_with_options_async(
        self,
        tmp_req: main_models.StopTimingSyntheticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopTimingSyntheticTaskResponse:
        tmp_req.validate()
        request = main_models.StopTimingSyntheticTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.task_ids):
            request.task_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopTimingSyntheticTask',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopTimingSyntheticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_timing_synthetic_task(
        self,
        request: main_models.StopTimingSyntheticTaskRequest,
    ) -> main_models.StopTimingSyntheticTaskResponse:
        runtime = RuntimeOptions()
        return self.stop_timing_synthetic_task_with_options(request, runtime)

    async def stop_timing_synthetic_task_async(
        self,
        request: main_models.StopTimingSyntheticTaskRequest,
    ) -> main_models.StopTimingSyntheticTaskResponse:
        runtime = RuntimeOptions()
        return await self.stop_timing_synthetic_task_with_options_async(request, runtime)

    def switch_synthetic_task_status_with_options(
        self,
        request: main_models.SwitchSyntheticTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchSyntheticTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.switch_status):
            query['SwitchStatus'] = request.switch_status
        if not DaraCore.is_null(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchSyntheticTaskStatus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchSyntheticTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_synthetic_task_status_with_options_async(
        self,
        request: main_models.SwitchSyntheticTaskStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SwitchSyntheticTaskStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.switch_status):
            query['SwitchStatus'] = request.switch_status
        if not DaraCore.is_null(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SwitchSyntheticTaskStatus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SwitchSyntheticTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_synthetic_task_status(
        self,
        request: main_models.SwitchSyntheticTaskStatusRequest,
    ) -> main_models.SwitchSyntheticTaskStatusResponse:
        runtime = RuntimeOptions()
        return self.switch_synthetic_task_status_with_options(request, runtime)

    async def switch_synthetic_task_status_async(
        self,
        request: main_models.SwitchSyntheticTaskStatusRequest,
    ) -> main_models.SwitchSyntheticTaskStatusResponse:
        runtime = RuntimeOptions()
        return await self.switch_synthetic_task_status_with_options_async(request, runtime)

    def sync_recording_rules_with_options(
        self,
        request: main_models.SyncRecordingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncRecordingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.target_clusters):
            query['TargetClusters'] = request.target_clusters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncRecordingRules',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncRecordingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_recording_rules_with_options_async(
        self,
        request: main_models.SyncRecordingRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SyncRecordingRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.target_clusters):
            query['TargetClusters'] = request.target_clusters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SyncRecordingRules',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncRecordingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_recording_rules(
        self,
        request: main_models.SyncRecordingRulesRequest,
    ) -> main_models.SyncRecordingRulesResponse:
        runtime = RuntimeOptions()
        return self.sync_recording_rules_with_options(request, runtime)

    async def sync_recording_rules_async(
        self,
        request: main_models.SyncRecordingRulesRequest,
    ) -> main_models.SyncRecordingRulesResponse:
        runtime = RuntimeOptions()
        return await self.sync_recording_rules_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-08-08',
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

    def uninstall_managed_prometheus_with_options(
        self,
        request: main_models.UninstallManagedPrometheusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallManagedPrometheusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UninstallManagedPrometheus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallManagedPrometheusResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_managed_prometheus_with_options_async(
        self,
        request: main_models.UninstallManagedPrometheusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallManagedPrometheusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UninstallManagedPrometheus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallManagedPrometheusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_managed_prometheus(
        self,
        request: main_models.UninstallManagedPrometheusRequest,
    ) -> main_models.UninstallManagedPrometheusResponse:
        runtime = RuntimeOptions()
        return self.uninstall_managed_prometheus_with_options(request, runtime)

    async def uninstall_managed_prometheus_async(
        self,
        request: main_models.UninstallManagedPrometheusRequest,
    ) -> main_models.UninstallManagedPrometheusResponse:
        runtime = RuntimeOptions()
        return await self.uninstall_managed_prometheus_with_options_async(request, runtime)

    def uninstall_prom_cluster_with_options(
        self,
        request: main_models.UninstallPromClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallPromClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UninstallPromCluster',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallPromClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_prom_cluster_with_options_async(
        self,
        request: main_models.UninstallPromClusterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallPromClusterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UninstallPromCluster',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallPromClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_prom_cluster(
        self,
        request: main_models.UninstallPromClusterRequest,
    ) -> main_models.UninstallPromClusterResponse:
        runtime = RuntimeOptions()
        return self.uninstall_prom_cluster_with_options(request, runtime)

    async def uninstall_prom_cluster_async(
        self,
        request: main_models.UninstallPromClusterRequest,
    ) -> main_models.UninstallPromClusterResponse:
        runtime = RuntimeOptions()
        return await self.uninstall_prom_cluster_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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
            version = '2019-08-08',
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

    def update_env_custom_job_with_options(
        self,
        request: main_models.UpdateEnvCustomJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnvCustomJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.custom_job_name):
            query['CustomJobName'] = request.custom_job_name
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        body = {}
        if not DaraCore.is_null(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnvCustomJob',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnvCustomJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_env_custom_job_with_options_async(
        self,
        request: main_models.UpdateEnvCustomJobRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnvCustomJobResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.custom_job_name):
            query['CustomJobName'] = request.custom_job_name
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        body = {}
        if not DaraCore.is_null(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnvCustomJob',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnvCustomJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_env_custom_job(
        self,
        request: main_models.UpdateEnvCustomJobRequest,
    ) -> main_models.UpdateEnvCustomJobResponse:
        runtime = RuntimeOptions()
        return self.update_env_custom_job_with_options(request, runtime)

    async def update_env_custom_job_async(
        self,
        request: main_models.UpdateEnvCustomJobRequest,
    ) -> main_models.UpdateEnvCustomJobResponse:
        runtime = RuntimeOptions()
        return await self.update_env_custom_job_with_options_async(request, runtime)

    def update_env_drop_metrics_rule_with_options(
        self,
        request: main_models.UpdateEnvDropMetricsRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnvDropMetricsRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.drop_metrics):
            body['DropMetrics'] = request.drop_metrics
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnvDropMetricsRule',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnvDropMetricsRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_env_drop_metrics_rule_with_options_async(
        self,
        request: main_models.UpdateEnvDropMetricsRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnvDropMetricsRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.drop_metrics):
            body['DropMetrics'] = request.drop_metrics
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnvDropMetricsRule',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnvDropMetricsRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_env_drop_metrics_rule(
        self,
        request: main_models.UpdateEnvDropMetricsRuleRequest,
    ) -> main_models.UpdateEnvDropMetricsRuleResponse:
        runtime = RuntimeOptions()
        return self.update_env_drop_metrics_rule_with_options(request, runtime)

    async def update_env_drop_metrics_rule_async(
        self,
        request: main_models.UpdateEnvDropMetricsRuleRequest,
    ) -> main_models.UpdateEnvDropMetricsRuleResponse:
        runtime = RuntimeOptions()
        return await self.update_env_drop_metrics_rule_with_options_async(request, runtime)

    def update_env_pod_monitor_with_options(
        self,
        request: main_models.UpdateEnvPodMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnvPodMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.pod_monitor_name):
            query['PodMonitorName'] = request.pod_monitor_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnvPodMonitor',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnvPodMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_env_pod_monitor_with_options_async(
        self,
        request: main_models.UpdateEnvPodMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnvPodMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.pod_monitor_name):
            query['PodMonitorName'] = request.pod_monitor_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not DaraCore.is_null(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnvPodMonitor',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnvPodMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_env_pod_monitor(
        self,
        request: main_models.UpdateEnvPodMonitorRequest,
    ) -> main_models.UpdateEnvPodMonitorResponse:
        runtime = RuntimeOptions()
        return self.update_env_pod_monitor_with_options(request, runtime)

    async def update_env_pod_monitor_async(
        self,
        request: main_models.UpdateEnvPodMonitorRequest,
    ) -> main_models.UpdateEnvPodMonitorResponse:
        runtime = RuntimeOptions()
        return await self.update_env_pod_monitor_with_options_async(request, runtime)

    def update_env_service_monitor_with_options(
        self,
        request: main_models.UpdateEnvServiceMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnvServiceMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_monitor_name):
            query['ServiceMonitorName'] = request.service_monitor_name
        body = {}
        if not DaraCore.is_null(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnvServiceMonitor',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnvServiceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_env_service_monitor_with_options_async(
        self,
        request: main_models.UpdateEnvServiceMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnvServiceMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_monitor_name):
            query['ServiceMonitorName'] = request.service_monitor_name
        body = {}
        if not DaraCore.is_null(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnvServiceMonitor',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnvServiceMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_env_service_monitor(
        self,
        request: main_models.UpdateEnvServiceMonitorRequest,
    ) -> main_models.UpdateEnvServiceMonitorResponse:
        runtime = RuntimeOptions()
        return self.update_env_service_monitor_with_options(request, runtime)

    async def update_env_service_monitor_async(
        self,
        request: main_models.UpdateEnvServiceMonitorRequest,
    ) -> main_models.UpdateEnvServiceMonitorResponse:
        runtime = RuntimeOptions()
        return await self.update_env_service_monitor_with_options_async(request, runtime)

    def update_environment_with_options(
        self,
        request: main_models.UpdateEnvironmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnvironmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.environment_name):
            query['EnvironmentName'] = request.environment_name
        if not DaraCore.is_null(request.fee_package):
            query['FeePackage'] = request.fee_package
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnvironment',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_environment_with_options_async(
        self,
        request: main_models.UpdateEnvironmentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnvironmentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.environment_name):
            query['EnvironmentName'] = request.environment_name
        if not DaraCore.is_null(request.fee_package):
            query['FeePackage'] = request.fee_package
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnvironment',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_environment(
        self,
        request: main_models.UpdateEnvironmentRequest,
    ) -> main_models.UpdateEnvironmentResponse:
        runtime = RuntimeOptions()
        return self.update_environment_with_options(request, runtime)

    async def update_environment_async(
        self,
        request: main_models.UpdateEnvironmentRequest,
    ) -> main_models.UpdateEnvironmentResponse:
        runtime = RuntimeOptions()
        return await self.update_environment_with_options_async(request, runtime)

    def update_grafana_workspace_with_options(
        self,
        request: main_models.UpdateGrafanaWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGrafanaWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not DaraCore.is_null(request.grafana_workspace_name):
            query['GrafanaWorkspaceName'] = request.grafana_workspace_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGrafanaWorkspace',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGrafanaWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_grafana_workspace_with_options_async(
        self,
        request: main_models.UpdateGrafanaWorkspaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGrafanaWorkspaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not DaraCore.is_null(request.grafana_workspace_name):
            query['GrafanaWorkspaceName'] = request.grafana_workspace_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGrafanaWorkspace',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGrafanaWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_grafana_workspace(
        self,
        request: main_models.UpdateGrafanaWorkspaceRequest,
    ) -> main_models.UpdateGrafanaWorkspaceResponse:
        runtime = RuntimeOptions()
        return self.update_grafana_workspace_with_options(request, runtime)

    async def update_grafana_workspace_async(
        self,
        request: main_models.UpdateGrafanaWorkspaceRequest,
    ) -> main_models.UpdateGrafanaWorkspaceResponse:
        runtime = RuntimeOptions()
        return await self.update_grafana_workspace_with_options_async(request, runtime)

    def update_grafana_workspace_version_with_options(
        self,
        request: main_models.UpdateGrafanaWorkspaceVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGrafanaWorkspaceVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.grafana_version):
            query['GrafanaVersion'] = request.grafana_version
        if not DaraCore.is_null(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGrafanaWorkspaceVersion',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGrafanaWorkspaceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_grafana_workspace_version_with_options_async(
        self,
        request: main_models.UpdateGrafanaWorkspaceVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateGrafanaWorkspaceVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.grafana_version):
            query['GrafanaVersion'] = request.grafana_version
        if not DaraCore.is_null(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateGrafanaWorkspaceVersion',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateGrafanaWorkspaceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_grafana_workspace_version(
        self,
        request: main_models.UpdateGrafanaWorkspaceVersionRequest,
    ) -> main_models.UpdateGrafanaWorkspaceVersionResponse:
        runtime = RuntimeOptions()
        return self.update_grafana_workspace_version_with_options(request, runtime)

    async def update_grafana_workspace_version_async(
        self,
        request: main_models.UpdateGrafanaWorkspaceVersionRequest,
    ) -> main_models.UpdateGrafanaWorkspaceVersionResponse:
        runtime = RuntimeOptions()
        return await self.update_grafana_workspace_version_with_options_async(request, runtime)

    def update_integration_with_options(
        self,
        request: main_models.UpdateIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIntegrationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_recover):
            body['AutoRecover'] = request.auto_recover
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.duplicate_key):
            body['DuplicateKey'] = request.duplicate_key
        if not DaraCore.is_null(request.extended_field_redefine_rules):
            body['ExtendedFieldRedefineRules'] = request.extended_field_redefine_rules
        if not DaraCore.is_null(request.field_redefine_rules):
            body['FieldRedefineRules'] = request.field_redefine_rules
        if not DaraCore.is_null(request.initiative_recover_field):
            body['InitiativeRecoverField'] = request.initiative_recover_field
        if not DaraCore.is_null(request.initiative_recover_value):
            body['InitiativeRecoverValue'] = request.initiative_recover_value
        if not DaraCore.is_null(request.integration_id):
            body['IntegrationId'] = request.integration_id
        if not DaraCore.is_null(request.integration_name):
            body['IntegrationName'] = request.integration_name
        if not DaraCore.is_null(request.integration_product_type):
            body['IntegrationProductType'] = request.integration_product_type
        if not DaraCore.is_null(request.liveness):
            body['Liveness'] = request.liveness
        if not DaraCore.is_null(request.recover_time):
            body['RecoverTime'] = request.recover_time
        if not DaraCore.is_null(request.stat):
            body['Stat'] = request.stat
        if not DaraCore.is_null(request.state):
            body['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_integration_with_options_async(
        self,
        request: main_models.UpdateIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateIntegrationResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.auto_recover):
            body['AutoRecover'] = request.auto_recover
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.duplicate_key):
            body['DuplicateKey'] = request.duplicate_key
        if not DaraCore.is_null(request.extended_field_redefine_rules):
            body['ExtendedFieldRedefineRules'] = request.extended_field_redefine_rules
        if not DaraCore.is_null(request.field_redefine_rules):
            body['FieldRedefineRules'] = request.field_redefine_rules
        if not DaraCore.is_null(request.initiative_recover_field):
            body['InitiativeRecoverField'] = request.initiative_recover_field
        if not DaraCore.is_null(request.initiative_recover_value):
            body['InitiativeRecoverValue'] = request.initiative_recover_value
        if not DaraCore.is_null(request.integration_id):
            body['IntegrationId'] = request.integration_id
        if not DaraCore.is_null(request.integration_name):
            body['IntegrationName'] = request.integration_name
        if not DaraCore.is_null(request.integration_product_type):
            body['IntegrationProductType'] = request.integration_product_type
        if not DaraCore.is_null(request.liveness):
            body['Liveness'] = request.liveness
        if not DaraCore.is_null(request.recover_time):
            body['RecoverTime'] = request.recover_time
        if not DaraCore.is_null(request.stat):
            body['Stat'] = request.stat
        if not DaraCore.is_null(request.state):
            body['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_integration(
        self,
        request: main_models.UpdateIntegrationRequest,
    ) -> main_models.UpdateIntegrationResponse:
        runtime = RuntimeOptions()
        return self.update_integration_with_options(request, runtime)

    async def update_integration_async(
        self,
        request: main_models.UpdateIntegrationRequest,
    ) -> main_models.UpdateIntegrationResponse:
        runtime = RuntimeOptions()
        return await self.update_integration_with_options_async(request, runtime)

    def update_metric_drop_with_options(
        self,
        request: main_models.UpdateMetricDropRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMetricDropResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.metric_drop):
            query['MetricDrop'] = request.metric_drop
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMetricDrop',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMetricDropResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_metric_drop_with_options_async(
        self,
        request: main_models.UpdateMetricDropRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMetricDropResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.metric_drop):
            query['MetricDrop'] = request.metric_drop
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMetricDrop',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMetricDropResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_metric_drop(
        self,
        request: main_models.UpdateMetricDropRequest,
    ) -> main_models.UpdateMetricDropResponse:
        runtime = RuntimeOptions()
        return self.update_metric_drop_with_options(request, runtime)

    async def update_metric_drop_async(
        self,
        request: main_models.UpdateMetricDropRequest,
    ) -> main_models.UpdateMetricDropResponse:
        runtime = RuntimeOptions()
        return await self.update_metric_drop_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusAlertRule',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusAlertRule',
            version = '2019-08-08',
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

    def update_prometheus_global_view_with_options(
        self,
        request: main_models.UpdatePrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all_sub_clusters_success):
            query['AllSubClustersSuccess'] = request.all_sub_clusters_success
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.most_region_id):
            query['MostRegionId'] = request.most_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sub_clusters_json):
            query['SubClustersJson'] = request.sub_clusters_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_global_view_with_options_async(
        self,
        request: main_models.UpdatePrometheusGlobalViewRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusGlobalViewResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all_sub_clusters_success):
            query['AllSubClustersSuccess'] = request.all_sub_clusters_success
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.most_region_id):
            query['MostRegionId'] = request.most_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.sub_clusters_json):
            query['SubClustersJson'] = request.sub_clusters_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusGlobalView',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_global_view(
        self,
        request: main_models.UpdatePrometheusGlobalViewRequest,
    ) -> main_models.UpdatePrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return self.update_prometheus_global_view_with_options(request, runtime)

    async def update_prometheus_global_view_async(
        self,
        request: main_models.UpdatePrometheusGlobalViewRequest,
    ) -> main_models.UpdatePrometheusGlobalViewResponse:
        runtime = RuntimeOptions()
        return await self.update_prometheus_global_view_with_options_async(request, runtime)

    def update_prometheus_instance_with_options(
        self,
        request: main_models.UpdatePrometheusInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.archive_duration):
            query['ArchiveDuration'] = request.archive_duration
        if not DaraCore.is_null(request.auth_free_read_policy):
            query['AuthFreeReadPolicy'] = request.auth_free_read_policy
        if not DaraCore.is_null(request.auth_free_write_policy):
            query['AuthFreeWritePolicy'] = request.auth_free_write_policy
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.enable_auth_free_read):
            query['EnableAuthFreeRead'] = request.enable_auth_free_read
        if not DaraCore.is_null(request.enable_auth_free_write):
            query['EnableAuthFreeWrite'] = request.enable_auth_free_write
        if not DaraCore.is_null(request.enable_auth_token):
            query['EnableAuthToken'] = request.enable_auth_token
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.storage_duration):
            query['StorageDuration'] = request.storage_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusInstance',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_instance_with_options_async(
        self,
        request: main_models.UpdatePrometheusInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.archive_duration):
            query['ArchiveDuration'] = request.archive_duration
        if not DaraCore.is_null(request.auth_free_read_policy):
            query['AuthFreeReadPolicy'] = request.auth_free_read_policy
        if not DaraCore.is_null(request.auth_free_write_policy):
            query['AuthFreeWritePolicy'] = request.auth_free_write_policy
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.enable_auth_free_read):
            query['EnableAuthFreeRead'] = request.enable_auth_free_read
        if not DaraCore.is_null(request.enable_auth_free_write):
            query['EnableAuthFreeWrite'] = request.enable_auth_free_write
        if not DaraCore.is_null(request.enable_auth_token):
            query['EnableAuthToken'] = request.enable_auth_token
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.storage_duration):
            query['StorageDuration'] = request.storage_duration
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusInstance',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_instance(
        self,
        request: main_models.UpdatePrometheusInstanceRequest,
    ) -> main_models.UpdatePrometheusInstanceResponse:
        runtime = RuntimeOptions()
        return self.update_prometheus_instance_with_options(request, runtime)

    async def update_prometheus_instance_async(
        self,
        request: main_models.UpdatePrometheusInstanceRequest,
    ) -> main_models.UpdatePrometheusInstanceResponse:
        runtime = RuntimeOptions()
        return await self.update_prometheus_instance_with_options_async(request, runtime)

    def update_prometheus_integration_with_options(
        self,
        request: main_models.UpdatePrometheusIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusIntegrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_integration_with_options_async(
        self,
        request: main_models.UpdatePrometheusIntegrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusIntegrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not DaraCore.is_null(request.param):
            query['Param'] = request.param
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusIntegration',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_integration(
        self,
        request: main_models.UpdatePrometheusIntegrationRequest,
    ) -> main_models.UpdatePrometheusIntegrationResponse:
        runtime = RuntimeOptions()
        return self.update_prometheus_integration_with_options(request, runtime)

    async def update_prometheus_integration_async(
        self,
        request: main_models.UpdatePrometheusIntegrationRequest,
    ) -> main_models.UpdatePrometheusIntegrationResponse:
        runtime = RuntimeOptions()
        return await self.update_prometheus_integration_with_options_async(request, runtime)

    def update_prometheus_monitoring_with_options(
        self,
        request: main_models.UpdatePrometheusMonitoringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusMonitoringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        body = {}
        if not DaraCore.is_null(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusMonitoring',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_monitoring_with_options_async(
        self,
        request: main_models.UpdatePrometheusMonitoringRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusMonitoringResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        body = {}
        if not DaraCore.is_null(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePrometheusMonitoring',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusMonitoringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_monitoring(
        self,
        request: main_models.UpdatePrometheusMonitoringRequest,
    ) -> main_models.UpdatePrometheusMonitoringResponse:
        runtime = RuntimeOptions()
        return self.update_prometheus_monitoring_with_options(request, runtime)

    async def update_prometheus_monitoring_async(
        self,
        request: main_models.UpdatePrometheusMonitoringRequest,
    ) -> main_models.UpdatePrometheusMonitoringResponse:
        runtime = RuntimeOptions()
        return await self.update_prometheus_monitoring_with_options_async(request, runtime)

    def update_prometheus_monitoring_status_with_options(
        self,
        request: main_models.UpdatePrometheusMonitoringStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusMonitoringStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
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
            action = 'UpdatePrometheusMonitoringStatus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusMonitoringStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_monitoring_status_with_options_async(
        self,
        request: main_models.UpdatePrometheusMonitoringStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePrometheusMonitoringStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not DaraCore.is_null(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
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
            action = 'UpdatePrometheusMonitoringStatus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePrometheusMonitoringStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_monitoring_status(
        self,
        request: main_models.UpdatePrometheusMonitoringStatusRequest,
    ) -> main_models.UpdatePrometheusMonitoringStatusResponse:
        runtime = RuntimeOptions()
        return self.update_prometheus_monitoring_status_with_options(request, runtime)

    async def update_prometheus_monitoring_status_async(
        self,
        request: main_models.UpdatePrometheusMonitoringStatusRequest,
    ) -> main_models.UpdatePrometheusMonitoringStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_prometheus_monitoring_status_with_options_async(request, runtime)

    def update_rum_app_with_options(
        self,
        request: main_models.UpdateRumAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRumAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_config):
            query['AppConfig'] = request.app_config
        if not DaraCore.is_null(request.auto_restart):
            query['AutoRestart'] = request.auto_restart
        if not DaraCore.is_null(request.backend_service_trace_region):
            query['BackendServiceTraceRegion'] = request.backend_service_trace_region
        if not DaraCore.is_null(request.bonree_sdkconfig_json):
            query['BonreeSDKConfigJson'] = request.bonree_sdkconfig_json
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.is_subscribe):
            query['IsSubscribe'] = request.is_subscribe
        if not DaraCore.is_null(request.nickname):
            query['Nickname'] = request.nickname
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.real_region_id):
            query['RealRegionId'] = request.real_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.restart):
            query['Restart'] = request.restart
        if not DaraCore.is_null(request.service_domain_operation_json):
            query['ServiceDomainOperationJson'] = request.service_domain_operation_json
        if not DaraCore.is_null(request.stop):
            query['Stop'] = request.stop
        if not DaraCore.is_null(request.web_sdkconfig_json):
            query['WebSDKConfigJson'] = request.web_sdkconfig_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRumApp',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRumAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rum_app_with_options_async(
        self,
        request: main_models.UpdateRumAppRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRumAppResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.app_config):
            query['AppConfig'] = request.app_config
        if not DaraCore.is_null(request.auto_restart):
            query['AutoRestart'] = request.auto_restart
        if not DaraCore.is_null(request.backend_service_trace_region):
            query['BackendServiceTraceRegion'] = request.backend_service_trace_region
        if not DaraCore.is_null(request.bonree_sdkconfig_json):
            query['BonreeSDKConfigJson'] = request.bonree_sdkconfig_json
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.is_subscribe):
            query['IsSubscribe'] = request.is_subscribe
        if not DaraCore.is_null(request.nickname):
            query['Nickname'] = request.nickname
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.real_region_id):
            query['RealRegionId'] = request.real_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.restart):
            query['Restart'] = request.restart
        if not DaraCore.is_null(request.service_domain_operation_json):
            query['ServiceDomainOperationJson'] = request.service_domain_operation_json
        if not DaraCore.is_null(request.stop):
            query['Stop'] = request.stop
        if not DaraCore.is_null(request.web_sdkconfig_json):
            query['WebSDKConfigJson'] = request.web_sdkconfig_json
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRumApp',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRumAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rum_app(
        self,
        request: main_models.UpdateRumAppRequest,
    ) -> main_models.UpdateRumAppResponse:
        runtime = RuntimeOptions()
        return self.update_rum_app_with_options(request, runtime)

    async def update_rum_app_async(
        self,
        request: main_models.UpdateRumAppRequest,
    ) -> main_models.UpdateRumAppResponse:
        runtime = RuntimeOptions()
        return await self.update_rum_app_with_options_async(request, runtime)

    def update_rum_file_status_with_options(
        self,
        request: main_models.UpdateRumFileStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRumFileStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRumFileStatus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRumFileStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rum_file_status_with_options_async(
        self,
        request: main_models.UpdateRumFileStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRumFileStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.size):
            query['Size'] = request.size
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.uuid):
            query['Uuid'] = request.uuid
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRumFileStatus',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRumFileStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rum_file_status(
        self,
        request: main_models.UpdateRumFileStatusRequest,
    ) -> main_models.UpdateRumFileStatusResponse:
        runtime = RuntimeOptions()
        return self.update_rum_file_status_with_options(request, runtime)

    async def update_rum_file_status_async(
        self,
        request: main_models.UpdateRumFileStatusRequest,
    ) -> main_models.UpdateRumFileStatusResponse:
        runtime = RuntimeOptions()
        return await self.update_rum_file_status_with_options_async(request, runtime)

    def update_timing_synthetic_task_with_options(
        self,
        tmp_req: main_models.UpdateTimingSyntheticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTimingSyntheticTaskResponse:
        tmp_req.validate()
        request = main_models.UpdateTimingSyntheticTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.available_assertions):
            request.available_assertions_shrink = Utils.array_to_string_with_specified_style(tmp_req.available_assertions, 'AvailableAssertions', 'json')
        if not DaraCore.is_null(tmp_req.common_setting):
            request.common_setting_shrink = Utils.array_to_string_with_specified_style(tmp_req.common_setting, 'CommonSetting', 'json')
        if not DaraCore.is_null(tmp_req.custom_period):
            request.custom_period_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_period, 'CustomPeriod', 'json')
        if not DaraCore.is_null(tmp_req.monitor_conf):
            request.monitor_conf_shrink = Utils.array_to_string_with_specified_style(tmp_req.monitor_conf, 'MonitorConf', 'json')
        if not DaraCore.is_null(tmp_req.monitors):
            request.monitors_shrink = Utils.array_to_string_with_specified_style(tmp_req.monitors, 'Monitors', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.available_assertions_shrink):
            query['AvailableAssertions'] = request.available_assertions_shrink
        if not DaraCore.is_null(request.common_setting_shrink):
            query['CommonSetting'] = request.common_setting_shrink
        if not DaraCore.is_null(request.custom_period_shrink):
            query['CustomPeriod'] = request.custom_period_shrink
        if not DaraCore.is_null(request.frequency):
            query['Frequency'] = request.frequency
        if not DaraCore.is_null(request.monitor_conf_shrink):
            query['MonitorConf'] = request.monitor_conf_shrink
        if not DaraCore.is_null(request.monitors_shrink):
            query['Monitors'] = request.monitors_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTimingSyntheticTask',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTimingSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_timing_synthetic_task_with_options_async(
        self,
        tmp_req: main_models.UpdateTimingSyntheticTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTimingSyntheticTaskResponse:
        tmp_req.validate()
        request = main_models.UpdateTimingSyntheticTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.available_assertions):
            request.available_assertions_shrink = Utils.array_to_string_with_specified_style(tmp_req.available_assertions, 'AvailableAssertions', 'json')
        if not DaraCore.is_null(tmp_req.common_setting):
            request.common_setting_shrink = Utils.array_to_string_with_specified_style(tmp_req.common_setting, 'CommonSetting', 'json')
        if not DaraCore.is_null(tmp_req.custom_period):
            request.custom_period_shrink = Utils.array_to_string_with_specified_style(tmp_req.custom_period, 'CustomPeriod', 'json')
        if not DaraCore.is_null(tmp_req.monitor_conf):
            request.monitor_conf_shrink = Utils.array_to_string_with_specified_style(tmp_req.monitor_conf, 'MonitorConf', 'json')
        if not DaraCore.is_null(tmp_req.monitors):
            request.monitors_shrink = Utils.array_to_string_with_specified_style(tmp_req.monitors, 'Monitors', 'json')
        if not DaraCore.is_null(tmp_req.tags):
            request.tags_shrink = Utils.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not DaraCore.is_null(request.available_assertions_shrink):
            query['AvailableAssertions'] = request.available_assertions_shrink
        if not DaraCore.is_null(request.common_setting_shrink):
            query['CommonSetting'] = request.common_setting_shrink
        if not DaraCore.is_null(request.custom_period_shrink):
            query['CustomPeriod'] = request.custom_period_shrink
        if not DaraCore.is_null(request.frequency):
            query['Frequency'] = request.frequency
        if not DaraCore.is_null(request.monitor_conf_shrink):
            query['MonitorConf'] = request.monitor_conf_shrink
        if not DaraCore.is_null(request.monitors_shrink):
            query['Monitors'] = request.monitors_shrink
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTimingSyntheticTask',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTimingSyntheticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_timing_synthetic_task(
        self,
        request: main_models.UpdateTimingSyntheticTaskRequest,
    ) -> main_models.UpdateTimingSyntheticTaskResponse:
        runtime = RuntimeOptions()
        return self.update_timing_synthetic_task_with_options(request, runtime)

    async def update_timing_synthetic_task_async(
        self,
        request: main_models.UpdateTimingSyntheticTaskRequest,
    ) -> main_models.UpdateTimingSyntheticTaskResponse:
        runtime = RuntimeOptions()
        return await self.update_timing_synthetic_task_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.recover_body):
            query['RecoverBody'] = request.recover_body
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWebhook',
            version = '2019-08-08',
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
        if not DaraCore.is_null(request.recover_body):
            query['RecoverBody'] = request.recover_body
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.url):
            query['Url'] = request.url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateWebhook',
            version = '2019-08-08',
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

    def upgrade_addon_release_with_options(
        self,
        request: main_models.UpgradeAddonReleaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeAddonReleaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.release_name):
            query['ReleaseName'] = request.release_name
        if not DaraCore.is_null(request.values):
            query['Values'] = request.values
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeAddonRelease',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeAddonReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_addon_release_with_options_async(
        self,
        request: main_models.UpgradeAddonReleaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeAddonReleaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.release_name):
            query['ReleaseName'] = request.release_name
        if not DaraCore.is_null(request.values):
            query['Values'] = request.values
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeAddonRelease',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeAddonReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_addon_release(
        self,
        request: main_models.UpgradeAddonReleaseRequest,
    ) -> main_models.UpgradeAddonReleaseResponse:
        runtime = RuntimeOptions()
        return self.upgrade_addon_release_with_options(request, runtime)

    async def upgrade_addon_release_async(
        self,
        request: main_models.UpgradeAddonReleaseRequest,
    ) -> main_models.UpgradeAddonReleaseResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_addon_release_with_options_async(request, runtime)

    def upgrade_environment_feature_with_options(
        self,
        request: main_models.UpgradeEnvironmentFeatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeEnvironmentFeatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not DaraCore.is_null(request.feature_version):
            query['FeatureVersion'] = request.feature_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.values):
            query['Values'] = request.values
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeEnvironmentFeature',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeEnvironmentFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_environment_feature_with_options_async(
        self,
        request: main_models.UpgradeEnvironmentFeatureRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeEnvironmentFeatureResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not DaraCore.is_null(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not DaraCore.is_null(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not DaraCore.is_null(request.feature_version):
            query['FeatureVersion'] = request.feature_version
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.values):
            query['Values'] = request.values
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeEnvironmentFeature',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeEnvironmentFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_environment_feature(
        self,
        request: main_models.UpgradeEnvironmentFeatureRequest,
    ) -> main_models.UpgradeEnvironmentFeatureResponse:
        runtime = RuntimeOptions()
        return self.upgrade_environment_feature_with_options(request, runtime)

    async def upgrade_environment_feature_async(
        self,
        request: main_models.UpgradeEnvironmentFeatureRequest,
    ) -> main_models.UpgradeEnvironmentFeatureResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_environment_feature_with_options_async(request, runtime)

    def upload_with_options(
        self,
        request: main_models.UploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.file):
            body['File'] = request.file
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Upload',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_with_options_async(
        self,
        request: main_models.UploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.edition):
            query['Edition'] = request.edition
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.pid):
            query['Pid'] = request.pid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.version):
            query['Version'] = request.version
        body = {}
        if not DaraCore.is_null(request.file):
            body['File'] = request.file
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Upload',
            version = '2019-08-08',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload(
        self,
        request: main_models.UploadRequest,
    ) -> main_models.UploadResponse:
        runtime = RuntimeOptions()
        return self.upload_with_options(request, runtime)

    async def upload_async(
        self,
        request: main_models.UploadRequest,
    ) -> main_models.UploadResponse:
        runtime = RuntimeOptions()
        return await self.upload_with_options_async(request, runtime)
