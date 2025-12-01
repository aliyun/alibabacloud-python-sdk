# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dbs20190306 import models as dbs_20190306_models
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
            'cn-qingdao': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-beijing': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-chengdu': 'dbs-api.cn-chengdu.aliyuncs.com',
            'cn-zhangjiakou': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-huhehaote': 'dbs-api.cn-huhehaote.aliyuncs.com',
            'cn-hangzhou': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shanghai': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-hongkong': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'ap-southeast-1': 'dbs-api.ap-southeast-1.aliyuncs.com',
            'ap-southeast-2': 'dbs-api.ap-southeast-2.aliyuncs.com',
            'ap-southeast-3': 'dbs-api.ap-southeast-3.aliyuncs.com',
            'ap-southeast-5': 'dbs-api.ap-southeast-5.aliyuncs.com',
            'ap-northeast-1': 'dbs-api.ap-northeast-1.aliyuncs.com',
            'us-west-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'us-east-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'eu-central-1': 'dbs-api.eu-central-1.aliyuncs.com',
            'cn-hangzhou-finance': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shanghai-finance-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'cn-shenzhen-finance-1': 'dbs-api.cn-hangzhou.aliyuncs.com',
            'ap-south-1': 'dbs-api.ap-south-1.aliyuncs.com',
            'eu-west-1': 'dbs-api.eu-west-1.aliyuncs.com',
            'me-east-1': 'dbs-api.me-east-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dbs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def configure_backup_plan_with_options(
        self,
        request: dbs_20190306_models.ConfigureBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ConfigureBackupPlanResponse:
        """
        @summary Configures a DBS backup schedule.
        
        @param request: ConfigureBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_start_backup):
            query['AutoStartBackup'] = request.auto_start_backup
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.backup_log_interval_seconds):
            query['BackupLogIntervalSeconds'] = request.backup_log_interval_seconds
        if not UtilClient.is_unset(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not UtilClient.is_unset(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not UtilClient.is_unset(request.backup_rate_limit):
            query['BackupRateLimit'] = request.backup_rate_limit
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.backup_speed_limit):
            query['BackupSpeedLimit'] = request.backup_speed_limit
        if not UtilClient.is_unset(request.backup_start_time):
            query['BackupStartTime'] = request.backup_start_time
        if not UtilClient.is_unset(request.backup_storage_type):
            query['BackupStorageType'] = request.backup_storage_type
        if not UtilClient.is_unset(request.backup_strategy_type):
            query['BackupStrategyType'] = request.backup_strategy_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not UtilClient.is_unset(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not UtilClient.is_unset(request.duplication_archive_period):
            query['DuplicationArchivePeriod'] = request.duplication_archive_period
        if not UtilClient.is_unset(request.duplication_infrequent_access_period):
            query['DuplicationInfrequentAccessPeriod'] = request.duplication_infrequent_access_period
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.ossbucket_name):
            query['OSSBucketName'] = request.ossbucket_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
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
            action='ConfigureBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ConfigureBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_backup_plan_with_options_async(
        self,
        request: dbs_20190306_models.ConfigureBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ConfigureBackupPlanResponse:
        """
        @summary Configures a DBS backup schedule.
        
        @param request: ConfigureBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ConfigureBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_start_backup):
            query['AutoStartBackup'] = request.auto_start_backup
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.backup_log_interval_seconds):
            query['BackupLogIntervalSeconds'] = request.backup_log_interval_seconds
        if not UtilClient.is_unset(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not UtilClient.is_unset(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not UtilClient.is_unset(request.backup_rate_limit):
            query['BackupRateLimit'] = request.backup_rate_limit
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.backup_speed_limit):
            query['BackupSpeedLimit'] = request.backup_speed_limit
        if not UtilClient.is_unset(request.backup_start_time):
            query['BackupStartTime'] = request.backup_start_time
        if not UtilClient.is_unset(request.backup_storage_type):
            query['BackupStorageType'] = request.backup_storage_type
        if not UtilClient.is_unset(request.backup_strategy_type):
            query['BackupStrategyType'] = request.backup_strategy_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not UtilClient.is_unset(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not UtilClient.is_unset(request.duplication_archive_period):
            query['DuplicationArchivePeriod'] = request.duplication_archive_period
        if not UtilClient.is_unset(request.duplication_infrequent_access_period):
            query['DuplicationInfrequentAccessPeriod'] = request.duplication_infrequent_access_period
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.ossbucket_name):
            query['OSSBucketName'] = request.ossbucket_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
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
            action='ConfigureBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ConfigureBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_backup_plan(
        self,
        request: dbs_20190306_models.ConfigureBackupPlanRequest,
    ) -> dbs_20190306_models.ConfigureBackupPlanResponse:
        """
        @summary Configures a DBS backup schedule.
        
        @param request: ConfigureBackupPlanRequest
        @return: ConfigureBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.configure_backup_plan_with_options(request, runtime)

    async def configure_backup_plan_async(
        self,
        request: dbs_20190306_models.ConfigureBackupPlanRequest,
    ) -> dbs_20190306_models.ConfigureBackupPlanResponse:
        """
        @summary Configures a DBS backup schedule.
        
        @param request: ConfigureBackupPlanRequest
        @return: ConfigureBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.configure_backup_plan_with_options_async(request, runtime)

    def create_and_start_backup_plan_with_options(
        self,
        request: dbs_20190306_models.CreateAndStartBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateAndStartBackupPlanResponse:
        """
        @summary Creates, configures, and starts a backup schedule.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://help.aliyun.com/document_detail/70005.html) of Database Backup (DBS).
        
        @param request: CreateAndStartBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAndStartBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.backup_log_interval_seconds):
            query['BackupLogIntervalSeconds'] = request.backup_log_interval_seconds
        if not UtilClient.is_unset(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not UtilClient.is_unset(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not UtilClient.is_unset(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not UtilClient.is_unset(request.backup_rate_limit):
            query['BackupRateLimit'] = request.backup_rate_limit
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.backup_speed_limit):
            query['BackupSpeedLimit'] = request.backup_speed_limit
        if not UtilClient.is_unset(request.backup_start_time):
            query['BackupStartTime'] = request.backup_start_time
        if not UtilClient.is_unset(request.backup_storage_type):
            query['BackupStorageType'] = request.backup_storage_type
        if not UtilClient.is_unset(request.backup_strategy_type):
            query['BackupStrategyType'] = request.backup_strategy_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not UtilClient.is_unset(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not UtilClient.is_unset(request.database_region):
            query['DatabaseRegion'] = request.database_region
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.duplication_archive_period):
            query['DuplicationArchivePeriod'] = request.duplication_archive_period
        if not UtilClient.is_unset(request.duplication_infrequent_access_period):
            query['DuplicationInfrequentAccessPeriod'] = request.duplication_infrequent_access_period
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.ossbucket_name):
            query['OSSBucketName'] = request.ossbucket_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
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
        if not UtilClient.is_unset(request.storage_region):
            query['StorageRegion'] = request.storage_region
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAndStartBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateAndStartBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_and_start_backup_plan_with_options_async(
        self,
        request: dbs_20190306_models.CreateAndStartBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateAndStartBackupPlanResponse:
        """
        @summary Creates, configures, and starts a backup schedule.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://help.aliyun.com/document_detail/70005.html) of Database Backup (DBS).
        
        @param request: CreateAndStartBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAndStartBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.backup_log_interval_seconds):
            query['BackupLogIntervalSeconds'] = request.backup_log_interval_seconds
        if not UtilClient.is_unset(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not UtilClient.is_unset(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not UtilClient.is_unset(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not UtilClient.is_unset(request.backup_rate_limit):
            query['BackupRateLimit'] = request.backup_rate_limit
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.backup_speed_limit):
            query['BackupSpeedLimit'] = request.backup_speed_limit
        if not UtilClient.is_unset(request.backup_start_time):
            query['BackupStartTime'] = request.backup_start_time
        if not UtilClient.is_unset(request.backup_storage_type):
            query['BackupStorageType'] = request.backup_storage_type
        if not UtilClient.is_unset(request.backup_strategy_type):
            query['BackupStrategyType'] = request.backup_strategy_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not UtilClient.is_unset(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not UtilClient.is_unset(request.database_region):
            query['DatabaseRegion'] = request.database_region
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.duplication_archive_period):
            query['DuplicationArchivePeriod'] = request.duplication_archive_period
        if not UtilClient.is_unset(request.duplication_infrequent_access_period):
            query['DuplicationInfrequentAccessPeriod'] = request.duplication_infrequent_access_period
        if not UtilClient.is_unset(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.ossbucket_name):
            query['OSSBucketName'] = request.ossbucket_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
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
        if not UtilClient.is_unset(request.storage_region):
            query['StorageRegion'] = request.storage_region
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAndStartBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateAndStartBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_and_start_backup_plan(
        self,
        request: dbs_20190306_models.CreateAndStartBackupPlanRequest,
    ) -> dbs_20190306_models.CreateAndStartBackupPlanResponse:
        """
        @summary Creates, configures, and starts a backup schedule.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://help.aliyun.com/document_detail/70005.html) of Database Backup (DBS).
        
        @param request: CreateAndStartBackupPlanRequest
        @return: CreateAndStartBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_and_start_backup_plan_with_options(request, runtime)

    async def create_and_start_backup_plan_async(
        self,
        request: dbs_20190306_models.CreateAndStartBackupPlanRequest,
    ) -> dbs_20190306_models.CreateAndStartBackupPlanResponse:
        """
        @summary Creates, configures, and starts a backup schedule.
        
        @description Before you call this operation, make sure that you fully understand the billing methods and [pricing](https://help.aliyun.com/document_detail/70005.html) of Database Backup (DBS).
        
        @param request: CreateAndStartBackupPlanRequest
        @return: CreateAndStartBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_and_start_backup_plan_with_options_async(request, runtime)

    def create_backup_plan_with_options(
        self,
        request: dbs_20190306_models.CreateBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateBackupPlanResponse:
        """
        @summary Creates a backup schedule.
        
        @description For more information about how to create a backup schedule in the Database Backup (DBS) console, see [Purchase a backup schedule](https://help.aliyun.com/document_detail/65909.html).
        
        @param request: CreateBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_region):
            query['DatabaseRegion'] = request.database_region
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.storage_region):
            query['StorageRegion'] = request.storage_region
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_plan_with_options_async(
        self,
        request: dbs_20190306_models.CreateBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateBackupPlanResponse:
        """
        @summary Creates a backup schedule.
        
        @description For more information about how to create a backup schedule in the Database Backup (DBS) console, see [Purchase a backup schedule](https://help.aliyun.com/document_detail/65909.html).
        
        @param request: CreateBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_region):
            query['DatabaseRegion'] = request.database_region
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.from_app):
            query['FromApp'] = request.from_app
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.storage_region):
            query['StorageRegion'] = request.storage_region
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup_plan(
        self,
        request: dbs_20190306_models.CreateBackupPlanRequest,
    ) -> dbs_20190306_models.CreateBackupPlanResponse:
        """
        @summary Creates a backup schedule.
        
        @description For more information about how to create a backup schedule in the Database Backup (DBS) console, see [Purchase a backup schedule](https://help.aliyun.com/document_detail/65909.html).
        
        @param request: CreateBackupPlanRequest
        @return: CreateBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_backup_plan_with_options(request, runtime)

    async def create_backup_plan_async(
        self,
        request: dbs_20190306_models.CreateBackupPlanRequest,
    ) -> dbs_20190306_models.CreateBackupPlanResponse:
        """
        @summary Creates a backup schedule.
        
        @description For more information about how to create a backup schedule in the Database Backup (DBS) console, see [Purchase a backup schedule](https://help.aliyun.com/document_detail/65909.html).
        
        @param request: CreateBackupPlanRequest
        @return: CreateBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_plan_with_options_async(request, runtime)

    def create_full_backup_set_download_with_options(
        self,
        request: dbs_20190306_models.CreateFullBackupSetDownloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateFullBackupSetDownloadResponse:
        """
        @summary Creates and starts a full backup set download task.
        
        @param request: CreateFullBackupSetDownloadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFullBackupSetDownloadResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_data_format):
            query['BackupSetDataFormat'] = request.backup_set_data_format
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFullBackupSetDownload',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateFullBackupSetDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_full_backup_set_download_with_options_async(
        self,
        request: dbs_20190306_models.CreateFullBackupSetDownloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateFullBackupSetDownloadResponse:
        """
        @summary Creates and starts a full backup set download task.
        
        @param request: CreateFullBackupSetDownloadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateFullBackupSetDownloadResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_data_format):
            query['BackupSetDataFormat'] = request.backup_set_data_format
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFullBackupSetDownload',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateFullBackupSetDownloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_full_backup_set_download(
        self,
        request: dbs_20190306_models.CreateFullBackupSetDownloadRequest,
    ) -> dbs_20190306_models.CreateFullBackupSetDownloadResponse:
        """
        @summary Creates and starts a full backup set download task.
        
        @param request: CreateFullBackupSetDownloadRequest
        @return: CreateFullBackupSetDownloadResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_full_backup_set_download_with_options(request, runtime)

    async def create_full_backup_set_download_async(
        self,
        request: dbs_20190306_models.CreateFullBackupSetDownloadRequest,
    ) -> dbs_20190306_models.CreateFullBackupSetDownloadResponse:
        """
        @summary Creates and starts a full backup set download task.
        
        @param request: CreateFullBackupSetDownloadRequest
        @return: CreateFullBackupSetDownloadResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_full_backup_set_download_with_options_async(request, runtime)

    def create_get_dblist_from_agent_task_with_options(
        self,
        request: dbs_20190306_models.CreateGetDBListFromAgentTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateGetDBListFromAgentTaskResponse:
        """
        @summary Creates a task to obtain a database list by using a backup gateway.
        
        @description This API operation returns a task ID. You can call the [GetDBListFromAgent](https://help.aliyun.com/document_detail/2869852.html) operation to query the task result based on the task ID.
        
        @param request: CreateGetDBListFromAgentTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGetDBListFromAgentTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGetDBListFromAgentTask',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateGetDBListFromAgentTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_get_dblist_from_agent_task_with_options_async(
        self,
        request: dbs_20190306_models.CreateGetDBListFromAgentTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateGetDBListFromAgentTaskResponse:
        """
        @summary Creates a task to obtain a database list by using a backup gateway.
        
        @description This API operation returns a task ID. You can call the [GetDBListFromAgent](https://help.aliyun.com/document_detail/2869852.html) operation to query the task result based on the task ID.
        
        @param request: CreateGetDBListFromAgentTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateGetDBListFromAgentTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.database_type):
            query['DatabaseType'] = request.database_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not UtilClient.is_unset(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGetDBListFromAgentTask',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateGetDBListFromAgentTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_get_dblist_from_agent_task(
        self,
        request: dbs_20190306_models.CreateGetDBListFromAgentTaskRequest,
    ) -> dbs_20190306_models.CreateGetDBListFromAgentTaskResponse:
        """
        @summary Creates a task to obtain a database list by using a backup gateway.
        
        @description This API operation returns a task ID. You can call the [GetDBListFromAgent](https://help.aliyun.com/document_detail/2869852.html) operation to query the task result based on the task ID.
        
        @param request: CreateGetDBListFromAgentTaskRequest
        @return: CreateGetDBListFromAgentTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_get_dblist_from_agent_task_with_options(request, runtime)

    async def create_get_dblist_from_agent_task_async(
        self,
        request: dbs_20190306_models.CreateGetDBListFromAgentTaskRequest,
    ) -> dbs_20190306_models.CreateGetDBListFromAgentTaskResponse:
        """
        @summary Creates a task to obtain a database list by using a backup gateway.
        
        @description This API operation returns a task ID. You can call the [GetDBListFromAgent](https://help.aliyun.com/document_detail/2869852.html) operation to query the task result based on the task ID.
        
        @param request: CreateGetDBListFromAgentTaskRequest
        @return: CreateGetDBListFromAgentTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_get_dblist_from_agent_task_with_options_async(request, runtime)

    def create_increment_backup_set_download_with_options(
        self,
        request: dbs_20190306_models.CreateIncrementBackupSetDownloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateIncrementBackupSetDownloadResponse:
        """
        @summary Creates and starts an incremental backup set download task.
        
        @param request: CreateIncrementBackupSetDownloadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIncrementBackupSetDownloadResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_data_format):
            query['BackupSetDataFormat'] = request.backup_set_data_format
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.backup_set_name):
            query['BackupSetName'] = request.backup_set_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIncrementBackupSetDownload',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateIncrementBackupSetDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_increment_backup_set_download_with_options_async(
        self,
        request: dbs_20190306_models.CreateIncrementBackupSetDownloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateIncrementBackupSetDownloadResponse:
        """
        @summary Creates and starts an incremental backup set download task.
        
        @param request: CreateIncrementBackupSetDownloadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateIncrementBackupSetDownloadResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_set_data_format):
            query['BackupSetDataFormat'] = request.backup_set_data_format
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.backup_set_name):
            query['BackupSetName'] = request.backup_set_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIncrementBackupSetDownload',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateIncrementBackupSetDownloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_increment_backup_set_download(
        self,
        request: dbs_20190306_models.CreateIncrementBackupSetDownloadRequest,
    ) -> dbs_20190306_models.CreateIncrementBackupSetDownloadResponse:
        """
        @summary Creates and starts an incremental backup set download task.
        
        @param request: CreateIncrementBackupSetDownloadRequest
        @return: CreateIncrementBackupSetDownloadResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_increment_backup_set_download_with_options(request, runtime)

    async def create_increment_backup_set_download_async(
        self,
        request: dbs_20190306_models.CreateIncrementBackupSetDownloadRequest,
    ) -> dbs_20190306_models.CreateIncrementBackupSetDownloadResponse:
        """
        @summary Creates and starts an incremental backup set download task.
        
        @param request: CreateIncrementBackupSetDownloadRequest
        @return: CreateIncrementBackupSetDownloadResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_increment_backup_set_download_with_options_async(request, runtime)

    def create_restore_task_with_options(
        self,
        request: dbs_20190306_models.CreateRestoreTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateRestoreTaskResponse:
        """
        @summary Creates a restoration task.
        
        @param request: CreateRestoreTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRestoreTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not UtilClient.is_unset(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not UtilClient.is_unset(request.destination_endpoint_database_name):
            query['DestinationEndpointDatabaseName'] = request.destination_endpoint_database_name
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
        if not UtilClient.is_unset(request.duplicate_conflict):
            query['DuplicateConflict'] = request.duplicate_conflict
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.restore_dir):
            query['RestoreDir'] = request.restore_dir
        if not UtilClient.is_unset(request.restore_home):
            query['RestoreHome'] = request.restore_home
        if not UtilClient.is_unset(request.restore_objects):
            query['RestoreObjects'] = request.restore_objects
        if not UtilClient.is_unset(request.restore_task_name):
            query['RestoreTaskName'] = request.restore_task_name
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRestoreTask',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateRestoreTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_restore_task_with_options_async(
        self,
        request: dbs_20190306_models.CreateRestoreTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.CreateRestoreTaskResponse:
        """
        @summary Creates a restoration task.
        
        @param request: CreateRestoreTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateRestoreTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not UtilClient.is_unset(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not UtilClient.is_unset(request.destination_endpoint_database_name):
            query['DestinationEndpointDatabaseName'] = request.destination_endpoint_database_name
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
        if not UtilClient.is_unset(request.duplicate_conflict):
            query['DuplicateConflict'] = request.duplicate_conflict
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.restore_dir):
            query['RestoreDir'] = request.restore_dir
        if not UtilClient.is_unset(request.restore_home):
            query['RestoreHome'] = request.restore_home
        if not UtilClient.is_unset(request.restore_objects):
            query['RestoreObjects'] = request.restore_objects
        if not UtilClient.is_unset(request.restore_task_name):
            query['RestoreTaskName'] = request.restore_task_name
        if not UtilClient.is_unset(request.restore_time):
            query['RestoreTime'] = request.restore_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRestoreTask',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.CreateRestoreTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_restore_task(
        self,
        request: dbs_20190306_models.CreateRestoreTaskRequest,
    ) -> dbs_20190306_models.CreateRestoreTaskResponse:
        """
        @summary Creates a restoration task.
        
        @param request: CreateRestoreTaskRequest
        @return: CreateRestoreTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_restore_task_with_options(request, runtime)

    async def create_restore_task_async(
        self,
        request: dbs_20190306_models.CreateRestoreTaskRequest,
    ) -> dbs_20190306_models.CreateRestoreTaskResponse:
        """
        @summary Creates a restoration task.
        
        @param request: CreateRestoreTaskRequest
        @return: CreateRestoreTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_restore_task_with_options_async(request, runtime)

    def describe_backup_gateway_list_with_options(
        self,
        request: dbs_20190306_models.DescribeBackupGatewayListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeBackupGatewayListResponse:
        """
        @summary Queries backup gateways.
        
        @param request: DescribeBackupGatewayListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupGatewayListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupGatewayList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeBackupGatewayListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_gateway_list_with_options_async(
        self,
        request: dbs_20190306_models.DescribeBackupGatewayListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeBackupGatewayListResponse:
        """
        @summary Queries backup gateways.
        
        @param request: DescribeBackupGatewayListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupGatewayListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupGatewayList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeBackupGatewayListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_gateway_list(
        self,
        request: dbs_20190306_models.DescribeBackupGatewayListRequest,
    ) -> dbs_20190306_models.DescribeBackupGatewayListResponse:
        """
        @summary Queries backup gateways.
        
        @param request: DescribeBackupGatewayListRequest
        @return: DescribeBackupGatewayListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_gateway_list_with_options(request, runtime)

    async def describe_backup_gateway_list_async(
        self,
        request: dbs_20190306_models.DescribeBackupGatewayListRequest,
    ) -> dbs_20190306_models.DescribeBackupGatewayListResponse:
        """
        @summary Queries backup gateways.
        
        @param request: DescribeBackupGatewayListRequest
        @return: DescribeBackupGatewayListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_gateway_list_with_options_async(request, runtime)

    def describe_backup_plan_billing_with_options(
        self,
        request: dbs_20190306_models.DescribeBackupPlanBillingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeBackupPlanBillingResponse:
        """
        @summary Queries the billing information of a backup schedule.
        
        @param request: DescribeBackupPlanBillingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPlanBillingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.show_storage_type):
            query['ShowStorageType'] = request.show_storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPlanBilling',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeBackupPlanBillingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_plan_billing_with_options_async(
        self,
        request: dbs_20190306_models.DescribeBackupPlanBillingRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeBackupPlanBillingResponse:
        """
        @summary Queries the billing information of a backup schedule.
        
        @param request: DescribeBackupPlanBillingRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPlanBillingResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.show_storage_type):
            query['ShowStorageType'] = request.show_storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPlanBilling',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeBackupPlanBillingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_plan_billing(
        self,
        request: dbs_20190306_models.DescribeBackupPlanBillingRequest,
    ) -> dbs_20190306_models.DescribeBackupPlanBillingResponse:
        """
        @summary Queries the billing information of a backup schedule.
        
        @param request: DescribeBackupPlanBillingRequest
        @return: DescribeBackupPlanBillingResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_plan_billing_with_options(request, runtime)

    async def describe_backup_plan_billing_async(
        self,
        request: dbs_20190306_models.DescribeBackupPlanBillingRequest,
    ) -> dbs_20190306_models.DescribeBackupPlanBillingResponse:
        """
        @summary Queries the billing information of a backup schedule.
        
        @param request: DescribeBackupPlanBillingRequest
        @return: DescribeBackupPlanBillingResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_plan_billing_with_options_async(request, runtime)

    def describe_backup_plan_list_with_options(
        self,
        request: dbs_20190306_models.DescribeBackupPlanListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeBackupPlanListResponse:
        """
        @summary Query the list of backup plans
        
        @description Before using this interface, please activate the OSS service in advance. For more information, see [Object Storage Service (OSS)](https://help.aliyun.com/document_detail/31817.html).
        
        @param request: DescribeBackupPlanListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPlanListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not UtilClient.is_unset(request.backup_plan_status):
            query['BackupPlanStatus'] = request.backup_plan_status
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPlanList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeBackupPlanListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_plan_list_with_options_async(
        self,
        request: dbs_20190306_models.DescribeBackupPlanListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeBackupPlanListResponse:
        """
        @summary Query the list of backup plans
        
        @description Before using this interface, please activate the OSS service in advance. For more information, see [Object Storage Service (OSS)](https://help.aliyun.com/document_detail/31817.html).
        
        @param request: DescribeBackupPlanListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPlanListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not UtilClient.is_unset(request.backup_plan_status):
            query['BackupPlanStatus'] = request.backup_plan_status
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPlanList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeBackupPlanListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_plan_list(
        self,
        request: dbs_20190306_models.DescribeBackupPlanListRequest,
    ) -> dbs_20190306_models.DescribeBackupPlanListResponse:
        """
        @summary Query the list of backup plans
        
        @description Before using this interface, please activate the OSS service in advance. For more information, see [Object Storage Service (OSS)](https://help.aliyun.com/document_detail/31817.html).
        
        @param request: DescribeBackupPlanListRequest
        @return: DescribeBackupPlanListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_plan_list_with_options(request, runtime)

    async def describe_backup_plan_list_async(
        self,
        request: dbs_20190306_models.DescribeBackupPlanListRequest,
    ) -> dbs_20190306_models.DescribeBackupPlanListResponse:
        """
        @summary Query the list of backup plans
        
        @description Before using this interface, please activate the OSS service in advance. For more information, see [Object Storage Service (OSS)](https://help.aliyun.com/document_detail/31817.html).
        
        @param request: DescribeBackupPlanListRequest
        @return: DescribeBackupPlanListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_plan_list_with_options_async(request, runtime)

    def describe_backup_set_download_task_list_with_options(
        self,
        request: dbs_20190306_models.DescribeBackupSetDownloadTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeBackupSetDownloadTaskListResponse:
        """
        @summary Queries backup set download tasks.
        
        @param request: DescribeBackupSetDownloadTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupSetDownloadTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_download_task_id):
            query['BackupSetDownloadTaskId'] = request.backup_set_download_task_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupSetDownloadTaskList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeBackupSetDownloadTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_set_download_task_list_with_options_async(
        self,
        request: dbs_20190306_models.DescribeBackupSetDownloadTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeBackupSetDownloadTaskListResponse:
        """
        @summary Queries backup set download tasks.
        
        @param request: DescribeBackupSetDownloadTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupSetDownloadTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_download_task_id):
            query['BackupSetDownloadTaskId'] = request.backup_set_download_task_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupSetDownloadTaskList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeBackupSetDownloadTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_set_download_task_list(
        self,
        request: dbs_20190306_models.DescribeBackupSetDownloadTaskListRequest,
    ) -> dbs_20190306_models.DescribeBackupSetDownloadTaskListResponse:
        """
        @summary Queries backup set download tasks.
        
        @param request: DescribeBackupSetDownloadTaskListRequest
        @return: DescribeBackupSetDownloadTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_set_download_task_list_with_options(request, runtime)

    async def describe_backup_set_download_task_list_async(
        self,
        request: dbs_20190306_models.DescribeBackupSetDownloadTaskListRequest,
    ) -> dbs_20190306_models.DescribeBackupSetDownloadTaskListResponse:
        """
        @summary Queries backup set download tasks.
        
        @param request: DescribeBackupSetDownloadTaskListRequest
        @return: DescribeBackupSetDownloadTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_set_download_task_list_with_options_async(request, runtime)

    def describe_dlaservice_with_options(
        self,
        request: dbs_20190306_models.DescribeDLAServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeDLAServiceResponse:
        """
        @summary Queries the status of the Data Lake Analytics (DLA) service for a backup schedule.
        
        @param request: DescribeDLAServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDLAServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDLAService',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeDLAServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dlaservice_with_options_async(
        self,
        request: dbs_20190306_models.DescribeDLAServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeDLAServiceResponse:
        """
        @summary Queries the status of the Data Lake Analytics (DLA) service for a backup schedule.
        
        @param request: DescribeDLAServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDLAServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDLAService',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeDLAServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dlaservice(
        self,
        request: dbs_20190306_models.DescribeDLAServiceRequest,
    ) -> dbs_20190306_models.DescribeDLAServiceResponse:
        """
        @summary Queries the status of the Data Lake Analytics (DLA) service for a backup schedule.
        
        @param request: DescribeDLAServiceRequest
        @return: DescribeDLAServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dlaservice_with_options(request, runtime)

    async def describe_dlaservice_async(
        self,
        request: dbs_20190306_models.DescribeDLAServiceRequest,
    ) -> dbs_20190306_models.DescribeDLAServiceResponse:
        """
        @summary Queries the status of the Data Lake Analytics (DLA) service for a backup schedule.
        
        @param request: DescribeDLAServiceRequest
        @return: DescribeDLAServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dlaservice_with_options_async(request, runtime)

    def describe_full_backup_list_with_options(
        self,
        request: dbs_20190306_models.DescribeFullBackupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeFullBackupListResponse:
        """
        @summary cn-hangzhou
        
        @param request: DescribeFullBackupListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFullBackupListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.show_storage_type):
            query['ShowStorageType'] = request.show_storage_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFullBackupList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeFullBackupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_full_backup_list_with_options_async(
        self,
        request: dbs_20190306_models.DescribeFullBackupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeFullBackupListResponse:
        """
        @summary cn-hangzhou
        
        @param request: DescribeFullBackupListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeFullBackupListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.show_storage_type):
            query['ShowStorageType'] = request.show_storage_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFullBackupList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeFullBackupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_full_backup_list(
        self,
        request: dbs_20190306_models.DescribeFullBackupListRequest,
    ) -> dbs_20190306_models.DescribeFullBackupListResponse:
        """
        @summary cn-hangzhou
        
        @param request: DescribeFullBackupListRequest
        @return: DescribeFullBackupListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_full_backup_list_with_options(request, runtime)

    async def describe_full_backup_list_async(
        self,
        request: dbs_20190306_models.DescribeFullBackupListRequest,
    ) -> dbs_20190306_models.DescribeFullBackupListResponse:
        """
        @summary cn-hangzhou
        
        @param request: DescribeFullBackupListRequest
        @return: DescribeFullBackupListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_full_backup_list_with_options_async(request, runtime)

    def describe_increment_backup_list_with_options(
        self,
        request: dbs_20190306_models.DescribeIncrementBackupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeIncrementBackupListResponse:
        """
        @summary Queries incremental backup tasks.
        
        @param request: DescribeIncrementBackupListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIncrementBackupListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.show_storage_type):
            query['ShowStorageType'] = request.show_storage_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIncrementBackupList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeIncrementBackupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_increment_backup_list_with_options_async(
        self,
        request: dbs_20190306_models.DescribeIncrementBackupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeIncrementBackupListResponse:
        """
        @summary Queries incremental backup tasks.
        
        @param request: DescribeIncrementBackupListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeIncrementBackupListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.show_storage_type):
            query['ShowStorageType'] = request.show_storage_type
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIncrementBackupList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeIncrementBackupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_increment_backup_list(
        self,
        request: dbs_20190306_models.DescribeIncrementBackupListRequest,
    ) -> dbs_20190306_models.DescribeIncrementBackupListResponse:
        """
        @summary Queries incremental backup tasks.
        
        @param request: DescribeIncrementBackupListRequest
        @return: DescribeIncrementBackupListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_increment_backup_list_with_options(request, runtime)

    async def describe_increment_backup_list_async(
        self,
        request: dbs_20190306_models.DescribeIncrementBackupListRequest,
    ) -> dbs_20190306_models.DescribeIncrementBackupListResponse:
        """
        @summary Queries incremental backup tasks.
        
        @param request: DescribeIncrementBackupListRequest
        @return: DescribeIncrementBackupListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_increment_backup_list_with_options_async(request, runtime)

    def describe_job_error_code_with_options(
        self,
        request: dbs_20190306_models.DescribeJobErrorCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeJobErrorCodeResponse:
        """
        @summary Queries the error information of a Database Backup (DBS) task.
        
        @param request: DescribeJobErrorCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobErrorCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobErrorCode',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeJobErrorCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_error_code_with_options_async(
        self,
        request: dbs_20190306_models.DescribeJobErrorCodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeJobErrorCodeResponse:
        """
        @summary Queries the error information of a Database Backup (DBS) task.
        
        @param request: DescribeJobErrorCodeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeJobErrorCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobErrorCode',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeJobErrorCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_error_code(
        self,
        request: dbs_20190306_models.DescribeJobErrorCodeRequest,
    ) -> dbs_20190306_models.DescribeJobErrorCodeResponse:
        """
        @summary Queries the error information of a Database Backup (DBS) task.
        
        @param request: DescribeJobErrorCodeRequest
        @return: DescribeJobErrorCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_job_error_code_with_options(request, runtime)

    async def describe_job_error_code_async(
        self,
        request: dbs_20190306_models.DescribeJobErrorCodeRequest,
    ) -> dbs_20190306_models.DescribeJobErrorCodeResponse:
        """
        @summary Queries the error information of a Database Backup (DBS) task.
        
        @param request: DescribeJobErrorCodeRequest
        @return: DescribeJobErrorCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_job_error_code_with_options_async(request, runtime)

    def describe_node_cidr_list_with_options(
        self,
        request: dbs_20190306_models.DescribeNodeCidrListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeNodeCidrListResponse:
        """
        @summary Queries the CIDR blocks of nodes on which Database Backup (DBS) is running.
        
        @param request: DescribeNodeCidrListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodeCidrListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodeCidrList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeNodeCidrListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_node_cidr_list_with_options_async(
        self,
        request: dbs_20190306_models.DescribeNodeCidrListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeNodeCidrListResponse:
        """
        @summary Queries the CIDR blocks of nodes on which Database Backup (DBS) is running.
        
        @param request: DescribeNodeCidrListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeNodeCidrListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodeCidrList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeNodeCidrListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_node_cidr_list(
        self,
        request: dbs_20190306_models.DescribeNodeCidrListRequest,
    ) -> dbs_20190306_models.DescribeNodeCidrListResponse:
        """
        @summary Queries the CIDR blocks of nodes on which Database Backup (DBS) is running.
        
        @param request: DescribeNodeCidrListRequest
        @return: DescribeNodeCidrListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_node_cidr_list_with_options(request, runtime)

    async def describe_node_cidr_list_async(
        self,
        request: dbs_20190306_models.DescribeNodeCidrListRequest,
    ) -> dbs_20190306_models.DescribeNodeCidrListResponse:
        """
        @summary Queries the CIDR blocks of nodes on which Database Backup (DBS) is running.
        
        @param request: DescribeNodeCidrListRequest
        @return: DescribeNodeCidrListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_node_cidr_list_with_options_async(request, runtime)

    def describe_pre_check_progress_list_with_options(
        self,
        request: dbs_20190306_models.DescribePreCheckProgressListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribePreCheckProgressListResponse:
        """
        @summary Queries the precheck progress of a backup schedule or a restore task.
        
        @param request: DescribePreCheckProgressListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePreCheckProgressListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.restore_task_id):
            query['RestoreTaskId'] = request.restore_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePreCheckProgressList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribePreCheckProgressListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pre_check_progress_list_with_options_async(
        self,
        request: dbs_20190306_models.DescribePreCheckProgressListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribePreCheckProgressListResponse:
        """
        @summary Queries the precheck progress of a backup schedule or a restore task.
        
        @param request: DescribePreCheckProgressListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribePreCheckProgressListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.restore_task_id):
            query['RestoreTaskId'] = request.restore_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePreCheckProgressList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribePreCheckProgressListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pre_check_progress_list(
        self,
        request: dbs_20190306_models.DescribePreCheckProgressListRequest,
    ) -> dbs_20190306_models.DescribePreCheckProgressListResponse:
        """
        @summary Queries the precheck progress of a backup schedule or a restore task.
        
        @param request: DescribePreCheckProgressListRequest
        @return: DescribePreCheckProgressListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_pre_check_progress_list_with_options(request, runtime)

    async def describe_pre_check_progress_list_async(
        self,
        request: dbs_20190306_models.DescribePreCheckProgressListRequest,
    ) -> dbs_20190306_models.DescribePreCheckProgressListResponse:
        """
        @summary Queries the precheck progress of a backup schedule or a restore task.
        
        @param request: DescribePreCheckProgressListRequest
        @return: DescribePreCheckProgressListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_pre_check_progress_list_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: dbs_20190306_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeRegionsResponse:
        """
        @summary Queries the regions that Database Backup (DBS) supports.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: dbs_20190306_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeRegionsResponse:
        """
        @summary Queries the regions that Database Backup (DBS) supports.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: dbs_20190306_models.DescribeRegionsRequest,
    ) -> dbs_20190306_models.DescribeRegionsResponse:
        """
        @summary Queries the regions that Database Backup (DBS) supports.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: dbs_20190306_models.DescribeRegionsRequest,
    ) -> dbs_20190306_models.DescribeRegionsResponse:
        """
        @summary Queries the regions that Database Backup (DBS) supports.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_restore_range_info_with_options(
        self,
        request: dbs_20190306_models.DescribeRestoreRangeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeRestoreRangeInfoResponse:
        """
        @summary Queries the range of time to which you can restore data in a backup schedule.
        
        @param request: DescribeRestoreRangeInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRestoreRangeInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.begin_timestamp_for_restore):
            query['BeginTimestampForRestore'] = request.begin_timestamp_for_restore
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_timestamp_for_restore):
            query['EndTimestampForRestore'] = request.end_timestamp_for_restore
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.recently_restore):
            query['RecentlyRestore'] = request.recently_restore
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreRangeInfo',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeRestoreRangeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_range_info_with_options_async(
        self,
        request: dbs_20190306_models.DescribeRestoreRangeInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeRestoreRangeInfoResponse:
        """
        @summary Queries the range of time to which you can restore data in a backup schedule.
        
        @param request: DescribeRestoreRangeInfoRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRestoreRangeInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.begin_timestamp_for_restore):
            query['BeginTimestampForRestore'] = request.begin_timestamp_for_restore
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_timestamp_for_restore):
            query['EndTimestampForRestore'] = request.end_timestamp_for_restore
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.recently_restore):
            query['RecentlyRestore'] = request.recently_restore
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreRangeInfo',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeRestoreRangeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_range_info(
        self,
        request: dbs_20190306_models.DescribeRestoreRangeInfoRequest,
    ) -> dbs_20190306_models.DescribeRestoreRangeInfoResponse:
        """
        @summary Queries the range of time to which you can restore data in a backup schedule.
        
        @param request: DescribeRestoreRangeInfoRequest
        @return: DescribeRestoreRangeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_range_info_with_options(request, runtime)

    async def describe_restore_range_info_async(
        self,
        request: dbs_20190306_models.DescribeRestoreRangeInfoRequest,
    ) -> dbs_20190306_models.DescribeRestoreRangeInfoResponse:
        """
        @summary Queries the range of time to which you can restore data in a backup schedule.
        
        @param request: DescribeRestoreRangeInfoRequest
        @return: DescribeRestoreRangeInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_restore_range_info_with_options_async(request, runtime)

    def describe_restore_task_list_with_options(
        self,
        request: dbs_20190306_models.DescribeRestoreTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeRestoreTaskListResponse:
        """
        @summary Queries restore tasks.
        
        @param request: DescribeRestoreTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRestoreTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.restore_task_id):
            query['RestoreTaskId'] = request.restore_task_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreTaskList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeRestoreTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_task_list_with_options_async(
        self,
        request: dbs_20190306_models.DescribeRestoreTaskListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DescribeRestoreTaskListResponse:
        """
        @summary Queries restore tasks.
        
        @param request: DescribeRestoreTaskListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRestoreTaskListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.restore_task_id):
            query['RestoreTaskId'] = request.restore_task_id
        if not UtilClient.is_unset(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRestoreTaskList',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DescribeRestoreTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_task_list(
        self,
        request: dbs_20190306_models.DescribeRestoreTaskListRequest,
    ) -> dbs_20190306_models.DescribeRestoreTaskListResponse:
        """
        @summary Queries restore tasks.
        
        @param request: DescribeRestoreTaskListRequest
        @return: DescribeRestoreTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_restore_task_list_with_options(request, runtime)

    async def describe_restore_task_list_async(
        self,
        request: dbs_20190306_models.DescribeRestoreTaskListRequest,
    ) -> dbs_20190306_models.DescribeRestoreTaskListResponse:
        """
        @summary Queries restore tasks.
        
        @param request: DescribeRestoreTaskListRequest
        @return: DescribeRestoreTaskListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_restore_task_list_with_options_async(request, runtime)

    def disable_backup_log_with_options(
        self,
        request: dbs_20190306_models.DisableBackupLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DisableBackupLogResponse:
        """
        @summary Disables incremental backup for a backup schedule.
        
        @description ### Impact
        After you disable the incremental log backup feature, your backup schedule no longer performs incremental log backups.
        
        @param request: DisableBackupLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableBackupLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableBackupLog',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DisableBackupLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_backup_log_with_options_async(
        self,
        request: dbs_20190306_models.DisableBackupLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.DisableBackupLogResponse:
        """
        @summary Disables incremental backup for a backup schedule.
        
        @description ### Impact
        After you disable the incremental log backup feature, your backup schedule no longer performs incremental log backups.
        
        @param request: DisableBackupLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DisableBackupLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableBackupLog',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.DisableBackupLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_backup_log(
        self,
        request: dbs_20190306_models.DisableBackupLogRequest,
    ) -> dbs_20190306_models.DisableBackupLogResponse:
        """
        @summary Disables incremental backup for a backup schedule.
        
        @description ### Impact
        After you disable the incremental log backup feature, your backup schedule no longer performs incremental log backups.
        
        @param request: DisableBackupLogRequest
        @return: DisableBackupLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_backup_log_with_options(request, runtime)

    async def disable_backup_log_async(
        self,
        request: dbs_20190306_models.DisableBackupLogRequest,
    ) -> dbs_20190306_models.DisableBackupLogResponse:
        """
        @summary Disables incremental backup for a backup schedule.
        
        @description ### Impact
        After you disable the incremental log backup feature, your backup schedule no longer performs incremental log backups.
        
        @param request: DisableBackupLogRequest
        @return: DisableBackupLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.disable_backup_log_with_options_async(request, runtime)

    def enable_backup_log_with_options(
        self,
        request: dbs_20190306_models.EnableBackupLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.EnableBackupLogResponse:
        """
        @summary Enables incremental backup for a backup schedule.
        
        @description ## Impact
        It is free to enable the incremental log backup feature. However, the backup traffic and storage capacity generated by the feature are billed in the same way as the full backup feature, and can be offset by the free quota of backup schedules or storage plans.
        
        @param request: EnableBackupLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableBackupLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableBackupLog',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.EnableBackupLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_backup_log_with_options_async(
        self,
        request: dbs_20190306_models.EnableBackupLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.EnableBackupLogResponse:
        """
        @summary Enables incremental backup for a backup schedule.
        
        @description ## Impact
        It is free to enable the incremental log backup feature. However, the backup traffic and storage capacity generated by the feature are billed in the same way as the full backup feature, and can be offset by the free quota of backup schedules or storage plans.
        
        @param request: EnableBackupLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: EnableBackupLogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableBackupLog',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.EnableBackupLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_backup_log(
        self,
        request: dbs_20190306_models.EnableBackupLogRequest,
    ) -> dbs_20190306_models.EnableBackupLogResponse:
        """
        @summary Enables incremental backup for a backup schedule.
        
        @description ## Impact
        It is free to enable the incremental log backup feature. However, the backup traffic and storage capacity generated by the feature are billed in the same way as the full backup feature, and can be offset by the free quota of backup schedules or storage plans.
        
        @param request: EnableBackupLogRequest
        @return: EnableBackupLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_backup_log_with_options(request, runtime)

    async def enable_backup_log_async(
        self,
        request: dbs_20190306_models.EnableBackupLogRequest,
    ) -> dbs_20190306_models.EnableBackupLogResponse:
        """
        @summary Enables incremental backup for a backup schedule.
        
        @description ## Impact
        It is free to enable the incremental log backup feature. However, the backup traffic and storage capacity generated by the feature are billed in the same way as the full backup feature, and can be offset by the free quota of backup schedules or storage plans.
        
        @param request: EnableBackupLogRequest
        @return: EnableBackupLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.enable_backup_log_with_options_async(request, runtime)

    def get_dblist_from_agent_with_options(
        self,
        request: dbs_20190306_models.GetDBListFromAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.GetDBListFromAgentResponse:
        """
        @summary Queries the result of a task that is used to query a database list by using a backup gateway based on the ID of the task.
        
        @param request: GetDBListFromAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDBListFromAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDBListFromAgent',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.GetDBListFromAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dblist_from_agent_with_options_async(
        self,
        request: dbs_20190306_models.GetDBListFromAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.GetDBListFromAgentResponse:
        """
        @summary Queries the result of a task that is used to query a database list by using a backup gateway based on the ID of the task.
        
        @param request: GetDBListFromAgentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetDBListFromAgentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDBListFromAgent',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.GetDBListFromAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dblist_from_agent(
        self,
        request: dbs_20190306_models.GetDBListFromAgentRequest,
    ) -> dbs_20190306_models.GetDBListFromAgentResponse:
        """
        @summary Queries the result of a task that is used to query a database list by using a backup gateway based on the ID of the task.
        
        @param request: GetDBListFromAgentRequest
        @return: GetDBListFromAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_dblist_from_agent_with_options(request, runtime)

    async def get_dblist_from_agent_async(
        self,
        request: dbs_20190306_models.GetDBListFromAgentRequest,
    ) -> dbs_20190306_models.GetDBListFromAgentResponse:
        """
        @summary Queries the result of a task that is used to query a database list by using a backup gateway based on the ID of the task.
        
        @param request: GetDBListFromAgentRequest
        @return: GetDBListFromAgentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_dblist_from_agent_with_options_async(request, runtime)

    def initialize_dbs_service_linked_role_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.InitializeDbsServiceLinkedRoleResponse:
        """
        @summary Grants the AliyunServiceRoleForDBS role to Database Backup (DBS).
        
        @param request: InitializeDbsServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitializeDbsServiceLinkedRoleResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='InitializeDbsServiceLinkedRole',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.InitializeDbsServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_dbs_service_linked_role_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.InitializeDbsServiceLinkedRoleResponse:
        """
        @summary Grants the AliyunServiceRoleForDBS role to Database Backup (DBS).
        
        @param request: InitializeDbsServiceLinkedRoleRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: InitializeDbsServiceLinkedRoleResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='InitializeDbsServiceLinkedRole',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.InitializeDbsServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize_dbs_service_linked_role(self) -> dbs_20190306_models.InitializeDbsServiceLinkedRoleResponse:
        """
        @summary Grants the AliyunServiceRoleForDBS role to Database Backup (DBS).
        
        @return: InitializeDbsServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.initialize_dbs_service_linked_role_with_options(runtime)

    async def initialize_dbs_service_linked_role_async(self) -> dbs_20190306_models.InitializeDbsServiceLinkedRoleResponse:
        """
        @summary Grants the AliyunServiceRoleForDBS role to Database Backup (DBS).
        
        @return: InitializeDbsServiceLinkedRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.initialize_dbs_service_linked_role_with_options_async(runtime)

    def modify_backup_objects_with_options(
        self,
        request: dbs_20190306_models.ModifyBackupObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupObjectsResponse:
        """
        @summary Modifies backup objects of a backup schedule in Database Backup (DBS).
        
        @param request: ModifyBackupObjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupObjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupObjects',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyBackupObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_objects_with_options_async(
        self,
        request: dbs_20190306_models.ModifyBackupObjectsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupObjectsResponse:
        """
        @summary Modifies backup objects of a backup schedule in Database Backup (DBS).
        
        @param request: ModifyBackupObjectsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupObjectsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupObjects',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyBackupObjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_objects(
        self,
        request: dbs_20190306_models.ModifyBackupObjectsRequest,
    ) -> dbs_20190306_models.ModifyBackupObjectsResponse:
        """
        @summary Modifies backup objects of a backup schedule in Database Backup (DBS).
        
        @param request: ModifyBackupObjectsRequest
        @return: ModifyBackupObjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_objects_with_options(request, runtime)

    async def modify_backup_objects_async(
        self,
        request: dbs_20190306_models.ModifyBackupObjectsRequest,
    ) -> dbs_20190306_models.ModifyBackupObjectsResponse:
        """
        @summary Modifies backup objects of a backup schedule in Database Backup (DBS).
        
        @param request: ModifyBackupObjectsRequest
        @return: ModifyBackupObjectsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_objects_with_options_async(request, runtime)

    def modify_backup_plan_name_with_options(
        self,
        request: dbs_20190306_models.ModifyBackupPlanNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupPlanNameResponse:
        """
        @summary Changes the name of a backup schedule.
        
        @param request: ModifyBackupPlanNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupPlanNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPlanName',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyBackupPlanNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_plan_name_with_options_async(
        self,
        request: dbs_20190306_models.ModifyBackupPlanNameRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupPlanNameResponse:
        """
        @summary Changes the name of a backup schedule.
        
        @param request: ModifyBackupPlanNameRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupPlanNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPlanName',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyBackupPlanNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_plan_name(
        self,
        request: dbs_20190306_models.ModifyBackupPlanNameRequest,
    ) -> dbs_20190306_models.ModifyBackupPlanNameResponse:
        """
        @summary Changes the name of a backup schedule.
        
        @param request: ModifyBackupPlanNameRequest
        @return: ModifyBackupPlanNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_plan_name_with_options(request, runtime)

    async def modify_backup_plan_name_async(
        self,
        request: dbs_20190306_models.ModifyBackupPlanNameRequest,
    ) -> dbs_20190306_models.ModifyBackupPlanNameResponse:
        """
        @summary Changes the name of a backup schedule.
        
        @param request: ModifyBackupPlanNameRequest
        @return: ModifyBackupPlanNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_plan_name_with_options_async(request, runtime)

    def modify_backup_set_download_rules_with_options(
        self,
        request: dbs_20190306_models.ModifyBackupSetDownloadRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupSetDownloadRulesResponse:
        """
        @summary Enables, configures, or disables the automatic download feature.
        
        @param request: ModifyBackupSetDownloadRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupSetDownloadRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_download_dir):
            query['BackupSetDownloadDir'] = request.backup_set_download_dir
        if not UtilClient.is_unset(request.backup_set_download_target_type):
            query['BackupSetDownloadTargetType'] = request.backup_set_download_target_type
        if not UtilClient.is_unset(request.backup_set_download_target_type_location):
            query['BackupSetDownloadTargetTypeLocation'] = request.backup_set_download_target_type_location
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.full_data_format):
            query['FullDataFormat'] = request.full_data_format
        if not UtilClient.is_unset(request.increment_data_format):
            query['IncrementDataFormat'] = request.increment_data_format
        if not UtilClient.is_unset(request.open_auto_download):
            query['OpenAutoDownload'] = request.open_auto_download
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupSetDownloadRules',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyBackupSetDownloadRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_set_download_rules_with_options_async(
        self,
        request: dbs_20190306_models.ModifyBackupSetDownloadRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupSetDownloadRulesResponse:
        """
        @summary Enables, configures, or disables the automatic download feature.
        
        @param request: ModifyBackupSetDownloadRulesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupSetDownloadRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_set_download_dir):
            query['BackupSetDownloadDir'] = request.backup_set_download_dir
        if not UtilClient.is_unset(request.backup_set_download_target_type):
            query['BackupSetDownloadTargetType'] = request.backup_set_download_target_type
        if not UtilClient.is_unset(request.backup_set_download_target_type_location):
            query['BackupSetDownloadTargetTypeLocation'] = request.backup_set_download_target_type_location
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.full_data_format):
            query['FullDataFormat'] = request.full_data_format
        if not UtilClient.is_unset(request.increment_data_format):
            query['IncrementDataFormat'] = request.increment_data_format
        if not UtilClient.is_unset(request.open_auto_download):
            query['OpenAutoDownload'] = request.open_auto_download
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupSetDownloadRules',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyBackupSetDownloadRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_set_download_rules(
        self,
        request: dbs_20190306_models.ModifyBackupSetDownloadRulesRequest,
    ) -> dbs_20190306_models.ModifyBackupSetDownloadRulesResponse:
        """
        @summary Enables, configures, or disables the automatic download feature.
        
        @param request: ModifyBackupSetDownloadRulesRequest
        @return: ModifyBackupSetDownloadRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_set_download_rules_with_options(request, runtime)

    async def modify_backup_set_download_rules_async(
        self,
        request: dbs_20190306_models.ModifyBackupSetDownloadRulesRequest,
    ) -> dbs_20190306_models.ModifyBackupSetDownloadRulesResponse:
        """
        @summary Enables, configures, or disables the automatic download feature.
        
        @param request: ModifyBackupSetDownloadRulesRequest
        @return: ModifyBackupSetDownloadRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_set_download_rules_with_options_async(request, runtime)

    def modify_backup_source_endpoint_with_options(
        self,
        request: dbs_20190306_models.ModifyBackupSourceEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupSourceEndpointResponse:
        """
        @summary Modifies the data source of a backup schedule.
        
        @param request: ModifyBackupSourceEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupSourceEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not UtilClient.is_unset(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
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
            action='ModifyBackupSourceEndpoint',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyBackupSourceEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_source_endpoint_with_options_async(
        self,
        request: dbs_20190306_models.ModifyBackupSourceEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupSourceEndpointResponse:
        """
        @summary Modifies the data source of a backup schedule.
        
        @param request: ModifyBackupSourceEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupSourceEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not UtilClient.is_unset(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not UtilClient.is_unset(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
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
            action='ModifyBackupSourceEndpoint',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyBackupSourceEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_source_endpoint(
        self,
        request: dbs_20190306_models.ModifyBackupSourceEndpointRequest,
    ) -> dbs_20190306_models.ModifyBackupSourceEndpointResponse:
        """
        @summary Modifies the data source of a backup schedule.
        
        @param request: ModifyBackupSourceEndpointRequest
        @return: ModifyBackupSourceEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_source_endpoint_with_options(request, runtime)

    async def modify_backup_source_endpoint_async(
        self,
        request: dbs_20190306_models.ModifyBackupSourceEndpointRequest,
    ) -> dbs_20190306_models.ModifyBackupSourceEndpointResponse:
        """
        @summary Modifies the data source of a backup schedule.
        
        @param request: ModifyBackupSourceEndpointRequest
        @return: ModifyBackupSourceEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_source_endpoint_with_options_async(request, runtime)

    def modify_backup_strategy_with_options(
        self,
        request: dbs_20190306_models.ModifyBackupStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupStrategyResponse:
        """
        @summary Modifies the backup time of a backup schedule.
        
        @param request: ModifyBackupStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_log_interval_seconds):
            query['BackupLogIntervalSeconds'] = request.backup_log_interval_seconds
        if not UtilClient.is_unset(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_start_time):
            query['BackupStartTime'] = request.backup_start_time
        if not UtilClient.is_unset(request.backup_strategy_type):
            query['BackupStrategyType'] = request.backup_strategy_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupStrategy',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyBackupStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_strategy_with_options_async(
        self,
        request: dbs_20190306_models.ModifyBackupStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyBackupStrategyResponse:
        """
        @summary Modifies the backup time of a backup schedule.
        
        @param request: ModifyBackupStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_log_interval_seconds):
            query['BackupLogIntervalSeconds'] = request.backup_log_interval_seconds
        if not UtilClient.is_unset(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_start_time):
            query['BackupStartTime'] = request.backup_start_time
        if not UtilClient.is_unset(request.backup_strategy_type):
            query['BackupStrategyType'] = request.backup_strategy_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupStrategy',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyBackupStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_strategy(
        self,
        request: dbs_20190306_models.ModifyBackupStrategyRequest,
    ) -> dbs_20190306_models.ModifyBackupStrategyResponse:
        """
        @summary Modifies the backup time of a backup schedule.
        
        @param request: ModifyBackupStrategyRequest
        @return: ModifyBackupStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_strategy_with_options(request, runtime)

    async def modify_backup_strategy_async(
        self,
        request: dbs_20190306_models.ModifyBackupStrategyRequest,
    ) -> dbs_20190306_models.ModifyBackupStrategyResponse:
        """
        @summary Modifies the backup time of a backup schedule.
        
        @param request: ModifyBackupStrategyRequest
        @return: ModifyBackupStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_strategy_with_options_async(request, runtime)

    def modify_storage_strategy_with_options(
        self,
        request: dbs_20190306_models.ModifyStorageStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyStorageStrategyResponse:
        """
        @summary Modifies the lifecycle of data that is backed up based on a backup schedule.
        
        @param request: ModifyStorageStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyStorageStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.duplication_archive_period):
            query['DuplicationArchivePeriod'] = request.duplication_archive_period
        if not UtilClient.is_unset(request.duplication_infrequent_access_period):
            query['DuplicationInfrequentAccessPeriod'] = request.duplication_infrequent_access_period
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStorageStrategy',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyStorageStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_storage_strategy_with_options_async(
        self,
        request: dbs_20190306_models.ModifyStorageStrategyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ModifyStorageStrategyResponse:
        """
        @summary Modifies the lifecycle of data that is backed up based on a backup schedule.
        
        @param request: ModifyStorageStrategyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyStorageStrategyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.duplication_archive_period):
            query['DuplicationArchivePeriod'] = request.duplication_archive_period
        if not UtilClient.is_unset(request.duplication_infrequent_access_period):
            query['DuplicationInfrequentAccessPeriod'] = request.duplication_infrequent_access_period
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStorageStrategy',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ModifyStorageStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_storage_strategy(
        self,
        request: dbs_20190306_models.ModifyStorageStrategyRequest,
    ) -> dbs_20190306_models.ModifyStorageStrategyResponse:
        """
        @summary Modifies the lifecycle of data that is backed up based on a backup schedule.
        
        @param request: ModifyStorageStrategyRequest
        @return: ModifyStorageStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_storage_strategy_with_options(request, runtime)

    async def modify_storage_strategy_async(
        self,
        request: dbs_20190306_models.ModifyStorageStrategyRequest,
    ) -> dbs_20190306_models.ModifyStorageStrategyResponse:
        """
        @summary Modifies the lifecycle of data that is backed up based on a backup schedule.
        
        @param request: ModifyStorageStrategyRequest
        @return: ModifyStorageStrategyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_storage_strategy_with_options_async(request, runtime)

    def release_backup_plan_with_options(
        self,
        request: dbs_20190306_models.ReleaseBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ReleaseBackupPlanResponse:
        """
        @summary Releases a pay-as-you-go backup schedule.
        
        @description ## Impacts
        After a pay-as-you-go backup schedule is released, it stops providing services. Database Backup (DBS) no longer charges you fees for this backup schedule.
        
        @param request: ReleaseBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ReleaseBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_backup_plan_with_options_async(
        self,
        request: dbs_20190306_models.ReleaseBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.ReleaseBackupPlanResponse:
        """
        @summary Releases a pay-as-you-go backup schedule.
        
        @description ## Impacts
        After a pay-as-you-go backup schedule is released, it stops providing services. Database Backup (DBS) no longer charges you fees for this backup schedule.
        
        @param request: ReleaseBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.ReleaseBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_backup_plan(
        self,
        request: dbs_20190306_models.ReleaseBackupPlanRequest,
    ) -> dbs_20190306_models.ReleaseBackupPlanResponse:
        """
        @summary Releases a pay-as-you-go backup schedule.
        
        @description ## Impacts
        After a pay-as-you-go backup schedule is released, it stops providing services. Database Backup (DBS) no longer charges you fees for this backup schedule.
        
        @param request: ReleaseBackupPlanRequest
        @return: ReleaseBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_backup_plan_with_options(request, runtime)

    async def release_backup_plan_async(
        self,
        request: dbs_20190306_models.ReleaseBackupPlanRequest,
    ) -> dbs_20190306_models.ReleaseBackupPlanResponse:
        """
        @summary Releases a pay-as-you-go backup schedule.
        
        @description ## Impacts
        After a pay-as-you-go backup schedule is released, it stops providing services. Database Backup (DBS) no longer charges you fees for this backup schedule.
        
        @param request: ReleaseBackupPlanRequest
        @return: ReleaseBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_backup_plan_with_options_async(request, runtime)

    def renew_backup_plan_with_options(
        self,
        request: dbs_20190306_models.RenewBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.RenewBackupPlanResponse:
        """
        @summary Renews a backup schedule.
        
        @param request: RenewBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.RenewBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_backup_plan_with_options_async(
        self,
        request: dbs_20190306_models.RenewBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.RenewBackupPlanResponse:
        """
        @summary Renews a backup schedule.
        
        @param request: RenewBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.RenewBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_backup_plan(
        self,
        request: dbs_20190306_models.RenewBackupPlanRequest,
    ) -> dbs_20190306_models.RenewBackupPlanResponse:
        """
        @summary Renews a backup schedule.
        
        @param request: RenewBackupPlanRequest
        @return: RenewBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_backup_plan_with_options(request, runtime)

    async def renew_backup_plan_async(
        self,
        request: dbs_20190306_models.RenewBackupPlanRequest,
    ) -> dbs_20190306_models.RenewBackupPlanResponse:
        """
        @summary Renews a backup schedule.
        
        @param request: RenewBackupPlanRequest
        @return: RenewBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_backup_plan_with_options_async(request, runtime)

    def start_backup_plan_with_options(
        self,
        request: dbs_20190306_models.StartBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.StartBackupPlanResponse:
        """
        @summary Starts a backup schedule.
        
        @param request: StartBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.StartBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_backup_plan_with_options_async(
        self,
        request: dbs_20190306_models.StartBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.StartBackupPlanResponse:
        """
        @summary Starts a backup schedule.
        
        @param request: StartBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.StartBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_backup_plan(
        self,
        request: dbs_20190306_models.StartBackupPlanRequest,
    ) -> dbs_20190306_models.StartBackupPlanResponse:
        """
        @summary Starts a backup schedule.
        
        @param request: StartBackupPlanRequest
        @return: StartBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_backup_plan_with_options(request, runtime)

    async def start_backup_plan_async(
        self,
        request: dbs_20190306_models.StartBackupPlanRequest,
    ) -> dbs_20190306_models.StartBackupPlanResponse:
        """
        @summary Starts a backup schedule.
        
        @param request: StartBackupPlanRequest
        @return: StartBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_backup_plan_with_options_async(request, runtime)

    def start_restore_task_with_options(
        self,
        request: dbs_20190306_models.StartRestoreTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.StartRestoreTaskResponse:
        """
        @summary Starts a restore task.
        
        @param request: StartRestoreTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartRestoreTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.restore_task_id):
            query['RestoreTaskId'] = request.restore_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRestoreTask',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.StartRestoreTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_restore_task_with_options_async(
        self,
        request: dbs_20190306_models.StartRestoreTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.StartRestoreTaskResponse:
        """
        @summary Starts a restore task.
        
        @param request: StartRestoreTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartRestoreTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.restore_task_id):
            query['RestoreTaskId'] = request.restore_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRestoreTask',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.StartRestoreTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_restore_task(
        self,
        request: dbs_20190306_models.StartRestoreTaskRequest,
    ) -> dbs_20190306_models.StartRestoreTaskResponse:
        """
        @summary Starts a restore task.
        
        @param request: StartRestoreTaskRequest
        @return: StartRestoreTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_restore_task_with_options(request, runtime)

    async def start_restore_task_async(
        self,
        request: dbs_20190306_models.StartRestoreTaskRequest,
    ) -> dbs_20190306_models.StartRestoreTaskResponse:
        """
        @summary Starts a restore task.
        
        @param request: StartRestoreTaskRequest
        @return: StartRestoreTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_restore_task_with_options_async(request, runtime)

    def stop_backup_plan_with_options(
        self,
        request: dbs_20190306_models.StopBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.StopBackupPlanResponse:
        """
        @summary Stops a backup schedule.
        
        @param request: StopBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stop_method):
            query['StopMethod'] = request.stop_method
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.StopBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_backup_plan_with_options_async(
        self,
        request: dbs_20190306_models.StopBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.StopBackupPlanResponse:
        """
        @summary Stops a backup schedule.
        
        @param request: StopBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stop_method):
            query['StopMethod'] = request.stop_method
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.StopBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_backup_plan(
        self,
        request: dbs_20190306_models.StopBackupPlanRequest,
    ) -> dbs_20190306_models.StopBackupPlanResponse:
        """
        @summary Stops a backup schedule.
        
        @param request: StopBackupPlanRequest
        @return: StopBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_backup_plan_with_options(request, runtime)

    async def stop_backup_plan_async(
        self,
        request: dbs_20190306_models.StopBackupPlanRequest,
    ) -> dbs_20190306_models.StopBackupPlanResponse:
        """
        @summary Stops a backup schedule.
        
        @param request: StopBackupPlanRequest
        @return: StopBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_backup_plan_with_options_async(request, runtime)

    def upgrade_backup_plan_with_options(
        self,
        request: dbs_20190306_models.UpgradeBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.UpgradeBackupPlanResponse:
        """
        @summary Upgrades a backup schedule.
        
        @param request: UpgradeBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.UpgradeBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_backup_plan_with_options_async(
        self,
        request: dbs_20190306_models.UpgradeBackupPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> dbs_20190306_models.UpgradeBackupPlanResponse:
        """
        @summary Upgrades a backup schedule.
        
        @param request: UpgradeBackupPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeBackupPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeBackupPlan',
            version='2019-03-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            dbs_20190306_models.UpgradeBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_backup_plan(
        self,
        request: dbs_20190306_models.UpgradeBackupPlanRequest,
    ) -> dbs_20190306_models.UpgradeBackupPlanResponse:
        """
        @summary Upgrades a backup schedule.
        
        @param request: UpgradeBackupPlanRequest
        @return: UpgradeBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_backup_plan_with_options(request, runtime)

    async def upgrade_backup_plan_async(
        self,
        request: dbs_20190306_models.UpgradeBackupPlanRequest,
    ) -> dbs_20190306_models.UpgradeBackupPlanResponse:
        """
        @summary Upgrades a backup schedule.
        
        @param request: UpgradeBackupPlanRequest
        @return: UpgradeBackupPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_backup_plan_with_options_async(request, runtime)
