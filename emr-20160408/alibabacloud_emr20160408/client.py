# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_emr20160408 import models as emr_20160408_models
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
            'cn-beijing': 'emr.aliyuncs.com',
            'cn-hangzhou': 'emr.aliyuncs.com',
            'cn-shanghai': 'emr.aliyuncs.com',
            'cn-shenzhen': 'emr.aliyuncs.com',
            'ap-southeast-1': 'emr.aliyuncs.com',
            'us-west-1': 'emr.aliyuncs.com',
            'cn-hangzhou-finance': 'emr.aliyuncs.com',
            'cn-shenzhen-finance-1': 'emr.aliyuncs.com',
            'cn-shanghai-finance-1': 'emr.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('emr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_cluster_service_with_options(
        self,
        request: emr_20160408_models.AddClusterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.AddClusterServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.AddClusterServiceResponse().from_map(
            self.do_rpcrequest('AddClusterService', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_cluster_service_with_options_async(
        self,
        request: emr_20160408_models.AddClusterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.AddClusterServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.AddClusterServiceResponse().from_map(
            await self.do_rpcrequest_async('AddClusterService', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_cluster_service(
        self,
        request: emr_20160408_models.AddClusterServiceRequest,
    ) -> emr_20160408_models.AddClusterServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_cluster_service_with_options(request, runtime)

    async def add_cluster_service_async(
        self,
        request: emr_20160408_models.AddClusterServiceRequest,
    ) -> emr_20160408_models.AddClusterServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_cluster_service_with_options_async(request, runtime)

    def add_scaling_config_item_v2with_options(
        self,
        request: emr_20160408_models.AddScalingConfigItemV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.AddScalingConfigItemV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.AddScalingConfigItemV2Response().from_map(
            self.do_rpcrequest('AddScalingConfigItemV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_scaling_config_item_v2with_options_async(
        self,
        request: emr_20160408_models.AddScalingConfigItemV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.AddScalingConfigItemV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.AddScalingConfigItemV2Response().from_map(
            await self.do_rpcrequest_async('AddScalingConfigItemV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_scaling_config_item_v2(
        self,
        request: emr_20160408_models.AddScalingConfigItemV2Request,
    ) -> emr_20160408_models.AddScalingConfigItemV2Response:
        runtime = util_models.RuntimeOptions()
        return self.add_scaling_config_item_v2with_options(request, runtime)

    async def add_scaling_config_item_v2_async(
        self,
        request: emr_20160408_models.AddScalingConfigItemV2Request,
    ) -> emr_20160408_models.AddScalingConfigItemV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.add_scaling_config_item_v2with_options_async(request, runtime)

    def authorize_security_group_with_options(
        self,
        request: emr_20160408_models.AuthorizeSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.AuthorizeSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.AuthorizeSecurityGroupResponse().from_map(
            self.do_rpcrequest('AuthorizeSecurityGroup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def authorize_security_group_with_options_async(
        self,
        request: emr_20160408_models.AuthorizeSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.AuthorizeSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.AuthorizeSecurityGroupResponse().from_map(
            await self.do_rpcrequest_async('AuthorizeSecurityGroup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def authorize_security_group(
        self,
        request: emr_20160408_models.AuthorizeSecurityGroupRequest,
    ) -> emr_20160408_models.AuthorizeSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.authorize_security_group_with_options(request, runtime)

    async def authorize_security_group_async(
        self,
        request: emr_20160408_models.AuthorizeSecurityGroupRequest,
    ) -> emr_20160408_models.AuthorizeSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.authorize_security_group_with_options_async(request, runtime)

    def cancel_order_with_options(
        self,
        request: emr_20160408_models.CancelOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CancelOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CancelOrderResponse().from_map(
            self.do_rpcrequest('CancelOrder', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cancel_order_with_options_async(
        self,
        request: emr_20160408_models.CancelOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CancelOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CancelOrderResponse().from_map(
            await self.do_rpcrequest_async('CancelOrder', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_order(
        self,
        request: emr_20160408_models.CancelOrderRequest,
    ) -> emr_20160408_models.CancelOrderResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_order_with_options(request, runtime)

    async def cancel_order_async(
        self,
        request: emr_20160408_models.CancelOrderRequest,
    ) -> emr_20160408_models.CancelOrderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_order_with_options_async(request, runtime)

    def cleanup_flow_entity_snapshot_with_options(
        self,
        request: emr_20160408_models.CleanupFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CleanupFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CleanupFlowEntitySnapshotResponse().from_map(
            self.do_rpcrequest('CleanupFlowEntitySnapshot', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def cleanup_flow_entity_snapshot_with_options_async(
        self,
        request: emr_20160408_models.CleanupFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CleanupFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CleanupFlowEntitySnapshotResponse().from_map(
            await self.do_rpcrequest_async('CleanupFlowEntitySnapshot', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cleanup_flow_entity_snapshot(
        self,
        request: emr_20160408_models.CleanupFlowEntitySnapshotRequest,
    ) -> emr_20160408_models.CleanupFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.cleanup_flow_entity_snapshot_with_options(request, runtime)

    async def cleanup_flow_entity_snapshot_async(
        self,
        request: emr_20160408_models.CleanupFlowEntitySnapshotRequest,
    ) -> emr_20160408_models.CleanupFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cleanup_flow_entity_snapshot_with_options_async(request, runtime)

    def clone_flow_with_options(
        self,
        request: emr_20160408_models.CloneFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CloneFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CloneFlowResponse().from_map(
            self.do_rpcrequest('CloneFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clone_flow_with_options_async(
        self,
        request: emr_20160408_models.CloneFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CloneFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CloneFlowResponse().from_map(
            await self.do_rpcrequest_async('CloneFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clone_flow(
        self,
        request: emr_20160408_models.CloneFlowRequest,
    ) -> emr_20160408_models.CloneFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.clone_flow_with_options(request, runtime)

    async def clone_flow_async(
        self,
        request: emr_20160408_models.CloneFlowRequest,
    ) -> emr_20160408_models.CloneFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clone_flow_with_options_async(request, runtime)

    def clone_flow_job_with_options(
        self,
        request: emr_20160408_models.CloneFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CloneFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CloneFlowJobResponse().from_map(
            self.do_rpcrequest('CloneFlowJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clone_flow_job_with_options_async(
        self,
        request: emr_20160408_models.CloneFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CloneFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CloneFlowJobResponse().from_map(
            await self.do_rpcrequest_async('CloneFlowJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clone_flow_job(
        self,
        request: emr_20160408_models.CloneFlowJobRequest,
    ) -> emr_20160408_models.CloneFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.clone_flow_job_with_options(request, runtime)

    async def clone_flow_job_async(
        self,
        request: emr_20160408_models.CloneFlowJobRequest,
    ) -> emr_20160408_models.CloneFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clone_flow_job_with_options_async(request, runtime)

    def commit_flow_entity_snapshot_with_options(
        self,
        request: emr_20160408_models.CommitFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CommitFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CommitFlowEntitySnapshotResponse().from_map(
            self.do_rpcrequest('CommitFlowEntitySnapshot', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def commit_flow_entity_snapshot_with_options_async(
        self,
        request: emr_20160408_models.CommitFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CommitFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CommitFlowEntitySnapshotResponse().from_map(
            await self.do_rpcrequest_async('CommitFlowEntitySnapshot', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def commit_flow_entity_snapshot(
        self,
        request: emr_20160408_models.CommitFlowEntitySnapshotRequest,
    ) -> emr_20160408_models.CommitFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.commit_flow_entity_snapshot_with_options(request, runtime)

    async def commit_flow_entity_snapshot_async(
        self,
        request: emr_20160408_models.CommitFlowEntitySnapshotRequest,
    ) -> emr_20160408_models.CommitFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.commit_flow_entity_snapshot_with_options_async(request, runtime)

    def create_backup_with_options(
        self,
        request: emr_20160408_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateBackupResponse().from_map(
            self.do_rpcrequest('CreateBackup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_backup_with_options_async(
        self,
        request: emr_20160408_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateBackupResponse().from_map(
            await self.do_rpcrequest_async('CreateBackup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_backup(
        self,
        request: emr_20160408_models.CreateBackupRequest,
    ) -> emr_20160408_models.CreateBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    async def create_backup_async(
        self,
        request: emr_20160408_models.CreateBackupRequest,
    ) -> emr_20160408_models.CreateBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_with_options_async(request, runtime)

    def create_backup_plan_with_options(
        self,
        request: emr_20160408_models.CreateBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateBackupPlanResponse().from_map(
            self.do_rpcrequest('CreateBackupPlan', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_backup_plan_with_options_async(
        self,
        request: emr_20160408_models.CreateBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateBackupPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateBackupPlanResponse().from_map(
            await self.do_rpcrequest_async('CreateBackupPlan', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_backup_plan(
        self,
        request: emr_20160408_models.CreateBackupPlanRequest,
    ) -> emr_20160408_models.CreateBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_backup_plan_with_options(request, runtime)

    async def create_backup_plan_async(
        self,
        request: emr_20160408_models.CreateBackupPlanRequest,
    ) -> emr_20160408_models.CreateBackupPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_plan_with_options_async(request, runtime)

    def create_cluster_bootstrap_action_with_options(
        self,
        request: emr_20160408_models.CreateClusterBootstrapActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateClusterBootstrapActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateClusterBootstrapActionResponse().from_map(
            self.do_rpcrequest('CreateClusterBootstrapAction', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cluster_bootstrap_action_with_options_async(
        self,
        request: emr_20160408_models.CreateClusterBootstrapActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateClusterBootstrapActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateClusterBootstrapActionResponse().from_map(
            await self.do_rpcrequest_async('CreateClusterBootstrapAction', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cluster_bootstrap_action(
        self,
        request: emr_20160408_models.CreateClusterBootstrapActionRequest,
    ) -> emr_20160408_models.CreateClusterBootstrapActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_bootstrap_action_with_options(request, runtime)

    async def create_cluster_bootstrap_action_async(
        self,
        request: emr_20160408_models.CreateClusterBootstrapActionRequest,
    ) -> emr_20160408_models.CreateClusterBootstrapActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_bootstrap_action_with_options_async(request, runtime)

    def create_cluster_template_with_options(
        self,
        request: emr_20160408_models.CreateClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateClusterTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateClusterTemplateResponse().from_map(
            self.do_rpcrequest('CreateClusterTemplate', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cluster_template_with_options_async(
        self,
        request: emr_20160408_models.CreateClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateClusterTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateClusterTemplateResponse().from_map(
            await self.do_rpcrequest_async('CreateClusterTemplate', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cluster_template(
        self,
        request: emr_20160408_models.CreateClusterTemplateRequest,
    ) -> emr_20160408_models.CreateClusterTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_template_with_options(request, runtime)

    async def create_cluster_template_async(
        self,
        request: emr_20160408_models.CreateClusterTemplateRequest,
    ) -> emr_20160408_models.CreateClusterTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_template_with_options_async(request, runtime)

    def create_cluster_v2with_options(
        self,
        request: emr_20160408_models.CreateClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateClusterV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateClusterV2Response().from_map(
            self.do_rpcrequest('CreateClusterV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cluster_v2with_options_async(
        self,
        request: emr_20160408_models.CreateClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateClusterV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateClusterV2Response().from_map(
            await self.do_rpcrequest_async('CreateClusterV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cluster_v2(
        self,
        request: emr_20160408_models.CreateClusterV2Request,
    ) -> emr_20160408_models.CreateClusterV2Response:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_v2with_options(request, runtime)

    async def create_cluster_v2_async(
        self,
        request: emr_20160408_models.CreateClusterV2Request,
    ) -> emr_20160408_models.CreateClusterV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_v2with_options_async(request, runtime)

    def create_cluster_with_template_with_options(
        self,
        request: emr_20160408_models.CreateClusterWithTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateClusterWithTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateClusterWithTemplateResponse().from_map(
            self.do_rpcrequest('CreateClusterWithTemplate', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cluster_with_template_with_options_async(
        self,
        request: emr_20160408_models.CreateClusterWithTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateClusterWithTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateClusterWithTemplateResponse().from_map(
            await self.do_rpcrequest_async('CreateClusterWithTemplate', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cluster_with_template(
        self,
        request: emr_20160408_models.CreateClusterWithTemplateRequest,
    ) -> emr_20160408_models.CreateClusterWithTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_template_with_options(request, runtime)

    async def create_cluster_with_template_async(
        self,
        request: emr_20160408_models.CreateClusterWithTemplateRequest,
    ) -> emr_20160408_models.CreateClusterWithTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_template_with_options_async(request, runtime)

    def create_data_source_with_options(
        self,
        request: emr_20160408_models.CreateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateDataSourceResponse().from_map(
            self.do_rpcrequest('CreateDataSource', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_data_source_with_options_async(
        self,
        request: emr_20160408_models.CreateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateDataSourceResponse().from_map(
            await self.do_rpcrequest_async('CreateDataSource', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_data_source(
        self,
        request: emr_20160408_models.CreateDataSourceRequest,
    ) -> emr_20160408_models.CreateDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_data_source_with_options(request, runtime)

    async def create_data_source_async(
        self,
        request: emr_20160408_models.CreateDataSourceRequest,
    ) -> emr_20160408_models.CreateDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_data_source_with_options_async(request, runtime)

    def create_execution_plan_with_options(
        self,
        request: emr_20160408_models.CreateExecutionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateExecutionPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateExecutionPlanResponse().from_map(
            self.do_rpcrequest('CreateExecutionPlan', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_execution_plan_with_options_async(
        self,
        request: emr_20160408_models.CreateExecutionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateExecutionPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateExecutionPlanResponse().from_map(
            await self.do_rpcrequest_async('CreateExecutionPlan', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_execution_plan(
        self,
        request: emr_20160408_models.CreateExecutionPlanRequest,
    ) -> emr_20160408_models.CreateExecutionPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_execution_plan_with_options(request, runtime)

    async def create_execution_plan_async(
        self,
        request: emr_20160408_models.CreateExecutionPlanRequest,
    ) -> emr_20160408_models.CreateExecutionPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_execution_plan_with_options_async(request, runtime)

    def create_flow_with_options(
        self,
        request: emr_20160408_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateFlowResponse().from_map(
            self.do_rpcrequest('CreateFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_with_options_async(
        self,
        request: emr_20160408_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateFlowResponse().from_map(
            await self.do_rpcrequest_async('CreateFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow(
        self,
        request: emr_20160408_models.CreateFlowRequest,
    ) -> emr_20160408_models.CreateFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_with_options(request, runtime)

    async def create_flow_async(
        self,
        request: emr_20160408_models.CreateFlowRequest,
    ) -> emr_20160408_models.CreateFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_with_options_async(request, runtime)

    def create_flow_category_with_options(
        self,
        request: emr_20160408_models.CreateFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateFlowCategoryResponse().from_map(
            self.do_rpcrequest('CreateFlowCategory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_category_with_options_async(
        self,
        request: emr_20160408_models.CreateFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateFlowCategoryResponse().from_map(
            await self.do_rpcrequest_async('CreateFlowCategory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_category(
        self,
        request: emr_20160408_models.CreateFlowCategoryRequest,
    ) -> emr_20160408_models.CreateFlowCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_category_with_options(request, runtime)

    async def create_flow_category_async(
        self,
        request: emr_20160408_models.CreateFlowCategoryRequest,
    ) -> emr_20160408_models.CreateFlowCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_category_with_options_async(request, runtime)

    def create_flow_edit_lock_with_options(
        self,
        request: emr_20160408_models.CreateFlowEditLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowEditLockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateFlowEditLockResponse().from_map(
            self.do_rpcrequest('CreateFlowEditLock', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_edit_lock_with_options_async(
        self,
        request: emr_20160408_models.CreateFlowEditLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowEditLockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateFlowEditLockResponse().from_map(
            await self.do_rpcrequest_async('CreateFlowEditLock', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_edit_lock(
        self,
        request: emr_20160408_models.CreateFlowEditLockRequest,
    ) -> emr_20160408_models.CreateFlowEditLockResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_edit_lock_with_options(request, runtime)

    async def create_flow_edit_lock_async(
        self,
        request: emr_20160408_models.CreateFlowEditLockRequest,
    ) -> emr_20160408_models.CreateFlowEditLockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_edit_lock_with_options_async(request, runtime)

    def create_flow_for_web_with_options(
        self,
        request: emr_20160408_models.CreateFlowForWebRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowForWebResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateFlowForWebResponse().from_map(
            self.do_rpcrequest('CreateFlowForWeb', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_for_web_with_options_async(
        self,
        request: emr_20160408_models.CreateFlowForWebRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowForWebResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateFlowForWebResponse().from_map(
            await self.do_rpcrequest_async('CreateFlowForWeb', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_for_web(
        self,
        request: emr_20160408_models.CreateFlowForWebRequest,
    ) -> emr_20160408_models.CreateFlowForWebResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_for_web_with_options(request, runtime)

    async def create_flow_for_web_async(
        self,
        request: emr_20160408_models.CreateFlowForWebRequest,
    ) -> emr_20160408_models.CreateFlowForWebResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_for_web_with_options_async(request, runtime)

    def create_flow_job_with_options(
        self,
        request: emr_20160408_models.CreateFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateFlowJobResponse().from_map(
            self.do_rpcrequest('CreateFlowJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_job_with_options_async(
        self,
        request: emr_20160408_models.CreateFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateFlowJobResponse().from_map(
            await self.do_rpcrequest_async('CreateFlowJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_job(
        self,
        request: emr_20160408_models.CreateFlowJobRequest,
    ) -> emr_20160408_models.CreateFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_job_with_options(request, runtime)

    async def create_flow_job_async(
        self,
        request: emr_20160408_models.CreateFlowJobRequest,
    ) -> emr_20160408_models.CreateFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_job_with_options_async(request, runtime)

    def create_flow_project_with_options(
        self,
        request: emr_20160408_models.CreateFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateFlowProjectResponse().from_map(
            self.do_rpcrequest('CreateFlowProject', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_project_with_options_async(
        self,
        request: emr_20160408_models.CreateFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateFlowProjectResponse().from_map(
            await self.do_rpcrequest_async('CreateFlowProject', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_project(
        self,
        request: emr_20160408_models.CreateFlowProjectRequest,
    ) -> emr_20160408_models.CreateFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_project_with_options(request, runtime)

    async def create_flow_project_async(
        self,
        request: emr_20160408_models.CreateFlowProjectRequest,
    ) -> emr_20160408_models.CreateFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_project_with_options_async(request, runtime)

    def create_flow_project_cluster_setting_with_options(
        self,
        request: emr_20160408_models.CreateFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateFlowProjectClusterSettingResponse().from_map(
            self.do_rpcrequest('CreateFlowProjectClusterSetting', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_project_cluster_setting_with_options_async(
        self,
        request: emr_20160408_models.CreateFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateFlowProjectClusterSettingResponse().from_map(
            await self.do_rpcrequest_async('CreateFlowProjectClusterSetting', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_project_cluster_setting(
        self,
        request: emr_20160408_models.CreateFlowProjectClusterSettingRequest,
    ) -> emr_20160408_models.CreateFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_project_cluster_setting_with_options(request, runtime)

    async def create_flow_project_cluster_setting_async(
        self,
        request: emr_20160408_models.CreateFlowProjectClusterSettingRequest,
    ) -> emr_20160408_models.CreateFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_project_cluster_setting_with_options_async(request, runtime)

    def create_flow_project_user_with_options(
        self,
        request: emr_20160408_models.CreateFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowProjectUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateFlowProjectUserResponse().from_map(
            self.do_rpcrequest('CreateFlowProjectUser', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_project_user_with_options_async(
        self,
        request: emr_20160408_models.CreateFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowProjectUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateFlowProjectUserResponse().from_map(
            await self.do_rpcrequest_async('CreateFlowProjectUser', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow_project_user(
        self,
        request: emr_20160408_models.CreateFlowProjectUserRequest,
    ) -> emr_20160408_models.CreateFlowProjectUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_project_user_with_options(request, runtime)

    async def create_flow_project_user_async(
        self,
        request: emr_20160408_models.CreateFlowProjectUserRequest,
    ) -> emr_20160408_models.CreateFlowProjectUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_project_user_with_options_async(request, runtime)

    def create_job_with_options(
        self,
        request: emr_20160408_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateJobResponse().from_map(
            self.do_rpcrequest('CreateJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_job_with_options_async(
        self,
        request: emr_20160408_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateJobResponse().from_map(
            await self.do_rpcrequest_async('CreateJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_job(
        self,
        request: emr_20160408_models.CreateJobRequest,
    ) -> emr_20160408_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_job_with_options(request, runtime)

    async def create_job_async(
        self,
        request: emr_20160408_models.CreateJobRequest,
    ) -> emr_20160408_models.CreateJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_job_with_options_async(request, runtime)

    def create_library_with_options(
        self,
        request: emr_20160408_models.CreateLibraryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateLibraryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateLibraryResponse().from_map(
            self.do_rpcrequest('CreateLibrary', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_library_with_options_async(
        self,
        request: emr_20160408_models.CreateLibraryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateLibraryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateLibraryResponse().from_map(
            await self.do_rpcrequest_async('CreateLibrary', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_library(
        self,
        request: emr_20160408_models.CreateLibraryRequest,
    ) -> emr_20160408_models.CreateLibraryResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_library_with_options(request, runtime)

    async def create_library_async(
        self,
        request: emr_20160408_models.CreateLibraryRequest,
    ) -> emr_20160408_models.CreateLibraryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_library_with_options_async(request, runtime)

    def create_meta_table_preview_task_with_options(
        self,
        request: emr_20160408_models.CreateMetaTablePreviewTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateMetaTablePreviewTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateMetaTablePreviewTaskResponse().from_map(
            self.do_rpcrequest('CreateMetaTablePreviewTask', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_meta_table_preview_task_with_options_async(
        self,
        request: emr_20160408_models.CreateMetaTablePreviewTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateMetaTablePreviewTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateMetaTablePreviewTaskResponse().from_map(
            await self.do_rpcrequest_async('CreateMetaTablePreviewTask', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_meta_table_preview_task(
        self,
        request: emr_20160408_models.CreateMetaTablePreviewTaskRequest,
    ) -> emr_20160408_models.CreateMetaTablePreviewTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_meta_table_preview_task_with_options(request, runtime)

    async def create_meta_table_preview_task_async(
        self,
        request: emr_20160408_models.CreateMetaTablePreviewTaskRequest,
    ) -> emr_20160408_models.CreateMetaTablePreviewTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_meta_table_preview_task_with_options_async(request, runtime)

    def create_note_with_options(
        self,
        request: emr_20160408_models.CreateNoteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateNoteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateNoteResponse().from_map(
            self.do_rpcrequest('CreateNote', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_note_with_options_async(
        self,
        request: emr_20160408_models.CreateNoteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateNoteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateNoteResponse().from_map(
            await self.do_rpcrequest_async('CreateNote', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_note(
        self,
        request: emr_20160408_models.CreateNoteRequest,
    ) -> emr_20160408_models.CreateNoteResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_note_with_options(request, runtime)

    async def create_note_async(
        self,
        request: emr_20160408_models.CreateNoteRequest,
    ) -> emr_20160408_models.CreateNoteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_note_with_options_async(request, runtime)

    def create_paragraph_with_options(
        self,
        request: emr_20160408_models.CreateParagraphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateParagraphResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateParagraphResponse().from_map(
            self.do_rpcrequest('CreateParagraph', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_paragraph_with_options_async(
        self,
        request: emr_20160408_models.CreateParagraphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateParagraphResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateParagraphResponse().from_map(
            await self.do_rpcrequest_async('CreateParagraph', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_paragraph(
        self,
        request: emr_20160408_models.CreateParagraphRequest,
    ) -> emr_20160408_models.CreateParagraphResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_paragraph_with_options(request, runtime)

    async def create_paragraph_async(
        self,
        request: emr_20160408_models.CreateParagraphRequest,
    ) -> emr_20160408_models.CreateParagraphResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_paragraph_with_options_async(request, runtime)

    def create_resource_pool_with_options(
        self,
        request: emr_20160408_models.CreateResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateResourcePoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateResourcePoolResponse().from_map(
            self.do_rpcrequest('CreateResourcePool', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_resource_pool_with_options_async(
        self,
        request: emr_20160408_models.CreateResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateResourcePoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateResourcePoolResponse().from_map(
            await self.do_rpcrequest_async('CreateResourcePool', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_resource_pool(
        self,
        request: emr_20160408_models.CreateResourcePoolRequest,
    ) -> emr_20160408_models.CreateResourcePoolResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_resource_pool_with_options(request, runtime)

    async def create_resource_pool_async(
        self,
        request: emr_20160408_models.CreateResourcePoolRequest,
    ) -> emr_20160408_models.CreateResourcePoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_pool_with_options_async(request, runtime)

    def create_resource_queue_with_options(
        self,
        request: emr_20160408_models.CreateResourceQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateResourceQueueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateResourceQueueResponse().from_map(
            self.do_rpcrequest('CreateResourceQueue', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_resource_queue_with_options_async(
        self,
        request: emr_20160408_models.CreateResourceQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateResourceQueueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateResourceQueueResponse().from_map(
            await self.do_rpcrequest_async('CreateResourceQueue', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_resource_queue(
        self,
        request: emr_20160408_models.CreateResourceQueueRequest,
    ) -> emr_20160408_models.CreateResourceQueueResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_resource_queue_with_options(request, runtime)

    async def create_resource_queue_async(
        self,
        request: emr_20160408_models.CreateResourceQueueRequest,
    ) -> emr_20160408_models.CreateResourceQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_queue_with_options_async(request, runtime)

    def create_scaling_group_v2with_options(
        self,
        request: emr_20160408_models.CreateScalingGroupV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateScalingGroupV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateScalingGroupV2Response().from_map(
            self.do_rpcrequest('CreateScalingGroupV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_scaling_group_v2with_options_async(
        self,
        request: emr_20160408_models.CreateScalingGroupV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateScalingGroupV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateScalingGroupV2Response().from_map(
            await self.do_rpcrequest_async('CreateScalingGroupV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scaling_group_v2(
        self,
        request: emr_20160408_models.CreateScalingGroupV2Request,
    ) -> emr_20160408_models.CreateScalingGroupV2Response:
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_group_v2with_options(request, runtime)

    async def create_scaling_group_v2_async(
        self,
        request: emr_20160408_models.CreateScalingGroupV2Request,
    ) -> emr_20160408_models.CreateScalingGroupV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.create_scaling_group_v2with_options_async(request, runtime)

    def create_scaling_rule_with_options(
        self,
        request: emr_20160408_models.CreateScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateScalingRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateScalingRuleResponse().from_map(
            self.do_rpcrequest('CreateScalingRule', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_scaling_rule_with_options_async(
        self,
        request: emr_20160408_models.CreateScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateScalingRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateScalingRuleResponse().from_map(
            await self.do_rpcrequest_async('CreateScalingRule', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_scaling_rule(
        self,
        request: emr_20160408_models.CreateScalingRuleRequest,
    ) -> emr_20160408_models.CreateScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_scaling_rule_with_options(request, runtime)

    async def create_scaling_rule_async(
        self,
        request: emr_20160408_models.CreateScalingRuleRequest,
    ) -> emr_20160408_models.CreateScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_scaling_rule_with_options_async(request, runtime)

    def create_tag_with_options(
        self,
        request: emr_20160408_models.CreateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateTagResponse().from_map(
            self.do_rpcrequest('CreateTag', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_tag_with_options_async(
        self,
        request: emr_20160408_models.CreateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateTagResponse().from_map(
            await self.do_rpcrequest_async('CreateTag', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_tag(
        self,
        request: emr_20160408_models.CreateTagRequest,
    ) -> emr_20160408_models.CreateTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_tag_with_options(request, runtime)

    async def create_tag_async(
        self,
        request: emr_20160408_models.CreateTagRequest,
    ) -> emr_20160408_models.CreateTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_tag_with_options_async(request, runtime)

    def create_user_with_options(
        self,
        request: emr_20160408_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateUserResponse().from_map(
            self.do_rpcrequest('CreateUser', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: emr_20160408_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateUserResponse().from_map(
            await self.do_rpcrequest_async('CreateUser', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_user(
        self,
        request: emr_20160408_models.CreateUserRequest,
    ) -> emr_20160408_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    async def create_user_async(
        self,
        request: emr_20160408_models.CreateUserRequest,
    ) -> emr_20160408_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_user_with_options_async(request, runtime)

    def create_users_with_options(
        self,
        request: emr_20160408_models.CreateUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateUsersResponse().from_map(
            self.do_rpcrequest('CreateUsers', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_users_with_options_async(
        self,
        request: emr_20160408_models.CreateUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.CreateUsersResponse().from_map(
            await self.do_rpcrequest_async('CreateUsers', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_users(
        self,
        request: emr_20160408_models.CreateUsersRequest,
    ) -> emr_20160408_models.CreateUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_users_with_options(request, runtime)

    async def create_users_async(
        self,
        request: emr_20160408_models.CreateUsersRequest,
    ) -> emr_20160408_models.CreateUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_users_with_options_async(request, runtime)

    def decommission_host_component_with_options(
        self,
        request: emr_20160408_models.DecommissionHostComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DecommissionHostComponentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DecommissionHostComponentResponse().from_map(
            self.do_rpcrequest('DecommissionHostComponent', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def decommission_host_component_with_options_async(
        self,
        request: emr_20160408_models.DecommissionHostComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DecommissionHostComponentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DecommissionHostComponentResponse().from_map(
            await self.do_rpcrequest_async('DecommissionHostComponent', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def decommission_host_component(
        self,
        request: emr_20160408_models.DecommissionHostComponentRequest,
    ) -> emr_20160408_models.DecommissionHostComponentResponse:
        runtime = util_models.RuntimeOptions()
        return self.decommission_host_component_with_options(request, runtime)

    async def decommission_host_component_async(
        self,
        request: emr_20160408_models.DecommissionHostComponentRequest,
    ) -> emr_20160408_models.DecommissionHostComponentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.decommission_host_component_with_options_async(request, runtime)

    def delete_cluster_template_with_options(
        self,
        request: emr_20160408_models.DeleteClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteClusterTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteClusterTemplateResponse().from_map(
            self.do_rpcrequest('DeleteClusterTemplate', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_cluster_template_with_options_async(
        self,
        request: emr_20160408_models.DeleteClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteClusterTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteClusterTemplateResponse().from_map(
            await self.do_rpcrequest_async('DeleteClusterTemplate', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cluster_template(
        self,
        request: emr_20160408_models.DeleteClusterTemplateRequest,
    ) -> emr_20160408_models.DeleteClusterTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_template_with_options(request, runtime)

    async def delete_cluster_template_async(
        self,
        request: emr_20160408_models.DeleteClusterTemplateRequest,
    ) -> emr_20160408_models.DeleteClusterTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_template_with_options_async(request, runtime)

    def delete_execution_plan_with_options(
        self,
        request: emr_20160408_models.DeleteExecutionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteExecutionPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteExecutionPlanResponse().from_map(
            self.do_rpcrequest('DeleteExecutionPlan', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_execution_plan_with_options_async(
        self,
        request: emr_20160408_models.DeleteExecutionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteExecutionPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteExecutionPlanResponse().from_map(
            await self.do_rpcrequest_async('DeleteExecutionPlan', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_execution_plan(
        self,
        request: emr_20160408_models.DeleteExecutionPlanRequest,
    ) -> emr_20160408_models.DeleteExecutionPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_execution_plan_with_options(request, runtime)

    async def delete_execution_plan_async(
        self,
        request: emr_20160408_models.DeleteExecutionPlanRequest,
    ) -> emr_20160408_models.DeleteExecutionPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_execution_plan_with_options_async(request, runtime)

    def delete_flow_with_options(
        self,
        request: emr_20160408_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteFlowResponse().from_map(
            self.do_rpcrequest('DeleteFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_with_options_async(
        self,
        request: emr_20160408_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteFlowResponse().from_map(
            await self.do_rpcrequest_async('DeleteFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow(
        self,
        request: emr_20160408_models.DeleteFlowRequest,
    ) -> emr_20160408_models.DeleteFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_with_options(request, runtime)

    async def delete_flow_async(
        self,
        request: emr_20160408_models.DeleteFlowRequest,
    ) -> emr_20160408_models.DeleteFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_with_options_async(request, runtime)

    def delete_flow_category_with_options(
        self,
        request: emr_20160408_models.DeleteFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteFlowCategoryResponse().from_map(
            self.do_rpcrequest('DeleteFlowCategory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_category_with_options_async(
        self,
        request: emr_20160408_models.DeleteFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteFlowCategoryResponse().from_map(
            await self.do_rpcrequest_async('DeleteFlowCategory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_category(
        self,
        request: emr_20160408_models.DeleteFlowCategoryRequest,
    ) -> emr_20160408_models.DeleteFlowCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_category_with_options(request, runtime)

    async def delete_flow_category_async(
        self,
        request: emr_20160408_models.DeleteFlowCategoryRequest,
    ) -> emr_20160408_models.DeleteFlowCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_category_with_options_async(request, runtime)

    def delete_flow_edit_lock_with_options(
        self,
        request: emr_20160408_models.DeleteFlowEditLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowEditLockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteFlowEditLockResponse().from_map(
            self.do_rpcrequest('DeleteFlowEditLock', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_edit_lock_with_options_async(
        self,
        request: emr_20160408_models.DeleteFlowEditLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowEditLockResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteFlowEditLockResponse().from_map(
            await self.do_rpcrequest_async('DeleteFlowEditLock', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_edit_lock(
        self,
        request: emr_20160408_models.DeleteFlowEditLockRequest,
    ) -> emr_20160408_models.DeleteFlowEditLockResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_edit_lock_with_options(request, runtime)

    async def delete_flow_edit_lock_async(
        self,
        request: emr_20160408_models.DeleteFlowEditLockRequest,
    ) -> emr_20160408_models.DeleteFlowEditLockResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_edit_lock_with_options_async(request, runtime)

    def delete_flow_job_with_options(
        self,
        request: emr_20160408_models.DeleteFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteFlowJobResponse().from_map(
            self.do_rpcrequest('DeleteFlowJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_job_with_options_async(
        self,
        request: emr_20160408_models.DeleteFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteFlowJobResponse().from_map(
            await self.do_rpcrequest_async('DeleteFlowJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_job(
        self,
        request: emr_20160408_models.DeleteFlowJobRequest,
    ) -> emr_20160408_models.DeleteFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_job_with_options(request, runtime)

    async def delete_flow_job_async(
        self,
        request: emr_20160408_models.DeleteFlowJobRequest,
    ) -> emr_20160408_models.DeleteFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_job_with_options_async(request, runtime)

    def delete_flow_project_with_options(
        self,
        request: emr_20160408_models.DeleteFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteFlowProjectResponse().from_map(
            self.do_rpcrequest('DeleteFlowProject', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_project_with_options_async(
        self,
        request: emr_20160408_models.DeleteFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteFlowProjectResponse().from_map(
            await self.do_rpcrequest_async('DeleteFlowProject', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_project(
        self,
        request: emr_20160408_models.DeleteFlowProjectRequest,
    ) -> emr_20160408_models.DeleteFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_project_with_options(request, runtime)

    async def delete_flow_project_async(
        self,
        request: emr_20160408_models.DeleteFlowProjectRequest,
    ) -> emr_20160408_models.DeleteFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_project_with_options_async(request, runtime)

    def delete_flow_project_cluster_setting_with_options(
        self,
        request: emr_20160408_models.DeleteFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteFlowProjectClusterSettingResponse().from_map(
            self.do_rpcrequest('DeleteFlowProjectClusterSetting', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_project_cluster_setting_with_options_async(
        self,
        request: emr_20160408_models.DeleteFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteFlowProjectClusterSettingResponse().from_map(
            await self.do_rpcrequest_async('DeleteFlowProjectClusterSetting', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_project_cluster_setting(
        self,
        request: emr_20160408_models.DeleteFlowProjectClusterSettingRequest,
    ) -> emr_20160408_models.DeleteFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_project_cluster_setting_with_options(request, runtime)

    async def delete_flow_project_cluster_setting_async(
        self,
        request: emr_20160408_models.DeleteFlowProjectClusterSettingRequest,
    ) -> emr_20160408_models.DeleteFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_project_cluster_setting_with_options_async(request, runtime)

    def delete_flow_project_user_with_options(
        self,
        request: emr_20160408_models.DeleteFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowProjectUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteFlowProjectUserResponse().from_map(
            self.do_rpcrequest('DeleteFlowProjectUser', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_project_user_with_options_async(
        self,
        request: emr_20160408_models.DeleteFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowProjectUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteFlowProjectUserResponse().from_map(
            await self.do_rpcrequest_async('DeleteFlowProjectUser', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow_project_user(
        self,
        request: emr_20160408_models.DeleteFlowProjectUserRequest,
    ) -> emr_20160408_models.DeleteFlowProjectUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_project_user_with_options(request, runtime)

    async def delete_flow_project_user_async(
        self,
        request: emr_20160408_models.DeleteFlowProjectUserRequest,
    ) -> emr_20160408_models.DeleteFlowProjectUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_project_user_with_options_async(request, runtime)

    def delete_job_with_options(
        self,
        request: emr_20160408_models.DeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteJobResponse().from_map(
            self.do_rpcrequest('DeleteJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        request: emr_20160408_models.DeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteJobResponse().from_map(
            await self.do_rpcrequest_async('DeleteJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_job(
        self,
        request: emr_20160408_models.DeleteJobRequest,
    ) -> emr_20160408_models.DeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_job_with_options(request, runtime)

    async def delete_job_async(
        self,
        request: emr_20160408_models.DeleteJobRequest,
    ) -> emr_20160408_models.DeleteJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_job_with_options_async(request, runtime)

    def delete_libraries_with_options(
        self,
        request: emr_20160408_models.DeleteLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteLibrariesResponse().from_map(
            self.do_rpcrequest('DeleteLibraries', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_libraries_with_options_async(
        self,
        request: emr_20160408_models.DeleteLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteLibrariesResponse().from_map(
            await self.do_rpcrequest_async('DeleteLibraries', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_libraries(
        self,
        request: emr_20160408_models.DeleteLibrariesRequest,
    ) -> emr_20160408_models.DeleteLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_libraries_with_options(request, runtime)

    async def delete_libraries_async(
        self,
        request: emr_20160408_models.DeleteLibrariesRequest,
    ) -> emr_20160408_models.DeleteLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_libraries_with_options_async(request, runtime)

    def delete_note_with_options(
        self,
        request: emr_20160408_models.DeleteNoteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteNoteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteNoteResponse().from_map(
            self.do_rpcrequest('DeleteNote', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_note_with_options_async(
        self,
        request: emr_20160408_models.DeleteNoteRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteNoteResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteNoteResponse().from_map(
            await self.do_rpcrequest_async('DeleteNote', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_note(
        self,
        request: emr_20160408_models.DeleteNoteRequest,
    ) -> emr_20160408_models.DeleteNoteResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_note_with_options(request, runtime)

    async def delete_note_async(
        self,
        request: emr_20160408_models.DeleteNoteRequest,
    ) -> emr_20160408_models.DeleteNoteResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_note_with_options_async(request, runtime)

    def delete_resource_pool_with_options(
        self,
        request: emr_20160408_models.DeleteResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteResourcePoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteResourcePoolResponse().from_map(
            self.do_rpcrequest('DeleteResourcePool', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_resource_pool_with_options_async(
        self,
        request: emr_20160408_models.DeleteResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteResourcePoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteResourcePoolResponse().from_map(
            await self.do_rpcrequest_async('DeleteResourcePool', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_resource_pool(
        self,
        request: emr_20160408_models.DeleteResourcePoolRequest,
    ) -> emr_20160408_models.DeleteResourcePoolResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_pool_with_options(request, runtime)

    async def delete_resource_pool_async(
        self,
        request: emr_20160408_models.DeleteResourcePoolRequest,
    ) -> emr_20160408_models.DeleteResourcePoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_resource_pool_with_options_async(request, runtime)

    def delete_resource_queue_with_options(
        self,
        request: emr_20160408_models.DeleteResourceQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteResourceQueueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteResourceQueueResponse().from_map(
            self.do_rpcrequest('DeleteResourceQueue', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_resource_queue_with_options_async(
        self,
        request: emr_20160408_models.DeleteResourceQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteResourceQueueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteResourceQueueResponse().from_map(
            await self.do_rpcrequest_async('DeleteResourceQueue', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_resource_queue(
        self,
        request: emr_20160408_models.DeleteResourceQueueRequest,
    ) -> emr_20160408_models.DeleteResourceQueueResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_queue_with_options(request, runtime)

    async def delete_resource_queue_async(
        self,
        request: emr_20160408_models.DeleteResourceQueueRequest,
    ) -> emr_20160408_models.DeleteResourceQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_resource_queue_with_options_async(request, runtime)

    def delete_scaling_rule_with_options(
        self,
        request: emr_20160408_models.DeleteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteScalingRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteScalingRuleResponse().from_map(
            self.do_rpcrequest('DeleteScalingRule', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_scaling_rule_with_options_async(
        self,
        request: emr_20160408_models.DeleteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteScalingRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteScalingRuleResponse().from_map(
            await self.do_rpcrequest_async('DeleteScalingRule', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_scaling_rule(
        self,
        request: emr_20160408_models.DeleteScalingRuleRequest,
    ) -> emr_20160408_models.DeleteScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_scaling_rule_with_options(request, runtime)

    async def delete_scaling_rule_async(
        self,
        request: emr_20160408_models.DeleteScalingRuleRequest,
    ) -> emr_20160408_models.DeleteScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_scaling_rule_with_options_async(request, runtime)

    def delete_tag_with_options(
        self,
        request: emr_20160408_models.DeleteTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteTagResponse().from_map(
            self.do_rpcrequest('DeleteTag', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_tag_with_options_async(
        self,
        request: emr_20160408_models.DeleteTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteTagResponse().from_map(
            await self.do_rpcrequest_async('DeleteTag', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_tag(
        self,
        request: emr_20160408_models.DeleteTagRequest,
    ) -> emr_20160408_models.DeleteTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_tag_with_options(request, runtime)

    async def delete_tag_async(
        self,
        request: emr_20160408_models.DeleteTagRequest,
    ) -> emr_20160408_models.DeleteTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_tag_with_options_async(request, runtime)

    def delete_user_with_options(
        self,
        request: emr_20160408_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteUserResponse().from_map(
            self.do_rpcrequest('DeleteUser', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: emr_20160408_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DeleteUserResponse().from_map(
            await self.do_rpcrequest_async('DeleteUser', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_user(
        self,
        request: emr_20160408_models.DeleteUserRequest,
    ) -> emr_20160408_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    async def delete_user_async(
        self,
        request: emr_20160408_models.DeleteUserRequest,
    ) -> emr_20160408_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_user_with_options_async(request, runtime)

    def describe_cluster_basic_info_with_options(
        self,
        request: emr_20160408_models.DescribeClusterBasicInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterBasicInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterBasicInfoResponse().from_map(
            self.do_rpcrequest('DescribeClusterBasicInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_basic_info_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterBasicInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterBasicInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterBasicInfoResponse().from_map(
            await self.do_rpcrequest_async('DescribeClusterBasicInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_basic_info(
        self,
        request: emr_20160408_models.DescribeClusterBasicInfoRequest,
    ) -> emr_20160408_models.DescribeClusterBasicInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_basic_info_with_options(request, runtime)

    async def describe_cluster_basic_info_async(
        self,
        request: emr_20160408_models.DescribeClusterBasicInfoRequest,
    ) -> emr_20160408_models.DescribeClusterBasicInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_basic_info_with_options_async(request, runtime)

    def describe_cluster_meta_collect_with_options(
        self,
        request: emr_20160408_models.DescribeClusterMetaCollectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterMetaCollectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterMetaCollectResponse().from_map(
            self.do_rpcrequest('DescribeClusterMetaCollect', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_meta_collect_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterMetaCollectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterMetaCollectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterMetaCollectResponse().from_map(
            await self.do_rpcrequest_async('DescribeClusterMetaCollect', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_meta_collect(
        self,
        request: emr_20160408_models.DescribeClusterMetaCollectRequest,
    ) -> emr_20160408_models.DescribeClusterMetaCollectResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_meta_collect_with_options(request, runtime)

    async def describe_cluster_meta_collect_async(
        self,
        request: emr_20160408_models.DescribeClusterMetaCollectRequest,
    ) -> emr_20160408_models.DescribeClusterMetaCollectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_meta_collect_with_options_async(request, runtime)

    def describe_cluster_operation_host_task_log_with_options(
        self,
        request: emr_20160408_models.DescribeClusterOperationHostTaskLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterOperationHostTaskLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterOperationHostTaskLogResponse().from_map(
            self.do_rpcrequest('DescribeClusterOperationHostTaskLog', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_operation_host_task_log_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterOperationHostTaskLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterOperationHostTaskLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterOperationHostTaskLogResponse().from_map(
            await self.do_rpcrequest_async('DescribeClusterOperationHostTaskLog', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_operation_host_task_log(
        self,
        request: emr_20160408_models.DescribeClusterOperationHostTaskLogRequest,
    ) -> emr_20160408_models.DescribeClusterOperationHostTaskLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_operation_host_task_log_with_options(request, runtime)

    async def describe_cluster_operation_host_task_log_async(
        self,
        request: emr_20160408_models.DescribeClusterOperationHostTaskLogRequest,
    ) -> emr_20160408_models.DescribeClusterOperationHostTaskLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_operation_host_task_log_with_options_async(request, runtime)

    def describe_cluster_resource_pool_scheduler_type_with_options(
        self,
        request: emr_20160408_models.DescribeClusterResourcePoolSchedulerTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterResourcePoolSchedulerTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterResourcePoolSchedulerTypeResponse().from_map(
            self.do_rpcrequest('DescribeClusterResourcePoolSchedulerType', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_resource_pool_scheduler_type_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterResourcePoolSchedulerTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterResourcePoolSchedulerTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterResourcePoolSchedulerTypeResponse().from_map(
            await self.do_rpcrequest_async('DescribeClusterResourcePoolSchedulerType', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_resource_pool_scheduler_type(
        self,
        request: emr_20160408_models.DescribeClusterResourcePoolSchedulerTypeRequest,
    ) -> emr_20160408_models.DescribeClusterResourcePoolSchedulerTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_resource_pool_scheduler_type_with_options(request, runtime)

    async def describe_cluster_resource_pool_scheduler_type_async(
        self,
        request: emr_20160408_models.DescribeClusterResourcePoolSchedulerTypeRequest,
    ) -> emr_20160408_models.DescribeClusterResourcePoolSchedulerTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_resource_pool_scheduler_type_with_options_async(request, runtime)

    def describe_cluster_service_with_options(
        self,
        request: emr_20160408_models.DescribeClusterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterServiceResponse().from_map(
            self.do_rpcrequest('DescribeClusterService', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_service_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterServiceResponse().from_map(
            await self.do_rpcrequest_async('DescribeClusterService', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_service(
        self,
        request: emr_20160408_models.DescribeClusterServiceRequest,
    ) -> emr_20160408_models.DescribeClusterServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_service_with_options(request, runtime)

    async def describe_cluster_service_async(
        self,
        request: emr_20160408_models.DescribeClusterServiceRequest,
    ) -> emr_20160408_models.DescribeClusterServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_service_with_options_async(request, runtime)

    def describe_cluster_service_config_with_options(
        self,
        request: emr_20160408_models.DescribeClusterServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterServiceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterServiceConfigResponse().from_map(
            self.do_rpcrequest('DescribeClusterServiceConfig', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_service_config_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterServiceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterServiceConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeClusterServiceConfig', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_service_config(
        self,
        request: emr_20160408_models.DescribeClusterServiceConfigRequest,
    ) -> emr_20160408_models.DescribeClusterServiceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_service_config_with_options(request, runtime)

    async def describe_cluster_service_config_async(
        self,
        request: emr_20160408_models.DescribeClusterServiceConfigRequest,
    ) -> emr_20160408_models.DescribeClusterServiceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_service_config_with_options_async(request, runtime)

    def describe_cluster_service_config_history_with_options(
        self,
        request: emr_20160408_models.DescribeClusterServiceConfigHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterServiceConfigHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterServiceConfigHistoryResponse().from_map(
            self.do_rpcrequest('DescribeClusterServiceConfigHistory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_service_config_history_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterServiceConfigHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterServiceConfigHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterServiceConfigHistoryResponse().from_map(
            await self.do_rpcrequest_async('DescribeClusterServiceConfigHistory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_service_config_history(
        self,
        request: emr_20160408_models.DescribeClusterServiceConfigHistoryRequest,
    ) -> emr_20160408_models.DescribeClusterServiceConfigHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_service_config_history_with_options(request, runtime)

    async def describe_cluster_service_config_history_async(
        self,
        request: emr_20160408_models.DescribeClusterServiceConfigHistoryRequest,
    ) -> emr_20160408_models.DescribeClusterServiceConfigHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_service_config_history_with_options_async(request, runtime)

    def describe_cluster_service_config_tag_with_options(
        self,
        request: emr_20160408_models.DescribeClusterServiceConfigTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterServiceConfigTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterServiceConfigTagResponse().from_map(
            self.do_rpcrequest('DescribeClusterServiceConfigTag', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_service_config_tag_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterServiceConfigTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterServiceConfigTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterServiceConfigTagResponse().from_map(
            await self.do_rpcrequest_async('DescribeClusterServiceConfigTag', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_service_config_tag(
        self,
        request: emr_20160408_models.DescribeClusterServiceConfigTagRequest,
    ) -> emr_20160408_models.DescribeClusterServiceConfigTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_service_config_tag_with_options(request, runtime)

    async def describe_cluster_service_config_tag_async(
        self,
        request: emr_20160408_models.DescribeClusterServiceConfigTagRequest,
    ) -> emr_20160408_models.DescribeClusterServiceConfigTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_service_config_tag_with_options_async(request, runtime)

    def describe_cluster_template_with_options(
        self,
        request: emr_20160408_models.DescribeClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterTemplateResponse().from_map(
            self.do_rpcrequest('DescribeClusterTemplate', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_template_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterTemplateResponse().from_map(
            await self.do_rpcrequest_async('DescribeClusterTemplate', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_template(
        self,
        request: emr_20160408_models.DescribeClusterTemplateRequest,
    ) -> emr_20160408_models.DescribeClusterTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_template_with_options(request, runtime)

    async def describe_cluster_template_async(
        self,
        request: emr_20160408_models.DescribeClusterTemplateRequest,
    ) -> emr_20160408_models.DescribeClusterTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_template_with_options_async(request, runtime)

    def describe_cluster_v2with_options(
        self,
        request: emr_20160408_models.DescribeClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterV2Response().from_map(
            self.do_rpcrequest('DescribeClusterV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_cluster_v2with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeClusterV2Response().from_map(
            await self.do_rpcrequest_async('DescribeClusterV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_v2(
        self,
        request: emr_20160408_models.DescribeClusterV2Request,
    ) -> emr_20160408_models.DescribeClusterV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_v2with_options(request, runtime)

    async def describe_cluster_v2_async(
        self,
        request: emr_20160408_models.DescribeClusterV2Request,
    ) -> emr_20160408_models.DescribeClusterV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_cluster_v2with_options_async(request, runtime)

    def describe_data_source_with_options(
        self,
        request: emr_20160408_models.DescribeDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeDataSourceResponse().from_map(
            self.do_rpcrequest('DescribeDataSource', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_data_source_with_options_async(
        self,
        request: emr_20160408_models.DescribeDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeDataSourceResponse().from_map(
            await self.do_rpcrequest_async('DescribeDataSource', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_data_source(
        self,
        request: emr_20160408_models.DescribeDataSourceRequest,
    ) -> emr_20160408_models.DescribeDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_data_source_with_options(request, runtime)

    async def describe_data_source_async(
        self,
        request: emr_20160408_models.DescribeDataSourceRequest,
    ) -> emr_20160408_models.DescribeDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_data_source_with_options_async(request, runtime)

    def describe_execution_plan_with_options(
        self,
        request: emr_20160408_models.DescribeExecutionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeExecutionPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeExecutionPlanResponse().from_map(
            self.do_rpcrequest('DescribeExecutionPlan', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_execution_plan_with_options_async(
        self,
        request: emr_20160408_models.DescribeExecutionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeExecutionPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeExecutionPlanResponse().from_map(
            await self.do_rpcrequest_async('DescribeExecutionPlan', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_execution_plan(
        self,
        request: emr_20160408_models.DescribeExecutionPlanRequest,
    ) -> emr_20160408_models.DescribeExecutionPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_execution_plan_with_options(request, runtime)

    async def describe_execution_plan_async(
        self,
        request: emr_20160408_models.DescribeExecutionPlanRequest,
    ) -> emr_20160408_models.DescribeExecutionPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_execution_plan_with_options_async(request, runtime)

    def describe_flow_with_options(
        self,
        request: emr_20160408_models.DescribeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowResponse().from_map(
            self.do_rpcrequest('DescribeFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow(
        self,
        request: emr_20160408_models.DescribeFlowRequest,
    ) -> emr_20160408_models.DescribeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_with_options(request, runtime)

    async def describe_flow_async(
        self,
        request: emr_20160408_models.DescribeFlowRequest,
    ) -> emr_20160408_models.DescribeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_with_options_async(request, runtime)

    def describe_flow_agent_token_with_options(
        self,
        request: emr_20160408_models.DescribeFlowAgentTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowAgentTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowAgentTokenResponse().from_map(
            self.do_rpcrequest('DescribeFlowAgentToken', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_agent_token_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowAgentTokenRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowAgentTokenResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowAgentTokenResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowAgentToken', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_agent_token(
        self,
        request: emr_20160408_models.DescribeFlowAgentTokenRequest,
    ) -> emr_20160408_models.DescribeFlowAgentTokenResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_agent_token_with_options(request, runtime)

    async def describe_flow_agent_token_async(
        self,
        request: emr_20160408_models.DescribeFlowAgentTokenRequest,
    ) -> emr_20160408_models.DescribeFlowAgentTokenResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_agent_token_with_options_async(request, runtime)

    def describe_flow_agent_user_with_options(
        self,
        request: emr_20160408_models.DescribeFlowAgentUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowAgentUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowAgentUserResponse().from_map(
            self.do_rpcrequest('DescribeFlowAgentUser', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_agent_user_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowAgentUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowAgentUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowAgentUserResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowAgentUser', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_agent_user(
        self,
        request: emr_20160408_models.DescribeFlowAgentUserRequest,
    ) -> emr_20160408_models.DescribeFlowAgentUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_agent_user_with_options(request, runtime)

    async def describe_flow_agent_user_async(
        self,
        request: emr_20160408_models.DescribeFlowAgentUserRequest,
    ) -> emr_20160408_models.DescribeFlowAgentUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_agent_user_with_options_async(request, runtime)

    def describe_flow_category_with_options(
        self,
        request: emr_20160408_models.DescribeFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowCategoryResponse().from_map(
            self.do_rpcrequest('DescribeFlowCategory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_category_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowCategoryResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowCategory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_category(
        self,
        request: emr_20160408_models.DescribeFlowCategoryRequest,
    ) -> emr_20160408_models.DescribeFlowCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_category_with_options(request, runtime)

    async def describe_flow_category_async(
        self,
        request: emr_20160408_models.DescribeFlowCategoryRequest,
    ) -> emr_20160408_models.DescribeFlowCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_category_with_options_async(request, runtime)

    def describe_flow_category_tree_with_options(
        self,
        request: emr_20160408_models.DescribeFlowCategoryTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowCategoryTreeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowCategoryTreeResponse().from_map(
            self.do_rpcrequest('DescribeFlowCategoryTree', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_category_tree_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowCategoryTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowCategoryTreeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowCategoryTreeResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowCategoryTree', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_category_tree(
        self,
        request: emr_20160408_models.DescribeFlowCategoryTreeRequest,
    ) -> emr_20160408_models.DescribeFlowCategoryTreeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_category_tree_with_options(request, runtime)

    async def describe_flow_category_tree_async(
        self,
        request: emr_20160408_models.DescribeFlowCategoryTreeRequest,
    ) -> emr_20160408_models.DescribeFlowCategoryTreeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_category_tree_with_options_async(request, runtime)

    def describe_flow_entity_snapshot_with_options(
        self,
        request: emr_20160408_models.DescribeFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowEntitySnapshotResponse().from_map(
            self.do_rpcrequest('DescribeFlowEntitySnapshot', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_entity_snapshot_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowEntitySnapshotResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowEntitySnapshot', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_entity_snapshot(
        self,
        request: emr_20160408_models.DescribeFlowEntitySnapshotRequest,
    ) -> emr_20160408_models.DescribeFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_entity_snapshot_with_options(request, runtime)

    async def describe_flow_entity_snapshot_async(
        self,
        request: emr_20160408_models.DescribeFlowEntitySnapshotRequest,
    ) -> emr_20160408_models.DescribeFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_entity_snapshot_with_options_async(request, runtime)

    def describe_flow_instance_with_options(
        self,
        request: emr_20160408_models.DescribeFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowInstanceResponse().from_map(
            self.do_rpcrequest('DescribeFlowInstance', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_instance_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowInstanceResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowInstance', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_instance(
        self,
        request: emr_20160408_models.DescribeFlowInstanceRequest,
    ) -> emr_20160408_models.DescribeFlowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_instance_with_options(request, runtime)

    async def describe_flow_instance_async(
        self,
        request: emr_20160408_models.DescribeFlowInstanceRequest,
    ) -> emr_20160408_models.DescribeFlowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_instance_with_options_async(request, runtime)

    def describe_flow_job_with_options(
        self,
        request: emr_20160408_models.DescribeFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowJobResponse().from_map(
            self.do_rpcrequest('DescribeFlowJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_job_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowJobResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_job(
        self,
        request: emr_20160408_models.DescribeFlowJobRequest,
    ) -> emr_20160408_models.DescribeFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_job_with_options(request, runtime)

    async def describe_flow_job_async(
        self,
        request: emr_20160408_models.DescribeFlowJobRequest,
    ) -> emr_20160408_models.DescribeFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_job_with_options_async(request, runtime)

    def describe_flow_node_instance_with_options(
        self,
        request: emr_20160408_models.DescribeFlowNodeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowNodeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowNodeInstanceResponse().from_map(
            self.do_rpcrequest('DescribeFlowNodeInstance', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_node_instance_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowNodeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowNodeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowNodeInstanceResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowNodeInstance', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_node_instance(
        self,
        request: emr_20160408_models.DescribeFlowNodeInstanceRequest,
    ) -> emr_20160408_models.DescribeFlowNodeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_node_instance_with_options(request, runtime)

    async def describe_flow_node_instance_async(
        self,
        request: emr_20160408_models.DescribeFlowNodeInstanceRequest,
    ) -> emr_20160408_models.DescribeFlowNodeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_node_instance_with_options_async(request, runtime)

    def describe_flow_node_instance_container_log_with_options(
        self,
        request: emr_20160408_models.DescribeFlowNodeInstanceContainerLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowNodeInstanceContainerLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowNodeInstanceContainerLogResponse().from_map(
            self.do_rpcrequest('DescribeFlowNodeInstanceContainerLog', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_node_instance_container_log_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowNodeInstanceContainerLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowNodeInstanceContainerLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowNodeInstanceContainerLogResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowNodeInstanceContainerLog', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_node_instance_container_log(
        self,
        request: emr_20160408_models.DescribeFlowNodeInstanceContainerLogRequest,
    ) -> emr_20160408_models.DescribeFlowNodeInstanceContainerLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_node_instance_container_log_with_options(request, runtime)

    async def describe_flow_node_instance_container_log_async(
        self,
        request: emr_20160408_models.DescribeFlowNodeInstanceContainerLogRequest,
    ) -> emr_20160408_models.DescribeFlowNodeInstanceContainerLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_node_instance_container_log_with_options_async(request, runtime)

    def describe_flow_node_instance_launcher_log_with_options(
        self,
        request: emr_20160408_models.DescribeFlowNodeInstanceLauncherLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowNodeInstanceLauncherLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowNodeInstanceLauncherLogResponse().from_map(
            self.do_rpcrequest('DescribeFlowNodeInstanceLauncherLog', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_node_instance_launcher_log_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowNodeInstanceLauncherLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowNodeInstanceLauncherLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowNodeInstanceLauncherLogResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowNodeInstanceLauncherLog', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_node_instance_launcher_log(
        self,
        request: emr_20160408_models.DescribeFlowNodeInstanceLauncherLogRequest,
    ) -> emr_20160408_models.DescribeFlowNodeInstanceLauncherLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_node_instance_launcher_log_with_options(request, runtime)

    async def describe_flow_node_instance_launcher_log_async(
        self,
        request: emr_20160408_models.DescribeFlowNodeInstanceLauncherLogRequest,
    ) -> emr_20160408_models.DescribeFlowNodeInstanceLauncherLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_node_instance_launcher_log_with_options_async(request, runtime)

    def describe_flow_project_with_options(
        self,
        request: emr_20160408_models.DescribeFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowProjectResponse().from_map(
            self.do_rpcrequest('DescribeFlowProject', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_project_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowProjectResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowProject', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_project(
        self,
        request: emr_20160408_models.DescribeFlowProjectRequest,
    ) -> emr_20160408_models.DescribeFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_project_with_options(request, runtime)

    async def describe_flow_project_async(
        self,
        request: emr_20160408_models.DescribeFlowProjectRequest,
    ) -> emr_20160408_models.DescribeFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_project_with_options_async(request, runtime)

    def describe_flow_project_cluster_setting_with_options(
        self,
        request: emr_20160408_models.DescribeFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowProjectClusterSettingResponse().from_map(
            self.do_rpcrequest('DescribeFlowProjectClusterSetting', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_project_cluster_setting_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeFlowProjectClusterSettingResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowProjectClusterSetting', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_project_cluster_setting(
        self,
        request: emr_20160408_models.DescribeFlowProjectClusterSettingRequest,
    ) -> emr_20160408_models.DescribeFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_project_cluster_setting_with_options(request, runtime)

    async def describe_flow_project_cluster_setting_async(
        self,
        request: emr_20160408_models.DescribeFlowProjectClusterSettingRequest,
    ) -> emr_20160408_models.DescribeFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_project_cluster_setting_with_options_async(request, runtime)

    def describe_job_with_options(
        self,
        request: emr_20160408_models.DescribeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeJobResponse().from_map(
            self.do_rpcrequest('DescribeJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_job_with_options_async(
        self,
        request: emr_20160408_models.DescribeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeJobResponse().from_map(
            await self.do_rpcrequest_async('DescribeJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_job(
        self,
        request: emr_20160408_models.DescribeJobRequest,
    ) -> emr_20160408_models.DescribeJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_job_with_options(request, runtime)

    async def describe_job_async(
        self,
        request: emr_20160408_models.DescribeJobRequest,
    ) -> emr_20160408_models.DescribeJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_with_options_async(request, runtime)

    def describe_library_detail_with_options(
        self,
        request: emr_20160408_models.DescribeLibraryDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeLibraryDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeLibraryDetailResponse().from_map(
            self.do_rpcrequest('DescribeLibraryDetail', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_library_detail_with_options_async(
        self,
        request: emr_20160408_models.DescribeLibraryDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeLibraryDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeLibraryDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeLibraryDetail', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_library_detail(
        self,
        request: emr_20160408_models.DescribeLibraryDetailRequest,
    ) -> emr_20160408_models.DescribeLibraryDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_library_detail_with_options(request, runtime)

    async def describe_library_detail_async(
        self,
        request: emr_20160408_models.DescribeLibraryDetailRequest,
    ) -> emr_20160408_models.DescribeLibraryDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_library_detail_with_options_async(request, runtime)

    def describe_library_install_task_detail_with_options(
        self,
        request: emr_20160408_models.DescribeLibraryInstallTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeLibraryInstallTaskDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeLibraryInstallTaskDetailResponse().from_map(
            self.do_rpcrequest('DescribeLibraryInstallTaskDetail', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_library_install_task_detail_with_options_async(
        self,
        request: emr_20160408_models.DescribeLibraryInstallTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeLibraryInstallTaskDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeLibraryInstallTaskDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeLibraryInstallTaskDetail', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_library_install_task_detail(
        self,
        request: emr_20160408_models.DescribeLibraryInstallTaskDetailRequest,
    ) -> emr_20160408_models.DescribeLibraryInstallTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_library_install_task_detail_with_options(request, runtime)

    async def describe_library_install_task_detail_async(
        self,
        request: emr_20160408_models.DescribeLibraryInstallTaskDetailRequest,
    ) -> emr_20160408_models.DescribeLibraryInstallTaskDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_library_install_task_detail_with_options_async(request, runtime)

    def describe_meta_table_preview_task_with_options(
        self,
        request: emr_20160408_models.DescribeMetaTablePreviewTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeMetaTablePreviewTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeMetaTablePreviewTaskResponse().from_map(
            self.do_rpcrequest('DescribeMetaTablePreviewTask', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_meta_table_preview_task_with_options_async(
        self,
        request: emr_20160408_models.DescribeMetaTablePreviewTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeMetaTablePreviewTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeMetaTablePreviewTaskResponse().from_map(
            await self.do_rpcrequest_async('DescribeMetaTablePreviewTask', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_meta_table_preview_task(
        self,
        request: emr_20160408_models.DescribeMetaTablePreviewTaskRequest,
    ) -> emr_20160408_models.DescribeMetaTablePreviewTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_meta_table_preview_task_with_options(request, runtime)

    async def describe_meta_table_preview_task_async(
        self,
        request: emr_20160408_models.DescribeMetaTablePreviewTaskRequest,
    ) -> emr_20160408_models.DescribeMetaTablePreviewTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_meta_table_preview_task_with_options_async(request, runtime)

    def describe_scaling_activity_with_options(
        self,
        request: emr_20160408_models.DescribeScalingActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingActivityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeScalingActivityResponse().from_map(
            self.do_rpcrequest('DescribeScalingActivity', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scaling_activity_with_options_async(
        self,
        request: emr_20160408_models.DescribeScalingActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingActivityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeScalingActivityResponse().from_map(
            await self.do_rpcrequest_async('DescribeScalingActivity', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_activity(
        self,
        request: emr_20160408_models.DescribeScalingActivityRequest,
    ) -> emr_20160408_models.DescribeScalingActivityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_activity_with_options(request, runtime)

    async def describe_scaling_activity_async(
        self,
        request: emr_20160408_models.DescribeScalingActivityRequest,
    ) -> emr_20160408_models.DescribeScalingActivityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_activity_with_options_async(request, runtime)

    def describe_scaling_common_config_with_options(
        self,
        request: emr_20160408_models.DescribeScalingCommonConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingCommonConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeScalingCommonConfigResponse().from_map(
            self.do_rpcrequest('DescribeScalingCommonConfig', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scaling_common_config_with_options_async(
        self,
        request: emr_20160408_models.DescribeScalingCommonConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingCommonConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeScalingCommonConfigResponse().from_map(
            await self.do_rpcrequest_async('DescribeScalingCommonConfig', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_common_config(
        self,
        request: emr_20160408_models.DescribeScalingCommonConfigRequest,
    ) -> emr_20160408_models.DescribeScalingCommonConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_common_config_with_options(request, runtime)

    async def describe_scaling_common_config_async(
        self,
        request: emr_20160408_models.DescribeScalingCommonConfigRequest,
    ) -> emr_20160408_models.DescribeScalingCommonConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_common_config_with_options_async(request, runtime)

    def describe_scaling_config_item_v2with_options(
        self,
        request: emr_20160408_models.DescribeScalingConfigItemV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingConfigItemV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeScalingConfigItemV2Response().from_map(
            self.do_rpcrequest('DescribeScalingConfigItemV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scaling_config_item_v2with_options_async(
        self,
        request: emr_20160408_models.DescribeScalingConfigItemV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingConfigItemV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeScalingConfigItemV2Response().from_map(
            await self.do_rpcrequest_async('DescribeScalingConfigItemV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_config_item_v2(
        self,
        request: emr_20160408_models.DescribeScalingConfigItemV2Request,
    ) -> emr_20160408_models.DescribeScalingConfigItemV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_config_item_v2with_options(request, runtime)

    async def describe_scaling_config_item_v2_async(
        self,
        request: emr_20160408_models.DescribeScalingConfigItemV2Request,
    ) -> emr_20160408_models.DescribeScalingConfigItemV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_config_item_v2with_options_async(request, runtime)

    def describe_scaling_group_instance_v2with_options(
        self,
        request: emr_20160408_models.DescribeScalingGroupInstanceV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingGroupInstanceV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeScalingGroupInstanceV2Response().from_map(
            self.do_rpcrequest('DescribeScalingGroupInstanceV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scaling_group_instance_v2with_options_async(
        self,
        request: emr_20160408_models.DescribeScalingGroupInstanceV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingGroupInstanceV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeScalingGroupInstanceV2Response().from_map(
            await self.do_rpcrequest_async('DescribeScalingGroupInstanceV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_group_instance_v2(
        self,
        request: emr_20160408_models.DescribeScalingGroupInstanceV2Request,
    ) -> emr_20160408_models.DescribeScalingGroupInstanceV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_group_instance_v2with_options(request, runtime)

    async def describe_scaling_group_instance_v2_async(
        self,
        request: emr_20160408_models.DescribeScalingGroupInstanceV2Request,
    ) -> emr_20160408_models.DescribeScalingGroupInstanceV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_group_instance_v2with_options_async(request, runtime)

    def describe_scaling_group_v2with_options(
        self,
        request: emr_20160408_models.DescribeScalingGroupV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingGroupV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeScalingGroupV2Response().from_map(
            self.do_rpcrequest('DescribeScalingGroupV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scaling_group_v2with_options_async(
        self,
        request: emr_20160408_models.DescribeScalingGroupV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingGroupV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeScalingGroupV2Response().from_map(
            await self.do_rpcrequest_async('DescribeScalingGroupV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_group_v2(
        self,
        request: emr_20160408_models.DescribeScalingGroupV2Request,
    ) -> emr_20160408_models.DescribeScalingGroupV2Response:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_group_v2with_options(request, runtime)

    async def describe_scaling_group_v2_async(
        self,
        request: emr_20160408_models.DescribeScalingGroupV2Request,
    ) -> emr_20160408_models.DescribeScalingGroupV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_group_v2with_options_async(request, runtime)

    def describe_scaling_rule_with_options(
        self,
        request: emr_20160408_models.DescribeScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeScalingRuleResponse().from_map(
            self.do_rpcrequest('DescribeScalingRule', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_scaling_rule_with_options_async(
        self,
        request: emr_20160408_models.DescribeScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeScalingRuleResponse().from_map(
            await self.do_rpcrequest_async('DescribeScalingRule', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_scaling_rule(
        self,
        request: emr_20160408_models.DescribeScalingRuleRequest,
    ) -> emr_20160408_models.DescribeScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_scaling_rule_with_options(request, runtime)

    async def describe_scaling_rule_async(
        self,
        request: emr_20160408_models.DescribeScalingRuleRequest,
    ) -> emr_20160408_models.DescribeScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_scaling_rule_with_options_async(request, runtime)

    def describe_security_group_attribute_with_options(
        self,
        request: emr_20160408_models.DescribeSecurityGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeSecurityGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeSecurityGroupAttributeResponse().from_map(
            self.do_rpcrequest('DescribeSecurityGroupAttribute', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_security_group_attribute_with_options_async(
        self,
        request: emr_20160408_models.DescribeSecurityGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeSecurityGroupAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DescribeSecurityGroupAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeSecurityGroupAttribute', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_security_group_attribute(
        self,
        request: emr_20160408_models.DescribeSecurityGroupAttributeRequest,
    ) -> emr_20160408_models.DescribeSecurityGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_security_group_attribute_with_options(request, runtime)

    async def describe_security_group_attribute_async(
        self,
        request: emr_20160408_models.DescribeSecurityGroupAttributeRequest,
    ) -> emr_20160408_models.DescribeSecurityGroupAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_group_attribute_with_options_async(request, runtime)

    def detach_and_release_cluster_eni_with_options(
        self,
        request: emr_20160408_models.DetachAndReleaseClusterEniRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DetachAndReleaseClusterEniResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DetachAndReleaseClusterEniResponse().from_map(
            self.do_rpcrequest('DetachAndReleaseClusterEni', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def detach_and_release_cluster_eni_with_options_async(
        self,
        request: emr_20160408_models.DetachAndReleaseClusterEniRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DetachAndReleaseClusterEniResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DetachAndReleaseClusterEniResponse().from_map(
            await self.do_rpcrequest_async('DetachAndReleaseClusterEni', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_and_release_cluster_eni(
        self,
        request: emr_20160408_models.DetachAndReleaseClusterEniRequest,
    ) -> emr_20160408_models.DetachAndReleaseClusterEniResponse:
        runtime = util_models.RuntimeOptions()
        return self.detach_and_release_cluster_eni_with_options(request, runtime)

    async def detach_and_release_cluster_eni_async(
        self,
        request: emr_20160408_models.DetachAndReleaseClusterEniRequest,
    ) -> emr_20160408_models.DetachAndReleaseClusterEniResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detach_and_release_cluster_eni_with_options_async(request, runtime)

    def diff_flow_entity_snapshot_with_options(
        self,
        request: emr_20160408_models.DiffFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DiffFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DiffFlowEntitySnapshotResponse().from_map(
            self.do_rpcrequest('DiffFlowEntitySnapshot', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def diff_flow_entity_snapshot_with_options_async(
        self,
        request: emr_20160408_models.DiffFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DiffFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DiffFlowEntitySnapshotResponse().from_map(
            await self.do_rpcrequest_async('DiffFlowEntitySnapshot', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def diff_flow_entity_snapshot(
        self,
        request: emr_20160408_models.DiffFlowEntitySnapshotRequest,
    ) -> emr_20160408_models.DiffFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.diff_flow_entity_snapshot_with_options(request, runtime)

    async def diff_flow_entity_snapshot_async(
        self,
        request: emr_20160408_models.DiffFlowEntitySnapshotRequest,
    ) -> emr_20160408_models.DiffFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.diff_flow_entity_snapshot_with_options_async(request, runtime)

    def dump_meta_data_source_for_outer_with_options(
        self,
        request: emr_20160408_models.DumpMetaDataSourceForOuterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DumpMetaDataSourceForOuterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DumpMetaDataSourceForOuterResponse().from_map(
            self.do_rpcrequest('DumpMetaDataSourceForOuter', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def dump_meta_data_source_for_outer_with_options_async(
        self,
        request: emr_20160408_models.DumpMetaDataSourceForOuterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DumpMetaDataSourceForOuterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.DumpMetaDataSourceForOuterResponse().from_map(
            await self.do_rpcrequest_async('DumpMetaDataSourceForOuter', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def dump_meta_data_source_for_outer(
        self,
        request: emr_20160408_models.DumpMetaDataSourceForOuterRequest,
    ) -> emr_20160408_models.DumpMetaDataSourceForOuterResponse:
        runtime = util_models.RuntimeOptions()
        return self.dump_meta_data_source_for_outer_with_options(request, runtime)

    async def dump_meta_data_source_for_outer_async(
        self,
        request: emr_20160408_models.DumpMetaDataSourceForOuterRequest,
    ) -> emr_20160408_models.DumpMetaDataSourceForOuterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.dump_meta_data_source_for_outer_with_options_async(request, runtime)

    def get_flow_entity_relation_graph_with_options(
        self,
        request: emr_20160408_models.GetFlowEntityRelationGraphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetFlowEntityRelationGraphResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetFlowEntityRelationGraphResponse().from_map(
            self.do_rpcrequest('GetFlowEntityRelationGraph', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_flow_entity_relation_graph_with_options_async(
        self,
        request: emr_20160408_models.GetFlowEntityRelationGraphRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetFlowEntityRelationGraphResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetFlowEntityRelationGraphResponse().from_map(
            await self.do_rpcrequest_async('GetFlowEntityRelationGraph', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_flow_entity_relation_graph(
        self,
        request: emr_20160408_models.GetFlowEntityRelationGraphRequest,
    ) -> emr_20160408_models.GetFlowEntityRelationGraphResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_flow_entity_relation_graph_with_options(request, runtime)

    async def get_flow_entity_relation_graph_async(
        self,
        request: emr_20160408_models.GetFlowEntityRelationGraphRequest,
    ) -> emr_20160408_models.GetFlowEntityRelationGraphResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_flow_entity_relation_graph_with_options_async(request, runtime)

    def get_hdfs_capacity_statistic_info_with_options(
        self,
        request: emr_20160408_models.GetHdfsCapacityStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetHdfsCapacityStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetHdfsCapacityStatisticInfoResponse().from_map(
            self.do_rpcrequest('GetHdfsCapacityStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_hdfs_capacity_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetHdfsCapacityStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetHdfsCapacityStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetHdfsCapacityStatisticInfoResponse().from_map(
            await self.do_rpcrequest_async('GetHdfsCapacityStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_hdfs_capacity_statistic_info(
        self,
        request: emr_20160408_models.GetHdfsCapacityStatisticInfoRequest,
    ) -> emr_20160408_models.GetHdfsCapacityStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_hdfs_capacity_statistic_info_with_options(request, runtime)

    async def get_hdfs_capacity_statistic_info_async(
        self,
        request: emr_20160408_models.GetHdfsCapacityStatisticInfoRequest,
    ) -> emr_20160408_models.GetHdfsCapacityStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_hdfs_capacity_statistic_info_with_options_async(request, runtime)

    def get_job_input_statistic_info_with_options(
        self,
        request: emr_20160408_models.GetJobInputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetJobInputStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetJobInputStatisticInfoResponse().from_map(
            self.do_rpcrequest('GetJobInputStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_job_input_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetJobInputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetJobInputStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetJobInputStatisticInfoResponse().from_map(
            await self.do_rpcrequest_async('GetJobInputStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_input_statistic_info(
        self,
        request: emr_20160408_models.GetJobInputStatisticInfoRequest,
    ) -> emr_20160408_models.GetJobInputStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_input_statistic_info_with_options(request, runtime)

    async def get_job_input_statistic_info_async(
        self,
        request: emr_20160408_models.GetJobInputStatisticInfoRequest,
    ) -> emr_20160408_models.GetJobInputStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_input_statistic_info_with_options_async(request, runtime)

    def get_job_output_statistic_info_with_options(
        self,
        request: emr_20160408_models.GetJobOutputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetJobOutputStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetJobOutputStatisticInfoResponse().from_map(
            self.do_rpcrequest('GetJobOutputStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_job_output_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetJobOutputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetJobOutputStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetJobOutputStatisticInfoResponse().from_map(
            await self.do_rpcrequest_async('GetJobOutputStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_output_statistic_info(
        self,
        request: emr_20160408_models.GetJobOutputStatisticInfoRequest,
    ) -> emr_20160408_models.GetJobOutputStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_output_statistic_info_with_options(request, runtime)

    async def get_job_output_statistic_info_async(
        self,
        request: emr_20160408_models.GetJobOutputStatisticInfoRequest,
    ) -> emr_20160408_models.GetJobOutputStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_output_statistic_info_with_options_async(request, runtime)

    def get_job_running_time_statistic_info_with_options(
        self,
        request: emr_20160408_models.GetJobRunningTimeStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetJobRunningTimeStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetJobRunningTimeStatisticInfoResponse().from_map(
            self.do_rpcrequest('GetJobRunningTimeStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_job_running_time_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetJobRunningTimeStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetJobRunningTimeStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetJobRunningTimeStatisticInfoResponse().from_map(
            await self.do_rpcrequest_async('GetJobRunningTimeStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_job_running_time_statistic_info(
        self,
        request: emr_20160408_models.GetJobRunningTimeStatisticInfoRequest,
    ) -> emr_20160408_models.GetJobRunningTimeStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_job_running_time_statistic_info_with_options(request, runtime)

    async def get_job_running_time_statistic_info_async(
        self,
        request: emr_20160408_models.GetJobRunningTimeStatisticInfoRequest,
    ) -> emr_20160408_models.GetJobRunningTimeStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_job_running_time_statistic_info_with_options_async(request, runtime)

    def get_queue_input_statistic_info_with_options(
        self,
        request: emr_20160408_models.GetQueueInputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetQueueInputStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetQueueInputStatisticInfoResponse().from_map(
            self.do_rpcrequest('GetQueueInputStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_queue_input_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetQueueInputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetQueueInputStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetQueueInputStatisticInfoResponse().from_map(
            await self.do_rpcrequest_async('GetQueueInputStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_queue_input_statistic_info(
        self,
        request: emr_20160408_models.GetQueueInputStatisticInfoRequest,
    ) -> emr_20160408_models.GetQueueInputStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_queue_input_statistic_info_with_options(request, runtime)

    async def get_queue_input_statistic_info_async(
        self,
        request: emr_20160408_models.GetQueueInputStatisticInfoRequest,
    ) -> emr_20160408_models.GetQueueInputStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_queue_input_statistic_info_with_options_async(request, runtime)

    def get_queue_output_statistic_info_with_options(
        self,
        request: emr_20160408_models.GetQueueOutputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetQueueOutputStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetQueueOutputStatisticInfoResponse().from_map(
            self.do_rpcrequest('GetQueueOutputStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_queue_output_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetQueueOutputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetQueueOutputStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetQueueOutputStatisticInfoResponse().from_map(
            await self.do_rpcrequest_async('GetQueueOutputStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_queue_output_statistic_info(
        self,
        request: emr_20160408_models.GetQueueOutputStatisticInfoRequest,
    ) -> emr_20160408_models.GetQueueOutputStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_queue_output_statistic_info_with_options(request, runtime)

    async def get_queue_output_statistic_info_async(
        self,
        request: emr_20160408_models.GetQueueOutputStatisticInfoRequest,
    ) -> emr_20160408_models.GetQueueOutputStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_queue_output_statistic_info_with_options_async(request, runtime)

    def get_queue_submission_statistic_info_with_options(
        self,
        request: emr_20160408_models.GetQueueSubmissionStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetQueueSubmissionStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetQueueSubmissionStatisticInfoResponse().from_map(
            self.do_rpcrequest('GetQueueSubmissionStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_queue_submission_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetQueueSubmissionStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetQueueSubmissionStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetQueueSubmissionStatisticInfoResponse().from_map(
            await self.do_rpcrequest_async('GetQueueSubmissionStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_queue_submission_statistic_info(
        self,
        request: emr_20160408_models.GetQueueSubmissionStatisticInfoRequest,
    ) -> emr_20160408_models.GetQueueSubmissionStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_queue_submission_statistic_info_with_options(request, runtime)

    async def get_queue_submission_statistic_info_async(
        self,
        request: emr_20160408_models.GetQueueSubmissionStatisticInfoRequest,
    ) -> emr_20160408_models.GetQueueSubmissionStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_queue_submission_statistic_info_with_options_async(request, runtime)

    def get_user_input_statistic_info_with_options(
        self,
        request: emr_20160408_models.GetUserInputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetUserInputStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetUserInputStatisticInfoResponse().from_map(
            self.do_rpcrequest('GetUserInputStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_input_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetUserInputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetUserInputStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetUserInputStatisticInfoResponse().from_map(
            await self.do_rpcrequest_async('GetUserInputStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_input_statistic_info(
        self,
        request: emr_20160408_models.GetUserInputStatisticInfoRequest,
    ) -> emr_20160408_models.GetUserInputStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_input_statistic_info_with_options(request, runtime)

    async def get_user_input_statistic_info_async(
        self,
        request: emr_20160408_models.GetUserInputStatisticInfoRequest,
    ) -> emr_20160408_models.GetUserInputStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_input_statistic_info_with_options_async(request, runtime)

    def get_user_output_statistic_info_with_options(
        self,
        request: emr_20160408_models.GetUserOutputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetUserOutputStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetUserOutputStatisticInfoResponse().from_map(
            self.do_rpcrequest('GetUserOutputStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_output_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetUserOutputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetUserOutputStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetUserOutputStatisticInfoResponse().from_map(
            await self.do_rpcrequest_async('GetUserOutputStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_output_statistic_info(
        self,
        request: emr_20160408_models.GetUserOutputStatisticInfoRequest,
    ) -> emr_20160408_models.GetUserOutputStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_output_statistic_info_with_options(request, runtime)

    async def get_user_output_statistic_info_async(
        self,
        request: emr_20160408_models.GetUserOutputStatisticInfoRequest,
    ) -> emr_20160408_models.GetUserOutputStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_output_statistic_info_with_options_async(request, runtime)

    def get_user_submission_statistic_info_with_options(
        self,
        request: emr_20160408_models.GetUserSubmissionStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetUserSubmissionStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetUserSubmissionStatisticInfoResponse().from_map(
            self.do_rpcrequest('GetUserSubmissionStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def get_user_submission_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetUserSubmissionStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetUserSubmissionStatisticInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.GetUserSubmissionStatisticInfoResponse().from_map(
            await self.do_rpcrequest_async('GetUserSubmissionStatisticInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_user_submission_statistic_info(
        self,
        request: emr_20160408_models.GetUserSubmissionStatisticInfoRequest,
    ) -> emr_20160408_models.GetUserSubmissionStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_user_submission_statistic_info_with_options(request, runtime)

    async def get_user_submission_statistic_info_async(
        self,
        request: emr_20160408_models.GetUserSubmissionStatisticInfoRequest,
    ) -> emr_20160408_models.GetUserSubmissionStatisticInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_user_submission_statistic_info_with_options_async(request, runtime)

    def install_libraries_with_options(
        self,
        request: emr_20160408_models.InstallLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.InstallLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.InstallLibrariesResponse().from_map(
            self.do_rpcrequest('InstallLibraries', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def install_libraries_with_options_async(
        self,
        request: emr_20160408_models.InstallLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.InstallLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.InstallLibrariesResponse().from_map(
            await self.do_rpcrequest_async('InstallLibraries', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def install_libraries(
        self,
        request: emr_20160408_models.InstallLibrariesRequest,
    ) -> emr_20160408_models.InstallLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_libraries_with_options(request, runtime)

    async def install_libraries_async(
        self,
        request: emr_20160408_models.InstallLibrariesRequest,
    ) -> emr_20160408_models.InstallLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_libraries_with_options_async(request, runtime)

    def join_resource_group_with_options(
        self,
        request: emr_20160408_models.JoinResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.JoinResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.JoinResourceGroupResponse().from_map(
            self.do_rpcrequest('JoinResourceGroup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def join_resource_group_with_options_async(
        self,
        request: emr_20160408_models.JoinResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.JoinResourceGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.JoinResourceGroupResponse().from_map(
            await self.do_rpcrequest_async('JoinResourceGroup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def join_resource_group(
        self,
        request: emr_20160408_models.JoinResourceGroupRequest,
    ) -> emr_20160408_models.JoinResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_resource_group_with_options(request, runtime)

    async def join_resource_group_async(
        self,
        request: emr_20160408_models.JoinResourceGroupRequest,
    ) -> emr_20160408_models.JoinResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_resource_group_with_options_async(request, runtime)

    def kill_execution_job_instance_with_options(
        self,
        request: emr_20160408_models.KillExecutionJobInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.KillExecutionJobInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.KillExecutionJobInstanceResponse().from_map(
            self.do_rpcrequest('KillExecutionJobInstance', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def kill_execution_job_instance_with_options_async(
        self,
        request: emr_20160408_models.KillExecutionJobInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.KillExecutionJobInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.KillExecutionJobInstanceResponse().from_map(
            await self.do_rpcrequest_async('KillExecutionJobInstance', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def kill_execution_job_instance(
        self,
        request: emr_20160408_models.KillExecutionJobInstanceRequest,
    ) -> emr_20160408_models.KillExecutionJobInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.kill_execution_job_instance_with_options(request, runtime)

    async def kill_execution_job_instance_async(
        self,
        request: emr_20160408_models.KillExecutionJobInstanceRequest,
    ) -> emr_20160408_models.KillExecutionJobInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.kill_execution_job_instance_with_options_async(request, runtime)

    def kill_flow_job_with_options(
        self,
        request: emr_20160408_models.KillFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.KillFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.KillFlowJobResponse().from_map(
            self.do_rpcrequest('KillFlowJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def kill_flow_job_with_options_async(
        self,
        request: emr_20160408_models.KillFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.KillFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.KillFlowJobResponse().from_map(
            await self.do_rpcrequest_async('KillFlowJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def kill_flow_job(
        self,
        request: emr_20160408_models.KillFlowJobRequest,
    ) -> emr_20160408_models.KillFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.kill_flow_job_with_options(request, runtime)

    async def kill_flow_job_async(
        self,
        request: emr_20160408_models.KillFlowJobRequest,
    ) -> emr_20160408_models.KillFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.kill_flow_job_with_options_async(request, runtime)

    def list_advice_action_with_options(
        self,
        request: emr_20160408_models.ListAdviceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListAdviceActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListAdviceActionResponse().from_map(
            self.do_rpcrequest('ListAdviceAction', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_advice_action_with_options_async(
        self,
        request: emr_20160408_models.ListAdviceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListAdviceActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListAdviceActionResponse().from_map(
            await self.do_rpcrequest_async('ListAdviceAction', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_advice_action(
        self,
        request: emr_20160408_models.ListAdviceActionRequest,
    ) -> emr_20160408_models.ListAdviceActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_advice_action_with_options(request, runtime)

    async def list_advice_action_async(
        self,
        request: emr_20160408_models.ListAdviceActionRequest,
    ) -> emr_20160408_models.ListAdviceActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_advice_action_with_options_async(request, runtime)

    def list_apm_application_with_options(
        self,
        request: emr_20160408_models.ListApmApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListApmApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListApmApplicationResponse().from_map(
            self.do_rpcrequest('ListApmApplication', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_apm_application_with_options_async(
        self,
        request: emr_20160408_models.ListApmApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListApmApplicationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListApmApplicationResponse().from_map(
            await self.do_rpcrequest_async('ListApmApplication', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_apm_application(
        self,
        request: emr_20160408_models.ListApmApplicationRequest,
    ) -> emr_20160408_models.ListApmApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_apm_application_with_options(request, runtime)

    async def list_apm_application_async(
        self,
        request: emr_20160408_models.ListApmApplicationRequest,
    ) -> emr_20160408_models.ListApmApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_apm_application_with_options_async(request, runtime)

    def list_backups_with_options(
        self,
        request: emr_20160408_models.ListBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListBackupsResponse().from_map(
            self.do_rpcrequest('ListBackups', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_backups_with_options_async(
        self,
        request: emr_20160408_models.ListBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListBackupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListBackupsResponse().from_map(
            await self.do_rpcrequest_async('ListBackups', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_backups(
        self,
        request: emr_20160408_models.ListBackupsRequest,
    ) -> emr_20160408_models.ListBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_backups_with_options(request, runtime)

    async def list_backups_async(
        self,
        request: emr_20160408_models.ListBackupsRequest,
    ) -> emr_20160408_models.ListBackupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_backups_with_options_async(request, runtime)

    def list_cluster_host_with_options(
        self,
        request: emr_20160408_models.ListClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterHostResponse().from_map(
            self.do_rpcrequest('ListClusterHost', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_host_with_options_async(
        self,
        request: emr_20160408_models.ListClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterHostResponse().from_map(
            await self.do_rpcrequest_async('ListClusterHost', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_host(
        self,
        request: emr_20160408_models.ListClusterHostRequest,
    ) -> emr_20160408_models.ListClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_host_with_options(request, runtime)

    async def list_cluster_host_async(
        self,
        request: emr_20160408_models.ListClusterHostRequest,
    ) -> emr_20160408_models.ListClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_host_with_options_async(request, runtime)

    def list_cluster_host_component_with_options(
        self,
        request: emr_20160408_models.ListClusterHostComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterHostComponentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterHostComponentResponse().from_map(
            self.do_rpcrequest('ListClusterHostComponent', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_host_component_with_options_async(
        self,
        request: emr_20160408_models.ListClusterHostComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterHostComponentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterHostComponentResponse().from_map(
            await self.do_rpcrequest_async('ListClusterHostComponent', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_host_component(
        self,
        request: emr_20160408_models.ListClusterHostComponentRequest,
    ) -> emr_20160408_models.ListClusterHostComponentResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_host_component_with_options(request, runtime)

    async def list_cluster_host_component_async(
        self,
        request: emr_20160408_models.ListClusterHostComponentRequest,
    ) -> emr_20160408_models.ListClusterHostComponentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_host_component_with_options_async(request, runtime)

    def list_cluster_host_group_with_options(
        self,
        request: emr_20160408_models.ListClusterHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterHostGroupResponse().from_map(
            self.do_rpcrequest('ListClusterHostGroup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_host_group_with_options_async(
        self,
        request: emr_20160408_models.ListClusterHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterHostGroupResponse().from_map(
            await self.do_rpcrequest_async('ListClusterHostGroup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_host_group(
        self,
        request: emr_20160408_models.ListClusterHostGroupRequest,
    ) -> emr_20160408_models.ListClusterHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_host_group_with_options(request, runtime)

    async def list_cluster_host_group_async(
        self,
        request: emr_20160408_models.ListClusterHostGroupRequest,
    ) -> emr_20160408_models.ListClusterHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_host_group_with_options_async(request, runtime)

    def list_cluster_installed_service_with_options(
        self,
        request: emr_20160408_models.ListClusterInstalledServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterInstalledServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterInstalledServiceResponse().from_map(
            self.do_rpcrequest('ListClusterInstalledService', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_installed_service_with_options_async(
        self,
        request: emr_20160408_models.ListClusterInstalledServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterInstalledServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterInstalledServiceResponse().from_map(
            await self.do_rpcrequest_async('ListClusterInstalledService', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_installed_service(
        self,
        request: emr_20160408_models.ListClusterInstalledServiceRequest,
    ) -> emr_20160408_models.ListClusterInstalledServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_installed_service_with_options(request, runtime)

    async def list_cluster_installed_service_async(
        self,
        request: emr_20160408_models.ListClusterInstalledServiceRequest,
    ) -> emr_20160408_models.ListClusterInstalledServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_installed_service_with_options_async(request, runtime)

    def list_cluster_operation_with_options(
        self,
        request: emr_20160408_models.ListClusterOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterOperationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterOperationResponse().from_map(
            self.do_rpcrequest('ListClusterOperation', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_operation_with_options_async(
        self,
        request: emr_20160408_models.ListClusterOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterOperationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterOperationResponse().from_map(
            await self.do_rpcrequest_async('ListClusterOperation', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_operation(
        self,
        request: emr_20160408_models.ListClusterOperationRequest,
    ) -> emr_20160408_models.ListClusterOperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_operation_with_options(request, runtime)

    async def list_cluster_operation_async(
        self,
        request: emr_20160408_models.ListClusterOperationRequest,
    ) -> emr_20160408_models.ListClusterOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_operation_with_options_async(request, runtime)

    def list_cluster_operation_host_with_options(
        self,
        request: emr_20160408_models.ListClusterOperationHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterOperationHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterOperationHostResponse().from_map(
            self.do_rpcrequest('ListClusterOperationHost', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_operation_host_with_options_async(
        self,
        request: emr_20160408_models.ListClusterOperationHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterOperationHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterOperationHostResponse().from_map(
            await self.do_rpcrequest_async('ListClusterOperationHost', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_operation_host(
        self,
        request: emr_20160408_models.ListClusterOperationHostRequest,
    ) -> emr_20160408_models.ListClusterOperationHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_operation_host_with_options(request, runtime)

    async def list_cluster_operation_host_async(
        self,
        request: emr_20160408_models.ListClusterOperationHostRequest,
    ) -> emr_20160408_models.ListClusterOperationHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_operation_host_with_options_async(request, runtime)

    def list_cluster_operation_host_task_with_options(
        self,
        request: emr_20160408_models.ListClusterOperationHostTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterOperationHostTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterOperationHostTaskResponse().from_map(
            self.do_rpcrequest('ListClusterOperationHostTask', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_operation_host_task_with_options_async(
        self,
        request: emr_20160408_models.ListClusterOperationHostTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterOperationHostTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterOperationHostTaskResponse().from_map(
            await self.do_rpcrequest_async('ListClusterOperationHostTask', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_operation_host_task(
        self,
        request: emr_20160408_models.ListClusterOperationHostTaskRequest,
    ) -> emr_20160408_models.ListClusterOperationHostTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_operation_host_task_with_options(request, runtime)

    async def list_cluster_operation_host_task_async(
        self,
        request: emr_20160408_models.ListClusterOperationHostTaskRequest,
    ) -> emr_20160408_models.ListClusterOperationHostTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_operation_host_task_with_options_async(request, runtime)

    def list_cluster_operation_task_with_options(
        self,
        request: emr_20160408_models.ListClusterOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterOperationTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterOperationTaskResponse().from_map(
            self.do_rpcrequest('ListClusterOperationTask', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_operation_task_with_options_async(
        self,
        request: emr_20160408_models.ListClusterOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterOperationTaskResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterOperationTaskResponse().from_map(
            await self.do_rpcrequest_async('ListClusterOperationTask', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_operation_task(
        self,
        request: emr_20160408_models.ListClusterOperationTaskRequest,
    ) -> emr_20160408_models.ListClusterOperationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_operation_task_with_options(request, runtime)

    async def list_cluster_operation_task_async(
        self,
        request: emr_20160408_models.ListClusterOperationTaskRequest,
    ) -> emr_20160408_models.ListClusterOperationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_operation_task_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        request: emr_20160408_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClustersResponse().from_map(
            self.do_rpcrequest('ListClusters', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: emr_20160408_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClustersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClustersResponse().from_map(
            await self.do_rpcrequest_async('ListClusters', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_clusters(
        self,
        request: emr_20160408_models.ListClustersRequest,
    ) -> emr_20160408_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: emr_20160408_models.ListClustersRequest,
    ) -> emr_20160408_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_cluster_service_with_options(
        self,
        request: emr_20160408_models.ListClusterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterServiceResponse().from_map(
            self.do_rpcrequest('ListClusterService', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_service_with_options_async(
        self,
        request: emr_20160408_models.ListClusterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterServiceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterServiceResponse().from_map(
            await self.do_rpcrequest_async('ListClusterService', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_service(
        self,
        request: emr_20160408_models.ListClusterServiceRequest,
    ) -> emr_20160408_models.ListClusterServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_service_with_options(request, runtime)

    async def list_cluster_service_async(
        self,
        request: emr_20160408_models.ListClusterServiceRequest,
    ) -> emr_20160408_models.ListClusterServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_service_with_options_async(request, runtime)

    def list_cluster_service_component_with_options(
        self,
        request: emr_20160408_models.ListClusterServiceComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterServiceComponentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterServiceComponentResponse().from_map(
            self.do_rpcrequest('ListClusterServiceComponent', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_service_component_with_options_async(
        self,
        request: emr_20160408_models.ListClusterServiceComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterServiceComponentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterServiceComponentResponse().from_map(
            await self.do_rpcrequest_async('ListClusterServiceComponent', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_service_component(
        self,
        request: emr_20160408_models.ListClusterServiceComponentRequest,
    ) -> emr_20160408_models.ListClusterServiceComponentResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_service_component_with_options(request, runtime)

    async def list_cluster_service_component_async(
        self,
        request: emr_20160408_models.ListClusterServiceComponentRequest,
    ) -> emr_20160408_models.ListClusterServiceComponentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_service_component_with_options_async(request, runtime)

    def list_cluster_service_component_health_info_with_options(
        self,
        request: emr_20160408_models.ListClusterServiceComponentHealthInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterServiceComponentHealthInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterServiceComponentHealthInfoResponse().from_map(
            self.do_rpcrequest('ListClusterServiceComponentHealthInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_service_component_health_info_with_options_async(
        self,
        request: emr_20160408_models.ListClusterServiceComponentHealthInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterServiceComponentHealthInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterServiceComponentHealthInfoResponse().from_map(
            await self.do_rpcrequest_async('ListClusterServiceComponentHealthInfo', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_service_component_health_info(
        self,
        request: emr_20160408_models.ListClusterServiceComponentHealthInfoRequest,
    ) -> emr_20160408_models.ListClusterServiceComponentHealthInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_service_component_health_info_with_options(request, runtime)

    async def list_cluster_service_component_health_info_async(
        self,
        request: emr_20160408_models.ListClusterServiceComponentHealthInfoRequest,
    ) -> emr_20160408_models.ListClusterServiceComponentHealthInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_service_component_health_info_with_options_async(request, runtime)

    def list_cluster_service_config_history_with_options(
        self,
        request: emr_20160408_models.ListClusterServiceConfigHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterServiceConfigHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterServiceConfigHistoryResponse().from_map(
            self.do_rpcrequest('ListClusterServiceConfigHistory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_service_config_history_with_options_async(
        self,
        request: emr_20160408_models.ListClusterServiceConfigHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterServiceConfigHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterServiceConfigHistoryResponse().from_map(
            await self.do_rpcrequest_async('ListClusterServiceConfigHistory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_service_config_history(
        self,
        request: emr_20160408_models.ListClusterServiceConfigHistoryRequest,
    ) -> emr_20160408_models.ListClusterServiceConfigHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_service_config_history_with_options(request, runtime)

    async def list_cluster_service_config_history_async(
        self,
        request: emr_20160408_models.ListClusterServiceConfigHistoryRequest,
    ) -> emr_20160408_models.ListClusterServiceConfigHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_service_config_history_with_options_async(request, runtime)

    def list_cluster_service_quick_link_with_options(
        self,
        request: emr_20160408_models.ListClusterServiceQuickLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterServiceQuickLinkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterServiceQuickLinkResponse().from_map(
            self.do_rpcrequest('ListClusterServiceQuickLink', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_service_quick_link_with_options_async(
        self,
        request: emr_20160408_models.ListClusterServiceQuickLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterServiceQuickLinkResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterServiceQuickLinkResponse().from_map(
            await self.do_rpcrequest_async('ListClusterServiceQuickLink', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_service_quick_link(
        self,
        request: emr_20160408_models.ListClusterServiceQuickLinkRequest,
    ) -> emr_20160408_models.ListClusterServiceQuickLinkResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_service_quick_link_with_options(request, runtime)

    async def list_cluster_service_quick_link_async(
        self,
        request: emr_20160408_models.ListClusterServiceQuickLinkRequest,
    ) -> emr_20160408_models.ListClusterServiceQuickLinkResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_service_quick_link_with_options_async(request, runtime)

    def list_cluster_templates_with_options(
        self,
        request: emr_20160408_models.ListClusterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterTemplatesResponse().from_map(
            self.do_rpcrequest('ListClusterTemplates', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_cluster_templates_with_options_async(
        self,
        request: emr_20160408_models.ListClusterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterTemplatesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListClusterTemplatesResponse().from_map(
            await self.do_rpcrequest_async('ListClusterTemplates', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_templates(
        self,
        request: emr_20160408_models.ListClusterTemplatesRequest,
    ) -> emr_20160408_models.ListClusterTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_templates_with_options(request, runtime)

    async def list_cluster_templates_async(
        self,
        request: emr_20160408_models.ListClusterTemplatesRequest,
    ) -> emr_20160408_models.ListClusterTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_templates_with_options_async(request, runtime)

    def list_data_source_with_options(
        self,
        request: emr_20160408_models.ListDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListDataSourceResponse().from_map(
            self.do_rpcrequest('ListDataSource', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_data_source_with_options_async(
        self,
        request: emr_20160408_models.ListDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListDataSourceResponse().from_map(
            await self.do_rpcrequest_async('ListDataSource', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_data_source(
        self,
        request: emr_20160408_models.ListDataSourceRequest,
    ) -> emr_20160408_models.ListDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_data_source_with_options(request, runtime)

    async def list_data_source_async(
        self,
        request: emr_20160408_models.ListDataSourceRequest,
    ) -> emr_20160408_models.ListDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_data_source_with_options_async(request, runtime)

    def list_emr_available_config_with_options(
        self,
        request: emr_20160408_models.ListEmrAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListEmrAvailableConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListEmrAvailableConfigResponse().from_map(
            self.do_rpcrequest('ListEmrAvailableConfig', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_emr_available_config_with_options_async(
        self,
        request: emr_20160408_models.ListEmrAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListEmrAvailableConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListEmrAvailableConfigResponse().from_map(
            await self.do_rpcrequest_async('ListEmrAvailableConfig', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_emr_available_config(
        self,
        request: emr_20160408_models.ListEmrAvailableConfigRequest,
    ) -> emr_20160408_models.ListEmrAvailableConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_emr_available_config_with_options(request, runtime)

    async def list_emr_available_config_async(
        self,
        request: emr_20160408_models.ListEmrAvailableConfigRequest,
    ) -> emr_20160408_models.ListEmrAvailableConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_emr_available_config_with_options_async(request, runtime)

    def list_emr_available_resource_with_options(
        self,
        request: emr_20160408_models.ListEmrAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListEmrAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListEmrAvailableResourceResponse().from_map(
            self.do_rpcrequest('ListEmrAvailableResource', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_emr_available_resource_with_options_async(
        self,
        request: emr_20160408_models.ListEmrAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListEmrAvailableResourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListEmrAvailableResourceResponse().from_map(
            await self.do_rpcrequest_async('ListEmrAvailableResource', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_emr_available_resource(
        self,
        request: emr_20160408_models.ListEmrAvailableResourceRequest,
    ) -> emr_20160408_models.ListEmrAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_emr_available_resource_with_options(request, runtime)

    async def list_emr_available_resource_async(
        self,
        request: emr_20160408_models.ListEmrAvailableResourceRequest,
    ) -> emr_20160408_models.ListEmrAvailableResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_emr_available_resource_with_options_async(request, runtime)

    def list_emr_main_version_with_options(
        self,
        request: emr_20160408_models.ListEmrMainVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListEmrMainVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListEmrMainVersionResponse().from_map(
            self.do_rpcrequest('ListEmrMainVersion', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_emr_main_version_with_options_async(
        self,
        request: emr_20160408_models.ListEmrMainVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListEmrMainVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListEmrMainVersionResponse().from_map(
            await self.do_rpcrequest_async('ListEmrMainVersion', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_emr_main_version(
        self,
        request: emr_20160408_models.ListEmrMainVersionRequest,
    ) -> emr_20160408_models.ListEmrMainVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_emr_main_version_with_options(request, runtime)

    async def list_emr_main_version_async(
        self,
        request: emr_20160408_models.ListEmrMainVersionRequest,
    ) -> emr_20160408_models.ListEmrMainVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_emr_main_version_with_options_async(request, runtime)

    def list_execution_plan_instances_with_options(
        self,
        request: emr_20160408_models.ListExecutionPlanInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListExecutionPlanInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListExecutionPlanInstancesResponse().from_map(
            self.do_rpcrequest('ListExecutionPlanInstances', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_execution_plan_instances_with_options_async(
        self,
        request: emr_20160408_models.ListExecutionPlanInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListExecutionPlanInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListExecutionPlanInstancesResponse().from_map(
            await self.do_rpcrequest_async('ListExecutionPlanInstances', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_execution_plan_instances(
        self,
        request: emr_20160408_models.ListExecutionPlanInstancesRequest,
    ) -> emr_20160408_models.ListExecutionPlanInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_execution_plan_instances_with_options(request, runtime)

    async def list_execution_plan_instances_async(
        self,
        request: emr_20160408_models.ListExecutionPlanInstancesRequest,
    ) -> emr_20160408_models.ListExecutionPlanInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_execution_plan_instances_with_options_async(request, runtime)

    def list_execution_plans_with_options(
        self,
        request: emr_20160408_models.ListExecutionPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListExecutionPlansResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListExecutionPlansResponse().from_map(
            self.do_rpcrequest('ListExecutionPlans', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_execution_plans_with_options_async(
        self,
        request: emr_20160408_models.ListExecutionPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListExecutionPlansResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListExecutionPlansResponse().from_map(
            await self.do_rpcrequest_async('ListExecutionPlans', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_execution_plans(
        self,
        request: emr_20160408_models.ListExecutionPlansRequest,
    ) -> emr_20160408_models.ListExecutionPlansResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_execution_plans_with_options(request, runtime)

    async def list_execution_plans_async(
        self,
        request: emr_20160408_models.ListExecutionPlansRequest,
    ) -> emr_20160408_models.ListExecutionPlansResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_execution_plans_with_options_async(request, runtime)

    def list_flow_with_options(
        self,
        request: emr_20160408_models.ListFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowResponse().from_map(
            self.do_rpcrequest('ListFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_with_options_async(
        self,
        request: emr_20160408_models.ListFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowResponse().from_map(
            await self.do_rpcrequest_async('ListFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow(
        self,
        request: emr_20160408_models.ListFlowRequest,
    ) -> emr_20160408_models.ListFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_with_options(request, runtime)

    async def list_flow_async(
        self,
        request: emr_20160408_models.ListFlowRequest,
    ) -> emr_20160408_models.ListFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_with_options_async(request, runtime)

    def list_flow_category_with_options(
        self,
        request: emr_20160408_models.ListFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowCategoryResponse().from_map(
            self.do_rpcrequest('ListFlowCategory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_category_with_options_async(
        self,
        request: emr_20160408_models.ListFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowCategoryResponse().from_map(
            await self.do_rpcrequest_async('ListFlowCategory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_category(
        self,
        request: emr_20160408_models.ListFlowCategoryRequest,
    ) -> emr_20160408_models.ListFlowCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_category_with_options(request, runtime)

    async def list_flow_category_async(
        self,
        request: emr_20160408_models.ListFlowCategoryRequest,
    ) -> emr_20160408_models.ListFlowCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_category_with_options_async(request, runtime)

    def list_flow_cluster_with_options(
        self,
        request: emr_20160408_models.ListFlowClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowClusterResponse().from_map(
            self.do_rpcrequest('ListFlowCluster', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_cluster_with_options_async(
        self,
        request: emr_20160408_models.ListFlowClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowClusterResponse().from_map(
            await self.do_rpcrequest_async('ListFlowCluster', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_cluster(
        self,
        request: emr_20160408_models.ListFlowClusterRequest,
    ) -> emr_20160408_models.ListFlowClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_cluster_with_options(request, runtime)

    async def list_flow_cluster_async(
        self,
        request: emr_20160408_models.ListFlowClusterRequest,
    ) -> emr_20160408_models.ListFlowClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_cluster_with_options_async(request, runtime)

    def list_flow_cluster_all_with_options(
        self,
        request: emr_20160408_models.ListFlowClusterAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowClusterAllResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowClusterAllResponse().from_map(
            self.do_rpcrequest('ListFlowClusterAll', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_cluster_all_with_options_async(
        self,
        request: emr_20160408_models.ListFlowClusterAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowClusterAllResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowClusterAllResponse().from_map(
            await self.do_rpcrequest_async('ListFlowClusterAll', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_cluster_all(
        self,
        request: emr_20160408_models.ListFlowClusterAllRequest,
    ) -> emr_20160408_models.ListFlowClusterAllResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_cluster_all_with_options(request, runtime)

    async def list_flow_cluster_all_async(
        self,
        request: emr_20160408_models.ListFlowClusterAllRequest,
    ) -> emr_20160408_models.ListFlowClusterAllResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_cluster_all_with_options_async(request, runtime)

    def list_flow_cluster_all_hosts_with_options(
        self,
        request: emr_20160408_models.ListFlowClusterAllHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowClusterAllHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowClusterAllHostsResponse().from_map(
            self.do_rpcrequest('ListFlowClusterAllHosts', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_cluster_all_hosts_with_options_async(
        self,
        request: emr_20160408_models.ListFlowClusterAllHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowClusterAllHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowClusterAllHostsResponse().from_map(
            await self.do_rpcrequest_async('ListFlowClusterAllHosts', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_cluster_all_hosts(
        self,
        request: emr_20160408_models.ListFlowClusterAllHostsRequest,
    ) -> emr_20160408_models.ListFlowClusterAllHostsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_cluster_all_hosts_with_options(request, runtime)

    async def list_flow_cluster_all_hosts_async(
        self,
        request: emr_20160408_models.ListFlowClusterAllHostsRequest,
    ) -> emr_20160408_models.ListFlowClusterAllHostsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_cluster_all_hosts_with_options_async(request, runtime)

    def list_flow_cluster_host_with_options(
        self,
        request: emr_20160408_models.ListFlowClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowClusterHostResponse().from_map(
            self.do_rpcrequest('ListFlowClusterHost', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_cluster_host_with_options_async(
        self,
        request: emr_20160408_models.ListFlowClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowClusterHostResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowClusterHostResponse().from_map(
            await self.do_rpcrequest_async('ListFlowClusterHost', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_cluster_host(
        self,
        request: emr_20160408_models.ListFlowClusterHostRequest,
    ) -> emr_20160408_models.ListFlowClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_cluster_host_with_options(request, runtime)

    async def list_flow_cluster_host_async(
        self,
        request: emr_20160408_models.ListFlowClusterHostRequest,
    ) -> emr_20160408_models.ListFlowClusterHostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_cluster_host_with_options_async(request, runtime)

    def list_flow_entity_snapshot_with_options(
        self,
        request: emr_20160408_models.ListFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowEntitySnapshotResponse().from_map(
            self.do_rpcrequest('ListFlowEntitySnapshot', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_entity_snapshot_with_options_async(
        self,
        request: emr_20160408_models.ListFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowEntitySnapshotResponse().from_map(
            await self.do_rpcrequest_async('ListFlowEntitySnapshot', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_entity_snapshot(
        self,
        request: emr_20160408_models.ListFlowEntitySnapshotRequest,
    ) -> emr_20160408_models.ListFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_entity_snapshot_with_options(request, runtime)

    async def list_flow_entity_snapshot_async(
        self,
        request: emr_20160408_models.ListFlowEntitySnapshotRequest,
    ) -> emr_20160408_models.ListFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_entity_snapshot_with_options_async(request, runtime)

    def list_flow_instance_with_options(
        self,
        request: emr_20160408_models.ListFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowInstanceResponse().from_map(
            self.do_rpcrequest('ListFlowInstance', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_instance_with_options_async(
        self,
        request: emr_20160408_models.ListFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowInstanceResponse().from_map(
            await self.do_rpcrequest_async('ListFlowInstance', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_instance(
        self,
        request: emr_20160408_models.ListFlowInstanceRequest,
    ) -> emr_20160408_models.ListFlowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_instance_with_options(request, runtime)

    async def list_flow_instance_async(
        self,
        request: emr_20160408_models.ListFlowInstanceRequest,
    ) -> emr_20160408_models.ListFlowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_instance_with_options_async(request, runtime)

    def list_flow_job_with_options(
        self,
        request: emr_20160408_models.ListFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowJobResponse().from_map(
            self.do_rpcrequest('ListFlowJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_job_with_options_async(
        self,
        request: emr_20160408_models.ListFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowJobResponse().from_map(
            await self.do_rpcrequest_async('ListFlowJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_job(
        self,
        request: emr_20160408_models.ListFlowJobRequest,
    ) -> emr_20160408_models.ListFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_job_with_options(request, runtime)

    async def list_flow_job_async(
        self,
        request: emr_20160408_models.ListFlowJobRequest,
    ) -> emr_20160408_models.ListFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_job_with_options_async(request, runtime)

    def list_flow_job_history_with_options(
        self,
        request: emr_20160408_models.ListFlowJobHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowJobHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowJobHistoryResponse().from_map(
            self.do_rpcrequest('ListFlowJobHistory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_job_history_with_options_async(
        self,
        request: emr_20160408_models.ListFlowJobHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowJobHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowJobHistoryResponse().from_map(
            await self.do_rpcrequest_async('ListFlowJobHistory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_job_history(
        self,
        request: emr_20160408_models.ListFlowJobHistoryRequest,
    ) -> emr_20160408_models.ListFlowJobHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_job_history_with_options(request, runtime)

    async def list_flow_job_history_async(
        self,
        request: emr_20160408_models.ListFlowJobHistoryRequest,
    ) -> emr_20160408_models.ListFlowJobHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_job_history_with_options_async(request, runtime)

    def list_flow_node_instance_with_options(
        self,
        request: emr_20160408_models.ListFlowNodeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowNodeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowNodeInstanceResponse().from_map(
            self.do_rpcrequest('ListFlowNodeInstance', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_node_instance_with_options_async(
        self,
        request: emr_20160408_models.ListFlowNodeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowNodeInstanceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowNodeInstanceResponse().from_map(
            await self.do_rpcrequest_async('ListFlowNodeInstance', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_node_instance(
        self,
        request: emr_20160408_models.ListFlowNodeInstanceRequest,
    ) -> emr_20160408_models.ListFlowNodeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_node_instance_with_options(request, runtime)

    async def list_flow_node_instance_async(
        self,
        request: emr_20160408_models.ListFlowNodeInstanceRequest,
    ) -> emr_20160408_models.ListFlowNodeInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_node_instance_with_options_async(request, runtime)

    def list_flow_node_instance_container_status_with_options(
        self,
        request: emr_20160408_models.ListFlowNodeInstanceContainerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowNodeInstanceContainerStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowNodeInstanceContainerStatusResponse().from_map(
            self.do_rpcrequest('ListFlowNodeInstanceContainerStatus', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_node_instance_container_status_with_options_async(
        self,
        request: emr_20160408_models.ListFlowNodeInstanceContainerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowNodeInstanceContainerStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowNodeInstanceContainerStatusResponse().from_map(
            await self.do_rpcrequest_async('ListFlowNodeInstanceContainerStatus', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_node_instance_container_status(
        self,
        request: emr_20160408_models.ListFlowNodeInstanceContainerStatusRequest,
    ) -> emr_20160408_models.ListFlowNodeInstanceContainerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_node_instance_container_status_with_options(request, runtime)

    async def list_flow_node_instance_container_status_async(
        self,
        request: emr_20160408_models.ListFlowNodeInstanceContainerStatusRequest,
    ) -> emr_20160408_models.ListFlowNodeInstanceContainerStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_node_instance_container_status_with_options_async(request, runtime)

    def list_flow_node_sql_result_with_options(
        self,
        request: emr_20160408_models.ListFlowNodeSqlResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowNodeSqlResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowNodeSqlResultResponse().from_map(
            self.do_rpcrequest('ListFlowNodeSqlResult', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_node_sql_result_with_options_async(
        self,
        request: emr_20160408_models.ListFlowNodeSqlResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowNodeSqlResultResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowNodeSqlResultResponse().from_map(
            await self.do_rpcrequest_async('ListFlowNodeSqlResult', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_node_sql_result(
        self,
        request: emr_20160408_models.ListFlowNodeSqlResultRequest,
    ) -> emr_20160408_models.ListFlowNodeSqlResultResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_node_sql_result_with_options(request, runtime)

    async def list_flow_node_sql_result_async(
        self,
        request: emr_20160408_models.ListFlowNodeSqlResultRequest,
    ) -> emr_20160408_models.ListFlowNodeSqlResultResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_node_sql_result_with_options_async(request, runtime)

    def list_flow_project_with_options(
        self,
        request: emr_20160408_models.ListFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowProjectResponse().from_map(
            self.do_rpcrequest('ListFlowProject', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_project_with_options_async(
        self,
        request: emr_20160408_models.ListFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowProjectResponse().from_map(
            await self.do_rpcrequest_async('ListFlowProject', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_project(
        self,
        request: emr_20160408_models.ListFlowProjectRequest,
    ) -> emr_20160408_models.ListFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_project_with_options(request, runtime)

    async def list_flow_project_async(
        self,
        request: emr_20160408_models.ListFlowProjectRequest,
    ) -> emr_20160408_models.ListFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_project_with_options_async(request, runtime)

    def list_flow_project_cluster_setting_with_options(
        self,
        request: emr_20160408_models.ListFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowProjectClusterSettingResponse().from_map(
            self.do_rpcrequest('ListFlowProjectClusterSetting', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_project_cluster_setting_with_options_async(
        self,
        request: emr_20160408_models.ListFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowProjectClusterSettingResponse().from_map(
            await self.do_rpcrequest_async('ListFlowProjectClusterSetting', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_project_cluster_setting(
        self,
        request: emr_20160408_models.ListFlowProjectClusterSettingRequest,
    ) -> emr_20160408_models.ListFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_project_cluster_setting_with_options(request, runtime)

    async def list_flow_project_cluster_setting_async(
        self,
        request: emr_20160408_models.ListFlowProjectClusterSettingRequest,
    ) -> emr_20160408_models.ListFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_project_cluster_setting_with_options_async(request, runtime)

    def list_flow_project_user_with_options(
        self,
        request: emr_20160408_models.ListFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowProjectUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowProjectUserResponse().from_map(
            self.do_rpcrequest('ListFlowProjectUser', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_project_user_with_options_async(
        self,
        request: emr_20160408_models.ListFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowProjectUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListFlowProjectUserResponse().from_map(
            await self.do_rpcrequest_async('ListFlowProjectUser', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_project_user(
        self,
        request: emr_20160408_models.ListFlowProjectUserRequest,
    ) -> emr_20160408_models.ListFlowProjectUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_project_user_with_options(request, runtime)

    async def list_flow_project_user_async(
        self,
        request: emr_20160408_models.ListFlowProjectUserRequest,
    ) -> emr_20160408_models.ListFlowProjectUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_project_user_with_options_async(request, runtime)

    def list_job_execution_instances_with_options(
        self,
        request: emr_20160408_models.ListJobExecutionInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListJobExecutionInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListJobExecutionInstancesResponse().from_map(
            self.do_rpcrequest('ListJobExecutionInstances', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_job_execution_instances_with_options_async(
        self,
        request: emr_20160408_models.ListJobExecutionInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListJobExecutionInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListJobExecutionInstancesResponse().from_map(
            await self.do_rpcrequest_async('ListJobExecutionInstances', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_job_execution_instances(
        self,
        request: emr_20160408_models.ListJobExecutionInstancesRequest,
    ) -> emr_20160408_models.ListJobExecutionInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_job_execution_instances_with_options(request, runtime)

    async def list_job_execution_instances_async(
        self,
        request: emr_20160408_models.ListJobExecutionInstancesRequest,
    ) -> emr_20160408_models.ListJobExecutionInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_job_execution_instances_with_options_async(request, runtime)

    def list_job_instance_workers_with_options(
        self,
        request: emr_20160408_models.ListJobInstanceWorkersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListJobInstanceWorkersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListJobInstanceWorkersResponse().from_map(
            self.do_rpcrequest('ListJobInstanceWorkers', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_job_instance_workers_with_options_async(
        self,
        request: emr_20160408_models.ListJobInstanceWorkersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListJobInstanceWorkersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListJobInstanceWorkersResponse().from_map(
            await self.do_rpcrequest_async('ListJobInstanceWorkers', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_job_instance_workers(
        self,
        request: emr_20160408_models.ListJobInstanceWorkersRequest,
    ) -> emr_20160408_models.ListJobInstanceWorkersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_job_instance_workers_with_options(request, runtime)

    async def list_job_instance_workers_async(
        self,
        request: emr_20160408_models.ListJobInstanceWorkersRequest,
    ) -> emr_20160408_models.ListJobInstanceWorkersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_job_instance_workers_with_options_async(request, runtime)

    def list_jobs_with_options(
        self,
        request: emr_20160408_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListJobsResponse().from_map(
            self.do_rpcrequest('ListJobs', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: emr_20160408_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListJobsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListJobsResponse().from_map(
            await self.do_rpcrequest_async('ListJobs', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_jobs(
        self,
        request: emr_20160408_models.ListJobsRequest,
    ) -> emr_20160408_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_jobs_with_options(request, runtime)

    async def list_jobs_async(
        self,
        request: emr_20160408_models.ListJobsRequest,
    ) -> emr_20160408_models.ListJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_jobs_with_options_async(request, runtime)

    def list_libraries_with_options(
        self,
        request: emr_20160408_models.ListLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListLibrariesResponse().from_map(
            self.do_rpcrequest('ListLibraries', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_libraries_with_options_async(
        self,
        request: emr_20160408_models.ListLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListLibrariesResponse().from_map(
            await self.do_rpcrequest_async('ListLibraries', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_libraries(
        self,
        request: emr_20160408_models.ListLibrariesRequest,
    ) -> emr_20160408_models.ListLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_libraries_with_options(request, runtime)

    async def list_libraries_async(
        self,
        request: emr_20160408_models.ListLibrariesRequest,
    ) -> emr_20160408_models.ListLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_libraries_with_options_async(request, runtime)

    def list_library_install_tasks_with_options(
        self,
        request: emr_20160408_models.ListLibraryInstallTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListLibraryInstallTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListLibraryInstallTasksResponse().from_map(
            self.do_rpcrequest('ListLibraryInstallTasks', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_library_install_tasks_with_options_async(
        self,
        request: emr_20160408_models.ListLibraryInstallTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListLibraryInstallTasksResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListLibraryInstallTasksResponse().from_map(
            await self.do_rpcrequest_async('ListLibraryInstallTasks', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_library_install_tasks(
        self,
        request: emr_20160408_models.ListLibraryInstallTasksRequest,
    ) -> emr_20160408_models.ListLibraryInstallTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_library_install_tasks_with_options(request, runtime)

    async def list_library_install_tasks_async(
        self,
        request: emr_20160408_models.ListLibraryInstallTasksRequest,
    ) -> emr_20160408_models.ListLibraryInstallTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_library_install_tasks_with_options_async(request, runtime)

    def list_library_status_with_options(
        self,
        request: emr_20160408_models.ListLibraryStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListLibraryStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListLibraryStatusResponse().from_map(
            self.do_rpcrequest('ListLibraryStatus', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_library_status_with_options_async(
        self,
        request: emr_20160408_models.ListLibraryStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListLibraryStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListLibraryStatusResponse().from_map(
            await self.do_rpcrequest_async('ListLibraryStatus', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_library_status(
        self,
        request: emr_20160408_models.ListLibraryStatusRequest,
    ) -> emr_20160408_models.ListLibraryStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_library_status_with_options(request, runtime)

    async def list_library_status_async(
        self,
        request: emr_20160408_models.ListLibraryStatusRequest,
    ) -> emr_20160408_models.ListLibraryStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_library_status_with_options_async(request, runtime)

    def list_meta_cluster_with_options(
        self,
        request: emr_20160408_models.ListMetaClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListMetaClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListMetaClusterResponse().from_map(
            self.do_rpcrequest('ListMetaCluster', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_meta_cluster_with_options_async(
        self,
        request: emr_20160408_models.ListMetaClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListMetaClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListMetaClusterResponse().from_map(
            await self.do_rpcrequest_async('ListMetaCluster', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_meta_cluster(
        self,
        request: emr_20160408_models.ListMetaClusterRequest,
    ) -> emr_20160408_models.ListMetaClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_meta_cluster_with_options(request, runtime)

    async def list_meta_cluster_async(
        self,
        request: emr_20160408_models.ListMetaClusterRequest,
    ) -> emr_20160408_models.ListMetaClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_meta_cluster_with_options_async(request, runtime)

    def list_meta_data_source_cluster_for_outer_with_options(
        self,
        request: emr_20160408_models.ListMetaDataSourceClusterForOuterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListMetaDataSourceClusterForOuterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListMetaDataSourceClusterForOuterResponse().from_map(
            self.do_rpcrequest('ListMetaDataSourceClusterForOuter', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_meta_data_source_cluster_for_outer_with_options_async(
        self,
        request: emr_20160408_models.ListMetaDataSourceClusterForOuterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListMetaDataSourceClusterForOuterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListMetaDataSourceClusterForOuterResponse().from_map(
            await self.do_rpcrequest_async('ListMetaDataSourceClusterForOuter', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_meta_data_source_cluster_for_outer(
        self,
        request: emr_20160408_models.ListMetaDataSourceClusterForOuterRequest,
    ) -> emr_20160408_models.ListMetaDataSourceClusterForOuterResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_meta_data_source_cluster_for_outer_with_options(request, runtime)

    async def list_meta_data_source_cluster_for_outer_async(
        self,
        request: emr_20160408_models.ListMetaDataSourceClusterForOuterRequest,
    ) -> emr_20160408_models.ListMetaDataSourceClusterForOuterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_meta_data_source_cluster_for_outer_with_options_async(request, runtime)

    def list_notes_with_options(
        self,
        request: emr_20160408_models.ListNotesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListNotesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListNotesResponse().from_map(
            self.do_rpcrequest('ListNotes', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_notes_with_options_async(
        self,
        request: emr_20160408_models.ListNotesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListNotesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListNotesResponse().from_map(
            await self.do_rpcrequest_async('ListNotes', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_notes(
        self,
        request: emr_20160408_models.ListNotesRequest,
    ) -> emr_20160408_models.ListNotesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_notes_with_options(request, runtime)

    async def list_notes_async(
        self,
        request: emr_20160408_models.ListNotesRequest,
    ) -> emr_20160408_models.ListNotesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_notes_with_options_async(request, runtime)

    def list_resource_pool_with_options(
        self,
        request: emr_20160408_models.ListResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListResourcePoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListResourcePoolResponse().from_map(
            self.do_rpcrequest('ListResourcePool', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_resource_pool_with_options_async(
        self,
        request: emr_20160408_models.ListResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListResourcePoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListResourcePoolResponse().from_map(
            await self.do_rpcrequest_async('ListResourcePool', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_resource_pool(
        self,
        request: emr_20160408_models.ListResourcePoolRequest,
    ) -> emr_20160408_models.ListResourcePoolResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_pool_with_options(request, runtime)

    async def list_resource_pool_async(
        self,
        request: emr_20160408_models.ListResourcePoolRequest,
    ) -> emr_20160408_models.ListResourcePoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_pool_with_options_async(request, runtime)

    def list_roles_with_options(
        self,
        request: emr_20160408_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListRolesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListRolesResponse().from_map(
            self.do_rpcrequest('ListRoles', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: emr_20160408_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListRolesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListRolesResponse().from_map(
            await self.do_rpcrequest_async('ListRoles', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_roles(
        self,
        request: emr_20160408_models.ListRolesRequest,
    ) -> emr_20160408_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    async def list_roles_async(
        self,
        request: emr_20160408_models.ListRolesRequest,
    ) -> emr_20160408_models.ListRolesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_roles_with_options_async(request, runtime)

    def list_scaling_activity_v2with_options(
        self,
        request: emr_20160408_models.ListScalingActivityV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListScalingActivityV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListScalingActivityV2Response().from_map(
            self.do_rpcrequest('ListScalingActivityV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_scaling_activity_v2with_options_async(
        self,
        request: emr_20160408_models.ListScalingActivityV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListScalingActivityV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListScalingActivityV2Response().from_map(
            await self.do_rpcrequest_async('ListScalingActivityV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scaling_activity_v2(
        self,
        request: emr_20160408_models.ListScalingActivityV2Request,
    ) -> emr_20160408_models.ListScalingActivityV2Response:
        runtime = util_models.RuntimeOptions()
        return self.list_scaling_activity_v2with_options(request, runtime)

    async def list_scaling_activity_v2_async(
        self,
        request: emr_20160408_models.ListScalingActivityV2Request,
    ) -> emr_20160408_models.ListScalingActivityV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.list_scaling_activity_v2with_options_async(request, runtime)

    def list_scaling_config_item_v2with_options(
        self,
        request: emr_20160408_models.ListScalingConfigItemV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListScalingConfigItemV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListScalingConfigItemV2Response().from_map(
            self.do_rpcrequest('ListScalingConfigItemV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_scaling_config_item_v2with_options_async(
        self,
        request: emr_20160408_models.ListScalingConfigItemV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListScalingConfigItemV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListScalingConfigItemV2Response().from_map(
            await self.do_rpcrequest_async('ListScalingConfigItemV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scaling_config_item_v2(
        self,
        request: emr_20160408_models.ListScalingConfigItemV2Request,
    ) -> emr_20160408_models.ListScalingConfigItemV2Response:
        runtime = util_models.RuntimeOptions()
        return self.list_scaling_config_item_v2with_options(request, runtime)

    async def list_scaling_config_item_v2_async(
        self,
        request: emr_20160408_models.ListScalingConfigItemV2Request,
    ) -> emr_20160408_models.ListScalingConfigItemV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.list_scaling_config_item_v2with_options_async(request, runtime)

    def list_scaling_group_v2with_options(
        self,
        request: emr_20160408_models.ListScalingGroupV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListScalingGroupV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListScalingGroupV2Response().from_map(
            self.do_rpcrequest('ListScalingGroupV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_scaling_group_v2with_options_async(
        self,
        request: emr_20160408_models.ListScalingGroupV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListScalingGroupV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListScalingGroupV2Response().from_map(
            await self.do_rpcrequest_async('ListScalingGroupV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_scaling_group_v2(
        self,
        request: emr_20160408_models.ListScalingGroupV2Request,
    ) -> emr_20160408_models.ListScalingGroupV2Response:
        runtime = util_models.RuntimeOptions()
        return self.list_scaling_group_v2with_options(request, runtime)

    async def list_scaling_group_v2_async(
        self,
        request: emr_20160408_models.ListScalingGroupV2Request,
    ) -> emr_20160408_models.ListScalingGroupV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.list_scaling_group_v2with_options_async(request, runtime)

    def list_security_group_with_options(
        self,
        request: emr_20160408_models.ListSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListSecurityGroupResponse().from_map(
            self.do_rpcrequest('ListSecurityGroup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_security_group_with_options_async(
        self,
        request: emr_20160408_models.ListSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListSecurityGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListSecurityGroupResponse().from_map(
            await self.do_rpcrequest_async('ListSecurityGroup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_security_group(
        self,
        request: emr_20160408_models.ListSecurityGroupRequest,
    ) -> emr_20160408_models.ListSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_security_group_with_options(request, runtime)

    async def list_security_group_async(
        self,
        request: emr_20160408_models.ListSecurityGroupRequest,
    ) -> emr_20160408_models.ListSecurityGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_security_group_with_options_async(request, runtime)

    def list_stack_with_options(
        self,
        request: emr_20160408_models.ListStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListStackResponse().from_map(
            self.do_rpcrequest('ListStack', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_stack_with_options_async(
        self,
        request: emr_20160408_models.ListStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListStackResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListStackResponse().from_map(
            await self.do_rpcrequest_async('ListStack', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_stack(
        self,
        request: emr_20160408_models.ListStackRequest,
    ) -> emr_20160408_models.ListStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_with_options(request, runtime)

    async def list_stack_async(
        self,
        request: emr_20160408_models.ListStackRequest,
    ) -> emr_20160408_models.ListStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: emr_20160408_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListTagKeysResponse().from_map(
            self.do_rpcrequest('ListTagKeys', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: emr_20160408_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListTagKeysResponse().from_map(
            await self.do_rpcrequest_async('ListTagKeys', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_keys(
        self,
        request: emr_20160408_models.ListTagKeysRequest,
    ) -> emr_20160408_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: emr_20160408_models.ListTagKeysRequest,
    ) -> emr_20160408_models.ListTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: emr_20160408_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: emr_20160408_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListTagResourcesResponse().from_map(
            await self.do_rpcrequest_async('ListTagResources', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(
        self,
        request: emr_20160408_models.ListTagResourcesRequest,
    ) -> emr_20160408_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: emr_20160408_models.ListTagResourcesRequest,
    ) -> emr_20160408_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: emr_20160408_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListTagValuesResponse().from_map(
            self.do_rpcrequest('ListTagValues', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: emr_20160408_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListTagValuesResponse().from_map(
            await self.do_rpcrequest_async('ListTagValues', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_values(
        self,
        request: emr_20160408_models.ListTagValuesRequest,
    ) -> emr_20160408_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: emr_20160408_models.ListTagValuesRequest,
    ) -> emr_20160408_models.ListTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def list_users_with_options(
        self,
        request: emr_20160408_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListUsersResponse().from_map(
            self.do_rpcrequest('ListUsers', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: emr_20160408_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListUsersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListUsersResponse().from_map(
            await self.do_rpcrequest_async('ListUsers', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_users(
        self,
        request: emr_20160408_models.ListUsersRequest,
    ) -> emr_20160408_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    async def list_users_async(
        self,
        request: emr_20160408_models.ListUsersRequest,
    ) -> emr_20160408_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_users_with_options_async(request, runtime)

    def list_vswitch_with_options(
        self,
        request: emr_20160408_models.ListVswitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListVswitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListVswitchResponse().from_map(
            self.do_rpcrequest('ListVswitch', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_vswitch_with_options_async(
        self,
        request: emr_20160408_models.ListVswitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListVswitchResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ListVswitchResponse().from_map(
            await self.do_rpcrequest_async('ListVswitch', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_vswitch(
        self,
        request: emr_20160408_models.ListVswitchRequest,
    ) -> emr_20160408_models.ListVswitchResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_vswitch_with_options(request, runtime)

    async def list_vswitch_async(
        self,
        request: emr_20160408_models.ListVswitchRequest,
    ) -> emr_20160408_models.ListVswitchResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_vswitch_with_options_async(request, runtime)

    def modify_cluster_bootstrap_action_with_options(
        self,
        request: emr_20160408_models.ModifyClusterBootstrapActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterBootstrapActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyClusterBootstrapActionResponse().from_map(
            self.do_rpcrequest('ModifyClusterBootstrapAction', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cluster_bootstrap_action_with_options_async(
        self,
        request: emr_20160408_models.ModifyClusterBootstrapActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterBootstrapActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyClusterBootstrapActionResponse().from_map(
            await self.do_rpcrequest_async('ModifyClusterBootstrapAction', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cluster_bootstrap_action(
        self,
        request: emr_20160408_models.ModifyClusterBootstrapActionRequest,
    ) -> emr_20160408_models.ModifyClusterBootstrapActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_bootstrap_action_with_options(request, runtime)

    async def modify_cluster_bootstrap_action_async(
        self,
        request: emr_20160408_models.ModifyClusterBootstrapActionRequest,
    ) -> emr_20160408_models.ModifyClusterBootstrapActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_bootstrap_action_with_options_async(request, runtime)

    def modify_cluster_host_group_with_options(
        self,
        request: emr_20160408_models.ModifyClusterHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyClusterHostGroupResponse().from_map(
            self.do_rpcrequest('ModifyClusterHostGroup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cluster_host_group_with_options_async(
        self,
        request: emr_20160408_models.ModifyClusterHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyClusterHostGroupResponse().from_map(
            await self.do_rpcrequest_async('ModifyClusterHostGroup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cluster_host_group(
        self,
        request: emr_20160408_models.ModifyClusterHostGroupRequest,
    ) -> emr_20160408_models.ModifyClusterHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_host_group_with_options(request, runtime)

    async def modify_cluster_host_group_async(
        self,
        request: emr_20160408_models.ModifyClusterHostGroupRequest,
    ) -> emr_20160408_models.ModifyClusterHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_host_group_with_options_async(request, runtime)

    def modify_cluster_meta_collect_with_options(
        self,
        request: emr_20160408_models.ModifyClusterMetaCollectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterMetaCollectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyClusterMetaCollectResponse().from_map(
            self.do_rpcrequest('ModifyClusterMetaCollect', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cluster_meta_collect_with_options_async(
        self,
        request: emr_20160408_models.ModifyClusterMetaCollectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterMetaCollectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyClusterMetaCollectResponse().from_map(
            await self.do_rpcrequest_async('ModifyClusterMetaCollect', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cluster_meta_collect(
        self,
        request: emr_20160408_models.ModifyClusterMetaCollectRequest,
    ) -> emr_20160408_models.ModifyClusterMetaCollectResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_meta_collect_with_options(request, runtime)

    async def modify_cluster_meta_collect_async(
        self,
        request: emr_20160408_models.ModifyClusterMetaCollectRequest,
    ) -> emr_20160408_models.ModifyClusterMetaCollectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_meta_collect_with_options_async(request, runtime)

    def modify_cluster_name_with_options(
        self,
        request: emr_20160408_models.ModifyClusterNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyClusterNameResponse().from_map(
            self.do_rpcrequest('ModifyClusterName', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cluster_name_with_options_async(
        self,
        request: emr_20160408_models.ModifyClusterNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterNameResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyClusterNameResponse().from_map(
            await self.do_rpcrequest_async('ModifyClusterName', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cluster_name(
        self,
        request: emr_20160408_models.ModifyClusterNameRequest,
    ) -> emr_20160408_models.ModifyClusterNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_name_with_options(request, runtime)

    async def modify_cluster_name_async(
        self,
        request: emr_20160408_models.ModifyClusterNameRequest,
    ) -> emr_20160408_models.ModifyClusterNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_name_with_options_async(request, runtime)

    def modify_cluster_security_group_rule_with_options(
        self,
        request: emr_20160408_models.ModifyClusterSecurityGroupRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterSecurityGroupRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyClusterSecurityGroupRuleResponse().from_map(
            self.do_rpcrequest('ModifyClusterSecurityGroupRule', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cluster_security_group_rule_with_options_async(
        self,
        request: emr_20160408_models.ModifyClusterSecurityGroupRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterSecurityGroupRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyClusterSecurityGroupRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifyClusterSecurityGroupRule', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cluster_security_group_rule(
        self,
        request: emr_20160408_models.ModifyClusterSecurityGroupRuleRequest,
    ) -> emr_20160408_models.ModifyClusterSecurityGroupRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_security_group_rule_with_options(request, runtime)

    async def modify_cluster_security_group_rule_async(
        self,
        request: emr_20160408_models.ModifyClusterSecurityGroupRuleRequest,
    ) -> emr_20160408_models.ModifyClusterSecurityGroupRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_security_group_rule_with_options_async(request, runtime)

    def modify_cluster_service_config_with_options(
        self,
        request: emr_20160408_models.ModifyClusterServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterServiceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyClusterServiceConfigResponse().from_map(
            self.do_rpcrequest('ModifyClusterServiceConfig', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cluster_service_config_with_options_async(
        self,
        request: emr_20160408_models.ModifyClusterServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterServiceConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyClusterServiceConfigResponse().from_map(
            await self.do_rpcrequest_async('ModifyClusterServiceConfig', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cluster_service_config(
        self,
        request: emr_20160408_models.ModifyClusterServiceConfigRequest,
    ) -> emr_20160408_models.ModifyClusterServiceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_service_config_with_options(request, runtime)

    async def modify_cluster_service_config_async(
        self,
        request: emr_20160408_models.ModifyClusterServiceConfigRequest,
    ) -> emr_20160408_models.ModifyClusterServiceConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_service_config_with_options_async(request, runtime)

    def modify_cluster_template_with_options(
        self,
        request: emr_20160408_models.ModifyClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyClusterTemplateResponse().from_map(
            self.do_rpcrequest('ModifyClusterTemplate', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_cluster_template_with_options_async(
        self,
        request: emr_20160408_models.ModifyClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyClusterTemplateResponse().from_map(
            await self.do_rpcrequest_async('ModifyClusterTemplate', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_cluster_template(
        self,
        request: emr_20160408_models.ModifyClusterTemplateRequest,
    ) -> emr_20160408_models.ModifyClusterTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_cluster_template_with_options(request, runtime)

    async def modify_cluster_template_async(
        self,
        request: emr_20160408_models.ModifyClusterTemplateRequest,
    ) -> emr_20160408_models.ModifyClusterTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_cluster_template_with_options_async(request, runtime)

    def modify_execution_plan_with_options(
        self,
        request: emr_20160408_models.ModifyExecutionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyExecutionPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyExecutionPlanResponse().from_map(
            self.do_rpcrequest('ModifyExecutionPlan', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_execution_plan_with_options_async(
        self,
        request: emr_20160408_models.ModifyExecutionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyExecutionPlanResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyExecutionPlanResponse().from_map(
            await self.do_rpcrequest_async('ModifyExecutionPlan', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_execution_plan(
        self,
        request: emr_20160408_models.ModifyExecutionPlanRequest,
    ) -> emr_20160408_models.ModifyExecutionPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_execution_plan_with_options(request, runtime)

    async def modify_execution_plan_async(
        self,
        request: emr_20160408_models.ModifyExecutionPlanRequest,
    ) -> emr_20160408_models.ModifyExecutionPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_execution_plan_with_options_async(request, runtime)

    def modify_flow_with_options(
        self,
        request: emr_20160408_models.ModifyFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyFlowResponse().from_map(
            self.do_rpcrequest('ModifyFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_flow_with_options_async(
        self,
        request: emr_20160408_models.ModifyFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyFlowResponse().from_map(
            await self.do_rpcrequest_async('ModifyFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow(
        self,
        request: emr_20160408_models.ModifyFlowRequest,
    ) -> emr_20160408_models.ModifyFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_with_options(request, runtime)

    async def modify_flow_async(
        self,
        request: emr_20160408_models.ModifyFlowRequest,
    ) -> emr_20160408_models.ModifyFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_with_options_async(request, runtime)

    def modify_flow_category_with_options(
        self,
        request: emr_20160408_models.ModifyFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyFlowCategoryResponse().from_map(
            self.do_rpcrequest('ModifyFlowCategory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_flow_category_with_options_async(
        self,
        request: emr_20160408_models.ModifyFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowCategoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyFlowCategoryResponse().from_map(
            await self.do_rpcrequest_async('ModifyFlowCategory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_category(
        self,
        request: emr_20160408_models.ModifyFlowCategoryRequest,
    ) -> emr_20160408_models.ModifyFlowCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_category_with_options(request, runtime)

    async def modify_flow_category_async(
        self,
        request: emr_20160408_models.ModifyFlowCategoryRequest,
    ) -> emr_20160408_models.ModifyFlowCategoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_category_with_options_async(request, runtime)

    def modify_flow_for_web_with_options(
        self,
        request: emr_20160408_models.ModifyFlowForWebRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowForWebResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyFlowForWebResponse().from_map(
            self.do_rpcrequest('ModifyFlowForWeb', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_flow_for_web_with_options_async(
        self,
        request: emr_20160408_models.ModifyFlowForWebRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowForWebResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyFlowForWebResponse().from_map(
            await self.do_rpcrequest_async('ModifyFlowForWeb', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_for_web(
        self,
        request: emr_20160408_models.ModifyFlowForWebRequest,
    ) -> emr_20160408_models.ModifyFlowForWebResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_for_web_with_options(request, runtime)

    async def modify_flow_for_web_async(
        self,
        request: emr_20160408_models.ModifyFlowForWebRequest,
    ) -> emr_20160408_models.ModifyFlowForWebResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_for_web_with_options_async(request, runtime)

    def modify_flow_job_with_options(
        self,
        request: emr_20160408_models.ModifyFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyFlowJobResponse().from_map(
            self.do_rpcrequest('ModifyFlowJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_flow_job_with_options_async(
        self,
        request: emr_20160408_models.ModifyFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyFlowJobResponse().from_map(
            await self.do_rpcrequest_async('ModifyFlowJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_job(
        self,
        request: emr_20160408_models.ModifyFlowJobRequest,
    ) -> emr_20160408_models.ModifyFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_job_with_options(request, runtime)

    async def modify_flow_job_async(
        self,
        request: emr_20160408_models.ModifyFlowJobRequest,
    ) -> emr_20160408_models.ModifyFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_job_with_options_async(request, runtime)

    def modify_flow_project_with_options(
        self,
        request: emr_20160408_models.ModifyFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyFlowProjectResponse().from_map(
            self.do_rpcrequest('ModifyFlowProject', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_flow_project_with_options_async(
        self,
        request: emr_20160408_models.ModifyFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowProjectResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyFlowProjectResponse().from_map(
            await self.do_rpcrequest_async('ModifyFlowProject', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_project(
        self,
        request: emr_20160408_models.ModifyFlowProjectRequest,
    ) -> emr_20160408_models.ModifyFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_project_with_options(request, runtime)

    async def modify_flow_project_async(
        self,
        request: emr_20160408_models.ModifyFlowProjectRequest,
    ) -> emr_20160408_models.ModifyFlowProjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_project_with_options_async(request, runtime)

    def modify_flow_project_cluster_setting_with_options(
        self,
        request: emr_20160408_models.ModifyFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyFlowProjectClusterSettingResponse().from_map(
            self.do_rpcrequest('ModifyFlowProjectClusterSetting', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_flow_project_cluster_setting_with_options_async(
        self,
        request: emr_20160408_models.ModifyFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyFlowProjectClusterSettingResponse().from_map(
            await self.do_rpcrequest_async('ModifyFlowProjectClusterSetting', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow_project_cluster_setting(
        self,
        request: emr_20160408_models.ModifyFlowProjectClusterSettingRequest,
    ) -> emr_20160408_models.ModifyFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_project_cluster_setting_with_options(request, runtime)

    async def modify_flow_project_cluster_setting_async(
        self,
        request: emr_20160408_models.ModifyFlowProjectClusterSettingRequest,
    ) -> emr_20160408_models.ModifyFlowProjectClusterSettingResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_project_cluster_setting_with_options_async(request, runtime)

    def modify_job_with_options(
        self,
        request: emr_20160408_models.ModifyJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyJobResponse().from_map(
            self.do_rpcrequest('ModifyJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_job_with_options_async(
        self,
        request: emr_20160408_models.ModifyJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyJobResponse().from_map(
            await self.do_rpcrequest_async('ModifyJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_job(
        self,
        request: emr_20160408_models.ModifyJobRequest,
    ) -> emr_20160408_models.ModifyJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_job_with_options(request, runtime)

    async def modify_job_async(
        self,
        request: emr_20160408_models.ModifyJobRequest,
    ) -> emr_20160408_models.ModifyJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_job_with_options_async(request, runtime)

    def modify_resource_pool_with_options(
        self,
        request: emr_20160408_models.ModifyResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyResourcePoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyResourcePoolResponse().from_map(
            self.do_rpcrequest('ModifyResourcePool', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_resource_pool_with_options_async(
        self,
        request: emr_20160408_models.ModifyResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyResourcePoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyResourcePoolResponse().from_map(
            await self.do_rpcrequest_async('ModifyResourcePool', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_resource_pool(
        self,
        request: emr_20160408_models.ModifyResourcePoolRequest,
    ) -> emr_20160408_models.ModifyResourcePoolResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_pool_with_options(request, runtime)

    async def modify_resource_pool_async(
        self,
        request: emr_20160408_models.ModifyResourcePoolRequest,
    ) -> emr_20160408_models.ModifyResourcePoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_resource_pool_with_options_async(request, runtime)

    def modify_resource_pool_scheduler_type_with_options(
        self,
        request: emr_20160408_models.ModifyResourcePoolSchedulerTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyResourcePoolSchedulerTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyResourcePoolSchedulerTypeResponse().from_map(
            self.do_rpcrequest('ModifyResourcePoolSchedulerType', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_resource_pool_scheduler_type_with_options_async(
        self,
        request: emr_20160408_models.ModifyResourcePoolSchedulerTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyResourcePoolSchedulerTypeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyResourcePoolSchedulerTypeResponse().from_map(
            await self.do_rpcrequest_async('ModifyResourcePoolSchedulerType', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_resource_pool_scheduler_type(
        self,
        request: emr_20160408_models.ModifyResourcePoolSchedulerTypeRequest,
    ) -> emr_20160408_models.ModifyResourcePoolSchedulerTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_pool_scheduler_type_with_options(request, runtime)

    async def modify_resource_pool_scheduler_type_async(
        self,
        request: emr_20160408_models.ModifyResourcePoolSchedulerTypeRequest,
    ) -> emr_20160408_models.ModifyResourcePoolSchedulerTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_resource_pool_scheduler_type_with_options_async(request, runtime)

    def modify_resource_queue_with_options(
        self,
        request: emr_20160408_models.ModifyResourceQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyResourceQueueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyResourceQueueResponse().from_map(
            self.do_rpcrequest('ModifyResourceQueue', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_resource_queue_with_options_async(
        self,
        request: emr_20160408_models.ModifyResourceQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyResourceQueueResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyResourceQueueResponse().from_map(
            await self.do_rpcrequest_async('ModifyResourceQueue', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_resource_queue(
        self,
        request: emr_20160408_models.ModifyResourceQueueRequest,
    ) -> emr_20160408_models.ModifyResourceQueueResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_resource_queue_with_options(request, runtime)

    async def modify_resource_queue_async(
        self,
        request: emr_20160408_models.ModifyResourceQueueRequest,
    ) -> emr_20160408_models.ModifyResourceQueueResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_resource_queue_with_options_async(request, runtime)

    def modify_scaling_config_item_v2with_options(
        self,
        request: emr_20160408_models.ModifyScalingConfigItemV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyScalingConfigItemV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyScalingConfigItemV2Response().from_map(
            self.do_rpcrequest('ModifyScalingConfigItemV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_scaling_config_item_v2with_options_async(
        self,
        request: emr_20160408_models.ModifyScalingConfigItemV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyScalingConfigItemV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyScalingConfigItemV2Response().from_map(
            await self.do_rpcrequest_async('ModifyScalingConfigItemV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scaling_config_item_v2(
        self,
        request: emr_20160408_models.ModifyScalingConfigItemV2Request,
    ) -> emr_20160408_models.ModifyScalingConfigItemV2Response:
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_config_item_v2with_options(request, runtime)

    async def modify_scaling_config_item_v2_async(
        self,
        request: emr_20160408_models.ModifyScalingConfigItemV2Request,
    ) -> emr_20160408_models.ModifyScalingConfigItemV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.modify_scaling_config_item_v2with_options_async(request, runtime)

    def modify_scaling_group_v2with_options(
        self,
        request: emr_20160408_models.ModifyScalingGroupV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyScalingGroupV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyScalingGroupV2Response().from_map(
            self.do_rpcrequest('ModifyScalingGroupV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_scaling_group_v2with_options_async(
        self,
        request: emr_20160408_models.ModifyScalingGroupV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyScalingGroupV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyScalingGroupV2Response().from_map(
            await self.do_rpcrequest_async('ModifyScalingGroupV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scaling_group_v2(
        self,
        request: emr_20160408_models.ModifyScalingGroupV2Request,
    ) -> emr_20160408_models.ModifyScalingGroupV2Response:
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_group_v2with_options(request, runtime)

    async def modify_scaling_group_v2_async(
        self,
        request: emr_20160408_models.ModifyScalingGroupV2Request,
    ) -> emr_20160408_models.ModifyScalingGroupV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.modify_scaling_group_v2with_options_async(request, runtime)

    def modify_scaling_rule_with_options(
        self,
        request: emr_20160408_models.ModifyScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyScalingRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyScalingRuleResponse().from_map(
            self.do_rpcrequest('ModifyScalingRule', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_scaling_rule_with_options_async(
        self,
        request: emr_20160408_models.ModifyScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyScalingRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyScalingRuleResponse().from_map(
            await self.do_rpcrequest_async('ModifyScalingRule', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scaling_rule(
        self,
        request: emr_20160408_models.ModifyScalingRuleRequest,
    ) -> emr_20160408_models.ModifyScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_rule_with_options(request, runtime)

    async def modify_scaling_rule_async(
        self,
        request: emr_20160408_models.ModifyScalingRuleRequest,
    ) -> emr_20160408_models.ModifyScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_scaling_rule_with_options_async(request, runtime)

    def modify_scaling_task_group_with_options(
        self,
        request: emr_20160408_models.ModifyScalingTaskGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyScalingTaskGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyScalingTaskGroupResponse().from_map(
            self.do_rpcrequest('ModifyScalingTaskGroup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_scaling_task_group_with_options_async(
        self,
        request: emr_20160408_models.ModifyScalingTaskGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyScalingTaskGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ModifyScalingTaskGroupResponse().from_map(
            await self.do_rpcrequest_async('ModifyScalingTaskGroup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_scaling_task_group(
        self,
        request: emr_20160408_models.ModifyScalingTaskGroupRequest,
    ) -> emr_20160408_models.ModifyScalingTaskGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_scaling_task_group_with_options(request, runtime)

    async def modify_scaling_task_group_async(
        self,
        request: emr_20160408_models.ModifyScalingTaskGroupRequest,
    ) -> emr_20160408_models.ModifyScalingTaskGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_scaling_task_group_with_options_async(request, runtime)

    def query_alarm_history_with_options(
        self,
        request: emr_20160408_models.QueryAlarmHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.QueryAlarmHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.QueryAlarmHistoryResponse().from_map(
            self.do_rpcrequest('QueryAlarmHistory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_alarm_history_with_options_async(
        self,
        request: emr_20160408_models.QueryAlarmHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.QueryAlarmHistoryResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.QueryAlarmHistoryResponse().from_map(
            await self.do_rpcrequest_async('QueryAlarmHistory', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_alarm_history(
        self,
        request: emr_20160408_models.QueryAlarmHistoryRequest,
    ) -> emr_20160408_models.QueryAlarmHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_alarm_history_with_options(request, runtime)

    async def query_alarm_history_async(
        self,
        request: emr_20160408_models.QueryAlarmHistoryRequest,
    ) -> emr_20160408_models.QueryAlarmHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_alarm_history_with_options_async(request, runtime)

    def query_entity_with_options(
        self,
        request: emr_20160408_models.QueryEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.QueryEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.QueryEntityResponse().from_map(
            self.do_rpcrequest('QueryEntity', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_entity_with_options_async(
        self,
        request: emr_20160408_models.QueryEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.QueryEntityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.QueryEntityResponse().from_map(
            await self.do_rpcrequest_async('QueryEntity', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_entity(
        self,
        request: emr_20160408_models.QueryEntityRequest,
    ) -> emr_20160408_models.QueryEntityResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_entity_with_options(request, runtime)

    async def query_entity_async(
        self,
        request: emr_20160408_models.QueryEntityRequest,
    ) -> emr_20160408_models.QueryEntityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_entity_with_options_async(request, runtime)

    def query_table_data_with_options(
        self,
        request: emr_20160408_models.QueryTableDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.QueryTableDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.QueryTableDataResponse().from_map(
            self.do_rpcrequest('QueryTableData', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_table_data_with_options_async(
        self,
        request: emr_20160408_models.QueryTableDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.QueryTableDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.QueryTableDataResponse().from_map(
            await self.do_rpcrequest_async('QueryTableData', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_table_data(
        self,
        request: emr_20160408_models.QueryTableDataRequest,
    ) -> emr_20160408_models.QueryTableDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_table_data_with_options(request, runtime)

    async def query_table_data_async(
        self,
        request: emr_20160408_models.QueryTableDataRequest,
    ) -> emr_20160408_models.QueryTableDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_table_data_with_options_async(request, runtime)

    def query_tag_with_options(
        self,
        request: emr_20160408_models.QueryTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.QueryTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.QueryTagResponse().from_map(
            self.do_rpcrequest('QueryTag', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_tag_with_options_async(
        self,
        request: emr_20160408_models.QueryTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.QueryTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.QueryTagResponse().from_map(
            await self.do_rpcrequest_async('QueryTag', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_tag(
        self,
        request: emr_20160408_models.QueryTagRequest,
    ) -> emr_20160408_models.QueryTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_tag_with_options(request, runtime)

    async def query_tag_async(
        self,
        request: emr_20160408_models.QueryTagRequest,
    ) -> emr_20160408_models.QueryTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_tag_with_options_async(request, runtime)

    def query_trend_data_with_options(
        self,
        request: emr_20160408_models.QueryTrendDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.QueryTrendDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.QueryTrendDataResponse().from_map(
            self.do_rpcrequest('QueryTrendData', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def query_trend_data_with_options_async(
        self,
        request: emr_20160408_models.QueryTrendDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.QueryTrendDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.QueryTrendDataResponse().from_map(
            await self.do_rpcrequest_async('QueryTrendData', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_trend_data(
        self,
        request: emr_20160408_models.QueryTrendDataRequest,
    ) -> emr_20160408_models.QueryTrendDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_trend_data_with_options(request, runtime)

    async def query_trend_data_async(
        self,
        request: emr_20160408_models.QueryTrendDataRequest,
    ) -> emr_20160408_models.QueryTrendDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_trend_data_with_options_async(request, runtime)

    def refresh_cluster_resource_pool_with_options(
        self,
        request: emr_20160408_models.RefreshClusterResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RefreshClusterResourcePoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RefreshClusterResourcePoolResponse().from_map(
            self.do_rpcrequest('RefreshClusterResourcePool', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def refresh_cluster_resource_pool_with_options_async(
        self,
        request: emr_20160408_models.RefreshClusterResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RefreshClusterResourcePoolResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RefreshClusterResourcePoolResponse().from_map(
            await self.do_rpcrequest_async('RefreshClusterResourcePool', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def refresh_cluster_resource_pool(
        self,
        request: emr_20160408_models.RefreshClusterResourcePoolRequest,
    ) -> emr_20160408_models.RefreshClusterResourcePoolResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_cluster_resource_pool_with_options(request, runtime)

    async def refresh_cluster_resource_pool_async(
        self,
        request: emr_20160408_models.RefreshClusterResourcePoolRequest,
    ) -> emr_20160408_models.RefreshClusterResourcePoolResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_cluster_resource_pool_with_options_async(request, runtime)

    def release_cluster_with_options(
        self,
        request: emr_20160408_models.ReleaseClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ReleaseClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ReleaseClusterResponse().from_map(
            self.do_rpcrequest('ReleaseCluster', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_cluster_with_options_async(
        self,
        request: emr_20160408_models.ReleaseClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ReleaseClusterResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ReleaseClusterResponse().from_map(
            await self.do_rpcrequest_async('ReleaseCluster', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_cluster(
        self,
        request: emr_20160408_models.ReleaseClusterRequest,
    ) -> emr_20160408_models.ReleaseClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_cluster_with_options(request, runtime)

    async def release_cluster_async(
        self,
        request: emr_20160408_models.ReleaseClusterRequest,
    ) -> emr_20160408_models.ReleaseClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_cluster_with_options_async(request, runtime)

    def release_cluster_by_template_tag_for_internal_with_options(
        self,
        request: emr_20160408_models.ReleaseClusterByTemplateTagForInternalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ReleaseClusterByTemplateTagForInternalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ReleaseClusterByTemplateTagForInternalResponse().from_map(
            self.do_rpcrequest('ReleaseClusterByTemplateTagForInternal', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_cluster_by_template_tag_for_internal_with_options_async(
        self,
        request: emr_20160408_models.ReleaseClusterByTemplateTagForInternalRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ReleaseClusterByTemplateTagForInternalResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ReleaseClusterByTemplateTagForInternalResponse().from_map(
            await self.do_rpcrequest_async('ReleaseClusterByTemplateTagForInternal', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_cluster_by_template_tag_for_internal(
        self,
        request: emr_20160408_models.ReleaseClusterByTemplateTagForInternalRequest,
    ) -> emr_20160408_models.ReleaseClusterByTemplateTagForInternalResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_cluster_by_template_tag_for_internal_with_options(request, runtime)

    async def release_cluster_by_template_tag_for_internal_async(
        self,
        request: emr_20160408_models.ReleaseClusterByTemplateTagForInternalRequest,
    ) -> emr_20160408_models.ReleaseClusterByTemplateTagForInternalResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_cluster_by_template_tag_for_internal_with_options_async(request, runtime)

    def release_cluster_host_group_with_options(
        self,
        request: emr_20160408_models.ReleaseClusterHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ReleaseClusterHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ReleaseClusterHostGroupResponse().from_map(
            self.do_rpcrequest('ReleaseClusterHostGroup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def release_cluster_host_group_with_options_async(
        self,
        request: emr_20160408_models.ReleaseClusterHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ReleaseClusterHostGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ReleaseClusterHostGroupResponse().from_map(
            await self.do_rpcrequest_async('ReleaseClusterHostGroup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_cluster_host_group(
        self,
        request: emr_20160408_models.ReleaseClusterHostGroupRequest,
    ) -> emr_20160408_models.ReleaseClusterHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_cluster_host_group_with_options(request, runtime)

    async def release_cluster_host_group_async(
        self,
        request: emr_20160408_models.ReleaseClusterHostGroupRequest,
    ) -> emr_20160408_models.ReleaseClusterHostGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_cluster_host_group_with_options_async(request, runtime)

    def remove_scaling_config_item_v2with_options(
        self,
        request: emr_20160408_models.RemoveScalingConfigItemV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RemoveScalingConfigItemV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RemoveScalingConfigItemV2Response().from_map(
            self.do_rpcrequest('RemoveScalingConfigItemV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_scaling_config_item_v2with_options_async(
        self,
        request: emr_20160408_models.RemoveScalingConfigItemV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RemoveScalingConfigItemV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RemoveScalingConfigItemV2Response().from_map(
            await self.do_rpcrequest_async('RemoveScalingConfigItemV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_scaling_config_item_v2(
        self,
        request: emr_20160408_models.RemoveScalingConfigItemV2Request,
    ) -> emr_20160408_models.RemoveScalingConfigItemV2Response:
        runtime = util_models.RuntimeOptions()
        return self.remove_scaling_config_item_v2with_options(request, runtime)

    async def remove_scaling_config_item_v2_async(
        self,
        request: emr_20160408_models.RemoveScalingConfigItemV2Request,
    ) -> emr_20160408_models.RemoveScalingConfigItemV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.remove_scaling_config_item_v2with_options_async(request, runtime)

    def rerun_flow_with_options(
        self,
        request: emr_20160408_models.RerunFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RerunFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RerunFlowResponse().from_map(
            self.do_rpcrequest('RerunFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def rerun_flow_with_options_async(
        self,
        request: emr_20160408_models.RerunFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RerunFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RerunFlowResponse().from_map(
            await self.do_rpcrequest_async('RerunFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def rerun_flow(
        self,
        request: emr_20160408_models.RerunFlowRequest,
    ) -> emr_20160408_models.RerunFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.rerun_flow_with_options(request, runtime)

    async def rerun_flow_async(
        self,
        request: emr_20160408_models.RerunFlowRequest,
    ) -> emr_20160408_models.RerunFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rerun_flow_with_options_async(request, runtime)

    def resize_cluster_v2with_options(
        self,
        request: emr_20160408_models.ResizeClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ResizeClusterV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ResizeClusterV2Response().from_map(
            self.do_rpcrequest('ResizeClusterV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resize_cluster_v2with_options_async(
        self,
        request: emr_20160408_models.ResizeClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ResizeClusterV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ResizeClusterV2Response().from_map(
            await self.do_rpcrequest_async('ResizeClusterV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resize_cluster_v2(
        self,
        request: emr_20160408_models.ResizeClusterV2Request,
    ) -> emr_20160408_models.ResizeClusterV2Response:
        runtime = util_models.RuntimeOptions()
        return self.resize_cluster_v2with_options(request, runtime)

    async def resize_cluster_v2_async(
        self,
        request: emr_20160408_models.ResizeClusterV2Request,
    ) -> emr_20160408_models.ResizeClusterV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.resize_cluster_v2with_options_async(request, runtime)

    def restore_backup_with_options(
        self,
        request: emr_20160408_models.RestoreBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RestoreBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RestoreBackupResponse().from_map(
            self.do_rpcrequest('RestoreBackup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restore_backup_with_options_async(
        self,
        request: emr_20160408_models.RestoreBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RestoreBackupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RestoreBackupResponse().from_map(
            await self.do_rpcrequest_async('RestoreBackup', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restore_backup(
        self,
        request: emr_20160408_models.RestoreBackupRequest,
    ) -> emr_20160408_models.RestoreBackupResponse:
        runtime = util_models.RuntimeOptions()
        return self.restore_backup_with_options(request, runtime)

    async def restore_backup_async(
        self,
        request: emr_20160408_models.RestoreBackupRequest,
    ) -> emr_20160408_models.RestoreBackupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restore_backup_with_options_async(request, runtime)

    def restore_flow_entity_snapshot_with_options(
        self,
        request: emr_20160408_models.RestoreFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RestoreFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RestoreFlowEntitySnapshotResponse().from_map(
            self.do_rpcrequest('RestoreFlowEntitySnapshot', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def restore_flow_entity_snapshot_with_options_async(
        self,
        request: emr_20160408_models.RestoreFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RestoreFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RestoreFlowEntitySnapshotResponse().from_map(
            await self.do_rpcrequest_async('RestoreFlowEntitySnapshot', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restore_flow_entity_snapshot(
        self,
        request: emr_20160408_models.RestoreFlowEntitySnapshotRequest,
    ) -> emr_20160408_models.RestoreFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return self.restore_flow_entity_snapshot_with_options(request, runtime)

    async def restore_flow_entity_snapshot_async(
        self,
        request: emr_20160408_models.RestoreFlowEntitySnapshotRequest,
    ) -> emr_20160408_models.RestoreFlowEntitySnapshotResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restore_flow_entity_snapshot_with_options_async(request, runtime)

    def resume_execution_plan_scheduler_with_options(
        self,
        request: emr_20160408_models.ResumeExecutionPlanSchedulerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ResumeExecutionPlanSchedulerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ResumeExecutionPlanSchedulerResponse().from_map(
            self.do_rpcrequest('ResumeExecutionPlanScheduler', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resume_execution_plan_scheduler_with_options_async(
        self,
        request: emr_20160408_models.ResumeExecutionPlanSchedulerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ResumeExecutionPlanSchedulerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ResumeExecutionPlanSchedulerResponse().from_map(
            await self.do_rpcrequest_async('ResumeExecutionPlanScheduler', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_execution_plan_scheduler(
        self,
        request: emr_20160408_models.ResumeExecutionPlanSchedulerRequest,
    ) -> emr_20160408_models.ResumeExecutionPlanSchedulerResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_execution_plan_scheduler_with_options(request, runtime)

    async def resume_execution_plan_scheduler_async(
        self,
        request: emr_20160408_models.ResumeExecutionPlanSchedulerRequest,
    ) -> emr_20160408_models.ResumeExecutionPlanSchedulerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_execution_plan_scheduler_with_options_async(request, runtime)

    def resume_flow_with_options(
        self,
        request: emr_20160408_models.ResumeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ResumeFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ResumeFlowResponse().from_map(
            self.do_rpcrequest('ResumeFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def resume_flow_with_options_async(
        self,
        request: emr_20160408_models.ResumeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ResumeFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.ResumeFlowResponse().from_map(
            await self.do_rpcrequest_async('ResumeFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_flow(
        self,
        request: emr_20160408_models.ResumeFlowRequest,
    ) -> emr_20160408_models.ResumeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_flow_with_options(request, runtime)

    async def resume_flow_async(
        self,
        request: emr_20160408_models.ResumeFlowRequest,
    ) -> emr_20160408_models.ResumeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_flow_with_options_async(request, runtime)

    def retry_operation_with_options(
        self,
        request: emr_20160408_models.RetryOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RetryOperationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RetryOperationResponse().from_map(
            self.do_rpcrequest('RetryOperation', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def retry_operation_with_options_async(
        self,
        request: emr_20160408_models.RetryOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RetryOperationResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RetryOperationResponse().from_map(
            await self.do_rpcrequest_async('RetryOperation', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def retry_operation(
        self,
        request: emr_20160408_models.RetryOperationRequest,
    ) -> emr_20160408_models.RetryOperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_operation_with_options(request, runtime)

    async def retry_operation_async(
        self,
        request: emr_20160408_models.RetryOperationRequest,
    ) -> emr_20160408_models.RetryOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_operation_with_options_async(request, runtime)

    def run_cluster_service_action_with_options(
        self,
        request: emr_20160408_models.RunClusterServiceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RunClusterServiceActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RunClusterServiceActionResponse().from_map(
            self.do_rpcrequest('RunClusterServiceAction', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_cluster_service_action_with_options_async(
        self,
        request: emr_20160408_models.RunClusterServiceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RunClusterServiceActionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RunClusterServiceActionResponse().from_map(
            await self.do_rpcrequest_async('RunClusterServiceAction', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_cluster_service_action(
        self,
        request: emr_20160408_models.RunClusterServiceActionRequest,
    ) -> emr_20160408_models.RunClusterServiceActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_cluster_service_action_with_options(request, runtime)

    async def run_cluster_service_action_async(
        self,
        request: emr_20160408_models.RunClusterServiceActionRequest,
    ) -> emr_20160408_models.RunClusterServiceActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_cluster_service_action_with_options_async(request, runtime)

    def run_execution_plan_with_options(
        self,
        tmp_req: emr_20160408_models.RunExecutionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RunExecutionPlanResponse:
        UtilClient.validate_model(tmp_req)
        request = emr_20160408_models.RunExecutionPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.arguments):
            request.arguments_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.arguments, 'Arguments', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RunExecutionPlanResponse().from_map(
            self.do_rpcrequest('RunExecutionPlan', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_execution_plan_with_options_async(
        self,
        tmp_req: emr_20160408_models.RunExecutionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RunExecutionPlanResponse:
        UtilClient.validate_model(tmp_req)
        request = emr_20160408_models.RunExecutionPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.arguments):
            request.arguments_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.arguments, 'Arguments', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RunExecutionPlanResponse().from_map(
            await self.do_rpcrequest_async('RunExecutionPlan', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_execution_plan(
        self,
        request: emr_20160408_models.RunExecutionPlanRequest,
    ) -> emr_20160408_models.RunExecutionPlanResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_execution_plan_with_options(request, runtime)

    async def run_execution_plan_async(
        self,
        request: emr_20160408_models.RunExecutionPlanRequest,
    ) -> emr_20160408_models.RunExecutionPlanResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_execution_plan_with_options_async(request, runtime)

    def run_scaling_action_v2with_options(
        self,
        request: emr_20160408_models.RunScalingActionV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RunScalingActionV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RunScalingActionV2Response().from_map(
            self.do_rpcrequest('RunScalingActionV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def run_scaling_action_v2with_options_async(
        self,
        request: emr_20160408_models.RunScalingActionV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RunScalingActionV2Response:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.RunScalingActionV2Response().from_map(
            await self.do_rpcrequest_async('RunScalingActionV2', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_scaling_action_v2(
        self,
        request: emr_20160408_models.RunScalingActionV2Request,
    ) -> emr_20160408_models.RunScalingActionV2Response:
        runtime = util_models.RuntimeOptions()
        return self.run_scaling_action_v2with_options(request, runtime)

    async def run_scaling_action_v2_async(
        self,
        request: emr_20160408_models.RunScalingActionV2Request,
    ) -> emr_20160408_models.RunScalingActionV2Response:
        runtime = util_models.RuntimeOptions()
        return await self.run_scaling_action_v2with_options_async(request, runtime)

    def search_log_with_options(
        self,
        request: emr_20160408_models.SearchLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.SearchLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.SearchLogResponse().from_map(
            self.do_rpcrequest('SearchLog', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def search_log_with_options_async(
        self,
        request: emr_20160408_models.SearchLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.SearchLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.SearchLogResponse().from_map(
            await self.do_rpcrequest_async('SearchLog', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def search_log(
        self,
        request: emr_20160408_models.SearchLogRequest,
    ) -> emr_20160408_models.SearchLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.search_log_with_options(request, runtime)

    async def search_log_async(
        self,
        request: emr_20160408_models.SearchLogRequest,
    ) -> emr_20160408_models.SearchLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.search_log_with_options_async(request, runtime)

    def start_flow_with_options(
        self,
        request: emr_20160408_models.StartFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.StartFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.StartFlowResponse().from_map(
            self.do_rpcrequest('StartFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def start_flow_with_options_async(
        self,
        request: emr_20160408_models.StartFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.StartFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.StartFlowResponse().from_map(
            await self.do_rpcrequest_async('StartFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_flow(
        self,
        request: emr_20160408_models.StartFlowRequest,
    ) -> emr_20160408_models.StartFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_flow_with_options(request, runtime)

    async def start_flow_async(
        self,
        request: emr_20160408_models.StartFlowRequest,
    ) -> emr_20160408_models.StartFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_flow_with_options_async(request, runtime)

    def submit_flow_with_options(
        self,
        request: emr_20160408_models.SubmitFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.SubmitFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.SubmitFlowResponse().from_map(
            self.do_rpcrequest('SubmitFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_flow_with_options_async(
        self,
        request: emr_20160408_models.SubmitFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.SubmitFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.SubmitFlowResponse().from_map(
            await self.do_rpcrequest_async('SubmitFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_flow(
        self,
        request: emr_20160408_models.SubmitFlowRequest,
    ) -> emr_20160408_models.SubmitFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_flow_with_options(request, runtime)

    async def submit_flow_async(
        self,
        request: emr_20160408_models.SubmitFlowRequest,
    ) -> emr_20160408_models.SubmitFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_flow_with_options_async(request, runtime)

    def submit_flow_job_with_options(
        self,
        request: emr_20160408_models.SubmitFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.SubmitFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.SubmitFlowJobResponse().from_map(
            self.do_rpcrequest('SubmitFlowJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def submit_flow_job_with_options_async(
        self,
        request: emr_20160408_models.SubmitFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.SubmitFlowJobResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.SubmitFlowJobResponse().from_map(
            await self.do_rpcrequest_async('SubmitFlowJob', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_flow_job(
        self,
        request: emr_20160408_models.SubmitFlowJobRequest,
    ) -> emr_20160408_models.SubmitFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.submit_flow_job_with_options(request, runtime)

    async def submit_flow_job_async(
        self,
        request: emr_20160408_models.SubmitFlowJobRequest,
    ) -> emr_20160408_models.SubmitFlowJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.submit_flow_job_with_options_async(request, runtime)

    def suspend_execution_plan_scheduler_with_options(
        self,
        request: emr_20160408_models.SuspendExecutionPlanSchedulerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.SuspendExecutionPlanSchedulerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.SuspendExecutionPlanSchedulerResponse().from_map(
            self.do_rpcrequest('SuspendExecutionPlanScheduler', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def suspend_execution_plan_scheduler_with_options_async(
        self,
        request: emr_20160408_models.SuspendExecutionPlanSchedulerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.SuspendExecutionPlanSchedulerResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.SuspendExecutionPlanSchedulerResponse().from_map(
            await self.do_rpcrequest_async('SuspendExecutionPlanScheduler', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_execution_plan_scheduler(
        self,
        request: emr_20160408_models.SuspendExecutionPlanSchedulerRequest,
    ) -> emr_20160408_models.SuspendExecutionPlanSchedulerResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_execution_plan_scheduler_with_options(request, runtime)

    async def suspend_execution_plan_scheduler_async(
        self,
        request: emr_20160408_models.SuspendExecutionPlanSchedulerRequest,
    ) -> emr_20160408_models.SuspendExecutionPlanSchedulerResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_execution_plan_scheduler_with_options_async(request, runtime)

    def suspend_flow_with_options(
        self,
        request: emr_20160408_models.SuspendFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.SuspendFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.SuspendFlowResponse().from_map(
            self.do_rpcrequest('SuspendFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def suspend_flow_with_options_async(
        self,
        request: emr_20160408_models.SuspendFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.SuspendFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.SuspendFlowResponse().from_map(
            await self.do_rpcrequest_async('SuspendFlow', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def suspend_flow(
        self,
        request: emr_20160408_models.SuspendFlowRequest,
    ) -> emr_20160408_models.SuspendFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_flow_with_options(request, runtime)

    async def suspend_flow_async(
        self,
        request: emr_20160408_models.SuspendFlowRequest,
    ) -> emr_20160408_models.SuspendFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_flow_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: emr_20160408_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: emr_20160408_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.TagResourcesResponse().from_map(
            await self.do_rpcrequest_async('TagResources', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(
        self,
        request: emr_20160408_models.TagResourcesRequest,
    ) -> emr_20160408_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: emr_20160408_models.TagResourcesRequest,
    ) -> emr_20160408_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def tag_resources_system_tags_with_options(
        self,
        request: emr_20160408_models.TagResourcesSystemTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.TagResourcesSystemTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.TagResourcesSystemTagsResponse().from_map(
            self.do_rpcrequest('TagResourcesSystemTags', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def tag_resources_system_tags_with_options_async(
        self,
        request: emr_20160408_models.TagResourcesSystemTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.TagResourcesSystemTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.TagResourcesSystemTagsResponse().from_map(
            await self.do_rpcrequest_async('TagResourcesSystemTags', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources_system_tags(
        self,
        request: emr_20160408_models.TagResourcesSystemTagsRequest,
    ) -> emr_20160408_models.TagResourcesSystemTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_system_tags_with_options(request, runtime)

    async def tag_resources_system_tags_async(
        self,
        request: emr_20160408_models.TagResourcesSystemTagsRequest,
    ) -> emr_20160408_models.TagResourcesSystemTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_system_tags_with_options_async(request, runtime)

    def uninstall_libraries_with_options(
        self,
        request: emr_20160408_models.UninstallLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UninstallLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.UninstallLibrariesResponse().from_map(
            self.do_rpcrequest('UninstallLibraries', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def uninstall_libraries_with_options_async(
        self,
        request: emr_20160408_models.UninstallLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UninstallLibrariesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.UninstallLibrariesResponse().from_map(
            await self.do_rpcrequest_async('UninstallLibraries', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def uninstall_libraries(
        self,
        request: emr_20160408_models.UninstallLibrariesRequest,
    ) -> emr_20160408_models.UninstallLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return self.uninstall_libraries_with_options(request, runtime)

    async def uninstall_libraries_async(
        self,
        request: emr_20160408_models.UninstallLibrariesRequest,
    ) -> emr_20160408_models.UninstallLibrariesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.uninstall_libraries_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: emr_20160408_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: emr_20160408_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.UntagResourcesResponse().from_map(
            await self.do_rpcrequest_async('UntagResources', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(
        self,
        request: emr_20160408_models.UntagResourcesRequest,
    ) -> emr_20160408_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: emr_20160408_models.UntagResourcesRequest,
    ) -> emr_20160408_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def untag_resources_system_tags_with_options(
        self,
        request: emr_20160408_models.UntagResourcesSystemTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UntagResourcesSystemTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.UntagResourcesSystemTagsResponse().from_map(
            self.do_rpcrequest('UntagResourcesSystemTags', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def untag_resources_system_tags_with_options_async(
        self,
        request: emr_20160408_models.UntagResourcesSystemTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UntagResourcesSystemTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.UntagResourcesSystemTagsResponse().from_map(
            await self.do_rpcrequest_async('UntagResourcesSystemTags', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources_system_tags(
        self,
        request: emr_20160408_models.UntagResourcesSystemTagsRequest,
    ) -> emr_20160408_models.UntagResourcesSystemTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_system_tags_with_options(request, runtime)

    async def untag_resources_system_tags_async(
        self,
        request: emr_20160408_models.UntagResourcesSystemTagsRequest,
    ) -> emr_20160408_models.UntagResourcesSystemTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_system_tags_with_options_async(request, runtime)

    def update_data_source_with_options(
        self,
        request: emr_20160408_models.UpdateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UpdateDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.UpdateDataSourceResponse().from_map(
            self.do_rpcrequest('UpdateDataSource', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_data_source_with_options_async(
        self,
        request: emr_20160408_models.UpdateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UpdateDataSourceResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.UpdateDataSourceResponse().from_map(
            await self.do_rpcrequest_async('UpdateDataSource', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_data_source(
        self,
        request: emr_20160408_models.UpdateDataSourceRequest,
    ) -> emr_20160408_models.UpdateDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_data_source_with_options(request, runtime)

    async def update_data_source_async(
        self,
        request: emr_20160408_models.UpdateDataSourceRequest,
    ) -> emr_20160408_models.UpdateDataSourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_data_source_with_options_async(request, runtime)

    def update_library_install_task_status_with_options(
        self,
        request: emr_20160408_models.UpdateLibraryInstallTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UpdateLibraryInstallTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.UpdateLibraryInstallTaskStatusResponse().from_map(
            self.do_rpcrequest('UpdateLibraryInstallTaskStatus', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_library_install_task_status_with_options_async(
        self,
        request: emr_20160408_models.UpdateLibraryInstallTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UpdateLibraryInstallTaskStatusResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.UpdateLibraryInstallTaskStatusResponse().from_map(
            await self.do_rpcrequest_async('UpdateLibraryInstallTaskStatus', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_library_install_task_status(
        self,
        request: emr_20160408_models.UpdateLibraryInstallTaskStatusRequest,
    ) -> emr_20160408_models.UpdateLibraryInstallTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_library_install_task_status_with_options(request, runtime)

    async def update_library_install_task_status_async(
        self,
        request: emr_20160408_models.UpdateLibraryInstallTaskStatusRequest,
    ) -> emr_20160408_models.UpdateLibraryInstallTaskStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_library_install_task_status_with_options_async(request, runtime)

    def update_tag_with_options(
        self,
        request: emr_20160408_models.UpdateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UpdateTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.UpdateTagResponse().from_map(
            self.do_rpcrequest('UpdateTag', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_tag_with_options_async(
        self,
        request: emr_20160408_models.UpdateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UpdateTagResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.UpdateTagResponse().from_map(
            await self.do_rpcrequest_async('UpdateTag', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_tag(
        self,
        request: emr_20160408_models.UpdateTagRequest,
    ) -> emr_20160408_models.UpdateTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_tag_with_options(request, runtime)

    async def update_tag_async(
        self,
        request: emr_20160408_models.UpdateTagRequest,
    ) -> emr_20160408_models.UpdateTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_tag_with_options_async(request, runtime)

    def update_user_with_options(
        self,
        request: emr_20160408_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.UpdateUserResponse().from_map(
            self.do_rpcrequest('UpdateUser', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: emr_20160408_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return emr_20160408_models.UpdateUserResponse().from_map(
            await self.do_rpcrequest_async('UpdateUser', '2016-04-08', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_user(
        self,
        request: emr_20160408_models.UpdateUserRequest,
    ) -> emr_20160408_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    async def update_user_async(
        self,
        request: emr_20160408_models.UpdateUserRequest,
    ) -> emr_20160408_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_user_with_options_async(request, runtime)
