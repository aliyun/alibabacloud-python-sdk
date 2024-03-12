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
        self._signature_algorithm = 'v2'
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
        """
        @deprecated : AddIntegration is deprecated, please use ARMS::2019-08-08::InstallAddon instead.
        
        @param request: AddIntegrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddIntegrationResponse
        Deprecated
        """
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
        """
        @deprecated : AddIntegration is deprecated, please use ARMS::2019-08-08::InstallAddon instead.
        
        @param request: AddIntegrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddIntegrationResponse
        Deprecated
        """
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
        """
        @deprecated : AddIntegration is deprecated, please use ARMS::2019-08-08::InstallAddon instead.
        
        @param request: AddIntegrationRequest
        @return: AddIntegrationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.add_integration_with_options(request, runtime)

    async def add_integration_async(
        self,
        request: arms20190808_models.AddIntegrationRequest,
    ) -> arms20190808_models.AddIntegrationResponse:
        """
        @deprecated : AddIntegration is deprecated, please use ARMS::2019-08-08::InstallAddon instead.
        
        @param request: AddIntegrationRequest
        @return: AddIntegrationResponse
        Deprecated
        """
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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

    def add_prometheus_instance_with_options(
        self,
        request: arms20190808_models.AddPrometheusInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddPrometheusInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='AddPrometheusInstance',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddPrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_prometheus_instance_with_options_async(
        self,
        request: arms20190808_models.AddPrometheusInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddPrometheusInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
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
            action='AddPrometheusInstance',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddPrometheusInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_prometheus_instance(
        self,
        request: arms20190808_models.AddPrometheusInstanceRequest,
    ) -> arms20190808_models.AddPrometheusInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_prometheus_instance_with_options(request, runtime)

    async def add_prometheus_instance_async(
        self,
        request: arms20190808_models.AddPrometheusInstanceRequest,
    ) -> arms20190808_models.AddPrometheusInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_prometheus_instance_with_options_async(request, runtime)

    def add_prometheus_integration_with_options(
        self,
        request: arms20190808_models.AddPrometheusIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddPrometheusIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPrometheusIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddPrometheusIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_prometheus_integration_with_options_async(
        self,
        request: arms20190808_models.AddPrometheusIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddPrometheusIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPrometheusIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddPrometheusIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_prometheus_integration(
        self,
        request: arms20190808_models.AddPrometheusIntegrationRequest,
    ) -> arms20190808_models.AddPrometheusIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_prometheus_integration_with_options(request, runtime)

    async def add_prometheus_integration_async(
        self,
        request: arms20190808_models.AddPrometheusIntegrationRequest,
    ) -> arms20190808_models.AddPrometheusIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_prometheus_integration_with_options_async(request, runtime)

    def add_prometheus_remote_write_with_options(
        self,
        request: arms20190808_models.AddPrometheusRemoteWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddPrometheusRemoteWriteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.remote_write_yaml):
            body['RemoteWriteYaml'] = request.remote_write_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddPrometheusRemoteWrite',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddPrometheusRemoteWriteResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_prometheus_remote_write_with_options_async(
        self,
        request: arms20190808_models.AddPrometheusRemoteWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddPrometheusRemoteWriteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.remote_write_yaml):
            body['RemoteWriteYaml'] = request.remote_write_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddPrometheusRemoteWrite',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddPrometheusRemoteWriteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_prometheus_remote_write(
        self,
        request: arms20190808_models.AddPrometheusRemoteWriteRequest,
    ) -> arms20190808_models.AddPrometheusRemoteWriteResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_prometheus_remote_write_with_options(request, runtime)

    async def add_prometheus_remote_write_async(
        self,
        request: arms20190808_models.AddPrometheusRemoteWriteRequest,
    ) -> arms20190808_models.AddPrometheusRemoteWriteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_prometheus_remote_write_with_options_async(request, runtime)

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

    def add_tag_to_flink_cluster_with_options(
        self,
        request: arms20190808_models.AddTagToFlinkClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddTagToFlinkClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.flink_work_space_id):
            query['FlinkWorkSpaceId'] = request.flink_work_space_id
        if not UtilClient.is_unset(request.flink_work_space_name):
            query['FlinkWorkSpaceName'] = request.flink_work_space_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTagToFlinkCluster',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddTagToFlinkClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_tag_to_flink_cluster_with_options_async(
        self,
        request: arms20190808_models.AddTagToFlinkClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.AddTagToFlinkClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.flink_work_space_id):
            query['FlinkWorkSpaceId'] = request.flink_work_space_id
        if not UtilClient.is_unset(request.flink_work_space_name):
            query['FlinkWorkSpaceName'] = request.flink_work_space_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTagToFlinkCluster',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddTagToFlinkClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_tag_to_flink_cluster(
        self,
        request: arms20190808_models.AddTagToFlinkClusterRequest,
    ) -> arms20190808_models.AddTagToFlinkClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_tag_to_flink_cluster_with_options(request, runtime)

    async def add_tag_to_flink_cluster_async(
        self,
        request: arms20190808_models.AddTagToFlinkClusterRequest,
    ) -> arms20190808_models.AddTagToFlinkClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_tag_to_flink_cluster_with_options_async(request, runtime)

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

    def bind_prometheus_grafana_instance_with_options(
        self,
        request: arms20190808_models.BindPrometheusGrafanaInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.BindPrometheusGrafanaInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.grafana_instance_id):
            query['GrafanaInstanceId'] = request.grafana_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindPrometheusGrafanaInstance',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.BindPrometheusGrafanaInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def bind_prometheus_grafana_instance_with_options_async(
        self,
        request: arms20190808_models.BindPrometheusGrafanaInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.BindPrometheusGrafanaInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.grafana_instance_id):
            query['GrafanaInstanceId'] = request.grafana_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindPrometheusGrafanaInstance',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.BindPrometheusGrafanaInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def bind_prometheus_grafana_instance(
        self,
        request: arms20190808_models.BindPrometheusGrafanaInstanceRequest,
    ) -> arms20190808_models.BindPrometheusGrafanaInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.bind_prometheus_grafana_instance_with_options(request, runtime)

    async def bind_prometheus_grafana_instance_async(
        self,
        request: arms20190808_models.BindPrometheusGrafanaInstanceRequest,
    ) -> arms20190808_models.BindPrometheusGrafanaInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.bind_prometheus_grafana_instance_with_options_async(request, runtime)

    def block_alarm_notification_with_options(
        self,
        request: arms20190808_models.BlockAlarmNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.BlockAlarmNotificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BlockAlarmNotification',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.BlockAlarmNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    async def block_alarm_notification_with_options_async(
        self,
        request: arms20190808_models.BlockAlarmNotificationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.BlockAlarmNotificationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BlockAlarmNotification',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.BlockAlarmNotificationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def block_alarm_notification(
        self,
        request: arms20190808_models.BlockAlarmNotificationRequest,
    ) -> arms20190808_models.BlockAlarmNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return self.block_alarm_notification_with_options(request, runtime)

    async def block_alarm_notification_async(
        self,
        request: arms20190808_models.BlockAlarmNotificationRequest,
    ) -> arms20190808_models.BlockAlarmNotificationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.block_alarm_notification_with_options_async(request, runtime)

    def change_alarm_severity_with_options(
        self,
        request: arms20190808_models.ChangeAlarmSeverityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ChangeAlarmSeverityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeAlarmSeverity',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ChangeAlarmSeverityResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_alarm_severity_with_options_async(
        self,
        request: arms20190808_models.ChangeAlarmSeverityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ChangeAlarmSeverityResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeAlarmSeverity',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ChangeAlarmSeverityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_alarm_severity(
        self,
        request: arms20190808_models.ChangeAlarmSeverityRequest,
    ) -> arms20190808_models.ChangeAlarmSeverityResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_alarm_severity_with_options(request, runtime)

    async def change_alarm_severity_async(
        self,
        request: arms20190808_models.ChangeAlarmSeverityRequest,
    ) -> arms20190808_models.ChangeAlarmSeverityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_alarm_severity_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: arms20190808_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ChangeResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: arms20190808_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ChangeResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: arms20190808_models.ChangeResourceGroupRequest,
    ) -> arms20190808_models.ChangeResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: arms20190808_models.ChangeResourceGroupRequest,
    ) -> arms20190808_models.ChangeResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def check_commercial_status_with_options(
        self,
        request: arms20190808_models.CheckCommercialStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CheckCommercialStatusResponse:
        """
        You can call this operation to check whether ARMS is available for commercial use in a region.
        
        @param request: CheckCommercialStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCommercialStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCommercialStatus',
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
            arms20190808_models.CheckCommercialStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_commercial_status_with_options_async(
        self,
        request: arms20190808_models.CheckCommercialStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CheckCommercialStatusResponse:
        """
        You can call this operation to check whether ARMS is available for commercial use in a region.
        
        @param request: CheckCommercialStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckCommercialStatusResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCommercialStatus',
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
            arms20190808_models.CheckCommercialStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_commercial_status(
        self,
        request: arms20190808_models.CheckCommercialStatusRequest,
    ) -> arms20190808_models.CheckCommercialStatusResponse:
        """
        You can call this operation to check whether ARMS is available for commercial use in a region.
        
        @param request: CheckCommercialStatusRequest
        @return: CheckCommercialStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_commercial_status_with_options(request, runtime)

    async def check_commercial_status_async(
        self,
        request: arms20190808_models.CheckCommercialStatusRequest,
    ) -> arms20190808_models.CheckCommercialStatusResponse:
        """
        You can call this operation to check whether ARMS is available for commercial use in a region.
        
        @param request: CheckCommercialStatusRequest
        @return: CheckCommercialStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_commercial_status_with_options_async(request, runtime)

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

    def claim_alarm_with_options(
        self,
        request: arms20190808_models.ClaimAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ClaimAlarmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClaimAlarm',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ClaimAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def claim_alarm_with_options_async(
        self,
        request: arms20190808_models.ClaimAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ClaimAlarmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClaimAlarm',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ClaimAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def claim_alarm(
        self,
        request: arms20190808_models.ClaimAlarmRequest,
    ) -> arms20190808_models.ClaimAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return self.claim_alarm_with_options(request, runtime)

    async def claim_alarm_async(
        self,
        request: arms20190808_models.ClaimAlarmRequest,
    ) -> arms20190808_models.ClaimAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.claim_alarm_with_options_async(request, runtime)

    def close_alarm_with_options(
        self,
        request: arms20190808_models.CloseAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CloseAlarmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.solution):
            query['Solution'] = request.solution
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseAlarm',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CloseAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    async def close_alarm_with_options_async(
        self,
        request: arms20190808_models.CloseAlarmRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CloseAlarmResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.handler_id):
            query['HandlerId'] = request.handler_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.solution):
            query['Solution'] = request.solution
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseAlarm',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CloseAlarmResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def close_alarm(
        self,
        request: arms20190808_models.CloseAlarmRequest,
    ) -> arms20190808_models.CloseAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return self.close_alarm_with_options(request, runtime)

    async def close_alarm_async(
        self,
        request: arms20190808_models.CloseAlarmRequest,
    ) -> arms20190808_models.CloseAlarmResponse:
        runtime = util_models.RuntimeOptions()
        return await self.close_alarm_with_options_async(request, runtime)

    def config_app_with_options(
        self,
        request: arms20190808_models.ConfigAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ConfigAppResponse:
        """
        ***\
        
        @param request: ConfigAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
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
        """
        ***\
        
        @param request: ConfigAppRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
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
        """
        ***\
        
        @param request: ConfigAppRequest
        @return: ConfigAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_app_with_options(request, runtime)

    async def config_app_async(
        self,
        request: arms20190808_models.ConfigAppRequest,
    ) -> arms20190808_models.ConfigAppResponse:
        """
        ***\
        
        @param request: ConfigAppRequest
        @return: ConfigAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.config_app_with_options_async(request, runtime)

    def create_alert_contact_with_options(
        self,
        request: arms20190808_models.CreateAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateAlertContactResponse:
        """
        This operation is no longer maintained. To create or modify an alert contact, call the CreateOrUpdateContact operation provided by the new version of the Alert Management module.
        
        @param request: CreateAlertContactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAlertContactResponse
        """
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
        """
        This operation is no longer maintained. To create or modify an alert contact, call the CreateOrUpdateContact operation provided by the new version of the Alert Management module.
        
        @param request: CreateAlertContactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAlertContactResponse
        """
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
        """
        This operation is no longer maintained. To create or modify an alert contact, call the CreateOrUpdateContact operation provided by the new version of the Alert Management module.
        
        @param request: CreateAlertContactRequest
        @return: CreateAlertContactResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_alert_contact_with_options(request, runtime)

    async def create_alert_contact_async(
        self,
        request: arms20190808_models.CreateAlertContactRequest,
    ) -> arms20190808_models.CreateAlertContactResponse:
        """
        This operation is no longer maintained. To create or modify an alert contact, call the CreateOrUpdateContact operation provided by the new version of the Alert Management module.
        
        @param request: CreateAlertContactRequest
        @return: CreateAlertContactResponse
        """
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

    def create_env_custom_job_with_options(
        self,
        request: arms20190808_models.CreateEnvCustomJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateEnvCustomJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.custom_job_name):
            query['CustomJobName'] = request.custom_job_name
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEnvCustomJob',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateEnvCustomJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_env_custom_job_with_options_async(
        self,
        request: arms20190808_models.CreateEnvCustomJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateEnvCustomJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.custom_job_name):
            query['CustomJobName'] = request.custom_job_name
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEnvCustomJob',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateEnvCustomJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_env_custom_job(
        self,
        request: arms20190808_models.CreateEnvCustomJobRequest,
    ) -> arms20190808_models.CreateEnvCustomJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_env_custom_job_with_options(request, runtime)

    async def create_env_custom_job_async(
        self,
        request: arms20190808_models.CreateEnvCustomJobRequest,
    ) -> arms20190808_models.CreateEnvCustomJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_env_custom_job_with_options_async(request, runtime)

    def create_env_pod_monitor_with_options(
        self,
        request: arms20190808_models.CreateEnvPodMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateEnvPodMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEnvPodMonitor',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateEnvPodMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_env_pod_monitor_with_options_async(
        self,
        request: arms20190808_models.CreateEnvPodMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateEnvPodMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEnvPodMonitor',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateEnvPodMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_env_pod_monitor(
        self,
        request: arms20190808_models.CreateEnvPodMonitorRequest,
    ) -> arms20190808_models.CreateEnvPodMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_env_pod_monitor_with_options(request, runtime)

    async def create_env_pod_monitor_async(
        self,
        request: arms20190808_models.CreateEnvPodMonitorRequest,
    ) -> arms20190808_models.CreateEnvPodMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_env_pod_monitor_with_options_async(request, runtime)

    def create_env_service_monitor_with_options(
        self,
        request: arms20190808_models.CreateEnvServiceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateEnvServiceMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEnvServiceMonitor',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateEnvServiceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_env_service_monitor_with_options_async(
        self,
        request: arms20190808_models.CreateEnvServiceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateEnvServiceMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEnvServiceMonitor',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateEnvServiceMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_env_service_monitor(
        self,
        request: arms20190808_models.CreateEnvServiceMonitorRequest,
    ) -> arms20190808_models.CreateEnvServiceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_env_service_monitor_with_options(request, runtime)

    async def create_env_service_monitor_async(
        self,
        request: arms20190808_models.CreateEnvServiceMonitorRequest,
    ) -> arms20190808_models.CreateEnvServiceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_env_service_monitor_with_options_async(request, runtime)

    def create_environment_with_options(
        self,
        request: arms20190808_models.CreateEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.bind_resource_id):
            query['BindResourceId'] = request.bind_resource_id
        if not UtilClient.is_unset(request.environment_name):
            query['EnvironmentName'] = request.environment_name
        if not UtilClient.is_unset(request.environment_sub_type):
            query['EnvironmentSubType'] = request.environment_sub_type
        if not UtilClient.is_unset(request.environment_type):
            query['EnvironmentType'] = request.environment_type
        if not UtilClient.is_unset(request.managed_type):
            query['ManagedType'] = request.managed_type
        if not UtilClient.is_unset(request.prometheus_instance_id):
            query['PrometheusInstanceId'] = request.prometheus_instance_id
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
            action='CreateEnvironment',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_environment_with_options_async(
        self,
        request: arms20190808_models.CreateEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.bind_resource_id):
            query['BindResourceId'] = request.bind_resource_id
        if not UtilClient.is_unset(request.environment_name):
            query['EnvironmentName'] = request.environment_name
        if not UtilClient.is_unset(request.environment_sub_type):
            query['EnvironmentSubType'] = request.environment_sub_type
        if not UtilClient.is_unset(request.environment_type):
            query['EnvironmentType'] = request.environment_type
        if not UtilClient.is_unset(request.managed_type):
            query['ManagedType'] = request.managed_type
        if not UtilClient.is_unset(request.prometheus_instance_id):
            query['PrometheusInstanceId'] = request.prometheus_instance_id
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
            action='CreateEnvironment',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_environment(
        self,
        request: arms20190808_models.CreateEnvironmentRequest,
    ) -> arms20190808_models.CreateEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_environment_with_options(request, runtime)

    async def create_environment_async(
        self,
        request: arms20190808_models.CreateEnvironmentRequest,
    ) -> arms20190808_models.CreateEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_environment_with_options_async(request, runtime)

    def create_grafana_workspace_with_options(
        self,
        tmp_req: arms20190808_models.CreateGrafanaWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateGrafanaWorkspaceResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.CreateGrafanaWorkspaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.grafana_version):
            query['GrafanaVersion'] = request.grafana_version
        if not UtilClient.is_unset(request.grafana_workspace_edition):
            query['GrafanaWorkspaceEdition'] = request.grafana_workspace_edition
        if not UtilClient.is_unset(request.grafana_workspace_name):
            query['GrafanaWorkspaceName'] = request.grafana_workspace_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGrafanaWorkspace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateGrafanaWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_grafana_workspace_with_options_async(
        self,
        tmp_req: arms20190808_models.CreateGrafanaWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateGrafanaWorkspaceResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.CreateGrafanaWorkspaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.grafana_version):
            query['GrafanaVersion'] = request.grafana_version
        if not UtilClient.is_unset(request.grafana_workspace_edition):
            query['GrafanaWorkspaceEdition'] = request.grafana_workspace_edition
        if not UtilClient.is_unset(request.grafana_workspace_name):
            query['GrafanaWorkspaceName'] = request.grafana_workspace_name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGrafanaWorkspace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateGrafanaWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_grafana_workspace(
        self,
        request: arms20190808_models.CreateGrafanaWorkspaceRequest,
    ) -> arms20190808_models.CreateGrafanaWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_grafana_workspace_with_options(request, runtime)

    async def create_grafana_workspace_async(
        self,
        request: arms20190808_models.CreateGrafanaWorkspaceRequest,
    ) -> arms20190808_models.CreateGrafanaWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_grafana_workspace_with_options_async(request, runtime)

    def create_integration_with_options(
        self,
        request: arms20190808_models.CreateIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auto_recover):
            body['AutoRecover'] = request.auto_recover
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.integration_name):
            body['IntegrationName'] = request.integration_name
        if not UtilClient.is_unset(request.integration_product_type):
            body['IntegrationProductType'] = request.integration_product_type
        if not UtilClient.is_unset(request.recover_time):
            body['RecoverTime'] = request.recover_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_integration_with_options_async(
        self,
        request: arms20190808_models.CreateIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.auto_recover):
            body['AutoRecover'] = request.auto_recover
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.integration_name):
            body['IntegrationName'] = request.integration_name
        if not UtilClient.is_unset(request.integration_product_type):
            body['IntegrationProductType'] = request.integration_product_type
        if not UtilClient.is_unset(request.recover_time):
            body['RecoverTime'] = request.recover_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_integration(
        self,
        request: arms20190808_models.CreateIntegrationRequest,
    ) -> arms20190808_models.CreateIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_integration_with_options(request, runtime)

    async def create_integration_async(
        self,
        request: arms20190808_models.CreateIntegrationRequest,
    ) -> arms20190808_models.CreateIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_integration_with_options_async(request, runtime)

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
        if not UtilClient.is_unset(request.alert_piplines):
            body['AlertPiplines'] = request.alert_piplines
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
        if not UtilClient.is_unset(request.data_config):
            body['DataConfig'] = request.data_config
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.filters):
            body['Filters'] = request.filters
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.mark_tags):
            body['MarkTags'] = request.mark_tags
        if not UtilClient.is_unset(request.message):
            body['Message'] = request.message
        if not UtilClient.is_unset(request.metrics_key):
            body['MetricsKey'] = request.metrics_key
        if not UtilClient.is_unset(request.metrics_type):
            body['MetricsType'] = request.metrics_type
        if not UtilClient.is_unset(request.notice):
            body['Notice'] = request.notice
        if not UtilClient.is_unset(request.notify_mode):
            body['NotifyMode'] = request.notify_mode
        if not UtilClient.is_unset(request.notify_strategy):
            body['NotifyStrategy'] = request.notify_strategy
        if not UtilClient.is_unset(request.pids):
            body['Pids'] = request.pids
        if not UtilClient.is_unset(request.prom_ql):
            body['PromQL'] = request.prom_ql
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
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
        if not UtilClient.is_unset(request.alert_piplines):
            body['AlertPiplines'] = request.alert_piplines
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
        if not UtilClient.is_unset(request.data_config):
            body['DataConfig'] = request.data_config
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.filters):
            body['Filters'] = request.filters
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.mark_tags):
            body['MarkTags'] = request.mark_tags
        if not UtilClient.is_unset(request.message):
            body['Message'] = request.message
        if not UtilClient.is_unset(request.metrics_key):
            body['MetricsKey'] = request.metrics_key
        if not UtilClient.is_unset(request.metrics_type):
            body['MetricsType'] = request.metrics_type
        if not UtilClient.is_unset(request.notice):
            body['Notice'] = request.notice
        if not UtilClient.is_unset(request.notify_mode):
            body['NotifyMode'] = request.notify_mode
        if not UtilClient.is_unset(request.notify_strategy):
            body['NotifyStrategy'] = request.notify_strategy
        if not UtilClient.is_unset(request.pids):
            body['Pids'] = request.pids
        if not UtilClient.is_unset(request.prom_ql):
            body['PromQL'] = request.prom_ql
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
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
        query = {}
        if not UtilClient.is_unset(request.ding_robot_url):
            query['DingRobotUrl'] = request.ding_robot_url
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not UtilClient.is_unset(request.contact_id):
            body['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_name):
            body['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.is_email_verify):
            body['IsEmailVerify'] = request.is_email_verify
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.reissue_send_notice):
            body['ReissueSendNotice'] = request.reissue_send_notice
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        query = {}
        if not UtilClient.is_unset(request.ding_robot_url):
            query['DingRobotUrl'] = request.ding_robot_url
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not UtilClient.is_unset(request.contact_id):
            body['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_name):
            body['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.is_email_verify):
            body['IsEmailVerify'] = request.is_email_verify
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.reissue_send_notice):
            body['ReissueSendNotice'] = request.reissue_send_notice
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        if not UtilClient.is_unset(request.card_template):
            body['CardTemplate'] = request.card_template
        if not UtilClient.is_unset(request.daily_noc):
            body['DailyNoc'] = request.daily_noc
        if not UtilClient.is_unset(request.daily_noc_time):
            body['DailyNocTime'] = request.daily_noc_time
        if not UtilClient.is_unset(request.ding_sign_key):
            body['DingSignKey'] = request.ding_sign_key
        if not UtilClient.is_unset(request.enable_outgoing):
            body['EnableOutgoing'] = request.enable_outgoing
        if not UtilClient.is_unset(request.robot_address):
            body['RobotAddress'] = request.robot_address
        if not UtilClient.is_unset(request.robot_id):
            body['RobotId'] = request.robot_id
        if not UtilClient.is_unset(request.robot_name):
            body['RobotName'] = request.robot_name
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
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
        if not UtilClient.is_unset(request.card_template):
            body['CardTemplate'] = request.card_template
        if not UtilClient.is_unset(request.daily_noc):
            body['DailyNoc'] = request.daily_noc
        if not UtilClient.is_unset(request.daily_noc_time):
            body['DailyNocTime'] = request.daily_noc_time
        if not UtilClient.is_unset(request.ding_sign_key):
            body['DingSignKey'] = request.ding_sign_key
        if not UtilClient.is_unset(request.enable_outgoing):
            body['EnableOutgoing'] = request.enable_outgoing
        if not UtilClient.is_unset(request.robot_address):
            body['RobotAddress'] = request.robot_address
        if not UtilClient.is_unset(request.robot_id):
            body['RobotId'] = request.robot_id
        if not UtilClient.is_unset(request.robot_name):
            body['RobotName'] = request.robot_name
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
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
        if not UtilClient.is_unset(request.directed_mode):
            body['DirectedMode'] = request.directed_mode
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
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
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
        if not UtilClient.is_unset(request.directed_mode):
            body['DirectedMode'] = request.directed_mode
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
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
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
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
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
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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

    def create_prometheus_instance_with_options(
        self,
        request: arms20190808_models.CreatePrometheusInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreatePrometheusInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_sub_clusters_success):
            query['AllSubClustersSuccess'] = request.all_sub_clusters_success
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.grafana_instance_id):
            query['GrafanaInstanceId'] = request.grafana_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.sub_clusters_json):
            query['SubClustersJson'] = request.sub_clusters_json
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePrometheusInstance',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreatePrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prometheus_instance_with_options_async(
        self,
        request: arms20190808_models.CreatePrometheusInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreatePrometheusInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_sub_clusters_success):
            query['AllSubClustersSuccess'] = request.all_sub_clusters_success
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.grafana_instance_id):
            query['GrafanaInstanceId'] = request.grafana_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.sub_clusters_json):
            query['SubClustersJson'] = request.sub_clusters_json
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePrometheusInstance',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreatePrometheusInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prometheus_instance(
        self,
        request: arms20190808_models.CreatePrometheusInstanceRequest,
    ) -> arms20190808_models.CreatePrometheusInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_prometheus_instance_with_options(request, runtime)

    async def create_prometheus_instance_async(
        self,
        request: arms20190808_models.CreatePrometheusInstanceRequest,
    ) -> arms20190808_models.CreatePrometheusInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_prometheus_instance_with_options_async(request, runtime)

    def create_prometheus_monitoring_with_options(
        self,
        request: arms20190808_models.CreatePrometheusMonitoringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreatePrometheusMonitoringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrometheusMonitoring',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreatePrometheusMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_prometheus_monitoring_with_options_async(
        self,
        request: arms20190808_models.CreatePrometheusMonitoringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreatePrometheusMonitoringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrometheusMonitoring',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreatePrometheusMonitoringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_prometheus_monitoring(
        self,
        request: arms20190808_models.CreatePrometheusMonitoringRequest,
    ) -> arms20190808_models.CreatePrometheusMonitoringResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_prometheus_monitoring_with_options(request, runtime)

    async def create_prometheus_monitoring_async(
        self,
        request: arms20190808_models.CreatePrometheusMonitoringRequest,
    ) -> arms20190808_models.CreatePrometheusMonitoringResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_prometheus_monitoring_with_options_async(request, runtime)

    def create_retcode_app_with_options(
        self,
        request: arms20190808_models.CreateRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateRetcodeAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        if not UtilClient.is_unset(request.retcode_app_type):
            query['RetcodeAppType'] = request.retcode_app_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        if not UtilClient.is_unset(request.retcode_app_type):
            query['RetcodeAppType'] = request.retcode_app_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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

    def create_synthetic_task_with_options(
        self,
        tmp_req: arms20190808_models.CreateSyntheticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateSyntheticTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.CreateSyntheticTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.common_param):
            request.common_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.common_param, 'CommonParam', 'json')
        if not UtilClient.is_unset(tmp_req.download):
            request.download_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.download, 'Download', 'json')
        if not UtilClient.is_unset(tmp_req.extend_interval):
            request.extend_interval_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_interval, 'ExtendInterval', 'json')
        if not UtilClient.is_unset(tmp_req.monitor_list):
            request.monitor_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.monitor_list, 'MonitorList', 'json')
        if not UtilClient.is_unset(tmp_req.navigation):
            request.navigation_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.navigation, 'Navigation', 'json')
        if not UtilClient.is_unset(tmp_req.net):
            request.net_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.net, 'Net', 'json')
        if not UtilClient.is_unset(tmp_req.protocol):
            request.protocol_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.protocol, 'Protocol', 'json')
        query = {}
        if not UtilClient.is_unset(request.common_param_shrink):
            query['CommonParam'] = request.common_param_shrink
        if not UtilClient.is_unset(request.download_shrink):
            query['Download'] = request.download_shrink
        if not UtilClient.is_unset(request.extend_interval_shrink):
            query['ExtendInterval'] = request.extend_interval_shrink
        if not UtilClient.is_unset(request.interval_time):
            query['IntervalTime'] = request.interval_time
        if not UtilClient.is_unset(request.interval_type):
            query['IntervalType'] = request.interval_type
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.monitor_list_shrink):
            query['MonitorList'] = request.monitor_list_shrink
        if not UtilClient.is_unset(request.navigation_shrink):
            query['Navigation'] = request.navigation_shrink
        if not UtilClient.is_unset(request.net_shrink):
            query['Net'] = request.net_shrink
        if not UtilClient.is_unset(request.protocol_shrink):
            query['Protocol'] = request.protocol_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.update_task):
            query['UpdateTask'] = request.update_task
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSyntheticTask',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_synthetic_task_with_options_async(
        self,
        tmp_req: arms20190808_models.CreateSyntheticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateSyntheticTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.CreateSyntheticTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.common_param):
            request.common_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.common_param, 'CommonParam', 'json')
        if not UtilClient.is_unset(tmp_req.download):
            request.download_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.download, 'Download', 'json')
        if not UtilClient.is_unset(tmp_req.extend_interval):
            request.extend_interval_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_interval, 'ExtendInterval', 'json')
        if not UtilClient.is_unset(tmp_req.monitor_list):
            request.monitor_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.monitor_list, 'MonitorList', 'json')
        if not UtilClient.is_unset(tmp_req.navigation):
            request.navigation_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.navigation, 'Navigation', 'json')
        if not UtilClient.is_unset(tmp_req.net):
            request.net_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.net, 'Net', 'json')
        if not UtilClient.is_unset(tmp_req.protocol):
            request.protocol_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.protocol, 'Protocol', 'json')
        query = {}
        if not UtilClient.is_unset(request.common_param_shrink):
            query['CommonParam'] = request.common_param_shrink
        if not UtilClient.is_unset(request.download_shrink):
            query['Download'] = request.download_shrink
        if not UtilClient.is_unset(request.extend_interval_shrink):
            query['ExtendInterval'] = request.extend_interval_shrink
        if not UtilClient.is_unset(request.interval_time):
            query['IntervalTime'] = request.interval_time
        if not UtilClient.is_unset(request.interval_type):
            query['IntervalType'] = request.interval_type
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.monitor_list_shrink):
            query['MonitorList'] = request.monitor_list_shrink
        if not UtilClient.is_unset(request.navigation_shrink):
            query['Navigation'] = request.navigation_shrink
        if not UtilClient.is_unset(request.net_shrink):
            query['Net'] = request.net_shrink
        if not UtilClient.is_unset(request.protocol_shrink):
            query['Protocol'] = request.protocol_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.update_task):
            query['UpdateTask'] = request.update_task
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSyntheticTask',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateSyntheticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_synthetic_task(
        self,
        request: arms20190808_models.CreateSyntheticTaskRequest,
    ) -> arms20190808_models.CreateSyntheticTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_synthetic_task_with_options(request, runtime)

    async def create_synthetic_task_async(
        self,
        request: arms20190808_models.CreateSyntheticTaskRequest,
    ) -> arms20190808_models.CreateSyntheticTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_synthetic_task_with_options_async(request, runtime)

    def create_timing_synthetic_task_with_options(
        self,
        tmp_req: arms20190808_models.CreateTimingSyntheticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateTimingSyntheticTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.CreateTimingSyntheticTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.available_assertions):
            request.available_assertions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.available_assertions, 'AvailableAssertions', 'json')
        if not UtilClient.is_unset(tmp_req.common_setting):
            request.common_setting_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.common_setting, 'CommonSetting', 'json')
        if not UtilClient.is_unset(tmp_req.custom_period):
            request.custom_period_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_period, 'CustomPeriod', 'json')
        if not UtilClient.is_unset(tmp_req.monitor_conf):
            request.monitor_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.monitor_conf, 'MonitorConf', 'json')
        if not UtilClient.is_unset(tmp_req.monitors):
            request.monitors_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.monitors, 'Monitors', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.available_assertions_shrink):
            query['AvailableAssertions'] = request.available_assertions_shrink
        if not UtilClient.is_unset(request.common_setting_shrink):
            query['CommonSetting'] = request.common_setting_shrink
        if not UtilClient.is_unset(request.custom_period_shrink):
            query['CustomPeriod'] = request.custom_period_shrink
        if not UtilClient.is_unset(request.frequency):
            query['Frequency'] = request.frequency
        if not UtilClient.is_unset(request.monitor_category):
            query['MonitorCategory'] = request.monitor_category
        if not UtilClient.is_unset(request.monitor_conf_shrink):
            query['MonitorConf'] = request.monitor_conf_shrink
        if not UtilClient.is_unset(request.monitors_shrink):
            query['Monitors'] = request.monitors_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTimingSyntheticTask',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateTimingSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_timing_synthetic_task_with_options_async(
        self,
        tmp_req: arms20190808_models.CreateTimingSyntheticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.CreateTimingSyntheticTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.CreateTimingSyntheticTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.available_assertions):
            request.available_assertions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.available_assertions, 'AvailableAssertions', 'json')
        if not UtilClient.is_unset(tmp_req.common_setting):
            request.common_setting_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.common_setting, 'CommonSetting', 'json')
        if not UtilClient.is_unset(tmp_req.custom_period):
            request.custom_period_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_period, 'CustomPeriod', 'json')
        if not UtilClient.is_unset(tmp_req.monitor_conf):
            request.monitor_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.monitor_conf, 'MonitorConf', 'json')
        if not UtilClient.is_unset(tmp_req.monitors):
            request.monitors_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.monitors, 'Monitors', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.available_assertions_shrink):
            query['AvailableAssertions'] = request.available_assertions_shrink
        if not UtilClient.is_unset(request.common_setting_shrink):
            query['CommonSetting'] = request.common_setting_shrink
        if not UtilClient.is_unset(request.custom_period_shrink):
            query['CustomPeriod'] = request.custom_period_shrink
        if not UtilClient.is_unset(request.frequency):
            query['Frequency'] = request.frequency
        if not UtilClient.is_unset(request.monitor_category):
            query['MonitorCategory'] = request.monitor_category
        if not UtilClient.is_unset(request.monitor_conf_shrink):
            query['MonitorConf'] = request.monitor_conf_shrink
        if not UtilClient.is_unset(request.monitors_shrink):
            query['Monitors'] = request.monitors_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTimingSyntheticTask',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateTimingSyntheticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_timing_synthetic_task(
        self,
        request: arms20190808_models.CreateTimingSyntheticTaskRequest,
    ) -> arms20190808_models.CreateTimingSyntheticTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_timing_synthetic_task_with_options(request, runtime)

    async def create_timing_synthetic_task_async(
        self,
        request: arms20190808_models.CreateTimingSyntheticTaskRequest,
    ) -> arms20190808_models.CreateTimingSyntheticTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_timing_synthetic_task_with_options_async(request, runtime)

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

    def del_auth_token_with_options(
        self,
        request: arms20190808_models.DelAuthTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DelAuthTokenResponse:
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
            action='DelAuthToken',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DelAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def del_auth_token_with_options_async(
        self,
        request: arms20190808_models.DelAuthTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DelAuthTokenResponse:
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
            action='DelAuthToken',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DelAuthTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def del_auth_token(
        self,
        request: arms20190808_models.DelAuthTokenRequest,
    ) -> arms20190808_models.DelAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.del_auth_token_with_options(request, runtime)

    async def del_auth_token_async(
        self,
        request: arms20190808_models.DelAuthTokenRequest,
    ) -> arms20190808_models.DelAuthTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.del_auth_token_with_options_async(request, runtime)

    def delete_addon_release_with_options(
        self,
        request: arms20190808_models.DeleteAddonReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAddonReleaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.release_name):
            query['ReleaseName'] = request.release_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAddonRelease',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteAddonReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_addon_release_with_options_async(
        self,
        request: arms20190808_models.DeleteAddonReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAddonReleaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.release_name):
            query['ReleaseName'] = request.release_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAddonRelease',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteAddonReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_addon_release(
        self,
        request: arms20190808_models.DeleteAddonReleaseRequest,
    ) -> arms20190808_models.DeleteAddonReleaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_addon_release_with_options(request, runtime)

    async def delete_addon_release_async(
        self,
        request: arms20190808_models.DeleteAddonReleaseRequest,
    ) -> arms20190808_models.DeleteAddonReleaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_addon_release_with_options_async(request, runtime)

    def delete_alert_contact_with_options(
        self,
        request: arms20190808_models.DeleteAlertContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAlertContactResponse:
        """
        *******\
        
        @param request: DeleteAlertContactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAlertContactResponse
        """
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
        """
        *******\
        
        @param request: DeleteAlertContactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAlertContactResponse
        """
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
        """
        *******\
        
        @param request: DeleteAlertContactRequest
        @return: DeleteAlertContactResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_with_options(request, runtime)

    async def delete_alert_contact_async(
        self,
        request: arms20190808_models.DeleteAlertContactRequest,
    ) -> arms20190808_models.DeleteAlertContactResponse:
        """
        *******\
        
        @param request: DeleteAlertContactRequest
        @return: DeleteAlertContactResponse
        """
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

    def delete_app_list_with_options(
        self,
        request: arms20190808_models.DeleteAppListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAppListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pids):
            query['Pids'] = request.pids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppList',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteAppListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_app_list_with_options_async(
        self,
        request: arms20190808_models.DeleteAppListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteAppListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pids):
            query['Pids'] = request.pids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppList',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteAppListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_app_list(
        self,
        request: arms20190808_models.DeleteAppListRequest,
    ) -> arms20190808_models.DeleteAppListResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_app_list_with_options(request, runtime)

    async def delete_app_list_async(
        self,
        request: arms20190808_models.DeleteAppListRequest,
    ) -> arms20190808_models.DeleteAppListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_app_list_with_options_async(request, runtime)

    def delete_cms_exporter_with_options(
        self,
        request: arms20190808_models.DeleteCmsExporterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteCmsExporterResponse:
        """
        @deprecated : DeleteCmsExporter is deprecated, please use ARMS::2019-08-08::DeleteAddonRelease instead.
        
        @param request: DeleteCmsExporterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCmsExporterResponse
        Deprecated
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
        """
        @deprecated : DeleteCmsExporter is deprecated, please use ARMS::2019-08-08::DeleteAddonRelease instead.
        
        @param request: DeleteCmsExporterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteCmsExporterResponse
        Deprecated
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
        """
        @deprecated : DeleteCmsExporter is deprecated, please use ARMS::2019-08-08::DeleteAddonRelease instead.
        
        @param request: DeleteCmsExporterRequest
        @return: DeleteCmsExporterResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cms_exporter_with_options(request, runtime)

    async def delete_cms_exporter_async(
        self,
        request: arms20190808_models.DeleteCmsExporterRequest,
    ) -> arms20190808_models.DeleteCmsExporterResponse:
        """
        @deprecated : DeleteCmsExporter is deprecated, please use ARMS::2019-08-08::DeleteAddonRelease instead.
        
        @param request: DeleteCmsExporterRequest
        @return: DeleteCmsExporterResponse
        Deprecated
        """
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

    def delete_env_custom_job_with_options(
        self,
        request: arms20190808_models.DeleteEnvCustomJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteEnvCustomJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_job_name):
            query['CustomJobName'] = request.custom_job_name
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnvCustomJob',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteEnvCustomJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_env_custom_job_with_options_async(
        self,
        request: arms20190808_models.DeleteEnvCustomJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteEnvCustomJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_job_name):
            query['CustomJobName'] = request.custom_job_name
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnvCustomJob',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteEnvCustomJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_env_custom_job(
        self,
        request: arms20190808_models.DeleteEnvCustomJobRequest,
    ) -> arms20190808_models.DeleteEnvCustomJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_env_custom_job_with_options(request, runtime)

    async def delete_env_custom_job_async(
        self,
        request: arms20190808_models.DeleteEnvCustomJobRequest,
    ) -> arms20190808_models.DeleteEnvCustomJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_env_custom_job_with_options_async(request, runtime)

    def delete_env_pod_monitor_with_options(
        self,
        request: arms20190808_models.DeleteEnvPodMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteEnvPodMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.pod_monitor_name):
            query['PodMonitorName'] = request.pod_monitor_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnvPodMonitor',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteEnvPodMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_env_pod_monitor_with_options_async(
        self,
        request: arms20190808_models.DeleteEnvPodMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteEnvPodMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.pod_monitor_name):
            query['PodMonitorName'] = request.pod_monitor_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnvPodMonitor',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteEnvPodMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_env_pod_monitor(
        self,
        request: arms20190808_models.DeleteEnvPodMonitorRequest,
    ) -> arms20190808_models.DeleteEnvPodMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_env_pod_monitor_with_options(request, runtime)

    async def delete_env_pod_monitor_async(
        self,
        request: arms20190808_models.DeleteEnvPodMonitorRequest,
    ) -> arms20190808_models.DeleteEnvPodMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_env_pod_monitor_with_options_async(request, runtime)

    def delete_env_service_monitor_with_options(
        self,
        request: arms20190808_models.DeleteEnvServiceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteEnvServiceMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_monitor_name):
            query['ServiceMonitorName'] = request.service_monitor_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnvServiceMonitor',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteEnvServiceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_env_service_monitor_with_options_async(
        self,
        request: arms20190808_models.DeleteEnvServiceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteEnvServiceMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_monitor_name):
            query['ServiceMonitorName'] = request.service_monitor_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnvServiceMonitor',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteEnvServiceMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_env_service_monitor(
        self,
        request: arms20190808_models.DeleteEnvServiceMonitorRequest,
    ) -> arms20190808_models.DeleteEnvServiceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_env_service_monitor_with_options(request, runtime)

    async def delete_env_service_monitor_async(
        self,
        request: arms20190808_models.DeleteEnvServiceMonitorRequest,
    ) -> arms20190808_models.DeleteEnvServiceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_env_service_monitor_with_options_async(request, runtime)

    def delete_environment_with_options(
        self,
        request: arms20190808_models.DeleteEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_prom_instance):
            query['DeletePromInstance'] = request.delete_prom_instance
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnvironment',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_environment_with_options_async(
        self,
        request: arms20190808_models.DeleteEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_prom_instance):
            query['DeletePromInstance'] = request.delete_prom_instance
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnvironment',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_environment(
        self,
        request: arms20190808_models.DeleteEnvironmentRequest,
    ) -> arms20190808_models.DeleteEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_environment_with_options(request, runtime)

    async def delete_environment_async(
        self,
        request: arms20190808_models.DeleteEnvironmentRequest,
    ) -> arms20190808_models.DeleteEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_environment_with_options_async(request, runtime)

    def delete_environment_feature_with_options(
        self,
        request: arms20190808_models.DeleteEnvironmentFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteEnvironmentFeatureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnvironmentFeature',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteEnvironmentFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_environment_feature_with_options_async(
        self,
        request: arms20190808_models.DeleteEnvironmentFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteEnvironmentFeatureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEnvironmentFeature',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteEnvironmentFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_environment_feature(
        self,
        request: arms20190808_models.DeleteEnvironmentFeatureRequest,
    ) -> arms20190808_models.DeleteEnvironmentFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_environment_feature_with_options(request, runtime)

    async def delete_environment_feature_async(
        self,
        request: arms20190808_models.DeleteEnvironmentFeatureRequest,
    ) -> arms20190808_models.DeleteEnvironmentFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_environment_feature_with_options_async(request, runtime)

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

    def delete_grafana_resource_with_options(
        self,
        request: arms20190808_models.DeleteGrafanaResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteGrafanaResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGrafanaResource',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteGrafanaResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_grafana_resource_with_options_async(
        self,
        request: arms20190808_models.DeleteGrafanaResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteGrafanaResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGrafanaResource',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteGrafanaResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_grafana_resource(
        self,
        request: arms20190808_models.DeleteGrafanaResourceRequest,
    ) -> arms20190808_models.DeleteGrafanaResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_grafana_resource_with_options(request, runtime)

    async def delete_grafana_resource_async(
        self,
        request: arms20190808_models.DeleteGrafanaResourceRequest,
    ) -> arms20190808_models.DeleteGrafanaResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_grafana_resource_with_options_async(request, runtime)

    def delete_grafana_workspace_with_options(
        self,
        request: arms20190808_models.DeleteGrafanaWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteGrafanaWorkspaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGrafanaWorkspace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteGrafanaWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_grafana_workspace_with_options_async(
        self,
        request: arms20190808_models.DeleteGrafanaWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteGrafanaWorkspaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGrafanaWorkspace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteGrafanaWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_grafana_workspace(
        self,
        request: arms20190808_models.DeleteGrafanaWorkspaceRequest,
    ) -> arms20190808_models.DeleteGrafanaWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_grafana_workspace_with_options(request, runtime)

    async def delete_grafana_workspace_async(
        self,
        request: arms20190808_models.DeleteGrafanaWorkspaceRequest,
    ) -> arms20190808_models.DeleteGrafanaWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_grafana_workspace_with_options_async(request, runtime)

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
        """
        @deprecated : DeleteIntegration is deprecated, please use ARMS::2019-08-08::DeleteAddonRelease instead.
        
        @param request: DeleteIntegrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIntegrationResponse
        Deprecated
        """
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
        """
        @deprecated : DeleteIntegration is deprecated, please use ARMS::2019-08-08::DeleteAddonRelease instead.
        
        @param request: DeleteIntegrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteIntegrationResponse
        Deprecated
        """
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
        """
        @deprecated : DeleteIntegration is deprecated, please use ARMS::2019-08-08::DeleteAddonRelease instead.
        
        @param request: DeleteIntegrationRequest
        @return: DeleteIntegrationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_integration_with_options(request, runtime)

    async def delete_integration_async(
        self,
        request: arms20190808_models.DeleteIntegrationRequest,
    ) -> arms20190808_models.DeleteIntegrationResponse:
        """
        @deprecated : DeleteIntegration is deprecated, please use ARMS::2019-08-08::DeleteAddonRelease instead.
        
        @param request: DeleteIntegrationRequest
        @return: DeleteIntegrationResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_integration_with_options_async(request, runtime)

    def delete_integrations_with_options(
        self,
        request: arms20190808_models.DeleteIntegrationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteIntegrationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIntegrations',
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
            arms20190808_models.DeleteIntegrationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_integrations_with_options_async(
        self,
        request: arms20190808_models.DeleteIntegrationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteIntegrationsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIntegrations',
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
            arms20190808_models.DeleteIntegrationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_integrations(
        self,
        request: arms20190808_models.DeleteIntegrationsRequest,
    ) -> arms20190808_models.DeleteIntegrationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_integrations_with_options(request, runtime)

    async def delete_integrations_async(
        self,
        request: arms20190808_models.DeleteIntegrationsRequest,
    ) -> arms20190808_models.DeleteIntegrationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_integrations_with_options_async(request, runtime)

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
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
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
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
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

    def delete_prometheus_integration_with_options(
        self,
        request: arms20190808_models.DeletePrometheusIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeletePrometheusIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeletePrometheusIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_prometheus_integration_with_options_async(
        self,
        request: arms20190808_models.DeletePrometheusIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeletePrometheusIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeletePrometheusIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_prometheus_integration(
        self,
        request: arms20190808_models.DeletePrometheusIntegrationRequest,
    ) -> arms20190808_models.DeletePrometheusIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_prometheus_integration_with_options(request, runtime)

    async def delete_prometheus_integration_async(
        self,
        request: arms20190808_models.DeletePrometheusIntegrationRequest,
    ) -> arms20190808_models.DeletePrometheusIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_prometheus_integration_with_options_async(request, runtime)

    def delete_prometheus_monitoring_with_options(
        self,
        request: arms20190808_models.DeletePrometheusMonitoringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeletePrometheusMonitoringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusMonitoring',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeletePrometheusMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_prometheus_monitoring_with_options_async(
        self,
        request: arms20190808_models.DeletePrometheusMonitoringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeletePrometheusMonitoringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusMonitoring',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeletePrometheusMonitoringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_prometheus_monitoring(
        self,
        request: arms20190808_models.DeletePrometheusMonitoringRequest,
    ) -> arms20190808_models.DeletePrometheusMonitoringResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_prometheus_monitoring_with_options(request, runtime)

    async def delete_prometheus_monitoring_async(
        self,
        request: arms20190808_models.DeletePrometheusMonitoringRequest,
    ) -> arms20190808_models.DeletePrometheusMonitoringResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_prometheus_monitoring_with_options_async(request, runtime)

    def delete_prometheus_remote_write_with_options(
        self,
        request: arms20190808_models.DeletePrometheusRemoteWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeletePrometheusRemoteWriteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remote_write_names):
            query['RemoteWriteNames'] = request.remote_write_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusRemoteWrite',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeletePrometheusRemoteWriteResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_prometheus_remote_write_with_options_async(
        self,
        request: arms20190808_models.DeletePrometheusRemoteWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeletePrometheusRemoteWriteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remote_write_names):
            query['RemoteWriteNames'] = request.remote_write_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusRemoteWrite',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeletePrometheusRemoteWriteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_prometheus_remote_write(
        self,
        request: arms20190808_models.DeletePrometheusRemoteWriteRequest,
    ) -> arms20190808_models.DeletePrometheusRemoteWriteResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_prometheus_remote_write_with_options(request, runtime)

    async def delete_prometheus_remote_write_async(
        self,
        request: arms20190808_models.DeletePrometheusRemoteWriteRequest,
    ) -> arms20190808_models.DeletePrometheusRemoteWriteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_prometheus_remote_write_with_options_async(request, runtime)

    def delete_retcode_app_with_options(
        self,
        request: arms20190808_models.DeleteRetcodeAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteRetcodeAppResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
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
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
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

    def delete_source_map_with_options(
        self,
        tmp_req: arms20190808_models.DeleteSourceMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteSourceMapResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.DeleteSourceMapShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.fid_list):
            request.fid_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.fid_list, 'FidList', 'json')
        query = {}
        if not UtilClient.is_unset(request.fid_list_shrink):
            query['FidList'] = request.fid_list_shrink
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSourceMap',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteSourceMapResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_source_map_with_options_async(
        self,
        tmp_req: arms20190808_models.DeleteSourceMapRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteSourceMapResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.DeleteSourceMapShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.fid_list):
            request.fid_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.fid_list, 'FidList', 'json')
        query = {}
        if not UtilClient.is_unset(request.fid_list_shrink):
            query['FidList'] = request.fid_list_shrink
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSourceMap',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteSourceMapResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_source_map(
        self,
        request: arms20190808_models.DeleteSourceMapRequest,
    ) -> arms20190808_models.DeleteSourceMapResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_source_map_with_options(request, runtime)

    async def delete_source_map_async(
        self,
        request: arms20190808_models.DeleteSourceMapRequest,
    ) -> arms20190808_models.DeleteSourceMapResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_source_map_with_options_async(request, runtime)

    def delete_synthetic_task_with_options(
        self,
        request: arms20190808_models.DeleteSyntheticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteSyntheticTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSyntheticTask',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_synthetic_task_with_options_async(
        self,
        request: arms20190808_models.DeleteSyntheticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteSyntheticTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSyntheticTask',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteSyntheticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_synthetic_task(
        self,
        request: arms20190808_models.DeleteSyntheticTaskRequest,
    ) -> arms20190808_models.DeleteSyntheticTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_synthetic_task_with_options(request, runtime)

    async def delete_synthetic_task_async(
        self,
        request: arms20190808_models.DeleteSyntheticTaskRequest,
    ) -> arms20190808_models.DeleteSyntheticTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_synthetic_task_with_options_async(request, runtime)

    def delete_timing_synthetic_task_with_options(
        self,
        request: arms20190808_models.DeleteTimingSyntheticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteTimingSyntheticTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTimingSyntheticTask',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteTimingSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_timing_synthetic_task_with_options_async(
        self,
        request: arms20190808_models.DeleteTimingSyntheticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteTimingSyntheticTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTimingSyntheticTask',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteTimingSyntheticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_timing_synthetic_task(
        self,
        request: arms20190808_models.DeleteTimingSyntheticTaskRequest,
    ) -> arms20190808_models.DeleteTimingSyntheticTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_timing_synthetic_task_with_options(request, runtime)

    async def delete_timing_synthetic_task_async(
        self,
        request: arms20190808_models.DeleteTimingSyntheticTaskRequest,
    ) -> arms20190808_models.DeleteTimingSyntheticTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_timing_synthetic_task_with_options_async(request, runtime)

    def delete_trace_app_with_options(
        self,
        tmp_req: arms20190808_models.DeleteTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteTraceAppResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.DeleteTraceAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_reason):
            request.delete_reason_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.delete_reason, 'DeleteReason', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.delete_reason_shrink):
            query['DeleteReason'] = request.delete_reason_shrink
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
        tmp_req: arms20190808_models.DeleteTraceAppRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DeleteTraceAppResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.DeleteTraceAppShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_reason):
            request.delete_reason_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.delete_reason, 'DeleteReason', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.delete_reason_shrink):
            query['DeleteReason'] = request.delete_reason_shrink
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

    def describe_addon_release_with_options(
        self,
        request: arms20190808_models.DescribeAddonReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeAddonReleaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.release_name):
            query['ReleaseName'] = request.release_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAddonRelease',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeAddonReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_addon_release_with_options_async(
        self,
        request: arms20190808_models.DescribeAddonReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeAddonReleaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.release_name):
            query['ReleaseName'] = request.release_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAddonRelease',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeAddonReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_addon_release(
        self,
        request: arms20190808_models.DescribeAddonReleaseRequest,
    ) -> arms20190808_models.DescribeAddonReleaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_addon_release_with_options(request, runtime)

    async def describe_addon_release_async(
        self,
        request: arms20190808_models.DescribeAddonReleaseRequest,
    ) -> arms20190808_models.DescribeAddonReleaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_addon_release_with_options_async(request, runtime)

    def describe_contact_groups_with_options(
        self,
        request: arms20190808_models.DescribeContactGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeContactGroupsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.is_detail):
            query['IsDetail'] = request.is_detail
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
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.is_detail):
            query['IsDetail'] = request.is_detail
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
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
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
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
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

    def describe_env_custom_job_with_options(
        self,
        request: arms20190808_models.DescribeEnvCustomJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeEnvCustomJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_job_name):
            query['CustomJobName'] = request.custom_job_name
        if not UtilClient.is_unset(request.encrypt_yaml):
            query['EncryptYaml'] = request.encrypt_yaml
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnvCustomJob',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeEnvCustomJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_env_custom_job_with_options_async(
        self,
        request: arms20190808_models.DescribeEnvCustomJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeEnvCustomJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_job_name):
            query['CustomJobName'] = request.custom_job_name
        if not UtilClient.is_unset(request.encrypt_yaml):
            query['EncryptYaml'] = request.encrypt_yaml
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnvCustomJob',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeEnvCustomJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_env_custom_job(
        self,
        request: arms20190808_models.DescribeEnvCustomJobRequest,
    ) -> arms20190808_models.DescribeEnvCustomJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_env_custom_job_with_options(request, runtime)

    async def describe_env_custom_job_async(
        self,
        request: arms20190808_models.DescribeEnvCustomJobRequest,
    ) -> arms20190808_models.DescribeEnvCustomJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_env_custom_job_with_options_async(request, runtime)

    def describe_env_pod_monitor_with_options(
        self,
        request: arms20190808_models.DescribeEnvPodMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeEnvPodMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.pod_monitor_name):
            query['PodMonitorName'] = request.pod_monitor_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnvPodMonitor',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeEnvPodMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_env_pod_monitor_with_options_async(
        self,
        request: arms20190808_models.DescribeEnvPodMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeEnvPodMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.pod_monitor_name):
            query['PodMonitorName'] = request.pod_monitor_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnvPodMonitor',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeEnvPodMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_env_pod_monitor(
        self,
        request: arms20190808_models.DescribeEnvPodMonitorRequest,
    ) -> arms20190808_models.DescribeEnvPodMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_env_pod_monitor_with_options(request, runtime)

    async def describe_env_pod_monitor_async(
        self,
        request: arms20190808_models.DescribeEnvPodMonitorRequest,
    ) -> arms20190808_models.DescribeEnvPodMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_env_pod_monitor_with_options_async(request, runtime)

    def describe_env_service_monitor_with_options(
        self,
        request: arms20190808_models.DescribeEnvServiceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeEnvServiceMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_monitor_name):
            query['ServiceMonitorName'] = request.service_monitor_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnvServiceMonitor',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeEnvServiceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_env_service_monitor_with_options_async(
        self,
        request: arms20190808_models.DescribeEnvServiceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeEnvServiceMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_monitor_name):
            query['ServiceMonitorName'] = request.service_monitor_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnvServiceMonitor',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeEnvServiceMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_env_service_monitor(
        self,
        request: arms20190808_models.DescribeEnvServiceMonitorRequest,
    ) -> arms20190808_models.DescribeEnvServiceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_env_service_monitor_with_options(request, runtime)

    async def describe_env_service_monitor_async(
        self,
        request: arms20190808_models.DescribeEnvServiceMonitorRequest,
    ) -> arms20190808_models.DescribeEnvServiceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_env_service_monitor_with_options_async(request, runtime)

    def describe_environment_with_options(
        self,
        request: arms20190808_models.DescribeEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnvironment',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_environment_with_options_async(
        self,
        request: arms20190808_models.DescribeEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnvironment',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_environment(
        self,
        request: arms20190808_models.DescribeEnvironmentRequest,
    ) -> arms20190808_models.DescribeEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_environment_with_options(request, runtime)

    async def describe_environment_async(
        self,
        request: arms20190808_models.DescribeEnvironmentRequest,
    ) -> arms20190808_models.DescribeEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_environment_with_options_async(request, runtime)

    def describe_environment_feature_with_options(
        self,
        request: arms20190808_models.DescribeEnvironmentFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeEnvironmentFeatureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnvironmentFeature',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeEnvironmentFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_environment_feature_with_options_async(
        self,
        request: arms20190808_models.DescribeEnvironmentFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeEnvironmentFeatureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEnvironmentFeature',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeEnvironmentFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_environment_feature(
        self,
        request: arms20190808_models.DescribeEnvironmentFeatureRequest,
    ) -> arms20190808_models.DescribeEnvironmentFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_environment_feature_with_options(request, runtime)

    async def describe_environment_feature_async(
        self,
        request: arms20190808_models.DescribeEnvironmentFeatureRequest,
    ) -> arms20190808_models.DescribeEnvironmentFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_environment_feature_with_options_async(request, runtime)

    def describe_imrobots_with_options(
        self,
        request: arms20190808_models.DescribeIMRobotsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.DescribeIMRobotsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.robot_ids):
            query['RobotIds'] = request.robot_ids
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
        if not UtilClient.is_unset(request.robot_ids):
            query['RobotIds'] = request.robot_ids
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
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
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
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
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

    def enable_metric_with_options(
        self,
        request: arms20190808_models.EnableMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.EnableMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.drop_metric):
            query['DropMetric'] = request.drop_metric
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableMetric',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.EnableMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_metric_with_options_async(
        self,
        request: arms20190808_models.EnableMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.EnableMetricResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.drop_metric):
            query['DropMetric'] = request.drop_metric
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableMetric',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.EnableMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_metric(
        self,
        request: arms20190808_models.EnableMetricRequest,
    ) -> arms20190808_models.EnableMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_metric_with_options(request, runtime)

    async def enable_metric_async(
        self,
        request: arms20190808_models.EnableMetricRequest,
    ) -> arms20190808_models.EnableMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_metric_with_options_async(request, runtime)

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
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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

    def get_app_jvmconfig_with_options(
        self,
        request: arms20190808_models.GetAppJVMConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetAppJVMConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppJVMConfig',
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
            arms20190808_models.GetAppJVMConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_app_jvmconfig_with_options_async(
        self,
        request: arms20190808_models.GetAppJVMConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetAppJVMConfigResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppJVMConfig',
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
            arms20190808_models.GetAppJVMConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_app_jvmconfig(
        self,
        request: arms20190808_models.GetAppJVMConfigRequest,
    ) -> arms20190808_models.GetAppJVMConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_app_jvmconfig_with_options(request, runtime)

    async def get_app_jvmconfig_async(
        self,
        request: arms20190808_models.GetAppJVMConfigRequest,
    ) -> arms20190808_models.GetAppJVMConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_app_jvmconfig_with_options_async(request, runtime)

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

    def get_cloud_cluster_all_url_with_options(
        self,
        request: arms20190808_models.GetCloudClusterAllUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetCloudClusterAllUrlResponse:
        """
        @deprecated : GetCloudClusterAllUrl is deprecated, please use ARMS::2019-08-08::GetRemoteWriteUrl instead.
        
        @param request: GetCloudClusterAllUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCloudClusterAllUrlResponse
        Deprecated
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
            action='GetCloudClusterAllUrl',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetCloudClusterAllUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cloud_cluster_all_url_with_options_async(
        self,
        request: arms20190808_models.GetCloudClusterAllUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetCloudClusterAllUrlResponse:
        """
        @deprecated : GetCloudClusterAllUrl is deprecated, please use ARMS::2019-08-08::GetRemoteWriteUrl instead.
        
        @param request: GetCloudClusterAllUrlRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetCloudClusterAllUrlResponse
        Deprecated
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
            action='GetCloudClusterAllUrl',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetCloudClusterAllUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cloud_cluster_all_url(
        self,
        request: arms20190808_models.GetCloudClusterAllUrlRequest,
    ) -> arms20190808_models.GetCloudClusterAllUrlResponse:
        """
        @deprecated : GetCloudClusterAllUrl is deprecated, please use ARMS::2019-08-08::GetRemoteWriteUrl instead.
        
        @param request: GetCloudClusterAllUrlRequest
        @return: GetCloudClusterAllUrlResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_cluster_all_url_with_options(request, runtime)

    async def get_cloud_cluster_all_url_async(
        self,
        request: arms20190808_models.GetCloudClusterAllUrlRequest,
    ) -> arms20190808_models.GetCloudClusterAllUrlResponse:
        """
        @deprecated : GetCloudClusterAllUrl is deprecated, please use ARMS::2019-08-08::GetRemoteWriteUrl instead.
        
        @param request: GetCloudClusterAllUrlRequest
        @return: GetCloudClusterAllUrlResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_cloud_cluster_all_url_with_options_async(request, runtime)

    def get_cluster_all_url_with_options(
        self,
        request: arms20190808_models.GetClusterAllUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetClusterAllUrlResponse:
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
            action='GetClusterAllUrl',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetClusterAllUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_all_url_with_options_async(
        self,
        request: arms20190808_models.GetClusterAllUrlRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetClusterAllUrlResponse:
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
            action='GetClusterAllUrl',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetClusterAllUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_all_url(
        self,
        request: arms20190808_models.GetClusterAllUrlRequest,
    ) -> arms20190808_models.GetClusterAllUrlResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_all_url_with_options(request, runtime)

    async def get_cluster_all_url_async(
        self,
        request: arms20190808_models.GetClusterAllUrlRequest,
    ) -> arms20190808_models.GetClusterAllUrlResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_all_url_with_options_async(request, runtime)

    def get_commercial_status_with_options(
        self,
        request: arms20190808_models.GetCommercialStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetCommercialStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCommercialStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetCommercialStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_commercial_status_with_options_async(
        self,
        request: arms20190808_models.GetCommercialStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetCommercialStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCommercialStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetCommercialStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_commercial_status(
        self,
        request: arms20190808_models.GetCommercialStatusRequest,
    ) -> arms20190808_models.GetCommercialStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_commercial_status_with_options(request, runtime)

    async def get_commercial_status_async(
        self,
        request: arms20190808_models.GetCommercialStatusRequest,
    ) -> arms20190808_models.GetCommercialStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_commercial_status_with_options_async(request, runtime)

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

    def get_grafana_workspace_with_options(
        self,
        request: arms20190808_models.GetGrafanaWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetGrafanaWorkspaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGrafanaWorkspace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetGrafanaWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_grafana_workspace_with_options_async(
        self,
        request: arms20190808_models.GetGrafanaWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetGrafanaWorkspaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGrafanaWorkspace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetGrafanaWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_grafana_workspace(
        self,
        request: arms20190808_models.GetGrafanaWorkspaceRequest,
    ) -> arms20190808_models.GetGrafanaWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_grafana_workspace_with_options(request, runtime)

    async def get_grafana_workspace_async(
        self,
        request: arms20190808_models.GetGrafanaWorkspaceRequest,
    ) -> arms20190808_models.GetGrafanaWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_grafana_workspace_with_options_async(request, runtime)

    def get_integration_state_with_options(
        self,
        request: arms20190808_models.GetIntegrationStateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetIntegrationStateResponse:
        """
        @deprecated : GetIntegrationState is deprecated, please use ARMS::2019-08-08::DescribeAddonRelease instead.
        
        @param request: GetIntegrationStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIntegrationStateResponse
        Deprecated
        """
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
        """
        @deprecated : GetIntegrationState is deprecated, please use ARMS::2019-08-08::DescribeAddonRelease instead.
        
        @param request: GetIntegrationStateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetIntegrationStateResponse
        Deprecated
        """
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
        """
        @deprecated : GetIntegrationState is deprecated, please use ARMS::2019-08-08::DescribeAddonRelease instead.
        
        @param request: GetIntegrationStateRequest
        @return: GetIntegrationStateResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.get_integration_state_with_options(request, runtime)

    async def get_integration_state_async(
        self,
        request: arms20190808_models.GetIntegrationStateRequest,
    ) -> arms20190808_models.GetIntegrationStateResponse:
        """
        @deprecated : GetIntegrationState is deprecated, please use ARMS::2019-08-08::DescribeAddonRelease instead.
        
        @param request: GetIntegrationStateRequest
        @return: GetIntegrationStateResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_integration_state_with_options_async(request, runtime)

    def get_managed_prometheus_status_with_options(
        self,
        request: arms20190808_models.GetManagedPrometheusStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetManagedPrometheusStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetManagedPrometheusStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetManagedPrometheusStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_managed_prometheus_status_with_options_async(
        self,
        request: arms20190808_models.GetManagedPrometheusStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetManagedPrometheusStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetManagedPrometheusStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetManagedPrometheusStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_managed_prometheus_status(
        self,
        request: arms20190808_models.GetManagedPrometheusStatusRequest,
    ) -> arms20190808_models.GetManagedPrometheusStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_managed_prometheus_status_with_options(request, runtime)

    async def get_managed_prometheus_status_async(
        self,
        request: arms20190808_models.GetManagedPrometheusStatusRequest,
    ) -> arms20190808_models.GetManagedPrometheusStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_managed_prometheus_status_with_options_async(request, runtime)

    def get_multiple_trace_with_options(
        self,
        request: arms20190808_models.GetMultipleTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetMultipleTraceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
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

    def get_on_call_schedules_detail_with_options(
        self,
        request: arms20190808_models.GetOnCallSchedulesDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetOnCallSchedulesDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOnCallSchedulesDetail',
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
            arms20190808_models.GetOnCallSchedulesDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_on_call_schedules_detail_with_options_async(
        self,
        request: arms20190808_models.GetOnCallSchedulesDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetOnCallSchedulesDetailResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOnCallSchedulesDetail',
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
            arms20190808_models.GetOnCallSchedulesDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_on_call_schedules_detail(
        self,
        request: arms20190808_models.GetOnCallSchedulesDetailRequest,
    ) -> arms20190808_models.GetOnCallSchedulesDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_on_call_schedules_detail_with_options(request, runtime)

    async def get_on_call_schedules_detail_async(
        self,
        request: arms20190808_models.GetOnCallSchedulesDetailRequest,
    ) -> arms20190808_models.GetOnCallSchedulesDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_on_call_schedules_detail_with_options_async(request, runtime)

    def get_prometheus_api_token_with_options(
        self,
        request: arms20190808_models.GetPrometheusApiTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetPrometheusApiTokenResponse:
        """
        None.
        
        @param request: GetPrometheusApiTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrometheusApiTokenResponse
        """
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
        """
        None.
        
        @param request: GetPrometheusApiTokenRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetPrometheusApiTokenResponse
        """
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
        """
        None.
        
        @param request: GetPrometheusApiTokenRequest
        @return: GetPrometheusApiTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_prometheus_api_token_with_options(request, runtime)

    async def get_prometheus_api_token_async(
        self,
        request: arms20190808_models.GetPrometheusApiTokenRequest,
    ) -> arms20190808_models.GetPrometheusApiTokenResponse:
        """
        None.
        
        @param request: GetPrometheusApiTokenRequest
        @return: GetPrometheusApiTokenResponse
        """
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

    def get_prometheus_instance_with_options(
        self,
        request: arms20190808_models.GetPrometheusInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetPrometheusInstanceResponse:
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
            action='GetPrometheusInstance',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_instance_with_options_async(
        self,
        request: arms20190808_models.GetPrometheusInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetPrometheusInstanceResponse:
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
            action='GetPrometheusInstance',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_instance(
        self,
        request: arms20190808_models.GetPrometheusInstanceRequest,
    ) -> arms20190808_models.GetPrometheusInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_prometheus_instance_with_options(request, runtime)

    async def get_prometheus_instance_async(
        self,
        request: arms20190808_models.GetPrometheusInstanceRequest,
    ) -> arms20190808_models.GetPrometheusInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_prometheus_instance_with_options_async(request, runtime)

    def get_prometheus_integration_with_options(
        self,
        request: arms20190808_models.GetPrometheusIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetPrometheusIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_integration_with_options_async(
        self,
        request: arms20190808_models.GetPrometheusIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetPrometheusIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_integration(
        self,
        request: arms20190808_models.GetPrometheusIntegrationRequest,
    ) -> arms20190808_models.GetPrometheusIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_prometheus_integration_with_options(request, runtime)

    async def get_prometheus_integration_async(
        self,
        request: arms20190808_models.GetPrometheusIntegrationRequest,
    ) -> arms20190808_models.GetPrometheusIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_prometheus_integration_with_options_async(request, runtime)

    def get_prometheus_monitoring_with_options(
        self,
        request: arms20190808_models.GetPrometheusMonitoringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetPrometheusMonitoringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusMonitoring',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_monitoring_with_options_async(
        self,
        request: arms20190808_models.GetPrometheusMonitoringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetPrometheusMonitoringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusMonitoring',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusMonitoringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_monitoring(
        self,
        request: arms20190808_models.GetPrometheusMonitoringRequest,
    ) -> arms20190808_models.GetPrometheusMonitoringResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_prometheus_monitoring_with_options(request, runtime)

    async def get_prometheus_monitoring_async(
        self,
        request: arms20190808_models.GetPrometheusMonitoringRequest,
    ) -> arms20190808_models.GetPrometheusMonitoringResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_prometheus_monitoring_with_options_async(request, runtime)

    def get_prometheus_remote_write_with_options(
        self,
        request: arms20190808_models.GetPrometheusRemoteWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetPrometheusRemoteWriteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remote_write_name):
            query['RemoteWriteName'] = request.remote_write_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusRemoteWrite',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusRemoteWriteResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_prometheus_remote_write_with_options_async(
        self,
        request: arms20190808_models.GetPrometheusRemoteWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetPrometheusRemoteWriteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remote_write_name):
            query['RemoteWriteName'] = request.remote_write_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusRemoteWrite',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusRemoteWriteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_prometheus_remote_write(
        self,
        request: arms20190808_models.GetPrometheusRemoteWriteRequest,
    ) -> arms20190808_models.GetPrometheusRemoteWriteResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_prometheus_remote_write_with_options(request, runtime)

    async def get_prometheus_remote_write_async(
        self,
        request: arms20190808_models.GetPrometheusRemoteWriteRequest,
    ) -> arms20190808_models.GetPrometheusRemoteWriteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_prometheus_remote_write_with_options_async(request, runtime)

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

    def get_retcode_app_by_pid_with_options(
        self,
        request: arms20190808_models.GetRetcodeAppByPidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetRetcodeAppByPidResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRetcodeAppByPid',
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
            arms20190808_models.GetRetcodeAppByPidResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_retcode_app_by_pid_with_options_async(
        self,
        request: arms20190808_models.GetRetcodeAppByPidRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetRetcodeAppByPidResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRetcodeAppByPid',
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
            arms20190808_models.GetRetcodeAppByPidResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_retcode_app_by_pid(
        self,
        request: arms20190808_models.GetRetcodeAppByPidRequest,
    ) -> arms20190808_models.GetRetcodeAppByPidResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_retcode_app_by_pid_with_options(request, runtime)

    async def get_retcode_app_by_pid_async(
        self,
        request: arms20190808_models.GetRetcodeAppByPidRequest,
    ) -> arms20190808_models.GetRetcodeAppByPidResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_retcode_app_by_pid_with_options_async(request, runtime)

    def get_retcode_data_by_query_with_options(
        self,
        request: arms20190808_models.GetRetcodeDataByQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetRetcodeDataByQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRetcodeDataByQuery',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetRetcodeDataByQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_retcode_data_by_query_with_options_async(
        self,
        request: arms20190808_models.GetRetcodeDataByQueryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetRetcodeDataByQueryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRetcodeDataByQuery',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetRetcodeDataByQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_retcode_data_by_query(
        self,
        request: arms20190808_models.GetRetcodeDataByQueryRequest,
    ) -> arms20190808_models.GetRetcodeDataByQueryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_retcode_data_by_query_with_options(request, runtime)

    async def get_retcode_data_by_query_async(
        self,
        request: arms20190808_models.GetRetcodeDataByQueryRequest,
    ) -> arms20190808_models.GetRetcodeDataByQueryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_retcode_data_by_query_with_options_async(request, runtime)

    def get_retcode_logstore_with_options(
        self,
        request: arms20190808_models.GetRetcodeLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetRetcodeLogstoreResponse:
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
            action='GetRetcodeLogstore',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetRetcodeLogstoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_retcode_logstore_with_options_async(
        self,
        request: arms20190808_models.GetRetcodeLogstoreRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetRetcodeLogstoreResponse:
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
            action='GetRetcodeLogstore',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetRetcodeLogstoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_retcode_logstore(
        self,
        request: arms20190808_models.GetRetcodeLogstoreRequest,
    ) -> arms20190808_models.GetRetcodeLogstoreResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_retcode_logstore_with_options(request, runtime)

    async def get_retcode_logstore_async(
        self,
        request: arms20190808_models.GetRetcodeLogstoreRequest,
    ) -> arms20190808_models.GetRetcodeLogstoreResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_retcode_logstore_with_options_async(request, runtime)

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

    def get_source_map_info_with_options(
        self,
        request: arms20190808_models.GetSourceMapInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetSourceMapInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ascending_sequence):
            query['AscendingSequence'] = request.ascending_sequence
        if not UtilClient.is_unset(request.edition):
            query['Edition'] = request.edition
        if not UtilClient.is_unset(request.id):
            query['ID'] = request.id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order_field):
            query['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSourceMapInfo',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetSourceMapInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_source_map_info_with_options_async(
        self,
        request: arms20190808_models.GetSourceMapInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetSourceMapInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ascending_sequence):
            query['AscendingSequence'] = request.ascending_sequence
        if not UtilClient.is_unset(request.edition):
            query['Edition'] = request.edition
        if not UtilClient.is_unset(request.id):
            query['ID'] = request.id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order_field):
            query['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSourceMapInfo',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetSourceMapInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_source_map_info(
        self,
        request: arms20190808_models.GetSourceMapInfoRequest,
    ) -> arms20190808_models.GetSourceMapInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_source_map_info_with_options(request, runtime)

    async def get_source_map_info_async(
        self,
        request: arms20190808_models.GetSourceMapInfoRequest,
    ) -> arms20190808_models.GetSourceMapInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_source_map_info_with_options_async(request, runtime)

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

    def get_synthetic_monitors_with_options(
        self,
        tmp_req: arms20190808_models.GetSyntheticMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetSyntheticMonitorsResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.GetSyntheticMonitorsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSyntheticMonitors',
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
            arms20190808_models.GetSyntheticMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_synthetic_monitors_with_options_async(
        self,
        tmp_req: arms20190808_models.GetSyntheticMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetSyntheticMonitorsResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.GetSyntheticMonitorsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filter):
            request.filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filter, 'Filter', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSyntheticMonitors',
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
            arms20190808_models.GetSyntheticMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_synthetic_monitors(
        self,
        request: arms20190808_models.GetSyntheticMonitorsRequest,
    ) -> arms20190808_models.GetSyntheticMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_synthetic_monitors_with_options(request, runtime)

    async def get_synthetic_monitors_async(
        self,
        request: arms20190808_models.GetSyntheticMonitorsRequest,
    ) -> arms20190808_models.GetSyntheticMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_synthetic_monitors_with_options_async(request, runtime)

    def get_synthetic_task_detail_with_options(
        self,
        request: arms20190808_models.GetSyntheticTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetSyntheticTaskDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSyntheticTaskDetail',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetSyntheticTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_synthetic_task_detail_with_options_async(
        self,
        request: arms20190808_models.GetSyntheticTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetSyntheticTaskDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSyntheticTaskDetail',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetSyntheticTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_synthetic_task_detail(
        self,
        request: arms20190808_models.GetSyntheticTaskDetailRequest,
    ) -> arms20190808_models.GetSyntheticTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_synthetic_task_detail_with_options(request, runtime)

    async def get_synthetic_task_detail_async(
        self,
        request: arms20190808_models.GetSyntheticTaskDetailRequest,
    ) -> arms20190808_models.GetSyntheticTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_synthetic_task_detail_with_options_async(request, runtime)

    def get_synthetic_task_list_with_options(
        self,
        request: arms20190808_models.GetSyntheticTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetSyntheticTaskListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSyntheticTaskList',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetSyntheticTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_synthetic_task_list_with_options_async(
        self,
        request: arms20190808_models.GetSyntheticTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetSyntheticTaskListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSyntheticTaskList',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetSyntheticTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_synthetic_task_list(
        self,
        request: arms20190808_models.GetSyntheticTaskListRequest,
    ) -> arms20190808_models.GetSyntheticTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_synthetic_task_list_with_options(request, runtime)

    async def get_synthetic_task_list_async(
        self,
        request: arms20190808_models.GetSyntheticTaskListRequest,
    ) -> arms20190808_models.GetSyntheticTaskListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_synthetic_task_list_with_options_async(request, runtime)

    def get_synthetic_task_monitors_with_options(
        self,
        request: arms20190808_models.GetSyntheticTaskMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetSyntheticTaskMonitorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSyntheticTaskMonitors',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetSyntheticTaskMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_synthetic_task_monitors_with_options_async(
        self,
        request: arms20190808_models.GetSyntheticTaskMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetSyntheticTaskMonitorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSyntheticTaskMonitors',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetSyntheticTaskMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_synthetic_task_monitors(
        self,
        request: arms20190808_models.GetSyntheticTaskMonitorsRequest,
    ) -> arms20190808_models.GetSyntheticTaskMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_synthetic_task_monitors_with_options(request, runtime)

    async def get_synthetic_task_monitors_async(
        self,
        request: arms20190808_models.GetSyntheticTaskMonitorsRequest,
    ) -> arms20190808_models.GetSyntheticTaskMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_synthetic_task_monitors_with_options_async(request, runtime)

    def get_timing_synthetic_task_with_options(
        self,
        request: arms20190808_models.GetTimingSyntheticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetTimingSyntheticTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTimingSyntheticTask',
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
            arms20190808_models.GetTimingSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_timing_synthetic_task_with_options_async(
        self,
        request: arms20190808_models.GetTimingSyntheticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetTimingSyntheticTaskResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTimingSyntheticTask',
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
            arms20190808_models.GetTimingSyntheticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_timing_synthetic_task(
        self,
        request: arms20190808_models.GetTimingSyntheticTaskRequest,
    ) -> arms20190808_models.GetTimingSyntheticTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_timing_synthetic_task_with_options(request, runtime)

    async def get_timing_synthetic_task_async(
        self,
        request: arms20190808_models.GetTimingSyntheticTaskRequest,
    ) -> arms20190808_models.GetTimingSyntheticTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_timing_synthetic_task_with_options_async(request, runtime)

    def get_trace_with_options(
        self,
        request: arms20190808_models.GetTraceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.GetTraceResponse:
        """
        > You must use Application Real-Time Monitoring Service (ARMS) SDK for Java V2.7.24.
        
        @param request: GetTraceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTraceResponse
        """
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
        """
        > You must use Application Real-Time Monitoring Service (ARMS) SDK for Java V2.7.24.
        
        @param request: GetTraceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTraceResponse
        """
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
        """
        > You must use Application Real-Time Monitoring Service (ARMS) SDK for Java V2.7.24.
        
        @param request: GetTraceRequest
        @return: GetTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_trace_with_options(request, runtime)

    async def get_trace_async(
        self,
        request: arms20190808_models.GetTraceRequest,
    ) -> arms20190808_models.GetTraceResponse:
        """
        > You must use Application Real-Time Monitoring Service (ARMS) SDK for Java V2.7.24.
        
        @param request: GetTraceRequest
        @return: GetTraceResponse
        """
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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

    def import_app_alert_rules_with_options(
        self,
        request: arms20190808_models.ImportAppAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ImportAppAlertRulesResponse:
        """
        >  You can call the *ImportAppAlertRules** operation to import only the alert rules that are generated by Application Real-Time Monitoring Service (ARMS) for application monitoring and browser monitoring. This operation cannot be used to import custom alert rules, alert rules for Prometheus monitoring, or default emergency alert rules.
        
        @param request: ImportAppAlertRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportAppAlertRulesResponse
        """
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        """
        >  You can call the *ImportAppAlertRules** operation to import only the alert rules that are generated by Application Real-Time Monitoring Service (ARMS) for application monitoring and browser monitoring. This operation cannot be used to import custom alert rules, alert rules for Prometheus monitoring, or default emergency alert rules.
        
        @param request: ImportAppAlertRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ImportAppAlertRulesResponse
        """
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        """
        >  You can call the *ImportAppAlertRules** operation to import only the alert rules that are generated by Application Real-Time Monitoring Service (ARMS) for application monitoring and browser monitoring. This operation cannot be used to import custom alert rules, alert rules for Prometheus monitoring, or default emergency alert rules.
        
        @param request: ImportAppAlertRulesRequest
        @return: ImportAppAlertRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_app_alert_rules_with_options(request, runtime)

    async def import_app_alert_rules_async(
        self,
        request: arms20190808_models.ImportAppAlertRulesRequest,
    ) -> arms20190808_models.ImportAppAlertRulesResponse:
        """
        >  You can call the *ImportAppAlertRules** operation to import only the alert rules that are generated by Application Real-Time Monitoring Service (ARMS) for application monitoring and browser monitoring. This operation cannot be used to import custom alert rules, alert rules for Prometheus monitoring, or default emergency alert rules.
        
        @param request: ImportAppAlertRulesRequest
        @return: ImportAppAlertRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.import_app_alert_rules_with_options_async(request, runtime)

    def init_environment_with_options(
        self,
        request: arms20190808_models.InitEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.InitEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.managed_type):
            query['ManagedType'] = request.managed_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitEnvironment',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.InitEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_environment_with_options_async(
        self,
        request: arms20190808_models.InitEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.InitEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.managed_type):
            query['ManagedType'] = request.managed_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitEnvironment',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.InitEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_environment(
        self,
        request: arms20190808_models.InitEnvironmentRequest,
    ) -> arms20190808_models.InitEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_environment_with_options(request, runtime)

    async def init_environment_async(
        self,
        request: arms20190808_models.InitEnvironmentRequest,
    ) -> arms20190808_models.InitEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_environment_with_options_async(request, runtime)

    def install_addon_with_options(
        self,
        request: arms20190808_models.InstallAddonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.InstallAddonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.release_name):
            query['ReleaseName'] = request.release_name
        if not UtilClient.is_unset(request.values):
            query['Values'] = request.values
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallAddon',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.InstallAddonResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_addon_with_options_async(
        self,
        request: arms20190808_models.InstallAddonRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.InstallAddonResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.release_name):
            query['ReleaseName'] = request.release_name
        if not UtilClient.is_unset(request.values):
            query['Values'] = request.values
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallAddon',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.InstallAddonResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_addon(
        self,
        request: arms20190808_models.InstallAddonRequest,
    ) -> arms20190808_models.InstallAddonResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_addon_with_options(request, runtime)

    async def install_addon_async(
        self,
        request: arms20190808_models.InstallAddonRequest,
    ) -> arms20190808_models.InstallAddonResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_addon_with_options_async(request, runtime)

    def install_cms_exporter_with_options(
        self,
        request: arms20190808_models.InstallCmsExporterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.InstallCmsExporterResponse:
        """
        @deprecated : InstallCmsExporter is deprecated, please use ARMS::2019-08-08::InstallAddon instead.
        
        @param request: InstallCmsExporterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallCmsExporterResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cms_args):
            query['CmsArgs'] = request.cms_args
        if not UtilClient.is_unset(request.direct_args):
            query['DirectArgs'] = request.direct_args
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
        """
        @deprecated : InstallCmsExporter is deprecated, please use ARMS::2019-08-08::InstallAddon instead.
        
        @param request: InstallCmsExporterRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallCmsExporterResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cms_args):
            query['CmsArgs'] = request.cms_args
        if not UtilClient.is_unset(request.direct_args):
            query['DirectArgs'] = request.direct_args
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
        """
        @deprecated : InstallCmsExporter is deprecated, please use ARMS::2019-08-08::InstallAddon instead.
        
        @param request: InstallCmsExporterRequest
        @return: InstallCmsExporterResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.install_cms_exporter_with_options(request, runtime)

    async def install_cms_exporter_async(
        self,
        request: arms20190808_models.InstallCmsExporterRequest,
    ) -> arms20190808_models.InstallCmsExporterResponse:
        """
        @deprecated : InstallCmsExporter is deprecated, please use ARMS::2019-08-08::InstallAddon instead.
        
        @param request: InstallCmsExporterRequest
        @return: InstallCmsExporterResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.install_cms_exporter_with_options_async(request, runtime)

    def install_environment_feature_with_options(
        self,
        request: arms20190808_models.InstallEnvironmentFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.InstallEnvironmentFeatureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.feature_version):
            query['FeatureVersion'] = request.feature_version
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallEnvironmentFeature',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.InstallEnvironmentFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_environment_feature_with_options_async(
        self,
        request: arms20190808_models.InstallEnvironmentFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.InstallEnvironmentFeatureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.feature_version):
            query['FeatureVersion'] = request.feature_version
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallEnvironmentFeature',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.InstallEnvironmentFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_environment_feature(
        self,
        request: arms20190808_models.InstallEnvironmentFeatureRequest,
    ) -> arms20190808_models.InstallEnvironmentFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_environment_feature_with_options(request, runtime)

    async def install_environment_feature_async(
        self,
        request: arms20190808_models.InstallEnvironmentFeatureRequest,
    ) -> arms20190808_models.InstallEnvironmentFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_environment_feature_with_options_async(request, runtime)

    def install_managed_prometheus_with_options(
        self,
        request: arms20190808_models.InstallManagedPrometheusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.InstallManagedPrometheusResponse:
        """
        If you call the operation to monitor an ASK cluster or an ECS instance, a Prometheus agent is installed in the ASK cluster or ECS instance. Make sure that the ASK cluster or ECS instance has no Prometheus agent installed in advance.
        
        @param request: InstallManagedPrometheusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallManagedPrometheusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.grafana_instance_id):
            query['GrafanaInstanceId'] = request.grafana_instance_id
        if not UtilClient.is_unset(request.kube_config):
            query['KubeConfig'] = request.kube_config
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
        """
        If you call the operation to monitor an ASK cluster or an ECS instance, a Prometheus agent is installed in the ASK cluster or ECS instance. Make sure that the ASK cluster or ECS instance has no Prometheus agent installed in advance.
        
        @param request: InstallManagedPrometheusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InstallManagedPrometheusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.grafana_instance_id):
            query['GrafanaInstanceId'] = request.grafana_instance_id
        if not UtilClient.is_unset(request.kube_config):
            query['KubeConfig'] = request.kube_config
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
        """
        If you call the operation to monitor an ASK cluster or an ECS instance, a Prometheus agent is installed in the ASK cluster or ECS instance. Make sure that the ASK cluster or ECS instance has no Prometheus agent installed in advance.
        
        @param request: InstallManagedPrometheusRequest
        @return: InstallManagedPrometheusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.install_managed_prometheus_with_options(request, runtime)

    async def install_managed_prometheus_async(
        self,
        request: arms20190808_models.InstallManagedPrometheusRequest,
    ) -> arms20190808_models.InstallManagedPrometheusResponse:
        """
        If you call the operation to monitor an ASK cluster or an ECS instance, a Prometheus agent is installed in the ASK cluster or ECS instance. Make sure that the ASK cluster or ECS instance has no Prometheus agent installed in advance.
        
        @param request: InstallManagedPrometheusRequest
        @return: InstallManagedPrometheusResponse
        """
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

    def list_addon_releases_with_options(
        self,
        request: arms20190808_models.ListAddonReleasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListAddonReleasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['AddonName'] = request.addon_name
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddonReleases',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListAddonReleasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addon_releases_with_options_async(
        self,
        request: arms20190808_models.ListAddonReleasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListAddonReleasesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['AddonName'] = request.addon_name
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddonReleases',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListAddonReleasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_addon_releases(
        self,
        request: arms20190808_models.ListAddonReleasesRequest,
    ) -> arms20190808_models.ListAddonReleasesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_addon_releases_with_options(request, runtime)

    async def list_addon_releases_async(
        self,
        request: arms20190808_models.ListAddonReleasesRequest,
    ) -> arms20190808_models.ListAddonReleasesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_addon_releases_with_options_async(request, runtime)

    def list_addons_with_options(
        self,
        request: arms20190808_models.ListAddonsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListAddonsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.regexp):
            query['Regexp'] = request.regexp
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddons',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListAddonsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_addons_with_options_async(
        self,
        request: arms20190808_models.ListAddonsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListAddonsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.regexp):
            query['Regexp'] = request.regexp
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.search):
            query['Search'] = request.search
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAddons',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListAddonsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_addons(
        self,
        request: arms20190808_models.ListAddonsRequest,
    ) -> arms20190808_models.ListAddonsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_addons_with_options(request, runtime)

    async def list_addons_async(
        self,
        request: arms20190808_models.ListAddonsRequest,
    ) -> arms20190808_models.ListAddonsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_addons_with_options_async(request, runtime)

    def list_alert_events_with_options(
        self,
        request: arms20190808_models.ListAlertEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListAlertEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_name):
            query['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.matching_conditions):
            query['MatchingConditions'] = request.matching_conditions
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlertEvents',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListAlertEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alert_events_with_options_async(
        self,
        request: arms20190808_models.ListAlertEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListAlertEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_name):
            query['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.matching_conditions):
            query['MatchingConditions'] = request.matching_conditions
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlertEvents',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListAlertEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alert_events(
        self,
        request: arms20190808_models.ListAlertEventsRequest,
    ) -> arms20190808_models.ListAlertEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_alert_events_with_options(request, runtime)

    async def list_alert_events_async(
        self,
        request: arms20190808_models.ListAlertEventsRequest,
    ) -> arms20190808_models.ListAlertEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_alert_events_with_options_async(request, runtime)

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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
        """
        @deprecated : ListCmsInstances is deprecated, please use ARMS::2019-08-08::ListEnvironmentAddons instead.
        
        @param request: ListCmsInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCmsInstancesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type_filter):
            query['TypeFilter'] = request.type_filter
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
        """
        @deprecated : ListCmsInstances is deprecated, please use ARMS::2019-08-08::ListEnvironmentAddons instead.
        
        @param request: ListCmsInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListCmsInstancesResponse
        Deprecated
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type_filter):
            query['TypeFilter'] = request.type_filter
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
        """
        @deprecated : ListCmsInstances is deprecated, please use ARMS::2019-08-08::ListEnvironmentAddons instead.
        
        @param request: ListCmsInstancesRequest
        @return: ListCmsInstancesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return self.list_cms_instances_with_options(request, runtime)

    async def list_cms_instances_async(
        self,
        request: arms20190808_models.ListCmsInstancesRequest,
    ) -> arms20190808_models.ListCmsInstancesResponse:
        """
        @deprecated : ListCmsInstances is deprecated, please use ARMS::2019-08-08::ListEnvironmentAddons instead.
        
        @param request: ListCmsInstancesRequest
        @return: ListCmsInstancesResponse
        Deprecated
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_cms_instances_with_options_async(request, runtime)

    def list_dashboards_with_options(
        self,
        request: arms20190808_models.ListDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListDashboardsResponse:
        """
        None.
        
        @param request: ListDashboardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDashboardsResponse
        """
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
        """
        None.
        
        @param request: ListDashboardsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListDashboardsResponse
        """
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
        """
        None.
        
        @param request: ListDashboardsRequest
        @return: ListDashboardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dashboards_with_options(request, runtime)

    async def list_dashboards_async(
        self,
        request: arms20190808_models.ListDashboardsRequest,
    ) -> arms20190808_models.ListDashboardsResponse:
        """
        None.
        
        @param request: ListDashboardsRequest
        @return: ListDashboardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_dashboards_with_options_async(request, runtime)

    def list_dashboards_by_name_with_options(
        self,
        request: arms20190808_models.ListDashboardsByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListDashboardsByNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.dash_board_name):
            query['DashBoardName'] = request.dash_board_name
        if not UtilClient.is_unset(request.dash_board_version):
            query['DashBoardVersion'] = request.dash_board_version
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.only_query):
            query['OnlyQuery'] = request.only_query
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardsByName',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListDashboardsByNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dashboards_by_name_with_options_async(
        self,
        request: arms20190808_models.ListDashboardsByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListDashboardsByNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.dash_board_name):
            query['DashBoardName'] = request.dash_board_name
        if not UtilClient.is_unset(request.dash_board_version):
            query['DashBoardVersion'] = request.dash_board_version
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.only_query):
            query['OnlyQuery'] = request.only_query
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardsByName',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListDashboardsByNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dashboards_by_name(
        self,
        request: arms20190808_models.ListDashboardsByNameRequest,
    ) -> arms20190808_models.ListDashboardsByNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_dashboards_by_name_with_options(request, runtime)

    async def list_dashboards_by_name_async(
        self,
        request: arms20190808_models.ListDashboardsByNameRequest,
    ) -> arms20190808_models.ListDashboardsByNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_dashboards_by_name_with_options_async(request, runtime)

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

    def list_env_custom_jobs_with_options(
        self,
        request: arms20190808_models.ListEnvCustomJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListEnvCustomJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypt_yaml):
            query['EncryptYaml'] = request.encrypt_yaml
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvCustomJobs',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEnvCustomJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_env_custom_jobs_with_options_async(
        self,
        request: arms20190808_models.ListEnvCustomJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListEnvCustomJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.encrypt_yaml):
            query['EncryptYaml'] = request.encrypt_yaml
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvCustomJobs',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEnvCustomJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_env_custom_jobs(
        self,
        request: arms20190808_models.ListEnvCustomJobsRequest,
    ) -> arms20190808_models.ListEnvCustomJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_env_custom_jobs_with_options(request, runtime)

    async def list_env_custom_jobs_async(
        self,
        request: arms20190808_models.ListEnvCustomJobsRequest,
    ) -> arms20190808_models.ListEnvCustomJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_env_custom_jobs_with_options_async(request, runtime)

    def list_env_pod_monitors_with_options(
        self,
        request: arms20190808_models.ListEnvPodMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListEnvPodMonitorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvPodMonitors',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEnvPodMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_env_pod_monitors_with_options_async(
        self,
        request: arms20190808_models.ListEnvPodMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListEnvPodMonitorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvPodMonitors',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEnvPodMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_env_pod_monitors(
        self,
        request: arms20190808_models.ListEnvPodMonitorsRequest,
    ) -> arms20190808_models.ListEnvPodMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_env_pod_monitors_with_options(request, runtime)

    async def list_env_pod_monitors_async(
        self,
        request: arms20190808_models.ListEnvPodMonitorsRequest,
    ) -> arms20190808_models.ListEnvPodMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_env_pod_monitors_with_options_async(request, runtime)

    def list_env_service_monitors_with_options(
        self,
        request: arms20190808_models.ListEnvServiceMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListEnvServiceMonitorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvServiceMonitors',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEnvServiceMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_env_service_monitors_with_options_async(
        self,
        request: arms20190808_models.ListEnvServiceMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListEnvServiceMonitorsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvServiceMonitors',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEnvServiceMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_env_service_monitors(
        self,
        request: arms20190808_models.ListEnvServiceMonitorsRequest,
    ) -> arms20190808_models.ListEnvServiceMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_env_service_monitors_with_options(request, runtime)

    async def list_env_service_monitors_async(
        self,
        request: arms20190808_models.ListEnvServiceMonitorsRequest,
    ) -> arms20190808_models.ListEnvServiceMonitorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_env_service_monitors_with_options_async(request, runtime)

    def list_environment_dashboards_with_options(
        self,
        request: arms20190808_models.ListEnvironmentDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListEnvironmentDashboardsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['AddonName'] = request.addon_name
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironmentDashboards',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEnvironmentDashboardsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environment_dashboards_with_options_async(
        self,
        request: arms20190808_models.ListEnvironmentDashboardsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListEnvironmentDashboardsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['AddonName'] = request.addon_name
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironmentDashboards',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEnvironmentDashboardsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environment_dashboards(
        self,
        request: arms20190808_models.ListEnvironmentDashboardsRequest,
    ) -> arms20190808_models.ListEnvironmentDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_environment_dashboards_with_options(request, runtime)

    async def list_environment_dashboards_async(
        self,
        request: arms20190808_models.ListEnvironmentDashboardsRequest,
    ) -> arms20190808_models.ListEnvironmentDashboardsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_environment_dashboards_with_options_async(request, runtime)

    def list_environment_features_with_options(
        self,
        request: arms20190808_models.ListEnvironmentFeaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListEnvironmentFeaturesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironmentFeatures',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEnvironmentFeaturesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environment_features_with_options_async(
        self,
        request: arms20190808_models.ListEnvironmentFeaturesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListEnvironmentFeaturesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironmentFeatures',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEnvironmentFeaturesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environment_features(
        self,
        request: arms20190808_models.ListEnvironmentFeaturesRequest,
    ) -> arms20190808_models.ListEnvironmentFeaturesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_environment_features_with_options(request, runtime)

    async def list_environment_features_async(
        self,
        request: arms20190808_models.ListEnvironmentFeaturesRequest,
    ) -> arms20190808_models.ListEnvironmentFeaturesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_environment_features_with_options_async(request, runtime)

    def list_environments_with_options(
        self,
        tmp_req: arms20190808_models.ListEnvironmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListEnvironmentsResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.ListEnvironmentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['AddonName'] = request.addon_name
        if not UtilClient.is_unset(request.bind_resource_id):
            query['BindResourceId'] = request.bind_resource_id
        if not UtilClient.is_unset(request.environment_type):
            query['EnvironmentType'] = request.environment_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEnvironmentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_environments_with_options_async(
        self,
        tmp_req: arms20190808_models.ListEnvironmentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListEnvironmentsResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.ListEnvironmentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.addon_name):
            query['AddonName'] = request.addon_name
        if not UtilClient.is_unset(request.bind_resource_id):
            query['BindResourceId'] = request.bind_resource_id
        if not UtilClient.is_unset(request.environment_type):
            query['EnvironmentType'] = request.environment_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEnvironments',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEnvironmentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_environments(
        self,
        request: arms20190808_models.ListEnvironmentsRequest,
    ) -> arms20190808_models.ListEnvironmentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_environments_with_options(request, runtime)

    async def list_environments_async(
        self,
        request: arms20190808_models.ListEnvironmentsRequest,
    ) -> arms20190808_models.ListEnvironmentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_environments_with_options_async(request, runtime)

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

    def list_grafana_workspace_with_options(
        self,
        tmp_req: arms20190808_models.ListGrafanaWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListGrafanaWorkspaceResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.ListGrafanaWorkspaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGrafanaWorkspace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListGrafanaWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_grafana_workspace_with_options_async(
        self,
        tmp_req: arms20190808_models.ListGrafanaWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListGrafanaWorkspaceResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.ListGrafanaWorkspaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListGrafanaWorkspace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListGrafanaWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_grafana_workspace(
        self,
        request: arms20190808_models.ListGrafanaWorkspaceRequest,
    ) -> arms20190808_models.ListGrafanaWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_grafana_workspace_with_options(request, runtime)

    async def list_grafana_workspace_async(
        self,
        request: arms20190808_models.ListGrafanaWorkspaceRequest,
    ) -> arms20190808_models.ListGrafanaWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_grafana_workspace_with_options_async(request, runtime)

    def list_insights_events_with_options(
        self,
        request: arms20190808_models.ListInsightsEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListInsightsEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.insights_types):
            query['InsightsTypes'] = request.insights_types
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
            action='ListInsightsEvents',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListInsightsEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_insights_events_with_options_async(
        self,
        request: arms20190808_models.ListInsightsEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListInsightsEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.insights_types):
            query['InsightsTypes'] = request.insights_types
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
            action='ListInsightsEvents',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListInsightsEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_insights_events(
        self,
        request: arms20190808_models.ListInsightsEventsRequest,
    ) -> arms20190808_models.ListInsightsEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_insights_events_with_options(request, runtime)

    async def list_insights_events_async(
        self,
        request: arms20190808_models.ListInsightsEventsRequest,
    ) -> arms20190808_models.ListInsightsEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_insights_events_with_options_async(request, runtime)

    def list_integration_with_options(
        self,
        request: arms20190808_models.ListIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListIntegrationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntegration',
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
            arms20190808_models.ListIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_with_options_async(
        self,
        request: arms20190808_models.ListIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListIntegrationResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntegration',
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
            arms20190808_models.ListIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration(
        self,
        request: arms20190808_models.ListIntegrationRequest,
    ) -> arms20190808_models.ListIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_integration_with_options(request, runtime)

    async def list_integration_async(
        self,
        request: arms20190808_models.ListIntegrationRequest,
    ) -> arms20190808_models.ListIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_integration_with_options_async(request, runtime)

    def list_notification_policies_with_options(
        self,
        request: arms20190808_models.ListNotificationPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListNotificationPoliciesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directed_mode):
            query['DirectedMode'] = request.directed_mode
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
        if not UtilClient.is_unset(request.directed_mode):
            query['DirectedMode'] = request.directed_mode
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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

    def list_prometheus_instance_by_tag_and_resource_group_id_with_options(
        self,
        request: arms20190808_models.ListPrometheusInstanceByTagAndResourceGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPrometheusInstanceByTagAndResourceGroupIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusInstanceByTagAndResourceGroupId',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusInstanceByTagAndResourceGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_instance_by_tag_and_resource_group_id_with_options_async(
        self,
        request: arms20190808_models.ListPrometheusInstanceByTagAndResourceGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPrometheusInstanceByTagAndResourceGroupIdResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusInstanceByTagAndResourceGroupId',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusInstanceByTagAndResourceGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_instance_by_tag_and_resource_group_id(
        self,
        request: arms20190808_models.ListPrometheusInstanceByTagAndResourceGroupIdRequest,
    ) -> arms20190808_models.ListPrometheusInstanceByTagAndResourceGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_instance_by_tag_and_resource_group_id_with_options(request, runtime)

    async def list_prometheus_instance_by_tag_and_resource_group_id_async(
        self,
        request: arms20190808_models.ListPrometheusInstanceByTagAndResourceGroupIdRequest,
    ) -> arms20190808_models.ListPrometheusInstanceByTagAndResourceGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_prometheus_instance_by_tag_and_resource_group_id_with_options_async(request, runtime)

    def list_prometheus_instances_with_options(
        self,
        request: arms20190808_models.ListPrometheusInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPrometheusInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.show_global_view):
            query['ShowGlobalView'] = request.show_global_view
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusInstances',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_instances_with_options_async(
        self,
        request: arms20190808_models.ListPrometheusInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPrometheusInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.show_global_view):
            query['ShowGlobalView'] = request.show_global_view
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusInstances',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_instances(
        self,
        request: arms20190808_models.ListPrometheusInstancesRequest,
    ) -> arms20190808_models.ListPrometheusInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_instances_with_options(request, runtime)

    async def list_prometheus_instances_async(
        self,
        request: arms20190808_models.ListPrometheusInstancesRequest,
    ) -> arms20190808_models.ListPrometheusInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_prometheus_instances_with_options_async(request, runtime)

    def list_prometheus_integration_with_options(
        self,
        request: arms20190808_models.ListPrometheusIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPrometheusIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_integration_with_options_async(
        self,
        request: arms20190808_models.ListPrometheusIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPrometheusIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_integration(
        self,
        request: arms20190808_models.ListPrometheusIntegrationRequest,
    ) -> arms20190808_models.ListPrometheusIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_integration_with_options(request, runtime)

    async def list_prometheus_integration_async(
        self,
        request: arms20190808_models.ListPrometheusIntegrationRequest,
    ) -> arms20190808_models.ListPrometheusIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_prometheus_integration_with_options_async(request, runtime)

    def list_prometheus_monitoring_with_options(
        self,
        request: arms20190808_models.ListPrometheusMonitoringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPrometheusMonitoringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusMonitoring',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_monitoring_with_options_async(
        self,
        request: arms20190808_models.ListPrometheusMonitoringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPrometheusMonitoringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusMonitoring',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusMonitoringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_monitoring(
        self,
        request: arms20190808_models.ListPrometheusMonitoringRequest,
    ) -> arms20190808_models.ListPrometheusMonitoringResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_monitoring_with_options(request, runtime)

    async def list_prometheus_monitoring_async(
        self,
        request: arms20190808_models.ListPrometheusMonitoringRequest,
    ) -> arms20190808_models.ListPrometheusMonitoringResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_prometheus_monitoring_with_options_async(request, runtime)

    def list_prometheus_remote_writes_with_options(
        self,
        request: arms20190808_models.ListPrometheusRemoteWritesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPrometheusRemoteWritesResponse:
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
            action='ListPrometheusRemoteWrites',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusRemoteWritesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_prometheus_remote_writes_with_options_async(
        self,
        request: arms20190808_models.ListPrometheusRemoteWritesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListPrometheusRemoteWritesResponse:
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
            action='ListPrometheusRemoteWrites',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusRemoteWritesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_prometheus_remote_writes(
        self,
        request: arms20190808_models.ListPrometheusRemoteWritesRequest,
    ) -> arms20190808_models.ListPrometheusRemoteWritesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_remote_writes_with_options(request, runtime)

    async def list_prometheus_remote_writes_async(
        self,
        request: arms20190808_models.ListPrometheusRemoteWritesRequest,
    ) -> arms20190808_models.ListPrometheusRemoteWritesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_prometheus_remote_writes_with_options_async(request, runtime)

    def list_retcode_apps_with_options(
        self,
        request: arms20190808_models.ListRetcodeAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListRetcodeAppsResponse:
        """
        ***\
        
        @param request: ListRetcodeAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRetcodeAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        ***\
        
        @param request: ListRetcodeAppsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListRetcodeAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        """
        ***\
        
        @param request: ListRetcodeAppsRequest
        @return: ListRetcodeAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_retcode_apps_with_options(request, runtime)

    async def list_retcode_apps_async(
        self,
        request: arms20190808_models.ListRetcodeAppsRequest,
    ) -> arms20190808_models.ListRetcodeAppsResponse:
        """
        ***\
        
        @param request: ListRetcodeAppsRequest
        @return: ListRetcodeAppsResponse
        """
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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

    def list_synthetic_detail_with_options(
        self,
        tmp_req: arms20190808_models.ListSyntheticDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListSyntheticDetailResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.ListSyntheticDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.advanced_filters):
            request.advanced_filters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.advanced_filters, 'AdvancedFilters', 'json')
        if not UtilClient.is_unset(tmp_req.exact_filters):
            request.exact_filters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exact_filters, 'ExactFilters', 'json')
        if not UtilClient.is_unset(tmp_req.filters):
            request.filters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSyntheticDetail',
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
            arms20190808_models.ListSyntheticDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_synthetic_detail_with_options_async(
        self,
        tmp_req: arms20190808_models.ListSyntheticDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListSyntheticDetailResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.ListSyntheticDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.advanced_filters):
            request.advanced_filters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.advanced_filters, 'AdvancedFilters', 'json')
        if not UtilClient.is_unset(tmp_req.exact_filters):
            request.exact_filters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.exact_filters, 'ExactFilters', 'json')
        if not UtilClient.is_unset(tmp_req.filters):
            request.filters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSyntheticDetail',
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
            arms20190808_models.ListSyntheticDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_synthetic_detail(
        self,
        request: arms20190808_models.ListSyntheticDetailRequest,
    ) -> arms20190808_models.ListSyntheticDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_synthetic_detail_with_options(request, runtime)

    async def list_synthetic_detail_async(
        self,
        request: arms20190808_models.ListSyntheticDetailRequest,
    ) -> arms20190808_models.ListSyntheticDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_synthetic_detail_with_options_async(request, runtime)

    def list_timing_synthetic_tasks_with_options(
        self,
        tmp_req: arms20190808_models.ListTimingSyntheticTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListTimingSyntheticTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.ListTimingSyntheticTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.search):
            request.search_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.search, 'Search', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTimingSyntheticTasks',
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
            arms20190808_models.ListTimingSyntheticTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_timing_synthetic_tasks_with_options_async(
        self,
        tmp_req: arms20190808_models.ListTimingSyntheticTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListTimingSyntheticTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.ListTimingSyntheticTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.search):
            request.search_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.search, 'Search', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTimingSyntheticTasks',
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
            arms20190808_models.ListTimingSyntheticTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_timing_synthetic_tasks(
        self,
        request: arms20190808_models.ListTimingSyntheticTasksRequest,
    ) -> arms20190808_models.ListTimingSyntheticTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_timing_synthetic_tasks_with_options(request, runtime)

    async def list_timing_synthetic_tasks_async(
        self,
        request: arms20190808_models.ListTimingSyntheticTasksRequest,
    ) -> arms20190808_models.ListTimingSyntheticTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_timing_synthetic_tasks_with_options_async(request, runtime)

    def list_trace_apps_with_options(
        self,
        request: arms20190808_models.ListTraceAppsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.ListTraceAppsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
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
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
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

    def open_arms_service_second_version_with_options(
        self,
        request: arms20190808_models.OpenArmsServiceSecondVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.OpenArmsServiceSecondVersionResponse:
        """
        The *OpenArmsServiceSecondVersion** operation supports the following sub-service editions:
        *   Application Monitoring: Basic Edition
        *   Browser Monitoring: Basic Edition
        *   Synthetic Monitoring: Pro Edition (pay-as-you-go)
        *   Prometheus Service: Pro Edition
        
        @param request: OpenArmsServiceSecondVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenArmsServiceSecondVersionResponse
        """
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
        """
        The *OpenArmsServiceSecondVersion** operation supports the following sub-service editions:
        *   Application Monitoring: Basic Edition
        *   Browser Monitoring: Basic Edition
        *   Synthetic Monitoring: Pro Edition (pay-as-you-go)
        *   Prometheus Service: Pro Edition
        
        @param request: OpenArmsServiceSecondVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: OpenArmsServiceSecondVersionResponse
        """
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
        """
        The *OpenArmsServiceSecondVersion** operation supports the following sub-service editions:
        *   Application Monitoring: Basic Edition
        *   Browser Monitoring: Basic Edition
        *   Synthetic Monitoring: Pro Edition (pay-as-you-go)
        *   Prometheus Service: Pro Edition
        
        @param request: OpenArmsServiceSecondVersionRequest
        @return: OpenArmsServiceSecondVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.open_arms_service_second_version_with_options(request, runtime)

    async def open_arms_service_second_version_async(
        self,
        request: arms20190808_models.OpenArmsServiceSecondVersionRequest,
    ) -> arms20190808_models.OpenArmsServiceSecondVersionResponse:
        """
        The *OpenArmsServiceSecondVersion** operation supports the following sub-service editions:
        *   Application Monitoring: Basic Edition
        *   Browser Monitoring: Basic Edition
        *   Synthetic Monitoring: Pro Edition (pay-as-you-go)
        *   Prometheus Service: Pro Edition
        
        @param request: OpenArmsServiceSecondVersionRequest
        @return: OpenArmsServiceSecondVersionResponse
        """
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

    def query_app_metadata_with_options(
        self,
        request: arms20190808_models.QueryAppMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryAppMetadataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAppMetadata',
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
            arms20190808_models.QueryAppMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_app_metadata_with_options_async(
        self,
        request: arms20190808_models.QueryAppMetadataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryAppMetadataResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAppMetadata',
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
            arms20190808_models.QueryAppMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_app_metadata(
        self,
        request: arms20190808_models.QueryAppMetadataRequest,
    ) -> arms20190808_models.QueryAppMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_app_metadata_with_options(request, runtime)

    async def query_app_metadata_async(
        self,
        request: arms20190808_models.QueryAppMetadataRequest,
    ) -> arms20190808_models.QueryAppMetadataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_app_metadata_with_options_async(request, runtime)

    def query_app_topology_with_options(
        self,
        tmp_req: arms20190808_models.QueryAppTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryAppTopologyResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.QueryAppTopologyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filters):
            request.filters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.db):
            query['Db'] = request.db
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters_shrink):
            query['Filters'] = request.filters_shrink
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rpc):
            query['Rpc'] = request.rpc
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAppTopology',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.QueryAppTopologyResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_app_topology_with_options_async(
        self,
        tmp_req: arms20190808_models.QueryAppTopologyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryAppTopologyResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.QueryAppTopologyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filters):
            request.filters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.db):
            query['Db'] = request.db
        if not UtilClient.is_unset(request.db_name):
            query['DbName'] = request.db_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters_shrink):
            query['Filters'] = request.filters_shrink
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rpc):
            query['Rpc'] = request.rpc
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAppTopology',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.QueryAppTopologyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_app_topology(
        self,
        request: arms20190808_models.QueryAppTopologyRequest,
    ) -> arms20190808_models.QueryAppTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_app_topology_with_options(request, runtime)

    async def query_app_topology_async(
        self,
        request: arms20190808_models.QueryAppTopologyRequest,
    ) -> arms20190808_models.QueryAppTopologyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_app_topology_with_options_async(request, runtime)

    def query_commercial_usage_with_options(
        self,
        request: arms20190808_models.QueryCommercialUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryCommercialUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advanced_filters):
            query['AdvancedFilters'] = request.advanced_filters
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCommercialUsage',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.QueryCommercialUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_commercial_usage_with_options_async(
        self,
        request: arms20190808_models.QueryCommercialUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.QueryCommercialUsageResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.advanced_filters):
            query['AdvancedFilters'] = request.advanced_filters
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
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
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCommercialUsage',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.QueryCommercialUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_commercial_usage(
        self,
        request: arms20190808_models.QueryCommercialUsageRequest,
    ) -> arms20190808_models.QueryCommercialUsageResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_commercial_usage_with_options(request, runtime)

    async def query_commercial_usage_async(
        self,
        request: arms20190808_models.QueryCommercialUsageRequest,
    ) -> arms20190808_models.QueryCommercialUsageResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_commercial_usage_with_options_async(request, runtime)

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

    def restart_environment_feature_with_options(
        self,
        request: arms20190808_models.RestartEnvironmentFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.RestartEnvironmentFeatureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartEnvironmentFeature',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.RestartEnvironmentFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_environment_feature_with_options_async(
        self,
        request: arms20190808_models.RestartEnvironmentFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.RestartEnvironmentFeatureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartEnvironmentFeature',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.RestartEnvironmentFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_environment_feature(
        self,
        request: arms20190808_models.RestartEnvironmentFeatureRequest,
    ) -> arms20190808_models.RestartEnvironmentFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_environment_feature_with_options(request, runtime)

    async def restart_environment_feature_async(
        self,
        request: arms20190808_models.RestartEnvironmentFeatureRequest,
    ) -> arms20190808_models.RestartEnvironmentFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_environment_feature_with_options_async(request, runtime)

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
        """
        This operation is no longer maintained. To query alert contacts, call the DescribeContacts operation provided by the new version of Alert Management.
        
        @param request: SearchAlertContactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchAlertContactResponse
        """
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
        """
        This operation is no longer maintained. To query alert contacts, call the DescribeContacts operation provided by the new version of Alert Management.
        
        @param request: SearchAlertContactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchAlertContactResponse
        """
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
        """
        This operation is no longer maintained. To query alert contacts, call the DescribeContacts operation provided by the new version of Alert Management.
        
        @param request: SearchAlertContactRequest
        @return: SearchAlertContactResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_alert_contact_with_options(request, runtime)

    async def search_alert_contact_async(
        self,
        request: arms20190808_models.SearchAlertContactRequest,
    ) -> arms20190808_models.SearchAlertContactResponse:
        """
        This operation is no longer maintained. To query alert contacts, call the DescribeContacts operation provided by the new version of Alert Management.
        
        @param request: SearchAlertContactRequest
        @return: SearchAlertContactResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_contact_with_options_async(request, runtime)

    def search_alert_contact_group_with_options(
        self,
        request: arms20190808_models.SearchAlertContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertContactGroupResponse:
        """
        The operation is no longer maintained. Call the DescribeContactGroups operation in the alert management module to query alert contact groups.
        
        @param request: SearchAlertContactGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchAlertContactGroupResponse
        """
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
        """
        The operation is no longer maintained. Call the DescribeContactGroups operation in the alert management module to query alert contact groups.
        
        @param request: SearchAlertContactGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchAlertContactGroupResponse
        """
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
        """
        The operation is no longer maintained. Call the DescribeContactGroups operation in the alert management module to query alert contact groups.
        
        @param request: SearchAlertContactGroupRequest
        @return: SearchAlertContactGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_alert_contact_group_with_options(request, runtime)

    async def search_alert_contact_group_async(
        self,
        request: arms20190808_models.SearchAlertContactGroupRequest,
    ) -> arms20190808_models.SearchAlertContactGroupResponse:
        """
        The operation is no longer maintained. Call the DescribeContactGroups operation in the alert management module to query alert contact groups.
        
        @param request: SearchAlertContactGroupRequest
        @return: SearchAlertContactGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_contact_group_with_options_async(request, runtime)

    def search_alert_histories_with_options(
        self,
        request: arms20190808_models.SearchAlertHistoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertHistoriesResponse:
        """
        This operation is no longer maintained. To query alert records, call the ListAlerts operation provided by the new version of Alert Management.
        
        @param request: SearchAlertHistoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchAlertHistoriesResponse
        """
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
        """
        This operation is no longer maintained. To query alert records, call the ListAlerts operation provided by the new version of Alert Management.
        
        @param request: SearchAlertHistoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchAlertHistoriesResponse
        """
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
        """
        This operation is no longer maintained. To query alert records, call the ListAlerts operation provided by the new version of Alert Management.
        
        @param request: SearchAlertHistoriesRequest
        @return: SearchAlertHistoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_alert_histories_with_options(request, runtime)

    async def search_alert_histories_async(
        self,
        request: arms20190808_models.SearchAlertHistoriesRequest,
    ) -> arms20190808_models.SearchAlertHistoriesResponse:
        """
        This operation is no longer maintained. To query alert records, call the ListAlerts operation provided by the new version of Alert Management.
        
        @param request: SearchAlertHistoriesRequest
        @return: SearchAlertHistoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_histories_with_options_async(request, runtime)

    def search_alert_rules_with_options(
        self,
        request: arms20190808_models.SearchAlertRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchAlertRulesResponse:
        """
        The current operation is no longer maintained. You can call the GetAlertRules operation of Alert Management (New) to query existing alert rules.
        
        @param request: SearchAlertRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchAlertRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_rule_id):
            query['AlertRuleId'] = request.alert_rule_id
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.system_region_id):
            query['SystemRegionId'] = request.system_region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        """
        The current operation is no longer maintained. You can call the GetAlertRules operation of Alert Management (New) to query existing alert rules.
        
        @param request: SearchAlertRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchAlertRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_rule_id):
            query['AlertRuleId'] = request.alert_rule_id
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.system_region_id):
            query['SystemRegionId'] = request.system_region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        """
        The current operation is no longer maintained. You can call the GetAlertRules operation of Alert Management (New) to query existing alert rules.
        
        @param request: SearchAlertRulesRequest
        @return: SearchAlertRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_alert_rules_with_options(request, runtime)

    async def search_alert_rules_async(
        self,
        request: arms20190808_models.SearchAlertRulesRequest,
    ) -> arms20190808_models.SearchAlertRulesResponse:
        """
        The current operation is no longer maintained. You can call the GetAlertRules operation of Alert Management (New) to query existing alert rules.
        
        @param request: SearchAlertRulesRequest
        @return: SearchAlertRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.search_alert_rules_with_options_async(request, runtime)

    def search_events_with_options(
        self,
        request: arms20190808_models.SearchEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchEventsResponse:
        """
        Alert event records are different from alert notification records. Alert events are recorded every minute after an alert rule filters data. Alert events can be classified based on whether they are triggered or not. If a triggered event is not in the silence period, an alert notification is sent.
        
        @param request: SearchEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchEventsResponse
        """
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
        """
        Alert event records are different from alert notification records. Alert events are recorded every minute after an alert rule filters data. Alert events can be classified based on whether they are triggered or not. If a triggered event is not in the silence period, an alert notification is sent.
        
        @param request: SearchEventsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchEventsResponse
        """
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
        """
        Alert event records are different from alert notification records. Alert events are recorded every minute after an alert rule filters data. Alert events can be classified based on whether they are triggered or not. If a triggered event is not in the silence period, an alert notification is sent.
        
        @param request: SearchEventsRequest
        @return: SearchEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_events_with_options(request, runtime)

    async def search_events_async(
        self,
        request: arms20190808_models.SearchEventsRequest,
    ) -> arms20190808_models.SearchEventsResponse:
        """
        Alert event records are different from alert notification records. Alert events are recorded every minute after an alert rule filters data. Alert events can be classified based on whether they are triggered or not. If a triggered event is not in the silence period, an alert notification is sent.
        
        @param request: SearchEventsRequest
        @return: SearchEventsResponse
        """
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.retcode_app_id):
            query['RetcodeAppId'] = request.retcode_app_id
        if not UtilClient.is_unset(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.retcode_app_id):
            query['RetcodeAppId'] = request.retcode_app_id
        if not UtilClient.is_unset(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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

    def search_trace_app_by_name_with_options(
        self,
        request: arms20190808_models.SearchTraceAppByNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SearchTraceAppByNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        """
        > A maximum of 100 data entries can be returned each time this operation is called. If you want to query all existing traces, we recommend that you call the SearchTracesByPage operation. For more information, see [SearchTracesByPage](~~175866~~).
        
        @param request: SearchTracesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchTracesResponse
        """
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
        """
        > A maximum of 100 data entries can be returned each time this operation is called. If you want to query all existing traces, we recommend that you call the SearchTracesByPage operation. For more information, see [SearchTracesByPage](~~175866~~).
        
        @param request: SearchTracesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SearchTracesResponse
        """
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
        """
        > A maximum of 100 data entries can be returned each time this operation is called. If you want to query all existing traces, we recommend that you call the SearchTracesByPage operation. For more information, see [SearchTracesByPage](~~175866~~).
        
        @param request: SearchTracesRequest
        @return: SearchTracesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_traces_with_options(request, runtime)

    async def search_traces_async(
        self,
        request: arms20190808_models.SearchTracesRequest,
    ) -> arms20190808_models.SearchTracesResponse:
        """
        > A maximum of 100 data entries can be returned each time this operation is called. If you want to query all existing traces, we recommend that you call the SearchTracesByPage operation. For more information, see [SearchTracesByPage](~~175866~~).
        
        @param request: SearchTracesRequest
        @return: SearchTracesResponse
        """
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
        if not UtilClient.is_unset(request.is_error):
            query['IsError'] = request.is_error
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
        if not UtilClient.is_unset(request.is_error):
            query['IsError'] = request.is_error
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
        """
        After you receive the text message, verify the mobile number as prompted. Before you can specify a mobile phone number in a notification policy, you must verify the mobile phone number.
        
        @param request: SendTTSVerifyLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendTTSVerifyLinkResponse
        """
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
        """
        After you receive the text message, verify the mobile number as prompted. Before you can specify a mobile phone number in a notification policy, you must verify the mobile phone number.
        
        @param request: SendTTSVerifyLinkRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SendTTSVerifyLinkResponse
        """
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
        """
        After you receive the text message, verify the mobile number as prompted. Before you can specify a mobile phone number in a notification policy, you must verify the mobile phone number.
        
        @param request: SendTTSVerifyLinkRequest
        @return: SendTTSVerifyLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_ttsverify_link_with_options(request, runtime)

    async def send_ttsverify_link_async(
        self,
        request: arms20190808_models.SendTTSVerifyLinkRequest,
    ) -> arms20190808_models.SendTTSVerifyLinkResponse:
        """
        After you receive the text message, verify the mobile number as prompted. Before you can specify a mobile phone number in a notification policy, you must verify the mobile phone number.
        
        @param request: SendTTSVerifyLinkRequest
        @return: SendTTSVerifyLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.send_ttsverify_link_with_options_async(request, runtime)

    def set_retcode_share_status_with_options(
        self,
        request: arms20190808_models.SetRetcodeShareStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SetRetcodeShareStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
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
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
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

    def start_timing_synthetic_task_with_options(
        self,
        tmp_req: arms20190808_models.StartTimingSyntheticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.StartTimingSyntheticTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.StartTimingSyntheticTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_ids):
            request.task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartTimingSyntheticTask',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.StartTimingSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_timing_synthetic_task_with_options_async(
        self,
        tmp_req: arms20190808_models.StartTimingSyntheticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.StartTimingSyntheticTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.StartTimingSyntheticTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_ids):
            request.task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartTimingSyntheticTask',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.StartTimingSyntheticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_timing_synthetic_task(
        self,
        request: arms20190808_models.StartTimingSyntheticTaskRequest,
    ) -> arms20190808_models.StartTimingSyntheticTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_timing_synthetic_task_with_options(request, runtime)

    async def start_timing_synthetic_task_async(
        self,
        request: arms20190808_models.StartTimingSyntheticTaskRequest,
    ) -> arms20190808_models.StartTimingSyntheticTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_timing_synthetic_task_with_options_async(request, runtime)

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

    def stop_timing_synthetic_task_with_options(
        self,
        tmp_req: arms20190808_models.StopTimingSyntheticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.StopTimingSyntheticTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.StopTimingSyntheticTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_ids):
            request.task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopTimingSyntheticTask',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.StopTimingSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_timing_synthetic_task_with_options_async(
        self,
        tmp_req: arms20190808_models.StopTimingSyntheticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.StopTimingSyntheticTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.StopTimingSyntheticTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.task_ids):
            request.task_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.task_ids, 'TaskIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_ids_shrink):
            query['TaskIds'] = request.task_ids_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopTimingSyntheticTask',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.StopTimingSyntheticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_timing_synthetic_task(
        self,
        request: arms20190808_models.StopTimingSyntheticTaskRequest,
    ) -> arms20190808_models.StopTimingSyntheticTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_timing_synthetic_task_with_options(request, runtime)

    async def stop_timing_synthetic_task_async(
        self,
        request: arms20190808_models.StopTimingSyntheticTaskRequest,
    ) -> arms20190808_models.StopTimingSyntheticTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_timing_synthetic_task_with_options_async(request, runtime)

    def switch_synthetic_task_status_with_options(
        self,
        request: arms20190808_models.SwitchSyntheticTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SwitchSyntheticTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_status):
            query['SwitchStatus'] = request.switch_status
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchSyntheticTaskStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SwitchSyntheticTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_synthetic_task_status_with_options_async(
        self,
        request: arms20190808_models.SwitchSyntheticTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SwitchSyntheticTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_status):
            query['SwitchStatus'] = request.switch_status
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchSyntheticTaskStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SwitchSyntheticTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_synthetic_task_status(
        self,
        request: arms20190808_models.SwitchSyntheticTaskStatusRequest,
    ) -> arms20190808_models.SwitchSyntheticTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_synthetic_task_status_with_options(request, runtime)

    async def switch_synthetic_task_status_async(
        self,
        request: arms20190808_models.SwitchSyntheticTaskStatusRequest,
    ) -> arms20190808_models.SwitchSyntheticTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_synthetic_task_status_with_options_async(request, runtime)

    def sync_recording_rules_with_options(
        self,
        request: arms20190808_models.SyncRecordingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SyncRecordingRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.target_clusters):
            query['TargetClusters'] = request.target_clusters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncRecordingRules',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SyncRecordingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_recording_rules_with_options_async(
        self,
        request: arms20190808_models.SyncRecordingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.SyncRecordingRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.target_clusters):
            query['TargetClusters'] = request.target_clusters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncRecordingRules',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SyncRecordingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_recording_rules(
        self,
        request: arms20190808_models.SyncRecordingRulesRequest,
    ) -> arms20190808_models.SyncRecordingRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.sync_recording_rules_with_options(request, runtime)

    async def sync_recording_rules_async(
        self,
        request: arms20190808_models.SyncRecordingRulesRequest,
    ) -> arms20190808_models.SyncRecordingRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.sync_recording_rules_with_options_async(request, runtime)

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

    def uninstall_managed_prometheus_with_options(
        self,
        request: arms20190808_models.UninstallManagedPrometheusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UninstallManagedPrometheusResponse:
        """
        Make sure that the ASK cluster or ECS instance is monitored in Managed Service for Prometheus.
        
        @param request: UninstallManagedPrometheusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallManagedPrometheusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
        """
        Make sure that the ASK cluster or ECS instance is monitored in Managed Service for Prometheus.
        
        @param request: UninstallManagedPrometheusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UninstallManagedPrometheusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
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
        """
        Make sure that the ASK cluster or ECS instance is monitored in Managed Service for Prometheus.
        
        @param request: UninstallManagedPrometheusRequest
        @return: UninstallManagedPrometheusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.uninstall_managed_prometheus_with_options(request, runtime)

    async def uninstall_managed_prometheus_async(
        self,
        request: arms20190808_models.UninstallManagedPrometheusRequest,
    ) -> arms20190808_models.UninstallManagedPrometheusResponse:
        """
        Make sure that the ASK cluster or ECS instance is monitored in Managed Service for Prometheus.
        
        @param request: UninstallManagedPrometheusRequest
        @return: UninstallManagedPrometheusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.uninstall_managed_prometheus_with_options_async(request, runtime)

    def uninstall_prom_cluster_with_options(
        self,
        request: arms20190808_models.UninstallPromClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UninstallPromClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
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
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        """
        This operation is no longer maintained. To create or modify an alert contact, call the CreateOrUpdateContact operation provided by the new version of Alert Management.
        
        @param request: UpdateAlertContactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAlertContactResponse
        """
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
        """
        This operation is no longer maintained. To create or modify an alert contact, call the CreateOrUpdateContact operation provided by the new version of Alert Management.
        
        @param request: UpdateAlertContactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateAlertContactResponse
        """
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
        """
        This operation is no longer maintained. To create or modify an alert contact, call the CreateOrUpdateContact operation provided by the new version of Alert Management.
        
        @param request: UpdateAlertContactRequest
        @return: UpdateAlertContactResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_alert_contact_with_options(request, runtime)

    async def update_alert_contact_async(
        self,
        request: arms20190808_models.UpdateAlertContactRequest,
    ) -> arms20190808_models.UpdateAlertContactResponse:
        """
        This operation is no longer maintained. To create or modify an alert contact, call the CreateOrUpdateContact operation provided by the new version of Alert Management.
        
        @param request: UpdateAlertContactRequest
        @return: UpdateAlertContactResponse
        """
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

    def update_env_custom_job_with_options(
        self,
        request: arms20190808_models.UpdateEnvCustomJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateEnvCustomJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.custom_job_name):
            query['CustomJobName'] = request.custom_job_name
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnvCustomJob',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateEnvCustomJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_env_custom_job_with_options_async(
        self,
        request: arms20190808_models.UpdateEnvCustomJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateEnvCustomJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.custom_job_name):
            query['CustomJobName'] = request.custom_job_name
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnvCustomJob',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateEnvCustomJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_env_custom_job(
        self,
        request: arms20190808_models.UpdateEnvCustomJobRequest,
    ) -> arms20190808_models.UpdateEnvCustomJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_env_custom_job_with_options(request, runtime)

    async def update_env_custom_job_async(
        self,
        request: arms20190808_models.UpdateEnvCustomJobRequest,
    ) -> arms20190808_models.UpdateEnvCustomJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_env_custom_job_with_options_async(request, runtime)

    def update_env_pod_monitor_with_options(
        self,
        request: arms20190808_models.UpdateEnvPodMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateEnvPodMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.pod_monitor_name):
            query['PodMonitorName'] = request.pod_monitor_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnvPodMonitor',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateEnvPodMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_env_pod_monitor_with_options_async(
        self,
        request: arms20190808_models.UpdateEnvPodMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateEnvPodMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.pod_monitor_name):
            query['PodMonitorName'] = request.pod_monitor_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnvPodMonitor',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateEnvPodMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_env_pod_monitor(
        self,
        request: arms20190808_models.UpdateEnvPodMonitorRequest,
    ) -> arms20190808_models.UpdateEnvPodMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_env_pod_monitor_with_options(request, runtime)

    async def update_env_pod_monitor_async(
        self,
        request: arms20190808_models.UpdateEnvPodMonitorRequest,
    ) -> arms20190808_models.UpdateEnvPodMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_env_pod_monitor_with_options_async(request, runtime)

    def update_env_service_monitor_with_options(
        self,
        request: arms20190808_models.UpdateEnvServiceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateEnvServiceMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_monitor_name):
            query['ServiceMonitorName'] = request.service_monitor_name
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnvServiceMonitor',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateEnvServiceMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_env_service_monitor_with_options_async(
        self,
        request: arms20190808_models.UpdateEnvServiceMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateEnvServiceMonitorResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_monitor_name):
            query['ServiceMonitorName'] = request.service_monitor_name
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEnvServiceMonitor',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateEnvServiceMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_env_service_monitor(
        self,
        request: arms20190808_models.UpdateEnvServiceMonitorRequest,
    ) -> arms20190808_models.UpdateEnvServiceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_env_service_monitor_with_options(request, runtime)

    async def update_env_service_monitor_async(
        self,
        request: arms20190808_models.UpdateEnvServiceMonitorRequest,
    ) -> arms20190808_models.UpdateEnvServiceMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_env_service_monitor_with_options_async(request, runtime)

    def update_environment_with_options(
        self,
        request: arms20190808_models.UpdateEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.environment_name):
            query['EnvironmentName'] = request.environment_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnvironment',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_environment_with_options_async(
        self,
        request: arms20190808_models.UpdateEnvironmentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateEnvironmentResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.environment_name):
            query['EnvironmentName'] = request.environment_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnvironment',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateEnvironmentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_environment(
        self,
        request: arms20190808_models.UpdateEnvironmentRequest,
    ) -> arms20190808_models.UpdateEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_environment_with_options(request, runtime)

    async def update_environment_async(
        self,
        request: arms20190808_models.UpdateEnvironmentRequest,
    ) -> arms20190808_models.UpdateEnvironmentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_environment_with_options_async(request, runtime)

    def update_grafana_workspace_with_options(
        self,
        request: arms20190808_models.UpdateGrafanaWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateGrafanaWorkspaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not UtilClient.is_unset(request.grafana_workspace_name):
            query['GrafanaWorkspaceName'] = request.grafana_workspace_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGrafanaWorkspace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateGrafanaWorkspaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_grafana_workspace_with_options_async(
        self,
        request: arms20190808_models.UpdateGrafanaWorkspaceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateGrafanaWorkspaceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not UtilClient.is_unset(request.grafana_workspace_name):
            query['GrafanaWorkspaceName'] = request.grafana_workspace_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGrafanaWorkspace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateGrafanaWorkspaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_grafana_workspace(
        self,
        request: arms20190808_models.UpdateGrafanaWorkspaceRequest,
    ) -> arms20190808_models.UpdateGrafanaWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_grafana_workspace_with_options(request, runtime)

    async def update_grafana_workspace_async(
        self,
        request: arms20190808_models.UpdateGrafanaWorkspaceRequest,
    ) -> arms20190808_models.UpdateGrafanaWorkspaceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_grafana_workspace_with_options_async(request, runtime)

    def update_grafana_workspace_version_with_options(
        self,
        request: arms20190808_models.UpdateGrafanaWorkspaceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateGrafanaWorkspaceVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.grafana_version):
            query['GrafanaVersion'] = request.grafana_version
        if not UtilClient.is_unset(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGrafanaWorkspaceVersion',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateGrafanaWorkspaceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_grafana_workspace_version_with_options_async(
        self,
        request: arms20190808_models.UpdateGrafanaWorkspaceVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateGrafanaWorkspaceVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.grafana_version):
            query['GrafanaVersion'] = request.grafana_version
        if not UtilClient.is_unset(request.grafana_workspace_id):
            query['GrafanaWorkspaceId'] = request.grafana_workspace_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGrafanaWorkspaceVersion',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateGrafanaWorkspaceVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_grafana_workspace_version(
        self,
        request: arms20190808_models.UpdateGrafanaWorkspaceVersionRequest,
    ) -> arms20190808_models.UpdateGrafanaWorkspaceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_grafana_workspace_version_with_options(request, runtime)

    async def update_grafana_workspace_version_async(
        self,
        request: arms20190808_models.UpdateGrafanaWorkspaceVersionRequest,
    ) -> arms20190808_models.UpdateGrafanaWorkspaceVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_grafana_workspace_version_with_options_async(request, runtime)

    def update_integration_with_options(
        self,
        request: arms20190808_models.UpdateIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateIntegrationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_recover):
            body['AutoRecover'] = request.auto_recover
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.duplicate_key):
            body['DuplicateKey'] = request.duplicate_key
        if not UtilClient.is_unset(request.extended_field_redefine_rules):
            body['ExtendedFieldRedefineRules'] = request.extended_field_redefine_rules
        if not UtilClient.is_unset(request.field_redefine_rules):
            body['FieldRedefineRules'] = request.field_redefine_rules
        if not UtilClient.is_unset(request.initiative_recover_field):
            body['InitiativeRecoverField'] = request.initiative_recover_field
        if not UtilClient.is_unset(request.initiative_recover_value):
            body['InitiativeRecoverValue'] = request.initiative_recover_value
        if not UtilClient.is_unset(request.integration_id):
            body['IntegrationId'] = request.integration_id
        if not UtilClient.is_unset(request.integration_name):
            body['IntegrationName'] = request.integration_name
        if not UtilClient.is_unset(request.integration_product_type):
            body['IntegrationProductType'] = request.integration_product_type
        if not UtilClient.is_unset(request.liveness):
            body['Liveness'] = request.liveness
        if not UtilClient.is_unset(request.recover_time):
            body['RecoverTime'] = request.recover_time
        if not UtilClient.is_unset(request.stat):
            body['Stat'] = request.stat
        if not UtilClient.is_unset(request.state):
            body['State'] = request.state
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_integration_with_options_async(
        self,
        request: arms20190808_models.UpdateIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateIntegrationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_recover):
            body['AutoRecover'] = request.auto_recover
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.duplicate_key):
            body['DuplicateKey'] = request.duplicate_key
        if not UtilClient.is_unset(request.extended_field_redefine_rules):
            body['ExtendedFieldRedefineRules'] = request.extended_field_redefine_rules
        if not UtilClient.is_unset(request.field_redefine_rules):
            body['FieldRedefineRules'] = request.field_redefine_rules
        if not UtilClient.is_unset(request.initiative_recover_field):
            body['InitiativeRecoverField'] = request.initiative_recover_field
        if not UtilClient.is_unset(request.initiative_recover_value):
            body['InitiativeRecoverValue'] = request.initiative_recover_value
        if not UtilClient.is_unset(request.integration_id):
            body['IntegrationId'] = request.integration_id
        if not UtilClient.is_unset(request.integration_name):
            body['IntegrationName'] = request.integration_name
        if not UtilClient.is_unset(request.integration_product_type):
            body['IntegrationProductType'] = request.integration_product_type
        if not UtilClient.is_unset(request.liveness):
            body['Liveness'] = request.liveness
        if not UtilClient.is_unset(request.recover_time):
            body['RecoverTime'] = request.recover_time
        if not UtilClient.is_unset(request.stat):
            body['Stat'] = request.stat
        if not UtilClient.is_unset(request.state):
            body['State'] = request.state
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_integration(
        self,
        request: arms20190808_models.UpdateIntegrationRequest,
    ) -> arms20190808_models.UpdateIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_integration_with_options(request, runtime)

    async def update_integration_async(
        self,
        request: arms20190808_models.UpdateIntegrationRequest,
    ) -> arms20190808_models.UpdateIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_integration_with_options_async(request, runtime)

    def update_metric_drop_with_options(
        self,
        request: arms20190808_models.UpdateMetricDropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateMetricDropResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.metric_drop):
            query['MetricDrop'] = request.metric_drop
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMetricDrop',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateMetricDropResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_metric_drop_with_options_async(
        self,
        request: arms20190808_models.UpdateMetricDropRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateMetricDropResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.metric_drop):
            query['MetricDrop'] = request.metric_drop
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMetricDrop',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateMetricDropResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_metric_drop(
        self,
        request: arms20190808_models.UpdateMetricDropRequest,
    ) -> arms20190808_models.UpdateMetricDropResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_metric_drop_with_options(request, runtime)

    async def update_metric_drop_async(
        self,
        request: arms20190808_models.UpdateMetricDropRequest,
    ) -> arms20190808_models.UpdateMetricDropResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_metric_drop_with_options_async(request, runtime)

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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
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

    def update_prometheus_global_view_with_options(
        self,
        request: arms20190808_models.UpdatePrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdatePrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_sub_clusters_success):
            query['AllSubClustersSuccess'] = request.all_sub_clusters_success
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.most_region_id):
            query['MostRegionId'] = request.most_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sub_clusters_json):
            query['SubClustersJson'] = request.sub_clusters_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_global_view_with_options_async(
        self,
        request: arms20190808_models.UpdatePrometheusGlobalViewRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdatePrometheusGlobalViewResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_sub_clusters_success):
            query['AllSubClustersSuccess'] = request.all_sub_clusters_success
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.most_region_id):
            query['MostRegionId'] = request.most_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sub_clusters_json):
            query['SubClustersJson'] = request.sub_clusters_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusGlobalViewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_global_view(
        self,
        request: arms20190808_models.UpdatePrometheusGlobalViewRequest,
    ) -> arms20190808_models.UpdatePrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_prometheus_global_view_with_options(request, runtime)

    async def update_prometheus_global_view_async(
        self,
        request: arms20190808_models.UpdatePrometheusGlobalViewRequest,
    ) -> arms20190808_models.UpdatePrometheusGlobalViewResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_prometheus_global_view_with_options_async(request, runtime)

    def update_prometheus_integration_with_options(
        self,
        request: arms20190808_models.UpdatePrometheusIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdatePrometheusIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_integration_with_options_async(
        self,
        request: arms20190808_models.UpdatePrometheusIntegrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdatePrometheusIntegrationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusIntegrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_integration(
        self,
        request: arms20190808_models.UpdatePrometheusIntegrationRequest,
    ) -> arms20190808_models.UpdatePrometheusIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_prometheus_integration_with_options(request, runtime)

    async def update_prometheus_integration_async(
        self,
        request: arms20190808_models.UpdatePrometheusIntegrationRequest,
    ) -> arms20190808_models.UpdatePrometheusIntegrationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_prometheus_integration_with_options_async(request, runtime)

    def update_prometheus_monitoring_with_options(
        self,
        request: arms20190808_models.UpdatePrometheusMonitoringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdatePrometheusMonitoringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusMonitoring',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_monitoring_with_options_async(
        self,
        request: arms20190808_models.UpdatePrometheusMonitoringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdatePrometheusMonitoringResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusMonitoring',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusMonitoringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_monitoring(
        self,
        request: arms20190808_models.UpdatePrometheusMonitoringRequest,
    ) -> arms20190808_models.UpdatePrometheusMonitoringResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_prometheus_monitoring_with_options(request, runtime)

    async def update_prometheus_monitoring_async(
        self,
        request: arms20190808_models.UpdatePrometheusMonitoringRequest,
    ) -> arms20190808_models.UpdatePrometheusMonitoringResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_prometheus_monitoring_with_options_async(request, runtime)

    def update_prometheus_monitoring_status_with_options(
        self,
        request: arms20190808_models.UpdatePrometheusMonitoringStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdatePrometheusMonitoringStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
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
            action='UpdatePrometheusMonitoringStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusMonitoringStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_monitoring_status_with_options_async(
        self,
        request: arms20190808_models.UpdatePrometheusMonitoringStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdatePrometheusMonitoringStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
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
            action='UpdatePrometheusMonitoringStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusMonitoringStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_monitoring_status(
        self,
        request: arms20190808_models.UpdatePrometheusMonitoringStatusRequest,
    ) -> arms20190808_models.UpdatePrometheusMonitoringStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_prometheus_monitoring_status_with_options(request, runtime)

    async def update_prometheus_monitoring_status_async(
        self,
        request: arms20190808_models.UpdatePrometheusMonitoringStatusRequest,
    ) -> arms20190808_models.UpdatePrometheusMonitoringStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_prometheus_monitoring_status_with_options_async(request, runtime)

    def update_prometheus_remote_write_with_options(
        self,
        request: arms20190808_models.UpdatePrometheusRemoteWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdatePrometheusRemoteWriteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remote_write_name):
            query['RemoteWriteName'] = request.remote_write_name
        body = {}
        if not UtilClient.is_unset(request.remote_write_yaml):
            body['RemoteWriteYaml'] = request.remote_write_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusRemoteWrite',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusRemoteWriteResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_prometheus_remote_write_with_options_async(
        self,
        request: arms20190808_models.UpdatePrometheusRemoteWriteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdatePrometheusRemoteWriteResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remote_write_name):
            query['RemoteWriteName'] = request.remote_write_name
        body = {}
        if not UtilClient.is_unset(request.remote_write_yaml):
            body['RemoteWriteYaml'] = request.remote_write_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusRemoteWrite',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusRemoteWriteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_prometheus_remote_write(
        self,
        request: arms20190808_models.UpdatePrometheusRemoteWriteRequest,
    ) -> arms20190808_models.UpdatePrometheusRemoteWriteResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_prometheus_remote_write_with_options(request, runtime)

    async def update_prometheus_remote_write_async(
        self,
        request: arms20190808_models.UpdatePrometheusRemoteWriteRequest,
    ) -> arms20190808_models.UpdatePrometheusRemoteWriteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_prometheus_remote_write_with_options_async(request, runtime)

    def update_timing_synthetic_task_with_options(
        self,
        tmp_req: arms20190808_models.UpdateTimingSyntheticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateTimingSyntheticTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.UpdateTimingSyntheticTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.available_assertions):
            request.available_assertions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.available_assertions, 'AvailableAssertions', 'json')
        if not UtilClient.is_unset(tmp_req.common_setting):
            request.common_setting_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.common_setting, 'CommonSetting', 'json')
        if not UtilClient.is_unset(tmp_req.custom_period):
            request.custom_period_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_period, 'CustomPeriod', 'json')
        if not UtilClient.is_unset(tmp_req.monitor_conf):
            request.monitor_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.monitor_conf, 'MonitorConf', 'json')
        if not UtilClient.is_unset(tmp_req.monitors):
            request.monitors_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.monitors, 'Monitors', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.available_assertions_shrink):
            query['AvailableAssertions'] = request.available_assertions_shrink
        if not UtilClient.is_unset(request.common_setting_shrink):
            query['CommonSetting'] = request.common_setting_shrink
        if not UtilClient.is_unset(request.custom_period_shrink):
            query['CustomPeriod'] = request.custom_period_shrink
        if not UtilClient.is_unset(request.frequency):
            query['Frequency'] = request.frequency
        if not UtilClient.is_unset(request.monitor_conf_shrink):
            query['MonitorConf'] = request.monitor_conf_shrink
        if not UtilClient.is_unset(request.monitors_shrink):
            query['Monitors'] = request.monitors_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTimingSyntheticTask',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateTimingSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_timing_synthetic_task_with_options_async(
        self,
        tmp_req: arms20190808_models.UpdateTimingSyntheticTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateTimingSyntheticTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.UpdateTimingSyntheticTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.available_assertions):
            request.available_assertions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.available_assertions, 'AvailableAssertions', 'json')
        if not UtilClient.is_unset(tmp_req.common_setting):
            request.common_setting_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.common_setting, 'CommonSetting', 'json')
        if not UtilClient.is_unset(tmp_req.custom_period):
            request.custom_period_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.custom_period, 'CustomPeriod', 'json')
        if not UtilClient.is_unset(tmp_req.monitor_conf):
            request.monitor_conf_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.monitor_conf, 'MonitorConf', 'json')
        if not UtilClient.is_unset(tmp_req.monitors):
            request.monitors_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.monitors, 'Monitors', 'json')
        if not UtilClient.is_unset(tmp_req.tags):
            request.tags_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tags, 'Tags', 'json')
        query = {}
        if not UtilClient.is_unset(request.available_assertions_shrink):
            query['AvailableAssertions'] = request.available_assertions_shrink
        if not UtilClient.is_unset(request.common_setting_shrink):
            query['CommonSetting'] = request.common_setting_shrink
        if not UtilClient.is_unset(request.custom_period_shrink):
            query['CustomPeriod'] = request.custom_period_shrink
        if not UtilClient.is_unset(request.frequency):
            query['Frequency'] = request.frequency
        if not UtilClient.is_unset(request.monitor_conf_shrink):
            query['MonitorConf'] = request.monitor_conf_shrink
        if not UtilClient.is_unset(request.monitors_shrink):
            query['Monitors'] = request.monitors_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags_shrink):
            query['Tags'] = request.tags_shrink
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTimingSyntheticTask',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateTimingSyntheticTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_timing_synthetic_task(
        self,
        request: arms20190808_models.UpdateTimingSyntheticTaskRequest,
    ) -> arms20190808_models.UpdateTimingSyntheticTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_timing_synthetic_task_with_options(request, runtime)

    async def update_timing_synthetic_task_async(
        self,
        request: arms20190808_models.UpdateTimingSyntheticTaskRequest,
    ) -> arms20190808_models.UpdateTimingSyntheticTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_timing_synthetic_task_with_options_async(request, runtime)

    def update_webhook_with_options(
        self,
        request: arms20190808_models.UpdateWebhookRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpdateWebhookResponse:
        """
        This operation is no longer maintained. Call the CreateOrUpdateWebhookContact operation in the new alter management module to create or modify a webhook alert contact.
        
        @param request: UpdateWebhookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWebhookResponse
        """
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
        """
        This operation is no longer maintained. Call the CreateOrUpdateWebhookContact operation in the new alter management module to create or modify a webhook alert contact.
        
        @param request: UpdateWebhookRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateWebhookResponse
        """
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
        """
        This operation is no longer maintained. Call the CreateOrUpdateWebhookContact operation in the new alter management module to create or modify a webhook alert contact.
        
        @param request: UpdateWebhookRequest
        @return: UpdateWebhookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_webhook_with_options(request, runtime)

    async def update_webhook_async(
        self,
        request: arms20190808_models.UpdateWebhookRequest,
    ) -> arms20190808_models.UpdateWebhookResponse:
        """
        This operation is no longer maintained. Call the CreateOrUpdateWebhookContact operation in the new alter management module to create or modify a webhook alert contact.
        
        @param request: UpdateWebhookRequest
        @return: UpdateWebhookResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_webhook_with_options_async(request, runtime)

    def upgrade_addon_release_with_options(
        self,
        request: arms20190808_models.UpgradeAddonReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpgradeAddonReleaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.release_name):
            query['ReleaseName'] = request.release_name
        if not UtilClient.is_unset(request.values):
            query['Values'] = request.values
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeAddonRelease',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpgradeAddonReleaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_addon_release_with_options_async(
        self,
        request: arms20190808_models.UpgradeAddonReleaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpgradeAddonReleaseResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.addon_version):
            query['AddonVersion'] = request.addon_version
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.release_name):
            query['ReleaseName'] = request.release_name
        if not UtilClient.is_unset(request.values):
            query['Values'] = request.values
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeAddonRelease',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpgradeAddonReleaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_addon_release(
        self,
        request: arms20190808_models.UpgradeAddonReleaseRequest,
    ) -> arms20190808_models.UpgradeAddonReleaseResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_addon_release_with_options(request, runtime)

    async def upgrade_addon_release_async(
        self,
        request: arms20190808_models.UpgradeAddonReleaseRequest,
    ) -> arms20190808_models.UpgradeAddonReleaseResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_addon_release_with_options_async(request, runtime)

    def upgrade_environment_feature_with_options(
        self,
        request: arms20190808_models.UpgradeEnvironmentFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpgradeEnvironmentFeatureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.feature_version):
            query['FeatureVersion'] = request.feature_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.values):
            query['Values'] = request.values
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeEnvironmentFeature',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpgradeEnvironmentFeatureResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_environment_feature_with_options_async(
        self,
        request: arms20190808_models.UpgradeEnvironmentFeatureRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UpgradeEnvironmentFeatureResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_lang):
            query['AliyunLang'] = request.aliyun_lang
        if not UtilClient.is_unset(request.environment_id):
            query['EnvironmentId'] = request.environment_id
        if not UtilClient.is_unset(request.feature_name):
            query['FeatureName'] = request.feature_name
        if not UtilClient.is_unset(request.feature_version):
            query['FeatureVersion'] = request.feature_version
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.values):
            query['Values'] = request.values
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeEnvironmentFeature',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpgradeEnvironmentFeatureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_environment_feature(
        self,
        request: arms20190808_models.UpgradeEnvironmentFeatureRequest,
    ) -> arms20190808_models.UpgradeEnvironmentFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_environment_feature_with_options(request, runtime)

    async def upgrade_environment_feature_async(
        self,
        request: arms20190808_models.UpgradeEnvironmentFeatureRequest,
    ) -> arms20190808_models.UpgradeEnvironmentFeatureResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_environment_feature_with_options_async(request, runtime)

    def upload_with_options(
        self,
        request: arms20190808_models.UploadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> arms20190808_models.UploadResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.edition):
            query['Edition'] = request.edition
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        body = {}
        if not UtilClient.is_unset(request.file):
            body['File'] = request.file
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        if not UtilClient.is_unset(request.edition):
            query['Edition'] = request.edition
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        body = {}
        if not UtilClient.is_unset(request.file):
            body['File'] = request.file
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
