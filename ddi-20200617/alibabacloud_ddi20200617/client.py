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
