# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dbs20190306 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions

"""
"""
class Client(OpenApiClient):

    def __init__(
        self,
        config: open_api_util_models.Config,
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def configure_backup_plan_with_options(
        self,
        request: main_models.ConfigureBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_start_backup):
            query['AutoStartBackup'] = request.auto_start_backup
        if not DaraCore.is_null(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not DaraCore.is_null(request.backup_log_interval_seconds):
            query['BackupLogIntervalSeconds'] = request.backup_log_interval_seconds
        if not DaraCore.is_null(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not DaraCore.is_null(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not DaraCore.is_null(request.backup_rate_limit):
            query['BackupRateLimit'] = request.backup_rate_limit
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.backup_speed_limit):
            query['BackupSpeedLimit'] = request.backup_speed_limit
        if not DaraCore.is_null(request.backup_start_time):
            query['BackupStartTime'] = request.backup_start_time
        if not DaraCore.is_null(request.backup_storage_encrypt_method):
            query['BackupStorageEncryptMethod'] = request.backup_storage_encrypt_method
        if not DaraCore.is_null(request.backup_storage_type):
            query['BackupStorageType'] = request.backup_storage_type
        if not DaraCore.is_null(request.backup_strategy_type):
            query['BackupStrategyType'] = request.backup_strategy_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not DaraCore.is_null(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not DaraCore.is_null(request.duplication_archive_period):
            query['DuplicationArchivePeriod'] = request.duplication_archive_period
        if not DaraCore.is_null(request.duplication_infrequent_access_period):
            query['DuplicationInfrequentAccessPeriod'] = request.duplication_infrequent_access_period
        if not DaraCore.is_null(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not DaraCore.is_null(request.enable_mysql_physical_backup_binlog):
            query['EnableMysqlPhysicalBackupBinlog'] = request.enable_mysql_physical_backup_binlog
        if not DaraCore.is_null(request.enable_source_endpoint_ssl):
            query['EnableSourceEndpointSsl'] = request.enable_source_endpoint_ssl
        if not DaraCore.is_null(request.ossbucket_name):
            query['OSSBucketName'] = request.ossbucket_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not DaraCore.is_null(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not DaraCore.is_null(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not DaraCore.is_null(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not DaraCore.is_null(request.source_endpoint_oracle_home):
            query['SourceEndpointOracleHome'] = request.source_endpoint_oracle_home
        if not DaraCore.is_null(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not DaraCore.is_null(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not DaraCore.is_null(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not DaraCore.is_null(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not DaraCore.is_null(request.ssl_ca_pem):
            query['SslCaPem'] = request.ssl_ca_pem
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureBackupPlan',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def configure_backup_plan_with_options_async(
        self,
        request: main_models.ConfigureBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ConfigureBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_start_backup):
            query['AutoStartBackup'] = request.auto_start_backup
        if not DaraCore.is_null(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not DaraCore.is_null(request.backup_log_interval_seconds):
            query['BackupLogIntervalSeconds'] = request.backup_log_interval_seconds
        if not DaraCore.is_null(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not DaraCore.is_null(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not DaraCore.is_null(request.backup_rate_limit):
            query['BackupRateLimit'] = request.backup_rate_limit
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.backup_speed_limit):
            query['BackupSpeedLimit'] = request.backup_speed_limit
        if not DaraCore.is_null(request.backup_start_time):
            query['BackupStartTime'] = request.backup_start_time
        if not DaraCore.is_null(request.backup_storage_encrypt_method):
            query['BackupStorageEncryptMethod'] = request.backup_storage_encrypt_method
        if not DaraCore.is_null(request.backup_storage_type):
            query['BackupStorageType'] = request.backup_storage_type
        if not DaraCore.is_null(request.backup_strategy_type):
            query['BackupStrategyType'] = request.backup_strategy_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not DaraCore.is_null(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not DaraCore.is_null(request.duplication_archive_period):
            query['DuplicationArchivePeriod'] = request.duplication_archive_period
        if not DaraCore.is_null(request.duplication_infrequent_access_period):
            query['DuplicationInfrequentAccessPeriod'] = request.duplication_infrequent_access_period
        if not DaraCore.is_null(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not DaraCore.is_null(request.enable_mysql_physical_backup_binlog):
            query['EnableMysqlPhysicalBackupBinlog'] = request.enable_mysql_physical_backup_binlog
        if not DaraCore.is_null(request.enable_source_endpoint_ssl):
            query['EnableSourceEndpointSsl'] = request.enable_source_endpoint_ssl
        if not DaraCore.is_null(request.ossbucket_name):
            query['OSSBucketName'] = request.ossbucket_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not DaraCore.is_null(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not DaraCore.is_null(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not DaraCore.is_null(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not DaraCore.is_null(request.source_endpoint_oracle_home):
            query['SourceEndpointOracleHome'] = request.source_endpoint_oracle_home
        if not DaraCore.is_null(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not DaraCore.is_null(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not DaraCore.is_null(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not DaraCore.is_null(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not DaraCore.is_null(request.ssl_ca_pem):
            query['SslCaPem'] = request.ssl_ca_pem
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ConfigureBackupPlan',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ConfigureBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def configure_backup_plan(
        self,
        request: main_models.ConfigureBackupPlanRequest,
    ) -> main_models.ConfigureBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.configure_backup_plan_with_options(request, runtime)

    async def configure_backup_plan_async(
        self,
        request: main_models.ConfigureBackupPlanRequest,
    ) -> main_models.ConfigureBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.configure_backup_plan_with_options_async(request, runtime)

    def create_and_start_backup_plan_with_options(
        self,
        request: main_models.CreateAndStartBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAndStartBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not DaraCore.is_null(request.backup_log_interval_seconds):
            query['BackupLogIntervalSeconds'] = request.backup_log_interval_seconds
        if not DaraCore.is_null(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not DaraCore.is_null(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not DaraCore.is_null(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not DaraCore.is_null(request.backup_rate_limit):
            query['BackupRateLimit'] = request.backup_rate_limit
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.backup_speed_limit):
            query['BackupSpeedLimit'] = request.backup_speed_limit
        if not DaraCore.is_null(request.backup_start_time):
            query['BackupStartTime'] = request.backup_start_time
        if not DaraCore.is_null(request.backup_storage_type):
            query['BackupStorageType'] = request.backup_storage_type
        if not DaraCore.is_null(request.backup_strategy_type):
            query['BackupStrategyType'] = request.backup_strategy_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not DaraCore.is_null(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not DaraCore.is_null(request.database_region):
            query['DatabaseRegion'] = request.database_region
        if not DaraCore.is_null(request.database_type):
            query['DatabaseType'] = request.database_type
        if not DaraCore.is_null(request.duplication_archive_period):
            query['DuplicationArchivePeriod'] = request.duplication_archive_period
        if not DaraCore.is_null(request.duplication_infrequent_access_period):
            query['DuplicationInfrequentAccessPeriod'] = request.duplication_infrequent_access_period
        if not DaraCore.is_null(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not DaraCore.is_null(request.from_app):
            query['FromApp'] = request.from_app
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.ossbucket_name):
            query['OSSBucketName'] = request.ossbucket_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not DaraCore.is_null(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not DaraCore.is_null(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not DaraCore.is_null(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not DaraCore.is_null(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not DaraCore.is_null(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not DaraCore.is_null(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not DaraCore.is_null(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not DaraCore.is_null(request.storage_region):
            query['StorageRegion'] = request.storage_region
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAndStartBackupPlan',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAndStartBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_and_start_backup_plan_with_options_async(
        self,
        request: main_models.CreateAndStartBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAndStartBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not DaraCore.is_null(request.backup_log_interval_seconds):
            query['BackupLogIntervalSeconds'] = request.backup_log_interval_seconds
        if not DaraCore.is_null(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not DaraCore.is_null(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not DaraCore.is_null(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not DaraCore.is_null(request.backup_rate_limit):
            query['BackupRateLimit'] = request.backup_rate_limit
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.backup_speed_limit):
            query['BackupSpeedLimit'] = request.backup_speed_limit
        if not DaraCore.is_null(request.backup_start_time):
            query['BackupStartTime'] = request.backup_start_time
        if not DaraCore.is_null(request.backup_storage_type):
            query['BackupStorageType'] = request.backup_storage_type
        if not DaraCore.is_null(request.backup_strategy_type):
            query['BackupStrategyType'] = request.backup_strategy_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not DaraCore.is_null(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not DaraCore.is_null(request.database_region):
            query['DatabaseRegion'] = request.database_region
        if not DaraCore.is_null(request.database_type):
            query['DatabaseType'] = request.database_type
        if not DaraCore.is_null(request.duplication_archive_period):
            query['DuplicationArchivePeriod'] = request.duplication_archive_period
        if not DaraCore.is_null(request.duplication_infrequent_access_period):
            query['DuplicationInfrequentAccessPeriod'] = request.duplication_infrequent_access_period
        if not DaraCore.is_null(request.enable_backup_log):
            query['EnableBackupLog'] = request.enable_backup_log
        if not DaraCore.is_null(request.from_app):
            query['FromApp'] = request.from_app
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.ossbucket_name):
            query['OSSBucketName'] = request.ossbucket_name
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not DaraCore.is_null(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not DaraCore.is_null(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not DaraCore.is_null(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not DaraCore.is_null(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not DaraCore.is_null(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not DaraCore.is_null(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not DaraCore.is_null(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not DaraCore.is_null(request.storage_region):
            query['StorageRegion'] = request.storage_region
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAndStartBackupPlan',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAndStartBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_and_start_backup_plan(
        self,
        request: main_models.CreateAndStartBackupPlanRequest,
    ) -> main_models.CreateAndStartBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.create_and_start_backup_plan_with_options(request, runtime)

    async def create_and_start_backup_plan_async(
        self,
        request: main_models.CreateAndStartBackupPlanRequest,
    ) -> main_models.CreateAndStartBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.create_and_start_backup_plan_with_options_async(request, runtime)

    def create_backup_plan_with_options(
        self,
        request: main_models.CreateBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_region):
            query['DatabaseRegion'] = request.database_region
        if not DaraCore.is_null(request.database_type):
            query['DatabaseType'] = request.database_type
        if not DaraCore.is_null(request.from_app):
            query['FromApp'] = request.from_app
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.storage_region):
            query['StorageRegion'] = request.storage_region
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackupPlan',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_plan_with_options_async(
        self,
        request: main_models.CreateBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_region):
            query['DatabaseRegion'] = request.database_region
        if not DaraCore.is_null(request.database_type):
            query['DatabaseType'] = request.database_type
        if not DaraCore.is_null(request.from_app):
            query['FromApp'] = request.from_app
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.pay_type):
            query['PayType'] = request.pay_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.storage_region):
            query['StorageRegion'] = request.storage_region
        if not DaraCore.is_null(request.storage_type):
            query['StorageType'] = request.storage_type
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackupPlan',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup_plan(
        self,
        request: main_models.CreateBackupPlanRequest,
    ) -> main_models.CreateBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.create_backup_plan_with_options(request, runtime)

    async def create_backup_plan_async(
        self,
        request: main_models.CreateBackupPlanRequest,
    ) -> main_models.CreateBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.create_backup_plan_with_options_async(request, runtime)

    def create_full_backup_set_download_with_options(
        self,
        request: main_models.CreateFullBackupSetDownloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFullBackupSetDownloadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_set_data_format):
            query['BackupSetDataFormat'] = request.backup_set_data_format
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFullBackupSetDownload',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFullBackupSetDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_full_backup_set_download_with_options_async(
        self,
        request: main_models.CreateFullBackupSetDownloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFullBackupSetDownloadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_set_data_format):
            query['BackupSetDataFormat'] = request.backup_set_data_format
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFullBackupSetDownload',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFullBackupSetDownloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_full_backup_set_download(
        self,
        request: main_models.CreateFullBackupSetDownloadRequest,
    ) -> main_models.CreateFullBackupSetDownloadResponse:
        runtime = RuntimeOptions()
        return self.create_full_backup_set_download_with_options(request, runtime)

    async def create_full_backup_set_download_async(
        self,
        request: main_models.CreateFullBackupSetDownloadRequest,
    ) -> main_models.CreateFullBackupSetDownloadResponse:
        runtime = RuntimeOptions()
        return await self.create_full_backup_set_download_with_options_async(request, runtime)

    def create_get_dblist_from_agent_task_with_options(
        self,
        request: main_models.CreateGetDBListFromAgentTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGetDBListFromAgentTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_type):
            query['DatabaseType'] = request.database_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not DaraCore.is_null(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGetDBListFromAgentTask',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGetDBListFromAgentTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_get_dblist_from_agent_task_with_options_async(
        self,
        request: main_models.CreateGetDBListFromAgentTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGetDBListFromAgentTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.database_type):
            query['DatabaseType'] = request.database_type
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not DaraCore.is_null(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGetDBListFromAgentTask',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGetDBListFromAgentTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_get_dblist_from_agent_task(
        self,
        request: main_models.CreateGetDBListFromAgentTaskRequest,
    ) -> main_models.CreateGetDBListFromAgentTaskResponse:
        runtime = RuntimeOptions()
        return self.create_get_dblist_from_agent_task_with_options(request, runtime)

    async def create_get_dblist_from_agent_task_async(
        self,
        request: main_models.CreateGetDBListFromAgentTaskRequest,
    ) -> main_models.CreateGetDBListFromAgentTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_get_dblist_from_agent_task_with_options_async(request, runtime)

    def create_increment_backup_set_download_with_options(
        self,
        request: main_models.CreateIncrementBackupSetDownloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIncrementBackupSetDownloadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_set_data_format):
            query['BackupSetDataFormat'] = request.backup_set_data_format
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.backup_set_name):
            query['BackupSetName'] = request.backup_set_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIncrementBackupSetDownload',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIncrementBackupSetDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_increment_backup_set_download_with_options_async(
        self,
        request: main_models.CreateIncrementBackupSetDownloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateIncrementBackupSetDownloadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_set_data_format):
            query['BackupSetDataFormat'] = request.backup_set_data_format
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.backup_set_name):
            query['BackupSetName'] = request.backup_set_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateIncrementBackupSetDownload',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateIncrementBackupSetDownloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_increment_backup_set_download(
        self,
        request: main_models.CreateIncrementBackupSetDownloadRequest,
    ) -> main_models.CreateIncrementBackupSetDownloadResponse:
        runtime = RuntimeOptions()
        return self.create_increment_backup_set_download_with_options(request, runtime)

    async def create_increment_backup_set_download_async(
        self,
        request: main_models.CreateIncrementBackupSetDownloadRequest,
    ) -> main_models.CreateIncrementBackupSetDownloadResponse:
        runtime = RuntimeOptions()
        return await self.create_increment_backup_set_download_with_options_async(request, runtime)

    def create_restore_task_with_options(
        self,
        request: main_models.CreateRestoreTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRestoreTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_open_database):
            query['AutoOpenDatabase'] = request.auto_open_database
        if not DaraCore.is_null(request.auto_shutdown_database):
            query['AutoShutdownDatabase'] = request.auto_shutdown_database
        if not DaraCore.is_null(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not DaraCore.is_null(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not DaraCore.is_null(request.dest_database_instance_class):
            query['DestDatabaseInstanceClass'] = request.dest_database_instance_class
        if not DaraCore.is_null(request.dest_database_instance_database_version):
            query['DestDatabaseInstanceDatabaseVersion'] = request.dest_database_instance_database_version
        if not DaraCore.is_null(request.dest_database_instance_region):
            query['DestDatabaseInstanceRegion'] = request.dest_database_instance_region
        if not DaraCore.is_null(request.dest_database_instance_storage_size):
            query['DestDatabaseInstanceStorageSize'] = request.dest_database_instance_storage_size
        if not DaraCore.is_null(request.dest_database_instance_type):
            query['DestDatabaseInstanceType'] = request.dest_database_instance_type
        if not DaraCore.is_null(request.dest_database_instance_vswitch):
            query['DestDatabaseInstanceVSwitch'] = request.dest_database_instance_vswitch
        if not DaraCore.is_null(request.dest_database_instance_vpc):
            query['DestDatabaseInstanceVpc'] = request.dest_database_instance_vpc
        if not DaraCore.is_null(request.destination_endpoint_database_name):
            query['DestinationEndpointDatabaseName'] = request.destination_endpoint_database_name
        if not DaraCore.is_null(request.destination_endpoint_ip):
            query['DestinationEndpointIP'] = request.destination_endpoint_ip
        if not DaraCore.is_null(request.destination_endpoint_instance_id):
            query['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not DaraCore.is_null(request.destination_endpoint_instance_type):
            query['DestinationEndpointInstanceType'] = request.destination_endpoint_instance_type
        if not DaraCore.is_null(request.destination_endpoint_oracle_sid):
            query['DestinationEndpointOracleSID'] = request.destination_endpoint_oracle_sid
        if not DaraCore.is_null(request.destination_endpoint_password):
            query['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not DaraCore.is_null(request.destination_endpoint_port):
            query['DestinationEndpointPort'] = request.destination_endpoint_port
        if not DaraCore.is_null(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not DaraCore.is_null(request.destination_endpoint_user_name):
            query['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not DaraCore.is_null(request.duplicate_conflict):
            query['DuplicateConflict'] = request.duplicate_conflict
        if not DaraCore.is_null(request.enable_destination_endpoint_ssl):
            query['EnableDestinationEndpointSsl'] = request.enable_destination_endpoint_ssl
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.restore_destination_mode):
            query['RestoreDestinationMode'] = request.restore_destination_mode
        if not DaraCore.is_null(request.restore_dir):
            query['RestoreDir'] = request.restore_dir
        if not DaraCore.is_null(request.restore_home):
            query['RestoreHome'] = request.restore_home
        if not DaraCore.is_null(request.restore_objects):
            query['RestoreObjects'] = request.restore_objects
        if not DaraCore.is_null(request.restore_task_name):
            query['RestoreTaskName'] = request.restore_task_name
        if not DaraCore.is_null(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not DaraCore.is_null(request.ssl_ca_pem):
            query['SslCaPem'] = request.ssl_ca_pem
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRestoreTask',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRestoreTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_restore_task_with_options_async(
        self,
        request: main_models.CreateRestoreTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRestoreTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_open_database):
            query['AutoOpenDatabase'] = request.auto_open_database
        if not DaraCore.is_null(request.auto_shutdown_database):
            query['AutoShutdownDatabase'] = request.auto_shutdown_database
        if not DaraCore.is_null(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not DaraCore.is_null(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not DaraCore.is_null(request.dest_database_instance_class):
            query['DestDatabaseInstanceClass'] = request.dest_database_instance_class
        if not DaraCore.is_null(request.dest_database_instance_database_version):
            query['DestDatabaseInstanceDatabaseVersion'] = request.dest_database_instance_database_version
        if not DaraCore.is_null(request.dest_database_instance_region):
            query['DestDatabaseInstanceRegion'] = request.dest_database_instance_region
        if not DaraCore.is_null(request.dest_database_instance_storage_size):
            query['DestDatabaseInstanceStorageSize'] = request.dest_database_instance_storage_size
        if not DaraCore.is_null(request.dest_database_instance_type):
            query['DestDatabaseInstanceType'] = request.dest_database_instance_type
        if not DaraCore.is_null(request.dest_database_instance_vswitch):
            query['DestDatabaseInstanceVSwitch'] = request.dest_database_instance_vswitch
        if not DaraCore.is_null(request.dest_database_instance_vpc):
            query['DestDatabaseInstanceVpc'] = request.dest_database_instance_vpc
        if not DaraCore.is_null(request.destination_endpoint_database_name):
            query['DestinationEndpointDatabaseName'] = request.destination_endpoint_database_name
        if not DaraCore.is_null(request.destination_endpoint_ip):
            query['DestinationEndpointIP'] = request.destination_endpoint_ip
        if not DaraCore.is_null(request.destination_endpoint_instance_id):
            query['DestinationEndpointInstanceID'] = request.destination_endpoint_instance_id
        if not DaraCore.is_null(request.destination_endpoint_instance_type):
            query['DestinationEndpointInstanceType'] = request.destination_endpoint_instance_type
        if not DaraCore.is_null(request.destination_endpoint_oracle_sid):
            query['DestinationEndpointOracleSID'] = request.destination_endpoint_oracle_sid
        if not DaraCore.is_null(request.destination_endpoint_password):
            query['DestinationEndpointPassword'] = request.destination_endpoint_password
        if not DaraCore.is_null(request.destination_endpoint_port):
            query['DestinationEndpointPort'] = request.destination_endpoint_port
        if not DaraCore.is_null(request.destination_endpoint_region):
            query['DestinationEndpointRegion'] = request.destination_endpoint_region
        if not DaraCore.is_null(request.destination_endpoint_user_name):
            query['DestinationEndpointUserName'] = request.destination_endpoint_user_name
        if not DaraCore.is_null(request.duplicate_conflict):
            query['DuplicateConflict'] = request.duplicate_conflict
        if not DaraCore.is_null(request.enable_destination_endpoint_ssl):
            query['EnableDestinationEndpointSsl'] = request.enable_destination_endpoint_ssl
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.restore_destination_mode):
            query['RestoreDestinationMode'] = request.restore_destination_mode
        if not DaraCore.is_null(request.restore_dir):
            query['RestoreDir'] = request.restore_dir
        if not DaraCore.is_null(request.restore_home):
            query['RestoreHome'] = request.restore_home
        if not DaraCore.is_null(request.restore_objects):
            query['RestoreObjects'] = request.restore_objects
        if not DaraCore.is_null(request.restore_task_name):
            query['RestoreTaskName'] = request.restore_task_name
        if not DaraCore.is_null(request.restore_time):
            query['RestoreTime'] = request.restore_time
        if not DaraCore.is_null(request.ssl_ca_pem):
            query['SslCaPem'] = request.ssl_ca_pem
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRestoreTask',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRestoreTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_restore_task(
        self,
        request: main_models.CreateRestoreTaskRequest,
    ) -> main_models.CreateRestoreTaskResponse:
        runtime = RuntimeOptions()
        return self.create_restore_task_with_options(request, runtime)

    async def create_restore_task_async(
        self,
        request: main_models.CreateRestoreTaskRequest,
    ) -> main_models.CreateRestoreTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_restore_task_with_options_async(request, runtime)

    def describe_backup_gateway_list_with_options(
        self,
        request: main_models.DescribeBackupGatewayListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupGatewayListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupGatewayList',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupGatewayListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_gateway_list_with_options_async(
        self,
        request: main_models.DescribeBackupGatewayListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupGatewayListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.identifier):
            query['Identifier'] = request.identifier
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupGatewayList',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupGatewayListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_gateway_list(
        self,
        request: main_models.DescribeBackupGatewayListRequest,
    ) -> main_models.DescribeBackupGatewayListResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_gateway_list_with_options(request, runtime)

    async def describe_backup_gateway_list_async(
        self,
        request: main_models.DescribeBackupGatewayListRequest,
    ) -> main_models.DescribeBackupGatewayListResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_gateway_list_with_options_async(request, runtime)

    def describe_backup_plan_billing_with_options(
        self,
        request: main_models.DescribeBackupPlanBillingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPlanBillingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.show_storage_type):
            query['ShowStorageType'] = request.show_storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPlanBilling',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupPlanBillingResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_plan_billing_with_options_async(
        self,
        request: main_models.DescribeBackupPlanBillingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPlanBillingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.show_storage_type):
            query['ShowStorageType'] = request.show_storage_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPlanBilling',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupPlanBillingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_plan_billing(
        self,
        request: main_models.DescribeBackupPlanBillingRequest,
    ) -> main_models.DescribeBackupPlanBillingResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_plan_billing_with_options(request, runtime)

    async def describe_backup_plan_billing_async(
        self,
        request: main_models.DescribeBackupPlanBillingRequest,
    ) -> main_models.DescribeBackupPlanBillingResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_plan_billing_with_options_async(request, runtime)

    def describe_backup_plan_list_with_options(
        self,
        request: main_models.DescribeBackupPlanListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPlanListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not DaraCore.is_null(request.backup_plan_status):
            query['BackupPlanStatus'] = request.backup_plan_status
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.show_backup_strategy_info):
            query['ShowBackupStrategyInfo'] = request.show_backup_strategy_info
        if not DaraCore.is_null(request.show_recover_time_range):
            query['ShowRecoverTimeRange'] = request.show_recover_time_range
        if not DaraCore.is_null(request.show_storage_strategy_info):
            query['ShowStorageStrategyInfo'] = request.show_storage_strategy_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPlanList',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupPlanListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_plan_list_with_options_async(
        self,
        request: main_models.DescribeBackupPlanListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupPlanListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_method):
            query['BackupMethod'] = request.backup_method
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not DaraCore.is_null(request.backup_plan_status):
            query['BackupPlanStatus'] = request.backup_plan_status
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.show_backup_strategy_info):
            query['ShowBackupStrategyInfo'] = request.show_backup_strategy_info
        if not DaraCore.is_null(request.show_recover_time_range):
            query['ShowRecoverTimeRange'] = request.show_recover_time_range
        if not DaraCore.is_null(request.show_storage_strategy_info):
            query['ShowStorageStrategyInfo'] = request.show_storage_strategy_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupPlanList',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupPlanListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_plan_list(
        self,
        request: main_models.DescribeBackupPlanListRequest,
    ) -> main_models.DescribeBackupPlanListResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_plan_list_with_options(request, runtime)

    async def describe_backup_plan_list_async(
        self,
        request: main_models.DescribeBackupPlanListRequest,
    ) -> main_models.DescribeBackupPlanListResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_plan_list_with_options_async(request, runtime)

    def describe_backup_set_download_task_list_with_options(
        self,
        request: main_models.DescribeBackupSetDownloadTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupSetDownloadTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_set_download_task_id):
            query['BackupSetDownloadTaskId'] = request.backup_set_download_task_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupSetDownloadTaskList',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupSetDownloadTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_set_download_task_list_with_options_async(
        self,
        request: main_models.DescribeBackupSetDownloadTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeBackupSetDownloadTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_set_download_task_id):
            query['BackupSetDownloadTaskId'] = request.backup_set_download_task_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeBackupSetDownloadTaskList',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeBackupSetDownloadTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_set_download_task_list(
        self,
        request: main_models.DescribeBackupSetDownloadTaskListRequest,
    ) -> main_models.DescribeBackupSetDownloadTaskListResponse:
        runtime = RuntimeOptions()
        return self.describe_backup_set_download_task_list_with_options(request, runtime)

    async def describe_backup_set_download_task_list_async(
        self,
        request: main_models.DescribeBackupSetDownloadTaskListRequest,
    ) -> main_models.DescribeBackupSetDownloadTaskListResponse:
        runtime = RuntimeOptions()
        return await self.describe_backup_set_download_task_list_with_options_async(request, runtime)

    def describe_dlaservice_with_options(
        self,
        request: main_models.DescribeDLAServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDLAServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDLAService',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDLAServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dlaservice_with_options_async(
        self,
        request: main_models.DescribeDLAServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDLAServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDLAService',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDLAServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dlaservice(
        self,
        request: main_models.DescribeDLAServiceRequest,
    ) -> main_models.DescribeDLAServiceResponse:
        runtime = RuntimeOptions()
        return self.describe_dlaservice_with_options(request, runtime)

    async def describe_dlaservice_async(
        self,
        request: main_models.DescribeDLAServiceRequest,
    ) -> main_models.DescribeDLAServiceResponse:
        runtime = RuntimeOptions()
        return await self.describe_dlaservice_with_options_async(request, runtime)

    def describe_full_backup_list_with_options(
        self,
        request: main_models.DescribeFullBackupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFullBackupListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.backup_set_status):
            query['BackupSetStatus'] = request.backup_set_status
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.show_progress):
            query['ShowProgress'] = request.show_progress
        if not DaraCore.is_null(request.show_storage_type):
            query['ShowStorageType'] = request.show_storage_type
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFullBackupList',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFullBackupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_full_backup_list_with_options_async(
        self,
        request: main_models.DescribeFullBackupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeFullBackupListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not DaraCore.is_null(request.backup_set_status):
            query['BackupSetStatus'] = request.backup_set_status
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.show_progress):
            query['ShowProgress'] = request.show_progress
        if not DaraCore.is_null(request.show_storage_type):
            query['ShowStorageType'] = request.show_storage_type
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeFullBackupList',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeFullBackupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_full_backup_list(
        self,
        request: main_models.DescribeFullBackupListRequest,
    ) -> main_models.DescribeFullBackupListResponse:
        runtime = RuntimeOptions()
        return self.describe_full_backup_list_with_options(request, runtime)

    async def describe_full_backup_list_async(
        self,
        request: main_models.DescribeFullBackupListRequest,
    ) -> main_models.DescribeFullBackupListResponse:
        runtime = RuntimeOptions()
        return await self.describe_full_backup_list_with_options_async(request, runtime)

    def describe_increment_backup_list_with_options(
        self,
        request: main_models.DescribeIncrementBackupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIncrementBackupListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.show_storage_type):
            query['ShowStorageType'] = request.show_storage_type
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIncrementBackupList',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIncrementBackupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_increment_backup_list_with_options_async(
        self,
        request: main_models.DescribeIncrementBackupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeIncrementBackupListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.show_storage_type):
            query['ShowStorageType'] = request.show_storage_type
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeIncrementBackupList',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeIncrementBackupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_increment_backup_list(
        self,
        request: main_models.DescribeIncrementBackupListRequest,
    ) -> main_models.DescribeIncrementBackupListResponse:
        runtime = RuntimeOptions()
        return self.describe_increment_backup_list_with_options(request, runtime)

    async def describe_increment_backup_list_async(
        self,
        request: main_models.DescribeIncrementBackupListRequest,
    ) -> main_models.DescribeIncrementBackupListResponse:
        runtime = RuntimeOptions()
        return await self.describe_increment_backup_list_with_options_async(request, runtime)

    def describe_job_error_code_with_options(
        self,
        request: main_models.DescribeJobErrorCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobErrorCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobErrorCode',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobErrorCodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_job_error_code_with_options_async(
        self,
        request: main_models.DescribeJobErrorCodeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeJobErrorCodeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeJobErrorCode',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeJobErrorCodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_job_error_code(
        self,
        request: main_models.DescribeJobErrorCodeRequest,
    ) -> main_models.DescribeJobErrorCodeResponse:
        runtime = RuntimeOptions()
        return self.describe_job_error_code_with_options(request, runtime)

    async def describe_job_error_code_async(
        self,
        request: main_models.DescribeJobErrorCodeRequest,
    ) -> main_models.DescribeJobErrorCodeResponse:
        runtime = RuntimeOptions()
        return await self.describe_job_error_code_with_options_async(request, runtime)

    def describe_node_cidr_list_with_options(
        self,
        request: main_models.DescribeNodeCidrListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNodeCidrListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNodeCidrList',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNodeCidrListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_node_cidr_list_with_options_async(
        self,
        request: main_models.DescribeNodeCidrListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeNodeCidrListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.region):
            query['Region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeNodeCidrList',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeNodeCidrListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_node_cidr_list(
        self,
        request: main_models.DescribeNodeCidrListRequest,
    ) -> main_models.DescribeNodeCidrListResponse:
        runtime = RuntimeOptions()
        return self.describe_node_cidr_list_with_options(request, runtime)

    async def describe_node_cidr_list_async(
        self,
        request: main_models.DescribeNodeCidrListRequest,
    ) -> main_models.DescribeNodeCidrListResponse:
        runtime = RuntimeOptions()
        return await self.describe_node_cidr_list_with_options_async(request, runtime)

    def describe_pre_check_progress_list_with_options(
        self,
        request: main_models.DescribePreCheckProgressListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePreCheckProgressListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.restore_task_id):
            query['RestoreTaskId'] = request.restore_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePreCheckProgressList',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePreCheckProgressListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_pre_check_progress_list_with_options_async(
        self,
        request: main_models.DescribePreCheckProgressListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribePreCheckProgressListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.restore_task_id):
            query['RestoreTaskId'] = request.restore_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribePreCheckProgressList',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribePreCheckProgressListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_pre_check_progress_list(
        self,
        request: main_models.DescribePreCheckProgressListRequest,
    ) -> main_models.DescribePreCheckProgressListResponse:
        runtime = RuntimeOptions()
        return self.describe_pre_check_progress_list_with_options(request, runtime)

    async def describe_pre_check_progress_list_async(
        self,
        request: main_models.DescribePreCheckProgressListRequest,
    ) -> main_models.DescribePreCheckProgressListResponse:
        runtime = RuntimeOptions()
        return await self.describe_pre_check_progress_list_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_restore_range_info_with_options(
        self,
        request: main_models.DescribeRestoreRangeInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreRangeInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.begin_timestamp_for_restore):
            query['BeginTimestampForRestore'] = request.begin_timestamp_for_restore
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.end_timestamp_for_restore):
            query['EndTimestampForRestore'] = request.end_timestamp_for_restore
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.recently_restore):
            query['RecentlyRestore'] = request.recently_restore
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRestoreRangeInfo',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreRangeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_range_info_with_options_async(
        self,
        request: main_models.DescribeRestoreRangeInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreRangeInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.begin_timestamp_for_restore):
            query['BeginTimestampForRestore'] = request.begin_timestamp_for_restore
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.end_timestamp_for_restore):
            query['EndTimestampForRestore'] = request.end_timestamp_for_restore
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.recently_restore):
            query['RecentlyRestore'] = request.recently_restore
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRestoreRangeInfo',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreRangeInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_range_info(
        self,
        request: main_models.DescribeRestoreRangeInfoRequest,
    ) -> main_models.DescribeRestoreRangeInfoResponse:
        runtime = RuntimeOptions()
        return self.describe_restore_range_info_with_options(request, runtime)

    async def describe_restore_range_info_async(
        self,
        request: main_models.DescribeRestoreRangeInfoRequest,
    ) -> main_models.DescribeRestoreRangeInfoResponse:
        runtime = RuntimeOptions()
        return await self.describe_restore_range_info_with_options_async(request, runtime)

    def describe_restore_task_list_with_options(
        self,
        request: main_models.DescribeRestoreTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.restore_task_id):
            query['RestoreTaskId'] = request.restore_task_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRestoreTaskList',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_restore_task_list_with_options_async(
        self,
        request: main_models.DescribeRestoreTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRestoreTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.end_timestamp):
            query['EndTimestamp'] = request.end_timestamp
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.page_num):
            query['PageNum'] = request.page_num
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.restore_task_id):
            query['RestoreTaskId'] = request.restore_task_id
        if not DaraCore.is_null(request.start_timestamp):
            query['StartTimestamp'] = request.start_timestamp
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRestoreTaskList',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRestoreTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_restore_task_list(
        self,
        request: main_models.DescribeRestoreTaskListRequest,
    ) -> main_models.DescribeRestoreTaskListResponse:
        runtime = RuntimeOptions()
        return self.describe_restore_task_list_with_options(request, runtime)

    async def describe_restore_task_list_async(
        self,
        request: main_models.DescribeRestoreTaskListRequest,
    ) -> main_models.DescribeRestoreTaskListResponse:
        runtime = RuntimeOptions()
        return await self.describe_restore_task_list_with_options_async(request, runtime)

    def disable_backup_log_with_options(
        self,
        request: main_models.DisableBackupLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableBackupLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disable_mysql_physical_backup_binlog_only):
            query['DisableMysqlPhysicalBackupBinlogOnly'] = request.disable_mysql_physical_backup_binlog_only
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableBackupLog',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableBackupLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_backup_log_with_options_async(
        self,
        request: main_models.DisableBackupLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableBackupLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disable_mysql_physical_backup_binlog_only):
            query['DisableMysqlPhysicalBackupBinlogOnly'] = request.disable_mysql_physical_backup_binlog_only
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableBackupLog',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableBackupLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_backup_log(
        self,
        request: main_models.DisableBackupLogRequest,
    ) -> main_models.DisableBackupLogResponse:
        runtime = RuntimeOptions()
        return self.disable_backup_log_with_options(request, runtime)

    async def disable_backup_log_async(
        self,
        request: main_models.DisableBackupLogRequest,
    ) -> main_models.DisableBackupLogResponse:
        runtime = RuntimeOptions()
        return await self.disable_backup_log_with_options_async(request, runtime)

    def enable_backup_log_with_options(
        self,
        request: main_models.EnableBackupLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableBackupLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_mysql_physical_backup_binlog):
            query['EnableMysqlPhysicalBackupBinlog'] = request.enable_mysql_physical_backup_binlog
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableBackupLog',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableBackupLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_backup_log_with_options_async(
        self,
        request: main_models.EnableBackupLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableBackupLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.enable_mysql_physical_backup_binlog):
            query['EnableMysqlPhysicalBackupBinlog'] = request.enable_mysql_physical_backup_binlog
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableBackupLog',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableBackupLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_backup_log(
        self,
        request: main_models.EnableBackupLogRequest,
    ) -> main_models.EnableBackupLogResponse:
        runtime = RuntimeOptions()
        return self.enable_backup_log_with_options(request, runtime)

    async def enable_backup_log_async(
        self,
        request: main_models.EnableBackupLogRequest,
    ) -> main_models.EnableBackupLogResponse:
        runtime = RuntimeOptions()
        return await self.enable_backup_log_with_options_async(request, runtime)

    def get_dblist_from_agent_with_options(
        self,
        request: main_models.GetDBListFromAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDBListFromAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDBListFromAgent',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDBListFromAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_dblist_from_agent_with_options_async(
        self,
        request: main_models.GetDBListFromAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDBListFromAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDBListFromAgent',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDBListFromAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_dblist_from_agent(
        self,
        request: main_models.GetDBListFromAgentRequest,
    ) -> main_models.GetDBListFromAgentResponse:
        runtime = RuntimeOptions()
        return self.get_dblist_from_agent_with_options(request, runtime)

    async def get_dblist_from_agent_async(
        self,
        request: main_models.GetDBListFromAgentRequest,
    ) -> main_models.GetDBListFromAgentResponse:
        runtime = RuntimeOptions()
        return await self.get_dblist_from_agent_with_options_async(request, runtime)

    def initialize_dbs_service_linked_role_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.InitializeDbsServiceLinkedRoleResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'InitializeDbsServiceLinkedRole',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitializeDbsServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def initialize_dbs_service_linked_role_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.InitializeDbsServiceLinkedRoleResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'InitializeDbsServiceLinkedRole',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InitializeDbsServiceLinkedRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def initialize_dbs_service_linked_role(self) -> main_models.InitializeDbsServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return self.initialize_dbs_service_linked_role_with_options(runtime)

    async def initialize_dbs_service_linked_role_async(self) -> main_models.InitializeDbsServiceLinkedRoleResponse:
        runtime = RuntimeOptions()
        return await self.initialize_dbs_service_linked_role_with_options_async(runtime)

    def modify_backup_objects_with_options(
        self,
        request: main_models.ModifyBackupObjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupObjects',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_objects_with_options_async(
        self,
        request: main_models.ModifyBackupObjectsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupObjects',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupObjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_objects(
        self,
        request: main_models.ModifyBackupObjectsRequest,
    ) -> main_models.ModifyBackupObjectsResponse:
        runtime = RuntimeOptions()
        return self.modify_backup_objects_with_options(request, runtime)

    async def modify_backup_objects_async(
        self,
        request: main_models.ModifyBackupObjectsRequest,
    ) -> main_models.ModifyBackupObjectsResponse:
        runtime = RuntimeOptions()
        return await self.modify_backup_objects_with_options_async(request, runtime)

    def modify_backup_plan_name_with_options(
        self,
        request: main_models.ModifyBackupPlanNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupPlanNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupPlanName',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupPlanNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_plan_name_with_options_async(
        self,
        request: main_models.ModifyBackupPlanNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupPlanNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_plan_name):
            query['BackupPlanName'] = request.backup_plan_name
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupPlanName',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupPlanNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_plan_name(
        self,
        request: main_models.ModifyBackupPlanNameRequest,
    ) -> main_models.ModifyBackupPlanNameResponse:
        runtime = RuntimeOptions()
        return self.modify_backup_plan_name_with_options(request, runtime)

    async def modify_backup_plan_name_async(
        self,
        request: main_models.ModifyBackupPlanNameRequest,
    ) -> main_models.ModifyBackupPlanNameResponse:
        runtime = RuntimeOptions()
        return await self.modify_backup_plan_name_with_options_async(request, runtime)

    def modify_backup_set_download_rules_with_options(
        self,
        request: main_models.ModifyBackupSetDownloadRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupSetDownloadRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_set_download_dir):
            query['BackupSetDownloadDir'] = request.backup_set_download_dir
        if not DaraCore.is_null(request.backup_set_download_target_type):
            query['BackupSetDownloadTargetType'] = request.backup_set_download_target_type
        if not DaraCore.is_null(request.backup_set_download_target_type_location):
            query['BackupSetDownloadTargetTypeLocation'] = request.backup_set_download_target_type_location
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.full_data_format):
            query['FullDataFormat'] = request.full_data_format
        if not DaraCore.is_null(request.increment_data_format):
            query['IncrementDataFormat'] = request.increment_data_format
        if not DaraCore.is_null(request.open_auto_download):
            query['OpenAutoDownload'] = request.open_auto_download
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupSetDownloadRules',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupSetDownloadRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_set_download_rules_with_options_async(
        self,
        request: main_models.ModifyBackupSetDownloadRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupSetDownloadRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_set_download_dir):
            query['BackupSetDownloadDir'] = request.backup_set_download_dir
        if not DaraCore.is_null(request.backup_set_download_target_type):
            query['BackupSetDownloadTargetType'] = request.backup_set_download_target_type
        if not DaraCore.is_null(request.backup_set_download_target_type_location):
            query['BackupSetDownloadTargetTypeLocation'] = request.backup_set_download_target_type_location
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.full_data_format):
            query['FullDataFormat'] = request.full_data_format
        if not DaraCore.is_null(request.increment_data_format):
            query['IncrementDataFormat'] = request.increment_data_format
        if not DaraCore.is_null(request.open_auto_download):
            query['OpenAutoDownload'] = request.open_auto_download
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupSetDownloadRules',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupSetDownloadRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_set_download_rules(
        self,
        request: main_models.ModifyBackupSetDownloadRulesRequest,
    ) -> main_models.ModifyBackupSetDownloadRulesResponse:
        runtime = RuntimeOptions()
        return self.modify_backup_set_download_rules_with_options(request, runtime)

    async def modify_backup_set_download_rules_async(
        self,
        request: main_models.ModifyBackupSetDownloadRulesRequest,
    ) -> main_models.ModifyBackupSetDownloadRulesResponse:
        runtime = RuntimeOptions()
        return await self.modify_backup_set_download_rules_with_options_async(request, runtime)

    def modify_backup_source_endpoint_with_options(
        self,
        request: main_models.ModifyBackupSourceEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupSourceEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not DaraCore.is_null(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not DaraCore.is_null(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not DaraCore.is_null(request.enable_source_endpoint_ssl):
            query['EnableSourceEndpointSsl'] = request.enable_source_endpoint_ssl
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not DaraCore.is_null(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not DaraCore.is_null(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not DaraCore.is_null(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not DaraCore.is_null(request.source_endpoint_oracle_home):
            query['SourceEndpointOracleHome'] = request.source_endpoint_oracle_home
        if not DaraCore.is_null(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not DaraCore.is_null(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not DaraCore.is_null(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not DaraCore.is_null(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not DaraCore.is_null(request.ssl_ca_pem):
            query['SslCaPem'] = request.ssl_ca_pem
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupSourceEndpoint',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupSourceEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_source_endpoint_with_options_async(
        self,
        request: main_models.ModifyBackupSourceEndpointRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupSourceEndpointResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_gateway_id):
            query['BackupGatewayId'] = request.backup_gateway_id
        if not DaraCore.is_null(request.backup_objects):
            query['BackupObjects'] = request.backup_objects
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.cross_aliyun_id):
            query['CrossAliyunId'] = request.cross_aliyun_id
        if not DaraCore.is_null(request.cross_role_name):
            query['CrossRoleName'] = request.cross_role_name
        if not DaraCore.is_null(request.enable_source_endpoint_ssl):
            query['EnableSourceEndpointSsl'] = request.enable_source_endpoint_ssl
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.source_endpoint_database_name):
            query['SourceEndpointDatabaseName'] = request.source_endpoint_database_name
        if not DaraCore.is_null(request.source_endpoint_ip):
            query['SourceEndpointIP'] = request.source_endpoint_ip
        if not DaraCore.is_null(request.source_endpoint_instance_id):
            query['SourceEndpointInstanceID'] = request.source_endpoint_instance_id
        if not DaraCore.is_null(request.source_endpoint_instance_type):
            query['SourceEndpointInstanceType'] = request.source_endpoint_instance_type
        if not DaraCore.is_null(request.source_endpoint_oracle_home):
            query['SourceEndpointOracleHome'] = request.source_endpoint_oracle_home
        if not DaraCore.is_null(request.source_endpoint_oracle_sid):
            query['SourceEndpointOracleSID'] = request.source_endpoint_oracle_sid
        if not DaraCore.is_null(request.source_endpoint_password):
            query['SourceEndpointPassword'] = request.source_endpoint_password
        if not DaraCore.is_null(request.source_endpoint_port):
            query['SourceEndpointPort'] = request.source_endpoint_port
        if not DaraCore.is_null(request.source_endpoint_region):
            query['SourceEndpointRegion'] = request.source_endpoint_region
        if not DaraCore.is_null(request.source_endpoint_user_name):
            query['SourceEndpointUserName'] = request.source_endpoint_user_name
        if not DaraCore.is_null(request.ssl_ca_pem):
            query['SslCaPem'] = request.ssl_ca_pem
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupSourceEndpoint',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupSourceEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_source_endpoint(
        self,
        request: main_models.ModifyBackupSourceEndpointRequest,
    ) -> main_models.ModifyBackupSourceEndpointResponse:
        runtime = RuntimeOptions()
        return self.modify_backup_source_endpoint_with_options(request, runtime)

    async def modify_backup_source_endpoint_async(
        self,
        request: main_models.ModifyBackupSourceEndpointRequest,
    ) -> main_models.ModifyBackupSourceEndpointResponse:
        runtime = RuntimeOptions()
        return await self.modify_backup_source_endpoint_with_options_async(request, runtime)

    def modify_backup_strategy_with_options(
        self,
        request: main_models.ModifyBackupStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_log_interval_seconds):
            query['BackupLogIntervalSeconds'] = request.backup_log_interval_seconds
        if not DaraCore.is_null(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_start_time):
            query['BackupStartTime'] = request.backup_start_time
        if not DaraCore.is_null(request.backup_strategy_type):
            query['BackupStrategyType'] = request.backup_strategy_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupStrategy',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_strategy_with_options_async(
        self,
        request: main_models.ModifyBackupStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyBackupStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_log_interval_seconds):
            query['BackupLogIntervalSeconds'] = request.backup_log_interval_seconds
        if not DaraCore.is_null(request.backup_period):
            query['BackupPeriod'] = request.backup_period
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_start_time):
            query['BackupStartTime'] = request.backup_start_time
        if not DaraCore.is_null(request.backup_strategy_type):
            query['BackupStrategyType'] = request.backup_strategy_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyBackupStrategy',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyBackupStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_strategy(
        self,
        request: main_models.ModifyBackupStrategyRequest,
    ) -> main_models.ModifyBackupStrategyResponse:
        runtime = RuntimeOptions()
        return self.modify_backup_strategy_with_options(request, runtime)

    async def modify_backup_strategy_async(
        self,
        request: main_models.ModifyBackupStrategyRequest,
    ) -> main_models.ModifyBackupStrategyResponse:
        runtime = RuntimeOptions()
        return await self.modify_backup_strategy_with_options_async(request, runtime)

    def modify_storage_strategy_with_options(
        self,
        request: main_models.ModifyStorageStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyStorageStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.backup_storage_encrypt_method):
            query['BackupStorageEncryptMethod'] = request.backup_storage_encrypt_method
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.duplication_archive_period):
            query['DuplicationArchivePeriod'] = request.duplication_archive_period
        if not DaraCore.is_null(request.duplication_infrequent_access_period):
            query['DuplicationInfrequentAccessPeriod'] = request.duplication_infrequent_access_period
        if not DaraCore.is_null(request.increment_backup_retention_period):
            query['IncrementBackupRetentionPeriod'] = request.increment_backup_retention_period
        if not DaraCore.is_null(request.increment_duplication_archive_period):
            query['IncrementDuplicationArchivePeriod'] = request.increment_duplication_archive_period
        if not DaraCore.is_null(request.increment_duplication_infrequent_access_period):
            query['IncrementDuplicationInfrequentAccessPeriod'] = request.increment_duplication_infrequent_access_period
        if not DaraCore.is_null(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not DaraCore.is_null(request.log_duplication_archive_period):
            query['LogDuplicationArchivePeriod'] = request.log_duplication_archive_period
        if not DaraCore.is_null(request.log_duplication_infrequent_access_period):
            query['LogDuplicationInfrequentAccessPeriod'] = request.log_duplication_infrequent_access_period
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyStorageStrategy',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyStorageStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_storage_strategy_with_options_async(
        self,
        request: main_models.ModifyStorageStrategyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyStorageStrategyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not DaraCore.is_null(request.backup_storage_encrypt_method):
            query['BackupStorageEncryptMethod'] = request.backup_storage_encrypt_method
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.duplication_archive_period):
            query['DuplicationArchivePeriod'] = request.duplication_archive_period
        if not DaraCore.is_null(request.duplication_infrequent_access_period):
            query['DuplicationInfrequentAccessPeriod'] = request.duplication_infrequent_access_period
        if not DaraCore.is_null(request.increment_backup_retention_period):
            query['IncrementBackupRetentionPeriod'] = request.increment_backup_retention_period
        if not DaraCore.is_null(request.increment_duplication_archive_period):
            query['IncrementDuplicationArchivePeriod'] = request.increment_duplication_archive_period
        if not DaraCore.is_null(request.increment_duplication_infrequent_access_period):
            query['IncrementDuplicationInfrequentAccessPeriod'] = request.increment_duplication_infrequent_access_period
        if not DaraCore.is_null(request.log_backup_retention_period):
            query['LogBackupRetentionPeriod'] = request.log_backup_retention_period
        if not DaraCore.is_null(request.log_duplication_archive_period):
            query['LogDuplicationArchivePeriod'] = request.log_duplication_archive_period
        if not DaraCore.is_null(request.log_duplication_infrequent_access_period):
            query['LogDuplicationInfrequentAccessPeriod'] = request.log_duplication_infrequent_access_period
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyStorageStrategy',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyStorageStrategyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_storage_strategy(
        self,
        request: main_models.ModifyStorageStrategyRequest,
    ) -> main_models.ModifyStorageStrategyResponse:
        runtime = RuntimeOptions()
        return self.modify_storage_strategy_with_options(request, runtime)

    async def modify_storage_strategy_async(
        self,
        request: main_models.ModifyStorageStrategyRequest,
    ) -> main_models.ModifyStorageStrategyResponse:
        runtime = RuntimeOptions()
        return await self.modify_storage_strategy_with_options_async(request, runtime)

    def release_backup_plan_with_options(
        self,
        request: main_models.ReleaseBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseBackupPlan',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_backup_plan_with_options_async(
        self,
        request: main_models.ReleaseBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseBackupPlan',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_backup_plan(
        self,
        request: main_models.ReleaseBackupPlanRequest,
    ) -> main_models.ReleaseBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.release_backup_plan_with_options(request, runtime)

    async def release_backup_plan_async(
        self,
        request: main_models.ReleaseBackupPlanRequest,
    ) -> main_models.ReleaseBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.release_backup_plan_with_options_async(request, runtime)

    def renew_backup_plan_with_options(
        self,
        request: main_models.RenewBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewBackupPlan',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_backup_plan_with_options_async(
        self,
        request: main_models.RenewBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.used_time):
            query['UsedTime'] = request.used_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewBackupPlan',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_backup_plan(
        self,
        request: main_models.RenewBackupPlanRequest,
    ) -> main_models.RenewBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.renew_backup_plan_with_options(request, runtime)

    async def renew_backup_plan_async(
        self,
        request: main_models.RenewBackupPlanRequest,
    ) -> main_models.RenewBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.renew_backup_plan_with_options_async(request, runtime)

    def start_backup_plan_with_options(
        self,
        request: main_models.StartBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartBackupPlan',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_backup_plan_with_options_async(
        self,
        request: main_models.StartBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartBackupPlan',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_backup_plan(
        self,
        request: main_models.StartBackupPlanRequest,
    ) -> main_models.StartBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.start_backup_plan_with_options(request, runtime)

    async def start_backup_plan_async(
        self,
        request: main_models.StartBackupPlanRequest,
    ) -> main_models.StartBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.start_backup_plan_with_options_async(request, runtime)

    def start_restore_task_with_options(
        self,
        request: main_models.StartRestoreTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartRestoreTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.restore_task_id):
            query['RestoreTaskId'] = request.restore_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartRestoreTask',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartRestoreTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_restore_task_with_options_async(
        self,
        request: main_models.StartRestoreTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartRestoreTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.restore_task_id):
            query['RestoreTaskId'] = request.restore_task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartRestoreTask',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartRestoreTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_restore_task(
        self,
        request: main_models.StartRestoreTaskRequest,
    ) -> main_models.StartRestoreTaskResponse:
        runtime = RuntimeOptions()
        return self.start_restore_task_with_options(request, runtime)

    async def start_restore_task_async(
        self,
        request: main_models.StartRestoreTaskRequest,
    ) -> main_models.StartRestoreTaskResponse:
        runtime = RuntimeOptions()
        return await self.start_restore_task_with_options_async(request, runtime)

    def stop_backup_plan_with_options(
        self,
        request: main_models.StopBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.stop_method):
            query['StopMethod'] = request.stop_method
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopBackupPlan',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_backup_plan_with_options_async(
        self,
        request: main_models.StopBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not DaraCore.is_null(request.stop_method):
            query['StopMethod'] = request.stop_method
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopBackupPlan',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_backup_plan(
        self,
        request: main_models.StopBackupPlanRequest,
    ) -> main_models.StopBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.stop_backup_plan_with_options(request, runtime)

    async def stop_backup_plan_async(
        self,
        request: main_models.StopBackupPlanRequest,
    ) -> main_models.StopBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.stop_backup_plan_with_options_async(request, runtime)

    def upgrade_backup_plan_with_options(
        self,
        request: main_models.UpgradeBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeBackupPlan',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeBackupPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_backup_plan_with_options_async(
        self,
        request: main_models.UpgradeBackupPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeBackupPlanResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_plan_id):
            query['BackupPlanId'] = request.backup_plan_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.instance_class):
            query['InstanceClass'] = request.instance_class
        if not DaraCore.is_null(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeBackupPlan',
            version = '2019-03-06',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeBackupPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_backup_plan(
        self,
        request: main_models.UpgradeBackupPlanRequest,
    ) -> main_models.UpgradeBackupPlanResponse:
        runtime = RuntimeOptions()
        return self.upgrade_backup_plan_with_options(request, runtime)

    async def upgrade_backup_plan_async(
        self,
        request: main_models.UpgradeBackupPlanRequest,
    ) -> main_models.UpgradeBackupPlanResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_backup_plan_with_options_async(request, runtime)
