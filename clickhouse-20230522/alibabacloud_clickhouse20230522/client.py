# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_clickhouse20230522 import models as clickhouse_20230522_models
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
            'ap-northeast-2-pop': 'clickhouse.aliyuncs.com',
            'ap-southeast-1': 'clickhouse.aliyuncs.com',
            'cn-beijing': 'clickhouse.aliyuncs.com',
            'cn-beijing-finance-1': 'clickhouse.aliyuncs.com',
            'cn-beijing-finance-pop': 'clickhouse.aliyuncs.com',
            'cn-beijing-gov-1': 'clickhouse.aliyuncs.com',
            'cn-beijing-nu16-b01': 'clickhouse.aliyuncs.com',
            'cn-edge-1': 'clickhouse.aliyuncs.com',
            'cn-fujian': 'clickhouse.aliyuncs.com',
            'cn-haidian-cm12-c01': 'clickhouse.aliyuncs.com',
            'cn-hangzhou': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-finance': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'clickhouse.aliyuncs.com',
            'cn-hangzhou-test-306': 'clickhouse.aliyuncs.com',
            'cn-hongkong': 'clickhouse.aliyuncs.com',
            'cn-hongkong-finance-pop': 'clickhouse.aliyuncs.com',
            'cn-north-2-gov-1': 'clickhouse.aliyuncs.com',
            'cn-qingdao': 'clickhouse.aliyuncs.com',
            'cn-qingdao-nebula': 'clickhouse.aliyuncs.com',
            'cn-shanghai': 'clickhouse.aliyuncs.com',
            'cn-shanghai-et15-b01': 'clickhouse.aliyuncs.com',
            'cn-shanghai-et2-b01': 'clickhouse.aliyuncs.com',
            'cn-shanghai-finance-1': 'clickhouse.aliyuncs.com',
            'cn-shanghai-inner': 'clickhouse.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'clickhouse.aliyuncs.com',
            'cn-shenzhen': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-finance-1': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-inner': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'clickhouse.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'clickhouse.aliyuncs.com',
            'cn-wuhan': 'clickhouse.aliyuncs.com',
            'cn-yushanfang': 'clickhouse.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'clickhouse.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'clickhouse.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'clickhouse.aliyuncs.com',
            'eu-west-1-oxs': 'clickhouse.aliyuncs.com',
            'me-east-1': 'clickhouse.aliyuncs.com',
            'rus-west-1-pop': 'clickhouse.aliyuncs.com',
            'us-east-1': 'clickhouse.aliyuncs.com',
            'us-west-1': 'clickhouse.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('clickhouse', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def change_resource_group_with_options(
        self,
        request: clickhouse_20230522_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ChangeResourceGroupResponse:
        """
        @summary 资源转组
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: clickhouse_20230522_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ChangeResourceGroupResponse:
        """
        @summary 资源转组
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: clickhouse_20230522_models.ChangeResourceGroupRequest,
    ) -> clickhouse_20230522_models.ChangeResourceGroupResponse:
        """
        @summary 资源转组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: clickhouse_20230522_models.ChangeResourceGroupRequest,
    ) -> clickhouse_20230522_models.ChangeResourceGroupResponse:
        """
        @summary 资源转组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def create_account_with_options(
        self,
        tmp_req: clickhouse_20230522_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateAccountResponse:
        """
        @summary Creates a database account for an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param tmp_req: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
        UtilClient.validate_model(tmp_req)
        request = clickhouse_20230522_models.CreateAccountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dml_auth_setting):
            request.dml_auth_setting_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dml_auth_setting, 'DmlAuthSetting', 'json')
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dml_auth_setting_shrink):
            query['DmlAuthSetting'] = request.dml_auth_setting_shrink
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_with_options_async(
        self,
        tmp_req: clickhouse_20230522_models.CreateAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateAccountResponse:
        """
        @summary Creates a database account for an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param tmp_req: CreateAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateAccountResponse
        """
        UtilClient.validate_model(tmp_req)
        request = clickhouse_20230522_models.CreateAccountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dml_auth_setting):
            request.dml_auth_setting_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dml_auth_setting, 'DmlAuthSetting', 'json')
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.account_type):
            query['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dml_auth_setting_shrink):
            query['DmlAuthSetting'] = request.dml_auth_setting_shrink
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account(
        self,
        request: clickhouse_20230522_models.CreateAccountRequest,
    ) -> clickhouse_20230522_models.CreateAccountResponse:
        """
        @summary Creates a database account for an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    async def create_account_async(
        self,
        request: clickhouse_20230522_models.CreateAccountRequest,
    ) -> clickhouse_20230522_models.CreateAccountResponse:
        """
        @summary Creates a database account for an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: CreateAccountRequest
        @return: CreateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_account_with_options_async(request, runtime)

    def create_backup_policy_with_options(
        self,
        request: clickhouse_20230522_models.CreateBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateBackupPolicyResponse:
        """
        @summary Creates a backup policy for a specified ApsaraDB for ClickHouse cluster that runs Enterprise Edition.
        
        @param request: CreateBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackupPolicy',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_policy_with_options_async(
        self,
        request: clickhouse_20230522_models.CreateBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateBackupPolicyResponse:
        """
        @summary Creates a backup policy for a specified ApsaraDB for ClickHouse cluster that runs Enterprise Edition.
        
        @param request: CreateBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBackupPolicy',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup_policy(
        self,
        request: clickhouse_20230522_models.CreateBackupPolicyRequest,
    ) -> clickhouse_20230522_models.CreateBackupPolicyResponse:
        """
        @summary Creates a backup policy for a specified ApsaraDB for ClickHouse cluster that runs Enterprise Edition.
        
        @param request: CreateBackupPolicyRequest
        @return: CreateBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_backup_policy_with_options(request, runtime)

    async def create_backup_policy_async(
        self,
        request: clickhouse_20230522_models.CreateBackupPolicyRequest,
    ) -> clickhouse_20230522_models.CreateBackupPolicyResponse:
        """
        @summary Creates a backup policy for a specified ApsaraDB for ClickHouse cluster that runs Enterprise Edition.
        
        @param request: CreateBackupPolicyRequest
        @return: CreateBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_backup_policy_with_options_async(request, runtime)

    def create_dbwith_options(
        self,
        request: clickhouse_20230522_models.CreateDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateDBResponse:
        """
        @summary Creates an ApsaraDB for ClickHouse database.
        
        @param request: CreateDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDB',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbwith_options_async(
        self,
        request: clickhouse_20230522_models.CreateDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateDBResponse:
        """
        @summary Creates an ApsaraDB for ClickHouse database.
        
        @param request: CreateDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDB',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_db(
        self,
        request: clickhouse_20230522_models.CreateDBRequest,
    ) -> clickhouse_20230522_models.CreateDBResponse:
        """
        @summary Creates an ApsaraDB for ClickHouse database.
        
        @param request: CreateDBRequest
        @return: CreateDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbwith_options(request, runtime)

    async def create_db_async(
        self,
        request: clickhouse_20230522_models.CreateDBRequest,
    ) -> clickhouse_20230522_models.CreateDBResponse:
        """
        @summary Creates an ApsaraDB for ClickHouse database.
        
        @param request: CreateDBRequest
        @return: CreateDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbwith_options_async(request, runtime)

    def create_dbinstance_with_options(
        self,
        tmp_req: clickhouse_20230522_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateDBInstanceResponse:
        """
        @summary Creates an ApsaraDB for ClickHouse cluster that runs Enterprise Edition.
        
        @param tmp_req: CreateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = clickhouse_20230522_models.CreateDBInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.multi_zone):
            request.multi_zone_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.multi_zone, 'MultiZone', 'json')
        query = {}
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbtime_zone):
            query['DBTimeZone'] = request.dbtime_zone
        if not UtilClient.is_unset(request.deploy_schema):
            query['DeploySchema'] = request.deploy_schema
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.multi_zone_shrink):
            query['MultiZone'] = request.multi_zone_shrink
        if not UtilClient.is_unset(request.node_count):
            query['NodeCount'] = request.node_count
        if not UtilClient.is_unset(request.node_scale_max):
            query['NodeScaleMax'] = request.node_scale_max
        if not UtilClient.is_unset(request.node_scale_min):
            query['NodeScaleMin'] = request.node_scale_min
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not UtilClient.is_unset(request.scale_min):
            query['ScaleMin'] = request.scale_min
        if not UtilClient.is_unset(request.source_dbinstance_id):
            query['SourceDBInstanceId'] = request.source_dbinstance_id
        if not UtilClient.is_unset(request.storage_quota):
            query['StorageQuota'] = request.storage_quota
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dbinstance_with_options_async(
        self,
        tmp_req: clickhouse_20230522_models.CreateDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateDBInstanceResponse:
        """
        @summary Creates an ApsaraDB for ClickHouse cluster that runs Enterprise Edition.
        
        @param tmp_req: CreateDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateDBInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = clickhouse_20230522_models.CreateDBInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.multi_zone):
            request.multi_zone_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.multi_zone, 'MultiZone', 'json')
        query = {}
        if not UtilClient.is_unset(request.backup_set_id):
            query['BackupSetId'] = request.backup_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dbinstance_description):
            query['DBInstanceDescription'] = request.dbinstance_description
        if not UtilClient.is_unset(request.dbtime_zone):
            query['DBTimeZone'] = request.dbtime_zone
        if not UtilClient.is_unset(request.deploy_schema):
            query['DeploySchema'] = request.deploy_schema
        if not UtilClient.is_unset(request.engine):
            query['Engine'] = request.engine
        if not UtilClient.is_unset(request.engine_version):
            query['EngineVersion'] = request.engine_version
        if not UtilClient.is_unset(request.multi_zone_shrink):
            query['MultiZone'] = request.multi_zone_shrink
        if not UtilClient.is_unset(request.node_count):
            query['NodeCount'] = request.node_count
        if not UtilClient.is_unset(request.node_scale_max):
            query['NodeScaleMax'] = request.node_scale_max
        if not UtilClient.is_unset(request.node_scale_min):
            query['NodeScaleMin'] = request.node_scale_min
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not UtilClient.is_unset(request.scale_min):
            query['ScaleMin'] = request.scale_min
        if not UtilClient.is_unset(request.source_dbinstance_id):
            query['SourceDBInstanceId'] = request.source_dbinstance_id
        if not UtilClient.is_unset(request.storage_quota):
            query['StorageQuota'] = request.storage_quota
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dbinstance(
        self,
        request: clickhouse_20230522_models.CreateDBInstanceRequest,
    ) -> clickhouse_20230522_models.CreateDBInstanceResponse:
        """
        @summary Creates an ApsaraDB for ClickHouse cluster that runs Enterprise Edition.
        
        @param request: CreateDBInstanceRequest
        @return: CreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_dbinstance_with_options(request, runtime)

    async def create_dbinstance_async(
        self,
        request: clickhouse_20230522_models.CreateDBInstanceRequest,
    ) -> clickhouse_20230522_models.CreateDBInstanceResponse:
        """
        @summary Creates an ApsaraDB for ClickHouse cluster that runs Enterprise Edition.
        
        @param request: CreateDBInstanceRequest
        @return: CreateDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_dbinstance_with_options_async(request, runtime)

    def create_endpoint_with_options(
        self,
        request: clickhouse_20230522_models.CreateEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateEndpointResponse:
        """
        @summary Applies for a public endpoint.
        
        @param request: CreateEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_group_id):
            query['ComputingGroupId'] = request.computing_group_id
        if not UtilClient.is_unset(request.connection_prefix):
            query['ConnectionPrefix'] = request.connection_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_net_type):
            query['DBInstanceNetType'] = request.dbinstance_net_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEndpoint',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_endpoint_with_options_async(
        self,
        request: clickhouse_20230522_models.CreateEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.CreateEndpointResponse:
        """
        @summary Applies for a public endpoint.
        
        @param request: CreateEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_group_id):
            query['ComputingGroupId'] = request.computing_group_id
        if not UtilClient.is_unset(request.connection_prefix):
            query['ConnectionPrefix'] = request.connection_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_net_type):
            query['DBInstanceNetType'] = request.dbinstance_net_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEndpoint',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.CreateEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_endpoint(
        self,
        request: clickhouse_20230522_models.CreateEndpointRequest,
    ) -> clickhouse_20230522_models.CreateEndpointResponse:
        """
        @summary Applies for a public endpoint.
        
        @param request: CreateEndpointRequest
        @return: CreateEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_endpoint_with_options(request, runtime)

    async def create_endpoint_async(
        self,
        request: clickhouse_20230522_models.CreateEndpointRequest,
    ) -> clickhouse_20230522_models.CreateEndpointResponse:
        """
        @summary Applies for a public endpoint.
        
        @param request: CreateEndpointRequest
        @return: CreateEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_endpoint_with_options_async(request, runtime)

    def delete_account_with_options(
        self,
        request: clickhouse_20230522_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteAccountResponse:
        """
        @summary Deletes a database account from an ApsaraDB for ClickHouse cluster.
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_with_options_async(
        self,
        request: clickhouse_20230522_models.DeleteAccountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteAccountResponse:
        """
        @summary Deletes a database account from an ApsaraDB for ClickHouse cluster.
        
        @param request: DeleteAccountRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account(
        self,
        request: clickhouse_20230522_models.DeleteAccountRequest,
    ) -> clickhouse_20230522_models.DeleteAccountResponse:
        """
        @summary Deletes a database account from an ApsaraDB for ClickHouse cluster.
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    async def delete_account_async(
        self,
        request: clickhouse_20230522_models.DeleteAccountRequest,
    ) -> clickhouse_20230522_models.DeleteAccountResponse:
        """
        @summary Deletes a database account from an ApsaraDB for ClickHouse cluster.
        
        @param request: DeleteAccountRequest
        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_account_with_options_async(request, runtime)

    def delete_backup_policy_with_options(
        self,
        request: clickhouse_20230522_models.DeleteBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteBackupPolicyResponse:
        """
        @summary 修改备份策略
        
        @param request: DeleteBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupPolicy',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_policy_with_options_async(
        self,
        request: clickhouse_20230522_models.DeleteBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteBackupPolicyResponse:
        """
        @summary 修改备份策略
        
        @param request: DeleteBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBackupPolicy',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup_policy(
        self,
        request: clickhouse_20230522_models.DeleteBackupPolicyRequest,
    ) -> clickhouse_20230522_models.DeleteBackupPolicyResponse:
        """
        @summary 修改备份策略
        
        @param request: DeleteBackupPolicyRequest
        @return: DeleteBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_backup_policy_with_options(request, runtime)

    async def delete_backup_policy_async(
        self,
        request: clickhouse_20230522_models.DeleteBackupPolicyRequest,
    ) -> clickhouse_20230522_models.DeleteBackupPolicyResponse:
        """
        @summary 修改备份策略
        
        @param request: DeleteBackupPolicyRequest
        @return: DeleteBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_backup_policy_with_options_async(request, runtime)

    def delete_dbwith_options(
        self,
        request: clickhouse_20230522_models.DeleteDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteDBResponse:
        """
        @summary Deletes an ApsaraDB for ClickHouse database.
        
        @param request: DeleteDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDB',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteDBResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbwith_options_async(
        self,
        request: clickhouse_20230522_models.DeleteDBRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteDBResponse:
        """
        @summary Deletes an ApsaraDB for ClickHouse database.
        
        @param request: DeleteDBRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDB',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteDBResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_db(
        self,
        request: clickhouse_20230522_models.DeleteDBRequest,
    ) -> clickhouse_20230522_models.DeleteDBResponse:
        """
        @summary Deletes an ApsaraDB for ClickHouse database.
        
        @param request: DeleteDBRequest
        @return: DeleteDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbwith_options(request, runtime)

    async def delete_db_async(
        self,
        request: clickhouse_20230522_models.DeleteDBRequest,
    ) -> clickhouse_20230522_models.DeleteDBResponse:
        """
        @summary Deletes an ApsaraDB for ClickHouse database.
        
        @param request: DeleteDBRequest
        @return: DeleteDBResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbwith_options_async(request, runtime)

    def delete_dbinstance_with_options(
        self,
        request: clickhouse_20230522_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteDBInstanceResponse:
        """
        @summary Releases an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: DeleteDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dbinstance_with_options_async(
        self,
        request: clickhouse_20230522_models.DeleteDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteDBInstanceResponse:
        """
        @summary Releases an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: DeleteDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dbinstance(
        self,
        request: clickhouse_20230522_models.DeleteDBInstanceRequest,
    ) -> clickhouse_20230522_models.DeleteDBInstanceResponse:
        """
        @summary Releases an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: DeleteDBInstanceRequest
        @return: DeleteDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_dbinstance_with_options(request, runtime)

    async def delete_dbinstance_async(
        self,
        request: clickhouse_20230522_models.DeleteDBInstanceRequest,
    ) -> clickhouse_20230522_models.DeleteDBInstanceResponse:
        """
        @summary Releases an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: DeleteDBInstanceRequest
        @return: DeleteDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_dbinstance_with_options_async(request, runtime)

    def delete_endpoint_with_options(
        self,
        request: clickhouse_20230522_models.DeleteEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteEndpointResponse:
        """
        @summary Releases a public endpoint.
        
        @param request: DeleteEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_group_id):
            query['ComputingGroupId'] = request.computing_group_id
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_net_type):
            query['DBInstanceNetType'] = request.dbinstance_net_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEndpoint',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteEndpointResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_endpoint_with_options_async(
        self,
        request: clickhouse_20230522_models.DeleteEndpointRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DeleteEndpointResponse:
        """
        @summary Releases a public endpoint.
        
        @param request: DeleteEndpointRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteEndpointResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_group_id):
            query['ComputingGroupId'] = request.computing_group_id
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_net_type):
            query['DBInstanceNetType'] = request.dbinstance_net_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEndpoint',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DeleteEndpointResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_endpoint(
        self,
        request: clickhouse_20230522_models.DeleteEndpointRequest,
    ) -> clickhouse_20230522_models.DeleteEndpointResponse:
        """
        @summary Releases a public endpoint.
        
        @param request: DeleteEndpointRequest
        @return: DeleteEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_endpoint_with_options(request, runtime)

    async def delete_endpoint_async(
        self,
        request: clickhouse_20230522_models.DeleteEndpointRequest,
    ) -> clickhouse_20230522_models.DeleteEndpointResponse:
        """
        @summary Releases a public endpoint.
        
        @param request: DeleteEndpointRequest
        @return: DeleteEndpointResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_endpoint_with_options_async(request, runtime)

    def describe_account_authority_with_options(
        self,
        request: clickhouse_20230522_models.DescribeAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeAccountAuthorityResponse:
        """
        @summary Queries the permissions of a database account.
        
        @param request: DescribeAccountAuthorityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountAuthorityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountAuthority',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeAccountAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_account_authority_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeAccountAuthorityResponse:
        """
        @summary Queries the permissions of a database account.
        
        @param request: DescribeAccountAuthorityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountAuthorityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountAuthority',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeAccountAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_account_authority(
        self,
        request: clickhouse_20230522_models.DescribeAccountAuthorityRequest,
    ) -> clickhouse_20230522_models.DescribeAccountAuthorityResponse:
        """
        @summary Queries the permissions of a database account.
        
        @param request: DescribeAccountAuthorityRequest
        @return: DescribeAccountAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_account_authority_with_options(request, runtime)

    async def describe_account_authority_async(
        self,
        request: clickhouse_20230522_models.DescribeAccountAuthorityRequest,
    ) -> clickhouse_20230522_models.DescribeAccountAuthorityResponse:
        """
        @summary Queries the permissions of a database account.
        
        @param request: DescribeAccountAuthorityRequest
        @return: DescribeAccountAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_authority_with_options_async(request, runtime)

    def describe_accounts_with_options(
        self,
        request: clickhouse_20230522_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeAccountsResponse:
        """
        @summary Queries database accounts for an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_accounts_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeAccountsResponse:
        """
        @summary Queries database accounts for an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccounts',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_accounts(
        self,
        request: clickhouse_20230522_models.DescribeAccountsRequest,
    ) -> clickhouse_20230522_models.DescribeAccountsResponse:
        """
        @summary Queries database accounts for an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_accounts_with_options(request, runtime)

    async def describe_accounts_async(
        self,
        request: clickhouse_20230522_models.DescribeAccountsRequest,
    ) -> clickhouse_20230522_models.DescribeAccountsResponse:
        """
        @summary Queries database accounts for an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeAccountsRequest
        @return: DescribeAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_accounts_with_options_async(request, runtime)

    def describe_backup_policy_with_options(
        self,
        request: clickhouse_20230522_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeBackupPolicyResponse:
        """
        @summary 创建备份策略
        
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backup_policy_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeBackupPolicyResponse:
        """
        @summary 创建备份策略
        
        @param request: DescribeBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackupPolicy',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backup_policy(
        self,
        request: clickhouse_20230522_models.DescribeBackupPolicyRequest,
    ) -> clickhouse_20230522_models.DescribeBackupPolicyResponse:
        """
        @summary 创建备份策略
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backup_policy_with_options(request, runtime)

    async def describe_backup_policy_async(
        self,
        request: clickhouse_20230522_models.DescribeBackupPolicyRequest,
    ) -> clickhouse_20230522_models.DescribeBackupPolicyResponse:
        """
        @summary 创建备份策略
        
        @param request: DescribeBackupPolicyRequest
        @return: DescribeBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backup_policy_with_options_async(request, runtime)

    def describe_backups_with_options(
        self,
        request: clickhouse_20230522_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeBackupsResponse:
        """
        @summary 查询备份集
        
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_backups_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeBackupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeBackupsResponse:
        """
        @summary 查询备份集
        
        @param request: DescribeBackupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeBackupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_id):
            query['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBackups',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_backups(
        self,
        request: clickhouse_20230522_models.DescribeBackupsRequest,
    ) -> clickhouse_20230522_models.DescribeBackupsResponse:
        """
        @summary 查询备份集
        
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_backups_with_options(request, runtime)

    async def describe_backups_async(
        self,
        request: clickhouse_20230522_models.DescribeBackupsRequest,
    ) -> clickhouse_20230522_models.DescribeBackupsResponse:
        """
        @summary 查询备份集
        
        @param request: DescribeBackupsRequest
        @return: DescribeBackupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_backups_with_options_async(request, runtime)

    def describe_dbinstance_attribute_with_options(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeDBInstanceAttributeResponse:
        """
        @summary Queries the details of an ApsaraDB for ClickHouse cluster that runs Enterprise Edition.
        
        @param request: DescribeDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceAttribute',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeDBInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_attribute_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeDBInstanceAttributeResponse:
        """
        @summary Queries the details of an ApsaraDB for ClickHouse cluster that runs Enterprise Edition.
        
        @param request: DescribeDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceAttribute',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeDBInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_attribute(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceAttributeRequest,
    ) -> clickhouse_20230522_models.DescribeDBInstanceAttributeResponse:
        """
        @summary Queries the details of an ApsaraDB for ClickHouse cluster that runs Enterprise Edition.
        
        @param request: DescribeDBInstanceAttributeRequest
        @return: DescribeDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_attribute_with_options(request, runtime)

    async def describe_dbinstance_attribute_async(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceAttributeRequest,
    ) -> clickhouse_20230522_models.DescribeDBInstanceAttributeResponse:
        """
        @summary Queries the details of an ApsaraDB for ClickHouse cluster that runs Enterprise Edition.
        
        @param request: DescribeDBInstanceAttributeRequest
        @return: DescribeDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_attribute_with_options_async(request, runtime)

    def describe_dbinstance_config_with_options(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeDBInstanceConfigResponse:
        """
        @summary 查询实例参数配置
        
        @param request: DescribeDBInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceConfig',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeDBInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_config_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeDBInstanceConfigResponse:
        """
        @summary 查询实例参数配置
        
        @param request: DescribeDBInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceConfig',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeDBInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_config(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceConfigRequest,
    ) -> clickhouse_20230522_models.DescribeDBInstanceConfigResponse:
        """
        @summary 查询实例参数配置
        
        @param request: DescribeDBInstanceConfigRequest
        @return: DescribeDBInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_config_with_options(request, runtime)

    async def describe_dbinstance_config_async(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceConfigRequest,
    ) -> clickhouse_20230522_models.DescribeDBInstanceConfigResponse:
        """
        @summary 查询实例参数配置
        
        @param request: DescribeDBInstanceConfigRequest
        @return: DescribeDBInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_config_with_options_async(request, runtime)

    def describe_dbinstance_config_change_log_with_options(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceConfigChangeLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeDBInstanceConfigChangeLogResponse:
        """
        @summary 查询实例参数配置记录
        
        @param request: DescribeDBInstanceConfigChangeLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceConfigChangeLogResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceConfigChangeLog',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeDBInstanceConfigChangeLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_config_change_log_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceConfigChangeLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeDBInstanceConfigChangeLogResponse:
        """
        @summary 查询实例参数配置记录
        
        @param request: DescribeDBInstanceConfigChangeLogRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceConfigChangeLogResponse
        """
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceConfigChangeLog',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeDBInstanceConfigChangeLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_config_change_log(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceConfigChangeLogRequest,
    ) -> clickhouse_20230522_models.DescribeDBInstanceConfigChangeLogResponse:
        """
        @summary 查询实例参数配置记录
        
        @param request: DescribeDBInstanceConfigChangeLogRequest
        @return: DescribeDBInstanceConfigChangeLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_config_change_log_with_options(request, runtime)

    async def describe_dbinstance_config_change_log_async(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceConfigChangeLogRequest,
    ) -> clickhouse_20230522_models.DescribeDBInstanceConfigChangeLogResponse:
        """
        @summary 查询实例参数配置记录
        
        @param request: DescribeDBInstanceConfigChangeLogRequest
        @return: DescribeDBInstanceConfigChangeLogResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_config_change_log_with_options_async(request, runtime)

    def describe_dbinstance_data_sources_with_options(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeDBInstanceDataSourcesResponse:
        """
        @summary Queries the schema of a database or a table.
        
        @param request: DescribeDBInstanceDataSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceDataSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceDataSources',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeDBInstanceDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstance_data_sources_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceDataSourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeDBInstanceDataSourcesResponse:
        """
        @summary Queries the schema of a database or a table.
        
        @param request: DescribeDBInstanceDataSourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstanceDataSourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            query['DBName'] = request.dbname
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstanceDataSources',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeDBInstanceDataSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstance_data_sources(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceDataSourcesRequest,
    ) -> clickhouse_20230522_models.DescribeDBInstanceDataSourcesResponse:
        """
        @summary Queries the schema of a database or a table.
        
        @param request: DescribeDBInstanceDataSourcesRequest
        @return: DescribeDBInstanceDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstance_data_sources_with_options(request, runtime)

    async def describe_dbinstance_data_sources_async(
        self,
        request: clickhouse_20230522_models.DescribeDBInstanceDataSourcesRequest,
    ) -> clickhouse_20230522_models.DescribeDBInstanceDataSourcesResponse:
        """
        @summary Queries the schema of a database or a table.
        
        @param request: DescribeDBInstanceDataSourcesRequest
        @return: DescribeDBInstanceDataSourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstance_data_sources_with_options_async(request, runtime)

    def describe_dbinstances_with_options(
        self,
        request: clickhouse_20230522_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeDBInstancesResponse:
        """
        @summary Queries a list of ApsaraDB for ClickHouse clusters.
        
        @param request: DescribeDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not UtilClient.is_unset(request.dbinstance_status):
            query['DBInstanceStatus'] = request.dbinstance_status
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstances',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeDBInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dbinstances_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeDBInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeDBInstancesResponse:
        """
        @summary Queries a list of ApsaraDB for ClickHouse clusters.
        
        @param request: DescribeDBInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeDBInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_ids):
            query['DBInstanceIds'] = request.dbinstance_ids
        if not UtilClient.is_unset(request.dbinstance_status):
            query['DBInstanceStatus'] = request.dbinstance_status
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDBInstances',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeDBInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dbinstances(
        self,
        request: clickhouse_20230522_models.DescribeDBInstancesRequest,
    ) -> clickhouse_20230522_models.DescribeDBInstancesResponse:
        """
        @summary Queries a list of ApsaraDB for ClickHouse clusters.
        
        @param request: DescribeDBInstancesRequest
        @return: DescribeDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_dbinstances_with_options(request, runtime)

    async def describe_dbinstances_async(
        self,
        request: clickhouse_20230522_models.DescribeDBInstancesRequest,
    ) -> clickhouse_20230522_models.DescribeDBInstancesResponse:
        """
        @summary Queries a list of ApsaraDB for ClickHouse clusters.
        
        @param request: DescribeDBInstancesRequest
        @return: DescribeDBInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_dbinstances_with_options_async(request, runtime)

    def describe_endpoints_with_options(
        self,
        request: clickhouse_20230522_models.DescribeEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeEndpointsResponse:
        """
        @summary Queries the endpoint of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeEndpointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndpoints',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeEndpointsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_endpoints_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeEndpointsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeEndpointsResponse:
        """
        @summary Queries the endpoint of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeEndpointsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeEndpointsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndpoints',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeEndpointsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_endpoints(
        self,
        request: clickhouse_20230522_models.DescribeEndpointsRequest,
    ) -> clickhouse_20230522_models.DescribeEndpointsResponse:
        """
        @summary Queries the endpoint of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeEndpointsRequest
        @return: DescribeEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_endpoints_with_options(request, runtime)

    async def describe_endpoints_async(
        self,
        request: clickhouse_20230522_models.DescribeEndpointsRequest,
    ) -> clickhouse_20230522_models.DescribeEndpointsResponse:
        """
        @summary Queries the endpoint of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeEndpointsRequest
        @return: DescribeEndpointsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_endpoints_with_options_async(request, runtime)

    def describe_process_list_with_options(
        self,
        request: clickhouse_20230522_models.DescribeProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeProcessListResponse:
        """
        @summary Views running queries.
        
        @param request: DescribeProcessListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProcessListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_group_id):
            query['ComputingGroupId'] = request.computing_group_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.initial_query_id):
            query['InitialQueryId'] = request.initial_query_id
        if not UtilClient.is_unset(request.initial_user):
            query['InitialUser'] = request.initial_user
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.query_order):
            query['QueryOrder'] = request.query_order
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProcessList',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeProcessListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_process_list_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeProcessListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeProcessListResponse:
        """
        @summary Views running queries.
        
        @param request: DescribeProcessListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeProcessListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_group_id):
            query['ComputingGroupId'] = request.computing_group_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.initial_query_id):
            query['InitialQueryId'] = request.initial_query_id
        if not UtilClient.is_unset(request.initial_user):
            query['InitialUser'] = request.initial_user
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.query_order):
            query['QueryOrder'] = request.query_order
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeProcessList',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeProcessListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_process_list(
        self,
        request: clickhouse_20230522_models.DescribeProcessListRequest,
    ) -> clickhouse_20230522_models.DescribeProcessListResponse:
        """
        @summary Views running queries.
        
        @param request: DescribeProcessListRequest
        @return: DescribeProcessListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_process_list_with_options(request, runtime)

    async def describe_process_list_async(
        self,
        request: clickhouse_20230522_models.DescribeProcessListRequest,
    ) -> clickhouse_20230522_models.DescribeProcessListResponse:
        """
        @summary Views running queries.
        
        @param request: DescribeProcessListRequest
        @return: DescribeProcessListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_process_list_with_options_async(request, runtime)

    def describe_security_iplist_with_options(
        self,
        request: clickhouse_20230522_models.DescribeSecurityIPListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeSecurityIPListResponse:
        """
        @summary Queries the whitelist of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeSecurityIPListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityIPListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityIPList',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeSecurityIPListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_security_iplist_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeSecurityIPListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeSecurityIPListResponse:
        """
        @summary Queries the whitelist of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeSecurityIPListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSecurityIPListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSecurityIPList',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeSecurityIPListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_security_iplist(
        self,
        request: clickhouse_20230522_models.DescribeSecurityIPListRequest,
    ) -> clickhouse_20230522_models.DescribeSecurityIPListResponse:
        """
        @summary Queries the whitelist of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeSecurityIPListRequest
        @return: DescribeSecurityIPListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_security_iplist_with_options(request, runtime)

    async def describe_security_iplist_async(
        self,
        request: clickhouse_20230522_models.DescribeSecurityIPListRequest,
    ) -> clickhouse_20230522_models.DescribeSecurityIPListResponse:
        """
        @summary Queries the whitelist of an ApsaraDB for ClickHouse cluster.
        
        @param request: DescribeSecurityIPListRequest
        @return: DescribeSecurityIPListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_security_iplist_with_options_async(request, runtime)

    def describe_slow_log_records_with_options(
        self,
        request: clickhouse_20230522_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the details of slow query logs.
        
        @param request: DescribeSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_group_id):
            query['ComputingGroupId'] = request.computing_group_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeSlowLogRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_records_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeSlowLogRecordsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the details of slow query logs.
        
        @param request: DescribeSlowLogRecordsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogRecordsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_group_id):
            query['ComputingGroupId'] = request.computing_group_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogRecords',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeSlowLogRecordsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_records(
        self,
        request: clickhouse_20230522_models.DescribeSlowLogRecordsRequest,
    ) -> clickhouse_20230522_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the details of slow query logs.
        
        @param request: DescribeSlowLogRecordsRequest
        @return: DescribeSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_records_with_options(request, runtime)

    async def describe_slow_log_records_async(
        self,
        request: clickhouse_20230522_models.DescribeSlowLogRecordsRequest,
    ) -> clickhouse_20230522_models.DescribeSlowLogRecordsResponse:
        """
        @summary Queries the details of slow query logs.
        
        @param request: DescribeSlowLogRecordsRequest
        @return: DescribeSlowLogRecordsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_records_with_options_async(request, runtime)

    def describe_slow_log_trend_with_options(
        self,
        request: clickhouse_20230522_models.DescribeSlowLogTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeSlowLogTrendResponse:
        """
        @summary Queries the trend of slow query logs.
        
        @param request: DescribeSlowLogTrendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_group_id):
            query['ComputingGroupId'] = request.computing_group_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogTrend',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeSlowLogTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_slow_log_trend_with_options_async(
        self,
        request: clickhouse_20230522_models.DescribeSlowLogTrendRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.DescribeSlowLogTrendResponse:
        """
        @summary Queries the trend of slow query logs.
        
        @param request: DescribeSlowLogTrendRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeSlowLogTrendResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_group_id):
            query['ComputingGroupId'] = request.computing_group_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.query_duration_ms):
            query['QueryDurationMs'] = request.query_duration_ms
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlowLogTrend',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.DescribeSlowLogTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_slow_log_trend(
        self,
        request: clickhouse_20230522_models.DescribeSlowLogTrendRequest,
    ) -> clickhouse_20230522_models.DescribeSlowLogTrendResponse:
        """
        @summary Queries the trend of slow query logs.
        
        @param request: DescribeSlowLogTrendRequest
        @return: DescribeSlowLogTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_slow_log_trend_with_options(request, runtime)

    async def describe_slow_log_trend_async(
        self,
        request: clickhouse_20230522_models.DescribeSlowLogTrendRequest,
    ) -> clickhouse_20230522_models.DescribeSlowLogTrendResponse:
        """
        @summary Queries the trend of slow query logs.
        
        @param request: DescribeSlowLogTrendRequest
        @return: DescribeSlowLogTrendResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_slow_log_trend_with_options_async(request, runtime)

    def kill_process_with_options(
        self,
        request: clickhouse_20230522_models.KillProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.KillProcessResponse:
        """
        @summary Terminates an ongoing query.
        
        @param request: KillProcessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillProcessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_group_id):
            query['ComputingGroupId'] = request.computing_group_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.initial_query_id):
            query['InitialQueryId'] = request.initial_query_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KillProcess',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.KillProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def kill_process_with_options_async(
        self,
        request: clickhouse_20230522_models.KillProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.KillProcessResponse:
        """
        @summary Terminates an ongoing query.
        
        @param request: KillProcessRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: KillProcessResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_group_id):
            query['ComputingGroupId'] = request.computing_group_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.initial_query_id):
            query['InitialQueryId'] = request.initial_query_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='KillProcess',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.KillProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def kill_process(
        self,
        request: clickhouse_20230522_models.KillProcessRequest,
    ) -> clickhouse_20230522_models.KillProcessResponse:
        """
        @summary Terminates an ongoing query.
        
        @param request: KillProcessRequest
        @return: KillProcessResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.kill_process_with_options(request, runtime)

    async def kill_process_async(
        self,
        request: clickhouse_20230522_models.KillProcessRequest,
    ) -> clickhouse_20230522_models.KillProcessResponse:
        """
        @summary Terminates an ongoing query.
        
        @param request: KillProcessRequest
        @return: KillProcessResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.kill_process_with_options_async(request, runtime)

    def modify_account_authority_with_options(
        self,
        tmp_req: clickhouse_20230522_models.ModifyAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyAccountAuthorityResponse:
        """
        @summary Modifies the permissions of a database account.
        
        @param tmp_req: ModifyAccountAuthorityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountAuthorityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = clickhouse_20230522_models.ModifyAccountAuthorityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dml_auth_setting):
            request.dml_auth_setting_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dml_auth_setting, 'DmlAuthSetting', 'json')
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dml_auth_setting_shrink):
            query['DmlAuthSetting'] = request.dml_auth_setting_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountAuthority',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyAccountAuthorityResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_authority_with_options_async(
        self,
        tmp_req: clickhouse_20230522_models.ModifyAccountAuthorityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyAccountAuthorityResponse:
        """
        @summary Modifies the permissions of a database account.
        
        @param tmp_req: ModifyAccountAuthorityRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountAuthorityResponse
        """
        UtilClient.validate_model(tmp_req)
        request = clickhouse_20230522_models.ModifyAccountAuthorityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.dml_auth_setting):
            request.dml_auth_setting_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.dml_auth_setting, 'DmlAuthSetting', 'json')
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dml_auth_setting_shrink):
            query['DmlAuthSetting'] = request.dml_auth_setting_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountAuthority',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyAccountAuthorityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_authority(
        self,
        request: clickhouse_20230522_models.ModifyAccountAuthorityRequest,
    ) -> clickhouse_20230522_models.ModifyAccountAuthorityResponse:
        """
        @summary Modifies the permissions of a database account.
        
        @param request: ModifyAccountAuthorityRequest
        @return: ModifyAccountAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_authority_with_options(request, runtime)

    async def modify_account_authority_async(
        self,
        request: clickhouse_20230522_models.ModifyAccountAuthorityRequest,
    ) -> clickhouse_20230522_models.ModifyAccountAuthorityResponse:
        """
        @summary Modifies the permissions of a database account.
        
        @param request: ModifyAccountAuthorityRequest
        @return: ModifyAccountAuthorityResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_authority_with_options_async(request, runtime)

    def modify_account_description_with_options(
        self,
        request: clickhouse_20230522_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account.
        
        @param request: ModifyAccountDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyAccountDescriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_account_description_with_options_async(
        self,
        request: clickhouse_20230522_models.ModifyAccountDescriptionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account.
        
        @param request: ModifyAccountDescriptionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyAccountDescriptionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAccountDescription',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyAccountDescriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_account_description(
        self,
        request: clickhouse_20230522_models.ModifyAccountDescriptionRequest,
    ) -> clickhouse_20230522_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account.
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_account_description_with_options(request, runtime)

    async def modify_account_description_async(
        self,
        request: clickhouse_20230522_models.ModifyAccountDescriptionRequest,
    ) -> clickhouse_20230522_models.ModifyAccountDescriptionResponse:
        """
        @summary Modifies the description of a database account.
        
        @param request: ModifyAccountDescriptionRequest
        @return: ModifyAccountDescriptionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_account_description_with_options_async(request, runtime)

    def modify_backup_policy_with_options(
        self,
        request: clickhouse_20230522_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyBackupPolicyResponse:
        """
        @summary 修改备份策略
        
        @param request: ModifyBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyBackupPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_backup_policy_with_options_async(
        self,
        request: clickhouse_20230522_models.ModifyBackupPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyBackupPolicyResponse:
        """
        @summary 修改备份策略
        
        @param request: ModifyBackupPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyBackupPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backup_retention_period):
            query['BackupRetentionPeriod'] = request.backup_retention_period
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.preferred_backup_period):
            query['PreferredBackupPeriod'] = request.preferred_backup_period
        if not UtilClient.is_unset(request.preferred_backup_time):
            query['PreferredBackupTime'] = request.preferred_backup_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyBackupPolicy',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyBackupPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_backup_policy(
        self,
        request: clickhouse_20230522_models.ModifyBackupPolicyRequest,
    ) -> clickhouse_20230522_models.ModifyBackupPolicyResponse:
        """
        @summary 修改备份策略
        
        @param request: ModifyBackupPolicyRequest
        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_backup_policy_with_options(request, runtime)

    async def modify_backup_policy_async(
        self,
        request: clickhouse_20230522_models.ModifyBackupPolicyRequest,
    ) -> clickhouse_20230522_models.ModifyBackupPolicyResponse:
        """
        @summary 修改备份策略
        
        @param request: ModifyBackupPolicyRequest
        @return: ModifyBackupPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_backup_policy_with_options_async(request, runtime)

    def modify_dbinstance_attribute_with_options(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyDBInstanceAttributeResponse:
        """
        @summary Modifies the configurations of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attribute_type):
            query['AttributeType'] = request.attribute_type
        if not UtilClient.is_unset(request.attribute_value):
            query['AttributeValue'] = request.attribute_value
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceAttribute',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyDBInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_attribute_with_options_async(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyDBInstanceAttributeResponse:
        """
        @summary Modifies the configurations of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.attribute_type):
            query['AttributeType'] = request.attribute_type
        if not UtilClient.is_unset(request.attribute_value):
            query['AttributeValue'] = request.attribute_value
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceAttribute',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyDBInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_attribute(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceAttributeRequest,
    ) -> clickhouse_20230522_models.ModifyDBInstanceAttributeResponse:
        """
        @summary Modifies the configurations of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBInstanceAttributeRequest
        @return: ModifyDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_attribute_with_options(request, runtime)

    async def modify_dbinstance_attribute_async(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceAttributeRequest,
    ) -> clickhouse_20230522_models.ModifyDBInstanceAttributeResponse:
        """
        @summary Modifies the configurations of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBInstanceAttributeRequest
        @return: ModifyDBInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_attribute_with_options_async(request, runtime)

    def modify_dbinstance_class_with_options(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyDBInstanceClassResponse:
        """
        @summary Modifies the elastic scaling settings of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBInstanceClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_group_id):
            query['ComputingGroupId'] = request.computing_group_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_count):
            query['NodeCount'] = request.node_count
        if not UtilClient.is_unset(request.node_scale_max):
            query['NodeScaleMax'] = request.node_scale_max
        if not UtilClient.is_unset(request.node_scale_min):
            query['NodeScaleMin'] = request.node_scale_min
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not UtilClient.is_unset(request.scale_min):
            query['ScaleMin'] = request.scale_min
        if not UtilClient.is_unset(request.storage_quota):
            query['StorageQuota'] = request.storage_quota
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceClass',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyDBInstanceClassResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_class_with_options_async(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceClassRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyDBInstanceClassResponse:
        """
        @summary Modifies the elastic scaling settings of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBInstanceClassRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceClassResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_group_id):
            query['ComputingGroupId'] = request.computing_group_id
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.node_count):
            query['NodeCount'] = request.node_count
        if not UtilClient.is_unset(request.node_scale_max):
            query['NodeScaleMax'] = request.node_scale_max
        if not UtilClient.is_unset(request.node_scale_min):
            query['NodeScaleMin'] = request.node_scale_min
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scale_max):
            query['ScaleMax'] = request.scale_max
        if not UtilClient.is_unset(request.scale_min):
            query['ScaleMin'] = request.scale_min
        if not UtilClient.is_unset(request.storage_quota):
            query['StorageQuota'] = request.storage_quota
        if not UtilClient.is_unset(request.storage_type):
            query['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceClass',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyDBInstanceClassResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_class(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceClassRequest,
    ) -> clickhouse_20230522_models.ModifyDBInstanceClassResponse:
        """
        @summary Modifies the elastic scaling settings of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBInstanceClassRequest
        @return: ModifyDBInstanceClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_class_with_options(request, runtime)

    async def modify_dbinstance_class_async(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceClassRequest,
    ) -> clickhouse_20230522_models.ModifyDBInstanceClassResponse:
        """
        @summary Modifies the elastic scaling settings of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBInstanceClassRequest
        @return: ModifyDBInstanceClassResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_class_with_options_async(request, runtime)

    def modify_dbinstance_config_with_options(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyDBInstanceConfigResponse:
        """
        @summary 修改实例参数配置
        
        @param request: ModifyDBInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConfig',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyDBInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_config_with_options_async(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyDBInstanceConfigResponse:
        """
        @summary 修改实例参数配置
        
        @param request: ModifyDBInstanceConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConfig',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyDBInstanceConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_config(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceConfigRequest,
    ) -> clickhouse_20230522_models.ModifyDBInstanceConfigResponse:
        """
        @summary 修改实例参数配置
        
        @param request: ModifyDBInstanceConfigRequest
        @return: ModifyDBInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_config_with_options(request, runtime)

    async def modify_dbinstance_config_async(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceConfigRequest,
    ) -> clickhouse_20230522_models.ModifyDBInstanceConfigResponse:
        """
        @summary 修改实例参数配置
        
        @param request: ModifyDBInstanceConfigRequest
        @return: ModifyDBInstanceConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_config_with_options_async(request, runtime)

    def modify_dbinstance_connection_string_with_options(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary Modifies the endpoint of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceConnectionStringResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_group_id):
            query['ComputingGroupId'] = request.computing_group_id
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_net_type):
            query['DBInstanceNetType'] = request.dbinstance_net_type
        if not UtilClient.is_unset(request.disable_ports):
            query['DisablePorts'] = request.disable_ports
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyDBInstanceConnectionStringResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_dbinstance_connection_string_with_options_async(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceConnectionStringRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary Modifies the endpoint of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyDBInstanceConnectionStringResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.computing_group_id):
            query['ComputingGroupId'] = request.computing_group_id
        if not UtilClient.is_unset(request.connection_string):
            query['ConnectionString'] = request.connection_string
        if not UtilClient.is_unset(request.connection_string_prefix):
            query['ConnectionStringPrefix'] = request.connection_string_prefix
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbinstance_net_type):
            query['DBInstanceNetType'] = request.dbinstance_net_type
        if not UtilClient.is_unset(request.disable_ports):
            query['DisablePorts'] = request.disable_ports
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDBInstanceConnectionString',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifyDBInstanceConnectionStringResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_dbinstance_connection_string(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceConnectionStringRequest,
    ) -> clickhouse_20230522_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary Modifies the endpoint of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @return: ModifyDBInstanceConnectionStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_dbinstance_connection_string_with_options(request, runtime)

    async def modify_dbinstance_connection_string_async(
        self,
        request: clickhouse_20230522_models.ModifyDBInstanceConnectionStringRequest,
    ) -> clickhouse_20230522_models.ModifyDBInstanceConnectionStringResponse:
        """
        @summary Modifies the endpoint of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifyDBInstanceConnectionStringRequest
        @return: ModifyDBInstanceConnectionStringResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_dbinstance_connection_string_with_options_async(request, runtime)

    def modify_security_iplist_with_options(
        self,
        request: clickhouse_20230522_models.ModifySecurityIPListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifySecurityIPListResponse:
        """
        @summary Modifies the whitelist settings of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifySecurityIPListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityIPListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIPList',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifySecurityIPListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_security_iplist_with_options_async(
        self,
        request: clickhouse_20230522_models.ModifySecurityIPListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ModifySecurityIPListResponse:
        """
        @summary Modifies the whitelist settings of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifySecurityIPListRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifySecurityIPListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.modify_mode):
            query['ModifyMode'] = request.modify_mode
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_iplist):
            query['SecurityIPList'] = request.security_iplist
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySecurityIPList',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ModifySecurityIPListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_security_iplist(
        self,
        request: clickhouse_20230522_models.ModifySecurityIPListRequest,
    ) -> clickhouse_20230522_models.ModifySecurityIPListResponse:
        """
        @summary Modifies the whitelist settings of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifySecurityIPListRequest
        @return: ModifySecurityIPListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_security_iplist_with_options(request, runtime)

    async def modify_security_iplist_async(
        self,
        request: clickhouse_20230522_models.ModifySecurityIPListRequest,
    ) -> clickhouse_20230522_models.ModifySecurityIPListResponse:
        """
        @summary Modifies the whitelist settings of an ApsaraDB for ClickHouse cluster.
        
        @param request: ModifySecurityIPListRequest
        @return: ModifySecurityIPListResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_security_iplist_with_options_async(request, runtime)

    def reset_account_password_with_options(
        self,
        request: clickhouse_20230522_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of a database account for an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: ResetAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    async def reset_account_password_with_options_async(
        self,
        request: clickhouse_20230522_models.ResetAccountPasswordRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of a database account for an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: ResetAccountPasswordRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ResetAccountPasswordResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.ResetAccountPasswordResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reset_account_password(
        self,
        request: clickhouse_20230522_models.ResetAccountPasswordRequest,
    ) -> clickhouse_20230522_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of a database account for an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    async def reset_account_password_async(
        self,
        request: clickhouse_20230522_models.ResetAccountPasswordRequest,
    ) -> clickhouse_20230522_models.ResetAccountPasswordResponse:
        """
        @summary Resets the password of a database account for an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: ResetAccountPasswordRequest
        @return: ResetAccountPasswordResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reset_account_password_with_options_async(request, runtime)

    def restart_dbinstance_with_options(
        self,
        request: clickhouse_20230522_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.RestartDBInstanceResponse:
        """
        @summary Restarts an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: RestartDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.RestartDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_dbinstance_with_options_async(
        self,
        request: clickhouse_20230522_models.RestartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.RestartDBInstanceResponse:
        """
        @summary Restarts an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: RestartDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.RestartDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_dbinstance(
        self,
        request: clickhouse_20230522_models.RestartDBInstanceRequest,
    ) -> clickhouse_20230522_models.RestartDBInstanceResponse:
        """
        @summary Restarts an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: RestartDBInstanceRequest
        @return: RestartDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_dbinstance_with_options(request, runtime)

    async def restart_dbinstance_async(
        self,
        request: clickhouse_20230522_models.RestartDBInstanceRequest,
    ) -> clickhouse_20230522_models.RestartDBInstanceResponse:
        """
        @summary Restarts an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: RestartDBInstanceRequest
        @return: RestartDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_dbinstance_with_options_async(request, runtime)

    def start_dbinstance_with_options(
        self,
        request: clickhouse_20230522_models.StartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.StartDBInstanceResponse:
        """
        @summary Starts an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: StartDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.StartDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_dbinstance_with_options_async(
        self,
        request: clickhouse_20230522_models.StartDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.StartDBInstanceResponse:
        """
        @summary Starts an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: StartDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.StartDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_dbinstance(
        self,
        request: clickhouse_20230522_models.StartDBInstanceRequest,
    ) -> clickhouse_20230522_models.StartDBInstanceResponse:
        """
        @summary Starts an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: StartDBInstanceRequest
        @return: StartDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_dbinstance_with_options(request, runtime)

    async def start_dbinstance_async(
        self,
        request: clickhouse_20230522_models.StartDBInstanceRequest,
    ) -> clickhouse_20230522_models.StartDBInstanceResponse:
        """
        @summary Starts an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: StartDBInstanceRequest
        @return: StartDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_dbinstance_with_options_async(request, runtime)

    def stop_dbinstance_with_options(
        self,
        request: clickhouse_20230522_models.StopDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.StopDBInstanceResponse:
        """
        @summary Stops an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: StopDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.StopDBInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_dbinstance_with_options_async(
        self,
        request: clickhouse_20230522_models.StopDBInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.StopDBInstanceResponse:
        """
        @summary Stops an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: StopDBInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopDBInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDBInstance',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.StopDBInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_dbinstance(
        self,
        request: clickhouse_20230522_models.StopDBInstanceRequest,
    ) -> clickhouse_20230522_models.StopDBInstanceResponse:
        """
        @summary Stops an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: StopDBInstanceRequest
        @return: StopDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_dbinstance_with_options(request, runtime)

    async def stop_dbinstance_async(
        self,
        request: clickhouse_20230522_models.StopDBInstanceRequest,
    ) -> clickhouse_20230522_models.StopDBInstanceResponse:
        """
        @summary Stops an ApsaraDB for ClickHouse Enterprise Edition cluster.
        
        @param request: StopDBInstanceRequest
        @return: StopDBInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_dbinstance_with_options_async(request, runtime)

    def upgrade_minor_version_with_options(
        self,
        request: clickhouse_20230522_models.UpgradeMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.UpgradeMinorVersionResponse:
        """
        @summary Updates the minor engine version of an ApsaraDB for ClickHouse cluster that runs Enterprise Edition.
        
        @param request: UpgradeMinorVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeMinorVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        if not UtilClient.is_unset(request.target_minor_version):
            query['TargetMinorVersion'] = request.target_minor_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMinorVersion',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.UpgradeMinorVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_minor_version_with_options_async(
        self,
        request: clickhouse_20230522_models.UpgradeMinorVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> clickhouse_20230522_models.UpgradeMinorVersionResponse:
        """
        @summary Updates the minor engine version of an ApsaraDB for ClickHouse cluster that runs Enterprise Edition.
        
        @param request: UpgradeMinorVersionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeMinorVersionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            query['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.switch_time):
            query['SwitchTime'] = request.switch_time
        if not UtilClient.is_unset(request.switch_time_mode):
            query['SwitchTimeMode'] = request.switch_time_mode
        if not UtilClient.is_unset(request.target_minor_version):
            query['TargetMinorVersion'] = request.target_minor_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeMinorVersion',
            version='2023-05-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            clickhouse_20230522_models.UpgradeMinorVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_minor_version(
        self,
        request: clickhouse_20230522_models.UpgradeMinorVersionRequest,
    ) -> clickhouse_20230522_models.UpgradeMinorVersionResponse:
        """
        @summary Updates the minor engine version of an ApsaraDB for ClickHouse cluster that runs Enterprise Edition.
        
        @param request: UpgradeMinorVersionRequest
        @return: UpgradeMinorVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_minor_version_with_options(request, runtime)

    async def upgrade_minor_version_async(
        self,
        request: clickhouse_20230522_models.UpgradeMinorVersionRequest,
    ) -> clickhouse_20230522_models.UpgradeMinorVersionResponse:
        """
        @summary Updates the minor engine version of an ApsaraDB for ClickHouse cluster that runs Enterprise Edition.
        
        @param request: UpgradeMinorVersionRequest
        @return: UpgradeMinorVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_minor_version_with_options_async(request, runtime)
