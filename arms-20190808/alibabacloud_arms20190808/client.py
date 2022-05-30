# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_arms20190808 import models as arms20190808_models
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

    def add_asmintegration_with_options(
        self,
        request: arms20190808_models.AddASMIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddASMIntegrationResponse:
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
            action='AddASMIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddASMIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_asmintegration_with_options_async(
        self,
        request: arms20190808_models.AddASMIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddASMIntegrationResponse:
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
            action='AddASMIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddASMIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_asmintegration(
        self,
        request: arms20190808_models.AddASMIntegrationRequest,
    ) -> arms20190808_models.AddASMIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_asmintegration_with_options(request, runtime)

    async def add_asmintegration_async(
        self,
        request: arms20190808_models.AddASMIntegrationRequest,
    ) -> arms20190808_models.AddASMIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_asmintegration_with_options_async(request, runtime)

    def add_ali_cluster_ids_to_prometheus_global_view_with_options(
        self,
        request: arms20190808_models.AddAliClusterIdsToPrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddAliClusterIdsToPrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAliClusterIdsToPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddAliClusterIdsToPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_ali_cluster_ids_to_prometheus_global_view_with_options_async(
        self,
        request: arms20190808_models.AddAliClusterIdsToPrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddAliClusterIdsToPrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAliClusterIdsToPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddAliClusterIdsToPrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_ali_cluster_ids_to_prometheus_global_view(
        self,
        request: arms20190808_models.AddAliClusterIdsToPrometheusGlobalViewRequest,
    ) -> arms20190808_models.AddAliClusterIdsToPrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_ali_cluster_ids_to_prometheus_global_view_with_options(request, runtime)

    async def add_ali_cluster_ids_to_prometheus_global_view_async(
        self,
        request: arms20190808_models.AddAliClusterIdsToPrometheusGlobalViewRequest,
    ) -> arms20190808_models.AddAliClusterIdsToPrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_ali_cluster_ids_to_prometheus_global_view_with_options_async(request, runtime)

    def add_grafana_with_options(
        self,
        request: arms20190808_models.AddGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddGrafanaResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddGrafanaResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_grafana_with_options_async(
        self,
        request: arms20190808_models.AddGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddGrafanaResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddGrafanaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_grafana(
        self,
        request: arms20190808_models.AddGrafanaRequest,
    ) -> arms20190808_models.AddGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_grafana_with_options(request, runtime)

    async def add_grafana_async(
        self,
        request: arms20190808_models.AddGrafanaRequest,
    ) -> arms20190808_models.AddGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_grafana_with_options_async(request, runtime)

    def add_integration_with_options(
        self,
        request: arms20190808_models.AddIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddIntegrationResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_integration_with_options_async(
        self,
        request: arms20190808_models.AddIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddIntegrationResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_integration(
        self,
        request: arms20190808_models.AddIntegrationRequest,
    ) -> arms20190808_models.AddIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_integration_with_options(request, runtime)

    async def add_integration_async(
        self,
        request: arms20190808_models.AddIntegrationRequest,
    ) -> arms20190808_models.AddIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_integration_with_options_async(request, runtime)

    def add_prometheus_global_view_with_options(
        self,
        request: arms20190808_models.AddPrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddPrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.clusters):
            query['Clusters'] = request.clusters
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_prometheus_global_view_with_options_async(
        self,
        request: arms20190808_models.AddPrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddPrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.clusters):
            query['Clusters'] = request.clusters
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddPrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_prometheus_global_view(
        self,
        request: arms20190808_models.AddPrometheusGlobalViewRequest,
    ) -> arms20190808_models.AddPrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_prometheus_global_view_with_options(request, runtime)

    async def add_prometheus_global_view_async(
        self,
        request: arms20190808_models.AddPrometheusGlobalViewRequest,
    ) -> arms20190808_models.AddPrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_prometheus_global_view_with_options_async(request, runtime)

    def add_prometheus_global_view_by_ali_cluster_ids_with_options(
        self,
        request: arms20190808_models.AddPrometheusGlobalViewByAliClusterIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddPrometheusGlobalViewByAliClusterIdsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPrometheusGlobalViewByAliClusterIds',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddPrometheusGlobalViewByAliClusterIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_prometheus_global_view_by_ali_cluster_ids_with_options_async(
        self,
        request: arms20190808_models.AddPrometheusGlobalViewByAliClusterIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddPrometheusGlobalViewByAliClusterIdsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPrometheusGlobalViewByAliClusterIds',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddPrometheusGlobalViewByAliClusterIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_prometheus_global_view_by_ali_cluster_ids(
        self,
        request: arms20190808_models.AddPrometheusGlobalViewByAliClusterIdsRequest,
    ) -> arms20190808_models.AddPrometheusGlobalViewByAliClusterIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_prometheus_global_view_by_ali_cluster_ids_with_options(request, runtime)

    async def add_prometheus_global_view_by_ali_cluster_ids_async(
        self,
        request: arms20190808_models.AddPrometheusGlobalViewByAliClusterIdsRequest,
    ) -> arms20190808_models.AddPrometheusGlobalViewByAliClusterIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_prometheus_global_view_by_ali_cluster_ids_with_options_async(request, runtime)

    def add_recording_rule_with_options(
        self,
        request: arms20190808_models.AddRecordingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddRecordingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_yaml):
            query['RuleYaml'] = request.rule_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRecordingRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddRecordingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_recording_rule_with_options_async(
        self,
        request: arms20190808_models.AddRecordingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddRecordingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_yaml):
            query['RuleYaml'] = request.rule_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRecordingRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddRecordingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_recording_rule(
        self,
        request: arms20190808_models.AddRecordingRuleRequest,
    ) -> arms20190808_models.AddRecordingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_recording_rule_with_options(request, runtime)

    async def add_recording_rule_async(
        self,
        request: arms20190808_models.AddRecordingRuleRequest,
    ) -> arms20190808_models.AddRecordingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_recording_rule_with_options_async(request, runtime)

    def append_instances_to_prometheus_global_view_with_options(
        self,
        request: arms20190808_models.AppendInstancesToPrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AppendInstancesToPrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.clusters):
            query['Clusters'] = request.clusters
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AppendInstancesToPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AppendInstancesToPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def append_instances_to_prometheus_global_view_with_options_async(
        self,
        request: arms20190808_models.AppendInstancesToPrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AppendInstancesToPrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.clusters):
            query['Clusters'] = request.clusters
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AppendInstancesToPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AppendInstancesToPrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def append_instances_to_prometheus_global_view(
        self,
        request: arms20190808_models.AppendInstancesToPrometheusGlobalViewRequest,
    ) -> arms20190808_models.AppendInstancesToPrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return self.append_instances_to_prometheus_global_view_with_options(request, runtime)

    async def append_instances_to_prometheus_global_view_async(
        self,
        request: arms20190808_models.AppendInstancesToPrometheusGlobalViewRequest,
    ) -> arms20190808_models.AppendInstancesToPrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.append_instances_to_prometheus_global_view_with_options_async(request, runtime)

    def apply_scenario_with_options(
        self,
        tmp_req: arms20190808_models.ApplyScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ApplyScenarioResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.ApplyScenarioShrinkRequest()
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ApplyScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_scenario_with_options_async(
        self,
        tmp_req: arms20190808_models.ApplyScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ApplyScenarioResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.ApplyScenarioShrinkRequest()
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ApplyScenarioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_scenario(
        self,
        request: arms20190808_models.ApplyScenarioRequest,
    ) -> arms20190808_models.ApplyScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_scenario_with_options(request, runtime)

    async def apply_scenario_async(
        self,
        request: arms20190808_models.ApplyScenarioRequest,
    ) -> arms20190808_models.ApplyScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_scenario_with_options_async(request, runtime)

    def c_monitor_alert_event_with_options(
        self,
        request: arms20190808_models.CMonitorAlertEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CMonitorAlertEventResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CMonitorAlertEvent',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CMonitorAlertEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def c_monitor_alert_event_with_options_async(
        self,
        request: arms20190808_models.CMonitorAlertEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CMonitorAlertEventResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CMonitorAlertEvent',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CMonitorAlertEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def c_monitor_alert_event(
        self,
        request: arms20190808_models.CMonitorAlertEventRequest,
    ) -> arms20190808_models.CMonitorAlertEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.c_monitor_alert_event_with_options(request, runtime)

    async def c_monitor_alert_event_async(
        self,
        request: arms20190808_models.CMonitorAlertEventRequest,
    ) -> arms20190808_models.CMonitorAlertEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.c_monitor_alert_event_with_options_async(request, runtime)

    def check_service_status_with_options(
        self,
        request: arms20190808_models.CheckServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CheckServiceStatusResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CheckServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_status_with_options_async(
        self,
        request: arms20190808_models.CheckServiceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CheckServiceStatusResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CheckServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_status(
        self,
        request: arms20190808_models.CheckServiceStatusRequest,
    ) -> arms20190808_models.CheckServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.check_service_status_with_options(request, runtime)

    async def check_service_status_async(
        self,
        request: arms20190808_models.CheckServiceStatusRequest,
    ) -> arms20190808_models.CheckServiceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.check_service_status_with_options_async(request, runtime)

    def config_app_with_options(
        self,
        request: arms20190808_models.ConfigAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ConfigAppResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ConfigAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def config_app_with_options_async(
        self,
        request: arms20190808_models.ConfigAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ConfigAppResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ConfigAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def config_app(
        self,
        request: arms20190808_models.ConfigAppRequest,
    ) -> arms20190808_models.ConfigAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.config_app_with_options(request, runtime)

    async def config_app_async(
        self,
        request: arms20190808_models.ConfigAppRequest,
    ) -> arms20190808_models.ConfigAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.config_app_with_options_async(request, runtime)

    def create_alert_contact_with_options(
        self,
        request: arms20190808_models.CreateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateAlertContactResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alert_contact_with_options_async(
        self,
        request: arms20190808_models.CreateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateAlertContactResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alert_contact(
        self,
        request: arms20190808_models.CreateAlertContactRequest,
    ) -> arms20190808_models.CreateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_alert_contact_with_options(request, runtime)

    async def create_alert_contact_async(
        self,
        request: arms20190808_models.CreateAlertContactRequest,
    ) -> arms20190808_models.CreateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_alert_contact_with_options_async(request, runtime)

    def create_alert_contact_group_with_options(
        self,
        request: arms20190808_models.CreateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateAlertContactGroupResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_alert_contact_group_with_options_async(
        self,
        request: arms20190808_models.CreateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateAlertContactGroupResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_alert_contact_group(
        self,
        request: arms20190808_models.CreateAlertContactGroupRequest,
    ) -> arms20190808_models.CreateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_alert_contact_group_with_options(request, runtime)

    async def create_alert_contact_group_async(
        self,
        request: arms20190808_models.CreateAlertContactGroupRequest,
    ) -> arms20190808_models.CreateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_alert_contact_group_with_options_async(request, runtime)

    def create_dispatch_rule_with_options(
        self,
        request: arms20190808_models.CreateDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateDispatchRuleResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dispatch_rule_with_options_async(
        self,
        request: arms20190808_models.CreateDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateDispatchRuleResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateDispatchRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dispatch_rule(
        self,
        request: arms20190808_models.CreateDispatchRuleRequest,
    ) -> arms20190808_models.CreateDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dispatch_rule_with_options(request, runtime)

    async def create_dispatch_rule_async(
        self,
        request: arms20190808_models.CreateDispatchRuleRequest,
    ) -> arms20190808_models.CreateDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dispatch_rule_with_options_async(request, runtime)

    def create_or_update_alert_rule_with_options(
        self,
        request: arms20190808_models.CreateOrUpdateAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateOrUpdateAlertRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_check_type):
            body['AlertCheckType'] = request.alert_check_type
        if not UtilClient.is_unset(request.alert_group):
            body['AlertGroup'] = request.alert_group
        if not UtilClient.is_unset(request.alert_id):
            body['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.alert_name):
            body['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.alert_rule_content):
            body['AlertRuleContent'] = request.alert_rule_content
        if not UtilClient.is_unset(request.alert_status):
            body['AlertStatus'] = request.alert_status
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.annotations):
            body['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.auto_add_new_application):
            body['AutoAddNewApplication'] = request.auto_add_new_application
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.filters):
            body['Filters'] = request.filters
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.message):
            body['Message'] = request.message
        if not UtilClient.is_unset(request.metrics_key):
            body['MetricsKey'] = request.metrics_key
        if not UtilClient.is_unset(request.metrics_type):
            body['MetricsType'] = request.metrics_type
        if not UtilClient.is_unset(request.notify_strategy):
            body['NotifyStrategy'] = request.notify_strategy
        if not UtilClient.is_unset(request.pids):
            body['Pids'] = request.pids
        if not UtilClient.is_unset(request.prom_ql):
            body['PromQL'] = request.prom_ql
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateAlertRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_alert_rule_with_options_async(
        self,
        request: arms20190808_models.CreateOrUpdateAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateOrUpdateAlertRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_check_type):
            body['AlertCheckType'] = request.alert_check_type
        if not UtilClient.is_unset(request.alert_group):
            body['AlertGroup'] = request.alert_group
        if not UtilClient.is_unset(request.alert_id):
            body['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.alert_name):
            body['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.alert_rule_content):
            body['AlertRuleContent'] = request.alert_rule_content
        if not UtilClient.is_unset(request.alert_status):
            body['AlertStatus'] = request.alert_status
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.annotations):
            body['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.auto_add_new_application):
            body['AutoAddNewApplication'] = request.auto_add_new_application
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.filters):
            body['Filters'] = request.filters
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.message):
            body['Message'] = request.message
        if not UtilClient.is_unset(request.metrics_key):
            body['MetricsKey'] = request.metrics_key
        if not UtilClient.is_unset(request.metrics_type):
            body['MetricsType'] = request.metrics_type
        if not UtilClient.is_unset(request.notify_strategy):
            body['NotifyStrategy'] = request.notify_strategy
        if not UtilClient.is_unset(request.pids):
            body['Pids'] = request.pids
        if not UtilClient.is_unset(request.prom_ql):
            body['PromQL'] = request.prom_ql
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateAlertRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_alert_rule(
        self,
        request: arms20190808_models.CreateOrUpdateAlertRuleRequest,
    ) -> arms20190808_models.CreateOrUpdateAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_alert_rule_with_options(request, runtime)

    async def create_or_update_alert_rule_async(
        self,
        request: arms20190808_models.CreateOrUpdateAlertRuleRequest,
    ) -> arms20190808_models.CreateOrUpdateAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_or_update_alert_rule_with_options_async(request, runtime)

    def create_or_update_contact_with_options(
        self,
        request: arms20190808_models.CreateOrUpdateContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateOrUpdateContactResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.contact_id):
            body['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_name):
            body['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateContact',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_contact_with_options_async(
        self,
        request: arms20190808_models.CreateOrUpdateContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateOrUpdateContactResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.contact_id):
            body['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_name):
            body['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateContact',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_contact(
        self,
        request: arms20190808_models.CreateOrUpdateContactRequest,
    ) -> arms20190808_models.CreateOrUpdateContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_contact_with_options(request, runtime)

    async def create_or_update_contact_async(
        self,
        request: arms20190808_models.CreateOrUpdateContactRequest,
    ) -> arms20190808_models.CreateOrUpdateContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_or_update_contact_with_options_async(request, runtime)

    def create_or_update_contact_group_with_options(
        self,
        request: arms20190808_models.CreateOrUpdateContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateOrUpdateContactGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.contact_group_id):
            body['ContactGroupId'] = request.contact_group_id
        if not UtilClient.is_unset(request.contact_group_name):
            body['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.contact_ids):
            body['ContactIds'] = request.contact_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateContactGroup',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_contact_group_with_options_async(
        self,
        request: arms20190808_models.CreateOrUpdateContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateOrUpdateContactGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.contact_group_id):
            body['ContactGroupId'] = request.contact_group_id
        if not UtilClient.is_unset(request.contact_group_name):
            body['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.contact_ids):
            body['ContactIds'] = request.contact_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateContactGroup',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_contact_group(
        self,
        request: arms20190808_models.CreateOrUpdateContactGroupRequest,
    ) -> arms20190808_models.CreateOrUpdateContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_contact_group_with_options(request, runtime)

    async def create_or_update_contact_group_async(
        self,
        request: arms20190808_models.CreateOrUpdateContactGroupRequest,
    ) -> arms20190808_models.CreateOrUpdateContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_or_update_contact_group_with_options_async(request, runtime)

    def create_or_update_event_bridge_integration_with_options(
        self,
        request: arms20190808_models.CreateOrUpdateEventBridgeIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateOrUpdateEventBridgeIntegrationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key):
            body['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.access_secret):
            body['AccessSecret'] = request.access_secret
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.endpoint):
            body['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_bus_region_id):
            body['EventBusRegionId'] = request.event_bus_region_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateEventBridgeIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateEventBridgeIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_event_bridge_integration_with_options_async(
        self,
        request: arms20190808_models.CreateOrUpdateEventBridgeIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateOrUpdateEventBridgeIntegrationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key):
            body['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.access_secret):
            body['AccessSecret'] = request.access_secret
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.endpoint):
            body['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_bus_region_id):
            body['EventBusRegionId'] = request.event_bus_region_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateEventBridgeIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateEventBridgeIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_event_bridge_integration(
        self,
        request: arms20190808_models.CreateOrUpdateEventBridgeIntegrationRequest,
    ) -> arms20190808_models.CreateOrUpdateEventBridgeIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_event_bridge_integration_with_options(request, runtime)

    async def create_or_update_event_bridge_integration_async(
        self,
        request: arms20190808_models.CreateOrUpdateEventBridgeIntegrationRequest,
    ) -> arms20190808_models.CreateOrUpdateEventBridgeIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_or_update_event_bridge_integration_with_options_async(request, runtime)

    def create_or_update_imrobot_with_options(
        self,
        request: arms20190808_models.CreateOrUpdateIMRobotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateOrUpdateIMRobotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.daily_noc):
            body['DailyNoc'] = request.daily_noc
        if not UtilClient.is_unset(request.daily_noc_time):
            body['DailyNocTime'] = request.daily_noc_time
        if not UtilClient.is_unset(request.robot_address):
            body['RobotAddress'] = request.robot_address
        if not UtilClient.is_unset(request.robot_id):
            body['RobotId'] = request.robot_id
        if not UtilClient.is_unset(request.robot_name):
            body['RobotName'] = request.robot_name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateIMRobot',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateIMRobotResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_imrobot_with_options_async(
        self,
        request: arms20190808_models.CreateOrUpdateIMRobotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateOrUpdateIMRobotResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.daily_noc):
            body['DailyNoc'] = request.daily_noc
        if not UtilClient.is_unset(request.daily_noc_time):
            body['DailyNocTime'] = request.daily_noc_time
        if not UtilClient.is_unset(request.robot_address):
            body['RobotAddress'] = request.robot_address
        if not UtilClient.is_unset(request.robot_id):
            body['RobotId'] = request.robot_id
        if not UtilClient.is_unset(request.robot_name):
            body['RobotName'] = request.robot_name
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateIMRobot',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateIMRobotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_imrobot(
        self,
        request: arms20190808_models.CreateOrUpdateIMRobotRequest,
    ) -> arms20190808_models.CreateOrUpdateIMRobotResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_imrobot_with_options(request, runtime)

    async def create_or_update_imrobot_async(
        self,
        request: arms20190808_models.CreateOrUpdateIMRobotRequest,
    ) -> arms20190808_models.CreateOrUpdateIMRobotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_or_update_imrobot_with_options_async(request, runtime)

    def create_or_update_notification_policy_with_options(
        self,
        request: arms20190808_models.CreateOrUpdateNotificationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateOrUpdateNotificationPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.escalation_policy_id):
            body['EscalationPolicyId'] = request.escalation_policy_id
        if not UtilClient.is_unset(request.group_rule):
            body['GroupRule'] = request.group_rule
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.integration_id):
            body['IntegrationId'] = request.integration_id
        if not UtilClient.is_unset(request.matching_rules):
            body['MatchingRules'] = request.matching_rules
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.notify_rule):
            body['NotifyRule'] = request.notify_rule
        if not UtilClient.is_unset(request.notify_template):
            body['NotifyTemplate'] = request.notify_template
        if not UtilClient.is_unset(request.repeat):
            body['Repeat'] = request.repeat
        if not UtilClient.is_unset(request.repeat_interval):
            body['RepeatInterval'] = request.repeat_interval
        if not UtilClient.is_unset(request.send_recover_message):
            body['SendRecoverMessage'] = request.send_recover_message
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateNotificationPolicy',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateNotificationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_notification_policy_with_options_async(
        self,
        request: arms20190808_models.CreateOrUpdateNotificationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateOrUpdateNotificationPolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.escalation_policy_id):
            body['EscalationPolicyId'] = request.escalation_policy_id
        if not UtilClient.is_unset(request.group_rule):
            body['GroupRule'] = request.group_rule
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.integration_id):
            body['IntegrationId'] = request.integration_id
        if not UtilClient.is_unset(request.matching_rules):
            body['MatchingRules'] = request.matching_rules
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.notify_rule):
            body['NotifyRule'] = request.notify_rule
        if not UtilClient.is_unset(request.notify_template):
            body['NotifyTemplate'] = request.notify_template
        if not UtilClient.is_unset(request.repeat):
            body['Repeat'] = request.repeat
        if not UtilClient.is_unset(request.repeat_interval):
            body['RepeatInterval'] = request.repeat_interval
        if not UtilClient.is_unset(request.send_recover_message):
            body['SendRecoverMessage'] = request.send_recover_message
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateNotificationPolicy',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateNotificationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_notification_policy(
        self,
        request: arms20190808_models.CreateOrUpdateNotificationPolicyRequest,
    ) -> arms20190808_models.CreateOrUpdateNotificationPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_notification_policy_with_options(request, runtime)

    async def create_or_update_notification_policy_async(
        self,
        request: arms20190808_models.CreateOrUpdateNotificationPolicyRequest,
    ) -> arms20190808_models.CreateOrUpdateNotificationPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_or_update_notification_policy_with_options_async(request, runtime)

    def create_or_update_silence_policy_with_options(
        self,
        request: arms20190808_models.CreateOrUpdateSilencePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateOrUpdateSilencePolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.matching_rules):
            body['MatchingRules'] = request.matching_rules
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateSilencePolicy',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateSilencePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_silence_policy_with_options_async(
        self,
        request: arms20190808_models.CreateOrUpdateSilencePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateOrUpdateSilencePolicyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.matching_rules):
            body['MatchingRules'] = request.matching_rules
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateSilencePolicy',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateSilencePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_silence_policy(
        self,
        request: arms20190808_models.CreateOrUpdateSilencePolicyRequest,
    ) -> arms20190808_models.CreateOrUpdateSilencePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_silence_policy_with_options(request, runtime)

    async def create_or_update_silence_policy_async(
        self,
        request: arms20190808_models.CreateOrUpdateSilencePolicyRequest,
    ) -> arms20190808_models.CreateOrUpdateSilencePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_or_update_silence_policy_with_options_async(request, runtime)

    def create_or_update_webhook_contact_with_options(
        self,
        request: arms20190808_models.CreateOrUpdateWebhookContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateOrUpdateWebhookContactResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_headers):
            body['BizHeaders'] = request.biz_headers
        if not UtilClient.is_unset(request.biz_params):
            body['BizParams'] = request.biz_params
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.method):
            body['Method'] = request.method
        if not UtilClient.is_unset(request.recover_body):
            body['RecoverBody'] = request.recover_body
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        if not UtilClient.is_unset(request.webhook_id):
            body['WebhookId'] = request.webhook_id
        if not UtilClient.is_unset(request.webhook_name):
            body['WebhookName'] = request.webhook_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateWebhookContact',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateWebhookContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_or_update_webhook_contact_with_options_async(
        self,
        request: arms20190808_models.CreateOrUpdateWebhookContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateOrUpdateWebhookContactResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_headers):
            body['BizHeaders'] = request.biz_headers
        if not UtilClient.is_unset(request.biz_params):
            body['BizParams'] = request.biz_params
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.method):
            body['Method'] = request.method
        if not UtilClient.is_unset(request.recover_body):
            body['RecoverBody'] = request.recover_body
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        if not UtilClient.is_unset(request.webhook_id):
            body['WebhookId'] = request.webhook_id
        if not UtilClient.is_unset(request.webhook_name):
            body['WebhookName'] = request.webhook_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateWebhookContact',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateWebhookContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_or_update_webhook_contact(
        self,
        request: arms20190808_models.CreateOrUpdateWebhookContactRequest,
    ) -> arms20190808_models.CreateOrUpdateWebhookContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_webhook_contact_with_options(request, runtime)

    async def create_or_update_webhook_contact_async(
        self,
        request: arms20190808_models.CreateOrUpdateWebhookContactRequest,
    ) -> arms20190808_models.CreateOrUpdateWebhookContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_or_update_webhook_contact_with_options_async(request, runtime)

    def create_prometheus_alert_rule_with_options(
        self,
        request: arms20190808_models.CreatePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreatePrometheusAlertRuleResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreatePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prometheus_alert_rule_with_options_async(
        self,
        request: arms20190808_models.CreatePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreatePrometheusAlertRuleResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreatePrometheusAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prometheus_alert_rule(
        self,
        request: arms20190808_models.CreatePrometheusAlertRuleRequest,
    ) -> arms20190808_models.CreatePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_prometheus_alert_rule_with_options(request, runtime)

    async def create_prometheus_alert_rule_async(
        self,
        request: arms20190808_models.CreatePrometheusAlertRuleRequest,
    ) -> arms20190808_models.CreatePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_prometheus_alert_rule_with_options_async(request, runtime)

    def create_retcode_app_with_options(
        self,
        request: arms20190808_models.CreateRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateRetcodeAppResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateRetcodeAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_retcode_app_with_options_async(
        self,
        request: arms20190808_models.CreateRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateRetcodeAppResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateRetcodeAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_retcode_app(
        self,
        request: arms20190808_models.CreateRetcodeAppRequest,
    ) -> arms20190808_models.CreateRetcodeAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_retcode_app_with_options(request, runtime)

    async def create_retcode_app_async(
        self,
        request: arms20190808_models.CreateRetcodeAppRequest,
    ) -> arms20190808_models.CreateRetcodeAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_retcode_app_with_options_async(request, runtime)

    def create_webhook_with_options(
        self,
        request: arms20190808_models.CreateWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateWebhookResponse:
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
        if not UtilClient.is_unset(request.recover_body):
            query['RecoverBody'] = request.recover_body
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWebhook',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_webhook_with_options_async(
        self,
        request: arms20190808_models.CreateWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateWebhookResponse:
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
        if not UtilClient.is_unset(request.recover_body):
            query['RecoverBody'] = request.recover_body
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWebhook',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_webhook(
        self,
        request: arms20190808_models.CreateWebhookRequest,
    ) -> arms20190808_models.CreateWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_webhook_with_options(request, runtime)

    async def create_webhook_async(
        self,
        request: arms20190808_models.CreateWebhookRequest,
    ) -> arms20190808_models.CreateWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_webhook_with_options_async(request, runtime)

    def delete_asmintegration_with_options(
        self,
        request: arms20190808_models.DeleteASMIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteASMIntegrationResponse:
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
            action='DeleteASMIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteASMIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_asmintegration_with_options_async(
        self,
        request: arms20190808_models.DeleteASMIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteASMIntegrationResponse:
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
            action='DeleteASMIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteASMIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_asmintegration(
        self,
        request: arms20190808_models.DeleteASMIntegrationRequest,
    ) -> arms20190808_models.DeleteASMIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_asmintegration_with_options(request, runtime)

    async def delete_asmintegration_async(
        self,
        request: arms20190808_models.DeleteASMIntegrationRequest,
    ) -> arms20190808_models.DeleteASMIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_asmintegration_with_options_async(request, runtime)

    def delete_alert_contact_with_options(
        self,
        request: arms20190808_models.DeleteAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAlertContactResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_contact_with_options_async(
        self,
        request: arms20190808_models.DeleteAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAlertContactResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_contact(
        self,
        request: arms20190808_models.DeleteAlertContactRequest,
    ) -> arms20190808_models.DeleteAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_with_options(request, runtime)

    async def delete_alert_contact_async(
        self,
        request: arms20190808_models.DeleteAlertContactRequest,
    ) -> arms20190808_models.DeleteAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_contact_with_options_async(request, runtime)

    def delete_alert_contact_group_with_options(
        self,
        request: arms20190808_models.DeleteAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAlertContactGroupResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_contact_group_with_options_async(
        self,
        request: arms20190808_models.DeleteAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAlertContactGroupResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_contact_group(
        self,
        request: arms20190808_models.DeleteAlertContactGroupRequest,
    ) -> arms20190808_models.DeleteAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_group_with_options(request, runtime)

    async def delete_alert_contact_group_async(
        self,
        request: arms20190808_models.DeleteAlertContactGroupRequest,
    ) -> arms20190808_models.DeleteAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_contact_group_with_options_async(request, runtime)

    def delete_alert_rule_with_options(
        self,
        request: arms20190808_models.DeleteAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAlertRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlertRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_rule_with_options_async(
        self,
        request: arms20190808_models.DeleteAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAlertRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlertRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_rule(
        self,
        request: arms20190808_models.DeleteAlertRuleRequest,
    ) -> arms20190808_models.DeleteAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_rule_with_options(request, runtime)

    async def delete_alert_rule_async(
        self,
        request: arms20190808_models.DeleteAlertRuleRequest,
    ) -> arms20190808_models.DeleteAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_rule_with_options_async(request, runtime)

    def delete_alert_rules_with_options(
        self,
        request: arms20190808_models.DeleteAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAlertRulesResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_alert_rules_with_options_async(
        self,
        request: arms20190808_models.DeleteAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAlertRulesResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_alert_rules(
        self,
        request: arms20190808_models.DeleteAlertRulesRequest,
    ) -> arms20190808_models.DeleteAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_rules_with_options(request, runtime)

    async def delete_alert_rules_async(
        self,
        request: arms20190808_models.DeleteAlertRulesRequest,
    ) -> arms20190808_models.DeleteAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_alert_rules_with_options_async(request, runtime)

    def delete_cms_exporter_with_options(
        self,
        request: arms20190808_models.DeleteCmsExporterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteCmsExporterResponse:
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
            action='DeleteCmsExporter',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteCmsExporterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cms_exporter_with_options_async(
        self,
        request: arms20190808_models.DeleteCmsExporterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteCmsExporterResponse:
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
            action='DeleteCmsExporter',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteCmsExporterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cms_exporter(
        self,
        request: arms20190808_models.DeleteCmsExporterRequest,
    ) -> arms20190808_models.DeleteCmsExporterResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cms_exporter_with_options(request, runtime)

    async def delete_cms_exporter_async(
        self,
        request: arms20190808_models.DeleteCmsExporterRequest,
    ) -> arms20190808_models.DeleteCmsExporterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cms_exporter_with_options_async(request, runtime)

    def delete_contact_with_options(
        self,
        request: arms20190808_models.DeleteContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContact',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_with_options_async(
        self,
        request: arms20190808_models.DeleteContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContact',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact(
        self,
        request: arms20190808_models.DeleteContactRequest,
    ) -> arms20190808_models.DeleteContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_contact_with_options(request, runtime)

    async def delete_contact_async(
        self,
        request: arms20190808_models.DeleteContactRequest,
    ) -> arms20190808_models.DeleteContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_contact_with_options_async(request, runtime)

    def delete_contact_group_with_options(
        self,
        request: arms20190808_models.DeleteContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_id):
            query['ContactGroupId'] = request.contact_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContactGroup',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_group_with_options_async(
        self,
        request: arms20190808_models.DeleteContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteContactGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_id):
            query['ContactGroupId'] = request.contact_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContactGroup',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact_group(
        self,
        request: arms20190808_models.DeleteContactGroupRequest,
    ) -> arms20190808_models.DeleteContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_contact_group_with_options(request, runtime)

    async def delete_contact_group_async(
        self,
        request: arms20190808_models.DeleteContactGroupRequest,
    ) -> arms20190808_models.DeleteContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_contact_group_with_options_async(request, runtime)

    def delete_dispatch_rule_with_options(
        self,
        request: arms20190808_models.DeleteDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteDispatchRuleResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dispatch_rule_with_options_async(
        self,
        request: arms20190808_models.DeleteDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteDispatchRuleResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteDispatchRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dispatch_rule(
        self,
        request: arms20190808_models.DeleteDispatchRuleRequest,
    ) -> arms20190808_models.DeleteDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dispatch_rule_with_options(request, runtime)

    async def delete_dispatch_rule_async(
        self,
        request: arms20190808_models.DeleteDispatchRuleRequest,
    ) -> arms20190808_models.DeleteDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dispatch_rule_with_options_async(request, runtime)

    def delete_event_bridge_integration_with_options(
        self,
        request: arms20190808_models.DeleteEventBridgeIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteEventBridgeIntegrationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEventBridgeIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteEventBridgeIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_bridge_integration_with_options_async(
        self,
        request: arms20190808_models.DeleteEventBridgeIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteEventBridgeIntegrationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEventBridgeIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteEventBridgeIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_bridge_integration(
        self,
        request: arms20190808_models.DeleteEventBridgeIntegrationRequest,
    ) -> arms20190808_models.DeleteEventBridgeIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_event_bridge_integration_with_options(request, runtime)

    async def delete_event_bridge_integration_async(
        self,
        request: arms20190808_models.DeleteEventBridgeIntegrationRequest,
    ) -> arms20190808_models.DeleteEventBridgeIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_event_bridge_integration_with_options_async(request, runtime)

    def delete_imrobot_with_options(
        self,
        request: arms20190808_models.DeleteIMRobotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteIMRobotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.robot_id):
            query['RobotId'] = request.robot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIMRobot',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteIMRobotResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_imrobot_with_options_async(
        self,
        request: arms20190808_models.DeleteIMRobotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteIMRobotResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.robot_id):
            query['RobotId'] = request.robot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIMRobot',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteIMRobotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_imrobot(
        self,
        request: arms20190808_models.DeleteIMRobotRequest,
    ) -> arms20190808_models.DeleteIMRobotResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_imrobot_with_options(request, runtime)

    async def delete_imrobot_async(
        self,
        request: arms20190808_models.DeleteIMRobotRequest,
    ) -> arms20190808_models.DeleteIMRobotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_imrobot_with_options_async(request, runtime)

    def delete_integration_with_options(
        self,
        request: arms20190808_models.DeleteIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteIntegrationResponse:
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
            action='DeleteIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_integration_with_options_async(
        self,
        request: arms20190808_models.DeleteIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteIntegrationResponse:
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
            action='DeleteIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_integration(
        self,
        request: arms20190808_models.DeleteIntegrationRequest,
    ) -> arms20190808_models.DeleteIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_integration_with_options(request, runtime)

    async def delete_integration_async(
        self,
        request: arms20190808_models.DeleteIntegrationRequest,
    ) -> arms20190808_models.DeleteIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_integration_with_options_async(request, runtime)

    def delete_notification_policy_with_options(
        self,
        request: arms20190808_models.DeleteNotificationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteNotificationPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNotificationPolicy',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteNotificationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_notification_policy_with_options_async(
        self,
        request: arms20190808_models.DeleteNotificationPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteNotificationPolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNotificationPolicy',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteNotificationPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_notification_policy(
        self,
        request: arms20190808_models.DeleteNotificationPolicyRequest,
    ) -> arms20190808_models.DeleteNotificationPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_notification_policy_with_options(request, runtime)

    async def delete_notification_policy_async(
        self,
        request: arms20190808_models.DeleteNotificationPolicyRequest,
    ) -> arms20190808_models.DeleteNotificationPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_notification_policy_with_options_async(request, runtime)

    def delete_prometheus_alert_rule_with_options(
        self,
        request: arms20190808_models.DeletePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeletePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusAlertRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeletePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_prometheus_alert_rule_with_options_async(
        self,
        request: arms20190808_models.DeletePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeletePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusAlertRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeletePrometheusAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_prometheus_alert_rule(
        self,
        request: arms20190808_models.DeletePrometheusAlertRuleRequest,
    ) -> arms20190808_models.DeletePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_prometheus_alert_rule_with_options(request, runtime)

    async def delete_prometheus_alert_rule_async(
        self,
        request: arms20190808_models.DeletePrometheusAlertRuleRequest,
    ) -> arms20190808_models.DeletePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_prometheus_alert_rule_with_options_async(request, runtime)

    def delete_prometheus_global_view_with_options(
        self,
        request: arms20190808_models.DeletePrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeletePrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeletePrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_prometheus_global_view_with_options_async(
        self,
        request: arms20190808_models.DeletePrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeletePrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeletePrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_prometheus_global_view(
        self,
        request: arms20190808_models.DeletePrometheusGlobalViewRequest,
    ) -> arms20190808_models.DeletePrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_prometheus_global_view_with_options(request, runtime)

    async def delete_prometheus_global_view_async(
        self,
        request: arms20190808_models.DeletePrometheusGlobalViewRequest,
    ) -> arms20190808_models.DeletePrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_prometheus_global_view_with_options_async(request, runtime)

    def delete_retcode_app_with_options(
        self,
        request: arms20190808_models.DeleteRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteRetcodeAppResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteRetcodeAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_retcode_app_with_options_async(
        self,
        request: arms20190808_models.DeleteRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteRetcodeAppResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteRetcodeAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_retcode_app(
        self,
        request: arms20190808_models.DeleteRetcodeAppRequest,
    ) -> arms20190808_models.DeleteRetcodeAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_retcode_app_with_options(request, runtime)

    async def delete_retcode_app_async(
        self,
        request: arms20190808_models.DeleteRetcodeAppRequest,
    ) -> arms20190808_models.DeleteRetcodeAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_retcode_app_with_options_async(request, runtime)

    def delete_scenario_with_options(
        self,
        request: arms20190808_models.DeleteScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteScenarioResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scenario_with_options_async(
        self,
        request: arms20190808_models.DeleteScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteScenarioResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteScenarioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_scenario(
        self,
        request: arms20190808_models.DeleteScenarioRequest,
    ) -> arms20190808_models.DeleteScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scenario_with_options(request, runtime)

    async def delete_scenario_async(
        self,
        request: arms20190808_models.DeleteScenarioRequest,
    ) -> arms20190808_models.DeleteScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scenario_with_options_async(request, runtime)

    def delete_silence_policy_with_options(
        self,
        request: arms20190808_models.DeleteSilencePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteSilencePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSilencePolicy',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteSilencePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_silence_policy_with_options_async(
        self,
        request: arms20190808_models.DeleteSilencePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteSilencePolicyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSilencePolicy',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteSilencePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_silence_policy(
        self,
        request: arms20190808_models.DeleteSilencePolicyRequest,
    ) -> arms20190808_models.DeleteSilencePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_silence_policy_with_options(request, runtime)

    async def delete_silence_policy_async(
        self,
        request: arms20190808_models.DeleteSilencePolicyRequest,
    ) -> arms20190808_models.DeleteSilencePolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_silence_policy_with_options_async(request, runtime)

    def delete_trace_app_with_options(
        self,
        request: arms20190808_models.DeleteTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteTraceAppResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteTraceAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_trace_app_with_options_async(
        self,
        request: arms20190808_models.DeleteTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteTraceAppResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteTraceAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_trace_app(
        self,
        request: arms20190808_models.DeleteTraceAppRequest,
    ) -> arms20190808_models.DeleteTraceAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_trace_app_with_options(request, runtime)

    async def delete_trace_app_async(
        self,
        request: arms20190808_models.DeleteTraceAppRequest,
    ) -> arms20190808_models.DeleteTraceAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_trace_app_with_options_async(request, runtime)

    def delete_webhook_contact_with_options(
        self,
        request: arms20190808_models.DeleteWebhookContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteWebhookContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.webhook_id):
            query['WebhookId'] = request.webhook_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebhookContact',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteWebhookContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_webhook_contact_with_options_async(
        self,
        request: arms20190808_models.DeleteWebhookContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteWebhookContactResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.webhook_id):
            query['WebhookId'] = request.webhook_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebhookContact',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteWebhookContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_webhook_contact(
        self,
        request: arms20190808_models.DeleteWebhookContactRequest,
    ) -> arms20190808_models.DeleteWebhookContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_webhook_contact_with_options(request, runtime)

    async def delete_webhook_contact_async(
        self,
        request: arms20190808_models.DeleteWebhookContactRequest,
    ) -> arms20190808_models.DeleteWebhookContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_webhook_contact_with_options_async(request, runtime)

    def describe_contact_groups_with_options(
        self,
        request: arms20190808_models.DescribeContactGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeContactGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContactGroups',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeContactGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_contact_groups_with_options_async(
        self,
        request: arms20190808_models.DescribeContactGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeContactGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContactGroups',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeContactGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_contact_groups(
        self,
        request: arms20190808_models.DescribeContactGroupsRequest,
    ) -> arms20190808_models.DescribeContactGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_contact_groups_with_options(request, runtime)

    async def describe_contact_groups_async(
        self,
        request: arms20190808_models.DescribeContactGroupsRequest,
    ) -> arms20190808_models.DescribeContactGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_contact_groups_with_options_async(request, runtime)

    def describe_contacts_with_options(
        self,
        request: arms20190808_models.DescribeContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeContactsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContacts',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_contacts_with_options_async(
        self,
        request: arms20190808_models.DescribeContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeContactsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContacts',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_contacts(
        self,
        request: arms20190808_models.DescribeContactsRequest,
    ) -> arms20190808_models.DescribeContactsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_contacts_with_options(request, runtime)

    async def describe_contacts_async(
        self,
        request: arms20190808_models.DescribeContactsRequest,
    ) -> arms20190808_models.DescribeContactsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_contacts_with_options_async(request, runtime)

    def describe_dispatch_rule_with_options(
        self,
        request: arms20190808_models.DescribeDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeDispatchRuleResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dispatch_rule_with_options_async(
        self,
        request: arms20190808_models.DescribeDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeDispatchRuleResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeDispatchRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dispatch_rule(
        self,
        request: arms20190808_models.DescribeDispatchRuleRequest,
    ) -> arms20190808_models.DescribeDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dispatch_rule_with_options(request, runtime)

    async def describe_dispatch_rule_async(
        self,
        request: arms20190808_models.DescribeDispatchRuleRequest,
    ) -> arms20190808_models.DescribeDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dispatch_rule_with_options_async(request, runtime)

    def describe_imrobots_with_options(
        self,
        request: arms20190808_models.DescribeIMRobotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeIMRobotsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.robot_name):
            query['RobotName'] = request.robot_name
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIMRobots',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeIMRobotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_imrobots_with_options_async(
        self,
        request: arms20190808_models.DescribeIMRobotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeIMRobotsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.robot_name):
            query['RobotName'] = request.robot_name
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIMRobots',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeIMRobotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_imrobots(
        self,
        request: arms20190808_models.DescribeIMRobotsRequest,
    ) -> arms20190808_models.DescribeIMRobotsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_imrobots_with_options(request, runtime)

    async def describe_imrobots_async(
        self,
        request: arms20190808_models.DescribeIMRobotsRequest,
    ) -> arms20190808_models.DescribeIMRobotsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_imrobots_with_options_async(request, runtime)

    def describe_prometheus_alert_rule_with_options(
        self,
        request: arms20190808_models.DescribePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrometheusAlertRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_prometheus_alert_rule_with_options_async(
        self,
        request: arms20190808_models.DescribePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribePrometheusAlertRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrometheusAlertRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribePrometheusAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_prometheus_alert_rule(
        self,
        request: arms20190808_models.DescribePrometheusAlertRuleRequest,
    ) -> arms20190808_models.DescribePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_prometheus_alert_rule_with_options(request, runtime)

    async def describe_prometheus_alert_rule_async(
        self,
        request: arms20190808_models.DescribePrometheusAlertRuleRequest,
    ) -> arms20190808_models.DescribePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_prometheus_alert_rule_with_options_async(request, runtime)

    def describe_trace_license_key_with_options(
        self,
        request: arms20190808_models.DescribeTraceLicenseKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeTraceLicenseKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTraceLicenseKey',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeTraceLicenseKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_trace_license_key_with_options_async(
        self,
        request: arms20190808_models.DescribeTraceLicenseKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeTraceLicenseKeyResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTraceLicenseKey',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeTraceLicenseKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_trace_license_key(
        self,
        request: arms20190808_models.DescribeTraceLicenseKeyRequest,
    ) -> arms20190808_models.DescribeTraceLicenseKeyResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_trace_license_key_with_options(request, runtime)

    async def describe_trace_license_key_async(
        self,
        request: arms20190808_models.DescribeTraceLicenseKeyRequest,
    ) -> arms20190808_models.DescribeTraceLicenseKeyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_trace_license_key_with_options_async(request, runtime)

    def describe_webhook_contacts_with_options(
        self,
        request: arms20190808_models.DescribeWebhookContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeWebhookContactsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebhookContacts',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeWebhookContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_webhook_contacts_with_options_async(
        self,
        request: arms20190808_models.DescribeWebhookContactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeWebhookContactsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebhookContacts',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeWebhookContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_webhook_contacts(
        self,
        request: arms20190808_models.DescribeWebhookContactsRequest,
    ) -> arms20190808_models.DescribeWebhookContactsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_webhook_contacts_with_options(request, runtime)

    async def describe_webhook_contacts_async(
        self,
        request: arms20190808_models.DescribeWebhookContactsRequest,
    ) -> arms20190808_models.DescribeWebhookContactsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_webhook_contacts_with_options_async(request, runtime)

    def explore_trace_with_options(
        self,
        request: arms20190808_models.ExploreTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ExploreTraceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attributes):
            query['Attributes'] = request.attributes
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.kind):
            query['Kind'] = request.kind
        if not UtilClient.is_unset(request.max_duration):
            query['MaxDuration'] = request.max_duration
        if not UtilClient.is_unset(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.selected_field):
            query['SelectedField'] = request.selected_field
        if not UtilClient.is_unset(request.service_ip):
            query['ServiceIp'] = request.service_ip
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.span_name):
            query['SpanName'] = request.span_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status_code):
            query['StatusCode'] = request.status_code
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExploreTrace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ExploreTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def explore_trace_with_options_async(
        self,
        request: arms20190808_models.ExploreTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ExploreTraceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attributes):
            query['Attributes'] = request.attributes
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.kind):
            query['Kind'] = request.kind
        if not UtilClient.is_unset(request.max_duration):
            query['MaxDuration'] = request.max_duration
        if not UtilClient.is_unset(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.selected_field):
            query['SelectedField'] = request.selected_field
        if not UtilClient.is_unset(request.service_ip):
            query['ServiceIp'] = request.service_ip
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.span_name):
            query['SpanName'] = request.span_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status_code):
            query['StatusCode'] = request.status_code
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExploreTrace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ExploreTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def explore_trace(
        self,
        request: arms20190808_models.ExploreTraceRequest,
    ) -> arms20190808_models.ExploreTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.explore_trace_with_options(request, runtime)

    async def explore_trace_async(
        self,
        request: arms20190808_models.ExploreTraceRequest,
    ) -> arms20190808_models.ExploreTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.explore_trace_with_options_async(request, runtime)

    def get_asmintegration_state_with_options(
        self,
        request: arms20190808_models.GetASMIntegrationStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetASMIntegrationStateResponse:
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
            action='GetASMIntegrationState',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetASMIntegrationStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_asmintegration_state_with_options_async(
        self,
        request: arms20190808_models.GetASMIntegrationStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetASMIntegrationStateResponse:
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
            action='GetASMIntegrationState',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetASMIntegrationStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_asmintegration_state(
        self,
        request: arms20190808_models.GetASMIntegrationStateRequest,
    ) -> arms20190808_models.GetASMIntegrationStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_asmintegration_state_with_options(request, runtime)

    async def get_asmintegration_state_async(
        self,
        request: arms20190808_models.GetASMIntegrationStateRequest,
    ) -> arms20190808_models.GetASMIntegrationStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_asmintegration_state_with_options_async(request, runtime)

    def get_agent_download_url_with_options(
        self,
        request: arms20190808_models.GetAgentDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetAgentDownloadUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentDownloadUrl',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetAgentDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_agent_download_url_with_options_async(
        self,
        request: arms20190808_models.GetAgentDownloadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetAgentDownloadUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentDownloadUrl',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetAgentDownloadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_agent_download_url(
        self,
        request: arms20190808_models.GetAgentDownloadUrlRequest,
    ) -> arms20190808_models.GetAgentDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_agent_download_url_with_options(request, runtime)

    async def get_agent_download_url_async(
        self,
        request: arms20190808_models.GetAgentDownloadUrlRequest,
    ) -> arms20190808_models.GetAgentDownloadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_agent_download_url_with_options_async(request, runtime)

    def get_alert_rules_with_options(
        self,
        request: arms20190808_models.GetAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetAlertRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not UtilClient.is_unset(request.alert_names):
            query['AlertNames'] = request.alert_names
        if not UtilClient.is_unset(request.alert_status):
            query['AlertStatus'] = request.alert_status
        if not UtilClient.is_unset(request.alert_type):
            query['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlertRules',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_alert_rules_with_options_async(
        self,
        request: arms20190808_models.GetAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetAlertRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not UtilClient.is_unset(request.alert_names):
            query['AlertNames'] = request.alert_names
        if not UtilClient.is_unset(request.alert_status):
            query['AlertStatus'] = request.alert_status
        if not UtilClient.is_unset(request.alert_type):
            query['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlertRules',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_alert_rules(
        self,
        request: arms20190808_models.GetAlertRulesRequest,
    ) -> arms20190808_models.GetAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_alert_rules_with_options(request, runtime)

    async def get_alert_rules_async(
        self,
        request: arms20190808_models.GetAlertRulesRequest,
    ) -> arms20190808_models.GetAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_alert_rules_with_options_async(request, runtime)

    def get_app_api_by_page_with_options(
        self,
        request: arms20190808_models.GetAppApiByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetAppApiByPageResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetAppApiByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_api_by_page_with_options_async(
        self,
        request: arms20190808_models.GetAppApiByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetAppApiByPageResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetAppApiByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_api_by_page(
        self,
        request: arms20190808_models.GetAppApiByPageRequest,
    ) -> arms20190808_models.GetAppApiByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_api_by_page_with_options(request, runtime)

    async def get_app_api_by_page_async(
        self,
        request: arms20190808_models.GetAppApiByPageRequest,
    ) -> arms20190808_models.GetAppApiByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_api_by_page_with_options_async(request, runtime)

    def get_arms_agent_down_load_url_with_options(
        self,
        request: arms20190808_models.GetArmsAgentDownLoadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetArmsAgentDownLoadUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArmsAgentDownLoadUrl',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetArmsAgentDownLoadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_arms_agent_down_load_url_with_options_async(
        self,
        request: arms20190808_models.GetArmsAgentDownLoadUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetArmsAgentDownLoadUrlResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArmsAgentDownLoadUrl',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetArmsAgentDownLoadUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_arms_agent_down_load_url(
        self,
        request: arms20190808_models.GetArmsAgentDownLoadUrlRequest,
    ) -> arms20190808_models.GetArmsAgentDownLoadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_arms_agent_down_load_url_with_options(request, runtime)

    async def get_arms_agent_down_load_url_async(
        self,
        request: arms20190808_models.GetArmsAgentDownLoadUrlRequest,
    ) -> arms20190808_models.GetArmsAgentDownLoadUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_arms_agent_down_load_url_with_options_async(request, runtime)

    def get_auth_token_with_options(
        self,
        request: arms20190808_models.GetAuthTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetAuthTokenResponse:
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
            action='GetAuthToken',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auth_token_with_options_async(
        self,
        request: arms20190808_models.GetAuthTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetAuthTokenResponse:
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
            action='GetAuthToken',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetAuthTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auth_token(
        self,
        request: arms20190808_models.GetAuthTokenRequest,
    ) -> arms20190808_models.GetAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_auth_token_with_options(request, runtime)

    async def get_auth_token_async(
        self,
        request: arms20190808_models.GetAuthTokenRequest,
    ) -> arms20190808_models.GetAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auth_token_with_options_async(request, runtime)

    def get_cluster_info_with_options(
        self,
        request: arms20190808_models.GetClusterInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetClusterInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.query_user_id):
            query['QueryUserId'] = request.query_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterInfo',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetClusterInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_info_with_options_async(
        self,
        request: arms20190808_models.GetClusterInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetClusterInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.query_user_id):
            query['QueryUserId'] = request.query_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterInfo',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetClusterInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_info(
        self,
        request: arms20190808_models.GetClusterInfoRequest,
    ) -> arms20190808_models.GetClusterInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_info_with_options(request, runtime)

    async def get_cluster_info_async(
        self,
        request: arms20190808_models.GetClusterInfoRequest,
    ) -> arms20190808_models.GetClusterInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_info_with_options_async(request, runtime)

    def get_cluster_state_with_options(
        self,
        request: arms20190808_models.GetClusterStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetClusterStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.puser_id):
            query['PuserId'] = request.puser_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterState',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetClusterStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_state_with_options_async(
        self,
        request: arms20190808_models.GetClusterStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetClusterStateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.puser_id):
            query['PuserId'] = request.puser_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterState',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetClusterStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_state(
        self,
        request: arms20190808_models.GetClusterStateRequest,
    ) -> arms20190808_models.GetClusterStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_state_with_options(request, runtime)

    async def get_cluster_state_async(
        self,
        request: arms20190808_models.GetClusterStateRequest,
    ) -> arms20190808_models.GetClusterStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_state_with_options_async(request, runtime)

    def get_estimate_fee_info_with_options(
        self,
        request: arms20190808_models.GetEstimateFeeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetEstimateFeeInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEstimateFeeInfo',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetEstimateFeeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_estimate_fee_info_with_options_async(
        self,
        request: arms20190808_models.GetEstimateFeeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetEstimateFeeInfoResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEstimateFeeInfo',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetEstimateFeeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_estimate_fee_info(
        self,
        request: arms20190808_models.GetEstimateFeeInfoRequest,
    ) -> arms20190808_models.GetEstimateFeeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_estimate_fee_info_with_options(request, runtime)

    async def get_estimate_fee_info_async(
        self,
        request: arms20190808_models.GetEstimateFeeInfoRequest,
    ) -> arms20190808_models.GetEstimateFeeInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_estimate_fee_info_with_options_async(request, runtime)

    def get_explore_url_with_options(
        self,
        request: arms20190808_models.GetExploreUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetExploreUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExploreUrl',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetExploreUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_explore_url_with_options_async(
        self,
        request: arms20190808_models.GetExploreUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetExploreUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExploreUrl',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetExploreUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_explore_url(
        self,
        request: arms20190808_models.GetExploreUrlRequest,
    ) -> arms20190808_models.GetExploreUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_explore_url_with_options(request, runtime)

    async def get_explore_url_async(
        self,
        request: arms20190808_models.GetExploreUrlRequest,
    ) -> arms20190808_models.GetExploreUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_explore_url_with_options_async(request, runtime)

    def get_integration_state_with_options(
        self,
        request: arms20190808_models.GetIntegrationStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetIntegrationStateResponse:
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
            action='GetIntegrationState',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetIntegrationStateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_integration_state_with_options_async(
        self,
        request: arms20190808_models.GetIntegrationStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetIntegrationStateResponse:
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
            action='GetIntegrationState',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetIntegrationStateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_integration_state(
        self,
        request: arms20190808_models.GetIntegrationStateRequest,
    ) -> arms20190808_models.GetIntegrationStateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_integration_state_with_options(request, runtime)

    async def get_integration_state_async(
        self,
        request: arms20190808_models.GetIntegrationStateRequest,
    ) -> arms20190808_models.GetIntegrationStateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_integration_state_with_options_async(request, runtime)

    def get_multiple_trace_with_options(
        self,
        request: arms20190808_models.GetMultipleTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetMultipleTraceResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetMultipleTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multiple_trace_with_options_async(
        self,
        request: arms20190808_models.GetMultipleTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetMultipleTraceResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetMultipleTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multiple_trace(
        self,
        request: arms20190808_models.GetMultipleTraceRequest,
    ) -> arms20190808_models.GetMultipleTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_multiple_trace_with_options(request, runtime)

    async def get_multiple_trace_async(
        self,
        request: arms20190808_models.GetMultipleTraceRequest,
    ) -> arms20190808_models.GetMultipleTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_multiple_trace_with_options_async(request, runtime)

    def get_prometheus_api_token_with_options(
        self,
        request: arms20190808_models.GetPrometheusApiTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetPrometheusApiTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusApiToken',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusApiTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_api_token_with_options_async(
        self,
        request: arms20190808_models.GetPrometheusApiTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetPrometheusApiTokenResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusApiToken',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusApiTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_api_token(
        self,
        request: arms20190808_models.GetPrometheusApiTokenRequest,
    ) -> arms20190808_models.GetPrometheusApiTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_prometheus_api_token_with_options(request, runtime)

    async def get_prometheus_api_token_async(
        self,
        request: arms20190808_models.GetPrometheusApiTokenRequest,
    ) -> arms20190808_models.GetPrometheusApiTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_prometheus_api_token_with_options_async(request, runtime)

    def get_prometheus_global_view_with_options(
        self,
        request: arms20190808_models.GetPrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetPrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_global_view_with_options_async(
        self,
        request: arms20190808_models.GetPrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetPrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_global_view(
        self,
        request: arms20190808_models.GetPrometheusGlobalViewRequest,
    ) -> arms20190808_models.GetPrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_prometheus_global_view_with_options(request, runtime)

    async def get_prometheus_global_view_async(
        self,
        request: arms20190808_models.GetPrometheusGlobalViewRequest,
    ) -> arms20190808_models.GetPrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_prometheus_global_view_with_options_async(request, runtime)

    def get_recording_rule_with_options(
        self,
        request: arms20190808_models.GetRecordingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetRecordingRuleResponse:
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
            action='GetRecordingRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetRecordingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_recording_rule_with_options_async(
        self,
        request: arms20190808_models.GetRecordingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetRecordingRuleResponse:
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
            action='GetRecordingRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetRecordingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_recording_rule(
        self,
        request: arms20190808_models.GetRecordingRuleRequest,
    ) -> arms20190808_models.GetRecordingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_recording_rule_with_options(request, runtime)

    async def get_recording_rule_async(
        self,
        request: arms20190808_models.GetRecordingRuleRequest,
    ) -> arms20190808_models.GetRecordingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_recording_rule_with_options_async(request, runtime)

    def get_retcode_share_url_with_options(
        self,
        request: arms20190808_models.GetRetcodeShareUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetRetcodeShareUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRetcodeShareUrl',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetRetcodeShareUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_retcode_share_url_with_options_async(
        self,
        request: arms20190808_models.GetRetcodeShareUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetRetcodeShareUrlResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRetcodeShareUrl',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetRetcodeShareUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_retcode_share_url(
        self,
        request: arms20190808_models.GetRetcodeShareUrlRequest,
    ) -> arms20190808_models.GetRetcodeShareUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_retcode_share_url_with_options(request, runtime)

    async def get_retcode_share_url_async(
        self,
        request: arms20190808_models.GetRetcodeShareUrlRequest,
    ) -> arms20190808_models.GetRetcodeShareUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_retcode_share_url_with_options_async(request, runtime)

    def get_stack_with_options(
        self,
        request: arms20190808_models.GetStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetStackResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_with_options_async(
        self,
        request: arms20190808_models.GetStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetStackResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack(
        self,
        request: arms20190808_models.GetStackRequest,
    ) -> arms20190808_models.GetStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_with_options(request, runtime)

    async def get_stack_async(
        self,
        request: arms20190808_models.GetStackRequest,
    ) -> arms20190808_models.GetStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_with_options_async(request, runtime)

    def get_trace_with_options(
        self,
        request: arms20190808_models.GetTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetTraceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetTraceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trace_with_options_async(
        self,
        request: arms20190808_models.GetTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetTraceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetTraceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trace(
        self,
        request: arms20190808_models.GetTraceRequest,
    ) -> arms20190808_models.GetTraceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_trace_with_options(request, runtime)

    async def get_trace_async(
        self,
        request: arms20190808_models.GetTraceRequest,
    ) -> arms20190808_models.GetTraceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_trace_with_options_async(request, runtime)

    def get_trace_app_with_options(
        self,
        request: arms20190808_models.GetTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetTraceAppResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetTraceAppResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trace_app_with_options_async(
        self,
        request: arms20190808_models.GetTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetTraceAppResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetTraceAppResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trace_app(
        self,
        request: arms20190808_models.GetTraceAppRequest,
    ) -> arms20190808_models.GetTraceAppResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_trace_app_with_options(request, runtime)

    async def get_trace_app_async(
        self,
        request: arms20190808_models.GetTraceAppRequest,
    ) -> arms20190808_models.GetTraceAppResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_trace_app_with_options_async(request, runtime)

    def get_user_commercial_status_with_options(
        self,
        request: arms20190808_models.GetUserCommercialStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetUserCommercialStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserCommercialStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetUserCommercialStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_commercial_status_with_options_async(
        self,
        request: arms20190808_models.GetUserCommercialStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetUserCommercialStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserCommercialStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetUserCommercialStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_commercial_status(
        self,
        request: arms20190808_models.GetUserCommercialStatusRequest,
    ) -> arms20190808_models.GetUserCommercialStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_commercial_status_with_options(request, runtime)

    async def get_user_commercial_status_async(
        self,
        request: arms20190808_models.GetUserCommercialStatusRequest,
    ) -> arms20190808_models.GetUserCommercialStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_commercial_status_with_options_async(request, runtime)

    def import_app_alert_rules_with_options(
        self,
        request: arms20190808_models.ImportAppAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ImportAppAlertRulesResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ImportAppAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_app_alert_rules_with_options_async(
        self,
        request: arms20190808_models.ImportAppAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ImportAppAlertRulesResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ImportAppAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_app_alert_rules(
        self,
        request: arms20190808_models.ImportAppAlertRulesRequest,
    ) -> arms20190808_models.ImportAppAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.import_app_alert_rules_with_options(request, runtime)

    async def import_app_alert_rules_async(
        self,
        request: arms20190808_models.ImportAppAlertRulesRequest,
    ) -> arms20190808_models.ImportAppAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.import_app_alert_rules_with_options_async(request, runtime)

    def install_cms_exporter_with_options(
        self,
        request: arms20190808_models.InstallCmsExporterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.InstallCmsExporterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cms_args):
            query['CmsArgs'] = request.cms_args
        if not UtilClient.is_unset(request.enable_tag):
            query['EnableTag'] = request.enable_tag
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallCmsExporter',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.InstallCmsExporterResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_cms_exporter_with_options_async(
        self,
        request: arms20190808_models.InstallCmsExporterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.InstallCmsExporterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cms_args):
            query['CmsArgs'] = request.cms_args
        if not UtilClient.is_unset(request.enable_tag):
            query['EnableTag'] = request.enable_tag
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallCmsExporter',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.InstallCmsExporterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_cms_exporter(
        self,
        request: arms20190808_models.InstallCmsExporterRequest,
    ) -> arms20190808_models.InstallCmsExporterResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_cms_exporter_with_options(request, runtime)

    async def install_cms_exporter_async(
        self,
        request: arms20190808_models.InstallCmsExporterRequest,
    ) -> arms20190808_models.InstallCmsExporterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_cms_exporter_with_options_async(request, runtime)

    def install_managed_prometheus_with_options(
        self,
        request: arms20190808_models.InstallManagedPrometheusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.InstallManagedPrometheusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.kube_config):
            query['KubeConfig'] = request.kube_config
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallManagedPrometheus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.InstallManagedPrometheusResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_managed_prometheus_with_options_async(
        self,
        request: arms20190808_models.InstallManagedPrometheusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.InstallManagedPrometheusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.kube_config):
            query['KubeConfig'] = request.kube_config
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallManagedPrometheus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.InstallManagedPrometheusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_managed_prometheus(
        self,
        request: arms20190808_models.InstallManagedPrometheusRequest,
    ) -> arms20190808_models.InstallManagedPrometheusResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_managed_prometheus_with_options(request, runtime)

    async def install_managed_prometheus_async(
        self,
        request: arms20190808_models.InstallManagedPrometheusRequest,
    ) -> arms20190808_models.InstallManagedPrometheusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_managed_prometheus_with_options_async(request, runtime)

    def list_activated_alerts_with_options(
        self,
        request: arms20190808_models.ListActivatedAlertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListActivatedAlertsResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListActivatedAlertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_activated_alerts_with_options_async(
        self,
        request: arms20190808_models.ListActivatedAlertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListActivatedAlertsResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListActivatedAlertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_activated_alerts(
        self,
        request: arms20190808_models.ListActivatedAlertsRequest,
    ) -> arms20190808_models.ListActivatedAlertsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_activated_alerts_with_options(request, runtime)

    async def list_activated_alerts_async(
        self,
        request: arms20190808_models.ListActivatedAlertsRequest,
    ) -> arms20190808_models.ListActivatedAlertsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_activated_alerts_with_options_async(request, runtime)

    def list_alerts_with_options(
        self,
        request: arms20190808_models.ListAlertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListAlertsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_name):
            query['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.dispatch_rule_id):
            query['DispatchRuleId'] = request.dispatch_rule_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.show_activities):
            query['ShowActivities'] = request.show_activities
        if not UtilClient.is_unset(request.show_events):
            query['ShowEvents'] = request.show_events
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlerts',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListAlertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alerts_with_options_async(
        self,
        request: arms20190808_models.ListAlertsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListAlertsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_name):
            query['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.dispatch_rule_id):
            query['DispatchRuleId'] = request.dispatch_rule_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.show_activities):
            query['ShowActivities'] = request.show_activities
        if not UtilClient.is_unset(request.show_events):
            query['ShowEvents'] = request.show_events
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlerts',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListAlertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alerts(
        self,
        request: arms20190808_models.ListAlertsRequest,
    ) -> arms20190808_models.ListAlertsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_alerts_with_options(request, runtime)

    async def list_alerts_async(
        self,
        request: arms20190808_models.ListAlertsRequest,
    ) -> arms20190808_models.ListAlertsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_alerts_with_options_async(request, runtime)

    def list_cluster_from_grafana_with_options(
        self,
        request: arms20190808_models.ListClusterFromGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListClusterFromGrafanaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterFromGrafana',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListClusterFromGrafanaResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_from_grafana_with_options_async(
        self,
        request: arms20190808_models.ListClusterFromGrafanaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListClusterFromGrafanaResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterFromGrafana',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListClusterFromGrafanaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_from_grafana(
        self,
        request: arms20190808_models.ListClusterFromGrafanaRequest,
    ) -> arms20190808_models.ListClusterFromGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_from_grafana_with_options(request, runtime)

    async def list_cluster_from_grafana_async(
        self,
        request: arms20190808_models.ListClusterFromGrafanaRequest,
    ) -> arms20190808_models.ListClusterFromGrafanaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_from_grafana_with_options_async(request, runtime)

    def list_cms_instances_with_options(
        self,
        request: arms20190808_models.ListCmsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListCmsInstancesResponse:
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
            action='ListCmsInstances',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListCmsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cms_instances_with_options_async(
        self,
        request: arms20190808_models.ListCmsInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListCmsInstancesResponse:
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
            action='ListCmsInstances',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListCmsInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cms_instances(
        self,
        request: arms20190808_models.ListCmsInstancesRequest,
    ) -> arms20190808_models.ListCmsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cms_instances_with_options(request, runtime)

    async def list_cms_instances_async(
        self,
        request: arms20190808_models.ListCmsInstancesRequest,
    ) -> arms20190808_models.ListCmsInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cms_instances_with_options_async(request, runtime)

    def list_dashboards_with_options(
        self,
        request: arms20190808_models.ListDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListDashboardsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.dashboard_name):
            query['DashboardName'] = request.dashboard_name
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListDashboardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dashboards_with_options_async(
        self,
        request: arms20190808_models.ListDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListDashboardsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.dashboard_name):
            query['DashboardName'] = request.dashboard_name
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListDashboardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dashboards(
        self,
        request: arms20190808_models.ListDashboardsRequest,
    ) -> arms20190808_models.ListDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dashboards_with_options(request, runtime)

    async def list_dashboards_async(
        self,
        request: arms20190808_models.ListDashboardsRequest,
    ) -> arms20190808_models.ListDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dashboards_with_options_async(request, runtime)

    def list_dispatch_rule_with_options(
        self,
        request: arms20190808_models.ListDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListDispatchRuleResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dispatch_rule_with_options_async(
        self,
        request: arms20190808_models.ListDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListDispatchRuleResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListDispatchRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dispatch_rule(
        self,
        request: arms20190808_models.ListDispatchRuleRequest,
    ) -> arms20190808_models.ListDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dispatch_rule_with_options(request, runtime)

    async def list_dispatch_rule_async(
        self,
        request: arms20190808_models.ListDispatchRuleRequest,
    ) -> arms20190808_models.ListDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dispatch_rule_with_options_async(request, runtime)

    def list_escalation_policies_with_options(
        self,
        request: arms20190808_models.ListEscalationPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListEscalationPoliciesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEscalationPolicies',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEscalationPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_escalation_policies_with_options_async(
        self,
        request: arms20190808_models.ListEscalationPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListEscalationPoliciesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEscalationPolicies',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEscalationPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_escalation_policies(
        self,
        request: arms20190808_models.ListEscalationPoliciesRequest,
    ) -> arms20190808_models.ListEscalationPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_escalation_policies_with_options(request, runtime)

    async def list_escalation_policies_async(
        self,
        request: arms20190808_models.ListEscalationPoliciesRequest,
    ) -> arms20190808_models.ListEscalationPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_escalation_policies_with_options_async(request, runtime)

    def list_event_bridge_integrations_with_options(
        self,
        request: arms20190808_models.ListEventBridgeIntegrationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListEventBridgeIntegrationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventBridgeIntegrations',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEventBridgeIntegrationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_event_bridge_integrations_with_options_async(
        self,
        request: arms20190808_models.ListEventBridgeIntegrationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListEventBridgeIntegrationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventBridgeIntegrations',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEventBridgeIntegrationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_event_bridge_integrations(
        self,
        request: arms20190808_models.ListEventBridgeIntegrationsRequest,
    ) -> arms20190808_models.ListEventBridgeIntegrationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_event_bridge_integrations_with_options(request, runtime)

    async def list_event_bridge_integrations_async(
        self,
        request: arms20190808_models.ListEventBridgeIntegrationsRequest,
    ) -> arms20190808_models.ListEventBridgeIntegrationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_event_bridge_integrations_with_options_async(request, runtime)

    def list_notification_policies_with_options(
        self,
        request: arms20190808_models.ListNotificationPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListNotificationPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNotificationPolicies',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListNotificationPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_notification_policies_with_options_async(
        self,
        request: arms20190808_models.ListNotificationPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListNotificationPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNotificationPolicies',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListNotificationPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_notification_policies(
        self,
        request: arms20190808_models.ListNotificationPoliciesRequest,
    ) -> arms20190808_models.ListNotificationPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_notification_policies_with_options(request, runtime)

    async def list_notification_policies_async(
        self,
        request: arms20190808_models.ListNotificationPoliciesRequest,
    ) -> arms20190808_models.ListNotificationPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_notification_policies_with_options_async(request, runtime)

    def list_on_call_schedules_with_options(
        self,
        request: arms20190808_models.ListOnCallSchedulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListOnCallSchedulesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOnCallSchedules',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListOnCallSchedulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_on_call_schedules_with_options_async(
        self,
        request: arms20190808_models.ListOnCallSchedulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListOnCallSchedulesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOnCallSchedules',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListOnCallSchedulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_on_call_schedules(
        self,
        request: arms20190808_models.ListOnCallSchedulesRequest,
    ) -> arms20190808_models.ListOnCallSchedulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_on_call_schedules_with_options(request, runtime)

    async def list_on_call_schedules_async(
        self,
        request: arms20190808_models.ListOnCallSchedulesRequest,
    ) -> arms20190808_models.ListOnCallSchedulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_on_call_schedules_with_options_async(request, runtime)

    def list_prometheus_alert_rules_with_options(
        self,
        request: arms20190808_models.ListPrometheusAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPrometheusAlertRulesResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_alert_rules_with_options_async(
        self,
        request: arms20190808_models.ListPrometheusAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPrometheusAlertRulesResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_alert_rules(
        self,
        request: arms20190808_models.ListPrometheusAlertRulesRequest,
    ) -> arms20190808_models.ListPrometheusAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_alert_rules_with_options(request, runtime)

    async def list_prometheus_alert_rules_async(
        self,
        request: arms20190808_models.ListPrometheusAlertRulesRequest,
    ) -> arms20190808_models.ListPrometheusAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_prometheus_alert_rules_with_options_async(request, runtime)

    def list_prometheus_alert_templates_with_options(
        self,
        request: arms20190808_models.ListPrometheusAlertTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPrometheusAlertTemplatesResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusAlertTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_alert_templates_with_options_async(
        self,
        request: arms20190808_models.ListPrometheusAlertTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPrometheusAlertTemplatesResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusAlertTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_alert_templates(
        self,
        request: arms20190808_models.ListPrometheusAlertTemplatesRequest,
    ) -> arms20190808_models.ListPrometheusAlertTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_alert_templates_with_options(request, runtime)

    async def list_prometheus_alert_templates_async(
        self,
        request: arms20190808_models.ListPrometheusAlertTemplatesRequest,
    ) -> arms20190808_models.ListPrometheusAlertTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_prometheus_alert_templates_with_options_async(request, runtime)

    def list_prometheus_global_view_with_options(
        self,
        request: arms20190808_models.ListPrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_global_view_with_options_async(
        self,
        request: arms20190808_models.ListPrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_global_view(
        self,
        request: arms20190808_models.ListPrometheusGlobalViewRequest,
    ) -> arms20190808_models.ListPrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_global_view_with_options(request, runtime)

    async def list_prometheus_global_view_async(
        self,
        request: arms20190808_models.ListPrometheusGlobalViewRequest,
    ) -> arms20190808_models.ListPrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_prometheus_global_view_with_options_async(request, runtime)

    def list_retcode_apps_with_options(
        self,
        request: arms20190808_models.ListRetcodeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListRetcodeAppsResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListRetcodeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_retcode_apps_with_options_async(
        self,
        request: arms20190808_models.ListRetcodeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListRetcodeAppsResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListRetcodeAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_retcode_apps(
        self,
        request: arms20190808_models.ListRetcodeAppsRequest,
    ) -> arms20190808_models.ListRetcodeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_retcode_apps_with_options(request, runtime)

    async def list_retcode_apps_async(
        self,
        request: arms20190808_models.ListRetcodeAppsRequest,
    ) -> arms20190808_models.ListRetcodeAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_retcode_apps_with_options_async(request, runtime)

    def list_scenario_with_options(
        self,
        request: arms20190808_models.ListScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListScenarioResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_scenario_with_options_async(
        self,
        request: arms20190808_models.ListScenarioRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListScenarioResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListScenarioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_scenario(
        self,
        request: arms20190808_models.ListScenarioRequest,
    ) -> arms20190808_models.ListScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_scenario_with_options(request, runtime)

    async def list_scenario_async(
        self,
        request: arms20190808_models.ListScenarioRequest,
    ) -> arms20190808_models.ListScenarioResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_scenario_with_options_async(request, runtime)

    def list_silence_policies_with_options(
        self,
        request: arms20190808_models.ListSilencePoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListSilencePoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSilencePolicies',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListSilencePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_silence_policies_with_options_async(
        self,
        request: arms20190808_models.ListSilencePoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListSilencePoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSilencePolicies',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListSilencePoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_silence_policies(
        self,
        request: arms20190808_models.ListSilencePoliciesRequest,
    ) -> arms20190808_models.ListSilencePoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_silence_policies_with_options(request, runtime)

    async def list_silence_policies_async(
        self,
        request: arms20190808_models.ListSilencePoliciesRequest,
    ) -> arms20190808_models.ListSilencePoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_silence_policies_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: arms20190808_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: arms20190808_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: arms20190808_models.ListTagResourcesRequest,
    ) -> arms20190808_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: arms20190808_models.ListTagResourcesRequest,
    ) -> arms20190808_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_trace_apps_with_options(
        self,
        request: arms20190808_models.ListTraceAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListTraceAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTraceApps',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListTraceAppsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_trace_apps_with_options_async(
        self,
        request: arms20190808_models.ListTraceAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListTraceAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTraceApps',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListTraceAppsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_trace_apps(
        self,
        request: arms20190808_models.ListTraceAppsRequest,
    ) -> arms20190808_models.ListTraceAppsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_trace_apps_with_options(request, runtime)

    async def list_trace_apps_async(
        self,
        request: arms20190808_models.ListTraceAppsRequest,
    ) -> arms20190808_models.ListTraceAppsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_trace_apps_with_options_async(request, runtime)

    def manage_get_recording_rule_with_options(
        self,
        request: arms20190808_models.ManageGetRecordingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ManageGetRecordingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.query_user_id):
            query['QueryUserId'] = request.query_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ManageGetRecordingRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ManageGetRecordingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def manage_get_recording_rule_with_options_async(
        self,
        request: arms20190808_models.ManageGetRecordingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ManageGetRecordingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.query_user_id):
            query['QueryUserId'] = request.query_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ManageGetRecordingRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ManageGetRecordingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manage_get_recording_rule(
        self,
        request: arms20190808_models.ManageGetRecordingRuleRequest,
    ) -> arms20190808_models.ManageGetRecordingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.manage_get_recording_rule_with_options(request, runtime)

    async def manage_get_recording_rule_async(
        self,
        request: arms20190808_models.ManageGetRecordingRuleRequest,
    ) -> arms20190808_models.ManageGetRecordingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.manage_get_recording_rule_with_options_async(request, runtime)

    def manage_recording_rule_with_options(
        self,
        request: arms20190808_models.ManageRecordingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ManageRecordingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.query_user_id):
            query['QueryUserId'] = request.query_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_yaml):
            query['RuleYaml'] = request.rule_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ManageRecordingRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ManageRecordingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def manage_recording_rule_with_options_async(
        self,
        request: arms20190808_models.ManageRecordingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ManageRecordingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.query_user_id):
            query['QueryUserId'] = request.query_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_yaml):
            query['RuleYaml'] = request.rule_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ManageRecordingRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ManageRecordingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def manage_recording_rule(
        self,
        request: arms20190808_models.ManageRecordingRuleRequest,
    ) -> arms20190808_models.ManageRecordingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.manage_recording_rule_with_options(request, runtime)

    async def manage_recording_rule_async(
        self,
        request: arms20190808_models.ManageRecordingRuleRequest,
    ) -> arms20190808_models.ManageRecordingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.manage_recording_rule_with_options_async(request, runtime)

    def open_arms_default_slrwith_options(
        self,
        request: arms20190808_models.OpenArmsDefaultSLRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.OpenArmsDefaultSLRResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenArmsDefaultSLR',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.OpenArmsDefaultSLRResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_arms_default_slrwith_options_async(
        self,
        request: arms20190808_models.OpenArmsDefaultSLRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.OpenArmsDefaultSLRResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenArmsDefaultSLR',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.OpenArmsDefaultSLRResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_arms_default_slr(
        self,
        request: arms20190808_models.OpenArmsDefaultSLRRequest,
    ) -> arms20190808_models.OpenArmsDefaultSLRResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_arms_default_slrwith_options(request, runtime)

    async def open_arms_default_slr_async(
        self,
        request: arms20190808_models.OpenArmsDefaultSLRRequest,
    ) -> arms20190808_models.OpenArmsDefaultSLRResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_arms_default_slrwith_options_async(request, runtime)

    def open_arms_service_with_options(
        self,
        request: arms20190808_models.OpenArmsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.OpenArmsServiceResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.OpenArmsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_arms_service_with_options_async(
        self,
        request: arms20190808_models.OpenArmsServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.OpenArmsServiceResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.OpenArmsServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_arms_service(
        self,
        request: arms20190808_models.OpenArmsServiceRequest,
    ) -> arms20190808_models.OpenArmsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_arms_service_with_options(request, runtime)

    async def open_arms_service_async(
        self,
        request: arms20190808_models.OpenArmsServiceRequest,
    ) -> arms20190808_models.OpenArmsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_arms_service_with_options_async(request, runtime)

    def open_arms_service_second_version_with_options(
        self,
        request: arms20190808_models.OpenArmsServiceSecondVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.OpenArmsServiceSecondVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenArmsServiceSecondVersion',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.OpenArmsServiceSecondVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_arms_service_second_version_with_options_async(
        self,
        request: arms20190808_models.OpenArmsServiceSecondVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.OpenArmsServiceSecondVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenArmsServiceSecondVersion',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.OpenArmsServiceSecondVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_arms_service_second_version(
        self,
        request: arms20190808_models.OpenArmsServiceSecondVersionRequest,
    ) -> arms20190808_models.OpenArmsServiceSecondVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_arms_service_second_version_with_options(request, runtime)

    async def open_arms_service_second_version_async(
        self,
        request: arms20190808_models.OpenArmsServiceSecondVersionRequest,
    ) -> arms20190808_models.OpenArmsServiceSecondVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_arms_service_second_version_with_options_async(request, runtime)

    def open_vcluster_with_options(
        self,
        request: arms20190808_models.OpenVClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.OpenVClusterResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.OpenVClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_vcluster_with_options_async(
        self,
        request: arms20190808_models.OpenVClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.OpenVClusterResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.OpenVClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_vcluster(
        self,
        request: arms20190808_models.OpenVClusterRequest,
    ) -> arms20190808_models.OpenVClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_vcluster_with_options(request, runtime)

    async def open_vcluster_async(
        self,
        request: arms20190808_models.OpenVClusterRequest,
    ) -> arms20190808_models.OpenVClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_vcluster_with_options_async(request, runtime)

    def open_xtrace_default_slrwith_options(
        self,
        request: arms20190808_models.OpenXtraceDefaultSLRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.OpenXtraceDefaultSLRResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenXtraceDefaultSLR',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.OpenXtraceDefaultSLRResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_xtrace_default_slrwith_options_async(
        self,
        request: arms20190808_models.OpenXtraceDefaultSLRRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.OpenXtraceDefaultSLRResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenXtraceDefaultSLR',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.OpenXtraceDefaultSLRResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_xtrace_default_slr(
        self,
        request: arms20190808_models.OpenXtraceDefaultSLRRequest,
    ) -> arms20190808_models.OpenXtraceDefaultSLRResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_xtrace_default_slrwith_options(request, runtime)

    async def open_xtrace_default_slr_async(
        self,
        request: arms20190808_models.OpenXtraceDefaultSLRRequest,
    ) -> arms20190808_models.OpenXtraceDefaultSLRResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_xtrace_default_slrwith_options_async(request, runtime)

    def prom_vpc_exporter_manager_with_options(
        self,
        request: arms20190808_models.PromVpcExporterManagerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.PromVpcExporterManagerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.exporter_config):
            query['ExporterConfig'] = request.exporter_config
        if not UtilClient.is_unset(request.exporter_type):
            query['ExporterType'] = request.exporter_type
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PromVpcExporterManager',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.PromVpcExporterManagerResponse(),
            self.call_api(params, req, runtime)
        )

    async def prom_vpc_exporter_manager_with_options_async(
        self,
        request: arms20190808_models.PromVpcExporterManagerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.PromVpcExporterManagerResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.exporter_config):
            query['ExporterConfig'] = request.exporter_config
        if not UtilClient.is_unset(request.exporter_type):
            query['ExporterType'] = request.exporter_type
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PromVpcExporterManager',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.PromVpcExporterManagerResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def prom_vpc_exporter_manager(
        self,
        request: arms20190808_models.PromVpcExporterManagerRequest,
    ) -> arms20190808_models.PromVpcExporterManagerResponse:
        runtime = util_models.RuntimeOptions()
        return self.prom_vpc_exporter_manager_with_options(request, runtime)

    async def prom_vpc_exporter_manager_async(
        self,
        request: arms20190808_models.PromVpcExporterManagerRequest,
    ) -> arms20190808_models.PromVpcExporterManagerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.prom_vpc_exporter_manager_with_options_async(request, runtime)

    def query_dataset_with_options(
        self,
        request: arms20190808_models.QueryDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryDatasetResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.QueryDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_dataset_with_options_async(
        self,
        request: arms20190808_models.QueryDatasetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryDatasetResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.QueryDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_dataset(
        self,
        request: arms20190808_models.QueryDatasetRequest,
    ) -> arms20190808_models.QueryDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_with_options(request, runtime)

    async def query_dataset_async(
        self,
        request: arms20190808_models.QueryDatasetRequest,
    ) -> arms20190808_models.QueryDatasetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_dataset_with_options_async(request, runtime)

    def query_metric_by_page_with_options(
        self,
        request: arms20190808_models.QueryMetricByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryMetricByPageResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.QueryMetricByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_metric_by_page_with_options_async(
        self,
        request: arms20190808_models.QueryMetricByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryMetricByPageResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.QueryMetricByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_metric_by_page(
        self,
        request: arms20190808_models.QueryMetricByPageRequest,
    ) -> arms20190808_models.QueryMetricByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_metric_by_page_with_options(request, runtime)

    async def query_metric_by_page_async(
        self,
        request: arms20190808_models.QueryMetricByPageRequest,
    ) -> arms20190808_models.QueryMetricByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_metric_by_page_with_options_async(request, runtime)

    def query_prom_install_status_with_options(
        self,
        request: arms20190808_models.QueryPromInstallStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryPromInstallStatusResponse:
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
            action='QueryPromInstallStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.QueryPromInstallStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_prom_install_status_with_options_async(
        self,
        request: arms20190808_models.QueryPromInstallStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryPromInstallStatusResponse:
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
            action='QueryPromInstallStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.QueryPromInstallStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_prom_install_status(
        self,
        request: arms20190808_models.QueryPromInstallStatusRequest,
    ) -> arms20190808_models.QueryPromInstallStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_prom_install_status_with_options(request, runtime)

    async def query_prom_install_status_async(
        self,
        request: arms20190808_models.QueryPromInstallStatusRequest,
    ) -> arms20190808_models.QueryPromInstallStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_prom_install_status_with_options_async(request, runtime)

    def query_release_metric_with_options(
        self,
        request: arms20190808_models.QueryReleaseMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryReleaseMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.release_end_time):
            query['ReleaseEndTime'] = request.release_end_time
        if not UtilClient.is_unset(request.release_start_time):
            query['ReleaseStartTime'] = request.release_start_time
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryReleaseMetric',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.QueryReleaseMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_release_metric_with_options_async(
        self,
        request: arms20190808_models.QueryReleaseMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryReleaseMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.release_end_time):
            query['ReleaseEndTime'] = request.release_end_time
        if not UtilClient.is_unset(request.release_start_time):
            query['ReleaseStartTime'] = request.release_start_time
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryReleaseMetric',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.QueryReleaseMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_release_metric(
        self,
        request: arms20190808_models.QueryReleaseMetricRequest,
    ) -> arms20190808_models.QueryReleaseMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_release_metric_with_options(request, runtime)

    async def query_release_metric_async(
        self,
        request: arms20190808_models.QueryReleaseMetricRequest,
    ) -> arms20190808_models.QueryReleaseMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_release_metric_with_options_async(request, runtime)

    def query_traces_with_options(
        self,
        request: arms20190808_models.QueryTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryTracesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTraces',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.QueryTracesResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_traces_with_options_async(
        self,
        request: arms20190808_models.QueryTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryTracesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTraces',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.QueryTracesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_traces(
        self,
        request: arms20190808_models.QueryTracesRequest,
    ) -> arms20190808_models.QueryTracesResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_traces_with_options(request, runtime)

    async def query_traces_async(
        self,
        request: arms20190808_models.QueryTracesRequest,
    ) -> arms20190808_models.QueryTracesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_traces_with_options_async(request, runtime)

    def remove_ali_cluster_ids_from_prometheus_global_view_with_options(
        self,
        request: arms20190808_models.RemoveAliClusterIdsFromPrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.RemoveAliClusterIdsFromPrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAliClusterIdsFromPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.RemoveAliClusterIdsFromPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_ali_cluster_ids_from_prometheus_global_view_with_options_async(
        self,
        request: arms20190808_models.RemoveAliClusterIdsFromPrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.RemoveAliClusterIdsFromPrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAliClusterIdsFromPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.RemoveAliClusterIdsFromPrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_ali_cluster_ids_from_prometheus_global_view(
        self,
        request: arms20190808_models.RemoveAliClusterIdsFromPrometheusGlobalViewRequest,
    ) -> arms20190808_models.RemoveAliClusterIdsFromPrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_ali_cluster_ids_from_prometheus_global_view_with_options(request, runtime)

    async def remove_ali_cluster_ids_from_prometheus_global_view_async(
        self,
        request: arms20190808_models.RemoveAliClusterIdsFromPrometheusGlobalViewRequest,
    ) -> arms20190808_models.RemoveAliClusterIdsFromPrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_ali_cluster_ids_from_prometheus_global_view_with_options_async(request, runtime)

    def remove_sources_from_prometheus_global_view_with_options(
        self,
        request: arms20190808_models.RemoveSourcesFromPrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.RemoveSourcesFromPrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_names):
            query['SourceNames'] = request.source_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSourcesFromPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.RemoveSourcesFromPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_sources_from_prometheus_global_view_with_options_async(
        self,
        request: arms20190808_models.RemoveSourcesFromPrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.RemoveSourcesFromPrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_names):
            query['SourceNames'] = request.source_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSourcesFromPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.RemoveSourcesFromPrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_sources_from_prometheus_global_view(
        self,
        request: arms20190808_models.RemoveSourcesFromPrometheusGlobalViewRequest,
    ) -> arms20190808_models.RemoveSourcesFromPrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_sources_from_prometheus_global_view_with_options(request, runtime)

    async def remove_sources_from_prometheus_global_view_async(
        self,
        request: arms20190808_models.RemoveSourcesFromPrometheusGlobalViewRequest,
    ) -> arms20190808_models.RemoveSourcesFromPrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_sources_from_prometheus_global_view_with_options_async(request, runtime)

    def save_trace_app_config_with_options(
        self,
        request: arms20190808_models.SaveTraceAppConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SaveTraceAppConfigResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SaveTraceAppConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def save_trace_app_config_with_options_async(
        self,
        request: arms20190808_models.SaveTraceAppConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SaveTraceAppConfigResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SaveTraceAppConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def save_trace_app_config(
        self,
        request: arms20190808_models.SaveTraceAppConfigRequest,
    ) -> arms20190808_models.SaveTraceAppConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.save_trace_app_config_with_options(request, runtime)

    async def save_trace_app_config_async(
        self,
        request: arms20190808_models.SaveTraceAppConfigRequest,
    ) -> arms20190808_models.SaveTraceAppConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.save_trace_app_config_with_options_async(request, runtime)

    def search_alert_contact_with_options(
        self,
        request: arms20190808_models.SearchAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertContactResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_alert_contact_with_options_async(
        self,
        request: arms20190808_models.SearchAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertContactResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_alert_contact(
        self,
        request: arms20190808_models.SearchAlertContactRequest,
    ) -> arms20190808_models.SearchAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_alert_contact_with_options(request, runtime)

    async def search_alert_contact_async(
        self,
        request: arms20190808_models.SearchAlertContactRequest,
    ) -> arms20190808_models.SearchAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_contact_with_options_async(request, runtime)

    def search_alert_contact_group_with_options(
        self,
        request: arms20190808_models.SearchAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertContactGroupResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_alert_contact_group_with_options_async(
        self,
        request: arms20190808_models.SearchAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertContactGroupResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_alert_contact_group(
        self,
        request: arms20190808_models.SearchAlertContactGroupRequest,
    ) -> arms20190808_models.SearchAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_alert_contact_group_with_options(request, runtime)

    async def search_alert_contact_group_async(
        self,
        request: arms20190808_models.SearchAlertContactGroupRequest,
    ) -> arms20190808_models.SearchAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_contact_group_with_options_async(request, runtime)

    def search_alert_histories_with_options(
        self,
        request: arms20190808_models.SearchAlertHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertHistoriesResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchAlertHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_alert_histories_with_options_async(
        self,
        request: arms20190808_models.SearchAlertHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertHistoriesResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchAlertHistoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_alert_histories(
        self,
        request: arms20190808_models.SearchAlertHistoriesRequest,
    ) -> arms20190808_models.SearchAlertHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_alert_histories_with_options(request, runtime)

    async def search_alert_histories_async(
        self,
        request: arms20190808_models.SearchAlertHistoriesRequest,
    ) -> arms20190808_models.SearchAlertHistoriesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_histories_with_options_async(request, runtime)

    def search_alert_historys_with_options(
        self,
        request: arms20190808_models.SearchAlertHistorysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertHistorysResponse:
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
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchAlertHistorys',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchAlertHistorysResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_alert_historys_with_options_async(
        self,
        request: arms20190808_models.SearchAlertHistorysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertHistorysResponse:
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
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchAlertHistorys',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchAlertHistorysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_alert_historys(
        self,
        request: arms20190808_models.SearchAlertHistorysRequest,
    ) -> arms20190808_models.SearchAlertHistorysResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_alert_historys_with_options(request, runtime)

    async def search_alert_historys_async(
        self,
        request: arms20190808_models.SearchAlertHistorysRequest,
    ) -> arms20190808_models.SearchAlertHistorysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_historys_with_options_async(request, runtime)

    def search_alert_rules_with_options(
        self,
        request: arms20190808_models.SearchAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertRulesResponse:
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
        if not UtilClient.is_unset(request.system_region_id):
            query['SystemRegionId'] = request.system_region_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchAlertRules',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_alert_rules_with_options_async(
        self,
        request: arms20190808_models.SearchAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertRulesResponse:
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
        if not UtilClient.is_unset(request.system_region_id):
            query['SystemRegionId'] = request.system_region_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchAlertRules',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchAlertRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_alert_rules(
        self,
        request: arms20190808_models.SearchAlertRulesRequest,
    ) -> arms20190808_models.SearchAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_alert_rules_with_options(request, runtime)

    async def search_alert_rules_async(
        self,
        request: arms20190808_models.SearchAlertRulesRequest,
    ) -> arms20190808_models.SearchAlertRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_rules_with_options_async(request, runtime)

    def search_events_with_options(
        self,
        request: arms20190808_models.SearchEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchEventsResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_events_with_options_async(
        self,
        request: arms20190808_models.SearchEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchEventsResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_events(
        self,
        request: arms20190808_models.SearchEventsRequest,
    ) -> arms20190808_models.SearchEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_events_with_options(request, runtime)

    async def search_events_async(
        self,
        request: arms20190808_models.SearchEventsRequest,
    ) -> arms20190808_models.SearchEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_events_with_options_async(request, runtime)

    def search_retcode_app_by_page_with_options(
        self,
        request: arms20190808_models.SearchRetcodeAppByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchRetcodeAppByPageResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchRetcodeAppByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_retcode_app_by_page_with_options_async(
        self,
        request: arms20190808_models.SearchRetcodeAppByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchRetcodeAppByPageResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchRetcodeAppByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_retcode_app_by_page(
        self,
        request: arms20190808_models.SearchRetcodeAppByPageRequest,
    ) -> arms20190808_models.SearchRetcodeAppByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_retcode_app_by_page_with_options(request, runtime)

    async def search_retcode_app_by_page_async(
        self,
        request: arms20190808_models.SearchRetcodeAppByPageRequest,
    ) -> arms20190808_models.SearchRetcodeAppByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_retcode_app_by_page_with_options_async(request, runtime)

    def search_tag_names_with_options(
        self,
        request: arms20190808_models.SearchTagNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTagNamesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='SearchTagNames',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchTagNamesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_tag_names_with_options_async(
        self,
        request: arms20190808_models.SearchTagNamesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTagNamesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='SearchTagNames',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchTagNamesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_tag_names(
        self,
        request: arms20190808_models.SearchTagNamesRequest,
    ) -> arms20190808_models.SearchTagNamesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_tag_names_with_options(request, runtime)

    async def search_tag_names_async(
        self,
        request: arms20190808_models.SearchTagNamesRequest,
    ) -> arms20190808_models.SearchTagNamesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_tag_names_with_options_async(request, runtime)

    def search_tag_values_with_options(
        self,
        request: arms20190808_models.SearchTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='SearchTagValues',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_tag_values_with_options_async(
        self,
        request: arms20190808_models.SearchTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
            action='SearchTagValues',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_tag_values(
        self,
        request: arms20190808_models.SearchTagValuesRequest,
    ) -> arms20190808_models.SearchTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_tag_values_with_options(request, runtime)

    async def search_tag_values_async(
        self,
        request: arms20190808_models.SearchTagValuesRequest,
    ) -> arms20190808_models.SearchTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_tag_values_with_options_async(request, runtime)

    def search_trace_app_by_name_with_options(
        self,
        request: arms20190808_models.SearchTraceAppByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTraceAppByNameResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchTraceAppByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_trace_app_by_name_with_options_async(
        self,
        request: arms20190808_models.SearchTraceAppByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTraceAppByNameResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchTraceAppByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_trace_app_by_name(
        self,
        request: arms20190808_models.SearchTraceAppByNameRequest,
    ) -> arms20190808_models.SearchTraceAppByNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_trace_app_by_name_with_options(request, runtime)

    async def search_trace_app_by_name_async(
        self,
        request: arms20190808_models.SearchTraceAppByNameRequest,
    ) -> arms20190808_models.SearchTraceAppByNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_trace_app_by_name_with_options_async(request, runtime)

    def search_trace_app_by_page_with_options(
        self,
        request: arms20190808_models.SearchTraceAppByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTraceAppByPageResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchTraceAppByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_trace_app_by_page_with_options_async(
        self,
        request: arms20190808_models.SearchTraceAppByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTraceAppByPageResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchTraceAppByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_trace_app_by_page(
        self,
        request: arms20190808_models.SearchTraceAppByPageRequest,
    ) -> arms20190808_models.SearchTraceAppByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_trace_app_by_page_with_options(request, runtime)

    async def search_trace_app_by_page_async(
        self,
        request: arms20190808_models.SearchTraceAppByPageRequest,
    ) -> arms20190808_models.SearchTraceAppByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_trace_app_by_page_with_options_async(request, runtime)

    def search_traces_with_options(
        self,
        request: arms20190808_models.SearchTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTracesResponse:
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
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchTracesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_traces_with_options_async(
        self,
        request: arms20190808_models.SearchTracesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTracesResponse:
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
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchTracesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_traces(
        self,
        request: arms20190808_models.SearchTracesRequest,
    ) -> arms20190808_models.SearchTracesResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_traces_with_options(request, runtime)

    async def search_traces_async(
        self,
        request: arms20190808_models.SearchTracesRequest,
    ) -> arms20190808_models.SearchTracesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_traces_with_options_async(request, runtime)

    def search_traces_by_page_with_options(
        self,
        request: arms20190808_models.SearchTracesByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTracesByPageResponse:
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
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTracesByPage',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchTracesByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_traces_by_page_with_options_async(
        self,
        request: arms20190808_models.SearchTracesByPageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTracesByPageResponse:
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
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTracesByPage',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchTracesByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_traces_by_page(
        self,
        request: arms20190808_models.SearchTracesByPageRequest,
    ) -> arms20190808_models.SearchTracesByPageResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_traces_by_page_with_options(request, runtime)

    async def search_traces_by_page_async(
        self,
        request: arms20190808_models.SearchTracesByPageRequest,
    ) -> arms20190808_models.SearchTracesByPageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_traces_by_page_with_options_async(request, runtime)

    def send_ttsverify_link_with_options(
        self,
        request: arms20190808_models.SendTTSVerifyLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SendTTSVerifyLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.contact_id):
            body['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendTTSVerifyLink',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SendTTSVerifyLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_ttsverify_link_with_options_async(
        self,
        request: arms20190808_models.SendTTSVerifyLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SendTTSVerifyLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.contact_id):
            body['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendTTSVerifyLink',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SendTTSVerifyLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_ttsverify_link(
        self,
        request: arms20190808_models.SendTTSVerifyLinkRequest,
    ) -> arms20190808_models.SendTTSVerifyLinkResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_ttsverify_link_with_options(request, runtime)

    async def send_ttsverify_link_async(
        self,
        request: arms20190808_models.SendTTSVerifyLinkRequest,
    ) -> arms20190808_models.SendTTSVerifyLinkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_ttsverify_link_with_options_async(request, runtime)

    def set_retcode_share_status_with_options(
        self,
        request: arms20190808_models.SetRetcodeShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SetRetcodeShareStatusResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SetRetcodeShareStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_retcode_share_status_with_options_async(
        self,
        request: arms20190808_models.SetRetcodeShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SetRetcodeShareStatusResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SetRetcodeShareStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_retcode_share_status(
        self,
        request: arms20190808_models.SetRetcodeShareStatusRequest,
    ) -> arms20190808_models.SetRetcodeShareStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_retcode_share_status_with_options(request, runtime)

    async def set_retcode_share_status_async(
        self,
        request: arms20190808_models.SetRetcodeShareStatusRequest,
    ) -> arms20190808_models.SetRetcodeShareStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_retcode_share_status_with_options_async(request, runtime)

    def start_alert_with_options(
        self,
        request: arms20190808_models.StartAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.StartAlertResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.StartAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_alert_with_options_async(
        self,
        request: arms20190808_models.StartAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.StartAlertResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.StartAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_alert(
        self,
        request: arms20190808_models.StartAlertRequest,
    ) -> arms20190808_models.StartAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_alert_with_options(request, runtime)

    async def start_alert_async(
        self,
        request: arms20190808_models.StartAlertRequest,
    ) -> arms20190808_models.StartAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_alert_with_options_async(request, runtime)

    def stop_alert_with_options(
        self,
        request: arms20190808_models.StopAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.StopAlertResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.StopAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_alert_with_options_async(
        self,
        request: arms20190808_models.StopAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.StopAlertResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.StopAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_alert(
        self,
        request: arms20190808_models.StopAlertRequest,
    ) -> arms20190808_models.StopAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_alert_with_options(request, runtime)

    async def stop_alert_async(
        self,
        request: arms20190808_models.StopAlertRequest,
    ) -> arms20190808_models.StopAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_alert_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: arms20190808_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: arms20190808_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: arms20190808_models.TagResourcesRequest,
    ) -> arms20190808_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: arms20190808_models.TagResourcesRequest,
    ) -> arms20190808_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def turn_on_second_switch_with_options(
        self,
        request: arms20190808_models.TurnOnSecondSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.TurnOnSecondSwitchResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TurnOnSecondSwitch',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.TurnOnSecondSwitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def turn_on_second_switch_with_options_async(
        self,
        request: arms20190808_models.TurnOnSecondSwitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.TurnOnSecondSwitchResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TurnOnSecondSwitch',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.TurnOnSecondSwitchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def turn_on_second_switch(
        self,
        request: arms20190808_models.TurnOnSecondSwitchRequest,
    ) -> arms20190808_models.TurnOnSecondSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.turn_on_second_switch_with_options(request, runtime)

    async def turn_on_second_switch_async(
        self,
        request: arms20190808_models.TurnOnSecondSwitchRequest,
    ) -> arms20190808_models.TurnOnSecondSwitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.turn_on_second_switch_with_options_async(request, runtime)

    def uninstall_managed_prometheus_with_options(
        self,
        request: arms20190808_models.UninstallManagedPrometheusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UninstallManagedPrometheusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallManagedPrometheus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UninstallManagedPrometheusResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_managed_prometheus_with_options_async(
        self,
        request: arms20190808_models.UninstallManagedPrometheusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UninstallManagedPrometheusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallManagedPrometheus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UninstallManagedPrometheusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_managed_prometheus(
        self,
        request: arms20190808_models.UninstallManagedPrometheusRequest,
    ) -> arms20190808_models.UninstallManagedPrometheusResponse:
        runtime = util_models.RuntimeOptions()
        return self.uninstall_managed_prometheus_with_options(request, runtime)

    async def uninstall_managed_prometheus_async(
        self,
        request: arms20190808_models.UninstallManagedPrometheusRequest,
    ) -> arms20190808_models.UninstallManagedPrometheusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.uninstall_managed_prometheus_with_options_async(request, runtime)

    def uninstall_prom_cluster_with_options(
        self,
        request: arms20190808_models.UninstallPromClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UninstallPromClusterResponse:
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
            action='UninstallPromCluster',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UninstallPromClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_prom_cluster_with_options_async(
        self,
        request: arms20190808_models.UninstallPromClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UninstallPromClusterResponse:
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
            action='UninstallPromCluster',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UninstallPromClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_prom_cluster(
        self,
        request: arms20190808_models.UninstallPromClusterRequest,
    ) -> arms20190808_models.UninstallPromClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.uninstall_prom_cluster_with_options(request, runtime)

    async def uninstall_prom_cluster_async(
        self,
        request: arms20190808_models.UninstallPromClusterRequest,
    ) -> arms20190808_models.UninstallPromClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.uninstall_prom_cluster_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: arms20190808_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: arms20190808_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: arms20190808_models.UntagResourcesRequest,
    ) -> arms20190808_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: arms20190808_models.UntagResourcesRequest,
    ) -> arms20190808_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_alert_contact_with_options(
        self,
        request: arms20190808_models.UpdateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateAlertContactResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alert_contact_with_options_async(
        self,
        request: arms20190808_models.UpdateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateAlertContactResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateAlertContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alert_contact(
        self,
        request: arms20190808_models.UpdateAlertContactRequest,
    ) -> arms20190808_models.UpdateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_alert_contact_with_options(request, runtime)

    async def update_alert_contact_async(
        self,
        request: arms20190808_models.UpdateAlertContactRequest,
    ) -> arms20190808_models.UpdateAlertContactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_alert_contact_with_options_async(request, runtime)

    def update_alert_contact_group_with_options(
        self,
        request: arms20190808_models.UpdateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateAlertContactGroupResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alert_contact_group_with_options_async(
        self,
        request: arms20190808_models.UpdateAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateAlertContactGroupResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateAlertContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alert_contact_group(
        self,
        request: arms20190808_models.UpdateAlertContactGroupRequest,
    ) -> arms20190808_models.UpdateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_alert_contact_group_with_options(request, runtime)

    async def update_alert_contact_group_async(
        self,
        request: arms20190808_models.UpdateAlertContactGroupRequest,
    ) -> arms20190808_models.UpdateAlertContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_alert_contact_group_with_options_async(request, runtime)

    def update_alert_rule_with_options(
        self,
        request: arms20190808_models.UpdateAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateAlertRuleResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alert_rule_with_options_async(
        self,
        request: arms20190808_models.UpdateAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateAlertRuleResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alert_rule(
        self,
        request: arms20190808_models.UpdateAlertRuleRequest,
    ) -> arms20190808_models.UpdateAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_alert_rule_with_options(request, runtime)

    async def update_alert_rule_async(
        self,
        request: arms20190808_models.UpdateAlertRuleRequest,
    ) -> arms20190808_models.UpdateAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_alert_rule_with_options_async(request, runtime)

    def update_dispatch_rule_with_options(
        self,
        request: arms20190808_models.UpdateDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateDispatchRuleResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_dispatch_rule_with_options_async(
        self,
        request: arms20190808_models.UpdateDispatchRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateDispatchRuleResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateDispatchRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_dispatch_rule(
        self,
        request: arms20190808_models.UpdateDispatchRuleRequest,
    ) -> arms20190808_models.UpdateDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_dispatch_rule_with_options(request, runtime)

    async def update_dispatch_rule_async(
        self,
        request: arms20190808_models.UpdateDispatchRuleRequest,
    ) -> arms20190808_models.UpdateDispatchRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_dispatch_rule_with_options_async(request, runtime)

    def update_prometheus_alert_rule_with_options(
        self,
        request: arms20190808_models.UpdatePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdatePrometheusAlertRuleResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_alert_rule_with_options_async(
        self,
        request: arms20190808_models.UpdatePrometheusAlertRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdatePrometheusAlertRuleResponse:
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
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusAlertRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_alert_rule(
        self,
        request: arms20190808_models.UpdatePrometheusAlertRuleRequest,
    ) -> arms20190808_models.UpdatePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_prometheus_alert_rule_with_options(request, runtime)

    async def update_prometheus_alert_rule_async(
        self,
        request: arms20190808_models.UpdatePrometheusAlertRuleRequest,
    ) -> arms20190808_models.UpdatePrometheusAlertRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_prometheus_alert_rule_with_options_async(request, runtime)

    def update_webhook_with_options(
        self,
        request: arms20190808_models.UpdateWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateWebhookResponse:
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
        if not UtilClient.is_unset(request.recover_body):
            query['RecoverBody'] = request.recover_body
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWebhook',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_webhook_with_options_async(
        self,
        request: arms20190808_models.UpdateWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateWebhookResponse:
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
        if not UtilClient.is_unset(request.recover_body):
            query['RecoverBody'] = request.recover_body
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWebhook',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_webhook(
        self,
        request: arms20190808_models.UpdateWebhookRequest,
    ) -> arms20190808_models.UpdateWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_webhook_with_options(request, runtime)

    async def update_webhook_async(
        self,
        request: arms20190808_models.UpdateWebhookRequest,
    ) -> arms20190808_models.UpdateWebhookResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_webhook_with_options_async(request, runtime)

    def upload_with_options(
        self,
        request: arms20190808_models.UploadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UploadResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file):
            query['File'] = request.file
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Upload',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UploadResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_with_options_async(
        self,
        request: arms20190808_models.UploadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UploadResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file):
            query['File'] = request.file
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Upload',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UploadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload(
        self,
        request: arms20190808_models.UploadRequest,
    ) -> arms20190808_models.UploadResponse:
        runtime = util_models.RuntimeOptions()
        return self.upload_with_options(request, runtime)

    async def upload_async(
        self,
        request: arms20190808_models.UploadRequest,
    ) -> arms20190808_models.UploadResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upload_with_options_async(request, runtime)
