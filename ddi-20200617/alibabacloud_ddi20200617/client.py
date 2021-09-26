# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ddi20200617 import models as ddi_20200617_models
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
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'cn-qingdao': 'ddi.cn-qingdao.aliyuncs.com',
            'cn-chengdu': 'ddi.cn-chengdu.aliyuncs.com',
            'cn-zhangjiakou': 'ddi.cn-zhangjiakou.aliyuncs.com',
            'cn-huhehaote': 'ddi.cn-huhehaote.aliyuncs.com',
            'cn-hongkong': 'ddi.cn-hongkong.aliyuncs.com',
            'ap-southeast-2': 'ddi.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'ddi.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'ddi.ap-southeast-5.aliyuncs.com',
            'ap-northeast-1': 'ddi.ap-northeast-1.aliyuncs.com',
            'eu-west-1': 'ddi.eu-west-1.aliyuncs.com',
            'us-east-1': 'ddi.us-east-1.aliyuncs.com',
            'eu-central-1': 'ddi.eu-central-1.aliyuncs.com',
            'me-east-1': 'ddi.me-east-1.aliyuncs.com',
            'ap-south-1': 'ddi.ap-south-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('ddi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_flow_with_options(
        self,
        request: ddi_20200617_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowResponse(),
            self.do_rpcrequest('CreateFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_with_options_async(
        self,
        request: ddi_20200617_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowResponse(),
            await self.do_rpcrequest_async('CreateFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow(
        self,
        request: ddi_20200617_models.CreateFlowRequest,
    ) -> ddi_20200617_models.CreateFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_with_options(request, runtime)

    async def create_flow_async(
        self,
        request: ddi_20200617_models.CreateFlowRequest,
    ) -> ddi_20200617_models.CreateFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: ddi_20200617_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListUsersResponse(),
            self.do_rpcrequest('ListUsers', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: ddi_20200617_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListUsersResponse(),
            await self.do_rpcrequest_async('ListUsers', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users(
        self,
        request: ddi_20200617_models.ListUsersRequest,
    ) -> ddi_20200617_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: ddi_20200617_models.ListUsersRequest,
    ) -> ddi_20200617_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def modify_flow_project_with_options(
        self,
        request: ddi_20200617_models.ModifyFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowProjectResponse(),
            self.do_rpcrequest('ModifyFlowProject', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_flow_project_with_options_async(
        self,
        request: ddi_20200617_models.ModifyFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowProjectResponse(),
            await self.do_rpcrequest_async('ModifyFlowProject', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_project(
        self,
        request: ddi_20200617_models.ModifyFlowProjectRequest,
    ) -> ddi_20200617_models.ModifyFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_project_with_options(request, runtime)

    async def modify_flow_project_async(
        self,
        request: ddi_20200617_models.ModifyFlowProjectRequest,
    ) -> ddi_20200617_models.ModifyFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_project_with_options_async(request, runtime)

    def query_knox_user_password_with_options(
        self,
        request: ddi_20200617_models.QueryKnoxUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.QueryKnoxUserPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.QueryKnoxUserPasswordResponse(),
            self.do_rpcrequest('QueryKnoxUserPassword', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_knox_user_password_with_options_async(
        self,
        request: ddi_20200617_models.QueryKnoxUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.QueryKnoxUserPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.QueryKnoxUserPasswordResponse(),
            await self.do_rpcrequest_async('QueryKnoxUserPassword', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_knox_user_password(
        self,
        request: ddi_20200617_models.QueryKnoxUserPasswordRequest,
    ) -> ddi_20200617_models.QueryKnoxUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_knox_user_password_with_options(request, runtime)

    async def query_knox_user_password_async(
        self,
        request: ddi_20200617_models.QueryKnoxUserPasswordRequest,
    ) -> ddi_20200617_models.QueryKnoxUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_knox_user_password_with_options_async(request, runtime)

    def describe_flow_node_instance_launcher_log_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceLauncherLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceLauncherLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowNodeInstanceLauncherLogResponse(),
            self.do_rpcrequest('DescribeFlowNodeInstanceLauncherLog', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_node_instance_launcher_log_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceLauncherLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceLauncherLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowNodeInstanceLauncherLogResponse(),
            await self.do_rpcrequest_async('DescribeFlowNodeInstanceLauncherLog', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_node_instance_launcher_log(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceLauncherLogRequest,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceLauncherLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_node_instance_launcher_log_with_options(request, runtime)

    async def describe_flow_node_instance_launcher_log_async(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceLauncherLogRequest,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceLauncherLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_node_instance_launcher_log_with_options_async(request, runtime)

    def list_flow_with_options(
        self,
        request: ddi_20200617_models.ListFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowResponse(),
            self.do_rpcrequest('ListFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowResponse(),
            await self.do_rpcrequest_async('ListFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow(
        self,
        request: ddi_20200617_models.ListFlowRequest,
    ) -> ddi_20200617_models.ListFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_with_options(request, runtime)

    async def list_flow_async(
        self,
        request: ddi_20200617_models.ListFlowRequest,
    ) -> ddi_20200617_models.ListFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ddi_20200617_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ddi_20200617_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.UntagResourcesResponse(),
            await self.do_rpcrequest_async('UntagResources', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: ddi_20200617_models.UntagResourcesRequest,
    ) -> ddi_20200617_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ddi_20200617_models.UntagResourcesRequest,
    ) -> ddi_20200617_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def list_flow_cluster_host_with_options(
        self,
        request: ddi_20200617_models.ListFlowClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterHostResponse(),
            self.do_rpcrequest('ListFlowClusterHost', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_cluster_host_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterHostResponse(),
            await self.do_rpcrequest_async('ListFlowClusterHost', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_cluster_host(
        self,
        request: ddi_20200617_models.ListFlowClusterHostRequest,
    ) -> ddi_20200617_models.ListFlowClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_cluster_host_with_options(request, runtime)

    async def list_flow_cluster_host_async(
        self,
        request: ddi_20200617_models.ListFlowClusterHostRequest,
    ) -> ddi_20200617_models.ListFlowClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_cluster_host_with_options_async(request, runtime)

    def list_cluster_operation_with_options(
        self,
        request: ddi_20200617_models.ListClusterOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClusterOperationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterOperationResponse(),
            self.do_rpcrequest('ListClusterOperation', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_operation_with_options_async(
        self,
        request: ddi_20200617_models.ListClusterOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClusterOperationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterOperationResponse(),
            await self.do_rpcrequest_async('ListClusterOperation', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_operation(
        self,
        request: ddi_20200617_models.ListClusterOperationRequest,
    ) -> ddi_20200617_models.ListClusterOperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_operation_with_options(request, runtime)

    async def list_cluster_operation_async(
        self,
        request: ddi_20200617_models.ListClusterOperationRequest,
    ) -> ddi_20200617_models.ListClusterOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_operation_with_options_async(request, runtime)

    def list_flow_entity_snapshot_with_options(
        self,
        request: ddi_20200617_models.ListFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowEntitySnapshotResponse(),
            self.do_rpcrequest('ListFlowEntitySnapshot', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_entity_snapshot_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowEntitySnapshotResponse(),
            await self.do_rpcrequest_async('ListFlowEntitySnapshot', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_entity_snapshot(
        self,
        request: ddi_20200617_models.ListFlowEntitySnapshotRequest,
    ) -> ddi_20200617_models.ListFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_entity_snapshot_with_options(request, runtime)

    async def list_flow_entity_snapshot_async(
        self,
        request: ddi_20200617_models.ListFlowEntitySnapshotRequest,
    ) -> ddi_20200617_models.ListFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_entity_snapshot_with_options_async(request, runtime)

    def delete_cluster_template_with_options(
        self,
        request: ddi_20200617_models.DeleteClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteClusterTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteClusterTemplateResponse(),
            self.do_rpcrequest('DeleteClusterTemplate', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_cluster_template_with_options_async(
        self,
        request: ddi_20200617_models.DeleteClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteClusterTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteClusterTemplateResponse(),
            await self.do_rpcrequest_async('DeleteClusterTemplate', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cluster_template(
        self,
        request: ddi_20200617_models.DeleteClusterTemplateRequest,
    ) -> ddi_20200617_models.DeleteClusterTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_template_with_options(request, runtime)

    async def delete_cluster_template_async(
        self,
        request: ddi_20200617_models.DeleteClusterTemplateRequest,
    ) -> ddi_20200617_models.DeleteClusterTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_template_with_options_async(request, runtime)

    def cancel_order_with_options(
        self,
        request: ddi_20200617_models.CancelOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CancelOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CancelOrderResponse(),
            self.do_rpcrequest('CancelOrder', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_order_with_options_async(
        self,
        request: ddi_20200617_models.CancelOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CancelOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CancelOrderResponse(),
            await self.do_rpcrequest_async('CancelOrder', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_order(
        self,
        request: ddi_20200617_models.CancelOrderRequest,
    ) -> ddi_20200617_models.CancelOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_order_with_options(request, runtime)

    async def cancel_order_async(
        self,
        request: ddi_20200617_models.CancelOrderRequest,
    ) -> ddi_20200617_models.CancelOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_order_with_options_async(request, runtime)

    def clone_flow_job_with_options(
        self,
        request: ddi_20200617_models.CloneFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CloneFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CloneFlowJobResponse(),
            self.do_rpcrequest('CloneFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clone_flow_job_with_options_async(
        self,
        request: ddi_20200617_models.CloneFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CloneFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CloneFlowJobResponse(),
            await self.do_rpcrequest_async('CloneFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clone_flow_job(
        self,
        request: ddi_20200617_models.CloneFlowJobRequest,
    ) -> ddi_20200617_models.CloneFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.clone_flow_job_with_options(request, runtime)

    async def clone_flow_job_async(
        self,
        request: ddi_20200617_models.CloneFlowJobRequest,
    ) -> ddi_20200617_models.CloneFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clone_flow_job_with_options_async(request, runtime)

    def start_flow_with_options(
        self,
        request: ddi_20200617_models.StartFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.StartFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.StartFlowResponse(),
            self.do_rpcrequest('StartFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_flow_with_options_async(
        self,
        request: ddi_20200617_models.StartFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.StartFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.StartFlowResponse(),
            await self.do_rpcrequest_async('StartFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_flow(
        self,
        request: ddi_20200617_models.StartFlowRequest,
    ) -> ddi_20200617_models.StartFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_flow_with_options(request, runtime)

    async def start_flow_async(
        self,
        request: ddi_20200617_models.StartFlowRequest,
    ) -> ddi_20200617_models.StartFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_flow_with_options_async(request, runtime)

    def create_flow_job_with_options(
        self,
        request: ddi_20200617_models.CreateFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowJobResponse(),
            self.do_rpcrequest('CreateFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_job_with_options_async(
        self,
        request: ddi_20200617_models.CreateFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowJobResponse(),
            await self.do_rpcrequest_async('CreateFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_job(
        self,
        request: ddi_20200617_models.CreateFlowJobRequest,
    ) -> ddi_20200617_models.CreateFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_job_with_options(request, runtime)

    async def create_flow_job_async(
        self,
        request: ddi_20200617_models.CreateFlowJobRequest,
    ) -> ddi_20200617_models.CreateFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_job_with_options_async(request, runtime)

    def delete_flow_category_with_options(
        self,
        request: ddi_20200617_models.DeleteFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowCategoryResponse(),
            self.do_rpcrequest('DeleteFlowCategory', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_category_with_options_async(
        self,
        request: ddi_20200617_models.DeleteFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowCategoryResponse(),
            await self.do_rpcrequest_async('DeleteFlowCategory', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_category(
        self,
        request: ddi_20200617_models.DeleteFlowCategoryRequest,
    ) -> ddi_20200617_models.DeleteFlowCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_category_with_options(request, runtime)

    async def delete_flow_category_async(
        self,
        request: ddi_20200617_models.DeleteFlowCategoryRequest,
    ) -> ddi_20200617_models.DeleteFlowCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_category_with_options_async(request, runtime)

    def delete_flow_edit_lock_with_options(
        self,
        request: ddi_20200617_models.DeleteFlowEditLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowEditLockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowEditLockResponse(),
            self.do_rpcrequest('DeleteFlowEditLock', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_edit_lock_with_options_async(
        self,
        request: ddi_20200617_models.DeleteFlowEditLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowEditLockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowEditLockResponse(),
            await self.do_rpcrequest_async('DeleteFlowEditLock', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_edit_lock(
        self,
        request: ddi_20200617_models.DeleteFlowEditLockRequest,
    ) -> ddi_20200617_models.DeleteFlowEditLockResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_edit_lock_with_options(request, runtime)

    async def delete_flow_edit_lock_async(
        self,
        request: ddi_20200617_models.DeleteFlowEditLockRequest,
    ) -> ddi_20200617_models.DeleteFlowEditLockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_edit_lock_with_options_async(request, runtime)

    def resize_cluster_with_options(
        self,
        request: ddi_20200617_models.ResizeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ResizeClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ResizeClusterResponse(),
            self.do_rpcrequest('ResizeCluster', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resize_cluster_with_options_async(
        self,
        request: ddi_20200617_models.ResizeClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ResizeClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ResizeClusterResponse(),
            await self.do_rpcrequest_async('ResizeCluster', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resize_cluster(
        self,
        request: ddi_20200617_models.ResizeClusterRequest,
    ) -> ddi_20200617_models.ResizeClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.resize_cluster_with_options(request, runtime)

    async def resize_cluster_async(
        self,
        request: ddi_20200617_models.ResizeClusterRequest,
    ) -> ddi_20200617_models.ResizeClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resize_cluster_with_options_async(request, runtime)

    def describe_meta_table_preview_task_with_options(
        self,
        request: ddi_20200617_models.DescribeMetaTablePreviewTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeMetaTablePreviewTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeMetaTablePreviewTaskResponse(),
            self.do_rpcrequest('DescribeMetaTablePreviewTask', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meta_table_preview_task_with_options_async(
        self,
        request: ddi_20200617_models.DescribeMetaTablePreviewTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeMetaTablePreviewTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeMetaTablePreviewTaskResponse(),
            await self.do_rpcrequest_async('DescribeMetaTablePreviewTask', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_meta_table_preview_task(
        self,
        request: ddi_20200617_models.DescribeMetaTablePreviewTaskRequest,
    ) -> ddi_20200617_models.DescribeMetaTablePreviewTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meta_table_preview_task_with_options(request, runtime)

    async def describe_meta_table_preview_task_async(
        self,
        request: ddi_20200617_models.DescribeMetaTablePreviewTaskRequest,
    ) -> ddi_20200617_models.DescribeMetaTablePreviewTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meta_table_preview_task_with_options_async(request, runtime)

    def list_cluster_service_config_history_with_options(
        self,
        request: ddi_20200617_models.ListClusterServiceConfigHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClusterServiceConfigHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterServiceConfigHistoryResponse(),
            self.do_rpcrequest('ListClusterServiceConfigHistory', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_service_config_history_with_options_async(
        self,
        request: ddi_20200617_models.ListClusterServiceConfigHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClusterServiceConfigHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterServiceConfigHistoryResponse(),
            await self.do_rpcrequest_async('ListClusterServiceConfigHistory', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_service_config_history(
        self,
        request: ddi_20200617_models.ListClusterServiceConfigHistoryRequest,
    ) -> ddi_20200617_models.ListClusterServiceConfigHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_service_config_history_with_options(request, runtime)

    async def list_cluster_service_config_history_async(
        self,
        request: ddi_20200617_models.ListClusterServiceConfigHistoryRequest,
    ) -> ddi_20200617_models.ListClusterServiceConfigHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_service_config_history_with_options_async(request, runtime)

    def modify_scaling_config_item_with_options(
        self,
        request: ddi_20200617_models.ModifyScalingConfigItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyScalingConfigItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyScalingConfigItemResponse(),
            self.do_rpcrequest('ModifyScalingConfigItem', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_scaling_config_item_with_options_async(
        self,
        request: ddi_20200617_models.ModifyScalingConfigItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyScalingConfigItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyScalingConfigItemResponse(),
            await self.do_rpcrequest_async('ModifyScalingConfigItem', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scaling_config_item(
        self,
        request: ddi_20200617_models.ModifyScalingConfigItemRequest,
    ) -> ddi_20200617_models.ModifyScalingConfigItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_config_item_with_options(request, runtime)

    async def modify_scaling_config_item_async(
        self,
        request: ddi_20200617_models.ModifyScalingConfigItemRequest,
    ) -> ddi_20200617_models.ModifyScalingConfigItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_scaling_config_item_with_options_async(request, runtime)

    def list_flow_cluster_all_with_options(
        self,
        request: ddi_20200617_models.ListFlowClusterAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowClusterAllResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterAllResponse(),
            self.do_rpcrequest('ListFlowClusterAll', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_cluster_all_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowClusterAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowClusterAllResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterAllResponse(),
            await self.do_rpcrequest_async('ListFlowClusterAll', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_cluster_all(
        self,
        request: ddi_20200617_models.ListFlowClusterAllRequest,
    ) -> ddi_20200617_models.ListFlowClusterAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_cluster_all_with_options(request, runtime)

    async def list_flow_cluster_all_async(
        self,
        request: ddi_20200617_models.ListFlowClusterAllRequest,
    ) -> ddi_20200617_models.ListFlowClusterAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_cluster_all_with_options_async(request, runtime)

    def describe_scaling_group_with_options(
        self,
        request: ddi_20200617_models.DescribeScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeScalingGroupResponse(),
            self.do_rpcrequest('DescribeScalingGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scaling_group_with_options_async(
        self,
        request: ddi_20200617_models.DescribeScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeScalingGroupResponse(),
            await self.do_rpcrequest_async('DescribeScalingGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_group(
        self,
        request: ddi_20200617_models.DescribeScalingGroupRequest,
    ) -> ddi_20200617_models.DescribeScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_group_with_options(request, runtime)

    async def describe_scaling_group_async(
        self,
        request: ddi_20200617_models.DescribeScalingGroupRequest,
    ) -> ddi_20200617_models.DescribeScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_group_with_options_async(request, runtime)

    def list_scaling_group_with_options(
        self,
        request: ddi_20200617_models.ListScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListScalingGroupResponse(),
            self.do_rpcrequest('ListScalingGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_scaling_group_with_options_async(
        self,
        request: ddi_20200617_models.ListScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListScalingGroupResponse(),
            await self.do_rpcrequest_async('ListScalingGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scaling_group(
        self,
        request: ddi_20200617_models.ListScalingGroupRequest,
    ) -> ddi_20200617_models.ListScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_scaling_group_with_options(request, runtime)

    async def list_scaling_group_async(
        self,
        request: ddi_20200617_models.ListScalingGroupRequest,
    ) -> ddi_20200617_models.ListScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_scaling_group_with_options_async(request, runtime)

    def modify_flow_category_with_options(
        self,
        request: ddi_20200617_models.ModifyFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowCategoryResponse(),
            self.do_rpcrequest('ModifyFlowCategory', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_flow_category_with_options_async(
        self,
        request: ddi_20200617_models.ModifyFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowCategoryResponse(),
            await self.do_rpcrequest_async('ModifyFlowCategory', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_category(
        self,
        request: ddi_20200617_models.ModifyFlowCategoryRequest,
    ) -> ddi_20200617_models.ModifyFlowCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_category_with_options(request, runtime)

    async def modify_flow_category_async(
        self,
        request: ddi_20200617_models.ModifyFlowCategoryRequest,
    ) -> ddi_20200617_models.ModifyFlowCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_category_with_options_async(request, runtime)

    def modify_cluster_service_config_with_options(
        self,
        request: ddi_20200617_models.ModifyClusterServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyClusterServiceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyClusterServiceConfigResponse(),
            self.do_rpcrequest('ModifyClusterServiceConfig', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cluster_service_config_with_options_async(
        self,
        request: ddi_20200617_models.ModifyClusterServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyClusterServiceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyClusterServiceConfigResponse(),
            await self.do_rpcrequest_async('ModifyClusterServiceConfig', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cluster_service_config(
        self,
        request: ddi_20200617_models.ModifyClusterServiceConfigRequest,
    ) -> ddi_20200617_models.ModifyClusterServiceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_service_config_with_options(request, runtime)

    async def modify_cluster_service_config_async(
        self,
        request: ddi_20200617_models.ModifyClusterServiceConfigRequest,
    ) -> ddi_20200617_models.ModifyClusterServiceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_service_config_with_options_async(request, runtime)

    def clone_flow_with_options(
        self,
        request: ddi_20200617_models.CloneFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CloneFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CloneFlowResponse(),
            self.do_rpcrequest('CloneFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clone_flow_with_options_async(
        self,
        request: ddi_20200617_models.CloneFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CloneFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CloneFlowResponse(),
            await self.do_rpcrequest_async('CloneFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clone_flow(
        self,
        request: ddi_20200617_models.CloneFlowRequest,
    ) -> ddi_20200617_models.CloneFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.clone_flow_with_options(request, runtime)

    async def clone_flow_async(
        self,
        request: ddi_20200617_models.CloneFlowRequest,
    ) -> ddi_20200617_models.CloneFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clone_flow_with_options_async(request, runtime)

    def create_cluster_template_with_options(
        self,
        request: ddi_20200617_models.CreateClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateClusterTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateClusterTemplateResponse(),
            self.do_rpcrequest('CreateClusterTemplate', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cluster_template_with_options_async(
        self,
        request: ddi_20200617_models.CreateClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateClusterTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateClusterTemplateResponse(),
            await self.do_rpcrequest_async('CreateClusterTemplate', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cluster_template(
        self,
        request: ddi_20200617_models.CreateClusterTemplateRequest,
    ) -> ddi_20200617_models.CreateClusterTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_template_with_options(request, runtime)

    async def create_cluster_template_async(
        self,
        request: ddi_20200617_models.CreateClusterTemplateRequest,
    ) -> ddi_20200617_models.CreateClusterTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_template_with_options_async(request, runtime)

    def update_library_install_task_status_with_options(
        self,
        request: ddi_20200617_models.UpdateLibraryInstallTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.UpdateLibraryInstallTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.UpdateLibraryInstallTaskStatusResponse(),
            self.do_rpcrequest('UpdateLibraryInstallTaskStatus', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_library_install_task_status_with_options_async(
        self,
        request: ddi_20200617_models.UpdateLibraryInstallTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.UpdateLibraryInstallTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.UpdateLibraryInstallTaskStatusResponse(),
            await self.do_rpcrequest_async('UpdateLibraryInstallTaskStatus', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_library_install_task_status(
        self,
        request: ddi_20200617_models.UpdateLibraryInstallTaskStatusRequest,
    ) -> ddi_20200617_models.UpdateLibraryInstallTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_library_install_task_status_with_options(request, runtime)

    async def update_library_install_task_status_async(
        self,
        request: ddi_20200617_models.UpdateLibraryInstallTaskStatusRequest,
    ) -> ddi_20200617_models.UpdateLibraryInstallTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_library_install_task_status_with_options_async(request, runtime)

    def list_scaling_config_item_with_options(
        self,
        request: ddi_20200617_models.ListScalingConfigItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListScalingConfigItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListScalingConfigItemResponse(),
            self.do_rpcrequest('ListScalingConfigItem', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_scaling_config_item_with_options_async(
        self,
        request: ddi_20200617_models.ListScalingConfigItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListScalingConfigItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListScalingConfigItemResponse(),
            await self.do_rpcrequest_async('ListScalingConfigItem', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scaling_config_item(
        self,
        request: ddi_20200617_models.ListScalingConfigItemRequest,
    ) -> ddi_20200617_models.ListScalingConfigItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_scaling_config_item_with_options(request, runtime)

    async def list_scaling_config_item_async(
        self,
        request: ddi_20200617_models.ListScalingConfigItemRequest,
    ) -> ddi_20200617_models.ListScalingConfigItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_scaling_config_item_with_options_async(request, runtime)

    def list_flow_instance_with_options(
        self,
        request: ddi_20200617_models.ListFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowInstanceResponse(),
            self.do_rpcrequest('ListFlowInstance', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_instance_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowInstanceResponse(),
            await self.do_rpcrequest_async('ListFlowInstance', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_instance(
        self,
        request: ddi_20200617_models.ListFlowInstanceRequest,
    ) -> ddi_20200617_models.ListFlowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_instance_with_options(request, runtime)

    async def list_flow_instance_async(
        self,
        request: ddi_20200617_models.ListFlowInstanceRequest,
    ) -> ddi_20200617_models.ListFlowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_instance_with_options_async(request, runtime)

    def describe_scaling_metrics_with_options(
        self,
        request: ddi_20200617_models.DescribeScalingMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeScalingMetricsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeScalingMetricsResponse(),
            self.do_rpcrequest('DescribeScalingMetrics', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scaling_metrics_with_options_async(
        self,
        request: ddi_20200617_models.DescribeScalingMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeScalingMetricsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeScalingMetricsResponse(),
            await self.do_rpcrequest_async('DescribeScalingMetrics', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_metrics(
        self,
        request: ddi_20200617_models.DescribeScalingMetricsRequest,
    ) -> ddi_20200617_models.DescribeScalingMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_metrics_with_options(request, runtime)

    async def describe_scaling_metrics_async(
        self,
        request: ddi_20200617_models.DescribeScalingMetricsRequest,
    ) -> ddi_20200617_models.DescribeScalingMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_metrics_with_options_async(request, runtime)

    def untag_resources_system_tags_with_options(
        self,
        request: ddi_20200617_models.UntagResourcesSystemTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.UntagResourcesSystemTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.UntagResourcesSystemTagsResponse(),
            self.do_rpcrequest('UntagResourcesSystemTags', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_system_tags_with_options_async(
        self,
        request: ddi_20200617_models.UntagResourcesSystemTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.UntagResourcesSystemTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.UntagResourcesSystemTagsResponse(),
            await self.do_rpcrequest_async('UntagResourcesSystemTags', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources_system_tags(
        self,
        request: ddi_20200617_models.UntagResourcesSystemTagsRequest,
    ) -> ddi_20200617_models.UntagResourcesSystemTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_system_tags_with_options(request, runtime)

    async def untag_resources_system_tags_async(
        self,
        request: ddi_20200617_models.UntagResourcesSystemTagsRequest,
    ) -> ddi_20200617_models.UntagResourcesSystemTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_system_tags_with_options_async(request, runtime)

    def describe_flow_project_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowProjectResponse(),
            self.do_rpcrequest('DescribeFlowProject', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_project_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowProjectResponse(),
            await self.do_rpcrequest_async('DescribeFlowProject', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_project(
        self,
        request: ddi_20200617_models.DescribeFlowProjectRequest,
    ) -> ddi_20200617_models.DescribeFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_project_with_options(request, runtime)

    async def describe_flow_project_async(
        self,
        request: ddi_20200617_models.DescribeFlowProjectRequest,
    ) -> ddi_20200617_models.DescribeFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_project_with_options_async(request, runtime)

    def delete_security_white_list_with_options(
        self,
        request: ddi_20200617_models.DeleteSecurityWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteSecurityWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteSecurityWhiteListResponse(),
            self.do_rpcrequest('DeleteSecurityWhiteList', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_security_white_list_with_options_async(
        self,
        request: ddi_20200617_models.DeleteSecurityWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteSecurityWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteSecurityWhiteListResponse(),
            await self.do_rpcrequest_async('DeleteSecurityWhiteList', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_security_white_list(
        self,
        request: ddi_20200617_models.DeleteSecurityWhiteListRequest,
    ) -> ddi_20200617_models.DeleteSecurityWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_security_white_list_with_options(request, runtime)

    async def delete_security_white_list_async(
        self,
        request: ddi_20200617_models.DeleteSecurityWhiteListRequest,
    ) -> ddi_20200617_models.DeleteSecurityWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_security_white_list_with_options_async(request, runtime)

    def list_scaling_activity_with_options(
        self,
        request: ddi_20200617_models.ListScalingActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListScalingActivityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListScalingActivityResponse(),
            self.do_rpcrequest('ListScalingActivity', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_scaling_activity_with_options_async(
        self,
        request: ddi_20200617_models.ListScalingActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListScalingActivityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListScalingActivityResponse(),
            await self.do_rpcrequest_async('ListScalingActivity', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scaling_activity(
        self,
        request: ddi_20200617_models.ListScalingActivityRequest,
    ) -> ddi_20200617_models.ListScalingActivityResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_scaling_activity_with_options(request, runtime)

    async def list_scaling_activity_async(
        self,
        request: ddi_20200617_models.ListScalingActivityRequest,
    ) -> ddi_20200617_models.ListScalingActivityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_scaling_activity_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: ddi_20200617_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListTagValuesResponse(),
            self.do_rpcrequest('ListTagValues', '2020-06-17', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: ddi_20200617_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListTagValuesResponse(),
            await self.do_rpcrequest_async('ListTagValues', '2020-06-17', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_tag_values(
        self,
        request: ddi_20200617_models.ListTagValuesRequest,
    ) -> ddi_20200617_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: ddi_20200617_models.ListTagValuesRequest,
    ) -> ddi_20200617_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def list_cluster_installed_service_with_options(
        self,
        request: ddi_20200617_models.ListClusterInstalledServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClusterInstalledServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterInstalledServiceResponse(),
            self.do_rpcrequest('ListClusterInstalledService', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_installed_service_with_options_async(
        self,
        request: ddi_20200617_models.ListClusterInstalledServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClusterInstalledServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterInstalledServiceResponse(),
            await self.do_rpcrequest_async('ListClusterInstalledService', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_installed_service(
        self,
        request: ddi_20200617_models.ListClusterInstalledServiceRequest,
    ) -> ddi_20200617_models.ListClusterInstalledServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_installed_service_with_options(request, runtime)

    async def list_cluster_installed_service_async(
        self,
        request: ddi_20200617_models.ListClusterInstalledServiceRequest,
    ) -> ddi_20200617_models.ListClusterInstalledServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_installed_service_with_options_async(request, runtime)

    def run_cluster_service_action_with_options(
        self,
        request: ddi_20200617_models.RunClusterServiceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.RunClusterServiceActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.RunClusterServiceActionResponse(),
            self.do_rpcrequest('RunClusterServiceAction', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_cluster_service_action_with_options_async(
        self,
        request: ddi_20200617_models.RunClusterServiceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.RunClusterServiceActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.RunClusterServiceActionResponse(),
            await self.do_rpcrequest_async('RunClusterServiceAction', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_cluster_service_action(
        self,
        request: ddi_20200617_models.RunClusterServiceActionRequest,
    ) -> ddi_20200617_models.RunClusterServiceActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_cluster_service_action_with_options(request, runtime)

    async def run_cluster_service_action_async(
        self,
        request: ddi_20200617_models.RunClusterServiceActionRequest,
    ) -> ddi_20200617_models.RunClusterServiceActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_cluster_service_action_with_options_async(request, runtime)

    def suspend_flow_with_options(
        self,
        request: ddi_20200617_models.SuspendFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.SuspendFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.SuspendFlowResponse(),
            self.do_rpcrequest('SuspendFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def suspend_flow_with_options_async(
        self,
        request: ddi_20200617_models.SuspendFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.SuspendFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.SuspendFlowResponse(),
            await self.do_rpcrequest_async('SuspendFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_flow(
        self,
        request: ddi_20200617_models.SuspendFlowRequest,
    ) -> ddi_20200617_models.SuspendFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_flow_with_options(request, runtime)

    async def suspend_flow_async(
        self,
        request: ddi_20200617_models.SuspendFlowRequest,
    ) -> ddi_20200617_models.SuspendFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_flow_with_options_async(request, runtime)

    def create_flow_project_with_options(
        self,
        request: ddi_20200617_models.CreateFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowProjectResponse(),
            self.do_rpcrequest('CreateFlowProject', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_project_with_options_async(
        self,
        request: ddi_20200617_models.CreateFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowProjectResponse(),
            await self.do_rpcrequest_async('CreateFlowProject', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_project(
        self,
        request: ddi_20200617_models.CreateFlowProjectRequest,
    ) -> ddi_20200617_models.CreateFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_project_with_options(request, runtime)

    async def create_flow_project_async(
        self,
        request: ddi_20200617_models.CreateFlowProjectRequest,
    ) -> ddi_20200617_models.CreateFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_project_with_options_async(request, runtime)

    def list_flow_node_instance_container_status_with_options(
        self,
        request: ddi_20200617_models.ListFlowNodeInstanceContainerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowNodeInstanceContainerStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowNodeInstanceContainerStatusResponse(),
            self.do_rpcrequest('ListFlowNodeInstanceContainerStatus', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_node_instance_container_status_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowNodeInstanceContainerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowNodeInstanceContainerStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowNodeInstanceContainerStatusResponse(),
            await self.do_rpcrequest_async('ListFlowNodeInstanceContainerStatus', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_node_instance_container_status(
        self,
        request: ddi_20200617_models.ListFlowNodeInstanceContainerStatusRequest,
    ) -> ddi_20200617_models.ListFlowNodeInstanceContainerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_node_instance_container_status_with_options(request, runtime)

    async def list_flow_node_instance_container_status_async(
        self,
        request: ddi_20200617_models.ListFlowNodeInstanceContainerStatusRequest,
    ) -> ddi_20200617_models.ListFlowNodeInstanceContainerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_node_instance_container_status_with_options_async(request, runtime)

    def modify_cluster_template_with_options(
        self,
        request: ddi_20200617_models.ModifyClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyClusterTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyClusterTemplateResponse(),
            self.do_rpcrequest('ModifyClusterTemplate', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cluster_template_with_options_async(
        self,
        request: ddi_20200617_models.ModifyClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyClusterTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyClusterTemplateResponse(),
            await self.do_rpcrequest_async('ModifyClusterTemplate', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cluster_template(
        self,
        request: ddi_20200617_models.ModifyClusterTemplateRequest,
    ) -> ddi_20200617_models.ModifyClusterTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_template_with_options(request, runtime)

    async def modify_cluster_template_async(
        self,
        request: ddi_20200617_models.ModifyClusterTemplateRequest,
    ) -> ddi_20200617_models.ModifyClusterTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_template_with_options_async(request, runtime)

    def add_security_white_list_with_options(
        self,
        request: ddi_20200617_models.AddSecurityWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.AddSecurityWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.AddSecurityWhiteListResponse(),
            self.do_rpcrequest('AddSecurityWhiteList', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_security_white_list_with_options_async(
        self,
        request: ddi_20200617_models.AddSecurityWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.AddSecurityWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.AddSecurityWhiteListResponse(),
            await self.do_rpcrequest_async('AddSecurityWhiteList', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_security_white_list(
        self,
        request: ddi_20200617_models.AddSecurityWhiteListRequest,
    ) -> ddi_20200617_models.AddSecurityWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_security_white_list_with_options(request, runtime)

    async def add_security_white_list_async(
        self,
        request: ddi_20200617_models.AddSecurityWhiteListRequest,
    ) -> ddi_20200617_models.AddSecurityWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_security_white_list_with_options_async(request, runtime)

    def list_meta_cluster_with_options(
        self,
        request: ddi_20200617_models.ListMetaClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListMetaClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListMetaClusterResponse(),
            self.do_rpcrequest('ListMetaCluster', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_meta_cluster_with_options_async(
        self,
        request: ddi_20200617_models.ListMetaClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListMetaClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListMetaClusterResponse(),
            await self.do_rpcrequest_async('ListMetaCluster', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_meta_cluster(
        self,
        request: ddi_20200617_models.ListMetaClusterRequest,
    ) -> ddi_20200617_models.ListMetaClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_meta_cluster_with_options(request, runtime)

    async def list_meta_cluster_async(
        self,
        request: ddi_20200617_models.ListMetaClusterRequest,
    ) -> ddi_20200617_models.ListMetaClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_meta_cluster_with_options_async(request, runtime)

    def list_cluster_operation_host_with_options(
        self,
        request: ddi_20200617_models.ListClusterOperationHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClusterOperationHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterOperationHostResponse(),
            self.do_rpcrequest('ListClusterOperationHost', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_operation_host_with_options_async(
        self,
        request: ddi_20200617_models.ListClusterOperationHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClusterOperationHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterOperationHostResponse(),
            await self.do_rpcrequest_async('ListClusterOperationHost', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_operation_host(
        self,
        request: ddi_20200617_models.ListClusterOperationHostRequest,
    ) -> ddi_20200617_models.ListClusterOperationHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_operation_host_with_options(request, runtime)

    async def list_cluster_operation_host_async(
        self,
        request: ddi_20200617_models.ListClusterOperationHostRequest,
    ) -> ddi_20200617_models.ListClusterOperationHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_operation_host_with_options_async(request, runtime)

    def list_cluster_templates_with_options(
        self,
        request: ddi_20200617_models.ListClusterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClusterTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterTemplatesResponse(),
            self.do_rpcrequest('ListClusterTemplates', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_templates_with_options_async(
        self,
        request: ddi_20200617_models.ListClusterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClusterTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterTemplatesResponse(),
            await self.do_rpcrequest_async('ListClusterTemplates', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_templates(
        self,
        request: ddi_20200617_models.ListClusterTemplatesRequest,
    ) -> ddi_20200617_models.ListClusterTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_templates_with_options(request, runtime)

    async def list_cluster_templates_async(
        self,
        request: ddi_20200617_models.ListClusterTemplatesRequest,
    ) -> ddi_20200617_models.ListClusterTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_templates_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: ddi_20200617_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClustersResponse(),
            self.do_rpcrequest('ListClusters', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: ddi_20200617_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClustersResponse(),
            await self.do_rpcrequest_async('ListClusters', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_clusters(
        self,
        request: ddi_20200617_models.ListClustersRequest,
    ) -> ddi_20200617_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: ddi_20200617_models.ListClustersRequest,
    ) -> ddi_20200617_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def tag_resources_system_tags_with_options(
        self,
        request: ddi_20200617_models.TagResourcesSystemTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.TagResourcesSystemTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.TagResourcesSystemTagsResponse(),
            self.do_rpcrequest('TagResourcesSystemTags', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_system_tags_with_options_async(
        self,
        request: ddi_20200617_models.TagResourcesSystemTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.TagResourcesSystemTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.TagResourcesSystemTagsResponse(),
            await self.do_rpcrequest_async('TagResourcesSystemTags', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources_system_tags(
        self,
        request: ddi_20200617_models.TagResourcesSystemTagsRequest,
    ) -> ddi_20200617_models.TagResourcesSystemTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_system_tags_with_options(request, runtime)

    async def tag_resources_system_tags_async(
        self,
        request: ddi_20200617_models.TagResourcesSystemTagsRequest,
    ) -> ddi_20200617_models.TagResourcesSystemTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_system_tags_with_options_async(request, runtime)

    def modify_flow_job_with_options(
        self,
        request: ddi_20200617_models.ModifyFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowJobResponse(),
            self.do_rpcrequest('ModifyFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_flow_job_with_options_async(
        self,
        request: ddi_20200617_models.ModifyFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowJobResponse(),
            await self.do_rpcrequest_async('ModifyFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_job(
        self,
        request: ddi_20200617_models.ModifyFlowJobRequest,
    ) -> ddi_20200617_models.ModifyFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_job_with_options(request, runtime)

    async def modify_flow_job_async(
        self,
        request: ddi_20200617_models.ModifyFlowJobRequest,
    ) -> ddi_20200617_models.ModifyFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_job_with_options_async(request, runtime)

    def delete_flow_with_options(
        self,
        request: ddi_20200617_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowResponse(),
            self.do_rpcrequest('DeleteFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_with_options_async(
        self,
        request: ddi_20200617_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowResponse(),
            await self.do_rpcrequest_async('DeleteFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow(
        self,
        request: ddi_20200617_models.DeleteFlowRequest,
    ) -> ddi_20200617_models.DeleteFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_with_options(request, runtime)

    async def delete_flow_async(
        self,
        request: ddi_20200617_models.DeleteFlowRequest,
    ) -> ddi_20200617_models.DeleteFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_with_options_async(request, runtime)

    def create_flow_edit_lock_with_options(
        self,
        request: ddi_20200617_models.CreateFlowEditLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowEditLockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowEditLockResponse(),
            self.do_rpcrequest('CreateFlowEditLock', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_edit_lock_with_options_async(
        self,
        request: ddi_20200617_models.CreateFlowEditLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowEditLockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowEditLockResponse(),
            await self.do_rpcrequest_async('CreateFlowEditLock', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_edit_lock(
        self,
        request: ddi_20200617_models.CreateFlowEditLockRequest,
    ) -> ddi_20200617_models.CreateFlowEditLockResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_edit_lock_with_options(request, runtime)

    async def create_flow_edit_lock_async(
        self,
        request: ddi_20200617_models.CreateFlowEditLockRequest,
    ) -> ddi_20200617_models.CreateFlowEditLockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_edit_lock_with_options_async(request, runtime)

    def describe_flow_node_instance_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowNodeInstanceResponse(),
            self.do_rpcrequest('DescribeFlowNodeInstance', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_node_instance_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowNodeInstanceResponse(),
            await self.do_rpcrequest_async('DescribeFlowNodeInstance', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_node_instance(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceRequest,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_node_instance_with_options(request, runtime)

    async def describe_flow_node_instance_async(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceRequest,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_node_instance_with_options_async(request, runtime)

    def detach_and_release_cluster_eni_with_options(
        self,
        request: ddi_20200617_models.DetachAndReleaseClusterEniRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DetachAndReleaseClusterEniResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DetachAndReleaseClusterEniResponse(),
            self.do_rpcrequest('DetachAndReleaseClusterEni', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_and_release_cluster_eni_with_options_async(
        self,
        request: ddi_20200617_models.DetachAndReleaseClusterEniRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DetachAndReleaseClusterEniResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DetachAndReleaseClusterEniResponse(),
            await self.do_rpcrequest_async('DetachAndReleaseClusterEni', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_and_release_cluster_eni(
        self,
        request: ddi_20200617_models.DetachAndReleaseClusterEniRequest,
    ) -> ddi_20200617_models.DetachAndReleaseClusterEniResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_and_release_cluster_eni_with_options(request, runtime)

    async def detach_and_release_cluster_eni_async(
        self,
        request: ddi_20200617_models.DetachAndReleaseClusterEniRequest,
    ) -> ddi_20200617_models.DetachAndReleaseClusterEniResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_and_release_cluster_eni_with_options_async(request, runtime)

    def describe_scaling_group_instance_with_options(
        self,
        request: ddi_20200617_models.DescribeScalingGroupInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeScalingGroupInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeScalingGroupInstanceResponse(),
            self.do_rpcrequest('DescribeScalingGroupInstance', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scaling_group_instance_with_options_async(
        self,
        request: ddi_20200617_models.DescribeScalingGroupInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeScalingGroupInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeScalingGroupInstanceResponse(),
            await self.do_rpcrequest_async('DescribeScalingGroupInstance', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_group_instance(
        self,
        request: ddi_20200617_models.DescribeScalingGroupInstanceRequest,
    ) -> ddi_20200617_models.DescribeScalingGroupInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_group_instance_with_options(request, runtime)

    async def describe_scaling_group_instance_async(
        self,
        request: ddi_20200617_models.DescribeScalingGroupInstanceRequest,
    ) -> ddi_20200617_models.DescribeScalingGroupInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_group_instance_with_options_async(request, runtime)

    def create_cluster_host_group_with_options(
        self,
        request: ddi_20200617_models.CreateClusterHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateClusterHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateClusterHostGroupResponse(),
            self.do_rpcrequest('CreateClusterHostGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cluster_host_group_with_options_async(
        self,
        request: ddi_20200617_models.CreateClusterHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateClusterHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateClusterHostGroupResponse(),
            await self.do_rpcrequest_async('CreateClusterHostGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cluster_host_group(
        self,
        request: ddi_20200617_models.CreateClusterHostGroupRequest,
    ) -> ddi_20200617_models.CreateClusterHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_host_group_with_options(request, runtime)

    async def create_cluster_host_group_async(
        self,
        request: ddi_20200617_models.CreateClusterHostGroupRequest,
    ) -> ddi_20200617_models.CreateClusterHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_host_group_with_options_async(request, runtime)

    def describe_cluster_template_with_options(
        self,
        request: ddi_20200617_models.DescribeClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeClusterTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeClusterTemplateResponse(),
            self.do_rpcrequest('DescribeClusterTemplate', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_template_with_options_async(
        self,
        request: ddi_20200617_models.DescribeClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeClusterTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeClusterTemplateResponse(),
            await self.do_rpcrequest_async('DescribeClusterTemplate', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_template(
        self,
        request: ddi_20200617_models.DescribeClusterTemplateRequest,
    ) -> ddi_20200617_models.DescribeClusterTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_template_with_options(request, runtime)

    async def describe_cluster_template_async(
        self,
        request: ddi_20200617_models.DescribeClusterTemplateRequest,
    ) -> ddi_20200617_models.DescribeClusterTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_template_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ddi_20200617_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ddi_20200617_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.TagResourcesResponse(),
            await self.do_rpcrequest_async('TagResources', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: ddi_20200617_models.TagResourcesRequest,
    ) -> ddi_20200617_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ddi_20200617_models.TagResourcesRequest,
    ) -> ddi_20200617_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def commit_flow_entity_snapshot_with_options(
        self,
        request: ddi_20200617_models.CommitFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CommitFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CommitFlowEntitySnapshotResponse(),
            self.do_rpcrequest('CommitFlowEntitySnapshot', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def commit_flow_entity_snapshot_with_options_async(
        self,
        request: ddi_20200617_models.CommitFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CommitFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CommitFlowEntitySnapshotResponse(),
            await self.do_rpcrequest_async('CommitFlowEntitySnapshot', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def commit_flow_entity_snapshot(
        self,
        request: ddi_20200617_models.CommitFlowEntitySnapshotRequest,
    ) -> ddi_20200617_models.CommitFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.commit_flow_entity_snapshot_with_options(request, runtime)

    async def commit_flow_entity_snapshot_async(
        self,
        request: ddi_20200617_models.CommitFlowEntitySnapshotRequest,
    ) -> ddi_20200617_models.CommitFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.commit_flow_entity_snapshot_with_options_async(request, runtime)

    def submit_flow_job_with_options(
        self,
        request: ddi_20200617_models.SubmitFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.SubmitFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.SubmitFlowJobResponse(),
            self.do_rpcrequest('SubmitFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_flow_job_with_options_async(
        self,
        request: ddi_20200617_models.SubmitFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.SubmitFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.SubmitFlowJobResponse(),
            await self.do_rpcrequest_async('SubmitFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_flow_job(
        self,
        request: ddi_20200617_models.SubmitFlowJobRequest,
    ) -> ddi_20200617_models.SubmitFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_flow_job_with_options(request, runtime)

    async def submit_flow_job_async(
        self,
        request: ddi_20200617_models.SubmitFlowJobRequest,
    ) -> ddi_20200617_models.SubmitFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_flow_job_with_options_async(request, runtime)

    def list_flow_job_history_with_options(
        self,
        request: ddi_20200617_models.ListFlowJobHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowJobHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowJobHistoryResponse(),
            self.do_rpcrequest('ListFlowJobHistory', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_job_history_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowJobHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowJobHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowJobHistoryResponse(),
            await self.do_rpcrequest_async('ListFlowJobHistory', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_job_history(
        self,
        request: ddi_20200617_models.ListFlowJobHistoryRequest,
    ) -> ddi_20200617_models.ListFlowJobHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_job_history_with_options(request, runtime)

    async def list_flow_job_history_async(
        self,
        request: ddi_20200617_models.ListFlowJobHistoryRequest,
    ) -> ddi_20200617_models.ListFlowJobHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_job_history_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ddi_20200617_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2020-06-17', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ddi_20200617_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListTagResourcesResponse(),
            await self.do_rpcrequest_async('ListTagResources', '2020-06-17', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: ddi_20200617_models.ListTagResourcesRequest,
    ) -> ddi_20200617_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ddi_20200617_models.ListTagResourcesRequest,
    ) -> ddi_20200617_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_cluster_host_component_with_options(
        self,
        request: ddi_20200617_models.ListClusterHostComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClusterHostComponentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterHostComponentResponse(),
            self.do_rpcrequest('ListClusterHostComponent', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_host_component_with_options_async(
        self,
        request: ddi_20200617_models.ListClusterHostComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClusterHostComponentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterHostComponentResponse(),
            await self.do_rpcrequest_async('ListClusterHostComponent', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_host_component(
        self,
        request: ddi_20200617_models.ListClusterHostComponentRequest,
    ) -> ddi_20200617_models.ListClusterHostComponentResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_host_component_with_options(request, runtime)

    async def list_cluster_host_component_async(
        self,
        request: ddi_20200617_models.ListClusterHostComponentRequest,
    ) -> ddi_20200617_models.ListClusterHostComponentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_host_component_with_options_async(request, runtime)

    def modify_scaling_group_with_options(
        self,
        request: ddi_20200617_models.ModifyScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyScalingGroupResponse(),
            self.do_rpcrequest('ModifyScalingGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_scaling_group_with_options_async(
        self,
        request: ddi_20200617_models.ModifyScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyScalingGroupResponse(),
            await self.do_rpcrequest_async('ModifyScalingGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scaling_group(
        self,
        request: ddi_20200617_models.ModifyScalingGroupRequest,
    ) -> ddi_20200617_models.ModifyScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_group_with_options(request, runtime)

    async def modify_scaling_group_async(
        self,
        request: ddi_20200617_models.ModifyScalingGroupRequest,
    ) -> ddi_20200617_models.ModifyScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_scaling_group_with_options_async(request, runtime)

    def describe_flow_project_cluster_setting_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowProjectClusterSettingResponse(),
            self.do_rpcrequest('DescribeFlowProjectClusterSetting', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_project_cluster_setting_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowProjectClusterSettingResponse(),
            await self.do_rpcrequest_async('DescribeFlowProjectClusterSetting', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_project_cluster_setting(
        self,
        request: ddi_20200617_models.DescribeFlowProjectClusterSettingRequest,
    ) -> ddi_20200617_models.DescribeFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_project_cluster_setting_with_options(request, runtime)

    async def describe_flow_project_cluster_setting_async(
        self,
        request: ddi_20200617_models.DescribeFlowProjectClusterSettingRequest,
    ) -> ddi_20200617_models.DescribeFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_project_cluster_setting_with_options_async(request, runtime)

    def list_flow_project_cluster_setting_with_options(
        self,
        request: ddi_20200617_models.ListFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowProjectClusterSettingResponse(),
            self.do_rpcrequest('ListFlowProjectClusterSetting', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_project_cluster_setting_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowProjectClusterSettingResponse(),
            await self.do_rpcrequest_async('ListFlowProjectClusterSetting', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_project_cluster_setting(
        self,
        request: ddi_20200617_models.ListFlowProjectClusterSettingRequest,
    ) -> ddi_20200617_models.ListFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_project_cluster_setting_with_options(request, runtime)

    async def list_flow_project_cluster_setting_async(
        self,
        request: ddi_20200617_models.ListFlowProjectClusterSettingRequest,
    ) -> ddi_20200617_models.ListFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_project_cluster_setting_with_options_async(request, runtime)

    def submit_flow_with_options(
        self,
        request: ddi_20200617_models.SubmitFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.SubmitFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.SubmitFlowResponse(),
            self.do_rpcrequest('SubmitFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_flow_with_options_async(
        self,
        request: ddi_20200617_models.SubmitFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.SubmitFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.SubmitFlowResponse(),
            await self.do_rpcrequest_async('SubmitFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_flow(
        self,
        request: ddi_20200617_models.SubmitFlowRequest,
    ) -> ddi_20200617_models.SubmitFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_flow_with_options(request, runtime)

    async def submit_flow_async(
        self,
        request: ddi_20200617_models.SubmitFlowRequest,
    ) -> ddi_20200617_models.SubmitFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_flow_with_options_async(request, runtime)

    def describe_scaling_common_config_with_options(
        self,
        request: ddi_20200617_models.DescribeScalingCommonConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeScalingCommonConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeScalingCommonConfigResponse(),
            self.do_rpcrequest('DescribeScalingCommonConfig', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scaling_common_config_with_options_async(
        self,
        request: ddi_20200617_models.DescribeScalingCommonConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeScalingCommonConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeScalingCommonConfigResponse(),
            await self.do_rpcrequest_async('DescribeScalingCommonConfig', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_common_config(
        self,
        request: ddi_20200617_models.DescribeScalingCommonConfigRequest,
    ) -> ddi_20200617_models.DescribeScalingCommonConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_common_config_with_options(request, runtime)

    async def describe_scaling_common_config_async(
        self,
        request: ddi_20200617_models.DescribeScalingCommonConfigRequest,
    ) -> ddi_20200617_models.DescribeScalingCommonConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_common_config_with_options_async(request, runtime)

    def resume_flow_with_options(
        self,
        request: ddi_20200617_models.ResumeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ResumeFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ResumeFlowResponse(),
            self.do_rpcrequest('ResumeFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resume_flow_with_options_async(
        self,
        request: ddi_20200617_models.ResumeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ResumeFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ResumeFlowResponse(),
            await self.do_rpcrequest_async('ResumeFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_flow(
        self,
        request: ddi_20200617_models.ResumeFlowRequest,
    ) -> ddi_20200617_models.ResumeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_flow_with_options(request, runtime)

    async def resume_flow_async(
        self,
        request: ddi_20200617_models.ResumeFlowRequest,
    ) -> ddi_20200617_models.ResumeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_flow_with_options_async(request, runtime)

    def restore_flow_entity_snapshot_with_options(
        self,
        request: ddi_20200617_models.RestoreFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.RestoreFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.RestoreFlowEntitySnapshotResponse(),
            self.do_rpcrequest('RestoreFlowEntitySnapshot', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restore_flow_entity_snapshot_with_options_async(
        self,
        request: ddi_20200617_models.RestoreFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.RestoreFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.RestoreFlowEntitySnapshotResponse(),
            await self.do_rpcrequest_async('RestoreFlowEntitySnapshot', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restore_flow_entity_snapshot(
        self,
        request: ddi_20200617_models.RestoreFlowEntitySnapshotRequest,
    ) -> ddi_20200617_models.RestoreFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.restore_flow_entity_snapshot_with_options(request, runtime)

    async def restore_flow_entity_snapshot_async(
        self,
        request: ddi_20200617_models.RestoreFlowEntitySnapshotRequest,
    ) -> ddi_20200617_models.RestoreFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restore_flow_entity_snapshot_with_options_async(request, runtime)

    def create_library_with_options(
        self,
        request: ddi_20200617_models.CreateLibraryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateLibraryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateLibraryResponse(),
            self.do_rpcrequest('CreateLibrary', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_library_with_options_async(
        self,
        request: ddi_20200617_models.CreateLibraryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateLibraryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateLibraryResponse(),
            await self.do_rpcrequest_async('CreateLibrary', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_library(
        self,
        request: ddi_20200617_models.CreateLibraryRequest,
    ) -> ddi_20200617_models.CreateLibraryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_library_with_options(request, runtime)

    async def create_library_async(
        self,
        request: ddi_20200617_models.CreateLibraryRequest,
    ) -> ddi_20200617_models.CreateLibraryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_library_with_options_async(request, runtime)

    def list_vswitch_with_options(
        self,
        request: ddi_20200617_models.ListVswitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListVswitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListVswitchResponse(),
            self.do_rpcrequest('ListVswitch', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_vswitch_with_options_async(
        self,
        request: ddi_20200617_models.ListVswitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListVswitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListVswitchResponse(),
            await self.do_rpcrequest_async('ListVswitch', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vswitch(
        self,
        request: ddi_20200617_models.ListVswitchRequest,
    ) -> ddi_20200617_models.ListVswitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vswitch_with_options(request, runtime)

    async def list_vswitch_async(
        self,
        request: ddi_20200617_models.ListVswitchRequest,
    ) -> ddi_20200617_models.ListVswitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vswitch_with_options_async(request, runtime)

    def delete_flow_project_with_options(
        self,
        request: ddi_20200617_models.DeleteFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowProjectResponse(),
            self.do_rpcrequest('DeleteFlowProject', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_project_with_options_async(
        self,
        request: ddi_20200617_models.DeleteFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowProjectResponse(),
            await self.do_rpcrequest_async('DeleteFlowProject', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_project(
        self,
        request: ddi_20200617_models.DeleteFlowProjectRequest,
    ) -> ddi_20200617_models.DeleteFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_project_with_options(request, runtime)

    async def delete_flow_project_async(
        self,
        request: ddi_20200617_models.DeleteFlowProjectRequest,
    ) -> ddi_20200617_models.DeleteFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_project_with_options_async(request, runtime)

    def release_cluster_with_options(
        self,
        request: ddi_20200617_models.ReleaseClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ReleaseClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ReleaseClusterResponse(),
            self.do_rpcrequest('ReleaseCluster', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_cluster_with_options_async(
        self,
        request: ddi_20200617_models.ReleaseClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ReleaseClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ReleaseClusterResponse(),
            await self.do_rpcrequest_async('ReleaseCluster', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_cluster(
        self,
        request: ddi_20200617_models.ReleaseClusterRequest,
    ) -> ddi_20200617_models.ReleaseClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_cluster_with_options(request, runtime)

    async def release_cluster_async(
        self,
        request: ddi_20200617_models.ReleaseClusterRequest,
    ) -> ddi_20200617_models.ReleaseClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_cluster_with_options_async(request, runtime)

    def add_scaling_config_item_with_options(
        self,
        request: ddi_20200617_models.AddScalingConfigItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.AddScalingConfigItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.AddScalingConfigItemResponse(),
            self.do_rpcrequest('AddScalingConfigItem', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_scaling_config_item_with_options_async(
        self,
        request: ddi_20200617_models.AddScalingConfigItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.AddScalingConfigItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.AddScalingConfigItemResponse(),
            await self.do_rpcrequest_async('AddScalingConfigItem', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_scaling_config_item(
        self,
        request: ddi_20200617_models.AddScalingConfigItemRequest,
    ) -> ddi_20200617_models.AddScalingConfigItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_scaling_config_item_with_options(request, runtime)

    async def add_scaling_config_item_async(
        self,
        request: ddi_20200617_models.AddScalingConfigItemRequest,
    ) -> ddi_20200617_models.AddScalingConfigItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_scaling_config_item_with_options_async(request, runtime)

    def reset_user_password_with_options(
        self,
        request: ddi_20200617_models.ResetUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ResetUserPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ResetUserPasswordResponse(),
            self.do_rpcrequest('ResetUserPassword', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def reset_user_password_with_options_async(
        self,
        request: ddi_20200617_models.ResetUserPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ResetUserPasswordResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ResetUserPasswordResponse(),
            await self.do_rpcrequest_async('ResetUserPassword', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def reset_user_password(
        self,
        request: ddi_20200617_models.ResetUserPasswordRequest,
    ) -> ddi_20200617_models.ResetUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_user_password_with_options(request, runtime)

    async def reset_user_password_async(
        self,
        request: ddi_20200617_models.ResetUserPasswordRequest,
    ) -> ddi_20200617_models.ResetUserPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_user_password_with_options_async(request, runtime)

    def list_flow_cluster_all_hosts_with_options(
        self,
        request: ddi_20200617_models.ListFlowClusterAllHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowClusterAllHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterAllHostsResponse(),
            self.do_rpcrequest('ListFlowClusterAllHosts', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_cluster_all_hosts_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowClusterAllHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowClusterAllHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterAllHostsResponse(),
            await self.do_rpcrequest_async('ListFlowClusterAllHosts', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_cluster_all_hosts(
        self,
        request: ddi_20200617_models.ListFlowClusterAllHostsRequest,
    ) -> ddi_20200617_models.ListFlowClusterAllHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_cluster_all_hosts_with_options(request, runtime)

    async def list_flow_cluster_all_hosts_async(
        self,
        request: ddi_20200617_models.ListFlowClusterAllHostsRequest,
    ) -> ddi_20200617_models.ListFlowClusterAllHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_cluster_all_hosts_with_options_async(request, runtime)

    def delete_libraries_with_options(
        self,
        request: ddi_20200617_models.DeleteLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteLibrariesResponse(),
            self.do_rpcrequest('DeleteLibraries', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_libraries_with_options_async(
        self,
        request: ddi_20200617_models.DeleteLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteLibrariesResponse(),
            await self.do_rpcrequest_async('DeleteLibraries', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_libraries(
        self,
        request: ddi_20200617_models.DeleteLibrariesRequest,
    ) -> ddi_20200617_models.DeleteLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_libraries_with_options(request, runtime)

    async def delete_libraries_async(
        self,
        request: ddi_20200617_models.DeleteLibrariesRequest,
    ) -> ddi_20200617_models.DeleteLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_libraries_with_options_async(request, runtime)

    def describe_flow_category_tree_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowCategoryTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowCategoryTreeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowCategoryTreeResponse(),
            self.do_rpcrequest('DescribeFlowCategoryTree', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_category_tree_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowCategoryTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowCategoryTreeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowCategoryTreeResponse(),
            await self.do_rpcrequest_async('DescribeFlowCategoryTree', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_category_tree(
        self,
        request: ddi_20200617_models.DescribeFlowCategoryTreeRequest,
    ) -> ddi_20200617_models.DescribeFlowCategoryTreeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_category_tree_with_options(request, runtime)

    async def describe_flow_category_tree_async(
        self,
        request: ddi_20200617_models.DescribeFlowCategoryTreeRequest,
    ) -> ddi_20200617_models.DescribeFlowCategoryTreeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_category_tree_with_options_async(request, runtime)

    def list_datasource_instances_with_options(
        self,
        request: ddi_20200617_models.ListDatasourceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListDatasourceInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListDatasourceInstancesResponse(),
            self.do_rpcrequest('ListDatasourceInstances', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_datasource_instances_with_options_async(
        self,
        request: ddi_20200617_models.ListDatasourceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListDatasourceInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListDatasourceInstancesResponse(),
            await self.do_rpcrequest_async('ListDatasourceInstances', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_datasource_instances(
        self,
        request: ddi_20200617_models.ListDatasourceInstancesRequest,
    ) -> ddi_20200617_models.ListDatasourceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_datasource_instances_with_options(request, runtime)

    async def list_datasource_instances_async(
        self,
        request: ddi_20200617_models.ListDatasourceInstancesRequest,
    ) -> ddi_20200617_models.ListDatasourceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_datasource_instances_with_options_async(request, runtime)

    def list_flow_node_sql_result_with_options(
        self,
        request: ddi_20200617_models.ListFlowNodeSqlResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowNodeSqlResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowNodeSqlResultResponse(),
            self.do_rpcrequest('ListFlowNodeSqlResult', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_node_sql_result_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowNodeSqlResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowNodeSqlResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowNodeSqlResultResponse(),
            await self.do_rpcrequest_async('ListFlowNodeSqlResult', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_node_sql_result(
        self,
        request: ddi_20200617_models.ListFlowNodeSqlResultRequest,
    ) -> ddi_20200617_models.ListFlowNodeSqlResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_node_sql_result_with_options(request, runtime)

    async def list_flow_node_sql_result_async(
        self,
        request: ddi_20200617_models.ListFlowNodeSqlResultRequest,
    ) -> ddi_20200617_models.ListFlowNodeSqlResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_node_sql_result_with_options_async(request, runtime)

    def describe_flow_job_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowJobResponse(),
            self.do_rpcrequest('DescribeFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_job_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowJobResponse(),
            await self.do_rpcrequest_async('DescribeFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_job(
        self,
        request: ddi_20200617_models.DescribeFlowJobRequest,
    ) -> ddi_20200617_models.DescribeFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_job_with_options(request, runtime)

    async def describe_flow_job_async(
        self,
        request: ddi_20200617_models.DescribeFlowJobRequest,
    ) -> ddi_20200617_models.DescribeFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_job_with_options_async(request, runtime)

    def describe_library_install_task_detail_with_options(
        self,
        request: ddi_20200617_models.DescribeLibraryInstallTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeLibraryInstallTaskDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeLibraryInstallTaskDetailResponse(),
            self.do_rpcrequest('DescribeLibraryInstallTaskDetail', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_library_install_task_detail_with_options_async(
        self,
        request: ddi_20200617_models.DescribeLibraryInstallTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeLibraryInstallTaskDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeLibraryInstallTaskDetailResponse(),
            await self.do_rpcrequest_async('DescribeLibraryInstallTaskDetail', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_library_install_task_detail(
        self,
        request: ddi_20200617_models.DescribeLibraryInstallTaskDetailRequest,
    ) -> ddi_20200617_models.DescribeLibraryInstallTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_library_install_task_detail_with_options(request, runtime)

    async def describe_library_install_task_detail_async(
        self,
        request: ddi_20200617_models.DescribeLibraryInstallTaskDetailRequest,
    ) -> ddi_20200617_models.DescribeLibraryInstallTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_library_install_task_detail_with_options_async(request, runtime)

    def modify_flow_for_web_with_options(
        self,
        request: ddi_20200617_models.ModifyFlowForWebRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowForWebResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowForWebResponse(),
            self.do_rpcrequest('ModifyFlowForWeb', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_flow_for_web_with_options_async(
        self,
        request: ddi_20200617_models.ModifyFlowForWebRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowForWebResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowForWebResponse(),
            await self.do_rpcrequest_async('ModifyFlowForWeb', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_for_web(
        self,
        request: ddi_20200617_models.ModifyFlowForWebRequest,
    ) -> ddi_20200617_models.ModifyFlowForWebResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_for_web_with_options(request, runtime)

    async def modify_flow_for_web_async(
        self,
        request: ddi_20200617_models.ModifyFlowForWebRequest,
    ) -> ddi_20200617_models.ModifyFlowForWebResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_for_web_with_options_async(request, runtime)

    def remove_scaling_config_item_with_options(
        self,
        request: ddi_20200617_models.RemoveScalingConfigItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.RemoveScalingConfigItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.RemoveScalingConfigItemResponse(),
            self.do_rpcrequest('RemoveScalingConfigItem', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_scaling_config_item_with_options_async(
        self,
        request: ddi_20200617_models.RemoveScalingConfigItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.RemoveScalingConfigItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.RemoveScalingConfigItemResponse(),
            await self.do_rpcrequest_async('RemoveScalingConfigItem', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_scaling_config_item(
        self,
        request: ddi_20200617_models.RemoveScalingConfigItemRequest,
    ) -> ddi_20200617_models.RemoveScalingConfigItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_scaling_config_item_with_options(request, runtime)

    async def remove_scaling_config_item_async(
        self,
        request: ddi_20200617_models.RemoveScalingConfigItemRequest,
    ) -> ddi_20200617_models.RemoveScalingConfigItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_scaling_config_item_with_options_async(request, runtime)

    def describe_security_white_list_with_options(
        self,
        request: ddi_20200617_models.DescribeSecurityWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeSecurityWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeSecurityWhiteListResponse(),
            self.do_rpcrequest('DescribeSecurityWhiteList', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_white_list_with_options_async(
        self,
        request: ddi_20200617_models.DescribeSecurityWhiteListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeSecurityWhiteListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeSecurityWhiteListResponse(),
            await self.do_rpcrequest_async('DescribeSecurityWhiteList', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_white_list(
        self,
        request: ddi_20200617_models.DescribeSecurityWhiteListRequest,
    ) -> ddi_20200617_models.DescribeSecurityWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_white_list_with_options(request, runtime)

    async def describe_security_white_list_async(
        self,
        request: ddi_20200617_models.DescribeSecurityWhiteListRequest,
    ) -> ddi_20200617_models.DescribeSecurityWhiteListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_white_list_with_options_async(request, runtime)

    def describe_flow_node_instance_container_log_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceContainerLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceContainerLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowNodeInstanceContainerLogResponse(),
            self.do_rpcrequest('DescribeFlowNodeInstanceContainerLog', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_node_instance_container_log_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceContainerLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceContainerLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowNodeInstanceContainerLogResponse(),
            await self.do_rpcrequest_async('DescribeFlowNodeInstanceContainerLog', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_node_instance_container_log(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceContainerLogRequest,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceContainerLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_node_instance_container_log_with_options(request, runtime)

    async def describe_flow_node_instance_container_log_async(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceContainerLogRequest,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceContainerLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_node_instance_container_log_with_options_async(request, runtime)

    def rerun_flow_with_options(
        self,
        request: ddi_20200617_models.RerunFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.RerunFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.RerunFlowResponse(),
            self.do_rpcrequest('RerunFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rerun_flow_with_options_async(
        self,
        request: ddi_20200617_models.RerunFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.RerunFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.RerunFlowResponse(),
            await self.do_rpcrequest_async('RerunFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rerun_flow(
        self,
        request: ddi_20200617_models.RerunFlowRequest,
    ) -> ddi_20200617_models.RerunFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.rerun_flow_with_options(request, runtime)

    async def rerun_flow_async(
        self,
        request: ddi_20200617_models.RerunFlowRequest,
    ) -> ddi_20200617_models.RerunFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rerun_flow_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: ddi_20200617_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListTagKeysResponse(),
            self.do_rpcrequest('ListTagKeys', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: ddi_20200617_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListTagKeysResponse(),
            await self.do_rpcrequest_async('ListTagKeys', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_keys(
        self,
        request: ddi_20200617_models.ListTagKeysRequest,
    ) -> ddi_20200617_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: ddi_20200617_models.ListTagKeysRequest,
    ) -> ddi_20200617_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def describe_cluster_operation_host_task_log_with_options(
        self,
        request: ddi_20200617_models.DescribeClusterOperationHostTaskLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeClusterOperationHostTaskLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeClusterOperationHostTaskLogResponse(),
            self.do_rpcrequest('DescribeClusterOperationHostTaskLog', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_operation_host_task_log_with_options_async(
        self,
        request: ddi_20200617_models.DescribeClusterOperationHostTaskLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeClusterOperationHostTaskLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeClusterOperationHostTaskLogResponse(),
            await self.do_rpcrequest_async('DescribeClusterOperationHostTaskLog', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_operation_host_task_log(
        self,
        request: ddi_20200617_models.DescribeClusterOperationHostTaskLogRequest,
    ) -> ddi_20200617_models.DescribeClusterOperationHostTaskLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_operation_host_task_log_with_options(request, runtime)

    async def describe_cluster_operation_host_task_log_async(
        self,
        request: ddi_20200617_models.DescribeClusterOperationHostTaskLogRequest,
    ) -> ddi_20200617_models.DescribeClusterOperationHostTaskLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_operation_host_task_log_with_options_async(request, runtime)

    def kill_flow_job_with_options(
        self,
        request: ddi_20200617_models.KillFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.KillFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.KillFlowJobResponse(),
            self.do_rpcrequest('KillFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def kill_flow_job_with_options_async(
        self,
        request: ddi_20200617_models.KillFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.KillFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.KillFlowJobResponse(),
            await self.do_rpcrequest_async('KillFlowJob', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def kill_flow_job(
        self,
        request: ddi_20200617_models.KillFlowJobRequest,
    ) -> ddi_20200617_models.KillFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.kill_flow_job_with_options(request, runtime)

    async def kill_flow_job_async(
        self,
        request: ddi_20200617_models.KillFlowJobRequest,
    ) -> ddi_20200617_models.KillFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.kill_flow_job_with_options_async(request, runtime)

    def uninstall_libraries_with_options(
        self,
        request: ddi_20200617_models.UninstallLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.UninstallLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.UninstallLibrariesResponse(),
            self.do_rpcrequest('UninstallLibraries', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def uninstall_libraries_with_options_async(
        self,
        request: ddi_20200617_models.UninstallLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.UninstallLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.UninstallLibrariesResponse(),
            await self.do_rpcrequest_async('UninstallLibraries', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def uninstall_libraries(
        self,
        request: ddi_20200617_models.UninstallLibrariesRequest,
    ) -> ddi_20200617_models.UninstallLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return self.uninstall_libraries_with_options(request, runtime)

    async def uninstall_libraries_async(
        self,
        request: ddi_20200617_models.UninstallLibrariesRequest,
    ) -> ddi_20200617_models.UninstallLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.uninstall_libraries_with_options_async(request, runtime)

    def describe_cluster_v2with_options(
        self,
        request: ddi_20200617_models.DescribeClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeClusterV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeClusterV2Response(),
            self.do_rpcrequest('DescribeClusterV2', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_v2with_options_async(
        self,
        request: ddi_20200617_models.DescribeClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeClusterV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeClusterV2Response(),
            await self.do_rpcrequest_async('DescribeClusterV2', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_v2(
        self,
        request: ddi_20200617_models.DescribeClusterV2Request,
    ) -> ddi_20200617_models.DescribeClusterV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_v2with_options(request, runtime)

    async def describe_cluster_v2_async(
        self,
        request: ddi_20200617_models.DescribeClusterV2Request,
    ) -> ddi_20200617_models.DescribeClusterV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_v2with_options_async(request, runtime)

    def describe_flow_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowResponse(),
            self.do_rpcrequest('DescribeFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowResponse(),
            await self.do_rpcrequest_async('DescribeFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow(
        self,
        request: ddi_20200617_models.DescribeFlowRequest,
    ) -> ddi_20200617_models.DescribeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_with_options(request, runtime)

    async def describe_flow_async(
        self,
        request: ddi_20200617_models.DescribeFlowRequest,
    ) -> ddi_20200617_models.DescribeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_with_options_async(request, runtime)

    def list_flow_cluster_with_options(
        self,
        request: ddi_20200617_models.ListFlowClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterResponse(),
            self.do_rpcrequest('ListFlowCluster', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_cluster_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterResponse(),
            await self.do_rpcrequest_async('ListFlowCluster', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_cluster(
        self,
        request: ddi_20200617_models.ListFlowClusterRequest,
    ) -> ddi_20200617_models.ListFlowClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_cluster_with_options(request, runtime)

    async def list_flow_cluster_async(
        self,
        request: ddi_20200617_models.ListFlowClusterRequest,
    ) -> ddi_20200617_models.ListFlowClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_cluster_with_options_async(request, runtime)

    def list_ldap_users_with_options(
        self,
        request: ddi_20200617_models.ListLdapUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListLdapUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListLdapUsersResponse(),
            self.do_rpcrequest('ListLdapUsers', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_ldap_users_with_options_async(
        self,
        request: ddi_20200617_models.ListLdapUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListLdapUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListLdapUsersResponse(),
            await self.do_rpcrequest_async('ListLdapUsers', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ldap_users(
        self,
        request: ddi_20200617_models.ListLdapUsersRequest,
    ) -> ddi_20200617_models.ListLdapUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ldap_users_with_options(request, runtime)

    async def list_ldap_users_async(
        self,
        request: ddi_20200617_models.ListLdapUsersRequest,
    ) -> ddi_20200617_models.ListLdapUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ldap_users_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: ddi_20200617_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteUserResponse(),
            self.do_rpcrequest('DeleteUser', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: ddi_20200617_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteUserResponse(),
            await self.do_rpcrequest_async('DeleteUser', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user(
        self,
        request: ddi_20200617_models.DeleteUserRequest,
    ) -> ddi_20200617_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: ddi_20200617_models.DeleteUserRequest,
    ) -> ddi_20200617_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def create_flow_project_cluster_setting_with_options(
        self,
        request: ddi_20200617_models.CreateFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowProjectClusterSettingResponse(),
            self.do_rpcrequest('CreateFlowProjectClusterSetting', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_project_cluster_setting_with_options_async(
        self,
        request: ddi_20200617_models.CreateFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowProjectClusterSettingResponse(),
            await self.do_rpcrequest_async('CreateFlowProjectClusterSetting', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_project_cluster_setting(
        self,
        request: ddi_20200617_models.CreateFlowProjectClusterSettingRequest,
    ) -> ddi_20200617_models.CreateFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_project_cluster_setting_with_options(request, runtime)

    async def create_flow_project_cluster_setting_async(
        self,
        request: ddi_20200617_models.CreateFlowProjectClusterSettingRequest,
    ) -> ddi_20200617_models.CreateFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_project_cluster_setting_with_options_async(request, runtime)

    def describe_flow_instance_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowInstanceResponse(),
            self.do_rpcrequest('DescribeFlowInstance', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_instance_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowInstanceResponse(),
            await self.do_rpcrequest_async('DescribeFlowInstance', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_instance(
        self,
        request: ddi_20200617_models.DescribeFlowInstanceRequest,
    ) -> ddi_20200617_models.DescribeFlowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_instance_with_options(request, runtime)

    async def describe_flow_instance_async(
        self,
        request: ddi_20200617_models.DescribeFlowInstanceRequest,
    ) -> ddi_20200617_models.DescribeFlowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_instance_with_options_async(request, runtime)

    def create_flow_project_user_with_options(
        self,
        request: ddi_20200617_models.CreateFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowProjectUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowProjectUserResponse(),
            self.do_rpcrequest('CreateFlowProjectUser', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_project_user_with_options_async(
        self,
        request: ddi_20200617_models.CreateFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowProjectUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowProjectUserResponse(),
            await self.do_rpcrequest_async('CreateFlowProjectUser', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_project_user(
        self,
        request: ddi_20200617_models.CreateFlowProjectUserRequest,
    ) -> ddi_20200617_models.CreateFlowProjectUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_project_user_with_options(request, runtime)

    async def create_flow_project_user_async(
        self,
        request: ddi_20200617_models.CreateFlowProjectUserRequest,
    ) -> ddi_20200617_models.CreateFlowProjectUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_project_user_with_options_async(request, runtime)

    def create_flow_category_with_options(
        self,
        request: ddi_20200617_models.CreateFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowCategoryResponse(),
            self.do_rpcrequest('CreateFlowCategory', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_category_with_options_async(
        self,
        request: ddi_20200617_models.CreateFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowCategoryResponse(),
            await self.do_rpcrequest_async('CreateFlowCategory', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_category(
        self,
        request: ddi_20200617_models.CreateFlowCategoryRequest,
    ) -> ddi_20200617_models.CreateFlowCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_category_with_options(request, runtime)

    async def create_flow_category_async(
        self,
        request: ddi_20200617_models.CreateFlowCategoryRequest,
    ) -> ddi_20200617_models.CreateFlowCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_category_with_options_async(request, runtime)

    def delete_flow_project_cluster_setting_with_options(
        self,
        request: ddi_20200617_models.DeleteFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowProjectClusterSettingResponse(),
            self.do_rpcrequest('DeleteFlowProjectClusterSetting', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_project_cluster_setting_with_options_async(
        self,
        request: ddi_20200617_models.DeleteFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowProjectClusterSettingResponse(),
            await self.do_rpcrequest_async('DeleteFlowProjectClusterSetting', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_project_cluster_setting(
        self,
        request: ddi_20200617_models.DeleteFlowProjectClusterSettingRequest,
    ) -> ddi_20200617_models.DeleteFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_project_cluster_setting_with_options(request, runtime)

    async def delete_flow_project_cluster_setting_async(
        self,
        request: ddi_20200617_models.DeleteFlowProjectClusterSettingRequest,
    ) -> ddi_20200617_models.DeleteFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_project_cluster_setting_with_options_async(request, runtime)

    def list_libraries_with_options(
        self,
        request: ddi_20200617_models.ListLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListLibrariesResponse(),
            self.do_rpcrequest('ListLibraries', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_libraries_with_options_async(
        self,
        request: ddi_20200617_models.ListLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListLibrariesResponse(),
            await self.do_rpcrequest_async('ListLibraries', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_libraries(
        self,
        request: ddi_20200617_models.ListLibrariesRequest,
    ) -> ddi_20200617_models.ListLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_libraries_with_options(request, runtime)

    async def list_libraries_async(
        self,
        request: ddi_20200617_models.ListLibrariesRequest,
    ) -> ddi_20200617_models.ListLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_libraries_with_options_async(request, runtime)

    def run_scaling_action_with_options(
        self,
        request: ddi_20200617_models.RunScalingActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.RunScalingActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.RunScalingActionResponse(),
            self.do_rpcrequest('RunScalingAction', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_scaling_action_with_options_async(
        self,
        request: ddi_20200617_models.RunScalingActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.RunScalingActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.RunScalingActionResponse(),
            await self.do_rpcrequest_async('RunScalingAction', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_scaling_action(
        self,
        request: ddi_20200617_models.RunScalingActionRequest,
    ) -> ddi_20200617_models.RunScalingActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_scaling_action_with_options(request, runtime)

    async def run_scaling_action_async(
        self,
        request: ddi_20200617_models.RunScalingActionRequest,
    ) -> ddi_20200617_models.RunScalingActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_scaling_action_with_options_async(request, runtime)

    def install_libraries_with_options(
        self,
        request: ddi_20200617_models.InstallLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.InstallLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.InstallLibrariesResponse(),
            self.do_rpcrequest('InstallLibraries', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def install_libraries_with_options_async(
        self,
        request: ddi_20200617_models.InstallLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.InstallLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.InstallLibrariesResponse(),
            await self.do_rpcrequest_async('InstallLibraries', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def install_libraries(
        self,
        request: ddi_20200617_models.InstallLibrariesRequest,
    ) -> ddi_20200617_models.InstallLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_libraries_with_options(request, runtime)

    async def install_libraries_async(
        self,
        request: ddi_20200617_models.InstallLibrariesRequest,
    ) -> ddi_20200617_models.InstallLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_libraries_with_options_async(request, runtime)

    def list_flow_jobs_with_options(
        self,
        request: ddi_20200617_models.ListFlowJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowJobsResponse(),
            self.do_rpcrequest('ListFlowJobs', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_jobs_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowJobsResponse(),
            await self.do_rpcrequest_async('ListFlowJobs', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_jobs(
        self,
        request: ddi_20200617_models.ListFlowJobsRequest,
    ) -> ddi_20200617_models.ListFlowJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_jobs_with_options(request, runtime)

    async def list_flow_jobs_async(
        self,
        request: ddi_20200617_models.ListFlowJobsRequest,
    ) -> ddi_20200617_models.ListFlowJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_jobs_with_options_async(request, runtime)

    def modify_flow_with_options(
        self,
        request: ddi_20200617_models.ModifyFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowResponse(),
            self.do_rpcrequest('ModifyFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_flow_with_options_async(
        self,
        request: ddi_20200617_models.ModifyFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowResponse(),
            await self.do_rpcrequest_async('ModifyFlow', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow(
        self,
        request: ddi_20200617_models.ModifyFlowRequest,
    ) -> ddi_20200617_models.ModifyFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_with_options(request, runtime)

    async def modify_flow_async(
        self,
        request: ddi_20200617_models.ModifyFlowRequest,
    ) -> ddi_20200617_models.ModifyFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: ddi_20200617_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ddi_20200617_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeRegionsResponse(),
            await self.do_rpcrequest_async('DescribeRegions', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(
        self,
        request: ddi_20200617_models.DescribeRegionsRequest,
    ) -> ddi_20200617_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ddi_20200617_models.DescribeRegionsRequest,
    ) -> ddi_20200617_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def list_library_status_with_options(
        self,
        request: ddi_20200617_models.ListLibraryStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListLibraryStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListLibraryStatusResponse(),
            self.do_rpcrequest('ListLibraryStatus', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_library_status_with_options_async(
        self,
        request: ddi_20200617_models.ListLibraryStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListLibraryStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListLibraryStatusResponse(),
            await self.do_rpcrequest_async('ListLibraryStatus', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_library_status(
        self,
        request: ddi_20200617_models.ListLibraryStatusRequest,
    ) -> ddi_20200617_models.ListLibraryStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_library_status_with_options(request, runtime)

    async def list_library_status_async(
        self,
        request: ddi_20200617_models.ListLibraryStatusRequest,
    ) -> ddi_20200617_models.ListLibraryStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_library_status_with_options_async(request, runtime)

    def describe_cluster_service_config_with_options(
        self,
        request: ddi_20200617_models.DescribeClusterServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeClusterServiceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeClusterServiceConfigResponse(),
            self.do_rpcrequest('DescribeClusterServiceConfig', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_service_config_with_options_async(
        self,
        request: ddi_20200617_models.DescribeClusterServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeClusterServiceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeClusterServiceConfigResponse(),
            await self.do_rpcrequest_async('DescribeClusterServiceConfig', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_service_config(
        self,
        request: ddi_20200617_models.DescribeClusterServiceConfigRequest,
    ) -> ddi_20200617_models.DescribeClusterServiceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_service_config_with_options(request, runtime)

    async def describe_cluster_service_config_async(
        self,
        request: ddi_20200617_models.DescribeClusterServiceConfigRequest,
    ) -> ddi_20200617_models.DescribeClusterServiceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_service_config_with_options_async(request, runtime)

    def modify_flow_project_cluster_setting_with_options(
        self,
        request: ddi_20200617_models.ModifyFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowProjectClusterSettingResponse(),
            self.do_rpcrequest('ModifyFlowProjectClusterSetting', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_flow_project_cluster_setting_with_options_async(
        self,
        request: ddi_20200617_models.ModifyFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowProjectClusterSettingResponse(),
            await self.do_rpcrequest_async('ModifyFlowProjectClusterSetting', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_project_cluster_setting(
        self,
        request: ddi_20200617_models.ModifyFlowProjectClusterSettingRequest,
    ) -> ddi_20200617_models.ModifyFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_project_cluster_setting_with_options(request, runtime)

    async def modify_flow_project_cluster_setting_async(
        self,
        request: ddi_20200617_models.ModifyFlowProjectClusterSettingRequest,
    ) -> ddi_20200617_models.ModifyFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_project_cluster_setting_with_options_async(request, runtime)

    def delete_flow_project_user_with_options(
        self,
        request: ddi_20200617_models.DeleteFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowProjectUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowProjectUserResponse(),
            self.do_rpcrequest('DeleteFlowProjectUser', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_project_user_with_options_async(
        self,
        request: ddi_20200617_models.DeleteFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowProjectUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowProjectUserResponse(),
            await self.do_rpcrequest_async('DeleteFlowProjectUser', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_project_user(
        self,
        request: ddi_20200617_models.DeleteFlowProjectUserRequest,
    ) -> ddi_20200617_models.DeleteFlowProjectUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_project_user_with_options(request, runtime)

    async def delete_flow_project_user_async(
        self,
        request: ddi_20200617_models.DeleteFlowProjectUserRequest,
    ) -> ddi_20200617_models.DeleteFlowProjectUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_project_user_with_options_async(request, runtime)

    def create_cluster_v2with_options(
        self,
        request: ddi_20200617_models.CreateClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateClusterV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateClusterV2Response(),
            self.do_rpcrequest('CreateClusterV2', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cluster_v2with_options_async(
        self,
        request: ddi_20200617_models.CreateClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateClusterV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateClusterV2Response(),
            await self.do_rpcrequest_async('CreateClusterV2', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cluster_v2(
        self,
        request: ddi_20200617_models.CreateClusterV2Request,
    ) -> ddi_20200617_models.CreateClusterV2Response:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_v2with_options(request, runtime)

    async def create_cluster_v2_async(
        self,
        request: ddi_20200617_models.CreateClusterV2Request,
    ) -> ddi_20200617_models.CreateClusterV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_v2with_options_async(request, runtime)

    def modify_cluster_name_with_options(
        self,
        request: ddi_20200617_models.ModifyClusterNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyClusterNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyClusterNameResponse(),
            self.do_rpcrequest('ModifyClusterName', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cluster_name_with_options_async(
        self,
        request: ddi_20200617_models.ModifyClusterNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyClusterNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyClusterNameResponse(),
            await self.do_rpcrequest_async('ModifyClusterName', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cluster_name(
        self,
        request: ddi_20200617_models.ModifyClusterNameRequest,
    ) -> ddi_20200617_models.ModifyClusterNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_name_with_options(request, runtime)

    async def modify_cluster_name_async(
        self,
        request: ddi_20200617_models.ModifyClusterNameRequest,
    ) -> ddi_20200617_models.ModifyClusterNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_name_with_options_async(request, runtime)

    def list_cluster_operation_host_task_with_options(
        self,
        request: ddi_20200617_models.ListClusterOperationHostTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClusterOperationHostTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterOperationHostTaskResponse(),
            self.do_rpcrequest('ListClusterOperationHostTask', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_operation_host_task_with_options_async(
        self,
        request: ddi_20200617_models.ListClusterOperationHostTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClusterOperationHostTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterOperationHostTaskResponse(),
            await self.do_rpcrequest_async('ListClusterOperationHostTask', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_operation_host_task(
        self,
        request: ddi_20200617_models.ListClusterOperationHostTaskRequest,
    ) -> ddi_20200617_models.ListClusterOperationHostTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_operation_host_task_with_options(request, runtime)

    async def list_cluster_operation_host_task_async(
        self,
        request: ddi_20200617_models.ListClusterOperationHostTaskRequest,
    ) -> ddi_20200617_models.ListClusterOperationHostTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_operation_host_task_with_options_async(request, runtime)

    def describe_scaling_config_item_with_options(
        self,
        request: ddi_20200617_models.DescribeScalingConfigItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeScalingConfigItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeScalingConfigItemResponse(),
            self.do_rpcrequest('DescribeScalingConfigItem', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scaling_config_item_with_options_async(
        self,
        request: ddi_20200617_models.DescribeScalingConfigItemRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeScalingConfigItemResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeScalingConfigItemResponse(),
            await self.do_rpcrequest_async('DescribeScalingConfigItem', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_config_item(
        self,
        request: ddi_20200617_models.DescribeScalingConfigItemRequest,
    ) -> ddi_20200617_models.DescribeScalingConfigItemResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_config_item_with_options(request, runtime)

    async def describe_scaling_config_item_async(
        self,
        request: ddi_20200617_models.DescribeScalingConfigItemRequest,
    ) -> ddi_20200617_models.DescribeScalingConfigItemResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_config_item_with_options_async(request, runtime)

    def list_cluster_host_with_options(
        self,
        request: ddi_20200617_models.ListClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterHostResponse(),
            self.do_rpcrequest('ListClusterHost', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_host_with_options_async(
        self,
        request: ddi_20200617_models.ListClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClusterHostResponse(),
            await self.do_rpcrequest_async('ListClusterHost', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_host(
        self,
        request: ddi_20200617_models.ListClusterHostRequest,
    ) -> ddi_20200617_models.ListClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_host_with_options(request, runtime)

    async def list_cluster_host_async(
        self,
        request: ddi_20200617_models.ListClusterHostRequest,
    ) -> ddi_20200617_models.ListClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_host_with_options_async(request, runtime)

    def create_scaling_group_with_options(
        self,
        request: ddi_20200617_models.CreateScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateScalingGroupResponse(),
            self.do_rpcrequest('CreateScalingGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_scaling_group_with_options_async(
        self,
        request: ddi_20200617_models.CreateScalingGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateScalingGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateScalingGroupResponse(),
            await self.do_rpcrequest_async('CreateScalingGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scaling_group(
        self,
        request: ddi_20200617_models.CreateScalingGroupRequest,
    ) -> ddi_20200617_models.CreateScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_group_with_options(request, runtime)

    async def create_scaling_group_async(
        self,
        request: ddi_20200617_models.CreateScalingGroupRequest,
    ) -> ddi_20200617_models.CreateScalingGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scaling_group_with_options_async(request, runtime)

    def describe_cluster_service_with_options(
        self,
        request: ddi_20200617_models.DescribeClusterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeClusterServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeClusterServiceResponse(),
            self.do_rpcrequest('DescribeClusterService', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_service_with_options_async(
        self,
        request: ddi_20200617_models.DescribeClusterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeClusterServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeClusterServiceResponse(),
            await self.do_rpcrequest_async('DescribeClusterService', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_service(
        self,
        request: ddi_20200617_models.DescribeClusterServiceRequest,
    ) -> ddi_20200617_models.DescribeClusterServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_service_with_options(request, runtime)

    async def describe_cluster_service_async(
        self,
        request: ddi_20200617_models.DescribeClusterServiceRequest,
    ) -> ddi_20200617_models.DescribeClusterServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_service_with_options_async(request, runtime)

    def list_flow_projects_with_options(
        self,
        request: ddi_20200617_models.ListFlowProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowProjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowProjectsResponse(),
            self.do_rpcrequest('ListFlowProjects', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_projects_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowProjectsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowProjectsResponse(),
            await self.do_rpcrequest_async('ListFlowProjects', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_projects(
        self,
        request: ddi_20200617_models.ListFlowProjectsRequest,
    ) -> ddi_20200617_models.ListFlowProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_projects_with_options(request, runtime)

    async def list_flow_projects_async(
        self,
        request: ddi_20200617_models.ListFlowProjectsRequest,
    ) -> ddi_20200617_models.ListFlowProjectsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_projects_with_options_async(request, runtime)

    def create_meta_table_preview_task_with_options(
        self,
        request: ddi_20200617_models.CreateMetaTablePreviewTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateMetaTablePreviewTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateMetaTablePreviewTaskResponse(),
            self.do_rpcrequest('CreateMetaTablePreviewTask', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_meta_table_preview_task_with_options_async(
        self,
        request: ddi_20200617_models.CreateMetaTablePreviewTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateMetaTablePreviewTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateMetaTablePreviewTaskResponse(),
            await self.do_rpcrequest_async('CreateMetaTablePreviewTask', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_meta_table_preview_task(
        self,
        request: ddi_20200617_models.CreateMetaTablePreviewTaskRequest,
    ) -> ddi_20200617_models.CreateMetaTablePreviewTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_meta_table_preview_task_with_options(request, runtime)

    async def create_meta_table_preview_task_async(
        self,
        request: ddi_20200617_models.CreateMetaTablePreviewTaskRequest,
    ) -> ddi_20200617_models.CreateMetaTablePreviewTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_meta_table_preview_task_with_options_async(request, runtime)

    def list_flow_project_user_with_options(
        self,
        request: ddi_20200617_models.ListFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowProjectUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowProjectUserResponse(),
            self.do_rpcrequest('ListFlowProjectUser', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_project_user_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowProjectUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowProjectUserResponse(),
            await self.do_rpcrequest_async('ListFlowProjectUser', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_project_user(
        self,
        request: ddi_20200617_models.ListFlowProjectUserRequest,
    ) -> ddi_20200617_models.ListFlowProjectUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_project_user_with_options(request, runtime)

    async def list_flow_project_user_async(
        self,
        request: ddi_20200617_models.ListFlowProjectUserRequest,
    ) -> ddi_20200617_models.ListFlowProjectUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_project_user_with_options_async(request, runtime)

    def delete_cluster_host_group_with_options(
        self,
        request: ddi_20200617_models.DeleteClusterHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteClusterHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteClusterHostGroupResponse(),
            self.do_rpcrequest('DeleteClusterHostGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_cluster_host_group_with_options_async(
        self,
        request: ddi_20200617_models.DeleteClusterHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteClusterHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteClusterHostGroupResponse(),
            await self.do_rpcrequest_async('DeleteClusterHostGroup', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cluster_host_group(
        self,
        request: ddi_20200617_models.DeleteClusterHostGroupRequest,
    ) -> ddi_20200617_models.DeleteClusterHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_host_group_with_options(request, runtime)

    async def delete_cluster_host_group_async(
        self,
        request: ddi_20200617_models.DeleteClusterHostGroupRequest,
    ) -> ddi_20200617_models.DeleteClusterHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_host_group_with_options_async(request, runtime)

    def describe_library_detail_with_options(
        self,
        request: ddi_20200617_models.DescribeLibraryDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeLibraryDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeLibraryDetailResponse(),
            self.do_rpcrequest('DescribeLibraryDetail', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_library_detail_with_options_async(
        self,
        request: ddi_20200617_models.DescribeLibraryDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeLibraryDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeLibraryDetailResponse(),
            await self.do_rpcrequest_async('DescribeLibraryDetail', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_library_detail(
        self,
        request: ddi_20200617_models.DescribeLibraryDetailRequest,
    ) -> ddi_20200617_models.DescribeLibraryDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_library_detail_with_options(request, runtime)

    async def describe_library_detail_async(
        self,
        request: ddi_20200617_models.DescribeLibraryDetailRequest,
    ) -> ddi_20200617_models.DescribeLibraryDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_library_detail_with_options_async(request, runtime)

    def list_flows_with_options(
        self,
        request: ddi_20200617_models.ListFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowsResponse(),
            self.do_rpcrequest('ListFlows', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flows_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowsResponse(),
            await self.do_rpcrequest_async('ListFlows', '2020-06-17', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flows(
        self,
        request: ddi_20200617_models.ListFlowsRequest,
    ) -> ddi_20200617_models.ListFlowsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flows_with_options(request, runtime)

    async def list_flows_async(
        self,
        request: ddi_20200617_models.ListFlowsRequest,
    ) -> ddi_20200617_models.ListFlowsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flows_with_options_async(request, runtime)
