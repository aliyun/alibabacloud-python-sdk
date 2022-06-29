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

    def clone_flow_job_with_options(
        self,
        request: ddi_20200617_models.CloneFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CloneFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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

    def create_cluster_v2with_options(
        self,
        request: ddi_20200617_models.CreateClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateClusterV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorize_content):
            query['AuthorizeContent'] = request.authorize_content
        if not UtilClient.is_unset(request.auto):
            query['Auto'] = request.auto
        if not UtilClient.is_unset(request.auto_pay_order):
            query['AutoPayOrder'] = request.auto_pay_order
        if not UtilClient.is_unset(request.bootstrap_action):
            query['BootstrapAction'] = request.bootstrap_action
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.click_house_conf):
            query['ClickHouseConf'] = request.click_house_conf
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.configurations):
            query['Configurations'] = request.configurations
        if not UtilClient.is_unset(request.deposit_type):
            query['DepositType'] = request.deposit_type
        if not UtilClient.is_unset(request.emr_ver):
            query['EmrVer'] = request.emr_ver
        if not UtilClient.is_unset(request.enable_eas):
            query['EnableEas'] = request.enable_eas
        if not UtilClient.is_unset(request.enable_high_availability):
            query['EnableHighAvailability'] = request.enable_high_availability
        if not UtilClient.is_unset(request.enable_ssh):
            query['EnableSsh'] = request.enable_ssh
        if not UtilClient.is_unset(request.extra_attributes):
            query['ExtraAttributes'] = request.extra_attributes
        if not UtilClient.is_unset(request.host_component_info):
            query['HostComponentInfo'] = request.host_component_info
        if not UtilClient.is_unset(request.host_group):
            query['HostGroup'] = request.host_group
        if not UtilClient.is_unset(request.init_custom_hive_meta_db):
            query['InitCustomHiveMetaDB'] = request.init_custom_hive_meta_db
        if not UtilClient.is_unset(request.instance_generation):
            query['InstanceGeneration'] = request.instance_generation
        if not UtilClient.is_unset(request.is_open_public_ip):
            query['IsOpenPublicIp'] = request.is_open_public_ip
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.log_path):
            query['LogPath'] = request.log_path
        if not UtilClient.is_unset(request.machine_type):
            query['MachineType'] = request.machine_type
        if not UtilClient.is_unset(request.master_pwd):
            query['MasterPwd'] = request.master_pwd
        if not UtilClient.is_unset(request.meta_store_conf):
            query['MetaStoreConf'] = request.meta_store_conf
        if not UtilClient.is_unset(request.meta_store_type):
            query['MetaStoreType'] = request.meta_store_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.promotion_info):
            query['PromotionInfo'] = request.promotion_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.related_cluster_id):
            query['RelatedClusterId'] = request.related_cluster_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_name):
            query['SecurityGroupName'] = request.security_group_name
        if not UtilClient.is_unset(request.service_info):
            query['ServiceInfo'] = request.service_info
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.use_custom_hive_meta_db):
            query['UseCustomHiveMetaDB'] = request.use_custom_hive_meta_db
        if not UtilClient.is_unset(request.use_local_meta_db):
            query['UseLocalMetaDb'] = request.use_local_meta_db
        if not UtilClient.is_unset(request.user_defined_emr_ecs_role):
            query['UserDefinedEmrEcsRole'] = request.user_defined_emr_ecs_role
        if not UtilClient.is_unset(request.user_info):
            query['UserInfo'] = request.user_info
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.white_list_type):
            query['WhiteListType'] = request.white_list_type
        if not UtilClient.is_unset(request.zone_id):
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
        if not UtilClient.is_unset(request.authorize_content):
            query['AuthorizeContent'] = request.authorize_content
        if not UtilClient.is_unset(request.auto):
            query['Auto'] = request.auto
        if not UtilClient.is_unset(request.auto_pay_order):
            query['AutoPayOrder'] = request.auto_pay_order
        if not UtilClient.is_unset(request.bootstrap_action):
            query['BootstrapAction'] = request.bootstrap_action
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.click_house_conf):
            query['ClickHouseConf'] = request.click_house_conf
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.configurations):
            query['Configurations'] = request.configurations
        if not UtilClient.is_unset(request.deposit_type):
            query['DepositType'] = request.deposit_type
        if not UtilClient.is_unset(request.emr_ver):
            query['EmrVer'] = request.emr_ver
        if not UtilClient.is_unset(request.enable_eas):
            query['EnableEas'] = request.enable_eas
        if not UtilClient.is_unset(request.enable_high_availability):
            query['EnableHighAvailability'] = request.enable_high_availability
        if not UtilClient.is_unset(request.enable_ssh):
            query['EnableSsh'] = request.enable_ssh
        if not UtilClient.is_unset(request.extra_attributes):
            query['ExtraAttributes'] = request.extra_attributes
        if not UtilClient.is_unset(request.host_component_info):
            query['HostComponentInfo'] = request.host_component_info
        if not UtilClient.is_unset(request.host_group):
            query['HostGroup'] = request.host_group
        if not UtilClient.is_unset(request.init_custom_hive_meta_db):
            query['InitCustomHiveMetaDB'] = request.init_custom_hive_meta_db
        if not UtilClient.is_unset(request.instance_generation):
            query['InstanceGeneration'] = request.instance_generation
        if not UtilClient.is_unset(request.is_open_public_ip):
            query['IsOpenPublicIp'] = request.is_open_public_ip
        if not UtilClient.is_unset(request.key_pair_name):
            query['KeyPairName'] = request.key_pair_name
        if not UtilClient.is_unset(request.log_path):
            query['LogPath'] = request.log_path
        if not UtilClient.is_unset(request.machine_type):
            query['MachineType'] = request.machine_type
        if not UtilClient.is_unset(request.master_pwd):
            query['MasterPwd'] = request.master_pwd
        if not UtilClient.is_unset(request.meta_store_conf):
            query['MetaStoreConf'] = request.meta_store_conf
        if not UtilClient.is_unset(request.meta_store_type):
            query['MetaStoreType'] = request.meta_store_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.promotion_info):
            query['PromotionInfo'] = request.promotion_info
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.related_cluster_id):
            query['RelatedClusterId'] = request.related_cluster_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.security_group_name):
            query['SecurityGroupName'] = request.security_group_name
        if not UtilClient.is_unset(request.service_info):
            query['ServiceInfo'] = request.service_info
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.use_custom_hive_meta_db):
            query['UseCustomHiveMetaDB'] = request.use_custom_hive_meta_db
        if not UtilClient.is_unset(request.use_local_meta_db):
            query['UseLocalMetaDb'] = request.use_local_meta_db
        if not UtilClient.is_unset(request.user_defined_emr_ecs_role):
            query['UserDefinedEmrEcsRole'] = request.user_defined_emr_ecs_role
        if not UtilClient.is_unset(request.user_info):
            query['UserInfo'] = request.user_info
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.white_list_type):
            query['WhiteListType'] = request.white_list_type
        if not UtilClient.is_unset(request.zone_id):
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
        if not UtilClient.is_unset(request.alert_conf):
            query['AlertConf'] = request.alert_conf
        if not UtilClient.is_unset(request.alert_ding_ding_group_biz_id):
            query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        if not UtilClient.is_unset(request.alert_user_group_biz_id):
            query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        if not UtilClient.is_unset(request.application):
            query['Application'] = request.application
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.create_cluster):
            query['CreateCluster'] = request.create_cluster
        if not UtilClient.is_unset(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_schedule):
            query['EndSchedule'] = request.end_schedule
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.parent_category):
            query['ParentCategory'] = request.parent_category
        if not UtilClient.is_unset(request.parent_flow_list):
            query['ParentFlowList'] = request.parent_flow_list
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_schedule):
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
        if not UtilClient.is_unset(request.alert_conf):
            query['AlertConf'] = request.alert_conf
        if not UtilClient.is_unset(request.alert_ding_ding_group_biz_id):
            query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        if not UtilClient.is_unset(request.alert_user_group_biz_id):
            query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        if not UtilClient.is_unset(request.application):
            query['Application'] = request.application
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.create_cluster):
            query['CreateCluster'] = request.create_cluster
        if not UtilClient.is_unset(request.cron_expression):
            query['CronExpression'] = request.cron_expression
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_schedule):
            query['EndSchedule'] = request.end_schedule
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.parent_category):
            query['ParentCategory'] = request.parent_category
        if not UtilClient.is_unset(request.parent_flow_list):
            query['ParentFlowList'] = request.parent_flow_list
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_schedule):
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
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
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
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
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

    def create_flow_job_with_options(
        self,
        request: ddi_20200617_models.CreateFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.adhoc):
            query['Adhoc'] = request.adhoc
        if not UtilClient.is_unset(request.alert_conf):
            query['AlertConf'] = request.alert_conf
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.custom_variables):
            query['CustomVariables'] = request.custom_variables
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.env_conf):
            query['EnvConf'] = request.env_conf
        if not UtilClient.is_unset(request.fail_act):
            query['FailAct'] = request.fail_act
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.monitor_conf):
            query['MonitorConf'] = request.monitor_conf
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.param_conf):
            query['ParamConf'] = request.param_conf
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.parent_category):
            query['ParentCategory'] = request.parent_category
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_list):
            query['ResourceList'] = request.resource_list
        if not UtilClient.is_unset(request.retry_policy):
            query['RetryPolicy'] = request.retry_policy
        if not UtilClient.is_unset(request.run_conf):
            query['RunConf'] = request.run_conf
        if not UtilClient.is_unset(request.type):
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
        if not UtilClient.is_unset(request.adhoc):
            query['Adhoc'] = request.adhoc
        if not UtilClient.is_unset(request.alert_conf):
            query['AlertConf'] = request.alert_conf
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.custom_variables):
            query['CustomVariables'] = request.custom_variables
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.env_conf):
            query['EnvConf'] = request.env_conf
        if not UtilClient.is_unset(request.fail_act):
            query['FailAct'] = request.fail_act
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.monitor_conf):
            query['MonitorConf'] = request.monitor_conf
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.param_conf):
            query['ParamConf'] = request.param_conf
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.parent_category):
            query['ParentCategory'] = request.parent_category
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_list):
            query['ResourceList'] = request.resource_list
        if not UtilClient.is_unset(request.retry_policy):
            query['RetryPolicy'] = request.retry_policy
        if not UtilClient.is_unset(request.run_conf):
            query['RunConf'] = request.run_conf
        if not UtilClient.is_unset(request.type):
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
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
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
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
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

    def create_flow_project_user_with_options(
        self,
        request: ddi_20200617_models.CreateFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateFlowProjectUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user):
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
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user):
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

    def create_library_with_options(
        self,
        request: ddi_20200617_models.CreateLibraryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateLibraryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.library_version):
            query['LibraryVersion'] = request.library_version
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.properties):
            query['Properties'] = request.properties
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.source_location):
            query['SourceLocation'] = request.source_location
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLibrary',
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
            ddi_20200617_models.CreateLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_library_with_options_async(
        self,
        request: ddi_20200617_models.CreateLibraryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.CreateLibraryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.library_version):
            query['LibraryVersion'] = request.library_version
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.properties):
            query['Properties'] = request.properties
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.source_location):
            query['SourceLocation'] = request.source_location
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLibrary',
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
            ddi_20200617_models.CreateLibraryResponse(),
            await self.call_api_async(params, req, runtime)
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

    def delete_flow_with_options(
        self,
        request: ddi_20200617_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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

    def delete_flow_project_with_options(
        self,
        request: ddi_20200617_models.DeleteFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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

    def delete_flow_project_user_with_options(
        self,
        request: ddi_20200617_models.DeleteFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteFlowProjectUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_name):
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
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_name):
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

    def delete_libraries_with_options(
        self,
        request: ddi_20200617_models.DeleteLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteLibrariesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.library_biz_id_list):
            query['LibraryBizIdList'] = request.library_biz_id_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLibraries',
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
            ddi_20200617_models.DeleteLibrariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_libraries_with_options_async(
        self,
        request: ddi_20200617_models.DeleteLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DeleteLibrariesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.library_biz_id_list):
            query['LibraryBizIdList'] = request.library_biz_id_list
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLibraries',
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
            ddi_20200617_models.DeleteLibrariesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_cluster_v2with_options(
        self,
        request: ddi_20200617_models.DescribeClusterV2Request,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeClusterV2Response:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
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
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
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
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
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
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
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

    def describe_flow_job_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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

    def describe_flow_project_with_options(
        self,
        request: ddi_20200617_models.DescribeFlowProjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeFlowProjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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

    def describe_library_detail_with_options(
        self,
        request: ddi_20200617_models.DescribeLibraryDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeLibraryDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.library_biz_id):
            query['LibraryBizId'] = request.library_biz_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLibraryDetail',
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
            ddi_20200617_models.DescribeLibraryDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_library_detail_with_options_async(
        self,
        request: ddi_20200617_models.DescribeLibraryDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeLibraryDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.library_biz_id):
            query['LibraryBizId'] = request.library_biz_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLibraryDetail',
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
            ddi_20200617_models.DescribeLibraryDetailResponse(),
            await self.call_api_async(params, req, runtime)
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

    def describe_library_install_task_detail_with_options(
        self,
        request: ddi_20200617_models.DescribeLibraryInstallTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeLibraryInstallTaskDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_biz_id):
            query['TaskBizId'] = request.task_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLibraryInstallTaskDetail',
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
            ddi_20200617_models.DescribeLibraryInstallTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_library_install_task_detail_with_options_async(
        self,
        request: ddi_20200617_models.DescribeLibraryInstallTaskDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.DescribeLibraryInstallTaskDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.task_biz_id):
            query['TaskBizId'] = request.task_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLibraryInstallTaskDetail',
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
            ddi_20200617_models.DescribeLibraryInstallTaskDetailResponse(),
            await self.call_api_async(params, req, runtime)
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

    def install_libraries_with_options(
        self,
        request: ddi_20200617_models.InstallLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.InstallLibrariesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id_list):
            query['ClusterBizIdList'] = request.cluster_biz_id_list
        if not UtilClient.is_unset(request.library_biz_id):
            query['LibraryBizId'] = request.library_biz_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallLibraries',
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
            ddi_20200617_models.InstallLibrariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_libraries_with_options_async(
        self,
        request: ddi_20200617_models.InstallLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.InstallLibrariesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id_list):
            query['ClusterBizIdList'] = request.cluster_biz_id_list
        if not UtilClient.is_unset(request.library_biz_id):
            query['LibraryBizId'] = request.library_biz_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallLibraries',
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
            ddi_20200617_models.InstallLibrariesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def kill_flow_job_with_options(
        self,
        request: ddi_20200617_models.KillFlowJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.KillFlowJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_instance_id):
            query['JobInstanceId'] = request.job_instance_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.job_instance_id):
            query['JobInstanceId'] = request.job_instance_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.cluster_type_list):
            query['ClusterTypeList'] = request.cluster_type_list
        if not UtilClient.is_unset(request.create_type):
            query['CreateType'] = request.create_type
        if not UtilClient.is_unset(request.default_status):
            query['DefaultStatus'] = request.default_status
        if not UtilClient.is_unset(request.deposit_type):
            query['DepositType'] = request.deposit_type
        if not UtilClient.is_unset(request.expired_tag_list):
            query['ExpiredTagList'] = request.expired_tag_list
        if not UtilClient.is_unset(request.is_desc):
            query['IsDesc'] = request.is_desc
        if not UtilClient.is_unset(request.machine_type):
            query['MachineType'] = request.machine_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.tag):
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
        if not UtilClient.is_unset(request.cluster_type_list):
            query['ClusterTypeList'] = request.cluster_type_list
        if not UtilClient.is_unset(request.create_type):
            query['CreateType'] = request.create_type
        if not UtilClient.is_unset(request.default_status):
            query['DefaultStatus'] = request.default_status
        if not UtilClient.is_unset(request.deposit_type):
            query['DepositType'] = request.deposit_type
        if not UtilClient.is_unset(request.expired_tag_list):
            query['ExpiredTagList'] = request.expired_tag_list
        if not UtilClient.is_unset(request.is_desc):
            query['IsDesc'] = request.is_desc
        if not UtilClient.is_unset(request.machine_type):
            query['MachineType'] = request.machine_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.tag):
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
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.periodic):
            query['Periodic'] = request.periodic
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
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
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.periodic):
            query['Periodic'] = request.periodic
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
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

    def list_flow_job_history_with_options(
        self,
        request: ddi_20200617_models.ListFlowJobHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowJobHistoryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.time_range):
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
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status_list):
            query['StatusList'] = request.status_list
        if not UtilClient.is_unset(request.time_range):
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
        if not UtilClient.is_unset(request.adhoc):
            query['Adhoc'] = request.adhoc
        if not UtilClient.is_unset(request.exact_name):
            query['ExactName'] = request.exact_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
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
        if not UtilClient.is_unset(request.adhoc):
            query['Adhoc'] = request.adhoc
        if not UtilClient.is_unset(request.exact_name):
            query['ExactName'] = request.exact_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
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

    def list_flow_project_user_with_options(
        self,
        request: ddi_20200617_models.ListFlowProjectUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListFlowProjectUserResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
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
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
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

    def list_libraries_with_options(
        self,
        request: ddi_20200617_models.ListLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListLibrariesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.current_size):
            query['CurrentSize'] = request.current_size
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_field):
            query['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.order_mode):
            query['OrderMode'] = request.order_mode
        if not UtilClient.is_unset(request.page_count):
            query['PageCount'] = request.page_count
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLibraries',
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
            ddi_20200617_models.ListLibrariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_libraries_with_options_async(
        self,
        request: ddi_20200617_models.ListLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListLibrariesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.current_size):
            query['CurrentSize'] = request.current_size
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_field):
            query['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.order_mode):
            query['OrderMode'] = request.order_mode
        if not UtilClient.is_unset(request.page_count):
            query['PageCount'] = request.page_count
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLibraries',
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
            ddi_20200617_models.ListLibrariesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_library_install_tasks_with_options(
        self,
        request: ddi_20200617_models.ListLibraryInstallTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListLibraryInstallTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.current_size):
            query['CurrentSize'] = request.current_size
        if not UtilClient.is_unset(request.library_biz_id):
            query['LibraryBizId'] = request.library_biz_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_field):
            query['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.order_mode):
            query['OrderMode'] = request.order_mode
        if not UtilClient.is_unset(request.page_count):
            query['PageCount'] = request.page_count
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLibraryInstallTasks',
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
            ddi_20200617_models.ListLibraryInstallTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_library_install_tasks_with_options_async(
        self,
        request: ddi_20200617_models.ListLibraryInstallTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListLibraryInstallTasksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.current_size):
            query['CurrentSize'] = request.current_size
        if not UtilClient.is_unset(request.library_biz_id):
            query['LibraryBizId'] = request.library_biz_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_field):
            query['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.order_mode):
            query['OrderMode'] = request.order_mode
        if not UtilClient.is_unset(request.page_count):
            query['PageCount'] = request.page_count
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLibraryInstallTasks',
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
            ddi_20200617_models.ListLibraryInstallTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_library_install_tasks(
        self,
        request: ddi_20200617_models.ListLibraryInstallTasksRequest,
    ) -> ddi_20200617_models.ListLibraryInstallTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_library_install_tasks_with_options(request, runtime)

    async def list_library_install_tasks_async(
        self,
        request: ddi_20200617_models.ListLibraryInstallTasksRequest,
    ) -> ddi_20200617_models.ListLibraryInstallTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_library_install_tasks_with_options_async(request, runtime)

    def list_library_status_with_options(
        self,
        request: ddi_20200617_models.ListLibraryStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListLibraryStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.current_size):
            query['CurrentSize'] = request.current_size
        if not UtilClient.is_unset(request.library_biz_id):
            query['LibraryBizId'] = request.library_biz_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_field):
            query['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.order_mode):
            query['OrderMode'] = request.order_mode
        if not UtilClient.is_unset(request.page_count):
            query['PageCount'] = request.page_count
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLibraryStatus',
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
            ddi_20200617_models.ListLibraryStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_library_status_with_options_async(
        self,
        request: ddi_20200617_models.ListLibraryStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListLibraryStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id):
            query['ClusterBizId'] = request.cluster_biz_id
        if not UtilClient.is_unset(request.current_size):
            query['CurrentSize'] = request.current_size
        if not UtilClient.is_unset(request.library_biz_id):
            query['LibraryBizId'] = request.library_biz_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_field):
            query['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.order_mode):
            query['OrderMode'] = request.order_mode
        if not UtilClient.is_unset(request.page_count):
            query['PageCount'] = request.page_count
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLibraryStatus',
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
            ddi_20200617_models.ListLibraryStatusResponse(),
            await self.call_api_async(params, req, runtime)
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

    def list_tag_resources_with_options(
        self,
        request: ddi_20200617_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
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
            ddi_20200617_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ddi_20200617_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
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
            ddi_20200617_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def modify_flow_for_web_with_options(
        self,
        request: ddi_20200617_models.ModifyFlowForWebRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ModifyFlowForWebResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_conf):
            query['AlertConf'] = request.alert_conf
        if not UtilClient.is_unset(request.alert_ding_ding_group_biz_id):
            query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        if not UtilClient.is_unset(request.alert_user_group_biz_id):
            query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.create_cluster):
            query['CreateCluster'] = request.create_cluster
        if not UtilClient.is_unset(request.cron_expr):
            query['CronExpr'] = request.cron_expr
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_schedule):
            query['EndSchedule'] = request.end_schedule
        if not UtilClient.is_unset(request.graph):
            query['Graph'] = request.graph
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.parent_category):
            query['ParentCategory'] = request.parent_category
        if not UtilClient.is_unset(request.parent_flow_list):
            query['ParentFlowList'] = request.parent_flow_list
        if not UtilClient.is_unset(request.periodic):
            query['Periodic'] = request.periodic
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_schedule):
            query['StartSchedule'] = request.start_schedule
        if not UtilClient.is_unset(request.status):
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
        if not UtilClient.is_unset(request.alert_conf):
            query['AlertConf'] = request.alert_conf
        if not UtilClient.is_unset(request.alert_ding_ding_group_biz_id):
            query['AlertDingDingGroupBizId'] = request.alert_ding_ding_group_biz_id
        if not UtilClient.is_unset(request.alert_user_group_biz_id):
            query['AlertUserGroupBizId'] = request.alert_user_group_biz_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.create_cluster):
            query['CreateCluster'] = request.create_cluster
        if not UtilClient.is_unset(request.cron_expr):
            query['CronExpr'] = request.cron_expr
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_schedule):
            query['EndSchedule'] = request.end_schedule
        if not UtilClient.is_unset(request.graph):
            query['Graph'] = request.graph
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.namespace):
            query['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.parent_category):
            query['ParentCategory'] = request.parent_category
        if not UtilClient.is_unset(request.parent_flow_list):
            query['ParentFlowList'] = request.parent_flow_list
        if not UtilClient.is_unset(request.periodic):
            query['Periodic'] = request.periodic
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_schedule):
            query['StartSchedule'] = request.start_schedule
        if not UtilClient.is_unset(request.status):
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
        if not UtilClient.is_unset(request.alert_conf):
            query['AlertConf'] = request.alert_conf
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.custom_variables):
            query['CustomVariables'] = request.custom_variables
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.env_conf):
            query['EnvConf'] = request.env_conf
        if not UtilClient.is_unset(request.fail_act):
            query['FailAct'] = request.fail_act
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.knox_password):
            query['KnoxPassword'] = request.knox_password
        if not UtilClient.is_unset(request.knox_user):
            query['KnoxUser'] = request.knox_user
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.monitor_conf):
            query['MonitorConf'] = request.monitor_conf
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.param_conf):
            query['ParamConf'] = request.param_conf
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_list):
            query['ResourceList'] = request.resource_list
        if not UtilClient.is_unset(request.retry_policy):
            query['RetryPolicy'] = request.retry_policy
        if not UtilClient.is_unset(request.run_conf):
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
        if not UtilClient.is_unset(request.alert_conf):
            query['AlertConf'] = request.alert_conf
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.custom_variables):
            query['CustomVariables'] = request.custom_variables
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.env_conf):
            query['EnvConf'] = request.env_conf
        if not UtilClient.is_unset(request.fail_act):
            query['FailAct'] = request.fail_act
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.knox_password):
            query['KnoxPassword'] = request.knox_password
        if not UtilClient.is_unset(request.knox_user):
            query['KnoxUser'] = request.knox_user
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.monitor_conf):
            query['MonitorConf'] = request.monitor_conf
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.param_conf):
            query['ParamConf'] = request.param_conf
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_list):
            query['ResourceList'] = request.resource_list
        if not UtilClient.is_unset(request.retry_policy):
            query['RetryPolicy'] = request.retry_policy
        if not UtilClient.is_unset(request.run_conf):
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
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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

    def release_cluster_with_options(
        self,
        request: ddi_20200617_models.ReleaseClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ReleaseClusterResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_release):
            query['ForceRelease'] = request.force_release
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
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
        if not UtilClient.is_unset(request.force_release):
            query['ForceRelease'] = request.force_release
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
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
        if not UtilClient.is_unset(request.flow_instance_id):
            query['FlowInstanceId'] = request.flow_instance_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.re_run_fail):
            query['ReRunFail'] = request.re_run_fail
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.flow_instance_id):
            query['FlowInstanceId'] = request.flow_instance_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.re_run_fail):
            query['ReRunFail'] = request.re_run_fail
        if not UtilClient.is_unset(request.region_id):
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

    def resume_flow_with_options(
        self,
        request: ddi_20200617_models.ResumeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.ResumeFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.flow_instance_id):
            query['FlowInstanceId'] = request.flow_instance_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.flow_instance_id):
            query['FlowInstanceId'] = request.flow_instance_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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

    def submit_flow_with_options(
        self,
        request: ddi_20200617_models.SubmitFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.SubmitFlowResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conf):
            query['Conf'] = request.conf
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.conf):
            query['Conf'] = request.conf
        if not UtilClient.is_unset(request.flow_id):
            query['FlowId'] = request.flow_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.conf):
            query['Conf'] = request.conf
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.conf):
            query['Conf'] = request.conf
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.region_id):
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

    def tag_resources_with_options(
        self,
        request: ddi_20200617_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
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
            ddi_20200617_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ddi_20200617_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
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
            ddi_20200617_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def uninstall_libraries_with_options(
        self,
        request: ddi_20200617_models.UninstallLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.UninstallLibrariesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id_list):
            query['ClusterBizIdList'] = request.cluster_biz_id_list
        if not UtilClient.is_unset(request.library_biz_id):
            query['LibraryBizId'] = request.library_biz_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallLibraries',
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
            ddi_20200617_models.UninstallLibrariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_libraries_with_options_async(
        self,
        request: ddi_20200617_models.UninstallLibrariesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.UninstallLibrariesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_biz_id_list):
            query['ClusterBizIdList'] = request.cluster_biz_id_list
        if not UtilClient.is_unset(request.library_biz_id):
            query['LibraryBizId'] = request.library_biz_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallLibraries',
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
            ddi_20200617_models.UninstallLibrariesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def untag_resources_with_options(
        self,
        request: ddi_20200617_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
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
            ddi_20200617_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ddi_20200617_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
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
            ddi_20200617_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
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

    def update_library_install_task_status_with_options(
        self,
        request: ddi_20200617_models.UpdateLibraryInstallTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.UpdateLibraryInstallTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_biz_id):
            query['TaskBizId'] = request.task_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLibraryInstallTaskStatus',
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
            ddi_20200617_models.UpdateLibraryInstallTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_library_install_task_status_with_options_async(
        self,
        request: ddi_20200617_models.UpdateLibraryInstallTaskStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ddi_20200617_models.UpdateLibraryInstallTaskStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_biz_id):
            query['TaskBizId'] = request.task_biz_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLibraryInstallTaskStatus',
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
            ddi_20200617_models.UpdateLibraryInstallTaskStatusResponse(),
            await self.call_api_async(params, req, runtime)
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
