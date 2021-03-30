# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Comment'] = request.comment
        query['ClusterId'] = request.cluster_id
        query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddClusterService',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.AddClusterServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_cluster_service_with_options_async(
        self,
        request: emr_20160408_models.AddClusterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.AddClusterServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Comment'] = request.comment
        query['ClusterId'] = request.cluster_id
        query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddClusterService',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.AddClusterServiceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['ConfigItemType'] = request.config_item_type
        query['ConfigItemInformation'] = request.config_item_information
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddScalingConfigItemV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.AddScalingConfigItemV2Response(),
            self.call_api(params, req, runtime)
        )

    async def add_scaling_config_item_v2with_options_async(
        self,
        request: emr_20160408_models.AddScalingConfigItemV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.AddScalingConfigItemV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['ConfigItemType'] = request.config_item_type
        query['ConfigItemInformation'] = request.config_item_information
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddScalingConfigItemV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.AddScalingConfigItemV2Response(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['BizType'] = request.biz_type
        query['BizContent'] = request.biz_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AuthorizeSecurityGroup',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.AuthorizeSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_security_group_with_options_async(
        self,
        request: emr_20160408_models.AuthorizeSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.AuthorizeSecurityGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['BizType'] = request.biz_type
        query['BizContent'] = request.biz_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AuthorizeSecurityGroup',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.AuthorizeSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelOrder',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CancelOrderResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_order_with_options_async(
        self,
        request: emr_20160408_models.CancelOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CancelOrderResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CancelOrder',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CancelOrderResponse(),
            await self.call_api_async(params, req, runtime)
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

    def clone_flow_with_options(
        self,
        request: emr_20160408_models.CloneFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CloneFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CloneFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CloneFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_flow_with_options_async(
        self,
        request: emr_20160408_models.CloneFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CloneFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CloneFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CloneFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CloneFlowJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CloneFlowJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_flow_job_with_options_async(
        self,
        request: emr_20160408_models.CloneFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CloneFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CloneFlowJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CloneFlowJobResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_backup_with_options(
        self,
        request: emr_20160408_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['BackupPlanId'] = request.backup_plan_id
        query['MetadataType'] = request.metadata_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBackup',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_with_options_async(
        self,
        request: emr_20160408_models.CreateBackupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateBackupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['BackupPlanId'] = request.backup_plan_id
        query['MetadataType'] = request.metadata_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBackup',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateBackupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Name'] = request.name
        query['Description'] = request.description
        query['ClusterId'] = request.cluster_id
        query['RootPath'] = request.root_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBackupPlan',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_plan_with_options_async(
        self,
        request: emr_20160408_models.CreateBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateBackupPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Name'] = request.name
        query['Description'] = request.description
        query['ClusterId'] = request.cluster_id
        query['RootPath'] = request.root_path
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateBackupPlan',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['BootstrapAction'] = request.bootstrap_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateClusterBootstrapAction',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateClusterBootstrapActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_bootstrap_action_with_options_async(
        self,
        request: emr_20160408_models.CreateClusterBootstrapActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateClusterBootstrapActionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['BootstrapAction'] = request.bootstrap_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateClusterBootstrapAction',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateClusterBootstrapActionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateName'] = request.template_name
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['LogPath'] = request.log_path
        query['SecurityGroupId'] = request.security_group_id
        query['IsOpenPublicIp'] = request.is_open_public_ip
        query['SecurityGroupName'] = request.security_group_name
        query['Period'] = request.period
        query['AutoRenew'] = request.auto_renew
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['NetType'] = request.net_type
        query['UserDefinedEmrEcsRole'] = request.user_defined_emr_ecs_role
        query['EmrVer'] = request.emr_ver
        query['ClusterType'] = request.cluster_type
        query['HighAvailabilityEnable'] = request.high_availability_enable
        query['UseLocalMetaDb'] = request.use_local_meta_db
        query['IoOptimized'] = request.io_optimized
        query['SshEnable'] = request.ssh_enable
        query['InstanceGeneration'] = request.instance_generation
        query['MasterPwd'] = request.master_pwd
        query['KeyPairName'] = request.key_pair_name
        query['MetaStoreType'] = request.meta_store_type
        query['MetaStoreConf'] = request.meta_store_conf
        query['Configurations'] = request.configurations
        query['EasEnable'] = request.eas_enable
        query['DepositType'] = request.deposit_type
        query['MachineType'] = request.machine_type
        query['UseCustomHiveMetaDb'] = request.use_custom_hive_meta_db
        query['InitCustomHiveMetaDb'] = request.init_custom_hive_meta_db
        query['ResourceGroupId'] = request.resource_group_id
        query['OptionSoftWareList'] = request.option_soft_ware_list
        query['HostGroup'] = request.host_group
        query['BootstrapAction'] = request.bootstrap_action
        query['Config'] = request.config
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateClusterTemplate',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateClusterTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_template_with_options_async(
        self,
        request: emr_20160408_models.CreateClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateClusterTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateName'] = request.template_name
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['LogPath'] = request.log_path
        query['SecurityGroupId'] = request.security_group_id
        query['IsOpenPublicIp'] = request.is_open_public_ip
        query['SecurityGroupName'] = request.security_group_name
        query['Period'] = request.period
        query['AutoRenew'] = request.auto_renew
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['NetType'] = request.net_type
        query['UserDefinedEmrEcsRole'] = request.user_defined_emr_ecs_role
        query['EmrVer'] = request.emr_ver
        query['ClusterType'] = request.cluster_type
        query['HighAvailabilityEnable'] = request.high_availability_enable
        query['UseLocalMetaDb'] = request.use_local_meta_db
        query['IoOptimized'] = request.io_optimized
        query['SshEnable'] = request.ssh_enable
        query['InstanceGeneration'] = request.instance_generation
        query['MasterPwd'] = request.master_pwd
        query['KeyPairName'] = request.key_pair_name
        query['MetaStoreType'] = request.meta_store_type
        query['MetaStoreConf'] = request.meta_store_conf
        query['Configurations'] = request.configurations
        query['EasEnable'] = request.eas_enable
        query['DepositType'] = request.deposit_type
        query['MachineType'] = request.machine_type
        query['UseCustomHiveMetaDb'] = request.use_custom_hive_meta_db
        query['InitCustomHiveMetaDb'] = request.init_custom_hive_meta_db
        query['ResourceGroupId'] = request.resource_group_id
        query['OptionSoftWareList'] = request.option_soft_ware_list
        query['HostGroup'] = request.host_group
        query['BootstrapAction'] = request.bootstrap_action
        query['Config'] = request.config
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateClusterTemplate',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateClusterTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Name'] = request.name
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['LogPath'] = request.log_path
        query['SecurityGroupId'] = request.security_group_id
        query['IsOpenPublicIp'] = request.is_open_public_ip
        query['SecurityGroupName'] = request.security_group_name
        query['ChargeType'] = request.charge_type
        query['Period'] = request.period
        query['AutoRenew'] = request.auto_renew
        query['AutoPayOrder'] = request.auto_pay_order
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['NetType'] = request.net_type
        query['UserDefinedEmrEcsRole'] = request.user_defined_emr_ecs_role
        query['EmrVer'] = request.emr_ver
        query['ClusterType'] = request.cluster_type
        query['HighAvailabilityEnable'] = request.high_availability_enable
        query['UseLocalMetaDb'] = request.use_local_meta_db
        query['IoOptimized'] = request.io_optimized
        query['SshEnable'] = request.ssh_enable
        query['InstanceGeneration'] = request.instance_generation
        query['MasterPwd'] = request.master_pwd
        query['KeyPairName'] = request.key_pair_name
        query['MetaStoreType'] = request.meta_store_type
        query['MetaStoreConf'] = request.meta_store_conf
        query['ClickHouseConf'] = request.click_house_conf
        query['ExtraAttributes'] = request.extra_attributes
        query['DepositType'] = request.deposit_type
        query['MachineType'] = request.machine_type
        query['UseCustomHiveMetaDB'] = request.use_custom_hive_meta_db
        query['InitCustomHiveMetaDB'] = request.init_custom_hive_meta_db
        query['Configurations'] = request.configurations
        query['EasEnable'] = request.eas_enable
        query['RelatedClusterId'] = request.related_cluster_id
        query['WhiteListType'] = request.white_list_type
        query['AuthorizeContent'] = request.authorize_content
        query['ResourceGroupId'] = request.resource_group_id
        query['OptionSoftWareList'] = request.option_soft_ware_list
        query['UserInfo'] = request.user_info
        query['HostComponentInfo'] = request.host_component_info
        query['ServiceInfo'] = request.service_info
        query['PromotionInfo'] = request.promotion_info
        query['HostGroup'] = request.host_group
        query['BootstrapAction'] = request.bootstrap_action
        query['Config'] = request.config
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateClusterV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateClusterV2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_v2with_options_async(
        self,
        request: emr_20160408_models.CreateClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateClusterV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Name'] = request.name
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['LogPath'] = request.log_path
        query['SecurityGroupId'] = request.security_group_id
        query['IsOpenPublicIp'] = request.is_open_public_ip
        query['SecurityGroupName'] = request.security_group_name
        query['ChargeType'] = request.charge_type
        query['Period'] = request.period
        query['AutoRenew'] = request.auto_renew
        query['AutoPayOrder'] = request.auto_pay_order
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['NetType'] = request.net_type
        query['UserDefinedEmrEcsRole'] = request.user_defined_emr_ecs_role
        query['EmrVer'] = request.emr_ver
        query['ClusterType'] = request.cluster_type
        query['HighAvailabilityEnable'] = request.high_availability_enable
        query['UseLocalMetaDb'] = request.use_local_meta_db
        query['IoOptimized'] = request.io_optimized
        query['SshEnable'] = request.ssh_enable
        query['InstanceGeneration'] = request.instance_generation
        query['MasterPwd'] = request.master_pwd
        query['KeyPairName'] = request.key_pair_name
        query['MetaStoreType'] = request.meta_store_type
        query['MetaStoreConf'] = request.meta_store_conf
        query['ClickHouseConf'] = request.click_house_conf
        query['ExtraAttributes'] = request.extra_attributes
        query['DepositType'] = request.deposit_type
        query['MachineType'] = request.machine_type
        query['UseCustomHiveMetaDB'] = request.use_custom_hive_meta_db
        query['InitCustomHiveMetaDB'] = request.init_custom_hive_meta_db
        query['Configurations'] = request.configurations
        query['EasEnable'] = request.eas_enable
        query['RelatedClusterId'] = request.related_cluster_id
        query['WhiteListType'] = request.white_list_type
        query['AuthorizeContent'] = request.authorize_content
        query['ResourceGroupId'] = request.resource_group_id
        query['OptionSoftWareList'] = request.option_soft_ware_list
        query['UserInfo'] = request.user_info
        query['HostComponentInfo'] = request.host_component_info
        query['ServiceInfo'] = request.service_info
        query['PromotionInfo'] = request.promotion_info
        query['HostGroup'] = request.host_group
        query['BootstrapAction'] = request.bootstrap_action
        query['Config'] = request.config
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateClusterV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateClusterV2Response(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateBizId'] = request.template_biz_id
        query['UniqueTag'] = request.unique_tag
        query['ClusterName'] = request.cluster_name
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateClusterWithTemplate',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateClusterWithTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_template_with_options_async(
        self,
        request: emr_20160408_models.CreateClusterWithTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateClusterWithTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['TemplateBizId'] = request.template_biz_id
        query['UniqueTag'] = request.unique_tag
        query['ClusterName'] = request.cluster_name
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateClusterWithTemplate',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateClusterWithTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Name'] = request.name
        query['SourceType'] = request.source_type
        query['Description'] = request.description
        query['Conf'] = request.conf
        query['ClusterId'] = request.cluster_id
        query['NavParentId'] = request.nav_parent_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDataSource',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_data_source_with_options_async(
        self,
        request: emr_20160408_models.CreateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateDataSourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Name'] = request.name
        query['SourceType'] = request.source_type
        query['Description'] = request.description
        query['Conf'] = request.conf
        query['ClusterId'] = request.cluster_id
        query['NavParentId'] = request.nav_parent_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateDataSource',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Name'] = request.name
        query['Strategy'] = request.strategy
        query['TimeInterval'] = request.time_interval
        query['StartTime'] = request.start_time
        query['TimeUnit'] = request.time_unit
        query['DayOfWeek'] = request.day_of_week
        query['DayOfMonth'] = request.day_of_month
        query['ClusterId'] = request.cluster_id
        query['CreateClusterOnDemand'] = request.create_cluster_on_demand
        query['ClusterName'] = request.cluster_name
        query['ZoneId'] = request.zone_id
        query['LogEnable'] = request.log_enable
        query['LogPath'] = request.log_path
        query['SecurityGroupId'] = request.security_group_id
        query['IsOpenPublicIp'] = request.is_open_public_ip
        query['EmrVer'] = request.emr_ver
        query['ClusterType'] = request.cluster_type
        query['HighAvailabilityEnable'] = request.high_availability_enable
        query['UseLocalMetaDb'] = request.use_local_meta_db
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['NetType'] = request.net_type
        query['UserDefinedEmrEcsRole'] = request.user_defined_emr_ecs_role
        query['IoOptimized'] = request.io_optimized
        query['InstanceGeneration'] = request.instance_generation
        query['UseCustomHiveMetaDB'] = request.use_custom_hive_meta_db
        query['InitCustomHiveMetaDB'] = request.init_custom_hive_meta_db
        query['Configurations'] = request.configurations
        query['EasEnable'] = request.eas_enable
        query['WorkflowDefinition'] = request.workflow_definition
        query['JobIdList'] = request.job_id_list
        query['OptionSoftWareList'] = request.option_soft_ware_list
        query['EcsOrder'] = request.ecs_order
        query['BootstrapAction'] = request.bootstrap_action
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateExecutionPlan',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateExecutionPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_execution_plan_with_options_async(
        self,
        request: emr_20160408_models.CreateExecutionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateExecutionPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Name'] = request.name
        query['Strategy'] = request.strategy
        query['TimeInterval'] = request.time_interval
        query['StartTime'] = request.start_time
        query['TimeUnit'] = request.time_unit
        query['DayOfWeek'] = request.day_of_week
        query['DayOfMonth'] = request.day_of_month
        query['ClusterId'] = request.cluster_id
        query['CreateClusterOnDemand'] = request.create_cluster_on_demand
        query['ClusterName'] = request.cluster_name
        query['ZoneId'] = request.zone_id
        query['LogEnable'] = request.log_enable
        query['LogPath'] = request.log_path
        query['SecurityGroupId'] = request.security_group_id
        query['IsOpenPublicIp'] = request.is_open_public_ip
        query['EmrVer'] = request.emr_ver
        query['ClusterType'] = request.cluster_type
        query['HighAvailabilityEnable'] = request.high_availability_enable
        query['UseLocalMetaDb'] = request.use_local_meta_db
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['NetType'] = request.net_type
        query['UserDefinedEmrEcsRole'] = request.user_defined_emr_ecs_role
        query['IoOptimized'] = request.io_optimized
        query['InstanceGeneration'] = request.instance_generation
        query['UseCustomHiveMetaDB'] = request.use_custom_hive_meta_db
        query['InitCustomHiveMetaDB'] = request.init_custom_hive_meta_db
        query['Configurations'] = request.configurations
        query['EasEnable'] = request.eas_enable
        query['WorkflowDefinition'] = request.workflow_definition
        query['JobIdList'] = request.job_id_list
        query['OptionSoftWareList'] = request.option_soft_ware_list
        query['EcsOrder'] = request.ecs_order
        query['BootstrapAction'] = request.bootstrap_action
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateExecutionPlan',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateExecutionPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Name'] = request.name
        query['Description'] = request.description
        query['StartSchedule'] = request.start_schedule
        query['EndSchedule'] = request.end_schedule
        query['CronExpr'] = request.cron_expr
        query['CreateCluster'] = request.create_cluster
        query['ClusterId'] = request.cluster_id
        query['HostName'] = request.host_name
        query['Namespace'] = request.namespace
        query['LogArchiveLocation'] = request.log_archive_location
        query['Lifecycle'] = request.lifecycle
        query['Application'] = request.application
        query['AlertConf'] = request.alert_conf
        query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        query['ParentFlowList'] = request.parent_flow_list
        query['ParentCategory'] = request.parent_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_with_options_async(
        self,
        request: emr_20160408_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Name'] = request.name
        query['Description'] = request.description
        query['StartSchedule'] = request.start_schedule
        query['EndSchedule'] = request.end_schedule
        query['CronExpr'] = request.cron_expr
        query['CreateCluster'] = request.create_cluster
        query['ClusterId'] = request.cluster_id
        query['HostName'] = request.host_name
        query['Namespace'] = request.namespace
        query['LogArchiveLocation'] = request.log_archive_location
        query['Lifecycle'] = request.lifecycle
        query['Application'] = request.application
        query['AlertConf'] = request.alert_conf
        query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        query['ParentFlowList'] = request.parent_flow_list
        query['ParentCategory'] = request.parent_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Name'] = request.name
        query['Type'] = request.type
        query['ParentId'] = request.parent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFlowCategory',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateFlowCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_category_with_options_async(
        self,
        request: emr_20160408_models.CreateFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Name'] = request.name
        query['Type'] = request.type
        query['ParentId'] = request.parent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFlowCategory',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateFlowCategoryResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_flow_for_web_with_options(
        self,
        request: emr_20160408_models.CreateFlowForWebRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowForWebResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Name'] = request.name
        query['Description'] = request.description
        query['StartSchedule'] = request.start_schedule
        query['EndSchedule'] = request.end_schedule
        query['CronExpr'] = request.cron_expr
        query['CreateCluster'] = request.create_cluster
        query['ClusterId'] = request.cluster_id
        query['HostName'] = request.host_name
        query['Namespace'] = request.namespace
        query['LogArchiveLocation'] = request.log_archive_location
        query['Lifecycle'] = request.lifecycle
        query['Graph'] = request.graph
        query['AlertConf'] = request.alert_conf
        query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        query['ParentFlowList'] = request.parent_flow_list
        query['ParentCategory'] = request.parent_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFlowForWeb',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateFlowForWebResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_for_web_with_options_async(
        self,
        request: emr_20160408_models.CreateFlowForWebRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowForWebResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Name'] = request.name
        query['Description'] = request.description
        query['StartSchedule'] = request.start_schedule
        query['EndSchedule'] = request.end_schedule
        query['CronExpr'] = request.cron_expr
        query['CreateCluster'] = request.create_cluster
        query['ClusterId'] = request.cluster_id
        query['HostName'] = request.host_name
        query['Namespace'] = request.namespace
        query['LogArchiveLocation'] = request.log_archive_location
        query['Lifecycle'] = request.lifecycle
        query['Graph'] = request.graph
        query['AlertConf'] = request.alert_conf
        query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        query['ParentFlowList'] = request.parent_flow_list
        query['ParentCategory'] = request.parent_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFlowForWeb',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateFlowForWebResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Name'] = request.name
        query['Type'] = request.type
        query['FailAct'] = request.fail_act
        query['MaxRetry'] = request.max_retry
        query['RetryPolicy'] = request.retry_policy
        query['MaxRunningTimeSec'] = request.max_running_time_sec
        query['RetryInterval'] = request.retry_interval
        query['Mode'] = request.mode
        query['ParentCategory'] = request.parent_category
        query['Adhoc'] = request.adhoc
        query['ClusterId'] = request.cluster_id
        query['AlertConf'] = request.alert_conf
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFlowJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateFlowJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_job_with_options_async(
        self,
        request: emr_20160408_models.CreateFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Name'] = request.name
        query['Type'] = request.type
        query['FailAct'] = request.fail_act
        query['MaxRetry'] = request.max_retry
        query['RetryPolicy'] = request.retry_policy
        query['MaxRunningTimeSec'] = request.max_running_time_sec
        query['RetryInterval'] = request.retry_interval
        query['Mode'] = request.mode
        query['ParentCategory'] = request.parent_category
        query['Adhoc'] = request.adhoc
        query['ClusterId'] = request.cluster_id
        query['AlertConf'] = request.alert_conf
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFlowJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateFlowJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ProductType'] = request.product_type
        query['RegionId'] = request.region_id
        query['Name'] = request.name
        query['Description'] = request.description
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFlowProject',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateFlowProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_project_with_options_async(
        self,
        request: emr_20160408_models.CreateFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProductType'] = request.product_type
        query['RegionId'] = request.region_id
        query['Name'] = request.name
        query['Description'] = request.description
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFlowProject',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateFlowProjectResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['ClusterId'] = request.cluster_id
        query['DefaultUser'] = request.default_user
        query['DefaultQueue'] = request.default_queue
        query['UserList'] = request.user_list
        query['QueueList'] = request.queue_list
        query['HostList'] = request.host_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFlowProjectClusterSetting',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateFlowProjectClusterSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_project_cluster_setting_with_options_async(
        self,
        request: emr_20160408_models.CreateFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['ClusterId'] = request.cluster_id
        query['DefaultUser'] = request.default_user
        query['DefaultQueue'] = request.default_queue
        query['UserList'] = request.user_list
        query['QueueList'] = request.queue_list
        query['HostList'] = request.host_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFlowProjectClusterSetting',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateFlowProjectClusterSettingResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFlowProjectUser',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateFlowProjectUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_project_user_with_options_async(
        self,
        request: emr_20160408_models.CreateFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateFlowProjectUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateFlowProjectUser',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateFlowProjectUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Name'] = request.name
        query['RegionId'] = request.region_id
        query['Type'] = request.type
        query['RunParameter'] = request.run_parameter
        query['FailAct'] = request.fail_act
        query['MaxRetry'] = request.max_retry
        query['RetryInterval'] = request.retry_interval
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_with_options_async(
        self,
        request: emr_20160408_models.CreateJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Name'] = request.name
        query['RegionId'] = request.region_id
        query['Type'] = request.type
        query['RunParameter'] = request.run_parameter
        query['FailAct'] = request.fail_act
        query['MaxRetry'] = request.max_retry
        query['RetryInterval'] = request.retry_interval
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Type'] = request.type
        query['Name'] = request.name
        query['LibraryVersion'] = request.library_version
        query['SourceType'] = request.source_type
        query['SourceLocation'] = request.source_location
        query['Scope'] = request.scope
        query['Properties'] = request.properties
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateLibrary',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_library_with_options_async(
        self,
        request: emr_20160408_models.CreateLibraryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateLibraryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Type'] = request.type
        query['Name'] = request.name
        query['LibraryVersion'] = request.library_version
        query['SourceType'] = request.source_type
        query['SourceLocation'] = request.source_location
        query['Scope'] = request.scope
        query['Properties'] = request.properties
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateLibrary',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateLibraryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['DatabaseId'] = request.database_id
        query['TableId'] = request.table_id
        query['User'] = request.user
        query['Password'] = request.password
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMetaTablePreviewTask',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateMetaTablePreviewTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_meta_table_preview_task_with_options_async(
        self,
        request: emr_20160408_models.CreateMetaTablePreviewTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateMetaTablePreviewTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['DatabaseId'] = request.database_id
        query['TableId'] = request.table_id
        query['User'] = request.user
        query['Password'] = request.password
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMetaTablePreviewTask',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateMetaTablePreviewTaskResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_resource_pool_with_options(
        self,
        request: emr_20160408_models.CreateResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateResourcePoolResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Name'] = request.name
        query['ClusterId'] = request.cluster_id
        query['PoolType'] = request.pool_type
        query['Active'] = request.active
        query['Note'] = request.note
        query['YarnSiteConfig'] = request.yarn_site_config
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateResourcePool',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateResourcePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_pool_with_options_async(
        self,
        request: emr_20160408_models.CreateResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateResourcePoolResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Name'] = request.name
        query['ClusterId'] = request.cluster_id
        query['PoolType'] = request.pool_type
        query['Active'] = request.active
        query['Note'] = request.note
        query['YarnSiteConfig'] = request.yarn_site_config
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateResourcePool',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateResourcePoolResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Name'] = request.name
        query['QualifiedName'] = request.qualified_name
        query['ClusterId'] = request.cluster_id
        query['ParentQueueId'] = request.parent_queue_id
        query['Leaf'] = request.leaf
        query['ResourcePoolId'] = request.resource_pool_id
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateResourceQueue',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateResourceQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_queue_with_options_async(
        self,
        request: emr_20160408_models.CreateResourceQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateResourceQueueResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Name'] = request.name
        query['QualifiedName'] = request.qualified_name
        query['ClusterId'] = request.cluster_id
        query['ParentQueueId'] = request.parent_queue_id
        query['Leaf'] = request.leaf
        query['ResourcePoolId'] = request.resource_pool_id
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateResourceQueue',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateResourceQueueResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['Name'] = request.name
        query['Description'] = request.description
        query['HostGroupId'] = request.host_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateScalingGroupV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateScalingGroupV2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_scaling_group_v2with_options_async(
        self,
        request: emr_20160408_models.CreateScalingGroupV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateScalingGroupV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['Name'] = request.name
        query['Description'] = request.description
        query['HostGroupId'] = request.host_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateScalingGroupV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateScalingGroupV2Response(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['RuleCategory'] = request.rule_category
        query['RuleName'] = request.rule_name
        query['AdjustmentType'] = request.adjustment_type
        query['AdjustmentValue'] = request.adjustment_value
        query['Cooldown'] = request.cooldown
        query['LaunchTime'] = request.launch_time
        query['LaunchExpirationTime'] = request.launch_expiration_time
        query['RecurrenceType'] = request.recurrence_type
        query['RecurrenceValue'] = request.recurrence_value
        query['RecurrenceEndTime'] = request.recurrence_end_time
        query['WithGrace'] = request.with_grace
        query['TimeoutWithGrace'] = request.timeout_with_grace
        query['SchedulerTrigger'] = request.scheduler_trigger
        query['CloudWatchTrigger'] = request.cloud_watch_trigger
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateScalingRule',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_scaling_rule_with_options_async(
        self,
        request: emr_20160408_models.CreateScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['RuleCategory'] = request.rule_category
        query['RuleName'] = request.rule_name
        query['AdjustmentType'] = request.adjustment_type
        query['AdjustmentValue'] = request.adjustment_value
        query['Cooldown'] = request.cooldown
        query['LaunchTime'] = request.launch_time
        query['LaunchExpirationTime'] = request.launch_expiration_time
        query['RecurrenceType'] = request.recurrence_type
        query['RecurrenceValue'] = request.recurrence_value
        query['RecurrenceEndTime'] = request.recurrence_end_time
        query['WithGrace'] = request.with_grace
        query['TimeoutWithGrace'] = request.timeout_with_grace
        query['SchedulerTrigger'] = request.scheduler_trigger
        query['CloudWatchTrigger'] = request.cloud_watch_trigger
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateScalingRule',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Category'] = request.category
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTag',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tag_with_options_async(
        self,
        request: emr_20160408_models.CreateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateTagResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Category'] = request.category
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateTag',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateTagResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['AliyunUserId'] = request.aliyun_user_id
        query['UserName'] = request.user_name
        query['UserType'] = request.user_type
        query['Status'] = request.status
        query['Description'] = request.description
        query['RoleIdList'] = request.role_id_list
        query['GroupIdList'] = request.group_id_list
        query['UserAccountParamList'] = request.user_account_param_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: emr_20160408_models.CreateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['AliyunUserId'] = request.aliyun_user_id
        query['UserName'] = request.user_name
        query['UserType'] = request.user_type
        query['Status'] = request.status
        query['Description'] = request.description
        query['RoleIdList'] = request.role_id_list
        query['GroupIdList'] = request.group_id_list
        query['UserAccountParamList'] = request.user_account_param_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['UserInfo'] = request.user_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateUsers',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_users_with_options_async(
        self,
        request: emr_20160408_models.CreateUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.CreateUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['UserInfo'] = request.user_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateUsers',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.CreateUsersResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostInstanceId'] = request.host_instance_id
        query['ServiceName'] = request.service_name
        query['ComponentName'] = request.component_name
        query['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DecommissionHostComponent',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DecommissionHostComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def decommission_host_component_with_options_async(
        self,
        request: emr_20160408_models.DecommissionHostComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DecommissionHostComponentResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostInstanceId'] = request.host_instance_id
        query['ServiceName'] = request.service_name
        query['ComponentName'] = request.component_name
        query['TimeoutSeconds'] = request.timeout_seconds
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DecommissionHostComponent',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DecommissionHostComponentResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['BizId'] = request.biz_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteClusterTemplate',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteClusterTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_template_with_options_async(
        self,
        request: emr_20160408_models.DeleteClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteClusterTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['BizId'] = request.biz_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteClusterTemplate',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteClusterTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteExecutionPlan',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteExecutionPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_execution_plan_with_options_async(
        self,
        request: emr_20160408_models.DeleteExecutionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteExecutionPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteExecutionPlan',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteExecutionPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_with_options_async(
        self,
        request: emr_20160408_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFlowCategory',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteFlowCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_category_with_options_async(
        self,
        request: emr_20160408_models.DeleteFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFlowCategory',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteFlowCategoryResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_flow_job_with_options(
        self,
        request: emr_20160408_models.DeleteFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFlowJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteFlowJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_job_with_options_async(
        self,
        request: emr_20160408_models.DeleteFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFlowJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteFlowJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFlowProject',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteFlowProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_project_with_options_async(
        self,
        request: emr_20160408_models.DeleteFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFlowProject',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteFlowProjectResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFlowProjectClusterSetting',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteFlowProjectClusterSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_project_cluster_setting_with_options_async(
        self,
        request: emr_20160408_models.DeleteFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFlowProjectClusterSetting',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteFlowProjectClusterSettingResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFlowProjectUser',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteFlowProjectUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_project_user_with_options_async(
        self,
        request: emr_20160408_models.DeleteFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteFlowProjectUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteFlowProjectUser',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteFlowProjectUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_with_options_async(
        self,
        request: emr_20160408_models.DeleteJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['LibraryBizIdList'] = request.library_biz_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteLibraries',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteLibrariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_libraries_with_options_async(
        self,
        request: emr_20160408_models.DeleteLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteLibrariesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['LibraryBizIdList'] = request.library_biz_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteLibraries',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteLibrariesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_resource_pool_with_options(
        self,
        request: emr_20160408_models.DeleteResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteResourcePoolResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ResourcePoolId'] = request.resource_pool_id
        query['ClusterId'] = request.cluster_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteResourcePool',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteResourcePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_pool_with_options_async(
        self,
        request: emr_20160408_models.DeleteResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteResourcePoolResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ResourcePoolId'] = request.resource_pool_id
        query['ClusterId'] = request.cluster_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteResourcePool',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteResourcePoolResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ResourceQueueId'] = request.resource_queue_id
        query['ClusterId'] = request.cluster_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteResourceQueue',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteResourceQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_queue_with_options_async(
        self,
        request: emr_20160408_models.DeleteResourceQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteResourceQueueResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ResourceQueueId'] = request.resource_queue_id
        query['ClusterId'] = request.cluster_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteResourceQueue',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteResourceQueueResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['ScalingRuleId'] = request.scaling_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteScalingRule',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_scaling_rule_with_options_async(
        self,
        request: emr_20160408_models.DeleteScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['ScalingRuleId'] = request.scaling_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteScalingRule',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Category'] = request.category
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteTag',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_with_options_async(
        self,
        request: emr_20160408_models.DeleteTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteTagResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Category'] = request.category
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteTag',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteTagResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['UserId'] = request.user_id
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: emr_20160408_models.DeleteUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['UserId'] = request.user_id
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterBasicInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterBasicInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_basic_info_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterBasicInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterBasicInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterBasicInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterBasicInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterMetaCollect',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterMetaCollectResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_meta_collect_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterMetaCollectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterMetaCollectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterMetaCollect',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterMetaCollectResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['OperationId'] = request.operation_id
        query['HostId'] = request.host_id
        query['TaskId'] = request.task_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterOperationHostTaskLog',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterOperationHostTaskLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_operation_host_task_log_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterOperationHostTaskLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterOperationHostTaskLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['OperationId'] = request.operation_id
        query['HostId'] = request.host_id
        query['TaskId'] = request.task_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterOperationHostTaskLog',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterOperationHostTaskLogResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterResourcePoolSchedulerType',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterResourcePoolSchedulerTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_resource_pool_scheduler_type_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterResourcePoolSchedulerTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterResourcePoolSchedulerTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterResourcePoolSchedulerType',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterResourcePoolSchedulerTypeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterService',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_service_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterService',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterServiceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        query['ConfigVersion'] = request.config_version
        query['GroupId'] = request.group_id
        query['HostInstanceId'] = request.host_instance_id
        query['TagValue'] = request.tag_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterServiceConfig',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterServiceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_service_config_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterServiceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        query['ConfigVersion'] = request.config_version
        query['GroupId'] = request.group_id
        query['HostInstanceId'] = request.host_instance_id
        query['TagValue'] = request.tag_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterServiceConfig',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterServiceConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        query['ConfigVersion'] = request.config_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterServiceConfigHistory',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterServiceConfigHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_service_config_history_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterServiceConfigHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterServiceConfigHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        query['ConfigVersion'] = request.config_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterServiceConfigHistory',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterServiceConfigHistoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        query['ConfigTag'] = request.config_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterServiceConfigTag',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterServiceConfigTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_service_config_tag_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterServiceConfigTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterServiceConfigTagResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        query['ConfigTag'] = request.config_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterServiceConfigTag',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterServiceConfigTagResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['BizId'] = request.biz_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterTemplate',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_template_with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['BizId'] = request.biz_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterTemplate',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_v2with_options_async(
        self,
        request: emr_20160408_models.DescribeClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeClusterV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeClusterV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeClusterV2Response(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDataSource',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_data_source_with_options_async(
        self,
        request: emr_20160408_models.DescribeDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeDataSourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeDataSource',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeExecutionPlan',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeExecutionPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_execution_plan_with_options_async(
        self,
        request: emr_20160408_models.DescribeExecutionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeExecutionPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeExecutionPlan',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeExecutionPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_flow_category_with_options(
        self,
        request: emr_20160408_models.DescribeFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowCategory',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_category_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowCategory',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowCategoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Type'] = request.type
        query['Mode'] = request.mode
        query['Keyword'] = request.keyword
        query['CategoryId'] = request.category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowCategoryTree',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowCategoryTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_category_tree_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowCategoryTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowCategoryTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Type'] = request.type
        query['Mode'] = request.mode
        query['Keyword'] = request.keyword
        query['CategoryId'] = request.category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowCategoryTree',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowCategoryTreeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_flow_instance_with_options(
        self,
        request: emr_20160408_models.DescribeFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowInstance',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_instance_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowInstance',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_job_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowNodeInstance',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowNodeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_node_instance_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowNodeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowNodeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowNodeInstance',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowNodeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Offset'] = request.offset
        query['Length'] = request.length
        query['NodeInstanceId'] = request.node_instance_id
        query['AppId'] = request.app_id
        query['ContainerId'] = request.container_id
        query['LogName'] = request.log_name
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowNodeInstanceContainerLog',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowNodeInstanceContainerLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_node_instance_container_log_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowNodeInstanceContainerLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowNodeInstanceContainerLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Offset'] = request.offset
        query['Length'] = request.length
        query['NodeInstanceId'] = request.node_instance_id
        query['AppId'] = request.app_id
        query['ContainerId'] = request.container_id
        query['LogName'] = request.log_name
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowNodeInstanceContainerLog',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowNodeInstanceContainerLogResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Start'] = request.start
        query['Lines'] = request.lines
        query['Offset'] = request.offset
        query['Length'] = request.length
        query['Reverse'] = request.reverse
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['NodeInstanceId'] = request.node_instance_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowNodeInstanceLauncherLog',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowNodeInstanceLauncherLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_node_instance_launcher_log_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowNodeInstanceLauncherLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowNodeInstanceLauncherLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Start'] = request.start
        query['Lines'] = request.lines
        query['Offset'] = request.offset
        query['Length'] = request.length
        query['Reverse'] = request.reverse
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        query['NodeInstanceId'] = request.node_instance_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowNodeInstanceLauncherLog',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowNodeInstanceLauncherLogResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowProject',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_project_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowProject',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowProjectResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowProjectClusterSetting',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowProjectClusterSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_project_cluster_setting_with_options_async(
        self,
        request: emr_20160408_models.DescribeFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeFlowProjectClusterSetting',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeFlowProjectClusterSettingResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_with_options_async(
        self,
        request: emr_20160408_models.DescribeJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['LibraryBizId'] = request.library_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLibraryDetail',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeLibraryDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_library_detail_with_options_async(
        self,
        request: emr_20160408_models.DescribeLibraryDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeLibraryDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['LibraryBizId'] = request.library_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLibraryDetail',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeLibraryDetailResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['TaskBizId'] = request.task_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLibraryInstallTaskDetail',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeLibraryInstallTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_library_install_task_detail_with_options_async(
        self,
        request: emr_20160408_models.DescribeLibraryInstallTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeLibraryInstallTaskDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['TaskBizId'] = request.task_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeLibraryInstallTaskDetail',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeLibraryInstallTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['TaskId'] = request.task_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMetaTablePreviewTask',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeMetaTablePreviewTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_meta_table_preview_task_with_options_async(
        self,
        request: emr_20160408_models.DescribeMetaTablePreviewTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeMetaTablePreviewTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['TaskId'] = request.task_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMetaTablePreviewTask',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeMetaTablePreviewTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScalingActivity',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeScalingActivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_activity_with_options_async(
        self,
        request: emr_20160408_models.DescribeScalingActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingActivityResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScalingActivity',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeScalingActivityResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScalingCommonConfig',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeScalingCommonConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_common_config_with_options_async(
        self,
        request: emr_20160408_models.DescribeScalingCommonConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingCommonConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScalingCommonConfig',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeScalingCommonConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['ConfigItemType'] = request.config_item_type
        query['ScalingConfigItemId'] = request.scaling_config_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScalingConfigItemV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeScalingConfigItemV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_config_item_v2with_options_async(
        self,
        request: emr_20160408_models.DescribeScalingConfigItemV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingConfigItemV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['ConfigItemType'] = request.config_item_type
        query['ScalingConfigItemId'] = request.scaling_config_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScalingConfigItemV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeScalingConfigItemV2Response(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['HostGroupBizId'] = request.host_group_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScalingGroupInstanceV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeScalingGroupInstanceV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_group_instance_v2with_options_async(
        self,
        request: emr_20160408_models.DescribeScalingGroupInstanceV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingGroupInstanceV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['HostGroupBizId'] = request.host_group_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScalingGroupInstanceV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeScalingGroupInstanceV2Response(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['HostGroupBizId'] = request.host_group_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScalingGroupV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeScalingGroupV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_group_v2with_options_async(
        self,
        request: emr_20160408_models.DescribeScalingGroupV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingGroupV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['HostGroupBizId'] = request.host_group_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScalingGroupV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeScalingGroupV2Response(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['ScalingRuleId'] = request.scaling_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScalingRule',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_scaling_rule_with_options_async(
        self,
        request: emr_20160408_models.DescribeScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['ScalingRuleId'] = request.scaling_rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeScalingRule',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroupAttribute',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeSecurityGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_group_attribute_with_options_async(
        self,
        request: emr_20160408_models.DescribeSecurityGroupAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DescribeSecurityGroupAttributeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeSecurityGroupAttribute',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DescribeSecurityGroupAttributeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['TargetClusterId'] = request.target_cluster_id
        query['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetachAndReleaseClusterEni',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DetachAndReleaseClusterEniResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_and_release_cluster_eni_with_options_async(
        self,
        request: emr_20160408_models.DetachAndReleaseClusterEniRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.DetachAndReleaseClusterEniResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['TargetClusterId'] = request.target_cluster_id
        query['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DetachAndReleaseClusterEni',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.DetachAndReleaseClusterEniResponse(),
            await self.call_api_async(params, req, runtime)
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

    def get_hdfs_capacity_statistic_info_with_options(
        self,
        request: emr_20160408_models.GetHdfsCapacityStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetHdfsCapacityStatisticInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetHdfsCapacityStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetHdfsCapacityStatisticInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_hdfs_capacity_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetHdfsCapacityStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetHdfsCapacityStatisticInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetHdfsCapacityStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetHdfsCapacityStatisticInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetJobInputStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetJobInputStatisticInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_input_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetJobInputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetJobInputStatisticInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetJobInputStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetJobInputStatisticInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetJobOutputStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetJobOutputStatisticInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_output_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetJobOutputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetJobOutputStatisticInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetJobOutputStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetJobOutputStatisticInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetJobRunningTimeStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetJobRunningTimeStatisticInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_running_time_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetJobRunningTimeStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetJobRunningTimeStatisticInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetJobRunningTimeStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetJobRunningTimeStatisticInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetQueueInputStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetQueueInputStatisticInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_queue_input_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetQueueInputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetQueueInputStatisticInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetQueueInputStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetQueueInputStatisticInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetQueueOutputStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetQueueOutputStatisticInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_queue_output_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetQueueOutputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetQueueOutputStatisticInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetQueueOutputStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetQueueOutputStatisticInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        query['ApplicationType'] = request.application_type
        query['FinalStatus'] = request.final_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetQueueSubmissionStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetQueueSubmissionStatisticInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_queue_submission_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetQueueSubmissionStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetQueueSubmissionStatisticInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        query['ApplicationType'] = request.application_type
        query['FinalStatus'] = request.final_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetQueueSubmissionStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetQueueSubmissionStatisticInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetUserInputStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetUserInputStatisticInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_input_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetUserInputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetUserInputStatisticInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetUserInputStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetUserInputStatisticInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetUserOutputStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetUserOutputStatisticInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_output_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetUserOutputStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetUserOutputStatisticInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetUserOutputStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetUserOutputStatisticInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        query['ApplicationType'] = request.application_type
        query['FinalStatus'] = request.final_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetUserSubmissionStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetUserSubmissionStatisticInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_submission_statistic_info_with_options_async(
        self,
        request: emr_20160408_models.GetUserSubmissionStatisticInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.GetUserSubmissionStatisticInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['FromDatetime'] = request.from_datetime
        query['ToDatetime'] = request.to_datetime
        query['ApplicationType'] = request.application_type
        query['FinalStatus'] = request.final_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetUserSubmissionStatisticInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.GetUserSubmissionStatisticInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['LibraryBizId'] = request.library_biz_id
        query['ClusterBizIdList'] = request.cluster_biz_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='InstallLibraries',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.InstallLibrariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_libraries_with_options_async(
        self,
        request: emr_20160408_models.InstallLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.InstallLibrariesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['LibraryBizId'] = request.library_biz_id
        query['ClusterBizIdList'] = request.cluster_biz_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='InstallLibraries',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.InstallLibrariesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        query['ResourceId'] = request.resource_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='JoinResourceGroup',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.JoinResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_resource_group_with_options_async(
        self,
        request: emr_20160408_models.JoinResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.JoinResourceGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        query['ResourceId'] = request.resource_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='JoinResourceGroup',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.JoinResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
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

    def kill_flow_job_with_options(
        self,
        request: emr_20160408_models.KillFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.KillFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['JobInstanceId'] = request.job_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='KillFlowJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.KillFlowJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_flow_job_with_options_async(
        self,
        request: emr_20160408_models.KillFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.KillFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['JobInstanceId'] = request.job_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='KillFlowJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.KillFlowJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        query['Component'] = request.component
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAdviceAction',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListAdviceActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_advice_action_with_options_async(
        self,
        request: emr_20160408_models.ListAdviceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListAdviceActionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        query['Component'] = request.component
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListAdviceAction',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListAdviceActionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['StartTimeFrom'] = request.start_time_from
        query['StartTimeTo'] = request.start_time_to
        query['EndTimeFrom'] = request.end_time_from
        query['EndTimeTo'] = request.end_time_to
        query['ClusterId'] = request.cluster_id
        query['AppId'] = request.app_id
        query['State'] = request.state
        query['FinalStatus'] = request.final_status
        query['User'] = request.user
        query['Queue'] = request.queue
        query['Name'] = request.name
        query['JobType'] = request.job_type
        query['OrderBy'] = request.order_by
        query['DiagnoseResult'] = request.diagnose_result
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListApmApplication',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListApmApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_apm_application_with_options_async(
        self,
        request: emr_20160408_models.ListApmApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListApmApplicationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['StartTimeFrom'] = request.start_time_from
        query['StartTimeTo'] = request.start_time_to
        query['EndTimeFrom'] = request.end_time_from
        query['EndTimeTo'] = request.end_time_to
        query['ClusterId'] = request.cluster_id
        query['AppId'] = request.app_id
        query['State'] = request.state
        query['FinalStatus'] = request.final_status
        query['User'] = request.user
        query['Queue'] = request.queue
        query['Name'] = request.name
        query['JobType'] = request.job_type
        query['OrderBy'] = request.order_by
        query['DiagnoseResult'] = request.diagnose_result
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListApmApplication',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListApmApplicationResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Limit'] = request.limit
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['CurrentSize'] = request.current_size
        query['PageCount'] = request.page_count
        query['OrderMode'] = request.order_mode
        query['Id'] = request.id
        query['BizId'] = request.biz_id
        query['MetadataType'] = request.metadata_type
        query['ServiceName'] = request.service_name
        query['BackupPlanId'] = request.backup_plan_id
        query['ClusterId'] = request.cluster_id
        query['Status'] = request.status
        query['BackupId'] = request.backup_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListBackups',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_backups_with_options_async(
        self,
        request: emr_20160408_models.ListBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListBackupsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Limit'] = request.limit
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['CurrentSize'] = request.current_size
        query['PageCount'] = request.page_count
        query['OrderMode'] = request.order_mode
        query['Id'] = request.id
        query['BizId'] = request.biz_id
        query['MetadataType'] = request.metadata_type
        query['ServiceName'] = request.service_name
        query['BackupPlanId'] = request.backup_plan_id
        query['ClusterId'] = request.cluster_id
        query['Status'] = request.status
        query['BackupId'] = request.backup_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListBackups',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListBackupsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostInstanceId'] = request.host_instance_id
        query['HostGroupId'] = request.host_group_id
        query['HostName'] = request.host_name
        query['PrivateIp'] = request.private_ip
        query['PublicIp'] = request.public_ip
        query['GroupType'] = request.group_type
        query['ComponentName'] = request.component_name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterHost',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_host_with_options_async(
        self,
        request: emr_20160408_models.ListClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterHostResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostInstanceId'] = request.host_instance_id
        query['HostGroupId'] = request.host_group_id
        query['HostName'] = request.host_name
        query['PrivateIp'] = request.private_ip
        query['PublicIp'] = request.public_ip
        query['GroupType'] = request.group_type
        query['ComponentName'] = request.component_name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterHost',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterHostResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostInstanceId'] = request.host_instance_id
        query['HostName'] = request.host_name
        query['ServiceName'] = request.service_name
        query['ComponentName'] = request.component_name
        query['ComponentStatus'] = request.component_status
        query['HostRole'] = request.host_role
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterHostComponent',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterHostComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_host_component_with_options_async(
        self,
        request: emr_20160408_models.ListClusterHostComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterHostComponentResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostInstanceId'] = request.host_instance_id
        query['HostName'] = request.host_name
        query['ServiceName'] = request.service_name
        query['ComponentName'] = request.component_name
        query['ComponentStatus'] = request.component_status
        query['HostRole'] = request.host_role
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterHostComponent',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterHostComponentResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['HostGroupName'] = request.host_group_name
        query['HostGroupType'] = request.host_group_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterHostGroup',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_host_group_with_options_async(
        self,
        request: emr_20160408_models.ListClusterHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterHostGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['HostGroupName'] = request.host_group_name
        query['HostGroupType'] = request.host_group_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterHostGroup',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterInstalledService',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterInstalledServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_installed_service_with_options_async(
        self,
        request: emr_20160408_models.ListClusterInstalledServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterInstalledServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterInstalledService',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterInstalledServiceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['OperationId'] = request.operation_id
        query['ServiceName'] = request.service_name
        query['Status'] = request.status
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterOperation',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_operation_with_options_async(
        self,
        request: emr_20160408_models.ListClusterOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterOperationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['OperationId'] = request.operation_id
        query['ServiceName'] = request.service_name
        query['Status'] = request.status
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterOperation',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterOperationResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['OperationId'] = request.operation_id
        query['Status'] = request.status
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterOperationHost',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterOperationHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_operation_host_with_options_async(
        self,
        request: emr_20160408_models.ListClusterOperationHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterOperationHostResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['OperationId'] = request.operation_id
        query['Status'] = request.status
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterOperationHost',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterOperationHostResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['OperationId'] = request.operation_id
        query['HostId'] = request.host_id
        query['Status'] = request.status
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterOperationHostTask',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterOperationHostTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_operation_host_task_with_options_async(
        self,
        request: emr_20160408_models.ListClusterOperationHostTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterOperationHostTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['OperationId'] = request.operation_id
        query['HostId'] = request.host_id
        query['Status'] = request.status
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterOperationHostTask',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterOperationHostTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['OperationId'] = request.operation_id
        query['Status'] = request.status
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterOperationTask',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterOperationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_operation_task_with_options_async(
        self,
        request: emr_20160408_models.ListClusterOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterOperationTaskResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['OperationId'] = request.operation_id
        query['Status'] = request.status
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterOperationTask',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterOperationTaskResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['CreateType'] = request.create_type
        query['MachineType'] = request.machine_type
        query['IsDesc'] = request.is_desc
        query['DepositType'] = request.deposit_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['DefaultStatus'] = request.default_status
        query['Name'] = request.name
        query['VpcId'] = request.vpc_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ClusterTypeList'] = request.cluster_type_list
        query['StatusList'] = request.status_list
        query['Tag'] = request.tag
        query['ExpiredTagList'] = request.expired_tag_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: emr_20160408_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['CreateType'] = request.create_type
        query['MachineType'] = request.machine_type
        query['IsDesc'] = request.is_desc
        query['DepositType'] = request.deposit_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['DefaultStatus'] = request.default_status
        query['Name'] = request.name
        query['VpcId'] = request.vpc_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ClusterTypeList'] = request.cluster_type_list
        query['StatusList'] = request.status_list
        query['Tag'] = request.tag
        query['ExpiredTagList'] = request.expired_tag_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterService',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_service_with_options_async(
        self,
        request: emr_20160408_models.ListClusterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterService',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterServiceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['PodName'] = request.pod_name
        query['ServiceName'] = request.service_name
        query['ComponentName'] = request.component_name
        query['ComponentStatus'] = request.component_status
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterServiceComponent',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterServiceComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_service_component_with_options_async(
        self,
        request: emr_20160408_models.ListClusterServiceComponentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterServiceComponentResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['PodName'] = request.pod_name
        query['ServiceName'] = request.service_name
        query['ComponentName'] = request.component_name
        query['ComponentStatus'] = request.component_status
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterServiceComponent',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterServiceComponentResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterServiceComponentHealthInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterServiceComponentHealthInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_service_component_health_info_with_options_async(
        self,
        request: emr_20160408_models.ListClusterServiceComponentHealthInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterServiceComponentHealthInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterServiceComponentHealthInfo',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterServiceComponentHealthInfoResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        query['ConfigVersion'] = request.config_version
        query['HostGroupId'] = request.host_group_id
        query['HostInstanceId'] = request.host_instance_id
        query['ConfigFileName'] = request.config_file_name
        query['ConfigItemKey'] = request.config_item_key
        query['Author'] = request.author
        query['Comment'] = request.comment
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterServiceConfigHistory',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterServiceConfigHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_service_config_history_with_options_async(
        self,
        request: emr_20160408_models.ListClusterServiceConfigHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterServiceConfigHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        query['ConfigVersion'] = request.config_version
        query['HostGroupId'] = request.host_group_id
        query['HostInstanceId'] = request.host_instance_id
        query['ConfigFileName'] = request.config_file_name
        query['ConfigItemKey'] = request.config_item_key
        query['Author'] = request.author
        query['Comment'] = request.comment
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterServiceConfigHistory',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterServiceConfigHistoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        query['DirectType'] = request.direct_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterServiceQuickLink',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterServiceQuickLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_service_quick_link_with_options_async(
        self,
        request: emr_20160408_models.ListClusterServiceQuickLinkRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterServiceQuickLinkResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        query['DirectType'] = request.direct_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterServiceQuickLink',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterServiceQuickLinkResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['BizId'] = request.biz_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProductType'] = request.product_type
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterTemplates',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_templates_with_options_async(
        self,
        request: emr_20160408_models.ListClusterTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListClusterTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['BizId'] = request.biz_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProductType'] = request.product_type
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListClusterTemplates',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListClusterTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['Name'] = request.name
        query['SourceType'] = request.source_type
        query['CreateFrom'] = request.create_from
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDataSource',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_source_with_options_async(
        self,
        request: emr_20160408_models.ListDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListDataSourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['PageSize'] = request.page_size
        query['PageNumber'] = request.page_number
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['Name'] = request.name
        query['SourceType'] = request.source_type
        query['CreateFrom'] = request.create_from
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDataSource',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_disk_ops_events_with_options(
        self,
        request: emr_20160408_models.ListDiskOpsEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListDiskOpsEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['UserId'] = request.user_id
        query['ClusterId'] = request.cluster_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDiskOpsEvents',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListDiskOpsEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_disk_ops_events_with_options_async(
        self,
        request: emr_20160408_models.ListDiskOpsEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListDiskOpsEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['UserId'] = request.user_id
        query['ClusterId'] = request.cluster_id
        query['StartTime'] = request.start_time
        query['EndTime'] = request.end_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListDiskOpsEvents',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListDiskOpsEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_disk_ops_events(
        self,
        request: emr_20160408_models.ListDiskOpsEventsRequest,
    ) -> emr_20160408_models.ListDiskOpsEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_disk_ops_events_with_options(request, runtime)

    async def list_disk_ops_events_async(
        self,
        request: emr_20160408_models.ListDiskOpsEventsRequest,
    ) -> emr_20160408_models.ListDiskOpsEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_disk_ops_events_with_options_async(request, runtime)

    def list_emr_available_config_with_options(
        self,
        request: emr_20160408_models.ListEmrAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListEmrAvailableConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListEmrAvailableConfig',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListEmrAvailableConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_emr_available_config_with_options_async(
        self,
        request: emr_20160408_models.ListEmrAvailableConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListEmrAvailableConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListEmrAvailableConfig',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListEmrAvailableConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DestinationResource'] = request.destination_resource
        query['ClusterType'] = request.cluster_type
        query['InstanceChargeType'] = request.instance_charge_type
        query['SpotStrategy'] = request.spot_strategy
        query['ZoneId'] = request.zone_id
        query['NetType'] = request.net_type
        query['InstanceType'] = request.instance_type
        query['SystemDiskType'] = request.system_disk_type
        query['DataDiskType'] = request.data_disk_type
        query['DepositType'] = request.deposit_type
        query['ClusterId'] = request.cluster_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListEmrAvailableResource',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListEmrAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_emr_available_resource_with_options_async(
        self,
        request: emr_20160408_models.ListEmrAvailableResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListEmrAvailableResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['DestinationResource'] = request.destination_resource
        query['ClusterType'] = request.cluster_type
        query['InstanceChargeType'] = request.instance_charge_type
        query['SpotStrategy'] = request.spot_strategy
        query['ZoneId'] = request.zone_id
        query['NetType'] = request.net_type
        query['InstanceType'] = request.instance_type
        query['SystemDiskType'] = request.system_disk_type
        query['DataDiskType'] = request.data_disk_type
        query['DepositType'] = request.deposit_type
        query['ClusterId'] = request.cluster_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListEmrAvailableResource',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListEmrAvailableResourceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['EmrVersion'] = request.emr_version
        query['StackName'] = request.stack_name
        query['StackVersion'] = request.stack_version
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListEmrMainVersion',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListEmrMainVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_emr_main_version_with_options_async(
        self,
        request: emr_20160408_models.ListEmrMainVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListEmrMainVersionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['EmrVersion'] = request.emr_version
        query['StackName'] = request.stack_name
        query['StackVersion'] = request.stack_version
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListEmrMainVersion',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListEmrMainVersionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['OnlyLastInstance'] = request.only_last_instance
        query['IsDesc'] = request.is_desc
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ExecutionPlanIdList'] = request.execution_plan_id_list
        query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListExecutionPlanInstances',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListExecutionPlanInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_execution_plan_instances_with_options_async(
        self,
        request: emr_20160408_models.ListExecutionPlanInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListExecutionPlanInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['OnlyLastInstance'] = request.only_last_instance
        query['IsDesc'] = request.is_desc
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ExecutionPlanIdList'] = request.execution_plan_id_list
        query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListExecutionPlanInstances',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListExecutionPlanInstancesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_flow_with_options(
        self,
        request: emr_20160408_models.ListFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['JobId'] = request.job_id
        query['Name'] = request.name
        query['Id'] = request.id
        query['ClusterId'] = request.cluster_id
        query['Status'] = request.status
        query['Periodic'] = request.periodic
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_with_options_async(
        self,
        request: emr_20160408_models.ListFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['JobId'] = request.job_id
        query['Name'] = request.name
        query['Id'] = request.id
        query['ClusterId'] = request.cluster_id
        query['Status'] = request.status
        query['Periodic'] = request.periodic
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['ParentId'] = request.parent_id
        query['Root'] = request.root
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowCategory',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_category_with_options_async(
        self,
        request: emr_20160408_models.ListFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['ParentId'] = request.parent_id
        query['Root'] = request.root
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowCategory',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowCategoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowCluster',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_cluster_with_options_async(
        self,
        request: emr_20160408_models.ListFlowClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowCluster',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowClusterResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ProductType'] = request.product_type
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowClusterAll',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowClusterAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_cluster_all_with_options_async(
        self,
        request: emr_20160408_models.ListFlowClusterAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowClusterAllResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProductType'] = request.product_type
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowClusterAll',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowClusterAllResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['ClusterId'] = request.cluster_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowClusterAllHosts',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowClusterAllHostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_cluster_all_hosts_with_options_async(
        self,
        request: emr_20160408_models.ListFlowClusterAllHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowClusterAllHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['ClusterId'] = request.cluster_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowClusterAllHosts',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowClusterAllHostsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['ClusterId'] = request.cluster_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowClusterHost',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowClusterHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_cluster_host_with_options_async(
        self,
        request: emr_20160408_models.ListFlowClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowClusterHostResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['ClusterId'] = request.cluster_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowClusterHost',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowClusterHostResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_flow_instance_with_options(
        self,
        request: emr_20160408_models.ListFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['FlowId'] = request.flow_id
        query['FlowName'] = request.flow_name
        query['Owner'] = request.owner
        query['InstanceId'] = request.instance_id
        query['NodeInstanceId'] = request.node_instance_id
        query['TimeRange'] = request.time_range
        query['OrderBy'] = request.order_by
        query['OrderType'] = request.order_type
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowInstance',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_instance_with_options_async(
        self,
        request: emr_20160408_models.ListFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['FlowId'] = request.flow_id
        query['FlowName'] = request.flow_name
        query['Owner'] = request.owner
        query['InstanceId'] = request.instance_id
        query['NodeInstanceId'] = request.node_instance_id
        query['TimeRange'] = request.time_range
        query['OrderBy'] = request.order_by
        query['OrderType'] = request.order_type
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowInstance',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Type'] = request.type
        query['Adhoc'] = request.adhoc
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_job_with_options_async(
        self,
        request: emr_20160408_models.ListFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Type'] = request.type
        query['Adhoc'] = request.adhoc
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['JobType'] = request.job_type
        query['InstanceId'] = request.instance_id
        query['TimeRange'] = request.time_range
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowJobHistory',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowJobHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_job_history_with_options_async(
        self,
        request: emr_20160408_models.ListFlowJobHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowJobHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['JobType'] = request.job_type
        query['InstanceId'] = request.instance_id
        query['TimeRange'] = request.time_range
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowJobHistory',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowJobHistoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['StartTime'] = request.start_time
        query['OrderBy'] = request.order_by
        query['OrderType'] = request.order_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceGroupId'] = request.resource_group_id
        query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowNodeInstance',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowNodeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_node_instance_with_options_async(
        self,
        request: emr_20160408_models.ListFlowNodeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowNodeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['StartTime'] = request.start_time
        query['OrderBy'] = request.order_by
        query['OrderType'] = request.order_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceGroupId'] = request.resource_group_id
        query['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowNodeInstance',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowNodeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['NodeInstanceId'] = request.node_instance_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowNodeInstanceContainerStatus',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowNodeInstanceContainerStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_node_instance_container_status_with_options_async(
        self,
        request: emr_20160408_models.ListFlowNodeInstanceContainerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowNodeInstanceContainerStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['NodeInstanceId'] = request.node_instance_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowNodeInstanceContainerStatus',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowNodeInstanceContainerStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['NodeInstanceId'] = request.node_instance_id
        query['SqlIndex'] = request.sql_index
        query['Offset'] = request.offset
        query['Length'] = request.length
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowNodeSqlResult',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowNodeSqlResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_node_sql_result_with_options_async(
        self,
        request: emr_20160408_models.ListFlowNodeSqlResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowNodeSqlResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['NodeInstanceId'] = request.node_instance_id
        query['SqlIndex'] = request.sql_index
        query['Offset'] = request.offset
        query['Length'] = request.length
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowNodeSqlResult',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowNodeSqlResultResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ProductType'] = request.product_type
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowProject',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_project_with_options_async(
        self,
        request: emr_20160408_models.ListFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProductType'] = request.product_type
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowProject',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowProjectResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowProjectClusterSetting',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowProjectClusterSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_project_cluster_setting_with_options_async(
        self,
        request: emr_20160408_models.ListFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowProjectClusterSetting',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowProjectClusterSettingResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowProjectUser',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowProjectUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_project_user_with_options_async(
        self,
        request: emr_20160408_models.ListFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListFlowProjectUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListFlowProjectUser',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListFlowProjectUserResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ExecutionPlanInstanceId'] = request.execution_plan_instance_id
        query['IsDesc'] = request.is_desc
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListJobExecutionInstances',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListJobExecutionInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_execution_instances_with_options_async(
        self,
        request: emr_20160408_models.ListJobExecutionInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListJobExecutionInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ExecutionPlanInstanceId'] = request.execution_plan_instance_id
        query['IsDesc'] = request.is_desc
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListJobExecutionInstances',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListJobExecutionInstancesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_jobs_with_options(
        self,
        request: emr_20160408_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['IsDesc'] = request.is_desc
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['QueryType'] = request.query_type
        query['QueryString'] = request.query_string
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_jobs_with_options_async(
        self,
        request: emr_20160408_models.ListJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['IsDesc'] = request.is_desc
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['QueryType'] = request.query_type
        query['QueryString'] = request.query_string
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListJobs',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListJobsResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Limit'] = request.limit
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['CurrentSize'] = request.current_size
        query['PageCount'] = request.page_count
        query['OrderField'] = request.order_field
        query['OrderMode'] = request.order_mode
        query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListLibraries',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListLibrariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_libraries_with_options_async(
        self,
        request: emr_20160408_models.ListLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListLibrariesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Limit'] = request.limit
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['CurrentSize'] = request.current_size
        query['PageCount'] = request.page_count
        query['OrderField'] = request.order_field
        query['OrderMode'] = request.order_mode
        query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListLibraries',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListLibrariesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Limit'] = request.limit
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['CurrentSize'] = request.current_size
        query['PageCount'] = request.page_count
        query['OrderField'] = request.order_field
        query['OrderMode'] = request.order_mode
        query['LibraryBizId'] = request.library_biz_id
        query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListLibraryInstallTasks',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListLibraryInstallTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_library_install_tasks_with_options_async(
        self,
        request: emr_20160408_models.ListLibraryInstallTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListLibraryInstallTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Limit'] = request.limit
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['CurrentSize'] = request.current_size
        query['PageCount'] = request.page_count
        query['OrderField'] = request.order_field
        query['OrderMode'] = request.order_mode
        query['LibraryBizId'] = request.library_biz_id
        query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListLibraryInstallTasks',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListLibraryInstallTasksResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Limit'] = request.limit
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['CurrentSize'] = request.current_size
        query['PageCount'] = request.page_count
        query['OrderField'] = request.order_field
        query['OrderMode'] = request.order_mode
        query['LibraryBizId'] = request.library_biz_id
        query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListLibraryStatus',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListLibraryStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_library_status_with_options_async(
        self,
        request: emr_20160408_models.ListLibraryStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListLibraryStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Limit'] = request.limit
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['CurrentSize'] = request.current_size
        query['PageCount'] = request.page_count
        query['OrderField'] = request.order_field
        query['OrderMode'] = request.order_mode
        query['LibraryBizId'] = request.library_biz_id
        query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListLibraryStatus',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListLibraryStatusResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_resource_pool_with_options(
        self,
        request: emr_20160408_models.ListResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListResourcePoolResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['PoolType'] = request.pool_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListResourcePool',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListResourcePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_pool_with_options_async(
        self,
        request: emr_20160408_models.ListResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListResourcePoolResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['PoolType'] = request.pool_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListResourcePool',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListResourcePoolResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        request: emr_20160408_models.ListRolesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListRolesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['Limit'] = request.limit
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['CurrentSize'] = request.current_size
        query['PageCount'] = request.page_count
        query['OrderField'] = request.order_field
        query['OrderMode'] = request.order_mode
        query['ClusterBizId'] = request.cluster_biz_id
        query['HostGroupId'] = request.host_group_id
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['ScalingRuleName'] = request.scaling_rule_name
        query['HostGroupName'] = request.host_group_name
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListScalingActivityV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListScalingActivityV2Response(),
            self.call_api(params, req, runtime)
        )

    async def list_scaling_activity_v2with_options_async(
        self,
        request: emr_20160408_models.ListScalingActivityV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListScalingActivityV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['Limit'] = request.limit
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['CurrentSize'] = request.current_size
        query['PageCount'] = request.page_count
        query['OrderField'] = request.order_field
        query['OrderMode'] = request.order_mode
        query['ClusterBizId'] = request.cluster_biz_id
        query['HostGroupId'] = request.host_group_id
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['ScalingRuleName'] = request.scaling_rule_name
        query['HostGroupName'] = request.host_group_name
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListScalingActivityV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListScalingActivityV2Response(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['Limit'] = request.limit
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['CurrentSize'] = request.current_size
        query['PageCount'] = request.page_count
        query['OrderField'] = request.order_field
        query['OrderMode'] = request.order_mode
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['ConfigItemType'] = request.config_item_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListScalingConfigItemV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListScalingConfigItemV2Response(),
            self.call_api(params, req, runtime)
        )

    async def list_scaling_config_item_v2with_options_async(
        self,
        request: emr_20160408_models.ListScalingConfigItemV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListScalingConfigItemV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['Limit'] = request.limit
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['CurrentSize'] = request.current_size
        query['PageCount'] = request.page_count
        query['OrderField'] = request.order_field
        query['OrderMode'] = request.order_mode
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['ConfigItemType'] = request.config_item_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListScalingConfigItemV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListScalingConfigItemV2Response(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['Limit'] = request.limit
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['CurrentSize'] = request.current_size
        query['PageCount'] = request.page_count
        query['OrderField'] = request.order_field
        query['OrderMode'] = request.order_mode
        query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListScalingGroupV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListScalingGroupV2Response(),
            self.call_api(params, req, runtime)
        )

    async def list_scaling_group_v2with_options_async(
        self,
        request: emr_20160408_models.ListScalingGroupV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListScalingGroupV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['Limit'] = request.limit
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['CurrentSize'] = request.current_size
        query['PageCount'] = request.page_count
        query['OrderField'] = request.order_field
        query['OrderMode'] = request.order_mode
        query['ClusterBizId'] = request.cluster_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListScalingGroupV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListScalingGroupV2Response(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['NetType'] = request.net_type
        query['VpcId'] = request.vpc_id
        query['DepositType'] = request.deposit_type
        query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListSecurityGroup',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListSecurityGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_security_group_with_options_async(
        self,
        request: emr_20160408_models.ListSecurityGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListSecurityGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['NetType'] = request.net_type
        query['VpcId'] = request.vpc_id
        query['DepositType'] = request.deposit_type
        query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListSecurityGroup',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListSecurityGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['StackName'] = request.stack_name
        query['StackVersion'] = request.stack_version
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListStack',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_with_options_async(
        self,
        request: emr_20160408_models.ListStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListStackResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['StackName'] = request.stack_name
        query['StackVersion'] = request.stack_version
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListStack',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListStackResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['NextToken'] = request.next_token
        query['PageSize'] = request.page_size
        query['ResourceType'] = request.resource_type
        query['Category'] = request.category
        query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: emr_20160408_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['NextToken'] = request.next_token
        query['PageSize'] = request.page_size
        query['ResourceType'] = request.resource_type
        query['Category'] = request.category
        query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        query['NextToken'] = request.next_token
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: emr_20160408_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        query['NextToken'] = request.next_token
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Key'] = request.key
        query['NextToken'] = request.next_token
        query['PageSize'] = request.page_size
        query['ResourceType'] = request.resource_type
        query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: emr_20160408_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Key'] = request.key
        query['NextToken'] = request.next_token
        query['PageSize'] = request.page_size
        query['ResourceType'] = request.resource_type
        query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: emr_20160408_models.ListUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListUsersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['VpcId'] = request.vpc_id
        query['ZoneId'] = request.zone_id
        query['DepositType'] = request.deposit_type
        query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListVswitch',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListVswitchResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_vswitch_with_options_async(
        self,
        request: emr_20160408_models.ListVswitchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ListVswitchResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['VpcId'] = request.vpc_id
        query['ZoneId'] = request.zone_id
        query['DepositType'] = request.deposit_type
        query['ProductType'] = request.product_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListVswitch',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ListVswitchResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['Id'] = request.id
        query['BootstrapAction'] = request.bootstrap_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyClusterBootstrapAction',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyClusterBootstrapActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_bootstrap_action_with_options_async(
        self,
        request: emr_20160408_models.ModifyClusterBootstrapActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterBootstrapActionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['Id'] = request.id
        query['BootstrapAction'] = request.bootstrap_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyClusterBootstrapAction',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyClusterBootstrapActionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['HostGroupName'] = request.host_group_name
        query['SecurityGroupId'] = request.security_group_id
        query['VswitchId'] = request.vswitch_id
        query['Comment'] = request.comment
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyClusterHostGroup',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyClusterHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_host_group_with_options_async(
        self,
        request: emr_20160408_models.ModifyClusterHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterHostGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['HostGroupName'] = request.host_group_name
        query['SecurityGroupId'] = request.security_group_id
        query['VswitchId'] = request.vswitch_id
        query['Comment'] = request.comment
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyClusterHostGroup',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyClusterHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['SwitchOn'] = request.switch_on
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyClusterMetaCollect',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyClusterMetaCollectResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_meta_collect_with_options_async(
        self,
        request: emr_20160408_models.ModifyClusterMetaCollectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterMetaCollectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['SwitchOn'] = request.switch_on
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyClusterMetaCollect',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyClusterMetaCollectResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyClusterName',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyClusterNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_name_with_options_async(
        self,
        request: emr_20160408_models.ModifyClusterNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterNameResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyClusterName',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyClusterNameResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ModifyType'] = request.modify_type
        query['NicType'] = request.nic_type
        query['IpProtocol'] = request.ip_protocol
        query['PortRange'] = request.port_range
        query['WhiteIp'] = request.white_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyClusterSecurityGroupRule',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyClusterSecurityGroupRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_security_group_rule_with_options_async(
        self,
        request: emr_20160408_models.ModifyClusterSecurityGroupRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterSecurityGroupRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ModifyType'] = request.modify_type
        query['NicType'] = request.nic_type
        query['IpProtocol'] = request.ip_protocol
        query['PortRange'] = request.port_range
        query['WhiteIp'] = request.white_ip
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyClusterSecurityGroupRule',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyClusterSecurityGroupRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        query['Comment'] = request.comment
        query['ConfigParams'] = request.config_params
        query['CustomConfigParams'] = request.custom_config_params
        query['GroupId'] = request.group_id
        query['HostInstanceId'] = request.host_instance_id
        query['ConfigType'] = request.config_type
        query['RefreshHostConfig'] = request.refresh_host_config
        query['GatewayClusterIdList'] = request.gateway_cluster_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyClusterServiceConfig',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyClusterServiceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_service_config_with_options_async(
        self,
        request: emr_20160408_models.ModifyClusterServiceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterServiceConfigResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ServiceName'] = request.service_name
        query['Comment'] = request.comment
        query['ConfigParams'] = request.config_params
        query['CustomConfigParams'] = request.custom_config_params
        query['GroupId'] = request.group_id
        query['HostInstanceId'] = request.host_instance_id
        query['ConfigType'] = request.config_type
        query['RefreshHostConfig'] = request.refresh_host_config
        query['GatewayClusterIdList'] = request.gateway_cluster_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyClusterServiceConfig',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyClusterServiceConfigResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['BizId'] = request.biz_id
        query['TemplateName'] = request.template_name
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['LogPath'] = request.log_path
        query['SecurityGroupId'] = request.security_group_id
        query['IsOpenPublicIp'] = request.is_open_public_ip
        query['SecurityGroupName'] = request.security_group_name
        query['ChargeType'] = request.charge_type
        query['Period'] = request.period
        query['AutoRenew'] = request.auto_renew
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['NetType'] = request.net_type
        query['UserDefinedEmrEcsRole'] = request.user_defined_emr_ecs_role
        query['EmrVer'] = request.emr_ver
        query['ClusterType'] = request.cluster_type
        query['HighAvailabilityEnable'] = request.high_availability_enable
        query['UseLocalMetaDb'] = request.use_local_meta_db
        query['IoOptimized'] = request.io_optimized
        query['SshEnable'] = request.ssh_enable
        query['InstanceGeneration'] = request.instance_generation
        query['MasterPwd'] = request.master_pwd
        query['KeyPairName'] = request.key_pair_name
        query['MetaStoreType'] = request.meta_store_type
        query['MetaStoreConf'] = request.meta_store_conf
        query['Configurations'] = request.configurations
        query['EasEnable'] = request.eas_enable
        query['DepositType'] = request.deposit_type
        query['MachineType'] = request.machine_type
        query['UseCustomHiveMetaDb'] = request.use_custom_hive_meta_db
        query['InitCustomHiveMetaDb'] = request.init_custom_hive_meta_db
        query['ResourceGroupId'] = request.resource_group_id
        query['OptionSoftWareList'] = request.option_soft_ware_list
        query['HostGroup'] = request.host_group
        query['BootstrapAction'] = request.bootstrap_action
        query['Config'] = request.config
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyClusterTemplate',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyClusterTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_cluster_template_with_options_async(
        self,
        request: emr_20160408_models.ModifyClusterTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyClusterTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['BizId'] = request.biz_id
        query['TemplateName'] = request.template_name
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['LogPath'] = request.log_path
        query['SecurityGroupId'] = request.security_group_id
        query['IsOpenPublicIp'] = request.is_open_public_ip
        query['SecurityGroupName'] = request.security_group_name
        query['ChargeType'] = request.charge_type
        query['Period'] = request.period
        query['AutoRenew'] = request.auto_renew
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['NetType'] = request.net_type
        query['UserDefinedEmrEcsRole'] = request.user_defined_emr_ecs_role
        query['EmrVer'] = request.emr_ver
        query['ClusterType'] = request.cluster_type
        query['HighAvailabilityEnable'] = request.high_availability_enable
        query['UseLocalMetaDb'] = request.use_local_meta_db
        query['IoOptimized'] = request.io_optimized
        query['SshEnable'] = request.ssh_enable
        query['InstanceGeneration'] = request.instance_generation
        query['MasterPwd'] = request.master_pwd
        query['KeyPairName'] = request.key_pair_name
        query['MetaStoreType'] = request.meta_store_type
        query['MetaStoreConf'] = request.meta_store_conf
        query['Configurations'] = request.configurations
        query['EasEnable'] = request.eas_enable
        query['DepositType'] = request.deposit_type
        query['MachineType'] = request.machine_type
        query['UseCustomHiveMetaDb'] = request.use_custom_hive_meta_db
        query['InitCustomHiveMetaDb'] = request.init_custom_hive_meta_db
        query['ResourceGroupId'] = request.resource_group_id
        query['OptionSoftWareList'] = request.option_soft_ware_list
        query['HostGroup'] = request.host_group
        query['BootstrapAction'] = request.bootstrap_action
        query['Config'] = request.config
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyClusterTemplate',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyClusterTemplateResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClusterName'] = request.cluster_name
        query['ClusterId'] = request.cluster_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['LogEnable'] = request.log_enable
        query['LogPath'] = request.log_path
        query['SecurityGroupId'] = request.security_group_id
        query['IsOpenPublicIp'] = request.is_open_public_ip
        query['CreateClusterOnDemand'] = request.create_cluster_on_demand
        query['EmrVer'] = request.emr_ver
        query['ClusterType'] = request.cluster_type
        query['HighAvailabilityEnable'] = request.high_availability_enable
        query['UseLocalMetaDb'] = request.use_local_meta_db
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['NetType'] = request.net_type
        query['UserDefinedEmrEcsRole'] = request.user_defined_emr_ecs_role
        query['IoOptimized'] = request.io_optimized
        query['InstanceGeneration'] = request.instance_generation
        query['EasEnable'] = request.eas_enable
        query['WorkflowDefinition'] = request.workflow_definition
        query['UseCustomHiveMetaDB'] = request.use_custom_hive_meta_db
        query['InitCustomHiveMetaDB'] = request.init_custom_hive_meta_db
        query['Configurations'] = request.configurations
        query['Id'] = request.id
        query['ExecutionPlanVersion'] = request.execution_plan_version
        query['Name'] = request.name
        query['Strategy'] = request.strategy
        query['TimeInterval'] = request.time_interval
        query['StartTime'] = request.start_time
        query['TimeUnit'] = request.time_unit
        query['DayOfWeek'] = request.day_of_week
        query['DayOfMonth'] = request.day_of_month
        query['OptionSoftWareList'] = request.option_soft_ware_list
        query['EcsOrder'] = request.ecs_order
        query['BootstrapAction'] = request.bootstrap_action
        query['Config'] = request.config
        query['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyExecutionPlan',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyExecutionPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_execution_plan_with_options_async(
        self,
        request: emr_20160408_models.ModifyExecutionPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyExecutionPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['ClusterName'] = request.cluster_name
        query['ClusterId'] = request.cluster_id
        query['RegionId'] = request.region_id
        query['ZoneId'] = request.zone_id
        query['LogEnable'] = request.log_enable
        query['LogPath'] = request.log_path
        query['SecurityGroupId'] = request.security_group_id
        query['IsOpenPublicIp'] = request.is_open_public_ip
        query['CreateClusterOnDemand'] = request.create_cluster_on_demand
        query['EmrVer'] = request.emr_ver
        query['ClusterType'] = request.cluster_type
        query['HighAvailabilityEnable'] = request.high_availability_enable
        query['UseLocalMetaDb'] = request.use_local_meta_db
        query['VpcId'] = request.vpc_id
        query['VSwitchId'] = request.v_switch_id
        query['NetType'] = request.net_type
        query['UserDefinedEmrEcsRole'] = request.user_defined_emr_ecs_role
        query['IoOptimized'] = request.io_optimized
        query['InstanceGeneration'] = request.instance_generation
        query['EasEnable'] = request.eas_enable
        query['WorkflowDefinition'] = request.workflow_definition
        query['UseCustomHiveMetaDB'] = request.use_custom_hive_meta_db
        query['InitCustomHiveMetaDB'] = request.init_custom_hive_meta_db
        query['Configurations'] = request.configurations
        query['Id'] = request.id
        query['ExecutionPlanVersion'] = request.execution_plan_version
        query['Name'] = request.name
        query['Strategy'] = request.strategy
        query['TimeInterval'] = request.time_interval
        query['StartTime'] = request.start_time
        query['TimeUnit'] = request.time_unit
        query['DayOfWeek'] = request.day_of_week
        query['DayOfMonth'] = request.day_of_month
        query['OptionSoftWareList'] = request.option_soft_ware_list
        query['EcsOrder'] = request.ecs_order
        query['BootstrapAction'] = request.bootstrap_action
        query['Config'] = request.config
        query['JobIdList'] = request.job_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyExecutionPlan',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyExecutionPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Status'] = request.status
        query['Description'] = request.description
        query['Periodic'] = request.periodic
        query['StartSchedule'] = request.start_schedule
        query['EndSchedule'] = request.end_schedule
        query['CronExpr'] = request.cron_expr
        query['CreateCluster'] = request.create_cluster
        query['ClusterId'] = request.cluster_id
        query['HostName'] = request.host_name
        query['Namespace'] = request.namespace
        query['LogArchiveLocation'] = request.log_archive_location
        query['Lifecycle'] = request.lifecycle
        query['Application'] = request.application
        query['AlertConf'] = request.alert_conf
        query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        query['ParentFlowList'] = request.parent_flow_list
        query['ParentCategory'] = request.parent_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_with_options_async(
        self,
        request: emr_20160408_models.ModifyFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Status'] = request.status
        query['Description'] = request.description
        query['Periodic'] = request.periodic
        query['StartSchedule'] = request.start_schedule
        query['EndSchedule'] = request.end_schedule
        query['CronExpr'] = request.cron_expr
        query['CreateCluster'] = request.create_cluster
        query['ClusterId'] = request.cluster_id
        query['HostName'] = request.host_name
        query['Namespace'] = request.namespace
        query['LogArchiveLocation'] = request.log_archive_location
        query['Lifecycle'] = request.lifecycle
        query['Application'] = request.application
        query['AlertConf'] = request.alert_conf
        query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        query['ParentFlowList'] = request.parent_flow_list
        query['ParentCategory'] = request.parent_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['ParentId'] = request.parent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFlowCategory',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyFlowCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_category_with_options_async(
        self,
        request: emr_20160408_models.ModifyFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['ParentId'] = request.parent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFlowCategory',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyFlowCategoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Status'] = request.status
        query['Description'] = request.description
        query['Periodic'] = request.periodic
        query['StartSchedule'] = request.start_schedule
        query['EndSchedule'] = request.end_schedule
        query['CronExpr'] = request.cron_expr
        query['CreateCluster'] = request.create_cluster
        query['ClusterId'] = request.cluster_id
        query['HostName'] = request.host_name
        query['Namespace'] = request.namespace
        query['LogArchiveLocation'] = request.log_archive_location
        query['Lifecycle'] = request.lifecycle
        query['Graph'] = request.graph
        query['AlertConf'] = request.alert_conf
        query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        query['ParentFlowList'] = request.parent_flow_list
        query['ParentCategory'] = request.parent_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFlowForWeb',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyFlowForWebResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_for_web_with_options_async(
        self,
        request: emr_20160408_models.ModifyFlowForWebRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowForWebResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Status'] = request.status
        query['Description'] = request.description
        query['Periodic'] = request.periodic
        query['StartSchedule'] = request.start_schedule
        query['EndSchedule'] = request.end_schedule
        query['CronExpr'] = request.cron_expr
        query['CreateCluster'] = request.create_cluster
        query['ClusterId'] = request.cluster_id
        query['HostName'] = request.host_name
        query['Namespace'] = request.namespace
        query['LogArchiveLocation'] = request.log_archive_location
        query['Lifecycle'] = request.lifecycle
        query['Graph'] = request.graph
        query['AlertConf'] = request.alert_conf
        query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        query['ParentFlowList'] = request.parent_flow_list
        query['ParentCategory'] = request.parent_category
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFlowForWeb',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyFlowForWebResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Description'] = request.description
        query['FailAct'] = request.fail_act
        query['MaxRetry'] = request.max_retry
        query['RetryPolicy'] = request.retry_policy
        query['MaxRunningTimeSec'] = request.max_running_time_sec
        query['RetryInterval'] = request.retry_interval
        query['Params'] = request.params
        query['ParamConf'] = request.param_conf
        query['CustomVariables'] = request.custom_variables
        query['EnvConf'] = request.env_conf
        query['RunConf'] = request.run_conf
        query['MonitorConf'] = request.monitor_conf
        query['Mode'] = request.mode
        query['ClusterId'] = request.cluster_id
        query['AlertConf'] = request.alert_conf
        query['ResourceList'] = request.resource_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFlowJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyFlowJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_job_with_options_async(
        self,
        request: emr_20160408_models.ModifyFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Description'] = request.description
        query['FailAct'] = request.fail_act
        query['MaxRetry'] = request.max_retry
        query['RetryPolicy'] = request.retry_policy
        query['MaxRunningTimeSec'] = request.max_running_time_sec
        query['RetryInterval'] = request.retry_interval
        query['Params'] = request.params
        query['ParamConf'] = request.param_conf
        query['CustomVariables'] = request.custom_variables
        query['EnvConf'] = request.env_conf
        query['RunConf'] = request.run_conf
        query['MonitorConf'] = request.monitor_conf
        query['Mode'] = request.mode
        query['ClusterId'] = request.cluster_id
        query['AlertConf'] = request.alert_conf
        query['ResourceList'] = request.resource_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFlowJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyFlowJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Name'] = request.name
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFlowProject',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyFlowProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_project_with_options_async(
        self,
        request: emr_20160408_models.ModifyFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Name'] = request.name
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFlowProject',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyFlowProjectResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['ClusterId'] = request.cluster_id
        query['DefaultUser'] = request.default_user
        query['DefaultQueue'] = request.default_queue
        query['UserList'] = request.user_list
        query['QueueList'] = request.queue_list
        query['HostList'] = request.host_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFlowProjectClusterSetting',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyFlowProjectClusterSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_project_cluster_setting_with_options_async(
        self,
        request: emr_20160408_models.ModifyFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['ClusterId'] = request.cluster_id
        query['DefaultUser'] = request.default_user
        query['DefaultQueue'] = request.default_queue
        query['UserList'] = request.user_list
        query['QueueList'] = request.queue_list
        query['HostList'] = request.host_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyFlowProjectClusterSetting',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyFlowProjectClusterSettingResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['RegionId'] = request.region_id
        query['Type'] = request.type
        query['RunParameter'] = request.run_parameter
        query['FailAct'] = request.fail_act
        query['MaxRetry'] = request.max_retry
        query['RetryInterval'] = request.retry_interval
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_job_with_options_async(
        self,
        request: emr_20160408_models.ModifyJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['RegionId'] = request.region_id
        query['Type'] = request.type
        query['RunParameter'] = request.run_parameter
        query['FailAct'] = request.fail_act
        query['MaxRetry'] = request.max_retry
        query['RetryInterval'] = request.retry_interval
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Id'] = request.id
        query['Active'] = request.active
        query['Name'] = request.name
        query['ClusterId'] = request.cluster_id
        query['Yarnsiteconfig'] = request.yarnsiteconfig
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyResourcePool',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyResourcePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resource_pool_with_options_async(
        self,
        request: emr_20160408_models.ModifyResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyResourcePoolResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Id'] = request.id
        query['Active'] = request.active
        query['Name'] = request.name
        query['ClusterId'] = request.cluster_id
        query['Yarnsiteconfig'] = request.yarnsiteconfig
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyResourcePool',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyResourcePoolResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['SchedulerType'] = request.scheduler_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyResourcePoolSchedulerType',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyResourcePoolSchedulerTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resource_pool_scheduler_type_with_options_async(
        self,
        request: emr_20160408_models.ModifyResourcePoolSchedulerTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyResourcePoolSchedulerTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['SchedulerType'] = request.scheduler_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyResourcePoolSchedulerType',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyResourcePoolSchedulerTypeResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['QualifiedName'] = request.qualified_name
        query['ClusterId'] = request.cluster_id
        query['ParentQueueId'] = request.parent_queue_id
        query['Leaf'] = request.leaf
        query['ResourcePoolId'] = request.resource_pool_id
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyResourceQueue',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyResourceQueueResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_resource_queue_with_options_async(
        self,
        request: emr_20160408_models.ModifyResourceQueueRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyResourceQueueResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['QualifiedName'] = request.qualified_name
        query['ClusterId'] = request.cluster_id
        query['ParentQueueId'] = request.parent_queue_id
        query['Leaf'] = request.leaf
        query['ResourcePoolId'] = request.resource_pool_id
        query['Config'] = request.config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyResourceQueue',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyResourceQueueResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['ConfigItemBizId'] = request.config_item_biz_id
        query['ConfigItemType'] = request.config_item_type
        query['ConfigItemInformation'] = request.config_item_information
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyScalingConfigItemV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyScalingConfigItemV2Response(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_config_item_v2with_options_async(
        self,
        request: emr_20160408_models.ModifyScalingConfigItemV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyScalingConfigItemV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['ConfigItemBizId'] = request.config_item_biz_id
        query['ConfigItemType'] = request.config_item_type
        query['ConfigItemInformation'] = request.config_item_information
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyScalingConfigItemV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyScalingConfigItemV2Response(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['Name'] = request.name
        query['Description'] = request.description
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyScalingGroupV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyScalingGroupV2Response(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_group_v2with_options_async(
        self,
        request: emr_20160408_models.ModifyScalingGroupV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyScalingGroupV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['Name'] = request.name
        query['Description'] = request.description
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyScalingGroupV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyScalingGroupV2Response(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ScalingRuleId'] = request.scaling_rule_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['RuleName'] = request.rule_name
        query['AdjustmentType'] = request.adjustment_type
        query['AdjustmentValue'] = request.adjustment_value
        query['Cooldown'] = request.cooldown
        query['LaunchTime'] = request.launch_time
        query['LaunchExpirationTime'] = request.launch_expiration_time
        query['RecurrenceType'] = request.recurrence_type
        query['RecurrenceValue'] = request.recurrence_value
        query['RecurrenceEndTime'] = request.recurrence_end_time
        query['WithGrace'] = request.with_grace
        query['TimeoutWithGrace'] = request.timeout_with_grace
        query['SchedulerTrigger'] = request.scheduler_trigger
        query['CloudWatchTrigger'] = request.cloud_watch_trigger
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyScalingRule',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_rule_with_options_async(
        self,
        request: emr_20160408_models.ModifyScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyScalingRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ScalingRuleId'] = request.scaling_rule_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['RuleName'] = request.rule_name
        query['AdjustmentType'] = request.adjustment_type
        query['AdjustmentValue'] = request.adjustment_value
        query['Cooldown'] = request.cooldown
        query['LaunchTime'] = request.launch_time
        query['LaunchExpirationTime'] = request.launch_expiration_time
        query['RecurrenceType'] = request.recurrence_type
        query['RecurrenceValue'] = request.recurrence_value
        query['RecurrenceEndTime'] = request.recurrence_end_time
        query['WithGrace'] = request.with_grace
        query['TimeoutWithGrace'] = request.timeout_with_grace
        query['SchedulerTrigger'] = request.scheduler_trigger
        query['CloudWatchTrigger'] = request.cloud_watch_trigger
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyScalingRule',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['MinSize'] = request.min_size
        query['MaxSize'] = request.max_size
        query['DefaultCooldown'] = request.default_cooldown
        query['ActiveRuleCategory'] = request.active_rule_category
        query['WithGrace'] = request.with_grace
        query['TimeoutWithGrace'] = request.timeout_with_grace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyScalingTaskGroup',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyScalingTaskGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_scaling_task_group_with_options_async(
        self,
        request: emr_20160408_models.ModifyScalingTaskGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ModifyScalingTaskGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['MinSize'] = request.min_size
        query['MaxSize'] = request.max_size
        query['DefaultCooldown'] = request.default_cooldown
        query['ActiveRuleCategory'] = request.active_rule_category
        query['WithGrace'] = request.with_grace
        query['TimeoutWithGrace'] = request.timeout_with_grace
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyScalingTaskGroup',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ModifyScalingTaskGroupResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_entity_with_options(
        self,
        request: emr_20160408_models.QueryEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.QueryEntityResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Category'] = request.category
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryEntity',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.QueryEntityResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_entity_with_options_async(
        self,
        request: emr_20160408_models.QueryEntityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.QueryEntityResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Category'] = request.category
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryEntity',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.QueryEntityResponse(),
            await self.call_api_async(params, req, runtime)
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

    def query_tag_with_options(
        self,
        request: emr_20160408_models.QueryTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.QueryTagResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['EntityId'] = request.entity_id
        query['EntityType'] = request.entity_type
        query['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryTag',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.QueryTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_tag_with_options_async(
        self,
        request: emr_20160408_models.QueryTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.QueryTagResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['EntityId'] = request.entity_id
        query['EntityType'] = request.entity_type
        query['TagId'] = request.tag_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='QueryTag',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.QueryTagResponse(),
            await self.call_api_async(params, req, runtime)
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

    def refresh_cluster_resource_pool_with_options(
        self,
        request: emr_20160408_models.RefreshClusterResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RefreshClusterResourcePoolResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ResourcePoolId'] = request.resource_pool_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RefreshClusterResourcePool',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.RefreshClusterResourcePoolResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_cluster_resource_pool_with_options_async(
        self,
        request: emr_20160408_models.RefreshClusterResourcePoolRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RefreshClusterResourcePoolResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['ResourcePoolId'] = request.resource_pool_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RefreshClusterResourcePool',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.RefreshClusterResourcePoolResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['ForceRelease'] = request.force_release
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseCluster',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ReleaseClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_cluster_with_options_async(
        self,
        request: emr_20160408_models.ReleaseClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ReleaseClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['ForceRelease'] = request.force_release
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseCluster',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ReleaseClusterResponse(),
            await self.call_api_async(params, req, runtime)
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

    def release_cluster_host_group_with_options(
        self,
        request: emr_20160408_models.ReleaseClusterHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ReleaseClusterHostGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['InstanceIdList'] = request.instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseClusterHostGroup',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ReleaseClusterHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_cluster_host_group_with_options_async(
        self,
        request: emr_20160408_models.ReleaseClusterHostGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ReleaseClusterHostGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostGroupId'] = request.host_group_id
        query['InstanceIdList'] = request.instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ReleaseClusterHostGroup',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ReleaseClusterHostGroupResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['ConfigItemType'] = request.config_item_type
        query['ConfigItemBizId'] = request.config_item_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveScalingConfigItemV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.RemoveScalingConfigItemV2Response(),
            self.call_api(params, req, runtime)
        )

    async def remove_scaling_config_item_v2with_options_async(
        self,
        request: emr_20160408_models.RemoveScalingConfigItemV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RemoveScalingConfigItemV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['ConfigItemType'] = request.config_item_type
        query['ConfigItemBizId'] = request.config_item_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveScalingConfigItemV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.RemoveScalingConfigItemV2Response(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['FlowInstanceId'] = request.flow_instance_id
        query['ReRunFail'] = request.re_run_fail
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RerunFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.RerunFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def rerun_flow_with_options_async(
        self,
        request: emr_20160408_models.RerunFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RerunFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['FlowInstanceId'] = request.flow_instance_id
        query['ReRunFail'] = request.re_run_fail
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RerunFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.RerunFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['AutoPayOrder'] = request.auto_pay_order
        query['VswitchId'] = request.vswitch_id
        query['IsOpenPublicIp'] = request.is_open_public_ip
        query['HostComponentInfo'] = request.host_component_info
        query['HostGroup'] = request.host_group
        query['PromotionInfo'] = request.promotion_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResizeClusterV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ResizeClusterV2Response(),
            self.call_api(params, req, runtime)
        )

    async def resize_cluster_v2with_options_async(
        self,
        request: emr_20160408_models.ResizeClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ResizeClusterV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['AutoPayOrder'] = request.auto_pay_order
        query['VswitchId'] = request.vswitch_id
        query['IsOpenPublicIp'] = request.is_open_public_ip
        query['HostComponentInfo'] = request.host_component_info
        query['HostGroup'] = request.host_group
        query['PromotionInfo'] = request.promotion_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResizeClusterV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ResizeClusterV2Response(),
            await self.call_api_async(params, req, runtime)
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

    def resume_execution_plan_scheduler_with_options(
        self,
        request: emr_20160408_models.ResumeExecutionPlanSchedulerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ResumeExecutionPlanSchedulerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResumeExecutionPlanScheduler',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ResumeExecutionPlanSchedulerResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_execution_plan_scheduler_with_options_async(
        self,
        request: emr_20160408_models.ResumeExecutionPlanSchedulerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ResumeExecutionPlanSchedulerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResumeExecutionPlanScheduler',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ResumeExecutionPlanSchedulerResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['FlowInstanceId'] = request.flow_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResumeFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ResumeFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_flow_with_options_async(
        self,
        request: emr_20160408_models.ResumeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.ResumeFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['FlowInstanceId'] = request.flow_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ResumeFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.ResumeFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['OperationId'] = request.operation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RetryOperation',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.RetryOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_operation_with_options_async(
        self,
        request: emr_20160408_models.RetryOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RetryOperationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['OperationId'] = request.operation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RetryOperation',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.RetryOperationResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostIdList'] = request.host_id_list
        query['ServiceName'] = request.service_name
        query['ServiceActionName'] = request.service_action_name
        query['CustomCommand'] = request.custom_command
        query['ComponentNameList'] = request.component_name_list
        query['Comment'] = request.comment
        query['IsRolling'] = request.is_rolling
        query['ExecuteStrategy'] = request.execute_strategy
        query['CustomParams'] = request.custom_params
        query['Interval'] = request.interval
        query['NodeCountPerBatch'] = request.node_count_per_batch
        query['TotlerateFailCount'] = request.totlerate_fail_count
        query['OnlyRestartStaleConfigNodes'] = request.only_restart_stale_config_nodes
        query['TurnOnMaintenanceMode'] = request.turn_on_maintenance_mode
        query['HostGroupIdList'] = request.host_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RunClusterServiceAction',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.RunClusterServiceActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_cluster_service_action_with_options_async(
        self,
        request: emr_20160408_models.RunClusterServiceActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RunClusterServiceActionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostIdList'] = request.host_id_list
        query['ServiceName'] = request.service_name
        query['ServiceActionName'] = request.service_action_name
        query['CustomCommand'] = request.custom_command
        query['ComponentNameList'] = request.component_name_list
        query['Comment'] = request.comment
        query['IsRolling'] = request.is_rolling
        query['ExecuteStrategy'] = request.execute_strategy
        query['CustomParams'] = request.custom_params
        query['Interval'] = request.interval
        query['NodeCountPerBatch'] = request.node_count_per_batch
        query['TotlerateFailCount'] = request.totlerate_fail_count
        query['OnlyRestartStaleConfigNodes'] = request.only_restart_stale_config_nodes
        query['TurnOnMaintenanceMode'] = request.turn_on_maintenance_mode
        query['HostGroupIdList'] = request.host_group_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RunClusterServiceAction',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.RunClusterServiceActionResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['Arguments'] = request.arguments_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RunExecutionPlan',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.RunExecutionPlanResponse(),
            self.call_api(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['Arguments'] = request.arguments_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RunExecutionPlan',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.RunExecutionPlanResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ScalingActionType'] = request.scaling_action_type
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['ActionParam'] = request.action_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RunScalingActionV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.RunScalingActionV2Response(),
            self.call_api(params, req, runtime)
        )

    async def run_scaling_action_v2with_options_async(
        self,
        request: emr_20160408_models.RunScalingActionV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.RunScalingActionV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ScalingActionType'] = request.scaling_action_type
        query['ScalingGroupBizId'] = request.scaling_group_biz_id
        query['ActionParam'] = request.action_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RunScalingActionV2',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.RunScalingActionV2Response(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostInnerIp'] = request.host_inner_ip
        query['HostName'] = request.host_name
        query['LogstoreName'] = request.logstore_name
        query['FromTimestamp'] = request.from_timestamp
        query['ToTimestamp'] = request.to_timestamp
        query['SlsQueryString'] = request.sls_query_string
        query['Offset'] = request.offset
        query['Line'] = request.line
        query['Reverse'] = request.reverse
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchLog',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.SearchLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_log_with_options_async(
        self,
        request: emr_20160408_models.SearchLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.SearchLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ClusterId'] = request.cluster_id
        query['HostInnerIp'] = request.host_inner_ip
        query['HostName'] = request.host_name
        query['LogstoreName'] = request.logstore_name
        query['FromTimestamp'] = request.from_timestamp
        query['ToTimestamp'] = request.to_timestamp
        query['SlsQueryString'] = request.sls_query_string
        query['Offset'] = request.offset
        query['Line'] = request.line
        query['Reverse'] = request.reverse
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SearchLog',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.SearchLogResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['FlowInstanceId'] = request.flow_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.StartFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_flow_with_options_async(
        self,
        request: emr_20160408_models.StartFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.StartFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['FlowInstanceId'] = request.flow_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.StartFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['FlowId'] = request.flow_id
        query['Conf'] = request.conf
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.SubmitFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_flow_with_options_async(
        self,
        request: emr_20160408_models.SubmitFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.SubmitFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['FlowId'] = request.flow_id
        query['Conf'] = request.conf
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.SubmitFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['JobId'] = request.job_id
        query['JobInstanceId'] = request.job_instance_id
        query['ClusterId'] = request.cluster_id
        query['HostName'] = request.host_name
        query['Namespace'] = request.namespace
        query['Conf'] = request.conf
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitFlowJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.SubmitFlowJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_flow_job_with_options_async(
        self,
        request: emr_20160408_models.SubmitFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.SubmitFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['JobId'] = request.job_id
        query['JobInstanceId'] = request.job_instance_id
        query['ClusterId'] = request.cluster_id
        query['HostName'] = request.host_name
        query['Namespace'] = request.namespace
        query['Conf'] = request.conf
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SubmitFlowJob',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.SubmitFlowJobResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SuspendExecutionPlanScheduler',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.SuspendExecutionPlanSchedulerResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_execution_plan_scheduler_with_options_async(
        self,
        request: emr_20160408_models.SuspendExecutionPlanSchedulerRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.SuspendExecutionPlanSchedulerResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SuspendExecutionPlanScheduler',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.SuspendExecutionPlanSchedulerResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['FlowInstanceId'] = request.flow_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SuspendFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.SuspendFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_flow_with_options_async(
        self,
        request: emr_20160408_models.SuspendFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.SuspendFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['RegionId'] = request.region_id
        query['ProjectId'] = request.project_id
        query['FlowInstanceId'] = request.flow_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='SuspendFlow',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.SuspendFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: emr_20160408_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        query['ResourceId'] = request.resource_id
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def uninstall_libraries_with_options(
        self,
        request: emr_20160408_models.UninstallLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UninstallLibrariesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['LibraryBizId'] = request.library_biz_id
        query['ClusterBizIdList'] = request.cluster_biz_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UninstallLibraries',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.UninstallLibrariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_libraries_with_options_async(
        self,
        request: emr_20160408_models.UninstallLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UninstallLibrariesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['LibraryBizId'] = request.library_biz_id
        query['ClusterBizIdList'] = request.cluster_biz_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UninstallLibraries',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.UninstallLibrariesResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        query['All'] = request.all
        query['ResourceId'] = request.resource_id
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: emr_20160408_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['ResourceType'] = request.resource_type
        query['All'] = request.all
        query['ResourceId'] = request.resource_id
        query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_data_source_with_options(
        self,
        request: emr_20160408_models.UpdateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UpdateDataSourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Description'] = request.description
        query['Conf'] = request.conf
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDataSource',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.UpdateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_data_source_with_options_async(
        self,
        request: emr_20160408_models.UpdateDataSourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UpdateDataSourceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Description'] = request.description
        query['Conf'] = request.conf
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateDataSource',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.UpdateDataSourceResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['TaskBizId'] = request.task_biz_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateLibraryInstallTaskStatus',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.UpdateLibraryInstallTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_library_install_task_status_with_options_async(
        self,
        request: emr_20160408_models.UpdateLibraryInstallTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UpdateLibraryInstallTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['TaskBizId'] = request.task_biz_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateLibraryInstallTaskStatus',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.UpdateLibraryInstallTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Category'] = request.category
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateTag',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.UpdateTagResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tag_with_options_async(
        self,
        request: emr_20160408_models.UpdateTagRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UpdateTagResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['Id'] = request.id
        query['Name'] = request.name
        query['Category'] = request.category
        query['Description'] = request.description
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateTag',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.UpdateTagResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['AliyunUserId'] = request.aliyun_user_id
        query['UserName'] = request.user_name
        query['UserType'] = request.user_type
        query['Status'] = request.status
        query['Description'] = request.description
        query['RoleIdList'] = request.role_id_list
        query['GroupIdList'] = request.group_id_list
        query['UserAccountParamList'] = request.user_account_param_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: emr_20160408_models.UpdateUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> emr_20160408_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ResourceOwnerId'] = request.resource_owner_id
        query['RegionId'] = request.region_id
        query['AliyunUserId'] = request.aliyun_user_id
        query['UserName'] = request.user_name
        query['UserType'] = request.user_type
        query['Status'] = request.status
        query['Description'] = request.description
        query['RoleIdList'] = request.role_id_list
        query['GroupIdList'] = request.group_id_list
        query['UserAccountParamList'] = request.user_account_param_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2016-04-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20160408_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
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
