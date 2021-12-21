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

    def clone_flow_with_options(
        self,
        request: ddi_20200617_models.CloneFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CloneFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CloneFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_flow_with_options_async(
        self,
        request: ddi_20200617_models.CloneFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CloneFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CloneFlowResponse(),
            await self.call_api_async(params, req, runtime)
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

    def clone_flow_job_with_options(
        self,
        request: ddi_20200617_models.CloneFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CloneFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['Name'] = request.name
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneFlowJob',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CloneFlowJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def clone_flow_job_with_options_async(
        self,
        request: ddi_20200617_models.CloneFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CloneFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['Name'] = request.name
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloneFlowJob',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CloneFlowJobResponse(),
            await self.call_api_async(params, req, runtime)
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

    def commit_flow_entity_snapshot_with_options(
        self,
        request: ddi_20200617_models.CommitFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CommitFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EntityId'] = request.entity_id
        query['EntityType'] = request.entity_type
        query['Message'] = request.message
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CommitFlowEntitySnapshot',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CommitFlowEntitySnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def commit_flow_entity_snapshot_with_options_async(
        self,
        request: ddi_20200617_models.CommitFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CommitFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EntityId'] = request.entity_id
        query['EntityType'] = request.entity_type
        query['Message'] = request.message
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CommitFlowEntitySnapshot',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CommitFlowEntitySnapshotResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_cluster_v2with_options(
        self,
        request: ddi_20200617_models.CreateClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateClusterV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['AuthorizeContent'] = request.authorize_content
        query['Auto'] = request.auto
        query['AutoPayOrder'] = request.auto_pay_order
        query['BootstrapAction'] = request.bootstrap_action
        query['ChargeType'] = request.charge_type
        query['ClickHouseConf'] = request.click_house_conf
        query['ClientToken'] = request.client_token
        query['ClusterType'] = request.cluster_type
        query['Config'] = request.config
        query['Configurations'] = request.configurations
        query['DepositType'] = request.deposit_type
        query['EmrVer'] = request.emr_ver
        query['EnableEas'] = request.enable_eas
        query['EnableHighAvailability'] = request.enable_high_availability
        query['EnableSsh'] = request.enable_ssh
        query['ExtraAttributes'] = request.extra_attributes
        query['HostComponentInfo'] = request.host_component_info
        query['HostGroup'] = request.host_group
        query['InitCustomHiveMetaDB'] = request.init_custom_hive_meta_db
        query['InstanceGeneration'] = request.instance_generation
        query['IsOpenPublicIp'] = request.is_open_public_ip
        query['KeyPairName'] = request.key_pair_name
        query['LogPath'] = request.log_path
        query['MachineType'] = request.machine_type
        query['MasterPwd'] = request.master_pwd
        query['MetaStoreConf'] = request.meta_store_conf
        query['MetaStoreType'] = request.meta_store_type
        query['Name'] = request.name
        query['NetType'] = request.net_type
        query['Period'] = request.period
        query['PromotionInfo'] = request.promotion_info
        query['RegionId'] = request.region_id
        query['RelatedClusterId'] = request.related_cluster_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SecurityGroupId'] = request.security_group_id
        query['SecurityGroupName'] = request.security_group_name
        query['ServiceInfo'] = request.service_info
        query['Tag'] = request.tag
        query['UseCustomHiveMetaDB'] = request.use_custom_hive_meta_db
        query['UseLocalMetaDb'] = request.use_local_meta_db
        query['UserDefinedEmrEcsRole'] = request.user_defined_emr_ecs_role
        query['UserInfo'] = request.user_info
        query['VSwitchId'] = request.v_switch_id
        query['VpcId'] = request.vpc_id
        query['WhiteListType'] = request.white_list_type
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateClusterV2',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateClusterV2Response(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_v2with_options_async(
        self,
        request: ddi_20200617_models.CreateClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateClusterV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['AuthorizeContent'] = request.authorize_content
        query['Auto'] = request.auto
        query['AutoPayOrder'] = request.auto_pay_order
        query['BootstrapAction'] = request.bootstrap_action
        query['ChargeType'] = request.charge_type
        query['ClickHouseConf'] = request.click_house_conf
        query['ClientToken'] = request.client_token
        query['ClusterType'] = request.cluster_type
        query['Config'] = request.config
        query['Configurations'] = request.configurations
        query['DepositType'] = request.deposit_type
        query['EmrVer'] = request.emr_ver
        query['EnableEas'] = request.enable_eas
        query['EnableHighAvailability'] = request.enable_high_availability
        query['EnableSsh'] = request.enable_ssh
        query['ExtraAttributes'] = request.extra_attributes
        query['HostComponentInfo'] = request.host_component_info
        query['HostGroup'] = request.host_group
        query['InitCustomHiveMetaDB'] = request.init_custom_hive_meta_db
        query['InstanceGeneration'] = request.instance_generation
        query['IsOpenPublicIp'] = request.is_open_public_ip
        query['KeyPairName'] = request.key_pair_name
        query['LogPath'] = request.log_path
        query['MachineType'] = request.machine_type
        query['MasterPwd'] = request.master_pwd
        query['MetaStoreConf'] = request.meta_store_conf
        query['MetaStoreType'] = request.meta_store_type
        query['Name'] = request.name
        query['NetType'] = request.net_type
        query['Period'] = request.period
        query['PromotionInfo'] = request.promotion_info
        query['RegionId'] = request.region_id
        query['RelatedClusterId'] = request.related_cluster_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ResourceOwnerId'] = request.resource_owner_id
        query['SecurityGroupId'] = request.security_group_id
        query['SecurityGroupName'] = request.security_group_name
        query['ServiceInfo'] = request.service_info
        query['Tag'] = request.tag
        query['UseCustomHiveMetaDB'] = request.use_custom_hive_meta_db
        query['UseLocalMetaDb'] = request.use_local_meta_db
        query['UserDefinedEmrEcsRole'] = request.user_defined_emr_ecs_role
        query['UserInfo'] = request.user_info
        query['VSwitchId'] = request.v_switch_id
        query['VpcId'] = request.vpc_id
        query['WhiteListType'] = request.white_list_type
        query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateClusterV2',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateClusterV2Response(),
            await self.call_api_async(params, req, runtime)
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

    def create_flow_with_options(
        self,
        request: ddi_20200617_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlertConf'] = request.alert_conf
        query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        query['Application'] = request.application
        query['ClientToken'] = request.client_token
        query['ClusterId'] = request.cluster_id
        query['CreateCluster'] = request.create_cluster
        query['CronExpression'] = request.cron_expression
        query['Description'] = request.description
        query['EndSchedule'] = request.end_schedule
        query['HostName'] = request.host_name
        query['Name'] = request.name
        query['Namespace'] = request.namespace
        query['ParentCategory'] = request.parent_category
        query['ParentFlowList'] = request.parent_flow_list
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['StartSchedule'] = request.start_schedule
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_with_options_async(
        self,
        request: ddi_20200617_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlertConf'] = request.alert_conf
        query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        query['Application'] = request.application
        query['ClientToken'] = request.client_token
        query['ClusterId'] = request.cluster_id
        query['CreateCluster'] = request.create_cluster
        query['CronExpression'] = request.cron_expression
        query['Description'] = request.description
        query['EndSchedule'] = request.end_schedule
        query['HostName'] = request.host_name
        query['Name'] = request.name
        query['Namespace'] = request.namespace
        query['ParentCategory'] = request.parent_category
        query['ParentFlowList'] = request.parent_flow_list
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['StartSchedule'] = request.start_schedule
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_flow_category_with_options(
        self,
        request: ddi_20200617_models.CreateFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['Name'] = request.name
        query['ParentId'] = request.parent_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowCategory',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_category_with_options_async(
        self,
        request: ddi_20200617_models.CreateFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['Name'] = request.name
        query['ParentId'] = request.parent_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowCategory',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowCategoryResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_flow_edit_lock_with_options(
        self,
        request: ddi_20200617_models.CreateFlowEditLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowEditLockResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EntityId'] = request.entity_id
        query['Force'] = request.force
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowEditLock',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowEditLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_edit_lock_with_options_async(
        self,
        request: ddi_20200617_models.CreateFlowEditLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowEditLockResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EntityId'] = request.entity_id
        query['Force'] = request.force
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowEditLock',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowEditLockResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_flow_job_with_options(
        self,
        request: ddi_20200617_models.CreateFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Adhoc'] = request.adhoc
        query['AlertConf'] = request.alert_conf
        query['ClientToken'] = request.client_token
        query['ClusterId'] = request.cluster_id
        query['CustomVariables'] = request.custom_variables
        query['Description'] = request.description
        query['EnvConf'] = request.env_conf
        query['FailAct'] = request.fail_act
        query['Mode'] = request.mode
        query['MonitorConf'] = request.monitor_conf
        query['Name'] = request.name
        query['ParamConf'] = request.param_conf
        query['Params'] = request.params
        query['ParentCategory'] = request.parent_category
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['ResourceList'] = request.resource_list
        query['RetryPolicy'] = request.retry_policy
        query['RunConf'] = request.run_conf
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowJob',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_job_with_options_async(
        self,
        request: ddi_20200617_models.CreateFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Adhoc'] = request.adhoc
        query['AlertConf'] = request.alert_conf
        query['ClientToken'] = request.client_token
        query['ClusterId'] = request.cluster_id
        query['CustomVariables'] = request.custom_variables
        query['Description'] = request.description
        query['EnvConf'] = request.env_conf
        query['FailAct'] = request.fail_act
        query['Mode'] = request.mode
        query['MonitorConf'] = request.monitor_conf
        query['Name'] = request.name
        query['ParamConf'] = request.param_conf
        query['Params'] = request.params
        query['ParentCategory'] = request.parent_category
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['ResourceList'] = request.resource_list
        query['RetryPolicy'] = request.retry_policy
        query['RunConf'] = request.run_conf
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowJob',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowJobResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_flow_project_with_options(
        self,
        request: ddi_20200617_models.CreateFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['Name'] = request.name
        query['ProductType'] = request.product_type
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowProject',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_project_with_options_async(
        self,
        request: ddi_20200617_models.CreateFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['Description'] = request.description
        query['Name'] = request.name
        query['ProductType'] = request.product_type
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowProject',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowProjectResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_flow_project_cluster_setting_with_options(
        self,
        request: ddi_20200617_models.CreateFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['ClusterId'] = request.cluster_id
        query['DefaultQueue'] = request.default_queue
        query['DefaultUser'] = request.default_user
        query['HostList'] = request.host_list
        query['ProjectId'] = request.project_id
        query['QueueList'] = request.queue_list
        query['RegionId'] = request.region_id
        query['UserList'] = request.user_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowProjectClusterSetting',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowProjectClusterSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_project_cluster_setting_with_options_async(
        self,
        request: ddi_20200617_models.CreateFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['ClusterId'] = request.cluster_id
        query['DefaultQueue'] = request.default_queue
        query['DefaultUser'] = request.default_user
        query['HostList'] = request.host_list
        query['ProjectId'] = request.project_id
        query['QueueList'] = request.queue_list
        query['RegionId'] = request.region_id
        query['UserList'] = request.user_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowProjectClusterSetting',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowProjectClusterSettingResponse(),
            await self.call_api_async(params, req, runtime)
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

    def create_flow_project_user_with_options(
        self,
        request: ddi_20200617_models.CreateFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowProjectUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowProjectUser',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowProjectUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_flow_project_user_with_options_async(
        self,
        request: ddi_20200617_models.CreateFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowProjectUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClientToken'] = request.client_token
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['User'] = request.user
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFlowProjectUser',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.CreateFlowProjectUserResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_flow_with_options(
        self,
        request: ddi_20200617_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_with_options_async(
        self,
        request: ddi_20200617_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_flow_category_with_options(
        self,
        request: ddi_20200617_models.DeleteFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlowCategory',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_category_with_options_async(
        self,
        request: ddi_20200617_models.DeleteFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlowCategory',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowCategoryResponse(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['EntityId'] = request.entity_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlowEditLock',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowEditLockResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_edit_lock_with_options_async(
        self,
        request: ddi_20200617_models.DeleteFlowEditLockRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowEditLockResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EntityId'] = request.entity_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlowEditLock',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowEditLockResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_flow_project_with_options(
        self,
        request: ddi_20200617_models.DeleteFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlowProject',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_project_with_options_async(
        self,
        request: ddi_20200617_models.DeleteFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlowProject',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowProjectResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_flow_project_cluster_setting_with_options(
        self,
        request: ddi_20200617_models.DeleteFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlowProjectClusterSetting',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowProjectClusterSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_project_cluster_setting_with_options_async(
        self,
        request: ddi_20200617_models.DeleteFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlowProjectClusterSetting',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowProjectClusterSettingResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_flow_project_user_with_options(
        self,
        request: ddi_20200617_models.DeleteFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowProjectUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlowProjectUser',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowProjectUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_flow_project_user_with_options_async(
        self,
        request: ddi_20200617_models.DeleteFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowProjectUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFlowProjectUser',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DeleteFlowProjectUserResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_cluster_v2with_options(
        self,
        request: ddi_20200617_models.DescribeClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeClusterV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterV2',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeClusterV2Response(),
            self.call_api(params, req, runtime)
        )

    async def describe_cluster_v2with_options_async(
        self,
        request: ddi_20200617_models.DescribeClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeClusterV2Response:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterV2',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeClusterV2Response(),
            await self.call_api_async(params, req, runtime)
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
        query = {}
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_flow_category_tree_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowCategoryTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowCategoryTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CategoryId'] = request.category_id
        query['Keyword'] = request.keyword
        query['Mode'] = request.mode
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowCategoryTree',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowCategoryTreeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_category_tree_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowCategoryTreeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowCategoryTreeResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CategoryId'] = request.category_id
        query['Keyword'] = request.keyword
        query['Mode'] = request.mode
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowCategoryTree',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowCategoryTreeResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_flow_instance_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowInstance',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_instance_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowInstance',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_flow_job_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowJob',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_job_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowJob',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowJobResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_flow_node_instance_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowNodeInstance',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowNodeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_node_instance_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowNodeInstance',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowNodeInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_flow_node_instance_container_log_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceContainerLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceContainerLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ContainerId'] = request.container_id
        query['Length'] = request.length
        query['LogName'] = request.log_name
        query['NodeInstanceId'] = request.node_instance_id
        query['Offset'] = request.offset
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowNodeInstanceContainerLog',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowNodeInstanceContainerLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_node_instance_container_log_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceContainerLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceContainerLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ContainerId'] = request.container_id
        query['Length'] = request.length
        query['LogName'] = request.log_name
        query['NodeInstanceId'] = request.node_instance_id
        query['Offset'] = request.offset
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowNodeInstanceContainerLog',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowNodeInstanceContainerLogResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_flow_node_instance_launcher_log_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceLauncherLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceLauncherLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['Length'] = request.length
        query['Lines'] = request.lines
        query['NodeInstanceId'] = request.node_instance_id
        query['Offset'] = request.offset
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Reverse'] = request.reverse
        query['Start'] = request.start
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowNodeInstanceLauncherLog',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowNodeInstanceLauncherLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_node_instance_launcher_log_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowNodeInstanceLauncherLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowNodeInstanceLauncherLogResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EndTime'] = request.end_time
        query['Length'] = request.length
        query['Lines'] = request.lines
        query['NodeInstanceId'] = request.node_instance_id
        query['Offset'] = request.offset
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Reverse'] = request.reverse
        query['Start'] = request.start
        query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowNodeInstanceLauncherLog',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowNodeInstanceLauncherLogResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_flow_project_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowProject',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_project_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowProject',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowProjectResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_flow_project_cluster_setting_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowProjectClusterSetting',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowProjectClusterSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_project_cluster_setting_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowProjectClusterSetting',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowProjectClusterSettingResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_flow_slawith_options(
        self,
        request: ddi_20200617_models.DescribeFlowSLARequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowSLAResponse:
        UtilClient.validate_model(request)
        query = {}
        query['From'] = request.from_
        query['Metrics'] = request.metrics
        query['PeriodType'] = request.period_type
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ResourceOwnerId'] = request.resource_owner_id
        query['To'] = request.to
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowSLA',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowSLAResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_slawith_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowSLARequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowSLAResponse:
        UtilClient.validate_model(request)
        query = {}
        query['From'] = request.from_
        query['Metrics'] = request.metrics
        query['PeriodType'] = request.period_type
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ResourceOwnerId'] = request.resource_owner_id
        query['To'] = request.to
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowSLA',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowSLAResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_sla(
        self,
        request: ddi_20200617_models.DescribeFlowSLARequest,
    ) -> ddi_20200617_models.DescribeFlowSLAResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_slawith_options(request, runtime)

    async def describe_flow_sla_async(
        self,
        request: ddi_20200617_models.DescribeFlowSLARequest,
    ) -> ddi_20200617_models.DescribeFlowSLAResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_slawith_options_async(request, runtime)

    def describe_flow_variable_collection_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowVariableCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowVariableCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EntityId'] = request.entity_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowVariableCollection',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowVariableCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_flow_variable_collection_with_options_async(
        self,
        request: ddi_20200617_models.DescribeFlowVariableCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowVariableCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EntityId'] = request.entity_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFlowVariableCollection',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.DescribeFlowVariableCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_flow_variable_collection(
        self,
        request: ddi_20200617_models.DescribeFlowVariableCollectionRequest,
    ) -> ddi_20200617_models.DescribeFlowVariableCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_variable_collection_with_options(request, runtime)

    async def describe_flow_variable_collection_async(
        self,
        request: ddi_20200617_models.DescribeFlowVariableCollectionRequest,
    ) -> ddi_20200617_models.DescribeFlowVariableCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_variable_collection_with_options_async(request, runtime)

    def get_flow_audit_logs_with_options(
        self,
        request: ddi_20200617_models.GetFlowAuditLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.GetFlowAuditLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentSize'] = request.current_size
        query['EntityGroupId'] = request.entity_group_id
        query['EntityId'] = request.entity_id
        query['EntityType'] = request.entity_type
        query['Limit'] = request.limit
        query['Operation'] = request.operation
        query['OperatorId'] = request.operator_id
        query['OrderField'] = request.order_field
        query['OrderMode'] = request.order_mode
        query['PageCount'] = request.page_count
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFlowAuditLogs',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.GetFlowAuditLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_flow_audit_logs_with_options_async(
        self,
        request: ddi_20200617_models.GetFlowAuditLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.GetFlowAuditLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CurrentSize'] = request.current_size
        query['EntityGroupId'] = request.entity_group_id
        query['EntityId'] = request.entity_id
        query['EntityType'] = request.entity_type
        query['Limit'] = request.limit
        query['Operation'] = request.operation
        query['OperatorId'] = request.operator_id
        query['OrderField'] = request.order_field
        query['OrderMode'] = request.order_mode
        query['PageCount'] = request.page_count
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFlowAuditLogs',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.GetFlowAuditLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_flow_audit_logs(
        self,
        request: ddi_20200617_models.GetFlowAuditLogsRequest,
    ) -> ddi_20200617_models.GetFlowAuditLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_flow_audit_logs_with_options(request, runtime)

    async def get_flow_audit_logs_async(
        self,
        request: ddi_20200617_models.GetFlowAuditLogsRequest,
    ) -> ddi_20200617_models.GetFlowAuditLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_flow_audit_logs_with_options_async(request, runtime)

    def kill_flow_with_options(
        self,
        request: ddi_20200617_models.KillFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.KillFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FlowInstanceId'] = request.flow_instance_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KillFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.KillFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_flow_with_options_async(
        self,
        request: ddi_20200617_models.KillFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.KillFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FlowInstanceId'] = request.flow_instance_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KillFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.KillFlowResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_flow(
        self,
        request: ddi_20200617_models.KillFlowRequest,
    ) -> ddi_20200617_models.KillFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.kill_flow_with_options(request, runtime)

    async def kill_flow_async(
        self,
        request: ddi_20200617_models.KillFlowRequest,
    ) -> ddi_20200617_models.KillFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.kill_flow_with_options_async(request, runtime)

    def kill_flow_job_with_options(
        self,
        request: ddi_20200617_models.KillFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.KillFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobInstanceId'] = request.job_instance_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KillFlowJob',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.KillFlowJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_flow_job_with_options_async(
        self,
        request: ddi_20200617_models.KillFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.KillFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['JobInstanceId'] = request.job_instance_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KillFlowJob',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.KillFlowJobResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_clusters_with_options(
        self,
        request: ddi_20200617_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterTypeList'] = request.cluster_type_list
        query['CreateType'] = request.create_type
        query['DefaultStatus'] = request.default_status
        query['DepositType'] = request.deposit_type
        query['ExpiredTagList'] = request.expired_tag_list
        query['IsDesc'] = request.is_desc
        query['MachineType'] = request.machine_type
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StatusList'] = request.status_list
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        request: ddi_20200617_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListClustersResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterTypeList'] = request.cluster_type_list
        query['CreateType'] = request.create_type
        query['DefaultStatus'] = request.default_status
        query['DepositType'] = request.deposit_type
        query['ExpiredTagList'] = request.expired_tag_list
        query['IsDesc'] = request.is_desc
        query['MachineType'] = request.machine_type
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        query['ResourceOwnerId'] = request.resource_owner_id
        query['StatusList'] = request.status_list
        query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_flow_with_options(
        self,
        request: ddi_20200617_models.ListFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Id'] = request.id
        query['JobId'] = request.job_id
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Periodic'] = request.periodic
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Id'] = request.id
        query['JobId'] = request.job_id
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Periodic'] = request.periodic
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_flow_cluster_with_options(
        self,
        request: ddi_20200617_models.ListFlowClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowCluster',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_cluster_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowCluster',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_flow_cluster_all_with_options(
        self,
        request: ddi_20200617_models.ListFlowClusterAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowClusterAllResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProductType'] = request.product_type
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowClusterAll',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterAllResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_cluster_all_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowClusterAllRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowClusterAllResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ProductType'] = request.product_type
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowClusterAll',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterAllResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_flow_cluster_all_hosts_with_options(
        self,
        request: ddi_20200617_models.ListFlowClusterAllHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowClusterAllHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowClusterAllHosts',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterAllHostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_cluster_all_hosts_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowClusterAllHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowClusterAllHostsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowClusterAllHosts',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterAllHostsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_flow_cluster_host_with_options(
        self,
        request: ddi_20200617_models.ListFlowClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowClusterHostResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowClusterHost',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterHostResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_cluster_host_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowClusterHostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowClusterHostResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowClusterHost',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowClusterHostResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_flow_entity_snapshot_with_options(
        self,
        request: ddi_20200617_models.ListFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CommitterId'] = request.committer_id
        query['CurrentSize'] = request.current_size
        query['EntityGroupId'] = request.entity_group_id
        query['EntityId'] = request.entity_id
        query['EntityType'] = request.entity_type
        query['Limit'] = request.limit
        query['OrderField'] = request.order_field
        query['OrderMode'] = request.order_mode
        query['PageCount'] = request.page_count
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Revision'] = request.revision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowEntitySnapshot',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowEntitySnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_entity_snapshot_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CommitterId'] = request.committer_id
        query['CurrentSize'] = request.current_size
        query['EntityGroupId'] = request.entity_group_id
        query['EntityId'] = request.entity_id
        query['EntityType'] = request.entity_type
        query['Limit'] = request.limit
        query['OrderField'] = request.order_field
        query['OrderMode'] = request.order_mode
        query['PageCount'] = request.page_count
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Revision'] = request.revision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowEntitySnapshot',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowEntitySnapshotResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_flow_instance_with_options(
        self,
        request: ddi_20200617_models.ListFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FlowId'] = request.flow_id
        query['FlowName'] = request.flow_name
        query['Id'] = request.id
        query['InstanceId'] = request.instance_id
        query['OrderBy'] = request.order_by
        query['OrderType'] = request.order_type
        query['Owner'] = request.owner
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['StatusList'] = request.status_list
        query['TimeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowInstance',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_instance_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FlowId'] = request.flow_id
        query['FlowName'] = request.flow_name
        query['Id'] = request.id
        query['InstanceId'] = request.instance_id
        query['OrderBy'] = request.order_by
        query['OrderType'] = request.order_type
        query['Owner'] = request.owner
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['StatusList'] = request.status_list
        query['TimeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowInstance',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_flow_job_history_with_options(
        self,
        request: ddi_20200617_models.ListFlowJobHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowJobHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['InstanceId'] = request.instance_id
        query['JobType'] = request.job_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['StatusList'] = request.status_list
        query['TimeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowJobHistory',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowJobHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_job_history_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowJobHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowJobHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['InstanceId'] = request.instance_id
        query['JobType'] = request.job_type
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['StatusList'] = request.status_list
        query['TimeRange'] = request.time_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowJobHistory',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowJobHistoryResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_flow_jobs_with_options(
        self,
        request: ddi_20200617_models.ListFlowJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Adhoc'] = request.adhoc
        query['Id'] = request.id
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowJobs',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_jobs_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Adhoc'] = request.adhoc
        query['Id'] = request.id
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowJobs',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowJobsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_flow_node_instance_container_status_with_options(
        self,
        request: ddi_20200617_models.ListFlowNodeInstanceContainerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowNodeInstanceContainerStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['NodeInstanceId'] = request.node_instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowNodeInstanceContainerStatus',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowNodeInstanceContainerStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_node_instance_container_status_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowNodeInstanceContainerStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowNodeInstanceContainerStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        query['NodeInstanceId'] = request.node_instance_id
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowNodeInstanceContainerStatus',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowNodeInstanceContainerStatusResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_flow_node_sql_result_with_options(
        self,
        request: ddi_20200617_models.ListFlowNodeSqlResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowNodeSqlResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Length'] = request.length
        query['NodeInstanceId'] = request.node_instance_id
        query['Offset'] = request.offset
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['SqlIndex'] = request.sql_index
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowNodeSqlResult',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowNodeSqlResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_node_sql_result_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowNodeSqlResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowNodeSqlResultResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Length'] = request.length
        query['NodeInstanceId'] = request.node_instance_id
        query['Offset'] = request.offset
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['SqlIndex'] = request.sql_index
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowNodeSqlResult',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowNodeSqlResultResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_flow_project_cluster_setting_with_options(
        self,
        request: ddi_20200617_models.ListFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowProjectClusterSetting',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowProjectClusterSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_project_cluster_setting_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowProjectClusterSetting',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowProjectClusterSettingResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_flow_project_user_with_options(
        self,
        request: ddi_20200617_models.ListFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowProjectUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowProjectUser',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowProjectUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_project_user_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowProjectUserResponse:
        UtilClient.validate_model(request)
        query = {}
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowProjectUser',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowProjectUserResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_flow_projects_with_options(
        self,
        request: ddi_20200617_models.ListFlowProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProductType'] = request.product_type
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowProjects',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowProjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flow_projects_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowProjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowProjectsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['ProductType'] = request.product_type
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlowProjects',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowProjectsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_flows_with_options(
        self,
        request: ddi_20200617_models.ListFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Id'] = request.id
        query['JobId'] = request.job_id
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Periodic'] = request.periodic
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlows',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_flows_with_options_async(
        self,
        request: ddi_20200617_models.ListFlowsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowsResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Id'] = request.id
        query['JobId'] = request.job_id
        query['Name'] = request.name
        query['PageNumber'] = request.page_number
        query['PageSize'] = request.page_size
        query['Periodic'] = request.periodic
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFlows',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListFlowsResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_main_versions_with_options(
        self,
        request: ddi_20200617_models.ListMainVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListMainVersionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMainVersions',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListMainVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_main_versions_with_options_async(
        self,
        request: ddi_20200617_models.ListMainVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListMainVersionsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMainVersions',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ListMainVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_main_versions(
        self,
        request: ddi_20200617_models.ListMainVersionsRequest,
    ) -> ddi_20200617_models.ListMainVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_main_versions_with_options(request, runtime)

    async def list_main_versions_async(
        self,
        request: ddi_20200617_models.ListMainVersionsRequest,
    ) -> ddi_20200617_models.ListMainVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_main_versions_with_options_async(request, runtime)

    def modify_flow_with_options(
        self,
        request: ddi_20200617_models.ModifyFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlertConf'] = request.alert_conf
        query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        query['Application'] = request.application
        query['ClusterId'] = request.cluster_id
        query['CreateCluster'] = request.create_cluster
        query['CronExpr'] = request.cron_expr
        query['Description'] = request.description
        query['EndSchedule'] = request.end_schedule
        query['HostName'] = request.host_name
        query['Id'] = request.id
        query['Name'] = request.name
        query['ParentCategory'] = request.parent_category
        query['ParentFlowList'] = request.parent_flow_list
        query['Periodic'] = request.periodic
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['StartSchedule'] = request.start_schedule
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_with_options_async(
        self,
        request: ddi_20200617_models.ModifyFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlertConf'] = request.alert_conf
        query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        query['Application'] = request.application
        query['ClusterId'] = request.cluster_id
        query['CreateCluster'] = request.create_cluster
        query['CronExpr'] = request.cron_expr
        query['Description'] = request.description
        query['EndSchedule'] = request.end_schedule
        query['HostName'] = request.host_name
        query['Id'] = request.id
        query['Name'] = request.name
        query['ParentCategory'] = request.parent_category
        query['ParentFlowList'] = request.parent_flow_list
        query['Periodic'] = request.periodic
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['StartSchedule'] = request.start_schedule
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_flow_category_with_options(
        self,
        request: ddi_20200617_models.ModifyFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['Name'] = request.name
        query['ParentId'] = request.parent_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlowCategory',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_category_with_options_async(
        self,
        request: ddi_20200617_models.ModifyFlowCategoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowCategoryResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Id'] = request.id
        query['Name'] = request.name
        query['ParentId'] = request.parent_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlowCategory',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowCategoryResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_flow_for_web_with_options(
        self,
        request: ddi_20200617_models.ModifyFlowForWebRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowForWebResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlertConf'] = request.alert_conf
        query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        query['ClusterId'] = request.cluster_id
        query['CreateCluster'] = request.create_cluster
        query['CronExpr'] = request.cron_expr
        query['Description'] = request.description
        query['EndSchedule'] = request.end_schedule
        query['Graph'] = request.graph
        query['HostName'] = request.host_name
        query['Id'] = request.id
        query['Name'] = request.name
        query['Namespace'] = request.namespace
        query['ParentCategory'] = request.parent_category
        query['ParentFlowList'] = request.parent_flow_list
        query['Periodic'] = request.periodic
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['StartSchedule'] = request.start_schedule
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlowForWeb',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowForWebResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_for_web_with_options_async(
        self,
        request: ddi_20200617_models.ModifyFlowForWebRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowForWebResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlertConf'] = request.alert_conf
        query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        query['ClusterId'] = request.cluster_id
        query['CreateCluster'] = request.create_cluster
        query['CronExpr'] = request.cron_expr
        query['Description'] = request.description
        query['EndSchedule'] = request.end_schedule
        query['Graph'] = request.graph
        query['HostName'] = request.host_name
        query['Id'] = request.id
        query['Name'] = request.name
        query['Namespace'] = request.namespace
        query['ParentCategory'] = request.parent_category
        query['ParentFlowList'] = request.parent_flow_list
        query['Periodic'] = request.periodic
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['StartSchedule'] = request.start_schedule
        query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlowForWeb',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowForWebResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_flow_job_with_options(
        self,
        request: ddi_20200617_models.ModifyFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlertConf'] = request.alert_conf
        query['ClusterId'] = request.cluster_id
        query['CustomVariables'] = request.custom_variables
        query['Description'] = request.description
        query['EnvConf'] = request.env_conf
        query['FailAct'] = request.fail_act
        query['Id'] = request.id
        query['KnoxPassword'] = request.knox_password
        query['KnoxUser'] = request.knox_user
        query['Mode'] = request.mode
        query['MonitorConf'] = request.monitor_conf
        query['Name'] = request.name
        query['ParamConf'] = request.param_conf
        query['Params'] = request.params
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['ResourceList'] = request.resource_list
        query['RetryPolicy'] = request.retry_policy
        query['RunConf'] = request.run_conf
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlowJob',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_job_with_options_async(
        self,
        request: ddi_20200617_models.ModifyFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['AlertConf'] = request.alert_conf
        query['ClusterId'] = request.cluster_id
        query['CustomVariables'] = request.custom_variables
        query['Description'] = request.description
        query['EnvConf'] = request.env_conf
        query['FailAct'] = request.fail_act
        query['Id'] = request.id
        query['KnoxPassword'] = request.knox_password
        query['KnoxUser'] = request.knox_user
        query['Mode'] = request.mode
        query['MonitorConf'] = request.monitor_conf
        query['Name'] = request.name
        query['ParamConf'] = request.param_conf
        query['Params'] = request.params
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        query['ResourceList'] = request.resource_list
        query['RetryPolicy'] = request.retry_policy
        query['RunConf'] = request.run_conf
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlowJob',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowJobResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_flow_project_with_options(
        self,
        request: ddi_20200617_models.ModifyFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['Name'] = request.name
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlowProject',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowProjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_project_with_options_async(
        self,
        request: ddi_20200617_models.ModifyFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Description'] = request.description
        query['Name'] = request.name
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlowProject',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowProjectResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_flow_project_cluster_setting_with_options(
        self,
        request: ddi_20200617_models.ModifyFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['DefaultQueue'] = request.default_queue
        query['DefaultUser'] = request.default_user
        query['HostList'] = request.host_list
        query['ProjectId'] = request.project_id
        query['QueueList'] = request.queue_list
        query['RegionId'] = request.region_id
        query['UserList'] = request.user_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlowProjectClusterSetting',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowProjectClusterSettingResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_project_cluster_setting_with_options_async(
        self,
        request: ddi_20200617_models.ModifyFlowProjectClusterSettingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowProjectClusterSettingResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['DefaultQueue'] = request.default_queue
        query['DefaultUser'] = request.default_user
        query['HostList'] = request.host_list
        query['ProjectId'] = request.project_id
        query['QueueList'] = request.queue_list
        query['RegionId'] = request.region_id
        query['UserList'] = request.user_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlowProjectClusterSetting',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowProjectClusterSettingResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_flow_variable_collection_with_options(
        self,
        request: ddi_20200617_models.ModifyFlowVariableCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowVariableCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Data'] = request.data
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlowVariableCollection',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowVariableCollectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_flow_variable_collection_with_options_async(
        self,
        request: ddi_20200617_models.ModifyFlowVariableCollectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowVariableCollectionResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Data'] = request.data
        query['RegionId'] = request.region_id
        query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyFlowVariableCollection',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ModifyFlowVariableCollectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_flow_variable_collection(
        self,
        request: ddi_20200617_models.ModifyFlowVariableCollectionRequest,
    ) -> ddi_20200617_models.ModifyFlowVariableCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_variable_collection_with_options(request, runtime)

    async def modify_flow_variable_collection_async(
        self,
        request: ddi_20200617_models.ModifyFlowVariableCollectionRequest,
    ) -> ddi_20200617_models.ModifyFlowVariableCollectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_variable_collection_with_options_async(request, runtime)

    def release_cluster_with_options(
        self,
        request: ddi_20200617_models.ReleaseClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ReleaseClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ForceRelease'] = request.force_release
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseCluster',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ReleaseClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_cluster_with_options_async(
        self,
        request: ddi_20200617_models.ReleaseClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ReleaseClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ForceRelease'] = request.force_release
        query['Id'] = request.id
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseCluster',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ReleaseClusterResponse(),
            await self.call_api_async(params, req, runtime)
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

    def rerun_flow_with_options(
        self,
        request: ddi_20200617_models.RerunFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.RerunFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FlowInstanceId'] = request.flow_instance_id
        query['ProjectId'] = request.project_id
        query['ReRunFail'] = request.re_run_fail
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RerunFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.RerunFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def rerun_flow_with_options_async(
        self,
        request: ddi_20200617_models.RerunFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.RerunFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FlowInstanceId'] = request.flow_instance_id
        query['ProjectId'] = request.project_id
        query['ReRunFail'] = request.re_run_fail
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RerunFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.RerunFlowResponse(),
            await self.call_api_async(params, req, runtime)
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

    def restore_flow_entity_snapshot_with_options(
        self,
        request: ddi_20200617_models.RestoreFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.RestoreFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EntityId'] = request.entity_id
        query['EntityType'] = request.entity_type
        query['OperatorId'] = request.operator_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Revision'] = request.revision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreFlowEntitySnapshot',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.RestoreFlowEntitySnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def restore_flow_entity_snapshot_with_options_async(
        self,
        request: ddi_20200617_models.RestoreFlowEntitySnapshotRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.RestoreFlowEntitySnapshotResponse:
        UtilClient.validate_model(request)
        query = {}
        query['EntityId'] = request.entity_id
        query['EntityType'] = request.entity_type
        query['OperatorId'] = request.operator_id
        query['RegionId'] = request.region_id
        query['ResourceOwnerId'] = request.resource_owner_id
        query['Revision'] = request.revision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestoreFlowEntitySnapshot',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.RestoreFlowEntitySnapshotResponse(),
            await self.call_api_async(params, req, runtime)
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

    def resume_flow_with_options(
        self,
        request: ddi_20200617_models.ResumeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ResumeFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FlowInstanceId'] = request.flow_instance_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ResumeFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_flow_with_options_async(
        self,
        request: ddi_20200617_models.ResumeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ResumeFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FlowInstanceId'] = request.flow_instance_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.ResumeFlowResponse(),
            await self.call_api_async(params, req, runtime)
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

    def start_flow_with_options(
        self,
        request: ddi_20200617_models.StartFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.StartFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FlowInstanceId'] = request.flow_instance_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.StartFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_flow_with_options_async(
        self,
        request: ddi_20200617_models.StartFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.StartFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FlowInstanceId'] = request.flow_instance_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.StartFlowResponse(),
            await self.call_api_async(params, req, runtime)
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

    def submit_flow_with_options(
        self,
        request: ddi_20200617_models.SubmitFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.SubmitFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Conf'] = request.conf
        query['FlowId'] = request.flow_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.SubmitFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_flow_with_options_async(
        self,
        request: ddi_20200617_models.SubmitFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.SubmitFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['Conf'] = request.conf
        query['FlowId'] = request.flow_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.SubmitFlowResponse(),
            await self.call_api_async(params, req, runtime)
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

    def submit_flow_job_with_options(
        self,
        request: ddi_20200617_models.SubmitFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.SubmitFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Conf'] = request.conf
        query['HostName'] = request.host_name
        query['JobId'] = request.job_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitFlowJob',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.SubmitFlowJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def submit_flow_job_with_options_async(
        self,
        request: ddi_20200617_models.SubmitFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.SubmitFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ClusterId'] = request.cluster_id
        query['Conf'] = request.conf
        query['HostName'] = request.host_name
        query['JobId'] = request.job_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitFlowJob',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.SubmitFlowJobResponse(),
            await self.call_api_async(params, req, runtime)
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

    def suspend_flow_with_options(
        self,
        request: ddi_20200617_models.SuspendFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.SuspendFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FlowInstanceId'] = request.flow_instance_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.SuspendFlowResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_flow_with_options_async(
        self,
        request: ddi_20200617_models.SuspendFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.SuspendFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        query['FlowInstanceId'] = request.flow_instance_id
        query['ProjectId'] = request.project_id
        query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendFlow',
            version='2020-06-17',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ddi_20200617_models.SuspendFlowResponse(),
            await self.call_api_async(params, req, runtime)
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
