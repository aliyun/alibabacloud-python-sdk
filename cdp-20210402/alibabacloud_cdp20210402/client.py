# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cdp20210402 import models as cdp_20210402_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('cdp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_order_with_options(
        self,
        request: cdp_20210402_models.CancelOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.CancelOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelOrder',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/order/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.CancelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_order_with_options_async(
        self,
        request: cdp_20210402_models.CancelOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.CancelOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelOrder',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/order/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.CancelOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_order(
        self,
        request: cdp_20210402_models.CancelOrderRequest,
    ) -> cdp_20210402_models.CancelOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_order_with_options(request, headers, runtime)

    async def cancel_order_async(
        self,
        request: cdp_20210402_models.CancelOrderRequest,
    ) -> cdp_20210402_models.CancelOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_order_with_options_async(request, headers, runtime)

    def check_cluster_name_with_options(
        self,
        request: cdp_20210402_models.CheckClusterNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.CheckClusterNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckClusterName',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/check/cluster_name',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.CheckClusterNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_cluster_name_with_options_async(
        self,
        request: cdp_20210402_models.CheckClusterNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.CheckClusterNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckClusterName',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/check/cluster_name',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.CheckClusterNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_cluster_name(
        self,
        request: cdp_20210402_models.CheckClusterNameRequest,
    ) -> cdp_20210402_models.CheckClusterNameResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_cluster_name_with_options(request, headers, runtime)

    async def check_cluster_name_async(
        self,
        request: cdp_20210402_models.CheckClusterNameRequest,
    ) -> cdp_20210402_models.CheckClusterNameResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_cluster_name_with_options_async(request, headers, runtime)

    def confirm_notice_with_options(
        self,
        request: cdp_20210402_models.ConfirmNoticeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ConfirmNoticeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmNotice',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/confirm_notice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ConfirmNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_notice_with_options_async(
        self,
        request: cdp_20210402_models.ConfirmNoticeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ConfirmNoticeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmNotice',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/confirm_notice',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ConfirmNoticeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_notice(
        self,
        request: cdp_20210402_models.ConfirmNoticeRequest,
    ) -> cdp_20210402_models.ConfirmNoticeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.confirm_notice_with_options(request, headers, runtime)

    async def confirm_notice_async(
        self,
        request: cdp_20210402_models.ConfirmNoticeRequest,
    ) -> cdp_20210402_models.ConfirmNoticeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.confirm_notice_with_options_async(request, headers, runtime)

    def create_cluster_with_options(
        self,
        request: cdp_20210402_models.CreateClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_info):
            query['ClusterInfo'] = request.cluster_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        request: cdp_20210402_models.CreateClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.CreateClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_info):
            query['ClusterInfo'] = request.cluster_info
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: cdp_20210402_models.CreateClusterRequest,
    ) -> cdp_20210402_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_cluster_with_options(request, headers, runtime)

    async def create_cluster_async(
        self,
        request: cdp_20210402_models.CreateClusterRequest,
    ) -> cdp_20210402_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_cluster_with_options_async(request, headers, runtime)

    def get_cluster_detail_with_options(
        self,
        request: cdp_20210402_models.GetClusterDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.GetClusterDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterDetail',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.GetClusterDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_detail_with_options_async(
        self,
        request: cdp_20210402_models.GetClusterDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.GetClusterDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterDetail',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.GetClusterDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_detail(
        self,
        request: cdp_20210402_models.GetClusterDetailRequest,
    ) -> cdp_20210402_models.GetClusterDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_cluster_detail_with_options(request, headers, runtime)

    async def get_cluster_detail_async(
        self,
        request: cdp_20210402_models.GetClusterDetailRequest,
    ) -> cdp_20210402_models.GetClusterDetailResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_cluster_detail_with_options_async(request, headers, runtime)

    def has_default_role_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.HasDefaultRoleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='HasDefaultRole',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/user/has_default_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.HasDefaultRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def has_default_role_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.HasDefaultRoleResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='HasDefaultRole',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/user/has_default_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.HasDefaultRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def has_default_role(self) -> cdp_20210402_models.HasDefaultRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.has_default_role_with_options(headers, runtime)

    async def has_default_role_async(self) -> cdp_20210402_models.HasDefaultRoleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.has_default_role_with_options_async(headers, runtime)

    def initialize_cloudera_data_platform_with_options(
        self,
        client_token: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.InitializeClouderaDataPlatformResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='InitializeClouderaDataPlatform',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/user/create_default_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.InitializeClouderaDataPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_cloudera_data_platform_with_options_async(
        self,
        client_token: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.InitializeClouderaDataPlatformResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='InitializeClouderaDataPlatform',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/user/create_default_role',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.InitializeClouderaDataPlatformResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize_cloudera_data_platform(
        self,
        client_token: str,
    ) -> cdp_20210402_models.InitializeClouderaDataPlatformResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.initialize_cloudera_data_platform_with_options(client_token, headers, runtime)

    async def initialize_cloudera_data_platform_async(
        self,
        client_token: str,
    ) -> cdp_20210402_models.InitializeClouderaDataPlatformResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.initialize_cloudera_data_platform_with_options_async(client_token, headers, runtime)

    def list_default_components_with_options(
        self,
        request: cdp_20210402_models.ListDefaultComponentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ListDefaultComponentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.security_mode):
            query['SecurityMode'] = request.security_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDefaultComponents',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cdp/defaultComponents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListDefaultComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_default_components_with_options_async(
        self,
        request: cdp_20210402_models.ListDefaultComponentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ListDefaultComponentsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.security_mode):
            query['SecurityMode'] = request.security_mode
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDefaultComponents',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cdp/defaultComponents',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListDefaultComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_default_components(
        self,
        request: cdp_20210402_models.ListDefaultComponentsRequest,
    ) -> cdp_20210402_models.ListDefaultComponentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_default_components_with_options(request, headers, runtime)

    async def list_default_components_async(
        self,
        request: cdp_20210402_models.ListDefaultComponentsRequest,
    ) -> cdp_20210402_models.ListDefaultComponentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_default_components_with_options_async(request, headers, runtime)

    def list_node_group_constraints_with_options(
        self,
        request: cdp_20210402_models.ListNodeGroupConstraintsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ListNodeGroupConstraintsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeGroupConstraints',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cdp/nodeGroupConstraints',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListNodeGroupConstraintsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_group_constraints_with_options_async(
        self,
        request: cdp_20210402_models.ListNodeGroupConstraintsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ListNodeGroupConstraintsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeGroupConstraints',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cdp/nodeGroupConstraints',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListNodeGroupConstraintsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_group_constraints(
        self,
        request: cdp_20210402_models.ListNodeGroupConstraintsRequest,
    ) -> cdp_20210402_models.ListNodeGroupConstraintsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_node_group_constraints_with_options(request, headers, runtime)

    async def list_node_group_constraints_async(
        self,
        request: cdp_20210402_models.ListNodeGroupConstraintsRequest,
    ) -> cdp_20210402_models.ListNodeGroupConstraintsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_node_group_constraints_with_options_async(request, headers, runtime)

    def list_nodes_with_options(
        self,
        request: cdp_20210402_models.ListNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ListNodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/nodes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        request: cdp_20210402_models.ListNodesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ListNodesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/nodes',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: cdp_20210402_models.ListNodesRequest,
    ) -> cdp_20210402_models.ListNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_nodes_with_options(request, headers, runtime)

    async def list_nodes_async(
        self,
        request: cdp_20210402_models.ListNodesRequest,
    ) -> cdp_20210402_models.ListNodesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_nodes_with_options_async(request, headers, runtime)

    def list_operations_with_options(
        self,
        request: cdp_20210402_models.ListOperationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ListOperationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.parent_operation_node_id):
            query['ParentOperationNodeId'] = request.parent_operation_node_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOperations',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/operations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_operations_with_options_async(
        self,
        request: cdp_20210402_models.ListOperationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ListOperationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.parent_operation_node_id):
            query['ParentOperationNodeId'] = request.parent_operation_node_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOperations',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/operations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListOperationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_operations(
        self,
        request: cdp_20210402_models.ListOperationsRequest,
    ) -> cdp_20210402_models.ListOperationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_operations_with_options(request, headers, runtime)

    async def list_operations_async(
        self,
        request: cdp_20210402_models.ListOperationsRequest,
    ) -> cdp_20210402_models.ListOperationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_operations_with_options_async(request, headers, runtime)

    def list_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/region/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ListRegionsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRegions',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/region/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> cdp_20210402_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_regions_with_options(headers, runtime)

    async def list_regions_async(self) -> cdp_20210402_models.ListRegionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_regions_with_options_async(headers, runtime)

    def list_zones_with_options(
        self,
        request: cdp_20210402_models.ListZonesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ListZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListZones',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/user/zones',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_zones_with_options_async(
        self,
        request: cdp_20210402_models.ListZonesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ListZonesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListZones',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/user/zones',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ListZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_zones(
        self,
        request: cdp_20210402_models.ListZonesRequest,
    ) -> cdp_20210402_models.ListZonesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_zones_with_options(request, headers, runtime)

    async def list_zones_async(
        self,
        request: cdp_20210402_models.ListZonesRequest,
    ) -> cdp_20210402_models.ListZonesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_zones_with_options_async(request, headers, runtime)

    def query_order_with_options(
        self,
        request: cdp_20210402_models.QueryOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.QueryOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrder',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/order/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_order_with_options_async(
        self,
        request: cdp_20210402_models.QueryOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.QueryOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOrder',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/order/query',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_order(
        self,
        request: cdp_20210402_models.QueryOrderRequest,
    ) -> cdp_20210402_models.QueryOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_order_with_options(request, headers, runtime)

    async def query_order_async(
        self,
        request: cdp_20210402_models.QueryOrderRequest,
    ) -> cdp_20210402_models.QueryOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_order_with_options_async(request, headers, runtime)

    def query_price_with_options(
        self,
        request: cdp_20210402_models.QueryPriceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.QueryPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_specs):
            query['NodeGroupSpecs'] = request.node_group_specs
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPrice',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/buy/query_price',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_price_with_options_async(
        self,
        request: cdp_20210402_models.QueryPriceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.QueryPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.node_group_specs):
            query['NodeGroupSpecs'] = request.node_group_specs
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPrice',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/buy/query_price',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_price(
        self,
        request: cdp_20210402_models.QueryPriceRequest,
    ) -> cdp_20210402_models.QueryPriceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_price_with_options(request, headers, runtime)

    async def query_price_async(
        self,
        request: cdp_20210402_models.QueryPriceRequest,
    ) -> cdp_20210402_models.QueryPriceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_price_with_options_async(request, headers, runtime)

    def query_renew_order_with_options(
        self,
        request: cdp_20210402_models.QueryRenewOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.QueryRenewOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRenewOrder',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/order/query_renew_order',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryRenewOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_renew_order_with_options_async(
        self,
        request: cdp_20210402_models.QueryRenewOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.QueryRenewOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRenewOrder',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/order/query_renew_order',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryRenewOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_renew_order(
        self,
        request: cdp_20210402_models.QueryRenewOrderRequest,
    ) -> cdp_20210402_models.QueryRenewOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_renew_order_with_options(request, headers, runtime)

    async def query_renew_order_async(
        self,
        request: cdp_20210402_models.QueryRenewOrderRequest,
    ) -> cdp_20210402_models.QueryRenewOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_renew_order_with_options_async(request, headers, runtime)

    def query_renew_price_with_options(
        self,
        request: cdp_20210402_models.QueryRenewPriceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.QueryRenewPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRenewPrice',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/buy/query_renew_price',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryRenewPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_renew_price_with_options_async(
        self,
        request: cdp_20210402_models.QueryRenewPriceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.QueryRenewPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRenewPrice',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/buy/query_renew_price',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryRenewPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_renew_price(
        self,
        request: cdp_20210402_models.QueryRenewPriceRequest,
    ) -> cdp_20210402_models.QueryRenewPriceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_renew_price_with_options(request, headers, runtime)

    async def query_renew_price_async(
        self,
        request: cdp_20210402_models.QueryRenewPriceRequest,
    ) -> cdp_20210402_models.QueryRenewPriceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_renew_price_with_options_async(request, headers, runtime)

    def query_scale_up_order_with_options(
        self,
        request: cdp_20210402_models.QueryScaleUpOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.QueryScaleUpOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryScaleUpOrder',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/order/query_scale_up_order',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryScaleUpOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_scale_up_order_with_options_async(
        self,
        request: cdp_20210402_models.QueryScaleUpOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.QueryScaleUpOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryScaleUpOrder',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/order/query_scale_up_order',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryScaleUpOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_scale_up_order(
        self,
        request: cdp_20210402_models.QueryScaleUpOrderRequest,
    ) -> cdp_20210402_models.QueryScaleUpOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_scale_up_order_with_options(request, headers, runtime)

    async def query_scale_up_order_async(
        self,
        request: cdp_20210402_models.QueryScaleUpOrderRequest,
    ) -> cdp_20210402_models.QueryScaleUpOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_scale_up_order_with_options_async(request, headers, runtime)

    def query_scale_up_price_with_options(
        self,
        request: cdp_20210402_models.QueryScaleUpPriceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.QueryScaleUpPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.core_number):
            query['CoreNumber'] = request.core_number
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.node_group_type):
            query['NodeGroupType'] = request.node_group_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryScaleUpPrice',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/buy/query_scale_up_price',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryScaleUpPriceResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_scale_up_price_with_options_async(
        self,
        request: cdp_20210402_models.QueryScaleUpPriceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.QueryScaleUpPriceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.core_number):
            query['CoreNumber'] = request.core_number
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.node_group_type):
            query['NodeGroupType'] = request.node_group_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryScaleUpPrice',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/buy/query_scale_up_price',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.QueryScaleUpPriceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_scale_up_price(
        self,
        request: cdp_20210402_models.QueryScaleUpPriceRequest,
    ) -> cdp_20210402_models.QueryScaleUpPriceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.query_scale_up_price_with_options(request, headers, runtime)

    async def query_scale_up_price_async(
        self,
        request: cdp_20210402_models.QueryScaleUpPriceRequest,
    ) -> cdp_20210402_models.QueryScaleUpPriceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.query_scale_up_price_with_options_async(request, headers, runtime)

    def release_cluster_with_options(
        self,
        request: cdp_20210402_models.ReleaseClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ReleaseClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseCluster',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/release',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ReleaseClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_cluster_with_options_async(
        self,
        request: cdp_20210402_models.ReleaseClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ReleaseClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseCluster',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/release',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ReleaseClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_cluster(
        self,
        request: cdp_20210402_models.ReleaseClusterRequest,
    ) -> cdp_20210402_models.ReleaseClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.release_cluster_with_options(request, headers, runtime)

    async def release_cluster_async(
        self,
        request: cdp_20210402_models.ReleaseClusterRequest,
    ) -> cdp_20210402_models.ReleaseClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.release_cluster_with_options_async(request, headers, runtime)

    def renew_instance_with_options(
        self,
        request: cdp_20210402_models.RenewInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/order/renew_instance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: cdp_20210402_models.RenewInstanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.instances):
            query['Instances'] = request.instances
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/order/renew_instance',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        request: cdp_20210402_models.RenewInstanceRequest,
    ) -> cdp_20210402_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.renew_instance_with_options(request, headers, runtime)

    async def renew_instance_async(
        self,
        request: cdp_20210402_models.RenewInstanceRequest,
    ) -> cdp_20210402_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.renew_instance_with_options_async(request, headers, runtime)

    def scale_up_cluster_with_options(
        self,
        request: cdp_20210402_models.ScaleUpClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ScaleUpClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.core_number):
            query['CoreNumber'] = request.core_number
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.node_group_type):
            query['NodeGroupType'] = request.node_group_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleUpCluster',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/scale_up',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ScaleUpClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def scale_up_cluster_with_options_async(
        self,
        request: cdp_20210402_models.ScaleUpClusterRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.ScaleUpClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.core_number):
            query['CoreNumber'] = request.core_number
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.node_group_type):
            query['NodeGroupType'] = request.node_group_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleUpCluster',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/scale_up',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.ScaleUpClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def scale_up_cluster(
        self,
        request: cdp_20210402_models.ScaleUpClusterRequest,
    ) -> cdp_20210402_models.ScaleUpClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.scale_up_cluster_with_options(request, headers, runtime)

    async def scale_up_cluster_async(
        self,
        request: cdp_20210402_models.ScaleUpClusterRequest,
    ) -> cdp_20210402_models.ScaleUpClusterResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.scale_up_cluster_with_options_async(request, headers, runtime)

    def search_cluster_instances_with_options(
        self,
        request: cdp_20210402_models.SearchClusterInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.SearchClusterInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchClusterInstances',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/order/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.SearchClusterInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_cluster_instances_with_options_async(
        self,
        request: cdp_20210402_models.SearchClusterInstancesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.SearchClusterInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchClusterInstances',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/order/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.SearchClusterInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_cluster_instances(
        self,
        request: cdp_20210402_models.SearchClusterInstancesRequest,
    ) -> cdp_20210402_models.SearchClusterInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.search_cluster_instances_with_options(request, headers, runtime)

    async def search_cluster_instances_async(
        self,
        request: cdp_20210402_models.SearchClusterInstancesRequest,
    ) -> cdp_20210402_models.SearchClusterInstancesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.search_cluster_instances_with_options_async(request, headers, runtime)

    def single_order_with_options(
        self,
        request: cdp_20210402_models.SingleOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.SingleOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SingleOrder',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/order/single',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.SingleOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def single_order_with_options_async(
        self,
        request: cdp_20210402_models.SingleOrderRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.SingleOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SingleOrder',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/order/single',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.SingleOrderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def single_order(
        self,
        request: cdp_20210402_models.SingleOrderRequest,
    ) -> cdp_20210402_models.SingleOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.single_order_with_options(request, headers, runtime)

    async def single_order_async(
        self,
        request: cdp_20210402_models.SingleOrderRequest,
    ) -> cdp_20210402_models.SingleOrderResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.single_order_with_options_async(request, headers, runtime)

    def update_cluster_name_with_options(
        self,
        request: cdp_20210402_models.UpdateClusterNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.UpdateClusterNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClusterName',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/update_name',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.UpdateClusterNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_name_with_options_async(
        self,
        request: cdp_20210402_models.UpdateClusterNameRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.UpdateClusterNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClusterName',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/cluster/update_name',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.UpdateClusterNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster_name(
        self,
        request: cdp_20210402_models.UpdateClusterNameRequest,
    ) -> cdp_20210402_models.UpdateClusterNameResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_cluster_name_with_options(request, headers, runtime)

    async def update_cluster_name_async(
        self,
        request: cdp_20210402_models.UpdateClusterNameRequest,
    ) -> cdp_20210402_models.UpdateClusterNameResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_cluster_name_with_options_async(request, headers, runtime)

    def upload_license_with_options(
        self,
        region_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.UploadLicenseResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UploadLicense',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/user/upload',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.UploadLicenseResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_license_with_options_async(
        self,
        region_id: str,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> cdp_20210402_models.UploadLicenseResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UploadLicense',
            version='2021-04-02',
            protocol='HTTPS',
            pathname=f'/webapi/user/upload',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            cdp_20210402_models.UploadLicenseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_license(
        self,
        region_id: str,
    ) -> cdp_20210402_models.UploadLicenseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upload_license_with_options(region_id, headers, runtime)

    async def upload_license_async(
        self,
        region_id: str,
    ) -> cdp_20210402_models.UploadLicenseResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upload_license_with_options_async(region_id, headers, runtime)
