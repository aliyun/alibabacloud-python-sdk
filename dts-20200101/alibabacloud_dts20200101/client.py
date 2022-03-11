# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dts20200101 import models as dts_20200101_models
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
            'cn-qingdao': 'dts.aliyuncs.com',
            'cn-beijing': 'dts.aliyuncs.com',
            'cn-zhangjiakou': 'dts.aliyuncs.com',
            'cn-huhehaote': 'dts.aliyuncs.com',
            'cn-hangzhou': 'dts.aliyuncs.com',
            'cn-shanghai': 'dts.aliyuncs.com',
            'cn-shenzhen': 'dts.aliyuncs.com',
            'cn-hongkong': 'dts.aliyuncs.com',
            'ap-southeast-1': 'dts.aliyuncs.com',
            'ap-southeast-2': 'dts.aliyuncs.com',
            'ap-southeast-3': 'dts.aliyuncs.com',
            'ap-southeast-5': 'dts.aliyuncs.com',
            'eu-west-1': 'dts.aliyuncs.com',
            'us-west-1': 'dts.aliyuncs.com',
            'us-east-1': 'dts.aliyuncs.com',
            'eu-central-1': 'dts.aliyuncs.com',
            'me-east-1': 'dts.aliyuncs.com',
            'ap-south-1': 'dts.aliyuncs.com',
            'cn-hangzhou-finance': 'dts.aliyuncs.com',
            'cn-shanghai-finance-1': 'dts.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dts.aliyuncs.com',
            'cn-north-2-gov-1': 'dts.aliyuncs.com',
            'ap-northeast-2-pop': 'dts.aliyuncs.com',
            'cn-beijing-finance-1': 'dts.aliyuncs.com',
            'cn-beijing-finance-pop': 'dts.aliyuncs.com',
            'cn-beijing-gov-1': 'dts.aliyuncs.com',
            'cn-beijing-nu16-b01': 'dts.aliyuncs.com',
            'cn-chengdu': 'dts.aliyuncs.com',
            'cn-edge-1': 'dts.aliyuncs.com',
            'cn-fujian': 'dts.aliyuncs.com',
            'cn-haidian-cm12-c01': 'dts.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'dts.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'dts.aliyuncs.com',
            'cn-hangzhou-test-306': 'dts.aliyuncs.com',
            'cn-hongkong-finance-pop': 'dts.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'dts.aliyuncs.com',
            'cn-qingdao-nebula': 'dts.aliyuncs.com',
            'cn-shanghai-et15-b01': 'dts.aliyuncs.com',
            'cn-shanghai-et2-b01': 'dts.aliyuncs.com',
            'cn-shanghai-inner': 'dts.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'dts.aliyuncs.com',
            'cn-shenzhen-inner': 'dts.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'dts.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'dts.aliyuncs.com',
            'cn-wuhan': 'dts.aliyuncs.com',
            'cn-wulanchabu': 'dts.aliyuncs.com',
            'cn-yushanfang': 'dts.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'dts.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'dts.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'dts.aliyuncs.com',
            'eu-west-1-oxs': 'dts.aliyuncs.com',
            'rus-west-1-pop': 'dts.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dts', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def configure_dts_job_with_options(
        self,
        request: dts_20200101_models.ConfigureDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureDtsJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not UtilClient.is_unset(request.data_synchronization):
            query['DataSynchronization'] = request.data_synchronization
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.delay_notice):
            query['DelayNotice'] = request.delay_notice
        if not UtilClient.is_unset(request.delay_phone):
            query['DelayPhone'] = request.delay_phone
        if not UtilClient.is_unset(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not UtilClient.is_unset(request.destination_endpoint_data_base_name):
            query['DestinationEndpointDataBaseName'] = request.destination_endpoint_data_base_name
        if not UtilClient.is_unset(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not UtilClient.is_unset(request.destination_endpoint_ip):
            query['DestinationEndpointIP'] = request.destination_endpoint_ip
        if not UtilClient.is_unset(request.destination_endpoint_instance_id):
            query['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not UtilClient.is_unset(request.destination_endpoint_instance_type):
            query['DestinationEndpointInstanceType'] = request.destination_endpoint_instance_type
        if not UtilClient.is_unset(request.destination_endpoint_oracle_sid):
            query['DestinationEndpointOracleSID'] = request.destination_endpoint_oracle_sid
        if not UtilClient.is_unset(request.destination_endpoint_password):
            query['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not UtilClient.is_unset(request.destination_endpoint_port):
            query['DestinationEndpointPort'] = request.destination_endpoint_port
        if not UtilClient.is_unset(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not UtilClient.is_unset(request.destination_endpoint_user_name):
            query['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not UtilClient.is_unset(request.error_notice):
            query['ErrorNotice'] = request.error_notice
        if not UtilClient.is_unset(request.error_phone):
            query['ErrorPhone'] = request.error_phone
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_owner_id):
            query['SourceEndpointOwnerID'] = request.source_endpoint_owner_id
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_role):
            query['SourceEndpointRole'] = request.source_endpoint_role
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not UtilClient.is_unset(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        body = {}
        if not UtilClient.is_unset(request.db_list):
            body['DbList'] = request.db_list
        if not UtilClient.is_unset(request.reserve):
            body['Reserve'] = request.reserve
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_dts_job_with_options_async(
        self,
        request: dts_20200101_models.ConfigureDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureDtsJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not UtilClient.is_unset(request.data_synchronization):
            query['DataSynchronization'] = request.data_synchronization
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.delay_notice):
            query['DelayNotice'] = request.delay_notice
        if not UtilClient.is_unset(request.delay_phone):
            query['DelayPhone'] = request.delay_phone
        if not UtilClient.is_unset(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not UtilClient.is_unset(request.destination_endpoint_data_base_name):
            query['DestinationEndpointDataBaseName'] = request.destination_endpoint_data_base_name
        if not UtilClient.is_unset(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not UtilClient.is_unset(request.destination_endpoint_ip):
            query['DestinationEndpointIP'] = request.destination_endpoint_ip
        if not UtilClient.is_unset(request.destination_endpoint_instance_id):
            query['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not UtilClient.is_unset(request.destination_endpoint_instance_type):
            query['DestinationEndpointInstanceType'] = request.destination_endpoint_instance_type
        if not UtilClient.is_unset(request.destination_endpoint_oracle_sid):
            query['DestinationEndpointOracleSID'] = request.destination_endpoint_oracle_sid
        if not UtilClient.is_unset(request.destination_endpoint_password):
            query['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not UtilClient.is_unset(request.destination_endpoint_port):
            query['DestinationEndpointPort'] = request.destination_endpoint_port
        if not UtilClient.is_unset(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not UtilClient.is_unset(request.destination_endpoint_user_name):
            query['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not UtilClient.is_unset(request.error_notice):
            query['ErrorNotice'] = request.error_notice
        if not UtilClient.is_unset(request.error_phone):
            query['ErrorPhone'] = request.error_phone
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_owner_id):
            query['SourceEndpointOwnerID'] = request.source_endpoint_owner_id
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_role):
            query['SourceEndpointRole'] = request.source_endpoint_role
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not UtilClient.is_unset(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        body = {}
        if not UtilClient.is_unset(request.db_list):
            body['DbList'] = request.db_list
        if not UtilClient.is_unset(request.reserve):
            body['Reserve'] = request.reserve
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureDtsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_dts_job(
        self,
        request: dts_20200101_models.ConfigureDtsJobRequest,
    ) -> dts_20200101_models.ConfigureDtsJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_dts_job_with_options(request, runtime)

    async def configure_dts_job_async(
        self,
        request: dts_20200101_models.ConfigureDtsJobRequest,
    ) -> dts_20200101_models.ConfigureDtsJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_dts_job_with_options_async(request, runtime)

    def configure_migration_job_with_options(
        self,
        request: dts_20200101_models.ConfigureMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not UtilClient.is_unset(request.migration_reserved):
            query['MigrationReserved'] = request.migration_reserved
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        body = {}
        if not UtilClient.is_unset(request.migration_object):
            body['MigrationObject'] = request.migration_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_migration_job_with_options_async(
        self,
        request: dts_20200101_models.ConfigureMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not UtilClient.is_unset(request.migration_reserved):
            query['MigrationReserved'] = request.migration_reserved
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        body = {}
        if not UtilClient.is_unset(request.migration_object):
            body['MigrationObject'] = request.migration_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_migration_job(
        self,
        request: dts_20200101_models.ConfigureMigrationJobRequest,
    ) -> dts_20200101_models.ConfigureMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_migration_job_with_options(request, runtime)

    async def configure_migration_job_async(
        self,
        request: dts_20200101_models.ConfigureMigrationJobRequest,
    ) -> dts_20200101_models.ConfigureMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_migration_job_with_options_async(request, runtime)

    def configure_migration_job_alert_with_options(
        self,
        request: dts_20200101_models.ConfigureMigrationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureMigrationJobAlertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not UtilClient.is_unset(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not UtilClient.is_unset(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not UtilClient.is_unset(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not UtilClient.is_unset(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureMigrationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureMigrationJobAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_migration_job_alert_with_options_async(
        self,
        request: dts_20200101_models.ConfigureMigrationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureMigrationJobAlertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not UtilClient.is_unset(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not UtilClient.is_unset(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not UtilClient.is_unset(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not UtilClient.is_unset(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureMigrationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureMigrationJobAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_migration_job_alert(
        self,
        request: dts_20200101_models.ConfigureMigrationJobAlertRequest,
    ) -> dts_20200101_models.ConfigureMigrationJobAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_migration_job_alert_with_options(request, runtime)

    async def configure_migration_job_alert_async(
        self,
        request: dts_20200101_models.ConfigureMigrationJobAlertRequest,
    ) -> dts_20200101_models.ConfigureMigrationJobAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_migration_job_alert_with_options_async(request, runtime)

    def configure_subscription_with_options(
        self,
        request: dts_20200101_models.ConfigureSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.db_list):
            query['DbList'] = request.db_list
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.delay_notice):
            query['DelayNotice'] = request.delay_notice
        if not UtilClient.is_unset(request.delay_phone):
            query['DelayPhone'] = request.delay_phone
        if not UtilClient.is_unset(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not UtilClient.is_unset(request.error_notice):
            query['ErrorNotice'] = request.error_notice
        if not UtilClient.is_unset(request.error_phone):
            query['ErrorPhone'] = request.error_phone
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserve):
            query['Reserve'] = request.reserve
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_owner_id):
            query['SourceEndpointOwnerID'] = request.source_endpoint_owner_id
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_role):
            query['SourceEndpointRole'] = request.source_endpoint_role
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not UtilClient.is_unset(request.subscription_data_type_ddl):
            query['SubscriptionDataTypeDDL'] = request.subscription_data_type_ddl
        if not UtilClient.is_unset(request.subscription_data_type_dml):
            query['SubscriptionDataTypeDML'] = request.subscription_data_type_dml
        if not UtilClient.is_unset(request.subscription_instance_network_type):
            query['SubscriptionInstanceNetworkType'] = request.subscription_instance_network_type
        if not UtilClient.is_unset(request.subscription_instance_vpcid):
            query['SubscriptionInstanceVPCId'] = request.subscription_instance_vpcid
        if not UtilClient.is_unset(request.subscription_instance_vswitch_id):
            query['SubscriptionInstanceVSwitchId'] = request.subscription_instance_vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSubscription',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_subscription_with_options_async(
        self,
        request: dts_20200101_models.ConfigureSubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.db_list):
            query['DbList'] = request.db_list
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.delay_notice):
            query['DelayNotice'] = request.delay_notice
        if not UtilClient.is_unset(request.delay_phone):
            query['DelayPhone'] = request.delay_phone
        if not UtilClient.is_unset(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not UtilClient.is_unset(request.error_notice):
            query['ErrorNotice'] = request.error_notice
        if not UtilClient.is_unset(request.error_phone):
            query['ErrorPhone'] = request.error_phone
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reserve):
            query['Reserve'] = request.reserve
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_owner_id):
            query['SourceEndpointOwnerID'] = request.source_endpoint_owner_id
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_role):
            query['SourceEndpointRole'] = request.source_endpoint_role
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not UtilClient.is_unset(request.subscription_data_type_ddl):
            query['SubscriptionDataTypeDDL'] = request.subscription_data_type_ddl
        if not UtilClient.is_unset(request.subscription_data_type_dml):
            query['SubscriptionDataTypeDML'] = request.subscription_data_type_dml
        if not UtilClient.is_unset(request.subscription_instance_network_type):
            query['SubscriptionInstanceNetworkType'] = request.subscription_instance_network_type
        if not UtilClient.is_unset(request.subscription_instance_vpcid):
            query['SubscriptionInstanceVPCId'] = request.subscription_instance_vpcid
        if not UtilClient.is_unset(request.subscription_instance_vswitch_id):
            query['SubscriptionInstanceVSwitchId'] = request.subscription_instance_vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSubscription',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_subscription(
        self,
        request: dts_20200101_models.ConfigureSubscriptionRequest,
    ) -> dts_20200101_models.ConfigureSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_subscription_with_options(request, runtime)

    async def configure_subscription_async(
        self,
        request: dts_20200101_models.ConfigureSubscriptionRequest,
    ) -> dts_20200101_models.ConfigureSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_subscription_with_options_async(request, runtime)

    def configure_subscription_instance_with_options(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not UtilClient.is_unset(request.subscription_instance_name):
            query['SubscriptionInstanceName'] = request.subscription_instance_name
        if not UtilClient.is_unset(request.subscription_instance_network_type):
            query['SubscriptionInstanceNetworkType'] = request.subscription_instance_network_type
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        if not UtilClient.is_unset(request.subscription_data_type):
            query['SubscriptionDataType'] = request.subscription_data_type
        if not UtilClient.is_unset(request.subscription_instance):
            query['SubscriptionInstance'] = request.subscription_instance
        body = {}
        if not UtilClient.is_unset(request.subscription_object):
            body['SubscriptionObject'] = request.subscription_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSubscriptionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_subscription_instance_with_options_async(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not UtilClient.is_unset(request.subscription_instance_name):
            query['SubscriptionInstanceName'] = request.subscription_instance_name
        if not UtilClient.is_unset(request.subscription_instance_network_type):
            query['SubscriptionInstanceNetworkType'] = request.subscription_instance_network_type
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        if not UtilClient.is_unset(request.subscription_data_type):
            query['SubscriptionDataType'] = request.subscription_data_type
        if not UtilClient.is_unset(request.subscription_instance):
            query['SubscriptionInstance'] = request.subscription_instance
        body = {}
        if not UtilClient.is_unset(request.subscription_object):
            body['SubscriptionObject'] = request.subscription_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSubscriptionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_subscription_instance(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceRequest,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_subscription_instance_with_options(request, runtime)

    async def configure_subscription_instance_async(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceRequest,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_subscription_instance_with_options_async(request, runtime)

    def configure_subscription_instance_alert_with_options(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not UtilClient.is_unset(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not UtilClient.is_unset(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not UtilClient.is_unset(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not UtilClient.is_unset(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSubscriptionInstanceAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_subscription_instance_alert_with_options_async(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not UtilClient.is_unset(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not UtilClient.is_unset(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not UtilClient.is_unset(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not UtilClient.is_unset(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSubscriptionInstanceAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_subscription_instance_alert(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceAlertRequest,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_subscription_instance_alert_with_options(request, runtime)

    async def configure_subscription_instance_alert_async(
        self,
        request: dts_20200101_models.ConfigureSubscriptionInstanceAlertRequest,
    ) -> dts_20200101_models.ConfigureSubscriptionInstanceAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_subscription_instance_alert_with_options_async(request, runtime)

    def configure_synchronization_job_with_options(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not UtilClient.is_unset(request.migration_reserved):
            query['MigrationReserved'] = request.migration_reserved
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.synchronization_job_name):
            query['SynchronizationJobName'] = request.synchronization_job_name
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.partition_key):
            query['PartitionKey'] = request.partition_key
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        body = {}
        if not UtilClient.is_unset(request.synchronization_objects):
            body['SynchronizationObjects'] = request.synchronization_objects
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.checkpoint):
            query['Checkpoint'] = request.checkpoint
        if not UtilClient.is_unset(request.data_initialization):
            query['DataInitialization'] = request.data_initialization
        if not UtilClient.is_unset(request.migration_reserved):
            query['MigrationReserved'] = request.migration_reserved
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.structure_initialization):
            query['StructureInitialization'] = request.structure_initialization
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.synchronization_job_name):
            query['SynchronizationJobName'] = request.synchronization_job_name
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.partition_key):
            query['PartitionKey'] = request.partition_key
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        body = {}
        if not UtilClient.is_unset(request.synchronization_objects):
            body['SynchronizationObjects'] = request.synchronization_objects
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfigureSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSynchronizationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_synchronization_job(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_synchronization_job_with_options(request, runtime)

    async def configure_synchronization_job_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_synchronization_job_with_options_async(request, runtime)

    def configure_synchronization_job_alert_with_options(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobAlertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not UtilClient.is_unset(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not UtilClient.is_unset(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not UtilClient.is_unset(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not UtilClient.is_unset(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSynchronizationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSynchronizationJobAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_synchronization_job_alert_with_options_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobAlertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.delay_alert_phone):
            query['DelayAlertPhone'] = request.delay_alert_phone
        if not UtilClient.is_unset(request.delay_alert_status):
            query['DelayAlertStatus'] = request.delay_alert_status
        if not UtilClient.is_unset(request.delay_over_seconds):
            query['DelayOverSeconds'] = request.delay_over_seconds
        if not UtilClient.is_unset(request.error_alert_phone):
            query['ErrorAlertPhone'] = request.error_alert_phone
        if not UtilClient.is_unset(request.error_alert_status):
            query['ErrorAlertStatus'] = request.error_alert_status
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSynchronizationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSynchronizationJobAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_synchronization_job_alert(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobAlertRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_synchronization_job_alert_with_options(request, runtime)

    async def configure_synchronization_job_alert_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobAlertRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_synchronization_job_alert_with_options_async(request, runtime)

    def configure_synchronization_job_replicator_compare_with_options(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.synchronization_replicator_compare_enable):
            query['SynchronizationReplicatorCompareEnable'] = request.synchronization_replicator_compare_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSynchronizationJobReplicatorCompare',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_synchronization_job_replicator_compare_with_options_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.synchronization_replicator_compare_enable):
            query['SynchronizationReplicatorCompareEnable'] = request.synchronization_replicator_compare_enable
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigureSynchronizationJobReplicatorCompare',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_synchronization_job_replicator_compare(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse:
        runtime = util_models.RuntimeOptions()
        return self.configure_synchronization_job_replicator_compare_with_options(request, runtime)

    async def configure_synchronization_job_replicator_compare_async(
        self,
        request: dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareRequest,
    ) -> dts_20200101_models.ConfigureSynchronizationJobReplicatorCompareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.configure_synchronization_job_replicator_compare_with_options_async(request, runtime)

    def count_job_by_condition_with_options(
        self,
        request: dts_20200101_models.CountJobByConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CountJobByConditionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_db_type):
            query['DestDbType'] = request.dest_db_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.src_db_type):
            query['SrcDbType'] = request.src_db_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CountJobByCondition',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CountJobByConditionResponse(),
            self.call_api(params, req, runtime)
        )

    async def count_job_by_condition_with_options_async(
        self,
        request: dts_20200101_models.CountJobByConditionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CountJobByConditionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_db_type):
            query['DestDbType'] = request.dest_db_type
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.src_db_type):
            query['SrcDbType'] = request.src_db_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CountJobByCondition',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CountJobByConditionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def count_job_by_condition(
        self,
        request: dts_20200101_models.CountJobByConditionRequest,
    ) -> dts_20200101_models.CountJobByConditionResponse:
        runtime = util_models.RuntimeOptions()
        return self.count_job_by_condition_with_options(request, runtime)

    async def count_job_by_condition_async(
        self,
        request: dts_20200101_models.CountJobByConditionRequest,
    ) -> dts_20200101_models.CountJobByConditionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.count_job_by_condition_with_options_async(request, runtime)

    def create_consumer_channel_with_options(
        self,
        request: dts_20200101_models.CreateConsumerChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateConsumerChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateConsumerChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_channel_with_options_async(
        self,
        request: dts_20200101_models.CreateConsumerChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateConsumerChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateConsumerChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer_channel(
        self,
        request: dts_20200101_models.CreateConsumerChannelRequest,
    ) -> dts_20200101_models.CreateConsumerChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_channel_with_options(request, runtime)

    async def create_consumer_channel_async(
        self,
        request: dts_20200101_models.CreateConsumerChannelRequest,
    ) -> dts_20200101_models.CreateConsumerChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_consumer_channel_with_options_async(request, runtime)

    def create_consumer_group_with_options(
        self,
        request: dts_20200101_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateConsumerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_consumer_group_with_options_async(
        self,
        request: dts_20200101_models.CreateConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateConsumerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_consumer_group(
        self,
        request: dts_20200101_models.CreateConsumerGroupRequest,
    ) -> dts_20200101_models.CreateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_with_options(request, runtime)

    async def create_consumer_group_async(
        self,
        request: dts_20200101_models.CreateConsumerGroupRequest,
    ) -> dts_20200101_models.CreateConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_consumer_group_with_options_async(request, runtime)

    def create_dts_instance_with_options(
        self,
        request: dts_20200101_models.CreateDtsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateDtsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.compute_unit):
            query['ComputeUnit'] = request.compute_unit
        if not UtilClient.is_unset(request.database_count):
            query['DatabaseCount'] = request.database_count
        if not UtilClient.is_unset(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not UtilClient.is_unset(request.destination_region):
            query['DestinationRegion'] = request.destination_region
        if not UtilClient.is_unset(request.du):
            query['Du'] = request.du
        if not UtilClient.is_unset(request.fee_type):
            query['FeeType'] = request.fee_type
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_region):
            query['SourceRegion'] = request.source_region
        if not UtilClient.is_unset(request.sync_architecture):
            query['SyncArchitecture'] = request.sync_architecture
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDtsInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateDtsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dts_instance_with_options_async(
        self,
        request: dts_20200101_models.CreateDtsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateDtsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.compute_unit):
            query['ComputeUnit'] = request.compute_unit
        if not UtilClient.is_unset(request.database_count):
            query['DatabaseCount'] = request.database_count
        if not UtilClient.is_unset(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not UtilClient.is_unset(request.destination_region):
            query['DestinationRegion'] = request.destination_region
        if not UtilClient.is_unset(request.du):
            query['Du'] = request.du
        if not UtilClient.is_unset(request.fee_type):
            query['FeeType'] = request.fee_type
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.quantity):
            query['Quantity'] = request.quantity
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_region):
            query['SourceRegion'] = request.source_region
        if not UtilClient.is_unset(request.sync_architecture):
            query['SyncArchitecture'] = request.sync_architecture
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDtsInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateDtsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dts_instance(
        self,
        request: dts_20200101_models.CreateDtsInstanceRequest,
    ) -> dts_20200101_models.CreateDtsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dts_instance_with_options(request, runtime)

    async def create_dts_instance_async(
        self,
        request: dts_20200101_models.CreateDtsInstanceRequest,
    ) -> dts_20200101_models.CreateDtsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dts_instance_with_options_async(request, runtime)

    def create_job_monitor_rule_with_options(
        self,
        request: dts_20200101_models.CreateJobMonitorRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateJobMonitorRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobMonitorRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateJobMonitorRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_monitor_rule_with_options_async(
        self,
        request: dts_20200101_models.CreateJobMonitorRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateJobMonitorRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delay_rule_time):
            query['DelayRuleTime'] = request.delay_rule_time
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJobMonitorRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateJobMonitorRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job_monitor_rule(
        self,
        request: dts_20200101_models.CreateJobMonitorRuleRequest,
    ) -> dts_20200101_models.CreateJobMonitorRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_job_monitor_rule_with_options(request, runtime)

    async def create_job_monitor_rule_async(
        self,
        request: dts_20200101_models.CreateJobMonitorRuleRequest,
    ) -> dts_20200101_models.CreateJobMonitorRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_job_monitor_rule_with_options_async(request, runtime)

    def create_migration_job_with_options(
        self,
        request: dts_20200101_models.CreateMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_class):
            query['MigrationJobClass'] = request.migration_job_class
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_migration_job_with_options_async(
        self,
        request: dts_20200101_models.CreateMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_class):
            query['MigrationJobClass'] = request.migration_job_class
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_migration_job(
        self,
        request: dts_20200101_models.CreateMigrationJobRequest,
    ) -> dts_20200101_models.CreateMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_migration_job_with_options(request, runtime)

    async def create_migration_job_async(
        self,
        request: dts_20200101_models.CreateMigrationJobRequest,
    ) -> dts_20200101_models.CreateMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_migration_job_with_options_async(request, runtime)

    def create_subscription_instance_with_options(
        self,
        request: dts_20200101_models.CreateSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateSubscriptionInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateSubscriptionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_subscription_instance_with_options_async(
        self,
        request: dts_20200101_models.CreateSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateSubscriptionInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateSubscriptionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_subscription_instance(
        self,
        request: dts_20200101_models.CreateSubscriptionInstanceRequest,
    ) -> dts_20200101_models.CreateSubscriptionInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_subscription_instance_with_options(request, runtime)

    async def create_subscription_instance_async(
        self,
        request: dts_20200101_models.CreateSubscriptionInstanceRequest,
    ) -> dts_20200101_models.CreateSubscriptionInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_subscription_instance_with_options_async(request, runtime)

    def create_synchronization_job_with_options(
        self,
        request: dts_20200101_models.CreateSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateSynchronizationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_count):
            query['DBInstanceCount'] = request.dbinstance_count
        if not UtilClient.is_unset(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_region):
            query['SourceRegion'] = request.source_region
        if not UtilClient.is_unset(request.synchronization_job_class):
            query['SynchronizationJobClass'] = request.synchronization_job_class
        if not UtilClient.is_unset(request.topology):
            query['Topology'] = request.topology
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.network_type):
            query['networkType'] = request.network_type
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.CreateSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.CreateSynchronizationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_count):
            query['DBInstanceCount'] = request.dbinstance_count
        if not UtilClient.is_unset(request.dest_region):
            query['DestRegion'] = request.dest_region
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_region):
            query['SourceRegion'] = request.source_region
        if not UtilClient.is_unset(request.synchronization_job_class):
            query['SynchronizationJobClass'] = request.synchronization_job_class
        if not UtilClient.is_unset(request.topology):
            query['Topology'] = request.topology
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        if not UtilClient.is_unset(request.network_type):
            query['networkType'] = request.network_type
        if not UtilClient.is_unset(request.destination_endpoint):
            query['DestinationEndpoint'] = request.destination_endpoint
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.CreateSynchronizationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_synchronization_job(
        self,
        request: dts_20200101_models.CreateSynchronizationJobRequest,
    ) -> dts_20200101_models.CreateSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_synchronization_job_with_options(request, runtime)

    async def create_synchronization_job_async(
        self,
        request: dts_20200101_models.CreateSynchronizationJobRequest,
    ) -> dts_20200101_models.CreateSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_synchronization_job_with_options_async(request, runtime)

    def delete_consumer_channel_with_options(
        self,
        request: dts_20200101_models.DeleteConsumerChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteConsumerChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupId'] = request.consumer_group_id
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteConsumerChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_consumer_channel_with_options_async(
        self,
        request: dts_20200101_models.DeleteConsumerChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteConsumerChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupId'] = request.consumer_group_id
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteConsumerChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_consumer_channel(
        self,
        request: dts_20200101_models.DeleteConsumerChannelRequest,
    ) -> dts_20200101_models.DeleteConsumerChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_channel_with_options(request, runtime)

    async def delete_consumer_channel_async(
        self,
        request: dts_20200101_models.DeleteConsumerChannelRequest,
    ) -> dts_20200101_models.DeleteConsumerChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_consumer_channel_with_options_async(request, runtime)

    def delete_consumer_group_with_options(
        self,
        request: dts_20200101_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteConsumerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupID'] = request.consumer_group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_consumer_group_with_options_async(
        self,
        request: dts_20200101_models.DeleteConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteConsumerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupID'] = request.consumer_group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_consumer_group(
        self,
        request: dts_20200101_models.DeleteConsumerGroupRequest,
    ) -> dts_20200101_models.DeleteConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_with_options(request, runtime)

    async def delete_consumer_group_async(
        self,
        request: dts_20200101_models.DeleteConsumerGroupRequest,
    ) -> dts_20200101_models.DeleteConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_consumer_group_with_options_async(request, runtime)

    def delete_dts_job_with_options(
        self,
        request: dts_20200101_models.DeleteDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteDtsJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dts_job_with_options_async(
        self,
        request: dts_20200101_models.DeleteDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteDtsJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteDtsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dts_job(
        self,
        request: dts_20200101_models.DeleteDtsJobRequest,
    ) -> dts_20200101_models.DeleteDtsJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dts_job_with_options(request, runtime)

    async def delete_dts_job_async(
        self,
        request: dts_20200101_models.DeleteDtsJobRequest,
    ) -> dts_20200101_models.DeleteDtsJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dts_job_with_options_async(request, runtime)

    def delete_dts_jobs_with_options(
        self,
        request: dts_20200101_models.DeleteDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteDtsJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteDtsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dts_jobs_with_options_async(
        self,
        request: dts_20200101_models.DeleteDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteDtsJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteDtsJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dts_jobs(
        self,
        request: dts_20200101_models.DeleteDtsJobsRequest,
    ) -> dts_20200101_models.DeleteDtsJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_dts_jobs_with_options(request, runtime)

    async def delete_dts_jobs_async(
        self,
        request: dts_20200101_models.DeleteDtsJobsRequest,
    ) -> dts_20200101_models.DeleteDtsJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_dts_jobs_with_options_async(request, runtime)

    def delete_migration_job_with_options(
        self,
        request: dts_20200101_models.DeleteMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_migration_job_with_options_async(
        self,
        request: dts_20200101_models.DeleteMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_migration_job(
        self,
        request: dts_20200101_models.DeleteMigrationJobRequest,
    ) -> dts_20200101_models.DeleteMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_migration_job_with_options(request, runtime)

    async def delete_migration_job_async(
        self,
        request: dts_20200101_models.DeleteMigrationJobRequest,
    ) -> dts_20200101_models.DeleteMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_migration_job_with_options_async(request, runtime)

    def delete_subscription_instance_with_options(
        self,
        request: dts_20200101_models.DeleteSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteSubscriptionInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteSubscriptionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_subscription_instance_with_options_async(
        self,
        request: dts_20200101_models.DeleteSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteSubscriptionInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteSubscriptionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_subscription_instance(
        self,
        request: dts_20200101_models.DeleteSubscriptionInstanceRequest,
    ) -> dts_20200101_models.DeleteSubscriptionInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_subscription_instance_with_options(request, runtime)

    async def delete_subscription_instance_async(
        self,
        request: dts_20200101_models.DeleteSubscriptionInstanceRequest,
    ) -> dts_20200101_models.DeleteSubscriptionInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_subscription_instance_with_options_async(request, runtime)

    def delete_synchronization_job_with_options(
        self,
        request: dts_20200101_models.DeleteSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteSynchronizationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.DeleteSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DeleteSynchronizationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DeleteSynchronizationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_synchronization_job(
        self,
        request: dts_20200101_models.DeleteSynchronizationJobRequest,
    ) -> dts_20200101_models.DeleteSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_synchronization_job_with_options(request, runtime)

    async def delete_synchronization_job_async(
        self,
        request: dts_20200101_models.DeleteSynchronizationJobRequest,
    ) -> dts_20200101_models.DeleteSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_synchronization_job_with_options_async(request, runtime)

    def describe_connection_status_with_options(
        self,
        request: dts_20200101_models.DescribeConnectionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeConnectionStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_endpoint_architecture):
            query['DestinationEndpointArchitecture'] = request.destination_endpoint_architecture
        if not UtilClient.is_unset(request.destination_endpoint_database_name):
            query['DestinationEndpointDatabaseName'] = request.destination_endpoint_database_name
        if not UtilClient.is_unset(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not UtilClient.is_unset(request.destination_endpoint_ip):
            query['DestinationEndpointIP'] = request.destination_endpoint_ip
        if not UtilClient.is_unset(request.destination_endpoint_instance_id):
            query['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not UtilClient.is_unset(request.destination_endpoint_instance_type):
            query['DestinationEndpointInstanceType'] = request.destination_endpoint_instance_type
        if not UtilClient.is_unset(request.destination_endpoint_oracle_sid):
            query['DestinationEndpointOracleSID'] = request.destination_endpoint_oracle_sid
        if not UtilClient.is_unset(request.destination_endpoint_password):
            query['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not UtilClient.is_unset(request.destination_endpoint_port):
            query['DestinationEndpointPort'] = request.destination_endpoint_port
        if not UtilClient.is_unset(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not UtilClient.is_unset(request.destination_endpoint_user_name):
            query['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_endpoint_architecture):
            query['SourceEndpointArchitecture'] = request.source_endpoint_architecture
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConnectionStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeConnectionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_connection_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeConnectionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeConnectionStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_endpoint_architecture):
            query['DestinationEndpointArchitecture'] = request.destination_endpoint_architecture
        if not UtilClient.is_unset(request.destination_endpoint_database_name):
            query['DestinationEndpointDatabaseName'] = request.destination_endpoint_database_name
        if not UtilClient.is_unset(request.destination_endpoint_engine_name):
            query['DestinationEndpointEngineName'] = request.destination_endpoint_engine_name
        if not UtilClient.is_unset(request.destination_endpoint_ip):
            query['DestinationEndpointIP'] = request.destination_endpoint_ip
        if not UtilClient.is_unset(request.destination_endpoint_instance_id):
            query['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not UtilClient.is_unset(request.destination_endpoint_instance_type):
            query['DestinationEndpointInstanceType'] = request.destination_endpoint_instance_type
        if not UtilClient.is_unset(request.destination_endpoint_oracle_sid):
            query['DestinationEndpointOracleSID'] = request.destination_endpoint_oracle_sid
        if not UtilClient.is_unset(request.destination_endpoint_password):
            query['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not UtilClient.is_unset(request.destination_endpoint_port):
            query['DestinationEndpointPort'] = request.destination_endpoint_port
        if not UtilClient.is_unset(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not UtilClient.is_unset(request.destination_endpoint_user_name):
            query['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_endpoint_architecture):
            query['SourceEndpointArchitecture'] = request.source_endpoint_architecture
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not UtilClient.is_unset(request.source_endpoint_engine_name):
            query['SourceEndpointEngineName'] = request.source_endpoint_engine_name
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not UtilClient.is_unset(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not UtilClient.is_unset(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not UtilClient.is_unset(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConnectionStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeConnectionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_connection_status(
        self,
        request: dts_20200101_models.DescribeConnectionStatusRequest,
    ) -> dts_20200101_models.DescribeConnectionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_connection_status_with_options(request, runtime)

    async def describe_connection_status_async(
        self,
        request: dts_20200101_models.DescribeConnectionStatusRequest,
    ) -> dts_20200101_models.DescribeConnectionStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_connection_status_with_options_async(request, runtime)

    def describe_consumer_channel_with_options(
        self,
        request: dts_20200101_models.DescribeConsumerChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeConsumerChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_channel_id):
            query['ParentChannelId'] = request.parent_channel_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeConsumerChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_consumer_channel_with_options_async(
        self,
        request: dts_20200101_models.DescribeConsumerChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeConsumerChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_channel_id):
            query['ParentChannelId'] = request.parent_channel_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeConsumerChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_consumer_channel(
        self,
        request: dts_20200101_models.DescribeConsumerChannelRequest,
    ) -> dts_20200101_models.DescribeConsumerChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_consumer_channel_with_options(request, runtime)

    async def describe_consumer_channel_async(
        self,
        request: dts_20200101_models.DescribeConsumerChannelRequest,
    ) -> dts_20200101_models.DescribeConsumerChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_consumer_channel_with_options_async(request, runtime)

    def describe_consumer_group_with_options(
        self,
        request: dts_20200101_models.DescribeConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeConsumerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConsumerGroup',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_consumer_group_with_options_async(
        self,
        request: dts_20200101_models.DescribeConsumerGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeConsumerGroupResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConsumerGroup',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeConsumerGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_consumer_group(
        self,
        request: dts_20200101_models.DescribeConsumerGroupRequest,
    ) -> dts_20200101_models.DescribeConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_consumer_group_with_options(request, runtime)

    async def describe_consumer_group_async(
        self,
        request: dts_20200101_models.DescribeConsumerGroupRequest,
    ) -> dts_20200101_models.DescribeConsumerGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_consumer_group_with_options_async(request, runtime)

    def describe_dtsipwith_options(
        self,
        request: dts_20200101_models.DescribeDTSIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDTSIPResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDTSIP',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDTSIPResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dtsipwith_options_async(
        self,
        request: dts_20200101_models.DescribeDTSIPRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDTSIPResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDTSIP',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDTSIPResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dtsip(
        self,
        request: dts_20200101_models.DescribeDTSIPRequest,
    ) -> dts_20200101_models.DescribeDTSIPResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dtsipwith_options(request, runtime)

    async def describe_dtsip_async(
        self,
        request: dts_20200101_models.DescribeDTSIPRequest,
    ) -> dts_20200101_models.DescribeDTSIPResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dtsipwith_options_async(request, runtime)

    def describe_dts_etl_job_version_info_with_options(
        self,
        request: dts_20200101_models.DescribeDtsEtlJobVersionInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsEtlJobVersionInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsEtlJobVersionInfo',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDtsEtlJobVersionInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dts_etl_job_version_info_with_options_async(
        self,
        request: dts_20200101_models.DescribeDtsEtlJobVersionInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsEtlJobVersionInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsEtlJobVersionInfo',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDtsEtlJobVersionInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dts_etl_job_version_info(
        self,
        request: dts_20200101_models.DescribeDtsEtlJobVersionInfoRequest,
    ) -> dts_20200101_models.DescribeDtsEtlJobVersionInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dts_etl_job_version_info_with_options(request, runtime)

    async def describe_dts_etl_job_version_info_async(
        self,
        request: dts_20200101_models.DescribeDtsEtlJobVersionInfoRequest,
    ) -> dts_20200101_models.DescribeDtsEtlJobVersionInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dts_etl_job_version_info_with_options_async(request, runtime)

    def describe_dts_job_detail_with_options(
        self,
        request: dts_20200101_models.DescribeDtsJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsJobDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceID'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sync_sub_job_history):
            query['SyncSubJobHistory'] = request.sync_sub_job_history
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsJobDetail',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDtsJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dts_job_detail_with_options_async(
        self,
        request: dts_20200101_models.DescribeDtsJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsJobDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceID'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sync_sub_job_history):
            query['SyncSubJobHistory'] = request.sync_sub_job_history
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsJobDetail',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDtsJobDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dts_job_detail(
        self,
        request: dts_20200101_models.DescribeDtsJobDetailRequest,
    ) -> dts_20200101_models.DescribeDtsJobDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dts_job_detail_with_options(request, runtime)

    async def describe_dts_job_detail_async(
        self,
        request: dts_20200101_models.DescribeDtsJobDetailRequest,
    ) -> dts_20200101_models.DescribeDtsJobDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dts_job_detail_with_options_async(request, runtime)

    def describe_dts_jobs_with_options(
        self,
        request: dts_20200101_models.DescribeDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dedicated_cluster_node_id):
            query['DedicatedClusterNodeId'] = request.dedicated_cluster_node_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.order_column):
            query['OrderColumn'] = request.order_column
        if not UtilClient.is_unset(request.order_direction):
            query['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
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
            action='DescribeDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDtsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dts_jobs_with_options_async(
        self,
        request: dts_20200101_models.DescribeDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dedicated_cluster_id):
            query['DedicatedClusterId'] = request.dedicated_cluster_id
        if not UtilClient.is_unset(request.dedicated_cluster_node_id):
            query['DedicatedClusterNodeId'] = request.dedicated_cluster_node_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.order_column):
            query['OrderColumn'] = request.order_column
        if not UtilClient.is_unset(request.order_direction):
            query['OrderDirection'] = request.order_direction
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
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
            action='DescribeDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDtsJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dts_jobs(
        self,
        request: dts_20200101_models.DescribeDtsJobsRequest,
    ) -> dts_20200101_models.DescribeDtsJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dts_jobs_with_options(request, runtime)

    async def describe_dts_jobs_async(
        self,
        request: dts_20200101_models.DescribeDtsJobsRequest,
    ) -> dts_20200101_models.DescribeDtsJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dts_jobs_with_options_async(request, runtime)

    def describe_dts_service_log_with_options(
        self,
        request: dts_20200101_models.DescribeDtsServiceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsServiceLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.sub_job_type):
            query['SubJobType'] = request.sub_job_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsServiceLog',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDtsServiceLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dts_service_log_with_options_async(
        self,
        request: dts_20200101_models.DescribeDtsServiceLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeDtsServiceLogResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.sub_job_type):
            query['SubJobType'] = request.sub_job_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDtsServiceLog',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeDtsServiceLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dts_service_log(
        self,
        request: dts_20200101_models.DescribeDtsServiceLogRequest,
    ) -> dts_20200101_models.DescribeDtsServiceLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dts_service_log_with_options(request, runtime)

    async def describe_dts_service_log_async(
        self,
        request: dts_20200101_models.DescribeDtsServiceLogRequest,
    ) -> dts_20200101_models.DescribeDtsServiceLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dts_service_log_with_options_async(request, runtime)

    def describe_endpoint_switch_status_with_options(
        self,
        request: dts_20200101_models.DescribeEndpointSwitchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeEndpointSwitchStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndpointSwitchStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeEndpointSwitchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_endpoint_switch_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeEndpointSwitchStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeEndpointSwitchStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndpointSwitchStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeEndpointSwitchStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_endpoint_switch_status(
        self,
        request: dts_20200101_models.DescribeEndpointSwitchStatusRequest,
    ) -> dts_20200101_models.DescribeEndpointSwitchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_endpoint_switch_status_with_options(request, runtime)

    async def describe_endpoint_switch_status_async(
        self,
        request: dts_20200101_models.DescribeEndpointSwitchStatusRequest,
    ) -> dts_20200101_models.DescribeEndpointSwitchStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_endpoint_switch_status_with_options_async(request, runtime)

    def describe_etl_job_logs_with_options(
        self,
        request: dts_20200101_models.DescribeEtlJobLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeEtlJobLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEtlJobLogs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeEtlJobLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_etl_job_logs_with_options_async(
        self,
        request: dts_20200101_models.DescribeEtlJobLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeEtlJobLogsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEtlJobLogs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeEtlJobLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_etl_job_logs(
        self,
        request: dts_20200101_models.DescribeEtlJobLogsRequest,
    ) -> dts_20200101_models.DescribeEtlJobLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_etl_job_logs_with_options(request, runtime)

    async def describe_etl_job_logs_async(
        self,
        request: dts_20200101_models.DescribeEtlJobLogsRequest,
    ) -> dts_20200101_models.DescribeEtlJobLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_etl_job_logs_with_options_async(request, runtime)

    def describe_initialization_status_with_options(
        self,
        request: dts_20200101_models.DescribeInitializationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeInitializationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInitializationStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeInitializationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_initialization_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeInitializationStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeInitializationStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInitializationStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeInitializationStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_initialization_status(
        self,
        request: dts_20200101_models.DescribeInitializationStatusRequest,
    ) -> dts_20200101_models.DescribeInitializationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_initialization_status_with_options(request, runtime)

    async def describe_initialization_status_async(
        self,
        request: dts_20200101_models.DescribeInitializationStatusRequest,
    ) -> dts_20200101_models.DescribeInitializationStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_initialization_status_with_options_async(request, runtime)

    def describe_job_monitor_rule_with_options(
        self,
        request: dts_20200101_models.DescribeJobMonitorRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeJobMonitorRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobMonitorRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeJobMonitorRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_monitor_rule_with_options_async(
        self,
        request: dts_20200101_models.DescribeJobMonitorRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeJobMonitorRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobMonitorRule',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeJobMonitorRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_monitor_rule(
        self,
        request: dts_20200101_models.DescribeJobMonitorRuleRequest,
    ) -> dts_20200101_models.DescribeJobMonitorRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_job_monitor_rule_with_options(request, runtime)

    async def describe_job_monitor_rule_async(
        self,
        request: dts_20200101_models.DescribeJobMonitorRuleRequest,
    ) -> dts_20200101_models.DescribeJobMonitorRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_monitor_rule_with_options_async(request, runtime)

    def describe_migration_job_alert_with_options(
        self,
        request: dts_20200101_models.DescribeMigrationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobAlertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeMigrationJobAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_migration_job_alert_with_options_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobAlertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeMigrationJobAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_migration_job_alert(
        self,
        request: dts_20200101_models.DescribeMigrationJobAlertRequest,
    ) -> dts_20200101_models.DescribeMigrationJobAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_job_alert_with_options(request, runtime)

    async def describe_migration_job_alert_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobAlertRequest,
    ) -> dts_20200101_models.DescribeMigrationJobAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migration_job_alert_with_options_async(request, runtime)

    def describe_migration_job_detail_with_options(
        self,
        request: dts_20200101_models.DescribeMigrationJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobDetail',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeMigrationJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_migration_job_detail_with_options_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.migration_mode):
            query['MigrationMode'] = request.migration_mode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobDetail',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeMigrationJobDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_migration_job_detail(
        self,
        request: dts_20200101_models.DescribeMigrationJobDetailRequest,
    ) -> dts_20200101_models.DescribeMigrationJobDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_job_detail_with_options(request, runtime)

    async def describe_migration_job_detail_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobDetailRequest,
    ) -> dts_20200101_models.DescribeMigrationJobDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migration_job_detail_with_options_async(request, runtime)

    def describe_migration_job_status_with_options(
        self,
        request: dts_20200101_models.DescribeMigrationJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeMigrationJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_migration_job_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeMigrationJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_migration_job_status(
        self,
        request: dts_20200101_models.DescribeMigrationJobStatusRequest,
    ) -> dts_20200101_models.DescribeMigrationJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_job_status_with_options(request, runtime)

    async def describe_migration_job_status_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobStatusRequest,
    ) -> dts_20200101_models.DescribeMigrationJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migration_job_status_with_options_async(request, runtime)

    def describe_migration_jobs_with_options(
        self,
        request: dts_20200101_models.DescribeMigrationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeMigrationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_migration_jobs_with_options_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeMigrationJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.migration_job_name):
            query['MigrationJobName'] = request.migration_job_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMigrationJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeMigrationJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_migration_jobs(
        self,
        request: dts_20200101_models.DescribeMigrationJobsRequest,
    ) -> dts_20200101_models.DescribeMigrationJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_migration_jobs_with_options(request, runtime)

    async def describe_migration_jobs_async(
        self,
        request: dts_20200101_models.DescribeMigrationJobsRequest,
    ) -> dts_20200101_models.DescribeMigrationJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_migration_jobs_with_options_async(request, runtime)

    def describe_pre_check_status_with_options(
        self,
        request: dts_20200101_models.DescribePreCheckStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribePreCheckStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_code):
            query['JobCode'] = request.job_code
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.struct_phase):
            query['StructPhase'] = request.struct_phase
        if not UtilClient.is_unset(request.struct_type):
            query['StructType'] = request.struct_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePreCheckStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribePreCheckStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pre_check_status_with_options_async(
        self,
        request: dts_20200101_models.DescribePreCheckStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribePreCheckStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_code):
            query['JobCode'] = request.job_code
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.struct_phase):
            query['StructPhase'] = request.struct_phase
        if not UtilClient.is_unset(request.struct_type):
            query['StructType'] = request.struct_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePreCheckStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribePreCheckStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pre_check_status(
        self,
        request: dts_20200101_models.DescribePreCheckStatusRequest,
    ) -> dts_20200101_models.DescribePreCheckStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_pre_check_status_with_options(request, runtime)

    async def describe_pre_check_status_async(
        self,
        request: dts_20200101_models.DescribePreCheckStatusRequest,
    ) -> dts_20200101_models.DescribePreCheckStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_pre_check_status_with_options_async(request, runtime)

    def describe_subscription_instance_alert_with_options(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceAlertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInstanceAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSubscriptionInstanceAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_subscription_instance_alert_with_options_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceAlertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInstanceAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSubscriptionInstanceAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_subscription_instance_alert(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceAlertRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_instance_alert_with_options(request, runtime)

    async def describe_subscription_instance_alert_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceAlertRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_subscription_instance_alert_with_options_async(request, runtime)

    def describe_subscription_instance_status_with_options(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInstanceStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSubscriptionInstanceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_subscription_instance_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInstanceStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSubscriptionInstanceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_subscription_instance_status(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceStatusRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_instance_status_with_options(request, runtime)

    async def describe_subscription_instance_status_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstanceStatusRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstanceStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_subscription_instance_status_with_options_async(request, runtime)

    def describe_subscription_instances_with_options(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_name):
            query['SubscriptionInstanceName'] = request.subscription_instance_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInstances',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSubscriptionInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_subscription_instances_with_options_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionInstancesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_name):
            query['SubscriptionInstanceName'] = request.subscription_instance_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionInstances',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSubscriptionInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_subscription_instances(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstancesRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_instances_with_options(request, runtime)

    async def describe_subscription_instances_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionInstancesRequest,
    ) -> dts_20200101_models.DescribeSubscriptionInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_subscription_instances_with_options_async(request, runtime)

    def describe_subscription_meta_with_options(
        self,
        tmp_req: dts_20200101_models.DescribeSubscriptionMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionMetaResponse:
        UtilClient.validate_model(tmp_req)
        request = dts_20200101_models.DescribeSubscriptionMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_migration_job_ids):
            request.sub_migration_job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_migration_job_ids, 'SubMigrationJobIds', 'json')
        if not UtilClient.is_unset(tmp_req.topics):
            request.topics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.sub_migration_job_ids_shrink):
            query['SubMigrationJobIds'] = request.sub_migration_job_ids_shrink
        if not UtilClient.is_unset(request.topics_shrink):
            query['Topics'] = request.topics_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionMeta',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSubscriptionMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_subscription_meta_with_options_async(
        self,
        tmp_req: dts_20200101_models.DescribeSubscriptionMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSubscriptionMetaResponse:
        UtilClient.validate_model(tmp_req)
        request = dts_20200101_models.DescribeSubscriptionMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_migration_job_ids):
            request.sub_migration_job_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_migration_job_ids, 'SubMigrationJobIds', 'json')
        if not UtilClient.is_unset(tmp_req.topics):
            request.topics_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.topics, 'Topics', 'json')
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sid):
            query['Sid'] = request.sid
        if not UtilClient.is_unset(request.sub_migration_job_ids_shrink):
            query['SubMigrationJobIds'] = request.sub_migration_job_ids_shrink
        if not UtilClient.is_unset(request.topics_shrink):
            query['Topics'] = request.topics_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSubscriptionMeta',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSubscriptionMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_subscription_meta(
        self,
        request: dts_20200101_models.DescribeSubscriptionMetaRequest,
    ) -> dts_20200101_models.DescribeSubscriptionMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_subscription_meta_with_options(request, runtime)

    async def describe_subscription_meta_async(
        self,
        request: dts_20200101_models.DescribeSubscriptionMetaRequest,
    ) -> dts_20200101_models.DescribeSubscriptionMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_subscription_meta_with_options_async(request, runtime)

    def describe_synchronization_job_alert_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobAlertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationJobAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_synchronization_job_alert_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobAlertRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobAlertResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobAlert',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationJobAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_synchronization_job_alert(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobAlertRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobAlertResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_alert_with_options(request, runtime)

    async def describe_synchronization_job_alert_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobAlertRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobAlertResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_job_alert_with_options_async(request, runtime)

    def describe_synchronization_job_replicator_compare_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobReplicatorCompareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobReplicatorCompare',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_synchronization_job_replicator_compare_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobReplicatorCompareRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobReplicatorCompare',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_synchronization_job_replicator_compare(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobReplicatorCompareRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_replicator_compare_with_options(request, runtime)

    async def describe_synchronization_job_replicator_compare_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobReplicatorCompareRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobReplicatorCompareResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_job_replicator_compare_with_options_async(request, runtime)

    def describe_synchronization_job_status_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_synchronization_job_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationJobStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_synchronization_job_status(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_status_with_options(request, runtime)

    async def describe_synchronization_job_status_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_job_status_with_options_async(request, runtime)

    def describe_synchronization_job_status_list_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_job_id_list_json_str):
            query['SynchronizationJobIdListJsonStr'] = request.synchronization_job_id_list_json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobStatusList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationJobStatusListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_synchronization_job_status_list_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_job_id_list_json_str):
            query['SynchronizationJobIdListJsonStr'] = request.synchronization_job_id_list_json_str
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobStatusList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationJobStatusListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_synchronization_job_status_list(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusListRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_job_status_list_with_options(request, runtime)

    async def describe_synchronization_job_status_list_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobStatusListRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobStatusListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_job_status_list_with_options_async(request, runtime)

    def describe_synchronization_jobs_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_job_name):
            query['SynchronizationJobName'] = request.synchronization_job_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_synchronization_jobs_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_job_name):
            query['SynchronizationJobName'] = request.synchronization_job_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_synchronization_jobs(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobsRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_jobs_with_options(request, runtime)

    async def describe_synchronization_jobs_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationJobsRequest,
    ) -> dts_20200101_models.DescribeSynchronizationJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_jobs_with_options_async(request, runtime)

    def describe_synchronization_object_modify_status_with_options(
        self,
        request: dts_20200101_models.DescribeSynchronizationObjectModifyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationObjectModifyStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_synchronization_object_modify_status_with_options_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationObjectModifyStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSynchronizationObjectModifyStatus',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_synchronization_object_modify_status(
        self,
        request: dts_20200101_models.DescribeSynchronizationObjectModifyStatusRequest,
    ) -> dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_synchronization_object_modify_status_with_options(request, runtime)

    async def describe_synchronization_object_modify_status_async(
        self,
        request: dts_20200101_models.DescribeSynchronizationObjectModifyStatusRequest,
    ) -> dts_20200101_models.DescribeSynchronizationObjectModifyStatusResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_synchronization_object_modify_status_with_options_async(request, runtime)

    def describe_tag_keys_with_options(
        self,
        request: dts_20200101_models.DescribeTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
            action='DescribeTagKeys',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_keys_with_options_async(
        self,
        request: dts_20200101_models.DescribeTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeTagKeysResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
            action='DescribeTagKeys',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag_keys(
        self,
        request: dts_20200101_models.DescribeTagKeysRequest,
    ) -> dts_20200101_models.DescribeTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_keys_with_options(request, runtime)

    async def describe_tag_keys_async(
        self,
        request: dts_20200101_models.DescribeTagKeysRequest,
    ) -> dts_20200101_models.DescribeTagKeysResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_keys_with_options_async(request, runtime)

    def describe_tag_values_with_options(
        self,
        request: dts_20200101_models.DescribeTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
            action='DescribeTagValues',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_values_with_options_async(
        self,
        request: dts_20200101_models.DescribeTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.DescribeTagValuesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category):
            query['Category'] = request.category
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
            action='DescribeTagValues',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.DescribeTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag_values(
        self,
        request: dts_20200101_models.DescribeTagValuesRequest,
    ) -> dts_20200101_models.DescribeTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_values_with_options(request, runtime)

    async def describe_tag_values_async(
        self,
        request: dts_20200101_models.DescribeTagValuesRequest,
    ) -> dts_20200101_models.DescribeTagValuesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_values_with_options_async(request, runtime)

    def init_dts_rds_instance_with_options(
        self,
        request: dts_20200101_models.InitDtsRdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.InitDtsRdsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.endpoint_cen_id):
            query['EndpointCenId'] = request.endpoint_cen_id
        if not UtilClient.is_unset(request.endpoint_instance_id):
            query['EndpointInstanceId'] = request.endpoint_instance_id
        if not UtilClient.is_unset(request.endpoint_instance_type):
            query['EndpointInstanceType'] = request.endpoint_instance_type
        if not UtilClient.is_unset(request.endpoint_region):
            query['EndpointRegion'] = request.endpoint_region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitDtsRdsInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.InitDtsRdsInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def init_dts_rds_instance_with_options_async(
        self,
        request: dts_20200101_models.InitDtsRdsInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.InitDtsRdsInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.endpoint_cen_id):
            query['EndpointCenId'] = request.endpoint_cen_id
        if not UtilClient.is_unset(request.endpoint_instance_id):
            query['EndpointInstanceId'] = request.endpoint_instance_id
        if not UtilClient.is_unset(request.endpoint_instance_type):
            query['EndpointInstanceType'] = request.endpoint_instance_type
        if not UtilClient.is_unset(request.endpoint_region):
            query['EndpointRegion'] = request.endpoint_region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitDtsRdsInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.InitDtsRdsInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def init_dts_rds_instance(
        self,
        request: dts_20200101_models.InitDtsRdsInstanceRequest,
    ) -> dts_20200101_models.InitDtsRdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.init_dts_rds_instance_with_options(request, runtime)

    async def init_dts_rds_instance_async(
        self,
        request: dts_20200101_models.InitDtsRdsInstanceRequest,
    ) -> dts_20200101_models.InitDtsRdsInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.init_dts_rds_instance_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: dts_20200101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: dts_20200101_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ListTagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: dts_20200101_models.ListTagResourcesRequest,
    ) -> dts_20200101_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: dts_20200101_models.ListTagResourcesRequest,
    ) -> dts_20200101_models.ListTagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def modify_consumer_channel_with_options(
        self,
        request: dts_20200101_models.ModifyConsumerChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyConsumerChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupId'] = request.consumer_group_id
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyConsumerChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_consumer_channel_with_options_async(
        self,
        request: dts_20200101_models.ModifyConsumerChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyConsumerChannelResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupId'] = request.consumer_group_id
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyConsumerChannel',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyConsumerChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_consumer_channel(
        self,
        request: dts_20200101_models.ModifyConsumerChannelRequest,
    ) -> dts_20200101_models.ModifyConsumerChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_consumer_channel_with_options(request, runtime)

    async def modify_consumer_channel_async(
        self,
        request: dts_20200101_models.ModifyConsumerChannelRequest,
    ) -> dts_20200101_models.ModifyConsumerChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_consumer_channel_with_options_async(request, runtime)

    def modify_consumer_group_password_with_options(
        self,
        request: dts_20200101_models.ModifyConsumerGroupPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyConsumerGroupPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupID'] = request.consumer_group_id
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not UtilClient.is_unset(request.consumer_group_new_password):
            query['consumerGroupNewPassword'] = request.consumer_group_new_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyConsumerGroupPassword',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyConsumerGroupPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_consumer_group_password_with_options_async(
        self,
        request: dts_20200101_models.ModifyConsumerGroupPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyConsumerGroupPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupID'] = request.consumer_group_id
        if not UtilClient.is_unset(request.consumer_group_name):
            query['ConsumerGroupName'] = request.consumer_group_name
        if not UtilClient.is_unset(request.consumer_group_password):
            query['ConsumerGroupPassword'] = request.consumer_group_password
        if not UtilClient.is_unset(request.consumer_group_user_name):
            query['ConsumerGroupUserName'] = request.consumer_group_user_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not UtilClient.is_unset(request.consumer_group_new_password):
            query['consumerGroupNewPassword'] = request.consumer_group_new_password
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyConsumerGroupPassword',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyConsumerGroupPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_consumer_group_password(
        self,
        request: dts_20200101_models.ModifyConsumerGroupPasswordRequest,
    ) -> dts_20200101_models.ModifyConsumerGroupPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_consumer_group_password_with_options(request, runtime)

    async def modify_consumer_group_password_async(
        self,
        request: dts_20200101_models.ModifyConsumerGroupPasswordRequest,
    ) -> dts_20200101_models.ModifyConsumerGroupPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_consumer_group_password_with_options_async(request, runtime)

    def modify_consumption_timestamp_with_options(
        self,
        request: dts_20200101_models.ModifyConsumptionTimestampRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyConsumptionTimestampResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumption_timestamp):
            query['ConsumptionTimestamp'] = request.consumption_timestamp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyConsumptionTimestamp',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyConsumptionTimestampResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_consumption_timestamp_with_options_async(
        self,
        request: dts_20200101_models.ModifyConsumptionTimestampRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyConsumptionTimestampResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.consumption_timestamp):
            query['ConsumptionTimestamp'] = request.consumption_timestamp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyConsumptionTimestamp',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyConsumptionTimestampResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_consumption_timestamp(
        self,
        request: dts_20200101_models.ModifyConsumptionTimestampRequest,
    ) -> dts_20200101_models.ModifyConsumptionTimestampResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_consumption_timestamp_with_options(request, runtime)

    async def modify_consumption_timestamp_async(
        self,
        request: dts_20200101_models.ModifyConsumptionTimestampRequest,
    ) -> dts_20200101_models.ModifyConsumptionTimestampResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_consumption_timestamp_with_options_async(request, runtime)

    def modify_dts_job_with_options(
        self,
        tmp_req: dts_20200101_models.ModifyDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobResponse:
        UtilClient.validate_model(tmp_req)
        request = dts_20200101_models.ModifyDtsJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.db_list):
            request.db_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.db_list, 'DbList', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        body = {}
        if not UtilClient.is_unset(request.db_list_shrink):
            body['DbList'] = request.db_list_shrink
        if not UtilClient.is_unset(request.etl_operator_column_reference):
            body['EtlOperatorColumnReference'] = request.etl_operator_column_reference
        if not UtilClient.is_unset(request.modify_type_enum):
            body['ModifyTypeEnum'] = request.modify_type_enum
        if not UtilClient.is_unset(request.reserved):
            body['Reserved'] = request.reserved
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dts_job_with_options_async(
        self,
        tmp_req: dts_20200101_models.ModifyDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobResponse:
        UtilClient.validate_model(tmp_req)
        request = dts_20200101_models.ModifyDtsJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.db_list):
            request.db_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.db_list, 'DbList', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        body = {}
        if not UtilClient.is_unset(request.db_list_shrink):
            body['DbList'] = request.db_list_shrink
        if not UtilClient.is_unset(request.etl_operator_column_reference):
            body['EtlOperatorColumnReference'] = request.etl_operator_column_reference
        if not UtilClient.is_unset(request.modify_type_enum):
            body['ModifyTypeEnum'] = request.modify_type_enum
        if not UtilClient.is_unset(request.reserved):
            body['Reserved'] = request.reserved
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyDtsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dts_job(
        self,
        request: dts_20200101_models.ModifyDtsJobRequest,
    ) -> dts_20200101_models.ModifyDtsJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dts_job_with_options(request, runtime)

    async def modify_dts_job_async(
        self,
        request: dts_20200101_models.ModifyDtsJobRequest,
    ) -> dts_20200101_models.ModifyDtsJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dts_job_with_options_async(request, runtime)

    def modify_dts_job_name_with_options(
        self,
        request: dts_20200101_models.ModifyDtsJobNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobName',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyDtsJobNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dts_job_name_with_options_async(
        self,
        request: dts_20200101_models.ModifyDtsJobNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobNameResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.dts_job_name):
            query['DtsJobName'] = request.dts_job_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobName',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyDtsJobNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dts_job_name(
        self,
        request: dts_20200101_models.ModifyDtsJobNameRequest,
    ) -> dts_20200101_models.ModifyDtsJobNameResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dts_job_name_with_options(request, runtime)

    async def modify_dts_job_name_async(
        self,
        request: dts_20200101_models.ModifyDtsJobNameRequest,
    ) -> dts_20200101_models.ModifyDtsJobNameResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dts_job_name_with_options_async(request, runtime)

    def modify_dts_job_password_with_options(
        self,
        request: dts_20200101_models.ModifyDtsJobPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobPassword',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyDtsJobPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dts_job_password_with_options_async(
        self,
        request: dts_20200101_models.ModifyDtsJobPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifyDtsJobPasswordResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDtsJobPassword',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifyDtsJobPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dts_job_password(
        self,
        request: dts_20200101_models.ModifyDtsJobPasswordRequest,
    ) -> dts_20200101_models.ModifyDtsJobPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_dts_job_password_with_options(request, runtime)

    async def modify_dts_job_password_async(
        self,
        request: dts_20200101_models.ModifyDtsJobPasswordRequest,
    ) -> dts_20200101_models.ModifyDtsJobPasswordResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_dts_job_password_with_options_async(request, runtime)

    def modify_subscription_with_options(
        self,
        request: dts_20200101_models.ModifySubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifySubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_list):
            query['DbList'] = request.db_list
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_data_type_ddl):
            query['SubscriptionDataTypeDDL'] = request.subscription_data_type_ddl
        if not UtilClient.is_unset(request.subscription_data_type_dml):
            query['SubscriptionDataTypeDML'] = request.subscription_data_type_dml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySubscription',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifySubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_subscription_with_options_async(
        self,
        request: dts_20200101_models.ModifySubscriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifySubscriptionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.db_list):
            query['DbList'] = request.db_list
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_data_type_ddl):
            query['SubscriptionDataTypeDDL'] = request.subscription_data_type_ddl
        if not UtilClient.is_unset(request.subscription_data_type_dml):
            query['SubscriptionDataTypeDML'] = request.subscription_data_type_dml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySubscription',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifySubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_subscription(
        self,
        request: dts_20200101_models.ModifySubscriptionRequest,
    ) -> dts_20200101_models.ModifySubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_subscription_with_options(request, runtime)

    async def modify_subscription_async(
        self,
        request: dts_20200101_models.ModifySubscriptionRequest,
    ) -> dts_20200101_models.ModifySubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_subscription_with_options_async(request, runtime)

    def modify_subscription_object_with_options(
        self,
        request: dts_20200101_models.ModifySubscriptionObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifySubscriptionObjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not UtilClient.is_unset(request.subscription_object):
            query['SubscriptionObject'] = request.subscription_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySubscriptionObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifySubscriptionObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_subscription_object_with_options_async(
        self,
        request: dts_20200101_models.ModifySubscriptionObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifySubscriptionObjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        if not UtilClient.is_unset(request.subscription_object):
            query['SubscriptionObject'] = request.subscription_object
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySubscriptionObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifySubscriptionObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_subscription_object(
        self,
        request: dts_20200101_models.ModifySubscriptionObjectRequest,
    ) -> dts_20200101_models.ModifySubscriptionObjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_subscription_object_with_options(request, runtime)

    async def modify_subscription_object_async(
        self,
        request: dts_20200101_models.ModifySubscriptionObjectRequest,
    ) -> dts_20200101_models.ModifySubscriptionObjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_subscription_object_with_options_async(request, runtime)

    def modify_synchronization_object_with_options(
        self,
        request: dts_20200101_models.ModifySynchronizationObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifySynchronizationObjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        body = {}
        if not UtilClient.is_unset(request.synchronization_objects):
            body['SynchronizationObjects'] = request.synchronization_objects
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySynchronizationObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifySynchronizationObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_synchronization_object_with_options_async(
        self,
        request: dts_20200101_models.ModifySynchronizationObjectRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ModifySynchronizationObjectResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        body = {}
        if not UtilClient.is_unset(request.synchronization_objects):
            body['SynchronizationObjects'] = request.synchronization_objects
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifySynchronizationObject',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ModifySynchronizationObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_synchronization_object(
        self,
        request: dts_20200101_models.ModifySynchronizationObjectRequest,
    ) -> dts_20200101_models.ModifySynchronizationObjectResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_synchronization_object_with_options(request, runtime)

    async def modify_synchronization_object_async(
        self,
        request: dts_20200101_models.ModifySynchronizationObjectRequest,
    ) -> dts_20200101_models.ModifySynchronizationObjectResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_synchronization_object_with_options_async(request, runtime)

    def renew_instance_with_options(
        self,
        request: dts_20200101_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buy_count):
            query['BuyCount'] = request.buy_count
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.RenewInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_instance_with_options_async(
        self,
        request: dts_20200101_models.RenewInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.RenewInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buy_count):
            query['BuyCount'] = request.buy_count
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.RenewInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_instance(
        self,
        request: dts_20200101_models.RenewInstanceRequest,
    ) -> dts_20200101_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.renew_instance_with_options(request, runtime)

    async def renew_instance_async(
        self,
        request: dts_20200101_models.RenewInstanceRequest,
    ) -> dts_20200101_models.RenewInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.renew_instance_with_options_async(request, runtime)

    def reset_dts_job_with_options(
        self,
        request: dts_20200101_models.ResetDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ResetDtsJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ResetDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_dts_job_with_options_async(
        self,
        request: dts_20200101_models.ResetDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ResetDtsJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ResetDtsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_dts_job(
        self,
        request: dts_20200101_models.ResetDtsJobRequest,
    ) -> dts_20200101_models.ResetDtsJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_dts_job_with_options(request, runtime)

    async def reset_dts_job_async(
        self,
        request: dts_20200101_models.ResetDtsJobRequest,
    ) -> dts_20200101_models.ResetDtsJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_dts_job_with_options_async(request, runtime)

    def reset_synchronization_job_with_options(
        self,
        request: dts_20200101_models.ResetSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ResetSynchronizationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ResetSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.ResetSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ResetSynchronizationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ResetSynchronizationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_synchronization_job(
        self,
        request: dts_20200101_models.ResetSynchronizationJobRequest,
    ) -> dts_20200101_models.ResetSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.reset_synchronization_job_with_options(request, runtime)

    async def reset_synchronization_job_async(
        self,
        request: dts_20200101_models.ResetSynchronizationJobRequest,
    ) -> dts_20200101_models.ResetSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.reset_synchronization_job_with_options_async(request, runtime)

    def shield_precheck_with_options(
        self,
        request: dts_20200101_models.ShieldPrecheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ShieldPrecheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.precheck_items):
            query['PrecheckItems'] = request.precheck_items
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ShieldPrecheck',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ShieldPrecheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def shield_precheck_with_options_async(
        self,
        request: dts_20200101_models.ShieldPrecheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.ShieldPrecheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.precheck_items):
            query['PrecheckItems'] = request.precheck_items
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ShieldPrecheck',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.ShieldPrecheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def shield_precheck(
        self,
        request: dts_20200101_models.ShieldPrecheckRequest,
    ) -> dts_20200101_models.ShieldPrecheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.shield_precheck_with_options(request, runtime)

    async def shield_precheck_async(
        self,
        request: dts_20200101_models.ShieldPrecheckRequest,
    ) -> dts_20200101_models.ShieldPrecheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.shield_precheck_with_options_async(request, runtime)

    def skip_pre_check_with_options(
        self,
        request: dts_20200101_models.SkipPreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SkipPreCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.skip):
            query['Skip'] = request.skip
        if not UtilClient.is_unset(request.skip_pre_check_items):
            query['SkipPreCheckItems'] = request.skip_pre_check_items
        if not UtilClient.is_unset(request.skip_pre_check_names):
            query['SkipPreCheckNames'] = request.skip_pre_check_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SkipPreCheck',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SkipPreCheckResponse(),
            self.call_api(params, req, runtime)
        )

    async def skip_pre_check_with_options_async(
        self,
        request: dts_20200101_models.SkipPreCheckRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SkipPreCheckResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.skip):
            query['Skip'] = request.skip
        if not UtilClient.is_unset(request.skip_pre_check_items):
            query['SkipPreCheckItems'] = request.skip_pre_check_items
        if not UtilClient.is_unset(request.skip_pre_check_names):
            query['SkipPreCheckNames'] = request.skip_pre_check_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SkipPreCheck',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SkipPreCheckResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def skip_pre_check(
        self,
        request: dts_20200101_models.SkipPreCheckRequest,
    ) -> dts_20200101_models.SkipPreCheckResponse:
        runtime = util_models.RuntimeOptions()
        return self.skip_pre_check_with_options(request, runtime)

    async def skip_pre_check_async(
        self,
        request: dts_20200101_models.SkipPreCheckRequest,
    ) -> dts_20200101_models.SkipPreCheckResponse:
        runtime = util_models.RuntimeOptions()
        return await self.skip_pre_check_with_options_async(request, runtime)

    def start_dts_job_with_options(
        self,
        request: dts_20200101_models.StartDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartDtsJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StartDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_dts_job_with_options_async(
        self,
        request: dts_20200101_models.StartDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartDtsJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StartDtsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_dts_job(
        self,
        request: dts_20200101_models.StartDtsJobRequest,
    ) -> dts_20200101_models.StartDtsJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_dts_job_with_options(request, runtime)

    async def start_dts_job_async(
        self,
        request: dts_20200101_models.StartDtsJobRequest,
    ) -> dts_20200101_models.StartDtsJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_dts_job_with_options_async(request, runtime)

    def start_dts_jobs_with_options(
        self,
        request: dts_20200101_models.StartDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartDtsJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StartDtsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_dts_jobs_with_options_async(
        self,
        request: dts_20200101_models.StartDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartDtsJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StartDtsJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_dts_jobs(
        self,
        request: dts_20200101_models.StartDtsJobsRequest,
    ) -> dts_20200101_models.StartDtsJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_dts_jobs_with_options(request, runtime)

    async def start_dts_jobs_async(
        self,
        request: dts_20200101_models.StartDtsJobsRequest,
    ) -> dts_20200101_models.StartDtsJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_dts_jobs_with_options_async(request, runtime)

    def start_migration_job_with_options(
        self,
        request: dts_20200101_models.StartMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StartMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_migration_job_with_options_async(
        self,
        request: dts_20200101_models.StartMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StartMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_migration_job(
        self,
        request: dts_20200101_models.StartMigrationJobRequest,
    ) -> dts_20200101_models.StartMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_migration_job_with_options(request, runtime)

    async def start_migration_job_async(
        self,
        request: dts_20200101_models.StartMigrationJobRequest,
    ) -> dts_20200101_models.StartMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_migration_job_with_options_async(request, runtime)

    def start_subscription_instance_with_options(
        self,
        request: dts_20200101_models.StartSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartSubscriptionInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StartSubscriptionInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_subscription_instance_with_options_async(
        self,
        request: dts_20200101_models.StartSubscriptionInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartSubscriptionInstanceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.subscription_instance_id):
            query['SubscriptionInstanceId'] = request.subscription_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSubscriptionInstance',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StartSubscriptionInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_subscription_instance(
        self,
        request: dts_20200101_models.StartSubscriptionInstanceRequest,
    ) -> dts_20200101_models.StartSubscriptionInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_subscription_instance_with_options(request, runtime)

    async def start_subscription_instance_async(
        self,
        request: dts_20200101_models.StartSubscriptionInstanceRequest,
    ) -> dts_20200101_models.StartSubscriptionInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_subscription_instance_with_options_async(request, runtime)

    def start_synchronization_job_with_options(
        self,
        request: dts_20200101_models.StartSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartSynchronizationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StartSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.StartSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StartSynchronizationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StartSynchronizationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_synchronization_job(
        self,
        request: dts_20200101_models.StartSynchronizationJobRequest,
    ) -> dts_20200101_models.StartSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_synchronization_job_with_options(request, runtime)

    async def start_synchronization_job_async(
        self,
        request: dts_20200101_models.StartSynchronizationJobRequest,
    ) -> dts_20200101_models.StartSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_synchronization_job_with_options_async(request, runtime)

    def stop_dts_job_with_options(
        self,
        request: dts_20200101_models.StopDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StopDtsJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StopDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_dts_job_with_options_async(
        self,
        request: dts_20200101_models.StopDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StopDtsJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StopDtsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_dts_job(
        self,
        request: dts_20200101_models.StopDtsJobRequest,
    ) -> dts_20200101_models.StopDtsJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_dts_job_with_options(request, runtime)

    async def stop_dts_job_async(
        self,
        request: dts_20200101_models.StopDtsJobRequest,
    ) -> dts_20200101_models.StopDtsJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_dts_job_with_options_async(request, runtime)

    def stop_dts_jobs_with_options(
        self,
        request: dts_20200101_models.StopDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StopDtsJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StopDtsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_dts_jobs_with_options_async(
        self,
        request: dts_20200101_models.StopDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StopDtsJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StopDtsJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_dts_jobs(
        self,
        request: dts_20200101_models.StopDtsJobsRequest,
    ) -> dts_20200101_models.StopDtsJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_dts_jobs_with_options(request, runtime)

    async def stop_dts_jobs_async(
        self,
        request: dts_20200101_models.StopDtsJobsRequest,
    ) -> dts_20200101_models.StopDtsJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_dts_jobs_with_options_async(request, runtime)

    def stop_migration_job_with_options(
        self,
        request: dts_20200101_models.StopMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StopMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StopMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_migration_job_with_options_async(
        self,
        request: dts_20200101_models.StopMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.StopMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.StopMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_migration_job(
        self,
        request: dts_20200101_models.StopMigrationJobRequest,
    ) -> dts_20200101_models.StopMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_migration_job_with_options(request, runtime)

    async def stop_migration_job_async(
        self,
        request: dts_20200101_models.StopMigrationJobRequest,
    ) -> dts_20200101_models.StopMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_migration_job_with_options_async(request, runtime)

    def summary_job_detail_with_options(
        self,
        request: dts_20200101_models.SummaryJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SummaryJobDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_code):
            query['JobCode'] = request.job_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SummaryJobDetail',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SummaryJobDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def summary_job_detail_with_options_async(
        self,
        request: dts_20200101_models.SummaryJobDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SummaryJobDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.job_code):
            query['JobCode'] = request.job_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SummaryJobDetail',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SummaryJobDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def summary_job_detail(
        self,
        request: dts_20200101_models.SummaryJobDetailRequest,
    ) -> dts_20200101_models.SummaryJobDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.summary_job_detail_with_options(request, runtime)

    async def summary_job_detail_async(
        self,
        request: dts_20200101_models.SummaryJobDetailRequest,
    ) -> dts_20200101_models.SummaryJobDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.summary_job_detail_with_options_async(request, runtime)

    def suspend_dts_job_with_options(
        self,
        request: dts_20200101_models.SuspendDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendDtsJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SuspendDtsJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_dts_job_with_options_async(
        self,
        request: dts_20200101_models.SuspendDtsJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendDtsJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_instance_id):
            query['DtsInstanceId'] = request.dts_instance_id
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendDtsJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SuspendDtsJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_dts_job(
        self,
        request: dts_20200101_models.SuspendDtsJobRequest,
    ) -> dts_20200101_models.SuspendDtsJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_dts_job_with_options(request, runtime)

    async def suspend_dts_job_async(
        self,
        request: dts_20200101_models.SuspendDtsJobRequest,
    ) -> dts_20200101_models.SuspendDtsJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_dts_job_with_options_async(request, runtime)

    def suspend_dts_jobs_with_options(
        self,
        request: dts_20200101_models.SuspendDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendDtsJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SuspendDtsJobsResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_dts_jobs_with_options_async(
        self,
        request: dts_20200101_models.SuspendDtsJobsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendDtsJobsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_ids):
            query['DtsJobIds'] = request.dts_job_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendDtsJobs',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SuspendDtsJobsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_dts_jobs(
        self,
        request: dts_20200101_models.SuspendDtsJobsRequest,
    ) -> dts_20200101_models.SuspendDtsJobsResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_dts_jobs_with_options(request, runtime)

    async def suspend_dts_jobs_async(
        self,
        request: dts_20200101_models.SuspendDtsJobsRequest,
    ) -> dts_20200101_models.SuspendDtsJobsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_dts_jobs_with_options_async(request, runtime)

    def suspend_migration_job_with_options(
        self,
        request: dts_20200101_models.SuspendMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SuspendMigrationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_migration_job_with_options_async(
        self,
        request: dts_20200101_models.SuspendMigrationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendMigrationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.migration_job_id):
            query['MigrationJobId'] = request.migration_job_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendMigrationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SuspendMigrationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_migration_job(
        self,
        request: dts_20200101_models.SuspendMigrationJobRequest,
    ) -> dts_20200101_models.SuspendMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_migration_job_with_options(request, runtime)

    async def suspend_migration_job_async(
        self,
        request: dts_20200101_models.SuspendMigrationJobRequest,
    ) -> dts_20200101_models.SuspendMigrationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_migration_job_with_options_async(request, runtime)

    def suspend_synchronization_job_with_options(
        self,
        request: dts_20200101_models.SuspendSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendSynchronizationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SuspendSynchronizationJobResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_synchronization_job_with_options_async(
        self,
        request: dts_20200101_models.SuspendSynchronizationJobRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SuspendSynchronizationJobResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SuspendSynchronizationJob',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SuspendSynchronizationJobResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_synchronization_job(
        self,
        request: dts_20200101_models.SuspendSynchronizationJobRequest,
    ) -> dts_20200101_models.SuspendSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_synchronization_job_with_options(request, runtime)

    async def suspend_synchronization_job_async(
        self,
        request: dts_20200101_models.SuspendSynchronizationJobRequest,
    ) -> dts_20200101_models.SuspendSynchronizationJobResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_synchronization_job_with_options_async(request, runtime)

    def switch_synchronization_endpoint_with_options(
        self,
        request: dts_20200101_models.SwitchSynchronizationEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SwitchSynchronizationEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchSynchronizationEndpoint',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SwitchSynchronizationEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def switch_synchronization_endpoint_with_options_async(
        self,
        request: dts_20200101_models.SwitchSynchronizationEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.SwitchSynchronizationEndpointResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.synchronization_direction):
            query['SynchronizationDirection'] = request.synchronization_direction
        if not UtilClient.is_unset(request.synchronization_job_id):
            query['SynchronizationJobId'] = request.synchronization_job_id
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.source_endpoint):
            query['SourceEndpoint'] = request.source_endpoint
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchSynchronizationEndpoint',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.SwitchSynchronizationEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def switch_synchronization_endpoint(
        self,
        request: dts_20200101_models.SwitchSynchronizationEndpointRequest,
    ) -> dts_20200101_models.SwitchSynchronizationEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return self.switch_synchronization_endpoint_with_options(request, runtime)

    async def switch_synchronization_endpoint_async(
        self,
        request: dts_20200101_models.SwitchSynchronizationEndpointRequest,
    ) -> dts_20200101_models.SwitchSynchronizationEndpointResponse:
        runtime = util_models.RuntimeOptions()
        return await self.switch_synchronization_endpoint_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: dts_20200101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: dts_20200101_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.TagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: dts_20200101_models.TagResourcesRequest,
    ) -> dts_20200101_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: dts_20200101_models.TagResourcesRequest,
    ) -> dts_20200101_models.TagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def transfer_instance_class_with_options(
        self,
        request: dts_20200101_models.TransferInstanceClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.TransferInstanceClassResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferInstanceClass',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.TransferInstanceClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_instance_class_with_options_async(
        self,
        request: dts_20200101_models.TransferInstanceClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.TransferInstanceClassResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferInstanceClass',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.TransferInstanceClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_instance_class(
        self,
        request: dts_20200101_models.TransferInstanceClassRequest,
    ) -> dts_20200101_models.TransferInstanceClassResponse:
        runtime = util_models.RuntimeOptions()
        return self.transfer_instance_class_with_options(request, runtime)

    async def transfer_instance_class_async(
        self,
        request: dts_20200101_models.TransferInstanceClassRequest,
    ) -> dts_20200101_models.TransferInstanceClassResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_instance_class_with_options_async(request, runtime)

    def transfer_pay_type_with_options(
        self,
        request: dts_20200101_models.TransferPayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.TransferPayTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buy_count):
            query['BuyCount'] = request.buy_count
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferPayType',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.TransferPayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_pay_type_with_options_async(
        self,
        request: dts_20200101_models.TransferPayTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.TransferPayTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.buy_count):
            query['BuyCount'] = request.buy_count
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.dts_job_id):
            query['DtsJobId'] = request.dts_job_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferPayType',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.TransferPayTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_pay_type(
        self,
        request: dts_20200101_models.TransferPayTypeRequest,
    ) -> dts_20200101_models.TransferPayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.transfer_pay_type_with_options(request, runtime)

    async def transfer_pay_type_async(
        self,
        request: dts_20200101_models.TransferPayTypeRequest,
    ) -> dts_20200101_models.TransferPayTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.transfer_pay_type_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: dts_20200101_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: dts_20200101_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.UntagResourcesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: dts_20200101_models.UntagResourcesRequest,
    ) -> dts_20200101_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: dts_20200101_models.UntagResourcesRequest,
    ) -> dts_20200101_models.UntagResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def upgrade_two_way_with_options(
        self,
        request: dts_20200101_models.UpgradeTwoWayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.UpgradeTwoWayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeTwoWay',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.UpgradeTwoWayResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_two_way_with_options_async(
        self,
        request: dts_20200101_models.UpgradeTwoWayRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.UpgradeTwoWayResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeTwoWay',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.UpgradeTwoWayResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_two_way(
        self,
        request: dts_20200101_models.UpgradeTwoWayRequest,
    ) -> dts_20200101_models.UpgradeTwoWayResponse:
        runtime = util_models.RuntimeOptions()
        return self.upgrade_two_way_with_options(request, runtime)

    async def upgrade_two_way_async(
        self,
        request: dts_20200101_models.UpgradeTwoWayRequest,
    ) -> dts_20200101_models.UpgradeTwoWayResponse:
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_two_way_with_options_async(request, runtime)

    def white_ip_list_with_options(
        self,
        request: dts_20200101_models.WhiteIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.WhiteIpListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_region):
            query['DestinationRegion'] = request.destination_region
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WhiteIpList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.WhiteIpListResponse(),
            self.call_api(params, req, runtime)
        )

    async def white_ip_list_with_options_async(
        self,
        request: dts_20200101_models.WhiteIpListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dts_20200101_models.WhiteIpListResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_region):
            query['DestinationRegion'] = request.destination_region
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='WhiteIpList',
            version='2020-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dts_20200101_models.WhiteIpListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def white_ip_list(
        self,
        request: dts_20200101_models.WhiteIpListRequest,
    ) -> dts_20200101_models.WhiteIpListResponse:
        runtime = util_models.RuntimeOptions()
        return self.white_ip_list_with_options(request, runtime)

    async def white_ip_list_async(
        self,
        request: dts_20200101_models.WhiteIpListRequest,
    ) -> dts_20200101_models.WhiteIpListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.white_ip_list_with_options_async(request, runtime)
